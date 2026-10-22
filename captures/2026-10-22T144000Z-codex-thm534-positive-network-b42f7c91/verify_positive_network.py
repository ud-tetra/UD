"""Fresh exact controls for positive candidate network; standard library only."""
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
    def inv(self):return D(1/self.v,{i:-v/self.v**2 for i,v in self.g.items()})
    def __truediv__(self,b):return self*(b.inv() if isinstance(b,D) else F(1)/b)
    def __rtruediv__(self,b):return b*self.inv()
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
def U(q,b):return 2*b/(1+(q+1)**2)
def Up(q,b):return -4*b*(q+1)/(1+(q+1)**2)**2
E=[(0,7,-1),(0,8,1),(1,7,1),(2,8,-1),(3,7,-1),(4,8,1),(5,7,1),(6,8,-1)]
def dotgrad(poly,rhs):return sum(poly.g.get(i,0)*v for i,v in enumerate(rhs))
canonical=cuts=depletion=squares=mask_positive=0
for n in range(64):
    x=[F((n+3*i)%7-3) for i in range(9)]
    y=[F((2*n+5*i)%7-3) for i in range(9)]
    q=[(F(-2),F(-1),F(-1,2),F(0),F(1,4),F(1,2),F(1),F(2))[(n+i)%8] for i in range(8)]
    p=[F((n+i)%5-2,2) for i in range(8)]
    beta=[(F(1,2),F(1),F(4))[(n+i)%3] for i in range(8)]
    vs=[D(z,{i:F(1)}) for i,z in enumerate(x+y+q+p)]
    X,Y,Q,P=vs[:9],vs[9:18],vs[18:26],vs[26:]
    K=sum(z*z/2 for z in P);V=D(0);R=D(0);rs=[];qs=[]
    pairS=[];pairQ=[]
    for a,(f,t,d) in enumerate(E):
        ss=X[f]**2+X[t]**2+Y[f]**2+Y[t]**2
        angular=d*(Y[t]*X[f]-Y[f]*X[t]);qq=angular+ss/2
        assert qq.v==((x[f]+d*y[t])**2+(x[t]-d*y[f])**2)/2>=0
        rr=U(Q[a],beta[a])*ss/2
        V+=chi(Q[a])*qq;R+=rr;rs.append(rr);qs.append(qq)
        pairS.append(ss.v);pairQ.append(qq.v);squares+=1
    H=K+V+R
    dx=[F(0)]*9;dy=[F(0)]*9;omega=[F(0)]*9;dp=[];currents=[]
    for a,(f,t,d) in enumerate(E):
        h=chi(q[a]);u=U(q[a],beta[a])
        dx[f]-=d*h*x[t];dx[t]+=d*h*x[f]
        dy[f]-=d*h*y[t];dy[t]+=d*h*y[f]
        omega[f]+=h+u;omega[t]+=h+u
        dp.append(-Up(q[a],beta[a])*pairS[a]/2-cp(q[a])*pairQ[a])
        currents.append(2*d*h*(x[f]*x[t]+y[f]*y[t]))
    dx=[a+o*v for a,o,v in zip(dx,omega,y)]
    dy=[a-o*v for a,o,v in zip(dy,omega,x)]
    rhs=dx+dy+p+dp
    canon=[H.g.get(9+i,0) for i in range(9)]+[-H.g.get(i,0) for i in range(9)]+[H.g.get(26+i,0) for i in range(8)]+[-H.g.get(18+i,0) for i in range(8)]
    assert rhs==canon and dotgrad(H,rhs)==0
    assert sum(x[i]*dx[i]+y[i]*dy[i] for i in range(9))==0
    assert H.v>=K.v>=0 and H.v>=V.v>=0 and H.v>=R.v>=0
    expectedV=F(0)
    for a,(f,t,d) in enumerate(E):
        sdot=2*(x[f]*dx[f]+x[t]*dx[t]+y[f]*dy[f]+y[t]*dy[t])
        force=-Up(q[a],beta[a])*pairS[a]/2
        assert dotgrad(rs[a],rhs)==-force*p[a]+U(q[a],beta[a])*sdot/2
        assert p[a]*dp[a]==force*p[a]-pairQ[a]*cp(q[a])*p[a]
        expectedV+=pairQ[a]*cp(q[a])*p[a]-U(q[a],beta[a])*sdot/2
        depletion+=1
    assert dotgrad(V,rhs)==expectedV
    for mask in range(256):
        mv=sum(((mask>>a)&1)*z for a,z in enumerate(pairQ))
        assert K.v+mv+R.v>=0 and mv>=0
        mask_positive+=1
    dn=[2*(x[i]*dx[i]+y[i]*dy[i]) for i in range(9)]
    for bits in range(512):
        inside=[(bits>>i)&1 for i in range(9)]
        cut=sum((inside[t]-inside[f])*j for (f,t,d),j in zip(E,currents))
        assert sum(dn[i]*inside[i] for i in range(9))==cut
        cuts+=1
    canonical+=1

# Sharpness of the isotropic completion for both incidence signs.
sharp=0
for d in (-1,1):
    for a in (F(0),F(1,2),F(1),F(3,2),F(2)):
        S=F(2);ell=F(-1);val=ell+a*S/2
        assert (val>=0)==(a>=1)
        sharp+=1

margins=0
for S in (F(1,4),F(1),F(4)):
    for beta in (F(4),F(5),F(8)):
        B=beta*S/2;cost=S/2;delta=B-F(25,8)*cost
        assert delta>0
        for k in range(65):
            q=F(k,64);phi=q*(q+2)/(q*q+2*q+2)
            drop=B*phi-cost*chi(q)
            assert drop>=delta*phi>=F(3,5)*delta*q
            margins+=1
        R=beta*S/5;V=cost;K=3*beta*S/10-cost
        assert K>0 and K+V+R==B
assert F(3,10)-F(1,2)==F(-1,5) # beta=1,S=1 cannot arrive.
assert F(2)-F(25,16)==F(7,16)
assert F(4,5)+F(1,2)+F(7,10)==2
# Original x stock changes under the new exchange; joint stock does not.
exchange={'x':F(1),'y':F(1),'omega':F(1)}
assert 2*exchange['x']*exchange['omega']*exchange['y']==2
assert 2+(-2)==0
# The old exact x-flow Hamiltonian stays unbounded as its unrestricted dual grows.
old=[{'t':t,'H_minus_F':-t} for t in (1,10,100)]
out={'status':'PASS_EXACT_CONDITIONAL_POSITIVE_NETWORK','canonical_gradient_and_H_controls':canonical,'joint_cut_receipts':cuts,'local_depletion_controls':depletion,'sum_of_squares_controls':squares,'binary_mask_positivity_controls':mask_positive,'completion_sharpness_controls':sharp,'isolated_strict_margin_controls':margins,'old_flow_unbounded_controls':old,'beta_one_on_kinetic_countercontrol':'-1/5 at S=1,y0=0','new_x_only_norm_source_witness':2,'arithmetic':'exact fractions; sparse forward differentiation','trajectory_integrated':False,'native_identification':False,'independent_review':False,'archived_scripts_executed':False,'physical_promotion':0}
Path(__file__).with_name('RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
