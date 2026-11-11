#!/usr/bin/env python3
"""Finite numerical stress for conditional S18/S19 time-varying gate masks.

This is not a native gate-selection rule or physical experiment.
"""
from itertools import combinations
import numpy as np
V=range(4); E=list(combinations(V,2));F=list(combinations(V,3))
B1=np.zeros((4,6));B2=np.zeros((6,4));B3=np.zeros((4,1))
for k,(u,v) in enumerate(E):B1[u,k]=-1;B1[v,k]=1
for i,f in enumerate(F):
    for k in range(3):B2[E.index(f[:k]+f[k+1:]),i]=(-1)**k
for k in range(4):B3[F.index(tuple(v for v in V if v!=k)),0]=(-1)**k
assert np.max(abs(B1@B2))==0 and np.max(abs(B2@B3))==0
rng=np.random.default_rng(534070)
max_mass=0.; max_bianchi=0.; max_hodge=0.; max_var_up=0.
nonzero_curl=0; steps=0
for run in range(8):
    r=rng.random(4);r=r/r.sum();base=r.sum()
    for k in range(128):
        h=rng.integers(0,2,6);H=np.diag(h)
        j=-.25*H@B1.T@r
        after=r+B1@j
        curl=B2.T@j
        delta=B1@j
        varold=np.sum((r-r.mean())**2)
        varnew=np.sum((after-after.mean())**2)
        max_var_up=max(max_var_up,varnew-varold)
        max_mass=max(max_mass,abs(after.sum()-base))
        max_bianchi=max(max_bianchi,np.max(abs(B3.T@curl)))
        max_hodge=max(max_hodge,abs(4*np.dot(j,j)-np.dot(delta,delta)-np.dot(curl,curl)))
        assert after.min() >= -1e-14
        if np.linalg.norm(curl)>1e-12:nonzero_curl+=1
        steps+=1;r=after
assert max_mass<1e-13 and max_bianchi<1e-13 and max_hodge<1e-13 and max_var_up<1e-13
assert nonzero_curl>0
print('PASS',steps,'variable-mask numerical steps, nonzero curl cases',nonzero_curl)
print('max mass error',max_mass,'max cochain closure error',max_bianchi)
print('max Hodge mismatch',max_hodge,'max variance increase',max_var_up)
print('STATUS numerical constructor scope only; gate dynamics/physical phase source OPEN')
