"""Independent exact spectral-distance audit. No archived code is executed.

The optimized quantity is a necessary spectral lower bound, not the optimized
operator residual or a lower bound on endpoint error. All scale variation is
comparison only; it selects no native parameter or physical clock.
"""
import itertools
import json
from pathlib import Path
import numpy as np
import sympy as S
from scipy.linalg import expm

P = (2, 4, 6, 8, 10)

def sign(v):
    v = S.simplify(v)
    if v == 0 or v.is_zero is True:
        return 0
    if v.is_positive is True:
        return 1
    if v.is_negative is True:
        return -1
    raise AssertionError(f'Uncertified algebraic sign: {v}')

def exact_max(values):
    out = values[0]
    for v in values[1:]:
        if sign(v-out) > 0:
            out = v
    return S.simplify(out)

def lp_for_assignment(assignment, ratio):
    slopes = [S.Integer(0), S.Integer(1), ratio]
    lines = [(S.Integer(e*p), -e*slopes[a])
             for p,a in zip(P,assignment) for e in (-1,1)]
    candidates = [S.Integer(0)]
    for (c,a),(d,b) in itertools.combinations(lines,2):
        if sign(a-b) != 0:
            y = S.simplify((d-c)/(a-b))
            if sign(y) >= 0:
                candidates.append(y)
    # Floating ordering proposes the candidate only. The exact active slopes
    # below supply its global convex-program certificate independently.
    y = min(candidates,key=lambda z:max(float(c+a*z) for c,a in lines))
    epsilon = exact_max([c+a*y for c,a in lines])
    active = [(c,a) for c,a in lines if sign(c+a*y-epsilon) == 0]
    active_signs = [sign(a) for c,a in active]
    if sign(y) > 0:
        assert min(active_signs) <= 0 <= max(active_signs)
    else:
        assert max(active_signs) >= 0
    assert all(sign(epsilon-(c+a*y)) >= 0 for c,a in lines)
    return y,epsilon,active

def optimize(name,a,b):
    ratio = S.simplify(b/a)
    rows = []
    for i in range(6):
        for j in range(6-i):
            assignment = (0,)*i+(1,)*j+(2,)*(5-i-j)
            y,eps,active = lp_for_assignment(assignment,ratio)
            rows.append({'assignment':assignment,'x':S.simplify(y/a),
                         'epsilon':eps,'active_lines':active})
    best = rows[0]['epsilon']
    for row in rows[1:]:
        if sign(row['epsilon']-best) < 0:
            best = row['epsilon']
    assert all(sign(row['epsilon']-best) >= 0 for row in rows)
    exact_rows = [{k:([str(v) for v in val] if k=='assignment' else
                     [[str(c),str(s)] for c,s in val] if k=='active_lines' else str(val))
                   for k,val in row.items()} for row in rows]
    # Exhaustively allow nonmonotone assignments as an independent numerical
    # control; nearest ordered centres always admit a monotone assignment.
    numeric_best = float('inf')
    for ass in itertools.product((0,1,2),repeat=5):
        lines = [(e*p,-e*float([0,1,ratio][q])) for p,q in zip(P,ass) for e in (-1,1)]
        ys = [0.0]+[(d-c)/(u-v) for (c,u),(d,v) in itertools.combinations(lines,2)
                    if abs(u-v)>1e-12 and (d-c)/(u-v)>=0]
        numeric_best = min(numeric_best,min(max(c+u*y for c,u in lines) for y in ys))
    assert abs(numeric_best-float(best)) < 1e-10
    return {'name':name,'positive_native_frequencies':[str(a),str(b)],
            'exact_minimum':str(best),'numeric_minimum_diagnostic':float(best),
            'monotone_assignment_count':len(rows),'arbitrary_assignment_count':243,
            'global_exact_certificates':exact_rows,
            'optimal_certificate_rows':[r for r in exact_rows if sign(S.sympify(r['epsilon'])-best)==0]}

def simplex_generator(cells):
    chains = [sorted({s for cell in cells for s in itertools.combinations(cell,k+1)}) for k in range(4)]
    offsets = np.cumsum([0]+[len(c) for c in chains]).tolist()
    A = S.zeros(offsets[-1]);boundaries=[]
    for k in range(1,4):
        B = S.zeros(len(chains[k-1]),len(chains[k]))
        index = {s:j for j,s in enumerate(chains[k-1])}
        for col,s in enumerate(chains[k]):
            for j in range(k+1):
                B[index[s[:j]+s[j+1:]],col]=(-1)**j
        boundaries.append(B)
        A[offsets[k-1]:offsets[k],offsets[k]:offsets[k+1]]=B
        A[offsets[k]:offsets[k+1],offsets[k-1]:offsets[k]]=-B.T
    assert A.T == -A
    assert boundaries[0]*boundaries[1] == S.zeros(len(chains[0]),len(chains[2]))
    assert boundaries[1]*boundaries[2] == S.zeros(len(chains[1]),len(chains[3]))
    return A,[len(c) for c in chains]

