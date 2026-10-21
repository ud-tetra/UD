#!/usr/bin/env python3
"""THM-534 v0.6 endogenous source-current feedback, finite 30-step numeric test."""
from itertools import combinations
import numpy as np
from scipy.linalg import solve
v=list(range(4));E=list(combinations(v,2));F=list(combinations(v,3))
B1=np.zeros((4,6),complex);B2=np.zeros((6,4),complex);B3=np.zeros((4,1),complex)
for k,(a,b) in enumerate(E):B1[a,k]=-1;B1[b,k]=1
for k,f in enumerate(F):
    for t in range(3):B2[E.index(f[:t]+f[t+1:]),k]=(-1)**t
for k in range(4):B3[F.index(tuple(v[:k]+v[k+1:])),0]=(-1)**k
e=E.index((1,2));f=F.index((0,1,2));q=B2[e,f]
def gen(z):
    N=B2.copy();N[e,f]=q*z
    A=np.zeros((15,15),complex)
    for i,k,B in ((0,4,B1),(4,10,N),(10,14,B3)):
        A[i:i+B.shape[0],k:k+B.shape[1]]=B
        A[k:k+B.shape[1],i:i+B.shape[0]]=-B.conj().T
    return A
def jread(p):
    return float(2*np.imag(np.conj(p[4+e])*q*p[10+f]))
h=0.1;I=np.eye(15)
p=np.zeros(15,complex);p[4+e]=1/np.sqrt(2);p[10+f]=1j*q/np.sqrt(2)
assert abs(jread(p)-1)<1e-15
maxres=0; js=[]
for n in range(30):
    j=jread(p);js.append(j)
    z=(3+1j*j)/np.sqrt(9+j*j)
    A=gen(z)
    nxt=solve(I-h*A/2,(I+h*A/2)@p)
    mid=(p+nxt)/2
    for a in range(15):
        lhs=abs(nxt[a])**2-abs(p[a])**2
        rhs=sum(2*h*np.real(np.conj(mid[a])*A[a,b]*mid[b]) for b in range(15))
        maxres=max(maxres,abs(lhs-rhs))
    p=nxt
assert abs(np.vdot(p,p)-1)<1e-13 and maxres<7e-16
assert all(abs(j)>0.01 for j in js)
# Real initial condition remains exactly flat within floating error.
r=np.zeros(15,complex);r[4+e]=1
for _ in range(10):
    assert abs(jread(r))<1e-14
    A=gen(1)
    r=solve(I-h*A/2,(I+h*A/2)@r)
    assert np.max(np.abs(r.imag))<1e-14
print("PASS: 30 endogenous-current Cayley steps, nonzero sourced phase")
print("PASS: 15-component local continuity, max residual",maxres)
print("PASS: all-real control remains source-free for 10 steps")
print("NO CLAIM: source rule from native UD action or physical burden conservation")
