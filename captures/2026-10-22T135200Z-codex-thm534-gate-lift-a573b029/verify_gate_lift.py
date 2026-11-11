"""Fresh exact constructor checks of a conditional canonical gate extension."""
from fractions import Fraction as F
from itertools import combinations,permutations,product
from pathlib import Path
import json

def chi(q):
    if q<=0:return F(0)
    if q>=1:return F(1)
    return 10*q**3-15*q**4+6*q**5
def chip(q):return 30*q*q*(1-q)**2 if 0<q<1 else F(0)
CELLS=[(0,1,2,3),(0,1,2,4)]
FACES=sorted(set(combinations(CELLS[0],3))|set(combinations(CELLS[1],3)))
D=[[0,0] for _ in FACES]
for j,c in enumerate(CELLS):
    for k in range(4):D[FACES.index(c[:k]+c[k+1:])][j]=(1,-1)[j]*(-1)**k
CONTACTS=[(f,j) for f in range(7) for j in range(2) if D[f][j]]
def norm(x):return sum(v*v for v in x)
def angular(x,y,e):
    f,j=CONTACTS[e];k=7+j;return D[f][j]*(y[k]*x[f]-y[f]*x[k])
def apply(x,h):
    out=[F(0)]*9
    for e,(f,j) in enumerate(CONTACTS):
        d=D[f][j];k=7+j;out[f]-=d*h[e]*x[k];out[k]+=d*h[e]*x[f]
    return out
def energy(x,y,q,p):return norm(p)/2+sum(chi(q[e])*angular(x,y,e) for e in range(8))
def field(x,y,q,p):
    h=list(map(chi,q));dx=apply(x,h);dy=apply(y,h)
    dq=p[:];dp=[-chip(q[e])*angular(x,y,e) for e in range(8)]
    return dx,dy,dq,dp
def audit(x,y,q,p):
    dx,dy,dq,dp=field(x,y,q,p)
    assert sum(a*b for a,b in zip(x,dx))==sum(a*b for a,b in zip(y,dy))==0
    # Canonical gradient: H_x=-A y, H_y=A x, H_q=chi' ell, H_p=p.
    dh=-sum(a*b for a,b in zip(dy,dx))+sum(a*b for a,b in zip(dx,dy))
    dh+=sum(chip(q[e])*angular(x,y,e)*dq[e]+p[e]*dp[e] for e in range(8))
    assert dh==0
    currents=[2*D[f][j]*chi(q[e])*x[f]*x[7+j] for e,(f,j) in enumerate(CONTACTS)]
    for f in range(7):assert 2*x[f]*dx[f]==-sum(currents[e] for e,(ff,j) in enumerate(CONTACTS) if ff==f)
    for j in range(2):
        assert 2*x[7+j]*dx[7+j]==sum(currents[e] for e,(f,jj) in enumerate(CONTACTS) if jj==j)
        owned=2*x[7+j]*dx[7+j];receipt=F(0)
        for f in range(7):
            w=F(int(D[f][j]!=0),sum(int(v!=0) for v in D[f]));owned+=w*2*x[f]*dx[f]
            receipt+=sum(currents[e]*(int(jj==j)-w) for e,(ff,jj) in enumerate(CONTACTS) if ff==f)
        assert owned==receipt
    return dx,dy,dq,dp
states=[]
for seed in range(64):
    x=[F(i+1-seed%5,7) for i in range(9)];y=[F(2*i-seed%7,9) for i in range(9)]
    q=[F((seed+e)%7-1,4) for e in range(8)];p=[F((seed+2*e)%5-2,3) for e in range(8)]
    audit(x,y,q,p);states.append((x,y,q,p))
x,y,_,_=states[1]
for bits in product((0,1),repeat=8):
    q=[F(2) if b else F(-1) for b in bits];p=[F(0)]*8
    dx,dy,dq,dp=audit(x,y,q,p)
    assert dx==apply(x,bits) and dy==apply(y,bits) and dq==dp==[0]*8
