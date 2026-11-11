"""Current constructor checks: finite local ports and a declared occupancy lift."""
import json, math
from pathlib import Path
from fractions import Fraction as F
import numpy as np
import scipy.sparse as sp
from scipy.integrate import quad, solve_ivp

ROOT=Path(__file__).resolve().parent
checks=[]
def check(name, ok, kind='EXACT'):
    assert bool(ok), name
    checks.append(dict(name=name,status='PASS',kind=kind))
def rank(a):
    a=[[F(x) for x in row] for row in a];r=0
    for j in range(len(a[0])):
        pivot=next((k for k in range(r,len(a)) if a[k][j]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r];v=a[r][j];a[r]=[x/v for x in a[r]]
        for k in range(r+1,len(a)):
            v=a[k][j]
            if v:a[k]=[x-v*y for x,y in zip(a[k],a[r])]
        r+=1
        if r==len(a): break
    return r
data=json.loads((ROOT/'COMPLEX_AND_ACTION.json').read_text())
C=[[tuple(t) for t in cs] for cs in data['simplices']]
ids=[{s:i for i,s in enumerate(cs)} for cs in C];B=[]
for d in [1,2]:
    rr=[];cc=[];vv=[]
    for j,s in enumerate(C[d]):
        for k in range(d+1):rr.append(ids[d-1][s[:k]+s[k+1:]]);cc.append(j);vv.append((-1)**k)
    B.append(sp.csc_matrix((vv,(rr,cc)),shape=(len(C[d-1]),len(C[d])),dtype=np.int64))
B1,B2=B;check('boundary_nilpotence',(B1@B2).nnz==0)
u=119;star=[j for j,e in enumerate(C[1]) if u in e];signs=[-int(B1[u,j]) for j in star]
check('degree_12',len(star)==12)
T=np.zeros((720,12),dtype=np.int64)
for k,(j,s) in enumerate(zip(star,signs)):T[j,k]=s
Ktri=(B2.T@T).toarray() if sp.issparse(B2.T@T) else B2.T@T
check('local_cycle_constraint_rank_11',rank(Ktri)==11)
check('balanced_star_exact',np.array_equal(T@np.ones(12,dtype=np.int64),-B1[u,:].toarray().ravel()))
check('balanced_star_killed_by_triangles',np.array_equal(Ktri@np.ones(12,dtype=np.int64),np.zeros(1200,dtype=np.int64)))
for k in range(12):check('proper_star_no_kernel_drop_'+str(k),rank(np.delete(Ktri,k,axis=1))==11)

# Independently reconstruct the rational vertex pseudoinverse from its certified polynomial.
def mul(p,q):
    z=[0]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):z[i+j]+=x*y
    return z
q=[1]
for p in [[80,-20,1],[36,-18,1],[-9,1],[-12,1],[-14,1],[-15,1]]:q=mul(q,p)
L=(B1@B1.T).toarray().astype(object);I=np.eye(120,dtype=object);J=np.ones((120,120),dtype=object)
Z=np.zeros((120,120),dtype=object);power=I.copy()
for k in range(8):Z-=120*q[k+1]*power;power=power@L
Z+=q[1]*J;den=120*q[0]
check('exact_pseudoinverse_equation',np.array_equal(L@Z,q[0]*(120*I-J)))
check('exact_pseudoinverse_constant_null',np.array_equal(Z@np.ones(120,dtype=object),np.zeros(120,dtype=object)))
D=(B1@T).astype(object);G=np.eye(12,dtype=object)-np.array([[F(x,den) for x in row] for row in D.T@Z@D],dtype=object)
old=json.loads((ROOT/'sources/ROBUST_RETENTION_DATA.json').read_text())['leading_gram_exact']
check('gram_matches_prior_independent_reconstruction',G.tolist()==[[F(x) for x in row] for row in old])
K=np.array([[int(x*151200) for x in row] for row in G],dtype=object);I12=np.eye(12,dtype=object)
poly=K@(K-139152*I12)@((K-136460*I12)@(K-136460*I12)-5*1798**2*I12)
check('gram_annihilator_exact',np.array_equal(poly,np.zeros((12,12),dtype=object)))
check('gram_rank_11',rank(G)==11)
check('gram_rational_eigenspace_dim_5',rank(K-139152*I12)==7)
check('gram_trace_fixes_irrational_multiplicities',sum(K[i,i] for i in range(12))==5*139152+6*136460)
check('gram_uniform_null',np.array_equal(K@np.ones(12,dtype=object),np.zeros(12,dtype=object)))
lower=F(6823,7560)-F(7,8)
check('gram_min_eigenvalue_above_7_over_8',lower>0 and lower**2>5*F(899,75600)**2)
check('gram_max_eigenvalue_below_1',1-F(6823,7560)>0 and (1-F(6823,7560))**2>5*F(899,75600)**2)

