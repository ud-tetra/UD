"""Fresh exact method and rational-root receipt controls; no archived imports."""
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
    def norm(self):return self.r**2+self.i**2
    def inv(self):return C(self.r/self.norm(),-self.i/self.norm())
    def __truediv__(self,b):return self*(b.inv() if isinstance(b,C) else F(1)/b)
    def __eq__(self,b):
        b=b if isinstance(b,C) else C(b)
        return self.r==b.r and self.i==b.i
I=C(0,1)
def eye(n):return [[C(i==j) for j in range(n)] for i in range(n)]
def inv(A):
    n=len(A);a=[row[:]+erow for row,erow in zip(A,eye(n))]
    for c in range(n):
        k=next(i for i in range(c,n) if a[i][c].norm())
        a[c],a[k]=a[k],a[c];v=a[c][c].inv();a[c]=[v*z for z in a[c]]
        for i in range(n):
            if i==c:continue
            v=a[i][c]
            if v.norm():a[i]=[z-v*w for z,w in zip(a[i],a[c])]
    return [row[n:] for row in a]
def mv(A,u):return [sum((a*b for a,b in zip(row,u)),C()) for row in A]
def quad(u,L):
    z=sum((a.conj()*b for a,b in zip(u,mv(L,u))),C());assert z.i==0
    return z.r

def chi(q):
    if q<=0:return F(0)
    if q>=1:return F(1)
    return 10*q**3-15*q**4+6*q**5

def cp(q):return 30*q*q*(1-q)**2 if 0<q<1 else F(0)
def cpp(q):return 60*q*(1-q)*(1-2*q) if 0<q<1 else F(0)
def U(q,beta):return 2*beta/(1+(q+1)**2)
def Up(q,beta):return -4*beta*(q+1)/(1+(q+1)**2)**2
def Upp(q,beta):return -4*beta*(1-3*(q+1)**2)/(1+(q+1)**2)**3
def V(q,Q,S,beta):return chi(q)*Q+U(q,beta)*S/2
def Vp(q,Q,S,beta):return cp(q)*Q+Up(q,beta)*S/2
def DD(a,b,Q,S,beta):return (V(b,Q,S,beta)-V(a,Q,S,beta))/(b-a) if b!=a else Vp(a,Q,S,beta)
def residual(b,a,p,h,Q,S,beta):return b-a-h*p+h*h*DD(a,b,Q,S,beta)/2

def gate(a,p,h,Q,S,beta,iterations=40):
    M=15*Q+2*beta*S;B=F(15,8)*Q+beta*S
    assert h*h*M<4
    lo=a+h*p-h*h*B/2;hi=a+h*p+h*h*B/2
    assert residual(lo,a,p,h,Q,S,beta)<=0<=residual(hi,a,p,h,Q,S,beta)
    for _ in range(iterations):
        mid=(lo+hi)/2;rho=residual(mid,a,p,h,Q,S,beta)
        if rho==0:lo=hi=mid;break
        if rho<0:lo=mid
        else:hi=mid
    b=(lo+hi)/2;s=2*(b-a)/h-p
    rho=residual(b,a,p,h,Q,S,beta)
    eta=(s*s-p*p)/2+V(b,Q,S,beta)-V(a,Q,S,beta)
    assert eta==2*(b-a)*rho/(h*h)
    assert residual(lo,a,p,h,Q,S,beta)<=0<=residual(hi,a,p,h,Q,S,beta)
    assert hi-lo<=h*h*B/F(2)**iterations
    return b,s,eta,lo,hi,rho

def Lmatrix(n,E,q,beta):
    L=[[C() for _ in range(n)] for _ in range(n)]
    for e,(f,t) in enumerate(E):
        hh=chi(q[e]);uu=U(q[e],beta[e])
        L[f][f]+=hh+uu;L[t][t]+=hh+uu
        L[f][t]-=C(hh);L[t][f]-=C(hh)
    return L

def field(u,q,beta,tau,E):
    n=len(u);L=Lmatrix(n,E,q,beta);unit=eye(n)
    Cinv=inv([[unit[i][j]+I*tau*L[i][j]/2 for j in range(n)] for i in range(n)])
    rhs=mv([[unit[i][j]-I*tau*L[i][j]/2 for j in range(n)] for i in range(n)],u)
    v=mv(Cinv,rhs)
    assert sum(z.norm() for z in v)==sum(z.norm() for z in u)
    assert quad(v,L)==quad(u,L)
    mid=[(a+b)/2 for a,b in zip(u,v)];delta=[F(0)]*n
    for e,(f,t) in enumerate(E):
        J=2*tau*chi(q[e])*(mid[f].conj()*mid[t]).i
        delta[f]-=J;delta[t]+=J
    assert [b.norm()-a.norm() for a,b in zip(u,v)]==delta
    return v