def native_spectra():
    cases = [('DELTA3',[(0,1,2,3)]),
             ('K_MINUS',[(0,1,2,3),(0,1,2,4)]),
             ('K_PLUS',[(0,1,3,4),(0,2,3,4),(1,2,3,4)])]
    expected = {'DELTA3':{0:1,4:14},'K_MINUS':{0:1,3:8,5:14},'K_PLUS':{0:1,2:4,5:22}}
    rows=[];operators={}
    for name,cells in cases:
        A,f=simplex_generator(cells)
        square=-A*A
        actual=square.eigenvals()
        assert actual == expected[name],(name,actual)
        operators[name]=1j*np.asarray(A.tolist(),dtype=float)
        rows.append({'complex':name,'f_vector':f,'chain_dimension':sum(f),
                     'skew_characteristic_polynomial':str(S.factor(A.charpoly().as_expr())),
                     'H_squared_eigenvalues_with_multiplicity':{str(k):v for k,v in actual.items()},
                     'verification':'Exact generated boundaries, boundary composition, skewness and H-squared spectrum.'})
    return rows,operators

def residual_controls(operators):
    rng=np.random.default_rng(140626)
    n=10;Hp=np.zeros((11,11))
    for j in range(n):Hp[j,j+1]=Hp[j+1,j]=np.sqrt((j+1)*(n-j))
    assert np.allclose(np.linalg.eigvalsh(Hp),np.arange(-10,11,2))
    xvalues={'DELTA3':3.5,'K_MINUS':float(7*(S.sqrt(5)-S.sqrt(3))),
             'K_PLUS':float(3*S.sqrt(2))}
    floors={'DELTA3':3.,'K_MINUS':float(7*S.sqrt(15)-25),'K_PLUS':2.}
    rows=[]
    for name,H in operators.items():
        raw=rng.normal(size=(H.shape[0],11))+1j*rng.normal(size=(H.shape[0],11))
        E=np.linalg.qr(raw)[0]
        assert np.linalg.norm(E.conj().T@E-np.eye(11),2)<1e-12
        eta=np.linalg.norm(xvalues[name]*H@E-E@Hp,2)
        assert eta+1e-10>=floors[name]
        rows.append({'complex':name,'comparison_x':xvalues[name],
                     'dense_isometry_residual_numeric':float(eta),'necessary_spectral_floor':floors[name],
                     'scope':'Floating sanity control, not a source-defined encoding, optimizer or physical receipt.'})
    # Endpoint aliasing: a nonzero generator mismatch can produce identical
    # propagators. Therefore the residual floor gives no endpoint-error floor.
    T=np.pi/2
    H0=np.diag([0.,2.]);H1=H0+4*np.eye(2)
    mismatch=np.linalg.norm(H1-H0,2)
    endpoint=np.linalg.norm(expm(-1j*T*H1)-expm(-1j*T*H0),2)
    assert mismatch==4 and endpoint<1e-12
    # Simultaneously slowing both matched comparison generators scales eta
    # and inversely scales T; the dimensionless Duhamel product is unchanged.
    scales=[1.,0.1,0.01]
    budgets=[(np.pi/(2*k))*(k*3) for k in scales]
    assert max(budgets)-min(budgets)<1e-12
    return {'dense_residual_controls':rows,
            'endpoint_alias_control':{'generator_residual':mismatch,'endpoint_operator_difference':float(endpoint),
                                     'T':'pi/2','inference':'Residual lower bound does not imply actual endpoint error lower bound.'},
            'joint_slowing_control':{'kappa_values':scales,'dimensionless_products':budgets,
                                    'inference':'Common scaling does not shrink T eta.'}}

def main():
    exact=[optimize('DELTA3',S.Integer(2),S.Integer(2)),
           optimize('K_MINUS',S.sqrt(3),S.sqrt(5)),
           optimize('K_PLUS',S.sqrt(2),S.sqrt(5))]
    spectra,operators=native_spectra()
    assert S.simplify(S.sympify(exact[0]['exact_minimum'])-3)==0
    assert S.simplify(S.sympify(exact[1]['exact_minimum'])-(7*S.sqrt(15)-25))==0
    assert S.simplify(S.sympify(exact[2]['exact_minimum'])-2)==0
    result={'version':'0.1','status':'PASS','clock_word_length':10,
            'target_positive_frequencies':list(P),'exact_optimizers':exact,
            'optimized_scale_dispositions':{'DELTA3':'x=7/2','K_MINUS':'x=7*(sqrt(5)-sqrt(3))',
                                           'K_PLUS':'8/sqrt(5) <= x <= 3*sqrt(2)'},
            'generated_native_spectra':spectra,'negative_and_sanity_controls':residual_controls(operators),
            'necessary_inequality':'eta >= kappa*b(x); T*eta >= pi*b(x)/2 for T=pi/(2*kappa)',
            'exact_solver_certificate':'For each monotone assignment, the maximum of signed affine lines is convex. Every proposed optimizer has exact active slopes straddling zero (or valid one-sided boundary slope); all 21 branch minima are exactly compared. All 243 arbitrary assignments agree numerically.',
            'scope_limits':['Nearest-spectrum bound ignores orthogonality and frequency multiplicity; it need not be attainable by any isometry.',
                            'Comparison scale optimization does not choose any native metric, coupling or physical time.',
                            'Dense isometries are generated mathematical controls, not native-source encodings.',
                            'A large Duhamel upper-bound budget cannot certify a small error, but is not a proof of actual large endpoint error.'],
            'physical_promotion':0,'independent_human_review':'PENDING'}
    out=Path(__file__).with_name('native-spectral-parallel-results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','output':str(out),'branch_certificates':63,
                      'arbitrary_assignments':729,'exact_minima':[r['exact_minimum'] for r in exact]}))

if __name__=='__main__':main()
