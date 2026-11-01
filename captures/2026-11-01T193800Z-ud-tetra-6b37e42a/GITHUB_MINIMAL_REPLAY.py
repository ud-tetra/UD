#!/usr/bin/env python3
"""Compact exact Q81/odd-observer gate checks; full graded proofs in local ZIP."""
import sympy as s
from itertools import combinations

def carrier(tets):
    C=[sorted(set(a for t in tets for a in combinations(t,k+1))) for k in range(3)]
    D=[]
    for k in (1,2):
        I={t:i for i,t in enumerate(C[k-1])}
        m=s.zeros(len(C[k-1]),len(C[k]))
        for j,t in enumerate(C[k]):
            for i in range(len(t)):m[I[t[:i]+t[i+1:]],j]=(-1)**i
        D.append(m)
    B1,B2=D
    assert B1*B2==s.zeros(B1.rows,B2.cols)
    L=B1.T*B1+B2*B2.T
    x=s.Matrix(range(1,len(C[1])+1))
    lam=sorted(L.eigenvals())
    P={}
    for a in lam:
        z=s.eye(L.rows)
        for b in lam:
            if b!=a:z=z*(L-b*s.eye(L.rows))/(a-b)
        P[a]=z
    for a in lam:
        assert L*P[a]==a*P[a]
    return B1,L,x,P

k4=carrier([(0,1,2,3)])
km=carrier([(0,1,2,3),(0,1,2,4)])
kp=carrier([(0,1,3,4),(0,2,3,4),(1,2,3,4)])
assert k4[1].eigenvals()=={4:6}
assert km[1].eigenvals()=={3:3,5:6}
assert kp[1].eigenvals()=={2:1,5:9}
assert kp[0]*kp[3][2]==s.zeros(kp[0].rows,kp[1].cols)
assert (kp[3][2]*kp[2]).dot(kp[3][2]*kp[2])==s.Rational(16,3)
for B1,L,x,P in (k4,km,kp):
    cubic=sum(v**3 for v in B1*x)
    assert sum(v**3 for v in B1*(-x))==-cubic
    for a in P:
        assert P[a].T==P[a] and P[a]*P[a]==P[a]

p,G=s.symbols('p G',real=True)
K=p*s.exp(-s.I*G)+(1-p)*s.exp(s.I*G)
assert s.simplify(s.expand_complex(K)-(s.cos(G)-s.I*(2*p-1)*s.sin(G)))==0
assert s.trigsimp(s.expand_complex(K*s.conjugate(K))-(s.cos(G)**2+(2*p-1)**2*s.sin(G)**2))==0
print('PASS exact K4 Kminus Kplus observer-dark mode and Q63 context; physical promotion 0')
