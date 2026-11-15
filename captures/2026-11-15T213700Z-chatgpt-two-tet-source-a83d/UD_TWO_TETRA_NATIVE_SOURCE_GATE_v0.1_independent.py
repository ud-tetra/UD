#!/usr/bin/env python3
"""Independent stdlib/Fraction replay of candidate two-tetrahedron generator.
No SymPy, NumPy or SciPy. Exact finite state-graph arithmetic; not physical proof.
"""
from fractions import Fraction as F
from itertools import combinations,product
from math import comb
import json

left=(0,1,2,3);right=(0,1,2,4)
fac=sorted(set(combinations(left,3))|set(combinations(right,3)))
egs=sorted(set(e for f in fac for e in combinations(f,2)))
def adm(b,f):return len({b[i] for i in f})==2
def closure(b,t):return all(adm(b,f) for f in combinations(t,3))
valid=[]
for b in product((0,1),repeat=5):
 if closure(b,left) and closure(b,right):valid.append(b)
assert len(valid)==6
assert all(not (closure((b[:i]+(1-b[i],)+b[i+1:]),left) and closure((b[:i]+(1-b[i],)+b[i+1:]),right)) for b in valid for i in range(5))

M=3; states=[(n,d) for n in range(M+1) for d in range(4)]; I={s:i for i,s in enumerate(states)}
p=[F(comb(M,n),2**M*4) for n,d in states];D=[2*n-M for n,d in states]

def mat(a,closureflag=1):
 c=[1,0,-1,0];h=[(1+F(a)*x)/2 for x in c]
 T=[[F(0) for _ in states] for s in states]
 for s,(n,d) in enumerate(states):
  transitions=[((n-1,d),closureflag*h[d]*n),((n+1,d),closureflag*h[d]*(M-n)),((n,(d+1)%4),F(1,2)),((n,(d-1)%4),F(1,2))]
  for tgt,rate in transitions:
   if not (0<=tgt[0]<=M) or rate==0:continue
   j=I[tgt];T[s][j]+=rate;T[s][s]-=rate
 assert all(sum(row)==0 for row in T)
 assert all(T[i][j]>=0 for i in range(len(states)) for j in range(len(states)) if i!=j)
 assert all(sum(p[i]*T[i][j] for i in range(len(states)))==0 for j in range(len(states)))
 assert all(p[i]*T[i][j]==p[j]*T[j][i] for i in range(len(states)) for j in range(len(states)))
 return T

def apply(T,x):return [sum(T[i][j]*x[j] for j in range(len(x))) for i in range(len(x))]
def moment(T,k):
 y=D[:]
 for _ in range(k):y=apply(T,y)
 return sum(p[i]*D[i]*y[i] for i in range(len(p)))/M
for a in [0,F(1,2),1]:
 T=mat(a)
 assert moment(T,0)==1 and moment(T,1)==-1
 assert moment(T,2)==1+F(a*a,2)
T0=mat(0);T1=mat(1);Tsham=mat(1,0)
assert moment(T0,2)==1 and moment(T1,2)==F(3,2) and moment(Tsham,1)==0
# Exact graph covariance and 1/4 eigenmode along apex-antisymmetric faces
v=[0 if f==(0,1,2) else (1 if 3 in f else -1) for f in fac]
H=[[int(set(e).issubset(f)) for e in egs] for f in fac]
C=[[sum(H[i][k]*H[j][k] for k in range(len(egs))) *F(1,16) for j in range(len(fac))] for i in range(len(fac))]
assert [sum(C[i][j]*v[j] for j in range(7)) for i in range(7)]==[F(x,4) for x in v]
assert sum(x*x for x in v)==6
# For the declared centered face burden readout x_f=(2n−M)v_f/2, C_x = M vvT/4.
for i in range(7):
 for j in range(7):
  actual=sum(p[k]*F(D[k]*v[i],2)*F(D[k]*v[j],2) for k in range(16))
  assert actual==F(M*v[i]*v[j],4)
print(json.dumps({'replay':'PASS','method':'pure stdlib Fraction state enumeration','admissible_bit_states':len(valid),'admissible_single_flip_moves':0,'state_count':len(states),'C_D_prime_over_M':str(moment(T1,1)),'C_D_doubleprime_over_M':str(moment(T1,2)),'constant_control_doubleprime':str(moment(T0,2)),'sham_prime':str(moment(Tsham,1)),'face_mode_eigenvalue':'1/4','stock_each_transition':'conserved','physical_promotion':0},indent=2))
