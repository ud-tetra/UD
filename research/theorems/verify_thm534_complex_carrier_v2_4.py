#!/usr/bin/env python3
"""THM-534 v2.4 complex-carrier finite numerical network controls. NumPy only."""
import numpy as np
from itertools import product
rng=np.random.default_rng(53424)
D=np.array([[-1,1],[1,0],[0,-1],[-1,0],[0,1],[1,0],[0,-1]],float)
contacts=[(f,7+c,d) for f in range(7) for c in range(2) if (d:=D[f,c])!=0]
A=[];P=[]
for f,t,d in contacts:
    a=np.zeros((9,9));a[f,t]=-d;a[t,f]=d
    p=np.zeros((9,9));p[f,f]=p[t,t]=1
    A.append(a);P.append(p)
def gate(q):
    if q<=0:return (0.,0.)
    if q>=1:return (1.,0.)
    return 10*q**3-15*q**4+6*q**5,30*q*q-60*q**3+30*q**4
def potential(q,b):
    return 2*b/(1+(q+1)**2), -4*b*(q+1)/(1+(q+1)**2)**2
min_eig=10.;maxerr=0.
for bits in product((0,1),repeat=8):
    a=sum((bits[k]*A[k] for k in range(8)),np.zeros((9,9)))
    v=float(np.linalg.eigvalsh(4*np.eye(9)+1j*a)[0])
    min_eig=min(min_eig,v)
    assert v>-1e-12
for _ in range(250):
    q=rng.uniform(-.3,1.3,8);beta=rng.uniform(.25,2,8)
    p=rng.normal(size=8)
    psi=(rng.normal(size=9)+1j*rng.normal(size=9))/3
    chi=np.array([gate(u)[0] for u in q]);chip=np.array([gate(u)[1] for u in q])
    u=np.array([potential(z,b)[0] for z,b in zip(q,beta)])
    up=np.array([potential(z,b)[1] for z,b in zip(q,beta)])
    a=sum((chi[k]*A[k] for k in range(8)),np.zeros((9,9)))
    w=sum((u[k]*P[k]/2 for k in range(8)),np.zeros((9,9)))
    g=4*np.eye(9)+1j*a+w
    psidot=-1j*g@psi
    pdot=np.array([-chip[k]*np.vdot(psi,1j*A[k]@psi).real
                   -up[k]/2*np.vdot(psi,P[k]@psi).real for k in range(8)])
    dH=2*np.vdot(psidot,g@psi).real+sum(p[k]*(pdot[k]+chip[k]*np.vdot(psi,1j*A[k]@psi).real
                   +up[k]/2*np.vdot(psi,P[k]@psi).real) for k in range(8))
    dN=2*np.vdot(psi,psidot).real
    observed=2*np.real(np.conj(psi)*psidot)
    expected=2*np.real(np.conj(psi)*(a@psi))
    maxerr=max(maxerr,abs(dH),abs(dN),np.max(abs(observed-expected)))
    assert np.vdot(psi,g@psi).real>=-1e-12
assert maxerr<2e-12
print("PASS 256 Hermitian binary spectrum checks, min eigenvalue:",min_eig)
print("PASS 250 complex continuous gate energy/norm/local-current controls, max error:",maxerr)
print("Complex-carrier alternative CONDITIONAL; physical promotion 0")
