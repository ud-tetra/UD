"""New exact rational P1 refinement and damping checks; no third-party packages."""
import sys
sys.dont_write_bytecode=True
from fractions import Fraction as F
from itertools import combinations
import json
try:
 import numpy as np
except ImportError:
 np=None
from functools import lru_cache
from math import factorial
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def tr(a):return list(map(list,zip(*a)))
def mm(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in tr(b)] for r in a]
def mv(a,x):return [sum(v*w for v,w in zip(r,x)) for r in a]
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def add(a,b,c=1):return [[x+c*y for x,y in zip(r,s)] for r,s in zip(a,b)]
def inv(a):
 n=len(a);x=[list(map(F,r))+s for r,s in zip(a,eye(n))]
 for j in range(n):
  k=next(i for i in range(j,n) if x[i][j]);x[j],x[k]=x[k],x[j];p=x[j][j];x[j]=[z/p for z in x[j]]
  for i in range(n):
   if i!=j:
    p=x[i][j];x[i]=[u-p*v for u,v in zip(x[i],x[j])]
 return [r[n:] for r in x]
def quad(a,x):return dot(x,mv(a,x))
def zeros(n,m):return [[F(0)]*m for _ in range(n)]
points=[(F(0),F(0),F(1)),(F(1,2),F(1,2),F(0)),(F(-1,2),F(1,2),F(0)),(F(-1,2),F(-1,2),F(0)),(F(1,2),F(-1,2),F(0))]
tets=[(0,1,2,3),(0,1,3,4)]
def distance(p,i,j):return sum(w*(x-y)**2 for w,x,y in zip([F(1),F(1),F(1,2)],p[i],p[j]))
def assemble(p,ts,vol):
 n=len(p);K=zeros(n,n);M=zeros(n,n)
 for t,v in zip(ts,vol):
  gram=[[F(distance(p,t[0],t[i])+distance(p,t[0],t[j])-distance(p,t[i],t[j]),2) for j in range(1,4)] for i in range(1,4)];gi=inv(gram);local=zeros(4,4)
  for i in range(1,4):
   for j in range(1,4):local[i][j]=gi[i-1][j-1]
  for i in range(1,4):local[0][i]=local[i][0]=-sum(local[i][1:])
  local[0][0]=sum(sum(r) for r in gi)
  for i,a in enumerate(t):
   for j,b in enumerate(t):K[a][b]+=v*local[i][j];M[a][b]+=v*F(1+int(i==j),20)
 return K,M
def refine(p,ts):
 q=p[:];edges=sorted({e for t in ts for e in combinations(sorted(t),2)});mid={}
 P=eye(len(p))
 for i,j in edges:
  mid[i,j]=len(q);q.append(tuple((x+y)/2 for x,y in zip(p[i],p[j])));row=[F(0)]*len(p);row[i]=row[j]=F(1,2);P.append(row)
 def m(i,j):return mid[tuple(sorted([i,j]))]
 out=[]
 for i,j,k,l in ts:
  a,b,c,d,e,f=m(i,j),m(i,k),m(i,l),m(j,k),m(j,l),m(k,l)
  out.extend([(i,a,b,c),(j,a,d,e),(k,b,d,f),(l,c,e,f),(a,f,b,c),(a,f,c,e),(a,f,e,d),(a,f,d,b)])
 return q,out,P
