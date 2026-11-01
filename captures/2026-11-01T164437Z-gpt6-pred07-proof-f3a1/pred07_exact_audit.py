#!/usr/bin/env python3
"""UD PRED07 exact conditional theorem/counterexample audit.
Not a native constitutive law, physical experiment, or independent reviewer.
Python 3 + SymPy 1.14.
"""
import json
from itertools import combinations, permutations
from pathlib import Path
import sympy as S


def audit():
    b = S.symbols('b0:4', real=True)
    M = sum(b)
    Q = sum(z*z for z in b)
    gamma = S.symbols('gamma', positive=True, real=True)
    edges=list(combinations(range(4),2))
    B=S.zeros(4,len(edges))
    for i,(v,w) in enumerate(edges): B[v,i]=-1;B[w,i]=1
    L=B*B.T
    J=S.ones(4,4)
    assert L==4*S.eye(4)-J
    x=S.Matrix(b)
    s=S.Matrix([gamma*z*(z-Q/M) for z in b])
    F= -L*x/4+s
    assert S.factor(sum(s))==0
    assert S.factor(sum(F))==0
    # On connected K4 each zero-sum source equals divergence of a local edge current.
    js=(B.T*s)/4
    assert (B*js-s).applyfunc(S.simplify)==S.zeros(4,1)
    diff={}
    for i,j in combinations(range(4),2):
        factor=-1+gamma*(b[i]+b[j]-Q/M)
        assert S.simplify(F[i]-F[j]-(b[i]-b[j])*factor)==0
        diff[f'{i}{j}']=str(S.factor(factor))
    # Exact linearization on the mass-conserving 3D subspace at uniform burden.
    m=S.symbols('m',positive=True)
    jac=F.jacobian(x).subs({b[i]:m/4 for i in range(4)},simultaneous=True)
    # On vectors of zero sum: F'(u) v =(-1+gamma*m/4)*v.
    v=S.Matrix([1,-1,0,0])
    assert (jac*v-(-1+gamma*m/4)*v).applyfunc(S.simplify)==S.zeros(4,1)
    # Symmetric 1-high, 3-low branch reduces to scalar delta dynamics.
    delta=S.symbols('delta',real=True)
    special={b[0]:(m+3*delta)/4,b[1]:(m-delta)/4,b[2]:(m-delta)/4,b[3]:(m-delta)/4}
    reduced=S.factor((F[0]-F[1]).subs(special,simultaneous=True))
    claimed=S.factor(delta*(-1+gamma*(m/4+delta/2-3*delta**2/(4*m))))
    assert S.simplify(reduced-claimed)==0
    growth=S.factor(claimed.subs({m:4,gamma:2})/delta)
    assert S.simplify(growth-(1+delta-3*delta**2/8))==0
    ds=(4+2*S.sqrt(10))/3
    assert S.simplify(growth.subs(delta,ds))==0
    assert 0<float(ds)<4
    # 24 exact S4 equivariance tests on rational generic input with strict ordering.
    sample=S.Matrix([S.Rational(13,10),S.Rational(11,10),S.Rational(9,10),S.Rational(7,10)])
    assert sum(sample)==4
    def evalF(values):
        sm=sum(values);sq=sum(z*z for z in values)
        return S.Matrix([-((4*z-sm)/4)+2*z*(z-sq/sm) for z in values])
    for perm in permutations(range(4)):
        p=S.Matrix([sample[i] for i in perm])
        assert evalF(p)==S.Matrix([evalF(sample)[i] for i in perm])
    # K4 oriented-edge representation projectors; two independent metric sectors.
    Pg=(B.T*B)/4
    Pc=S.eye(6)-Pg
    assert Pg**2==Pg and Pc**2==Pc and Pg*Pc==S.zeros(6,6)
    assert Pg.T==Pg and Pc.T==Pc
    assert S.trace(Pg)==3 and S.trace(Pc)==3
    g,c=S.symbols('g c',positive=True)
    G=g*Pg+c*Pc
    assert S.trace(G)==3*(g+c)
    G0=G.subs({g:1,c:1})
    G1=G.subs({g:S.Rational(1,2),c:S.Rational(3,2)})
    assert all(G0[i,i]==G1[i,i]==1 for i in range(6))
    assert G0!=G1 and G0[0,1]!=G1[0,1]
    # Symmetry covariance of G under signed edge permutation.
    for perm in permutations(range(4)):
        P=S.zeros(6,6)
        for e,(v,w) in enumerate(edges):
            v1,w1=perm[v],perm[w]
            f=edges.index(tuple(sorted((v1,w1))))
            P[f,e]=1 if v1<w1 else -1
        assert P.T*G1*P==G1
    # Rank-one cycle example: derivative-only action does not see period.
    Bt=S.Matrix([[-1,0,1],[1,-1,0],[0,1,-1]])
    h=S.Matrix([S.Rational(1,3)]*3)
    assert Bt*h==S.zeros(3,1)
    assert S.factor(sum(h))==1
    assert (h.T*h)[0]==S.Rational(1,3)
    tau=S.symbols('tau',positive=True)
    period=lambda a:sum(a)
    S2=tau*period(2*h)**2/2;S3=tau*period(3*h)**2/2
    assert S.simplify(S3-S2-S.Rational(5,2)*tau)==0
    # Gauge invariance: any exact shift Bt.T phi integrates to zero.
    phi=S.Matrix(S.symbols('phi0:3'))
    assert S.simplify(period(h+Bt.T*phi)-period(h))==0
    return {
        'source_q162_conservative_mixing':'-L b/4',
        'new_source':'s_i=gamma b_i(b_i-Q/M), Q=sum_j b_j^2, M=sum_j b_j>0',
        'exact_mass_conservation':True,
        'source_is_an_internal_conservative_flux':'s=B*(B.T*s)/4; no external stock injection proved',
        'positive_simplex_invariance_proved_analytically':True,
        'uniform_linear_transverse_eigenvalue':'gamma*M/4-1',
        'instability_threshold':'gamma*M>4',
        'difference_sign_preserved':True,
        'symmetric_branch_delta_prime':str(claimed),
        'M4_gamma2_delta_star':str(ds),
        'M4_gamma2_delta_star_decimal':float(ds.evalf(13)),
        'S4_exact_permutation_cases':24,
        'K4_grad_projector_rank':S.trace(Pg),
        'K4_cycle_projector_rank':S.trace(Pc),
        'K4_metric_identifiability':'G=g Pgrad+c Pcycle; fixed trace and unit edge diagonal leave g+c=2',
        'explicit_metric_correlation_G1_edge01_edge02':str(G1[0,1]),
        'sector_action':'S_top(a)=tau*period_gamma(a)^2/2',
        'sector_gap_2_to_3':str(S.simplify(S3-S2)),
        'physical_promotion':0,
        'review_status':'DEFERRED',
        'label':'EXACT_CONDITIONAL_AND_CANDIDATE_SOURCE'
    }

if __name__=='__main__':
    out=audit()
    path=Path(__file__).resolve().parent/'EXACT_AUDIT.json'
    path.write_text(json.dumps(out,indent=2,default=str)+'\n')
    print(json.dumps(out,indent=2,default=str))
