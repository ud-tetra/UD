"""Independent exact checks; does not execute any partner-supplied code."""
from pathlib import Path
from itertools import combinations
import json, hashlib
import sympy as s

root=Path(__file__).resolve().parent
def carrier(cells):
    simplices=sorted({f for c in cells for n in range(1,5) for f in combinations(sorted(c),n)},key=lambda f:(len(f),f))
    ix={f:i for i,f in enumerate(simplices)}
    d=s.zeros(len(ix))
    for f,j in ix.items():
        if len(f)>1:
            for k in range(len(f)):d[ix[f[:k]+f[k+1:]],j]=(-1)**k
    assert d*d==s.zeros(d.rows)
    return simplices,d,d.T-d

ca,da,A=carrier([(0,1,2,3),(0,1,2,4)])
cb,db,B=carrier([(0,1,2,3),(0,1,2,4),(0,1,3,4)])
T=s.zeros(len(cb),len(ca))
for j,f in enumerate(ca):T[cb.index(f),j]=1
assert db*T==T*da and T.T*T==s.eye(23)
R=B*T-T*A; LA=-A*A; LB=-B*B
P0=(LA-3*s.eye(23))*(LA-5*s.eye(23))/15
P3=LA*(5*s.eye(23)-LA)/6
P5=LA*(LA-3*s.eye(23))/10
assert P0+P3+P5==s.eye(23)
assert R.rank()==4 and R*R.T*R==2*R
O=R.col_join(R*A) # A powers close by the known minimal polynomial.
assert O.rank()==8 and R*(P0+P5)==s.zeros(27,23)
assert R*A*(P0+P5)==s.zeros(27,23) and (P0+P5).rank()==15
assert A*(P0+P5)==(P0+P5)*A
PB2=LB*(5*s.eye(27)-LB)/6
W=P3*T.T*PB2*T*P3
assert W*W==s.Rational(2,3)*W and W.rank()==4
assert P3.rank()==8

# Stellar subdivision and a non-diagonal positive metric counterexample.
cc,dc,Ac=carrier([(0,1,2,3)])
cf,df,Af=carrier([(0,1,2,4),(0,1,3,4),(0,2,3,4),(1,2,3,4)])
S=s.zeros(29,15)
for j,f in enumerate(cc):
    if len(f)<4:S[cf.index(f),j]=1
for f,sign in [((0,1,2,4),1),((0,1,3,4),-1),((0,2,3,4),1),((1,2,3,4),-1)]:S[cf.index(f),14]=sign
assert df*S==S*dc and S.T*S==s.diag(*([1]*14+[4]))
Pi=s.zeros(15,29)
for j,f in enumerate(cf):
    mapped=tuple(0 if v==4 else v for v in f)
    if len(set(mapped))==len(mapped):
        sign=(-1)**sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))
        Pi[cc.index(tuple(sorted(mapped))),j]=sign
assert Pi*S==s.eye(15) and dc*Pi==Pi*df
N=s.eye(29)-S*Pi
H=Pi.T*Pi+N.T*N
assert S.T*H*S==s.eye(15)
# Positive definiteness is independently certified by exact LDL, in addition to the sum-of-squares proof.
_,D=H.LDLdecomposition()
assert all(D[i,i]>0 for i in range(29))
AH=H.inv()*df.T*H-df
assert AH*S==S*Ac and AH.T*H+H*AH==s.zeros(29)
assert H!=s.diag(*H.diagonal())

# Explicit two-state Kraus channel, consistent with the late source Bloch formula.
K0=s.diag(1/s.sqrt(2),1/s.sqrt(3))
K1=s.Matrix([[0,s.sqrt(s.Rational(2,3))],[1/s.sqrt(2),0]])
def E(rho):return s.simplify(K0*rho*K0.T+K1*rho*K1.T)
assert s.simplify(K0.T*K0+K1.T*K1)==s.eye(2)
sx=s.Matrix([[0,1],[1,0]]); sy=s.Matrix([[0,-s.I],[s.I,0]]); sz=s.diag(1,-1)
eta=(1+s.sqrt(2))/s.sqrt(6)
assert s.simplify(E(sx)-eta*sx)==s.zeros(2)
assert s.simplify(E(sy)-(1-s.sqrt(2))/s.sqrt(6)*sy)==s.zeros(2)
assert E(sz)==-sz/6 and E(s.eye(2))==s.eye(2)+sz/6
rho=s.diag(s.Rational(4,7),s.Rational(3,7)); assert E(rho)==rho
assert eta>s.Rational(5,7) and eta<1

