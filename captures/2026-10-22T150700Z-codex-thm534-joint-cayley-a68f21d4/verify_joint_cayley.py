"""Fresh Gaussian-rational finite-map controls; no archived replay execution."""
from fractions import Fraction as F
from pathlib import Path
import json
class C:
    def __init__(self,r=0,i=0):self.r=F(r);self.i=F(i)
    def __add__(self,b):
        b=b if isinstance(b,C) else C(b)
        return C(self.r+b.r,self.i+b.i)
    __radd__=__add__
    def __neg__(self):return C(-self.r,-self.i)
    def __sub__(self,b):return self+(-b if isinstance(b,C) else C(-b))
    def __mul__(self,b):
        b=b if isinstance(b,C) else C(b)
        return C(self.r*b.r-self.i*b.i,self.r*b.i+self.i*b.r)
    __rmul__=__mul__
    def conj(self):return C(self.r,-self.i)
    def norm(self):return self.r*self.r+self.i*self.i
    def inv(self):return C(self.r/self.norm(),-self.i/self.norm())
    def __truediv__(self,b):return self*(b.inv() if isinstance(b,C) else F(1)/b)
    def __eq__(self,b):
        b=b if isinstance(b,C) else C(b)
        return self.r==b.r and self.i==b.i
I=C(0,1);N=9
E=[(0,7,-1),(0,8,1),(1,7,1),(2,8,-1),(3,7,-1),(4,8,1),(5,7,1),(6,8,-1)]
BLOCKS=[(0,1),(2,4,6),(3,5,7)]
def eye():return [[C(int(i==j)) for j in range(N)] for i in range(N)]
def zero():return [[C() for _ in range(N)] for _ in range(N)]
def plus(A,B):return [[a+b for a,b in zip(ar,br)] for ar,br in zip(A,B)]
def scale(A,c):return [[c*v for v in row] for row in A]
def mm(A,B):return [[sum((A[i][k]*B[k][j] for k in range(N)),C()) for j in range(N)] for i in range(N)]
def mv(A,u):return [sum((v*w for v,w in zip(row,u)),C()) for row in A]
def dag(A):return [[A[j][i].conj() for j in range(N)] for i in range(N)]
def inv(A):
    aug=[row[:]+erow for row,erow in zip(A,eye())]
    for col in range(N):
        pivot=next(i for i in range(col,N) if aug[i][col].norm())
        aug[col],aug[pivot]=aug[pivot],aug[col];v=aug[col][col].inv();aug[col]=[v*x for x in aug[col]]
        for i in range(N):
            if i==col:continue
            v=aug[i][col]
            if v.norm():aug[i]=[x-v*y for x,y in zip(aug[i],aug[col])]
    return [row[N:] for row in aug]
def quadratic(u,A):return sum((a.conj()*b for a,b in zip(u,mv(A,u))),C())
def chi(q):
    if q<=0:return F(0)
    if q>=1:return F(1)
    return 10*q**3-15*q**4+6*q**5

def cp(q):return 30*q*q*(1-q)**2 if 0<q<1 else F(0)
def matrices(block,q,beta):
    L=zero();derivatives={}
    for e in block:
        f,t,_=E[e];h=chi(q[e]);U=2*beta[e]/(1+(q[e]+1)**2)
        hp=cp(q[e]);Up=-4*beta[e]*(q[e]+1)/(1+(q[e]+1)**2)**2
        for i in (f,t):L[i][i]+=h+U
        L[f][t]-=C(h);L[t][f]-=C(h)
        A=zero()
        for i in (f,t):A[i][i]=C(hp+Up)
        A[f][t]=A[t][f]=C(-hp);derivatives[e]=A
    return L,derivatives

def event(block,q,p,beta,u,eps=F(1,4),connection=False):
    L,Lq=matrices(block,q,beta);Cinv=inv(plus(eye(),scale(L,I*eps/2)))
    R=mm(Cinv,plus(eye(),scale(L,-I*eps/2)))
    new=mv(R,u);mid=mv(Cinv,u)
    assert mid==[(a+b)/2 for a,b in zip(u,new)]
    pn=p[:]
    for e,A in Lq.items():
        form=quadratic(mid,A);assert form.i==0
        pn[e]-=eps*form.r/2
        if connection:
            # Differentiate C*R=D, independently of the simplified connection.
            Rp=scale(mm(mm(Cinv,A),plus(eye(),R)),-I*eps/2)
            left=mm(dag(R),Rp)
            right=scale(mm(mm(dag(Cinv),A),Cinv),-I*eps)
            assert left==right
    return new,pn,R,L