assert field(x,y,[F(-1)]*8,[F(0)]*8)==([0]*9,[0]*9,[0]*8,[0]*8)
# Omitting gate backreaction loses total Hamiltonian conservation.
assert chip(F(1,2))*F(1)*F(2)==F(15,4)
# Fixed support alone does not fix a switching-energy receipt.
assert angular([F(1)]+[F(0)]*8,[F(0)]*9,0)==0
# A private contact d=+1: x=(1,0), dual=(0,1) has ell=1; dual=0 has ell=0.
sx=[F(0)]*9;sy=[F(0)]*9;sx[1]=1;sy[7]=1;private=CONTACTS.index((1,0))
assert angular(sx,sy,private)==1 and angular(sx,[F(0)]*9,private)==0
commutator_checks=0;changing_angular_controls=0
for xx,yy,qq,pp in states:
    hh=list(map(chi,qq));dx,dy,_,_=field(xx,yy,qq,pp)
    for e in range(8):
        unit=[F(int(i==e)) for i in range(8)];ex=apply(xx,unit)
        rate=sum(a*b for a,b in zip(dy,ex))+sum(a*b for a,b in zip(yy,apply(dx,unit)))
        comm=sum(yy[i]*(apply(dx,unit)[i]-apply(ex,hh)[i]) for i in range(9))
        assert rate==comm;commutator_checks+=1
        if rate:changing_angular_controls+=1
assert changing_angular_controls>0
# Positive-margin crossing certificate; each sample stands for any ell in [-B,B].
margin_checks=0
for pmin in (F(3,2),F(2),F(3)):
    for bound in (F(1,2),F(1),F(2)):
        delta=pmin*pmin/2-bound
        if delta<=0:continue
        for ell,q in product((-bound,F(0),bound),[F(i,16) for i in range(17)]):
            assert pmin*pmin-2*ell*chi(q)>=2*delta>0;margin_checks+=1
delta=F(15,8)**2/2-F(9,8)**2
assert delta==F(63,128) and F(121,63)<F(121,49)
# Gate profile facts and a distinct equally admissible control profile.
for q in [F(i,32) for i in range(33)]:
    assert 0<=chi(q)<=1 and 0<=chip(q)<=F(15,8)
assert chi(F(1,4))!=3*F(1,4)**2-2*F(1,4)**3

# Exact forward automatic differentiation for the six-coordinate finite map.
class Dual:
    def __init__(self,v,g=None):self.v=F(v);self.g=tuple(g or [F(0)]*6)
    def __add__(self,b):
        b=asdual(b);return Dual(self.v+b.v,[a+c for a,c in zip(self.g,b.g)])
    __radd__=__add__
    def __neg__(self):return Dual(-self.v,[-a for a in self.g])
    def __sub__(self,b):return self+-asdual(b)
    def __rsub__(self,b):return asdual(b)+-self
    def __mul__(self,b):
        b=asdual(b);return Dual(self.v*b.v,[a*b.v+c*self.v for a,c in zip(self.g,b.g)])
    __rmul__=__mul__
    def __truediv__(self,b):
        b=asdual(b);return Dual(self.v/b.v,[(a*b.v-c*self.v)/(b.v*b.v) for a,c in zip(self.g,b.g)])
    def __rtruediv__(self,b):return asdual(b)/self
    def __pow__(self,n):
        if n==0:return Dual(1)
        return Dual(self.v**n,[n*self.v**(n-1)*a for a in self.g])
def asdual(v):return v if isinstance(v,Dual) else Dual(v)
def profile_ad(q):
    if q.v<=0:return Dual(0),Dual(0)
    if q.v>=1:return Dual(1),Dual(0)
    return 10*q**3-15*q**4+6*q**5,30*q*q*(1-q)**2
EPS=F(1,4)
def finite(values,d=1,kick=True):
    z=[Dual(v,[F(int(i==j)) for j in range(6)]) for i,v in enumerate(values)]
    f,t,u,v,q,p=z;h,hp=profile_ad(q);b=EPS*h/2;c=(1-b*b)/(1+b*b);s=2*b/(1+b*b)
    ell=d*(v*f-u*t);reaction=EPS*hp/(1+b*b)*ell
    out=[c*f-d*s*t,d*s*f+c*t,c*u-d*s*v,d*s*u+c*v,q,p-reaction if kick else p]
    return [a.v for a in out],[list(a.g) for a in out]
