#!/usr/bin/env python3
"""Compact exact K4 Q169 graded transfer and divergence-observer kernel."""
from itertools import combinations
import sympy as s
V=range(4)
C=[list(combinations(V,k+1)) for k in range(4)]
I=[{f:i for i,f in enumerate(c)} for c in C];off=[0,4,10,14,15]
B=s.zeros(15)
for k in range(1,4):
    for j,f in enumerate(C[k]):
        for a in range(k+1):B[off[k-1]+I[k-1][f[:a]+f[a+1:]],off[k]+j]=(-1)**a
A=B.T-B;P0=s.zeros(15)
for i in range(4):
    for j in range(4):P0[i,j]=s.Rational(1,4)
assert B*B==s.zeros(15) and A*A==-4*(s.eye(15)-P0)
P=s.diag(*([0]*4+[1]*6+[0]*5));assert A*P!=P*A
x=s.Matrix([0]*4+[1,2,3,4,5,6]+[0]*5)
t=s.symbols('t',real=True);q=(x.T*x)[0];assert q==91
Y=s.cos(2*t)*x+s.sin(2*t)*A*x/2
assert s.trigsimp((Y.T*P*Y)[0]-q*s.cos(2*t)**2)==0
assert s.trigsimp((Y.T*(s.eye(15)-P)*Y)[0]-q*s.sin(2*t)**2)==0
B1=B[:4,4:10];B2=B[4:10,10:14];assert B1*B2==s.zeros(4,4)
assert B1*(x[4:10,:]+B2[:,0])==B1*x[4:10,:]
print('PASS: exact K4 source exchange and observer kernel; physical promotion 0')