# Nonnegative-boundary obstruction, arbitrary normalization reduced to a nonzero row.
f=np.array([F(2,3),F(-1,5)],dtype=object);c=f.copy()
check('blank_signed_burden_has_negative_outward_derivative',-sum(x*x for x in f)<0)
examples=[(F(3,7),F(-2,5)),(F(-1,9),F(4,3)),(F(0),F(0))]
for i,(q0,z0) in enumerate(examples):
    qp=max(q0,0);qm=max(-q0,0)
    check('rectification_difference_'+str(i),qp-qm==q0 and qp+qm==abs(q0))
    p=max(z0,0)+F(2,7);n=max(-z0,0)+F(2,7);m=p+n
    check('lift_hidden_storage_'+str(i),p-n==z0 and p*p+n*n==(m*m+z0*z0)/2)

# Exactly soluble scalar damped oscillator; numerical diagnostics label their scope.
def throughput(gamma,r):
    a=r/2;w=math.sqrt(gamma*gamma-a*a);delta=math.atan(a/w);t0=(math.pi/2+delta)/w
    return r/gamma+2*math.exp(-a*t0)/(-math.expm1(-a*math.pi/w))
bench=[]
for ratio in [2,10,100]:
    gamma=1.;r=1/ratio;a=r/2;w=math.sqrt(1-a*a);delta=math.atan(a/w)
    c=lambda t:math.exp(-a*t)*(math.cos(w*t)+a/w*math.sin(w*t))
    t0=(math.pi/2+delta)/w
    # Resolve each sign interval, avoiding an oscillatory absolute-value quadrature alias.
    zeros=[0.]+[(math.pi/2+delta+k*math.pi)/w for k in range(10000) if (math.pi/2+delta+k*math.pi)/w<60/r]+[60/r]
    integral=sum(abs(quad(c,lo,hi,epsabs=1e-11)[0]) for lo,hi in zip(zeros,zeros[1:]))
    W=throughput(gamma,r)
    check('throughput_integral_ratio_'+str(ratio),abs(integral-W)<1e-9,'NUMERICAL')
    bench.append(dict(gamma_over_r=ratio,gross_source=W,gross_sink_limit=W,exported_signed_storage=0.5))
gamma=1.;r=.2
def rhs(t,x):
    c,p,n=x;z=p-n;q=-gamma*c
    return [gamma*z,-r*p+max(q,0),-r*n+max(-q,0)]
sol=solve_ivp(rhs,[0,50],[1,0,0],rtol=1e-10,atol=1e-12,dense_output=True,max_step=.025)
t=np.linspace(0,50,4001);c,p,n=sol.sol(t);z=p-n;a=r/2;w=math.sqrt(1-a*a)
cref=np.exp(-a*t)*(np.cos(w*t)+a/w*np.sin(w*t))
zref=-np.exp(-a*t)*np.sin(w*t)/w
check('nonnegative_lift_trajectory',min(p.min(),n.min())>=-1e-12,'NUMERICAL')
check('lift_reproduces_signed_trajectory',max(np.max(abs(c-cref)),np.max(abs(z-zref)))<2e-8,'NUMERICAL')
check('common_mode_exceeds_absolute_signed_coordinate',np.all(p+n>=abs(z)-1e-12) and (p+n-abs(z)).max()>.1,'NUMERICAL')
result={'status':'PASS','physical_promotion':0,'checks':checks,'exact_checks':sum(x['kind']=='EXACT' for x in checks),'numerical_checks':sum(x['kind']=='NUMERICAL' for x in checks)}
(ROOT/'OCCUPANCY_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
(ROOT/'OCCUPANCY_DATA.json').write_text(json.dumps({'vertex':u,'star_edges':star,'outward_signs':signs,'gram':[[str(x) for x in row] for row in G],'gram_spectrum':[{'eigenvalue':'0','multiplicity':1},{'eigenvalue':'2899/3150','multiplicity':5},{'eigenvalue':'6823/7560 - 899*sqrt(5)/75600','multiplicity':3},{'eigenvalue':'6823/7560 + 899*sqrt(5)/75600','multiplicity':3}],'throughput_benchmarks':bench},indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}))
