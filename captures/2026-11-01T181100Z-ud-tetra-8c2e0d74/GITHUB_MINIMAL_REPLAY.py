#!/usr/bin/env python3
"""Compact exact K4 source-stock/flow observer replay, no empirical parameters."""
from itertools import combinations
import sympy as S

basis=[tuple(t) for k in range(4) for t in combinations(range(4),k+1)]
idx={t:i for i,t in enumerate(basis)}
B=S.zeros(15)
for t in basis:
    for j in range(len(t)):
        if len(t)>1:B[idx[t[:j]+t[j+1:]],idx[t]]+=(-1)**j
A=B.T-B
P0=S.zeros(15)
for i in range(4):
    for j in range(4):P0[i,j]=S.Rational(1,4)
assert B*B==S.zeros(15)
assert A*A==-4*(S.eye(15)-P0)
e=S.eye(15)[:,idx[(0,1)]]
s=S.symbols('s',real=True)
X=S.cos(2*s)*e+S.sin(2*s)*A*e/2
x0,x1,x2=X[:4,:],X[4:10,:],X[10:14,:]
B1,B2=B[:4,4:10],B[4:10,10:14]
S1=S.trigsimp((x1.T*x1)[0])
J01=S.trigsimp(2*(x1.T*B1.T*x0)[0])
J12=S.trigsimp(2*(x2.T*B2.T*x1)[0])
assert S.trigsimp(S1-S.cos(2*s)**2)==0
assert S.trigsimp(J12-J01-2*S.sin(4*s))==0
W=2*S1-1+S.I*(J12-J01)/2
assert S.trigsimp(S.re(W)-S.cos(4*s))==0
assert S.trigsimp(S.im(W)-S.sin(4*s))==0
print('PASS: Q165/Q166/Q169/Q170 native quadratic readout; physical promotion 0')
