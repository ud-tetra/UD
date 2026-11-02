#!/usr/bin/env python3
"""Minimal exact K4/Q63 and 1->4 topological-rank smoke test. Full source in local ZIP."""
from itertools import combinations
import sympy as s
def incidence(tets):
  T=[sorted(set(c for t in tets for c in combinations(t,k+1))) for k in range(4)]
  M=[]
  for k in (1,2,3):
    I={a:i for i,a in enumerate(T[k-1])}
    Z=s.zeros(len(T[k-1]),len(T[k]))
    for j,t in enumerate(T[k]):
      for i in range(k+1):Z[I[t[:i]+t[i+1:]],j]=(-1)**i
    M.append(Z)
  assert M[0]*M[1]==s.zeros(M[0].rows,M[1].cols)
  assert M[1]*M[2]==s.zeros(M[1].rows,M[2].cols)
  rank=[m.rank() for m in M]
  beta=[len(T[0])-rank[0],len(T[1])-rank[0]-rank[1],len(T[2])-rank[1]-rank[2],len(T[3])-rank[2]]
  return [len(a) for a in T],rank,beta
T=[]
for i in range(4):
 j=(i+1)%4
 for u in ((i,j,4+j),(i,4+j,4+i)):
  a,b,c=sorted(u)
  T.extend([tuple(sorted(t)) for t in [(a,a+8,b+8,c+8),(a,b,b+8,c+8),(a,b,c,c+8)]])
T=sorted(T); first=T[0]
C=sorted(T[1:]+[tuple(sorted((16,)+tuple(first[j] for j in range(4) if j!=k))) for k in range(4)])
assert incidence(T)==([16,56,64,24],[15,40,24],[1,1,0,0])
assert incidence(C)==([17,60,70,27],[16,43,27],[1,1,0,0])
theta,chi=s.symbols('theta chi',real=True)
K=s.exp(s.I*chi)*s.cos(theta)
assert s.simplify(K.subs(theta,s.pi/2))==0
assert s.simplify(s.conjugate(K)*K+s.sin(theta)**2-1)==0
print('PASS: source-scope K4 env null and 27-tet Betti smoke check; physical promotion 0')
