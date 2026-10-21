#!/usr/bin/env python3
"""THM-534 v0.6 exact conditional source-to-curvature and full-content Cayley verifier."""
from itertools import combinations
import sympy as s
v=list(range(4)); edges=list(combinations(v,2)); faces=list(combinations(v,3))
B1=s.zeros(4,6);B2=s.zeros(6,4);B3=s.zeros(4,1)
for i,(a,b) in enumerate(edges): B1[a,i]=-1;B1[b,i]=1
for i,f in enumerate(faces):
    for k in range(3): B2[edges.index(f[:k]+f[k+1:]),i]=(-1)**k
for i in range(4): B3[faces.index(tuple(v[:i]+v[i+1:])),0]=(-1)**i
assert B1*B2==s.zeros(4,4) and B2*B3==s.zeros(6,1)
assert B1.T*B1+B2*B2.T==4*s.eye(6)
e=edges.index((1,2));f=faces.index((0,1,2));q=B2[e,f]
j=s.symbols('j',real=True)
z=(3+s.I*j)/s.sqrt(9+j**2)
N=B2.copy();N[e,f]=q*z
Fdown=B1*N;Fup=N*B3
assert B1*Fup==Fdown*B3  # S16 exact sourced-defect compatibility square
assert s.simplify(z*s.conjugate(z))==1
assert s.simplify(Fdown.norm()**2-2*(z-1)*s.conjugate(z-1))==0
assert s.simplify(Fup.norm()**2-(z-1)*s.conjugate(z-1))==0
assert s.simplify((Fdown.norm()**2+Fup.norm()**2)/2-3*(1-3/s.sqrt(9+j*j)))==0
assert s.simplify(3*(1-3/s.sqrt(9+j*j))-j*j/s.sqrt(9+j*j)-(3-s.sqrt(9+j*j)))==0
N=N.subs(j,4);Fdown=B1*N;Fup=N*B3
assert s.simplify(Fdown.norm()**2-s.Rational(8,5))==0
assert s.simplify(Fup.norm()**2-s.Rational(4,5))==0
A=s.zeros(15)
for i,k,B in ((0,4,B1),(4,10,N),(10,14,B3)):
    A[i:i+B.rows,k:k+B.cols]=B
    A[k:k+B.cols,i:i+B.rows]=-B.conjugate().T
assert A.conjugate().T==-A
h=s.Rational(1,2)
C=(s.eye(15)-h*A/2).inv()*(s.eye(15)+h*A/2)
assert s.simplify(C.conjugate().T*C-s.eye(15))==s.zeros(15)
p0=s.zeros(15,1);p0[4+e,0]=1
p1=C*p0;mid=(p0+p1)/2
for a in range(15):
    change=s.conjugate(p1[a])*p1[a]-s.conjugate(p0[a])*p0[a]
    inflow=sum(h*(s.conjugate(mid[a])*A[a,b]*mid[b]+mid[a]*s.conjugate(A[a,b])*s.conjugate(mid[b])) for b in range(15))
    assert s.simplify(change-inflow)==0
assert s.simplify(sum(s.conjugate(x)*x for x in p1)-1)==0
print("PASS: exact S10 source curvature and j=4 receipt 8/5+4/5")
print("PASS: exact S11 full 15-dimensional Cayley norm and all 15 local flux receipts")
print("Physical packet-burden continuity OPEN; no THM-534 stochastic readout derived.")
