"""Fresh exact constructor controls; no archived-script imports."""
from fractions import Fraction as F
from pathlib import Path
import json

class D:
    def __init__(self,v,g=None): self.v=F(v); self.g=g or {}
    def __add__(self,b):
        b=b if isinstance(b,D) else D(b)
        keys=self.g.keys()|b.g.keys()
        return D(self.v+b.v,{i:self.g.get(i,0)+b.g.get(i,0) for i in keys})
    __radd__=__add__
    def __neg__(self):return D(-self.v,{i:-v for i,v in self.g.items()})
    def __sub__(self,b):return self+-b if isinstance(b,D) else self+D(-b)
    def __rsub__(self,b):return -self+b
    def __mul__(self,b):
        b=b if isinstance(b,D) else D(b)
        keys=self.g.keys()|b.g.keys()
        return D(self.v*b.v,{i:self.g.get(i,0)*b.v+self.v*b.g.get(i,0) for i in keys})
    __rmul__=__mul__
    def __pow__(self,n):
        r=D(1)
        for _ in range(n):r=r*self
        return r

def chi(q):
    v=q.v if isinstance(q,D) else q
    if v<=0:return D(0) if isinstance(q,D) else F(0)
    if v>=1:return D(1) if isinstance(q,D) else F(1)
    return 10*q**3-15*q**4+6*q**5

def prime(q):return 30*q*q*(1-q)**2 if 0<q<1 else F(0)
E=[(0,7,-1),(0,8,1),(1,7,1),(2,8,-1),(3,7,-1),(4,8,1),(5,7,1),(6,8,-1)]
canonical=cuts=norm_sources=0
for n in range(64):
    x=[F((n+3*i)%7-3) for i in range(9)]
    y=[F((2*n+5*i)%7-3) for i in range(9)]
    q=[(F(0),F(1,4),F(1,2),F(1))[(n+i)%4] for i in range(8)]
    p=[F((n+i)%5-2,2) for i in range(8)]
    alpha=[(F(1,2),F(1),F(2))[(n+i)%3] for i in range(8)]
    vals=x+y+q+p
    v=[D(z,{i:F(1)}) for i,z in enumerate(vals)]
    X,Y,Q,P=v[:9],v[9:18],v[18:26],v[26:]
    H=sum(F(1,2)*z*z for z in P)
    for a,(f,t,d) in enumerate(E):
        H+=chi(Q[a])*d*(Y[t]*X[f]-Y[f]*X[t])-F(1,2)*alpha[a]*Q[a]*(X[f]**2+X[t]**2)
    dx=[F(0)]*9;dy=[F(0)]*9;source=[F(0)]*9;dp=[]
    currents=[[],[]]
    for a,(f,t,d) in enumerate(E):
        h=chi(q[a]);g=alpha[a]*q[a]
        dx[f]-=d*h*x[t];dx[t]+=d*h*x[f]
        dy[f]-=d*h*y[t];dy[t]+=d*h*y[f]
        source[f]+=g*x[f];source[t]+=g*x[t]
        ell=d*(y[t]*x[f]-y[f]*x[t]);S=x[f]**2+x[t]**2
        dp.append(-prime(q[a])*ell+alpha[a]*S/2)
        for z,js in zip((x,y),currents):js.append(2*d*h*z[f]*z[t])
    dy=[a+b for a,b in zip(dy,source)]
    rhs=dx+dy+p+dp
    canon=[H.g.get(9+i,0) for i in range(9)]+[-H.g.get(i,0) for i in range(9)]+[H.g.get(26+i,0) for i in range(8)]+[-H.g.get(18+i,0) for i in range(8)]
    assert rhs==canon
    assert sum(H.g.get(i,0)*rhs[i] for i in range(34))==0
    assert sum(x[i]*dx[i] for i in range(9))==0
    assert sum(2*y[i]*dy[i] for i in range(9))==sum(2*y[i]*source[i] for i in range(9))
    canonical+=1
    if sum(2*y[i]*source[i] for i in range(9))!=0:norm_sources+=1
    for bits in range(512):
        inside=[(bits>>i)&1 for i in range(9)]
        for z,dz,js,isdual in ((x,dx,currents[0],False),(y,dy,currents[1],True)):
            boundary=sum((inside[t]-inside[f])*j for (f,t,d),j in zip(E,js))
            local_source=sum(2*y[i]*source[i]*inside[i] for i in range(9)) if isdual else F(0)
            assert sum(2*z[i]*dz[i]*inside[i] for i in range(9))==boundary+local_source
            cuts+=1

# Independent polynomial substitution checks in model time.
def add(a,b):
    c=a.copy()
    for i,v in b.items():c[i]=c.get(i,F(0))+v
    return {i:v for i,v in c.items() if v}
def mul(a,b):
    c={}
    for i,v in a.items():
        for j,w in b.items():c[i+j]=c.get(i+j,F(0))+v*w
    return {i:v for i,v in c.items() if v}
def scale(a,c):return {i:v*c for i,v in a.items() if v*c}
def der(a):return {i-1:i*v for i,v in a.items() if i and v}
def power(a,n):
    r={0:F(1)}
    for _ in range(n):r=mul(r,a)
    return r
polynomials=0
for alpha in (F(1,2),F(1),F(2)):
    for S in (F(1,4),F(1),F(4)):
        k=alpha*S/4;q={2:k};p={1:alpha*S/2};a={3:alpha**2*S/12}
        assert der(q)==p and der(p)=={0:alpha*S/2}
        assert der(a)==scale(q,alpha)
        assert scale(mul(p,p),F(1,2))==scale(q,alpha*S/2)
        ch=add(add(scale(power(q,3),10),scale(power(q,4),-15)),scale(power(q,5),6))
        theta={7:10*k**3/7,9:-15*k**4/9,11:6*k**5/11}
        assert der(theta)==ch
        assert scale(mul(a,a),S)=={6:alpha**4*S**3/144}
        assert alpha*S/2>0
        polynomials+=1
# Explicit onset-without-completion control: g=q(1-2q).
assert 1-4*F(0)>0
assert F(1,2)*(1-2*F(1,2))==0
assert F(3,4)*(1-2*F(3,4))<0
out={'status':'PASS_EXACT_CONDITIONAL_LOCAL_WAKE','canonical_gradient_and_H_controls':canonical,'cut_receipts':cuts,'nonzero_auxiliary_norm_source_cases':norm_sources,'isolated_polynomial_solution_controls':polynomials,'onset_without_completion_control':'g(q)=q(1-2q) on transition interval','arithmetic':'integers and fractions.Fraction; sparse exact forward differentiation','trajectory_numerically_integrated':False,'archived_scripts_executed':False,'independent_review':False,'physical_promotion':0}
Path(__file__).with_name('RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