alpha=s.symbols('alpha',nonnegative=True)
M=s.Matrix([[s.Rational(1,2),2*alpha/3,0],[s.Rational(1,2),s.Rational(1,3),s.Rational(6,7)],[0,2*(1-alpha)/3,s.Rational(1,7)]])
p=s.Matrix([12*alpha,9,7*(1-alpha)])/(16+5*alpha)
assert s.simplify(M*p-p)==s.zeros(3,1)
assert s.simplify(sum(p)-1)==0
assert p.subs(alpha,s.Rational(7,9))==s.Matrix([84,81,14])/179

z=s.symbols('z')
ring_results={}
for n in (4,5):
    cells=[tuple(sorted((i,(i+1)%n,n,n+1))) for i in range(n)]
    fs,_,Ar=carrier(cells)
    expected=z*(z*z+2)**2*(z*z+6)**7*(z*z+4)**8 if n==4 else z*(z*z+2)**2*(z*z+7)**3*(z**4+9*z*z+19)**8
    cp=s.factor(Ar.charpoly(z).as_expr())
    assert s.expand(cp-expected)==0
    ring_results[str(n)]={'f_vector':[sum(len(f)==k for f in fs) for k in range(1,5)],'characteristic_polynomial':str(cp)}
# Four tetrahedra can form a face-sharing cycle without a common edge when
# the hypothesis does not exclude additional face adjacencies.
cycle=[set((0,1,2,4)),set((0,1,3,4)),set((0,2,3,4)),set((1,2,3,4))]
assert all(len(cycle[i]&cycle[(i+1)%4])==3 for i in range(4))
assert set.intersection(*cycle)=={4}
checks={
 'status':'PASS','physical_promotion':0,'independent_review':False,
 'native_inclusion':{'dims':[23,27],'residual_rank':4,'nonzero_singular_values':['sqrt(2)']*4,'observable_rank':8,'protected_dimension':15,'compressed_sector_weights':['0 (multiplicity 4)','2/3 (multiplicity 4)'],'A_charpoly':str(s.factor(A.charpoly(z).as_expr())),'B_charpoly':str(s.factor(B.charpoly(z).as_expr()))},
 'stellar':{'dims':[15,29],'unit_top_norm_squared':4,'chain_map':True,'positive_metric_intertwines':True,'metric_is_diagonal':False,'metric_ldl_pivots':[str(D[i,i]) for i in range(29)]},
 'kraus':{'stationary':['4/7','3/7'],'bloch_linear':[str(eta),str((1-s.sqrt(2))/s.sqrt(6)),'-1/6'],'bloch_shift':['0','0','1/6'],'trace_distance_contraction':str(eta),'contraction_numeric':float(eta),'claimed_5_over_7_bound':'FALSE without a separately defined additional map','three_state_stationary':[str(v) for v in p]},
 'bipyramid_spectra':ring_results,
 'unqualified_four_cycle_spine_claim':'FALSE: four faces of the 4-simplex have only one common vertex; extra face adjacencies must be excluded for an induced-cycle hypothesis.',
 'proof_scope':'Exact finite matrix identities and symbolic channel equations. Approximate recurrence uses the manuscript pigeonhole proof. No provenance or dynamics for imported geometric, bath, scattering or Berry-phase interpretations is inferred.'}
(root/'PARTNER_CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n')
(root/'STELLAR_METRIC_CERTIFICATE.json').write_text(json.dumps({'simplices_coarse':cc,'simplices_fine':cf,'S':S.tolist(),'Pi':Pi.tolist(),'H':H.tolist(),'weighted_generator':AH.tolist()},default=str,indent=2)+'\n')
print(json.dumps(checks,indent=2))
