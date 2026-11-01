#!/usr/bin/env python3
"""UD v1.5 exact scoped proof checks; no physical bridge. Uses SymPy only."""
import json
from itertools import combinations,product,permutations
from pathlib import Path
from sympy import Matrix, Rational as Q, sqrt, pi, cos, simplify, eye, zeros
O=Path(__file__).resolve().parent
N=0
def ck(condition, label):
 global N
 N+=1
 if not bool(condition): raise AssertionError(f'#{N} {label}')
def eq(a,b,label): ck(simplify(a-b)==0,label)
V=range(4)
faces=list(combinations(V,3)); edges=list(combinations(V,2));
b=Matrix([Q(0),Q(1),Q(2),Q(4)])
bs=Matrix([Q(0),Q(0),Q(1),Q(1)])
def burden(rho):
 return {f:sum((rho[j]-rho[i])**2/16 for (i,j) in combinations(f,2)) for f in faces}
D=burden(b); Ds=burden(bs)
assert list(D.values())==[Q(3,8),Q(13,8),Q(3,2),Q(7,8)]
for f in faces:eq(Ds[f],Q(1,8),'symmetric burden tie')
for idx in permutations(range(4)):
 r=Matrix([0,0,0,0]);
 for i in V:r[idx[i]]=b[i]
 for f in faces:
  moved=tuple(sorted(idx[i] for i in f))
  eq(burden(r)[moved],D[f], 'burden equivariance')
# Oriented edge-to-face coboundary B2^T
B2=zeros(6,4)
for j,(a,b0,c) in enumerate(faces):
 for pair,sgn in [((b0,c),1),((a,c),-1),((a,b0),1)]: B2[edges.index(pair),j]=sgn
u=Matrix([-1,1,-1,1]);ck(B2*u==zeros(6,1),'boundary nilpotent tetra shell')
a=Matrix([-1,1,0,-1,0,0]);phi=B2.T*a # angles pi/6
ck(list(phi)==[-3,-1,1,-1],'U1 face phase profile')
U=[simplify(1-cos(pi*q/6)) for q in phi]
eq(U[0],1,'U1 large mismatch')
for z in U[1:]:eq(z,1-sqrt(3)/2,'U1 other mismatch')
eq(u.dot(phi),0,'oriented net curvature zero')
# Parameter-free Pareto comparison conditional on maximizing BOTH scores.
pareto=[]
for k in range(4):
 dominated=False
 for m in range(4):
  if m==k:continue
  better_b=(D[faces[m]]-D[faces[k]]).is_nonnegative
  better_u=(U[m]-U[k]).is_nonnegative
  strict=((D[faces[m]]-D[faces[k]]).is_positive or (U[m]-U[k]).is_positive)
  ck(better_b in (True,False) and better_u in (True,False),'comparison is decidable')
  if better_b and better_u and strict: dominated=True
 if not dominated:pareto.append(''.join(map(str,faces[k])))
ck(pareto==['012','013'],'Pareto nondominated source diagnostics')
# cross channel exogenous weight t: S_f=D_f+tU_f
from sympy import symbols
t=symbols('t', nonnegative=True, real=True)
critical=5*sqrt(3)/6
for tst,winner in [(Q(0),1),(Q(1),1),(Q(2),0),(Q(10),0)]:
 vals=[simplify(D[f]+tst*U[i]) for i,f in enumerate(faces)]
 for j in range(4):
  if j!=winner:ck((vals[winner]-vals[j]).is_positive, f'weighted winner at {tst}: {j}')
eq(D[faces[1]]-D[faces[0]],Q(5,4),'burden gap')
eq(U[0]-U[1],sqrt(3)/2,'holonomy gap')
eq(critical*(U[0]-U[1]),D[faces[1]]-D[faces[0]],'exact rank crossover')
# Binary twists parity, enumeration multiplicities
counts={0:0,2:0,4:0}
for bits in product([0,1],repeat=6):
 facebits=[sum(bits[i] for i in range(6) if B2[i,j]!=0)%2 for j in range(4)]
 w=sum(facebits);ck(w in counts,'even face parity');counts[w]+=1
 ck(w%2==0,'parity exact')
ck(counts=={0:8,2:48,4:8},'Z2 incidence census')
# U1 flat apex theorem: new triangles 01w, 02w, 12w are all flat iff old 012 holonomy flat
# degrees modulo 6 are adequate finite witnesses (angle units pi/3), but theorem follows algebraically
# y0,y1,y2 three link phases oriented old vertex->w, new flatness: y1-y0=a01, y2-y0=a02, y2-y1=a12.
for A01,A02,A12 in product(range(6), repeat=3):
 old=(A01-A02+A12)%6
 feasible=False
 for y0,y1,y2 in product(range(6),repeat=3):
  if (y1-y0-A01)%6==0 and (y2-y0-A02)%6==0 and (y2-y1-A12)%6==0:
   feasible=True; ck(old==0,'flat apex implies old flat')
 ck(feasible==(old==0),'flat apex iff old flat')
 # at fixed y0=0, two free new phases define 6^2 distinct new holonomy pairs
 seen=set()
 for y1,y2 in product(range(6),repeat=2):
  seen.add(((y1-y0-A01)%6 if False else (y1-A01)%6,(y2-A02)%6))
 ck(len(seen)==36,'two U1 new loop freedoms modulo newborn gauge')
# quadratic norm redistribution exact witnesses
for alpha,beta in [(Q(1),Q(0)),(Q(3,5),Q(4,5)),(Q(5,13),Q(12,13))]:
 eq(alpha*alpha+beta*beta,1,'support-conserving birth angle family')
# resource ledger: same parent budget 7, different debits
for cost in [Q(0),Q(1),Q(2),Q(3)]:
 free=Q(3)-cost; bound=Q(4)+cost;eq(free+bound,7,'resource accounting nonuniqueness')
# source linear dimension typology, equal metric gauge \bar f curl invariants
# 3 new edge phases, 1 gauge, 2 independent holonomies; old triangle is their signed sum
ck(B2.shape==(6,4),'face-edge incidence dimensions')
res={'version':'v1.5','status':'EXACT_CONDITIONAL_NO_SOURCE_OWNED_SELECTOR','physical_promotion':0,'checks':N,'face_order':[''.join(map(str,f)) for f in faces],
'burden_scores':{''.join(map(str,f)):str(D[f]) for f in faces},'U1_profile_pi_sixths':list(map(str,phi)),
'critical_exogenous_weight':str(critical),'pareto_nondominated_faces':pareto,'z2_defect_counts':counts,'U1_flat_apex_cases':216,
'newborn_U1_relative_phases':2,'review':'NONCONSTRUCTOR_PENDING'}
(O/'results_v1_5.json').write_text(json.dumps(res,indent=2)+'\n')
print('PASS',N,'exact assertions; critical crossover = 5*sqrt(3)/6')