OMEGA=[[F(0)]*6 for _ in range(6)]
for i,j in ((0,2),(1,3),(4,5)):OMEGA[i][j]=1;OMEGA[j][i]=-1
def symplectic(a):
    return all(sum(a[k][i]*OMEGA[k][l]*a[l][j] for k in range(6) for l in range(6))==OMEGA[i][j] for i in range(6) for j in range(6))
finite_checks=0
for seed,q,d in product(range(8),(F(-1),F(0),F(1,4),F(1,2),F(3,4),F(1),F(2)),(-1,1)):
    values=[F(seed+1,3),F(2-seed,5),F(seed-1,7),F(seed+2,4),q,F(2)]
    out,jac=finite(values,d);assert symplectic(jac)
    assert out[0]**2+out[1]**2==values[0]**2+values[1]**2
    assert out[2]**2+out[3]**2==values[2]**2+values[3]**2
    finite_checks+=1
control=[F(1),F(0),F(0),F(1),F(1,2),F(2)]
out,jac=finite(control);bad,jbad=finite(control,kick=False)
assert not symplectic(jbad) and out[5]==F(394,257)
assert out[:4]==[F(255,257),F(32,257),F(-32,257),F(255,257)]
assert (out[5]**2-control[5]**2)/2==F(-54480,66049)

def parity(s):return (-1)**sum(s[i]>s[j] for i in range(len(s)) for j in range(i+1,len(s)))
covariance=0
for pp in permutations((0,1,2)):
    for tips in ((3,4),(4,3)):
        perm=pp+tips;qmap=[];sign=[]
        for f in FACES:
            mapped=tuple(perm[v] for v in f);qmap.append(FACES.index(tuple(sorted(mapped))));sign.append(parity(mapped))
        for j,c in enumerate(CELLS):
            mapped=tuple(perm[v] for v in c);k=CELLS.index(tuple(sorted(mapped)));qmap.append(7+k);sign.append((1,-1)[j]*parity(mapped)*(1,-1)[k])
        emap=[CONTACTS.index((qmap[f],qmap[7+j]-7)) for f,j in CONTACTS]
        def move(a):
            out=[F(0)]*9
            for i in range(9):out[qmap[i]]=sign[i]*a[i]
            return out
        def movegate(a):
            out=[F(0)]*8
            for i in range(8):out[emap[i]]=a[i]
            return out
        for x,y,q,p in states:
            nx,ny,nq,np=move(x),move(y),movegate(q),movegate(p)
            assert energy(nx,ny,nq,np)==energy(x,y,q,p)
            dx,dy,dq,dp=field(x,y,q,p)
            assert field(nx,ny,nq,np)==(move(dx),move(dy),movegate(dq),movegate(dp));covariance+=1
RESULT={'status':'PASS_EXACT_CONDITIONAL_ENLARGED_CANONICAL_GATE_MODEL','continuous_hamiltonian_receipt_controls':len(states),'plateau_mask_controls':256,'signed_extended_covariance_checks':covariance,'finite_canonical_map_jacobian_checks':finite_checks,'readiness_margin_controls':margin_checks,'angular_commutator_controls':commutator_checks,'nonconstant_network_angular_controls':changing_angular_controls,'omitted_reaction_energy_derivative_witness':'15/4','finite_gate_momentum_after':'394/257','finite_contact_substep_full_H_defect':'-54480/66049','uncertain_preparation_margin':'63/128','off_plateau_at_rest_absorbing':True,'zero_dual_allows_zero_switching_work':True,'finite_substep_not_full_H_integrator':True,'extended_Kminus_state_dimension':34,'native_gate_registers_and_profile':'OPEN','global_norm_readiness_bound_not_local_source_law':True,'reset_and_reuse':'OPEN','outside_peer_review':False,'physical_promotion':0}
if __name__=='__main__':
    (Path(__file__).parent/'RESULTS.json').write_text(json.dumps(RESULT,indent=2)+'\n');print(json.dumps(RESULT,indent=2))
