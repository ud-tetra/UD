#!/usr/bin/env python3
"""THM-534 v0.6.1 source-quadrature norm-bound stress; finite numerical control."""
from itertools import combinations
import numpy as np
from scipy.linalg import solve
V=list(range(4));E=list(combinations(V,2));F=list(combinations(V,3))
B1=np.zeros((4,6),complex);B2=np.zeros((6,4),complex);B3=np.zeros((4,1),complex)
for k,(a,b) in enumerate(E):B1[a,k]=-1;B1[b,k]=1
for k,f in enumerate(F):
    for t in range(3):B2[E.index(f[:t]+f[t+1:]),k]=(-1)**t
for k in range(4):B3[F.index(tuple(V[:k]+V[k+1:])),0]=(-1)**k
e=E.index((1,2));f=F.index((0,1,2));q=B2[e,f]
def A(z):
    N=B2.copy();N[e,f]*=z
    out=np.zeros((15,15),complex)
    for a,b,M in ((0,4,B1),(4,10,N),(10,14,B3)):
        out[a:a+M.shape[0],b:b+M.shape[1]]=M
        out[b:b+M.shape[1],a:a+M.shape[0]]=-M.conj().T
    return out
rng=np.random.default_rng(534061)
maxlocal=maxnorm=maxq=maxcurv=0.
for trial in range(70):
    p=rng.normal(size=15)+1j*rng.normal(size=15)
    p/=np.linalg.norm(p)
    h=(0.03,0.2,0.7)[trial%3]
    for n in range(15):
        j=float(2*np.imag(np.conj(p[4+e])*q*p[10+f]))
        maxq=max(maxq,abs(j)); assert abs(j)<=1+2e-15
        z=(3+1j*j)/np.sqrt(9+j*j)
        maxcurv=max(maxcurv,2*abs(z-1)**2)
        H=A(z);I=np.eye(15)
        nxt=solve(I-h*H/2,(I+h*H/2)@p)
        mid=(p+nxt)/2
        delta=np.abs(nxt)**2-np.abs(p)**2
        flux=np.array([sum(2*h*np.real(np.conj(mid[a])*H[a,b]*mid[b]) for b in range(15)) for a in range(15)])
        maxlocal=max(maxlocal,float(np.max(np.abs(delta-flux))))
        maxnorm=max(maxnorm,abs(float(np.vdot(nxt,nxt).real)-1))
        p=nxt
assert maxcurv<=4*(1-3/np.sqrt(10))+3e-14
assert maxnorm<2e-12 and maxlocal<2e-13
print("PASS: 70 normalized complex initial states x 15 Cayley steps")
print("max norm drift",maxnorm,"max local flux residual",maxlocal)
print("max quadrature",maxq,"max lower curvature",maxcurv)
print("EXACT bound: |q|<=||psi||^2=1, lower curvature<=4(1-3/sqrt(10))")
print("Physical packet-burden correspondence OPEN")
