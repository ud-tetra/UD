"""Fresh exact candidate controls. No archived scripts imported or executed."""
from fractions import Fraction as F
from pathlib import Path
import json

class D:
    def __init__(self,v,g=None):self.v=F(v);self.g=g or {}
    def __add__(self,b):
        b=b if isinstance(b,D) else D(b)
        return D(self.v+b.v,{i:self.g.get(i,0)+b.g.get(i,0) for i in self.g.keys()|b.g.keys()})
    __radd__=__add__
    def __neg__(self):return D(-self.v,{i:-v for i,v in self.g.items()})
    def __sub__(self,b):return self+(-b if isinstance(b,D) else D(-b))
    def __rsub__(self,b):return -self+b
    def __mul__(self,b):
        b=b if isinstance(b,D) else D(b)
        return D(self.v*b.v,{i:self.g.get(i,0)*b.v+self.v*b.g.get(i,0) for i in self.g.keys()|b.g.keys()})
    __rmul__=__mul__
    def reciprocal(self):return D(1/self.v,{i:-v/self.v**2 for i,v in self.g.items()})
    def __truediv__(self,b):return self*(b.reciprocal() if isinstance(b,D) else F(1)/b)
    def __rtruediv__(self,b):return b*self.reciprocal()
    def __pow__(self,n):
        r=D(1)
        for _ in range(n):r=r*self
        return r

def chi(q):
    v=q.v if isinstance(q,D) else q
    if v<=0:return D(0) if isinstance(q,D) else F(0)
    if v>=1:return D(1) if isinstance(q,D) else F(1)
    return 10*q**3-15*q**4+6*q**5

def cp(q):return 30*q*q*(1-q)**2 if 0<q<1 else F(0)
def potential(q,b):return 2*b/(1+(q+1)**2)
def up(q,b):return -4*b*(q+1)/(1+(q+1)**2)**2
E=[(0,7,-1),(0,8,1),(1,7,1),(2,8,-1),(3,7,-1),(4,8,1),(5,7,1),(6,8,-1)]

def flow(x,y,q,p,beta):
    dx=[F(0)]*9;dy=[F(0)]*9;source=[F(0)]*9;dp=[];js=[[],[]]
    for a,(f,t,d) in enumerate(E):
        h=chi(q[a]);u=potential(q[a],beta[a]);S=x[f]**2+x[t]**2
        dx[f]-=d*h*x[t];dx[t]+=d*h*x[f]
        dy[f]-=d*h*y[t];dy[t]+=d*h*y[f]
        source[f]-=u*x[f];source[t]-=u*x[t]
        ell=d*(y[t]*x[f]-y[f]*x[t])
        dp.append(-up(q[a],beta[a])*S/2-cp(q[a])*ell)
        for z,arr in zip((x,y),js):arr.append(2*d*h*z[f]*z[t])
    dy=[v+s for v,s in zip(dy,source)]
    return dx,dy,p,dp,source,js

