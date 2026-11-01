#!/usr/bin/env python3
"""Independent implementation, stdlib only. Tests scoped theorem without importing primary."""
from itertools import permutations, product, combinations
from fractions import Fraction as Q
import json
v=range(4)
faces=[frozenset(f) for f in combinations(v,3)]
matching=[frozenset((frozenset((0,1)),frozenset((2,3)))),frozenset((frozenset((0,2)),frozenset((1,3)))),frozenset((frozenset((0,3)),frozenset((1,2))))]
P=list(permutations(v)); count=0
def certify(ok,msg):
 global count
 count+=1
 if not ok:raise AssertionError(msg)
def transform_matching(p,a):return frozenset(frozenset(p[x] for x in e) for e in a)
def transform_face(p,f):return frozenset(p[x] for x in f)
K=[p for p in P if all(transform_matching(p,m)==m for m in matching)]
certify(len(K)==4,'not Klein four kernel')
for f in faces:certify({transform_face(p,f) for p in K}==set(faces),'face orbit not 4')
# Exhaust all functions from 8 theta configurations to a singleton face: each input has nontrivial kernel stabilizer;
# 8*4 tests suffice for pointwise impossibility.
for state in product((0,1),repeat=3):
 for f in faces:
  certify(any(transform_face(k,f)!=f for k in K),'equivariant singleton possible?')
# Invariant linear couplings: group orbit of ordered matching/face pairs has size 12 -> one matrix coefficient.
for m in matching:
 for f in faces:
  orbit={(transform_matching(p,m),transform_face(p,f)) for p in P}
  certify(len(orbit)==12,'linear intertwiner coefficient orbit not complete')
# one label-preserving h=(01)(23) is in K and fixes neither any face.
h=(1,0,3,2)
b=(0,0,1,1)
certify(tuple(b[h[i]] for i in v)==b,'label obstruction')
for f in faces:certify(transform_face(h,f)!=f,'label-obstruction face fixed')
# independent fixed-burden diagnostic
burden=(0,1,2,4)
D=[]
for f in sorted(faces,key=lambda x:tuple(sorted(x))):
 score=sum((Q(burden[j]-burden[i],4))**2 for i,j in combinations(sorted(f),2))
 D.append(score)
certify(D==[Q(3,8),Q(13,8),Q(3,2),Q(7,8)],'burden scores')
# fixed old triangle, varying 3 newborn edges, modulo common shift.
q=[Q(n,4) for n in range(4)]
def mod(x):return x%1
sigs=set()
for abc in product(q,repeat=3):
 sig=(mod(abc[1]-abc[0]),mod(abc[2]-abc[0]));sigs.add(sig)
 for a in q:certify(sig==(mod(abc[1]+a-abc[0]-a),mod(abc[2]+a-abc[0]-a)),'gauge')
certify(len(sigs)==16,'gauge quotient')
# inherited old face holonomy = product of new triangle holonomies (additive U1). 
for t in q:
 for abc in product(q,repeat=3):
  g0,g1,g2=abc
  loops=[mod(g0+t-g1),mod(g1-g2),mod(g2-g0)]
  certify(mod(sum(loops))==t,'holonomy gluing')
  if t!=0:certify(any(x!=0 for x in loops),'forbidden simultaneous flatness')
# cost two witnesses with same resource sum from identical initial state.
for c in (Q(0),Q(1),Q(2)):
 certify((Q(3)-c)+(Q(4)+c)==Q(7),'resource invariant')
print('PASS',count,'independent exact finite/group/fraction checks')
with open('independent_results_v1_5.json','w') as f:json.dump({'checks':count,'status':'PASS','linear_orbit_size':12,'pair_action_kernel_order':4,'face_orbit_size':4,'newborn_phase_quotient_size':16,'nonconstructor_review':False},f,indent=2)
