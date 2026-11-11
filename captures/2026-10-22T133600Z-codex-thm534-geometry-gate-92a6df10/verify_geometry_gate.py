"""Fresh Fraction checks of conditional metric/Hamiltonian compatibility."""
from fractions import Fraction as F
from itertools import combinations,permutations,product
from pathlib import Path
import json

EPS=F(1,4)
def m(f,t):
    n=f*f+t*t
    return (f**4+t**4)/(n*n) if n else F(1)
def grad(f,t):
    n=f*f+t*t
    if not n:return F(0),F(0)
    p=f*f/n
    return ((4*p-2)*2*f*t*t/(n*n),-(4*p-2)*2*f*f*t/(n*n))
def field(f,t,d=1):h=m(f,t);return -d*h*t,d*h*f
def divergence(f,t,d=1):a,b=grad(f,t);return d*(-t*a+f*b)
def step(f,t,d=1):
    h=m(f,t);b=EPS*h/2;c=(1-b*b)/(1+b*b);s=2*b/(1+b*b)
    return c*f-d*s*t,d*s*f+c*t
def derivative(f,t,d=1):
    h=m(f,t);gf,gt=grad(f,t);b=EPS*h/2;c=(1-b*b)/(1+b*b);s=2*b/(1+b*b)
    dc=-4*b/(1+b*b)**2;ds=2*(1-b*b)/(1+b*b)**2
    vf=dc*f-d*ds*t;vt=d*ds*f+dc*t
    return [[c+vf*EPS*gf/2,-d*s+vf*EPS*gt/2],[d*s+vt*EPS*gf/2,c+vt*EPS*gt/2]]