def directional(poly,rhs):return sum(poly.g.get(i,0)*v for i,v in enumerate(rhs))
canonical=cuts=depletion=positive_R_rates=0
for n in range(64):
    x=[F((n+3*i)%7-3) for i in range(9)]
    y=[F((2*n+5*i)%7-3) for i in range(9)]
    q=[(F(-2),F(-1),F(-1,2),F(0),F(1,4),F(1,2),F(1),F(2))[(n+i)%8] for i in range(8)]
    p=[F((n+i)%5-2,2) for i in range(8)]
    beta=[(F(1,2),F(1),F(2))[(n+i)%3] for i in range(8)]
    vals=x+y+q+p;v=[D(z,{i:F(1)}) for i,z in enumerate(vals)]
    X,Y,Q,P=v[:9],v[9:18],v[18:26],v[26:]
    K=sum(z*z/2 for z in P);C=D(0);R=D(0);rs=[]
    for a,(f,t,d) in enumerate(E):
        C+=chi(Q[a])*d*(Y[t]*X[f]-Y[f]*X[t])
        rr=potential(Q[a],beta[a])*(X[f]**2+X[t]**2)/2
        rs.append(rr);R+=rr
    H=K+C+R
    dx,dy,dq,dp,src,js=flow(x,y,q,p,beta);rhs=dx+dy+dq+dp
    canonical_rhs=[H.g.get(9+i,0) for i in range(9)]+[-H.g.get(i,0) for i in range(9)]+[H.g.get(26+i,0) for i in range(8)]+[-H.g.get(18+i,0) for i in range(8)]
    assert rhs==canonical_rhs and directional(H,rhs)==0
    assert sum(x[i]*dx[i] for i in range(9))==0
    local_sum=F(0)
    for a,(f,t,d) in enumerate(E):
        u=potential(q[a],beta[a]);S=x[f]**2+x[t]**2
        Sdot=2*x[f]*dx[f]+2*x[t]*dx[t]
        force=-up(q[a],beta[a])*S/2
        ell=d*(y[t]*x[f]-y[f]*x[t])
        rdot=directional(rs[a],rhs)
        assert rdot==-force*p[a]+u*Sdot/2
        assert p[a]*dp[a]==force*p[a]-ell*cp(q[a])*p[a]
        local_sum+=u*Sdot/2-ell*cp(q[a])*p[a]
        positive_R_rates+=int(rdot>0);depletion+=1
    assert directional(K+R,rhs)==local_sum==-directional(C,rhs)
    bstar=max(sum(beta[a] for a,(f,t,d) in enumerate(E) if i in (f,t)) for i in range(9))
    assert 0<=R.v<=bstar*sum(z*z for z in x)
    canonical+=1
    for bits in range(512):
        inside=[(bits>>i)&1 for i in range(9)]
        for z,dz,curr,dual in ((x,dx,js[0],False),(y,dy,js[1],True)):
            cut=sum((inside[t]-inside[f])*j for (f,t,d),j in zip(E,curr))
            extra=sum(2*y[i]*src[i]*inside[i] for i in range(9)) if dual else F(0)
            assert sum(2*z[i]*dz[i]*inside[i] for i in range(9))==cut+extra
            cuts+=1

inequalities=margins=0
for k in range(65):
    q=F(k,64);phi=q*(q+2)/(q*q+2*q+2)
    assert 5*(q+2)-3*(q*q+2*q+2)==(1-q)*(3*q+4)
    assert F(3,5)*q<=phi<=q
    assert chi(q)<=F(15,8)*q and chi(q)<=F(25,8)*phi
    assert 0<=cp(q)<=F(15,8)
    inequalities+=1
    for B in (F(1,4),F(1,2),F(1),F(2)):
        for ratio in (F(-1),F(0),F(1,16),F(1,8),F(1,4)):
            ell=ratio*B;delta=B-F(25,8)*max(ell,0)
            assert delta>0
            drop=B*phi-ell*chi(q)
            assert drop>=delta*phi>=F(3,5)*delta*q
            margins+=1

funding=0
for beta in (F(1,2),F(1),F(2)):
    for S in (F(1,4),F(1),F(4)):
        B=beta*S/2
        for q in (F(0),F(1,4),F(1),F(2),F(10),F(100)):
            phi=q*(q+2)/(q*q+2*q+2)
            R=potential(q,beta)*S/2;K=B*phi
            assert K+R==B and 0<=K<B
            funding+=1
        assert potential(F(1),beta)*S/2==beta*S/5
        assert B*F(3,5)==3*beta*S/10
        # A burden above 3B/5 makes the arrival kinetic stock negative.
        assert B*F(3,5)-B<0
assert F(4)*F(5,3)<F(8,3)**2
# Explicit network replenishment: target 013/tau0, boundary 123/tau0 on.
x=[F(0)]*9;x[1]=x[7]=F(1);x[5]=F(2)
y=[F(0)]*9;q=[F(0)]*8;q[6]=F(1);p=[F(0)]*8
res=flow(x,y,q,p,[F(1)]*8);dx=res[0]
assert (2*x[1]*dx[1]+2*x[7]*dx[7])/2==2
# Full H remains unbounded below at fixed positive R for an on isolated pair.
unbounded=[{'dual_magnitude':M,'R':str(F(1,5)),'H':str(F(1,5)-M)} for M in (1,10,100)]
out={'status':'PASS_EXACT_CONDITIONAL_BOUNDED_POTENTIAL','canonical_gradient_H_controls':canonical,'cut_receipts':cuts,'local_depletion_controls':depletion,'positive_network_potential_rate_controls':positive_R_rates,'profile_inequality_controls':inequalities,'strict_margin_controls':margins,'isolated_positive_funding_controls':funding,'network_replenishment_witness_rate':2,'indefinite_H_controls':unbounded,'arithmetic':'exact fractions; sparse forward differentiation','opening_time_numerically_estimated':False,'independent_review':False,'archived_scripts_executed':False,'physical_promotion':0}
Path(__file__).with_name('RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
