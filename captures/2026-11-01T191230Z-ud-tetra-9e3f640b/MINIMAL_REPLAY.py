#!/usr/bin/env python3
"""Small independent-replay kernel for UD signed-reference gate v0.1."""
import itertools as it
import sympy as S
T=[t for k in range(1,5) for t in it.combinations(range(4),k)]
I={t:i for i,t in enumerate(T)}
B=S.zeros(15)
for t in T:
    for j in range(len(t)):
        if len(t)>1: B[I[t[:j]+t[j+1:]],I[t]]+=(-1)**j
A=B.T-B; P=S.zeros(15)
for i in range(4):
    for j in range(4): P[i,j]=S.Rational(1,4)
assert B*B==S.zeros(15) and A*A==-4*(S.eye(15)-P)
r=S.eye(15)[:,4]+S.eye(15)[:,5]; q=(r.T*r)[0]
s=S.symbols('s',real=True)
X=S.cos(2*s)*r+S.sin(2*s)*A*r/2
u=S.trigsimp(((r.T*X)[0]+S.I*(A*r/2).dot(X))/q)
assert S.trigsimp(S.re(u)-S.cos(2*s))==0
assert S.trigsimp(S.im(u)-S.sin(2*s))==0
edges=T[4:10]; E={v:i for i,v in enumerate(edges)}
Rsum=S.zeros(6)
for perm in it.permutations(range(4)):
    R=S.zeros(6)
    for i,(a,b) in enumerate(edges):
        v=(perm[a],perm[b]); R[E[tuple(sorted(v))],i]=1 if v[0]<v[1] else -1
    Rsum+=R
assert Rsum==S.zeros(6)
y=S.symbols('y0:6'); div=B[:4,4:10]*S.Matrix(y)
cubic=S.expand(sum(a**3 for a in div))
assert cubic!=0 and S.expand(cubic.subs({yy:-yy for yy in y},simultaneous=True)+cubic)==0
t=S.symbols('t',real=True)
assert S.simplify(S.exp(S.I*(t+S.pi))+S.exp(S.I*t))==0
assert S.simplify(S.exp(2*S.I*(t+S.pi))-S.exp(2*S.I*t))==0
assert S.cos(S.pi/2)==S.cos(3*S.pi/2) and S.exp(S.I*S.pi/2)!=S.exp(3*S.I*S.pi/2)
lmb=S.symbols('lambda',positive=True)
zd=S.diff(lmb*S.exp(S.I*t)-S.exp(2*S.I*t),t)
assert S.simplify(zd/(S.I*S.exp(S.I*t))-(lmb-2*S.exp(S.I*t)))==0
print('PASS: K4 relative reference, S4 linear zero, odd cubic, Q83 and gain gate; physical promotion 0')