def det(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
pair_checks=weighted_checks=nonzero_divergences=0
for i,j in product(range(-4,5),repeat=2):
    f,t=F(i,3),F(j,3)
    if not(f or t):continue
    for d in (-1,1):
        out=step(f,t,d);assert sum(v*v for v in out)==f*f+t*t
        assert det(derivative(f,t,d))==1+EPS*divergence(f,t,d)/(1+(EPS*m(f,t)/2)**2)
        gf,gt=grad(f,t);rho=1/m(f,t);rf,rt=-gf/m(f,t)**2,-gt/m(f,t)**2
        a,b=field(f,t,d);assert rho*divergence(f,t,d)+rf*a+rt*b==0
        pair_checks+=1;weighted_checks+=1
        if divergence(f,t,d):nonzero_divergences+=1
assert divergence(F(1),F(2))==F(24,25)
assert det(derivative(F(1),F(2)))==F(49889,40289)
assert field(F(1),F(1))!=tuple(a+b for a,b in zip(field(F(1),F(0)),field(F(0),F(1))))
x=step(F(1),F(0));y=step(F(1),F(1))
dot=sum(a*b for a,b in zip(x,y));assert dot==F(18641,16705) and dot!=1
balanced=(F(1),F(1));out=step(*balanced)
assert det(derivative(*balanced))==1 and m(*out)>m(*balanced)
weighted_jacobian=det(derivative(*balanced))*m(*balanced)/m(*out)
assert weighted_jacobian==F(66049**2,66049**2+16320**2) and weighted_jacobian<1

CELLS=[(0,1,2,3),(0,1,2,4)]
FACES=sorted(set(combinations(CELLS[0],3))|set(combinations(CELLS[1],3)))
D=[[0,0] for _ in FACES]
for j,c in enumerate(CELLS):
    for k in range(4):D[FACES.index(c[:k]+c[k+1:])][j]=(1,-1)[j]*(-1)**k
CONTACTS=[(f,j) for f in range(7) for j in range(2) if D[f][j]]
def tensor(z,unit=False,allowed=None):
    p=[[F(0) for _ in range(9)] for _ in range(9)]
    dp=[[[F(0) for _ in range(9)] for _ in range(9)] for _ in range(9)]
    for f,j in CONTACTS:
        if allowed is not None and (f,j) not in allowed:continue
        k=7+j;h=F(1) if unit else m(z[f],z[k]);gf,gt=(F(0),F(0)) if unit else grad(z[f],z[k]);d=D[f][j]
        p[f][k]=-d*h;p[k][f]=d*h
        for coord,g in ((f,gf),(k,gt)):dp[f][k][coord]=-d*g;dp[k][f][coord]=d*g
    return p,dp
def jacobi(p,dp,i,j,k):
    return sum(p[i][l]*dp[j][k][l]+p[j][l]*dp[k][i][l]+p[k][l]*dp[i][j][l] for l in range(9))
z=[F(1)]*9;z[5]=2
p,dp=tensor(z);triples=list(combinations(range(9),3))
witness=jacobi(p,dp,1,5,7);assert witness==F(-24,125)
assert sum(z[i]*sum(p[i][j]*z[j] for j in range(9)) for i in range(9))==0
unit,du=tensor(z,True);assert all(jacobi(unit,du,*ijk)==0 for ijk in triples)
isolated,di=tensor(z,allowed={(1,0)})
assert all(jacobi(isolated,di,*ijk)==0 for ijk in triples)
global_checks=0;nonpoisson_states=0
for seed in range(1,33):
    state=[F(i+seed,seed+2) for i in range(9)];pp,dd=tensor(state)
    values=[jacobi(pp,dd,*ijk) for ijk in triples];global_checks+=len(values)
    assert any(values);nonpoisson_states+=1
    assert sum(state[i]*sum(pp[i][j]*state[j] for j in range(9)) for i in range(9))==0
# A common scalar rescaling cannot remove this particular private-face star witness.
scale_controls=0
for scale,gs in ((F(1),[F(0)]*9),(1+sum(x*x for x in z),[2*x for x in z]),(1+z[7]**2,[F(0)]*7+[2*z[7],F(0)])):
    sp=[[scale*p[i][j] for j in range(9)] for i in range(9)]
    sd=[[[gs[k]*p[i][j]+scale*dp[i][j][k] for k in range(9)] for j in range(9)] for i in range(9)]
    assert jacobi(sp,sd,1,5,7)==scale*scale*witness;scale_controls+=1
# Endpoint witness that enforces core-independence for any valid pair-local bracket.
assert m(F(0),F(1))==1 and grad(F(0),F(1))[1]==0
assert m(F(0),F(1))*grad(F(2),F(1))[1]-m(F(2),F(1))*grad(F(0),F(1))[1]==F(-48,125)
def parity(s):return (-1)**sum(s[i]>s[j] for i in range(len(s)) for j in range(i+1,len(s)))
covariance_checks=0
for base in permutations((0,1,2)):
    for tips in ((3,4),(4,3)):
        perm=base+tips;q=[];sg=[]
        for f in FACES:
            mapped=tuple(perm[v] for v in f);q.append(FACES.index(tuple(sorted(mapped))));sg.append(parity(mapped))
        for j,c in enumerate(CELLS):
            mapped=tuple(perm[v] for v in c);k=CELLS.index(tuple(sorted(mapped)));q.append(7+k);sg.append((1,-1)[j]*parity(mapped)*(1,-1)[k])
        moved=[F(0)]*9
        for i in range(9):moved[q[i]]=sg[i]*z[i]
        mp,md=tensor(moved)
        for i,j,k in triples:
            assert jacobi(mp,md,q[i],q[j],q[k])==sg[i]*sg[j]*sg[k]*jacobi(p,dp,i,j,k);covariance_checks+=1
RESULT={'status':'PASS_EXACT_CONDITIONAL_COMPATIBILITY_OBSTRUCTION','pair_determinant_and_norm_checks':pair_checks,'continuous_weighted_area_checks':weighted_checks,'nonzero_divergence_controls':nonzero_divergences,'pair_divergence_witness':'24/25','finite_step_determinant_witness':'49889/40289','transition_inner_product_original':'1','transition_inner_product_after':'18641/16705','continuous_area_repair_not_preserved_by_frozen_step':str(weighted_jacobian),'global_jacobi_component_checks':global_checks,'nonpoisson_state_controls':nonpoisson_states,'Kminus_jacobi_indices':[1,5,7],'Kminus_jacobi_witness':'-24/125','unit_tensor_jacobi_checks':len(triples),'isolated_contact_jacobi_checks':len(triples),'scalar_rescaling_controls':scale_controls,'signed_jacobi_covariance_checks':covariance_checks,'conditional_unit_response_theorem':'Jacobi + pair-local coefficients + C1 regularity away from vacuum + unit axis responses imply m=1','scope':'Optional geometric compatibility gates; no retraction of v1.8 robustness/receipts','native_selection':'OPEN','outside_peer_review':False,'physical_promotion':0}
if __name__=='__main__':
    (Path(__file__).parent/'RESULTS.json').write_text(json.dumps(RESULT,indent=2)+'\n');print(json.dumps(RESULT,indent=2))