cases=connections=receipts=0
for n in range(16):
    u=[C((n+3*i)%7-3,(2*n+5*i)%7-3) for i in range(N)]
    q=[(F(0),F(1,4),F(1,2),F(1))[(n+i)%4] for i in range(8)]
    p=[F((n+i)%5-2,2) for i in range(8)]
    beta=[(F(1),F(4))[(n+i)%2] for i in range(8)]
    for block in BLOCKS:
        v,pn,R,L=event(block,q,p,beta,u,connection=True)
        assert mm(dag(R),R)==eye() and mm(mm(dag(R),L),R)==L
        assert sum(z.norm() for z in v)==sum(z.norm() for z in u)
        assert quadratic(v,L)==quadratic(u,L)
        mid=[(a+b)/2 for a,b in zip(u,v)];delta=[F(0)]*N
        for e in block:
            f,t,_=E[e];J=2*F(1,4)*chi(q[e])*(mid[f].conj()*mid[t]).i
            delta[f]-=J;delta[t]+=J;receipts+=1
        assert [b.norm()-a.norm() for a,b in zip(u,v)]==delta
        oldH=sum(z*z/2 for z in p)+quadratic(u,L).r/2
        newH=sum(z*z/2 for z in pn)+quadratic(v,L).r/2
        dp=[b-a for a,b in zip(p,pn)]
        assert newH-oldH==sum(a*b+b*b/2 for a,b in zip(p,dp))
        connections+=len(block);cases+=1
    # Private blocks commute on full lifted state, with the same frozen gates.
    v,p0,_,_=event(BLOCKS[1],q,p,beta,u)
    ab,pab,_,_=event(BLOCKS[2],q,p0,beta,v)
    v,p1,_,_=event(BLOCKS[2],q,p,beta,u)
    ba,pba,_,_=event(BLOCKS[1],q,p1,beta,v)
    assert ab==ba and pab==pba

q=[F(0)]*8;p=[F(0)]*8;beta=[F(1)]*8;u=[C(1) for _ in range(N)]
v,pn,R,L=event(BLOCKS[0],q,p,beta,u)
assert v[0]==C(F(15,17),F(-8,17))
assert v[7]==v[8]==C(F(63,65),F(-16,65))
assert pn[0]==pn[1]==F(266,1105)
assert sum(z*z/2 for z in pn)==F(70756,1221025)
assert quadratic(u,L).r/2==quadratic(v,L).r/2==2
# Equal-stock perturbations keep the same block and have exactly unit field gain.
ties=0
for delta in (F(1,4),F(1,16),F(1,64),F(1,256)):
    pert=u[:];pert[0]+=C(delta)
    w,pp,_,_=event(BLOCKS[0],q,p,beta,pert)
    assert sum((a-b).norm() for a,b in zip(v,w))==delta*delta
    assert max(abs(a-b) for a,b in zip(pn,pp))<=20*delta
    ties+=1
# Overlapping shared/private blocks are not interchangeable.
q=[F(1)]*8
_,_,Rs,_=event(BLOCKS[0],q,p,beta,u)
_,_,Rp,_=event(BLOCKS[1],q,p,beta,u)
assert mm(Rs,Rp)!=mm(Rp,Rs)
# Cell reflection fixes shared block; private blocks are interchanged.
perm=[0,2,1,4,3,6,5,8,7];ep=[1,0,3,2,5,4,7,6]
assert {ep[e] for e in BLOCKS[0]}==set(BLOCKS[0])
assert {ep[e] for e in BLOCKS[1]}==set(BLOCKS[2])
for Ablock,Bblock in ((BLOCKS[0],BLOCKS[0]),(BLOCKS[1],BLOCKS[2])):
    La,_=matrices(Ablock,q,beta);Lb,_=matrices(Bblock,q,beta)
    assert all(La[i][j]==Lb[perm[i]][perm[j]] for i in range(N) for j in range(N))
out={'status':'PASS_EXACT_CONDITIONAL_JOINT_CANONICAL_SUBSTEP','block_unitarity_norm_frozen_energy_cases':cases,'gate_connection_identity_checks':connections,'midpoint_contact_receipts':receipts,'private_lift_commutation_cases':16,'equal_stock_perturbation_controls':ties,'overlapping_block_noncommutation':True,'shared_block_onset_kick':'266/1105 for both gates','standalone_full_energy_defect':'70756/1221025','arithmetic':'exact Gaussian rational pairs; exact matrix inversion','full_H_preserved':False,'full_integrator_implemented':False,'native_priority_rule':False,'archived_scripts_executed':False,'independent_review':False,'physical_promotion':0}
Path(__file__).with_name('RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
