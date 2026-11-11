#!/usr/bin/env python3
"""THM534 v0.9 compact exact verifier. Candidate reservoir gate != frozen UD chi."""
import itertools
import sympy as s
V=range(4); E=list(itertools.combinations(V,2)); F=list(itertools.combinations(V,3))
B=s.zeros(4,6);D=s.zeros(6,4)
for i,(u,v) in enumerate(E):B[u,i]=-1;B[v,i]=1
for i,face in enumerate(F):
    for k in range(3):D[E.index(face[:k]+face[k+1:]),i]=(-1)**k
assert B*D==s.zeros(4,4)
def update(x,r,beta=(1,1,1,1),tau=(1,)*6):
    chi=tuple(int(bool(r[v]>0)) for v in V)
    h=tuple(chi[u]*chi[v]*beta[u]*beta[v]*tau[e] for e,(u,v) in enumerate(E))
    j=-s.diag(*h)*B.T*x/4
    p=x+B*j
    src=(r-p)/4
    return p+src,r-src,j,D.T*j,h,p,src
x=s.Matrix([1,0,0,0]);r=s.Matrix([1,1,1,0])
xx,rr,j,F0,h,p,src=update(x,r)
assert h==(1,1,0,1,0,0)
assert list(F0)==[0,s.Rational(1,4),s.Rational(1,4),0]
assert list(xx)==[s.Rational(5,8),s.Rational(7,16),s.Rational(7,16),0]
assert list(rr)==[s.Rational(7,8),s.Rational(13,16),s.Rational(13,16),0]
assert list(src)==[s.Rational(1,8),s.Rational(3,16),s.Rational(3,16),0]
P=s.eye(4)-B*s.diag(*h)*B.T/4
assert P.eigenvals()=={s.Integer(1):2,s.Rational(1,4):2}
lp=(15+s.sqrt(97))/32;lm=(15-s.sqrt(97))/32
cp=(s.sqrt(97)-9)/(2*s.sqrt(97));cm=1-cp
for n in range(12):
    a=s.simplify(cp*lp**n+cm*lm**n)
    assert s.simplify(x[0]-x[1]-a)==0
    nx,nr,j,face,g,pre,ss=update(x,r)
    assert face==s.Matrix([0,a/4,a/4,0])
    mu=s.Rational(1,2)
    en=lambda u,v: sum((z-mu)**2 for z in list(u)+list(v))
    loss=s.simplify(en(x,r)-en(nx,nr))
    assert loss>=s.simplify((face.T*face)[0]+s.Rational(3,8)*sum((pre[i]-r[i])**2 for i in V))
    x,r=nx,nr
    assert g==h and sum(x)+sum(r)==4
count=0
for chi in itertools.product((0,1),repeat=4):
    reserve=s.Matrix(chi)
    for beta in itertools.product((0,1),repeat=4):
        for i in V:
            inp=s.eye(4)[:,i]
            for tau in ((1,)*6,(0,)*6,(1,0,1,0,1,0),(0,1,0,1,0,1)):
                nx,nr,edge,face,h,p,src=update(inp,reserve,beta,tau)
                assert all(t>=0 for t in nx) and all(t>=0 for t in nr)
                assert sum(nx)+sum(nr)==sum(inp)+sum(reserve)
                count+=1
assert count==4096
# Independent reversible rotor control, not Q162.
rot=s.Matrix([1,0,0,0])
for t in range(9):
    k=s.Matrix([rot[0],-rot[2],0,rot[1],0,0])
    assert (D.T*k)[0]==1
    rot=rot+B*k
    assert list(rot)==([1,0,0,0] if t%3==2 else [0,1,0,0] if t%3==0 else [0,0,1,0])
print("PASS: 4096 exact positive-stock controls, closed mask, contrast eigenvalues and rotor")
print("IMPORTANT: r>0 is availability proxy, not native UD geometric closure; physical promotion 0")