def energy(u,q,p,beta,E):return sum(z*z/2 for z in p)+quad(u,Lmatrix(len(u),E,q,beta))/2

bounds=scalar=0
for k in range(-32,33):
    q=F(k,8)
    for beta in (F(1,2),F(1),F(4)):
        assert abs(cp(q))<=F(15,8) and abs(cpp(q))<=15
        assert abs(Up(q,beta))<=2*beta and abs(Upp(q,beta))<=4*beta
        bounds+=1
for a in (F(-1),F(0),F(1,4),F(1)):
    for p in (F(-1,4),F(0),F(1,2)):
        for Q in (F(0),F(1,4),F(1,2)):
            for S in (F(1),F(2)):
                for beta in (F(1,2),F(1)):
                    gate(a,p,F(1,32),Q,S,beta);scalar+=1

# Exact root and noncanonical determinant witness, including both field halves.
a=F(0);b=F(1,4);h=F(1,2);p0=F(16,41);p1=F(25,41)
Q=F(0);S=F(2);beta=F(1,2)
d=DD(a,b,Q,S,beta)
assert residual(b,a,p0,h,Q,S,beta)==0
assert b-a==h*(p0+p1)/2 and p1-p0==-h*d
Da=(d-Vp(a,Q,S,beta))/(b-a);Db=(Vp(b,Q,S,beta)-d)/(b-a)
det=(1+h*h*Da/2)/(1+h*h*Db/2)
assert det==F(6929,6920)
u=[C(1),C(1)];E2=[(0,1)]
uA=field(u,[a],[beta],h/2,E2)
assert (uA[0]-uA[1]).norm()==0 and sum(z.norm() for z in uA)==2
uB=field(uA,[b],[beta],h/2,E2)
assert energy(u,[a],[p0],[beta],E2)==energy(uB,[b],[p1],[beta],E2)==F(1937,3362)

# Complete 8-contact overlapping-carrier step: computed roots have explicit defects.
E=[(0,7),(0,8),(1,7),(2,8),(3,7),(4,8),(5,7),(6,8)]
u=[C(1) for _ in range(9)];q=[F(0)]*8;p=[F(0)]*8;betas=[F(1,2)]*8;h=F(1,16)
assert h*h*(15+2*max(betas))*sum(z.norm() for z in u)<4
H0=energy(u,q,p,betas,E);assert H0==4
uA=field(u,q,betas,h/2,E)
qn=[];pn=[];receipts=[];etas=[]
for e,(f,t) in enumerate(E):
    Q=(uA[f]-uA[t]).norm()/2;S=uA[f].norm()+uA[t].norm()
    b,s,eta,lo,hi,rho=gate(q[e],p[e],h,Q,S,betas[e])
    qn.append(b);pn.append(s);etas.append(eta)
    receipts.append({'contact':e,'q_lower':str(lo),'q_upper':str(hi),'q_approx':str(b),'scalar_root_residual':str(rho),'momentum_equation_residual':str(2*rho/h),'energy_defect':str(eta)})
assert energy(uA,qn,pn,betas,E)-H0==sum(etas)
uN=field(uA,qn,betas,h/2,E)
H1=energy(uN,qn,pn,betas,E)
assert H1-H0==sum(etas)
assert sum(z.norm() for z in uN)==9
assert sum(z*z/2 for z in pn)<=H0+sum(abs(z) for z in etas)
assert abs(H1-H0)<F(1,2**35)
assert all(qn[i]==qn[i^1] and pn[i]==pn[i^1] for i in (0,2,4,6))
Path(__file__).with_name('ROOT_INTERVALS.json').write_text(json.dumps({'steps':1,'iterations_per_gate_max':40,'arithmetic':'exact rational endpoints and defects','receipts':receipts},indent=2)+'\n')
out={'status':'PASS_CONDITIONAL_FULL_ENERGY_NORM_METHOD_WITH_ROOT_RECEIPTS','global_profile_bound_controls':bounds,'scalar_root_bracket_and_energy_receipts':scalar,'exact_full_step_witness_energy':'1937/3362','exact_full_step_noncanonical_determinant':str(det),'overlapping_network_steps':1,'overlapping_network_gates':8,'network_combined_norm':9,'network_initial_H':4,'network_energy_change_bound':'abs(H1-H0)<2^-35; exact value equals sum root energy defects','all_root_intervals_and_defects':'ROOT_INTERVALS.json','reflection_paired_gate_results':True,'exact_mathematical_roots_imply_energy_conservation':True,'computed_network_roots_are_approximate':True,'computed_field_linear_solves':'exact Gaussian rational','symplectic':False,'bounded_local_field_event':False,'physical_time_or_priority_rule':False,'archived_scripts_executed':False,'independent_review':False,'physical_promotion':0}
Path(__file__).with_name('RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
