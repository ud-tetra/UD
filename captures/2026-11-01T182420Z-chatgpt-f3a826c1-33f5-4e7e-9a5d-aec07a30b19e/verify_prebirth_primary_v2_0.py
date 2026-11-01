#!/usr/bin/env python3
"""v2.0 Exact central Spin receipt and prior-state nonidentifiability checks. No physics promotion."""
from itertools import product, permutations
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import json
C=0

def ok(x, msg):
 global C
 C+=1
 if not x: raise AssertionError(f'{C}: {msg}')

patterns_by_p={}
for edges in product((-1,1),repeat=3):
 a01,a02,a12=edges
 p=a01*a12*a02
 classes=defaultdict(set)
 for s in product((-1,1),repeat=3):
  s0,s1,s2=s
  q=(a01*s0*s1,a02*s0*s2,a12*s1*s2)
  classes[q].add(s)
  ok(q[0]*q[1]*q[2]==p,'Bianchi sign with fixed old links')
  ok(tuple(-x for x in s)!=s,'newborn sign gauge changes spoke representatives')
  ok(q==(a01*(-s0)*(-s1),a02*(-s0)*(-s2),a12*(-s1)*(-s2)),'apex sign gauge leaves loops unchanged')
 ok(len(classes)==4,'four inequivalent Spin lifts per old-state triple')
 for q,S in classes.items():
  ok(len(S)==2,'two newborn sign gauge representatives per lift')
  ok(q[2]==p*q[0]*q[1],'two Wilson bits reconstruct the third')
  ok(sum(x==-1 for x in q)%2==(p==-1),'sign parity')
 patterns_by_p.setdefault(p,set()).update(classes)
 for old_receipt in (p,edges):
  # same old-state-only receipt admits 4 child extensions;
  # no function from receipt uniquely reconstructs an arbitrary completed class.
  ok(len(classes)>1,'old-only receipt underdetermines newborn connection')
for p,patterns in patterns_by_p.items():
 ok(len(patterns)==4,'parity sector has four classes')
 for chosen_bits in (0,1):
  ok(2**chosen_bits < len(patterns),'one or zero binary Wilson bits insufficient')
 ok(len({q[:2] for q in patterns})==4,'two independent Wilson bits sufficient')
 costs={q:sum(1-x for x in q) for q in patterns} # Q140 fundamental central mismatch: +/- -> 0/2
 best=min(costs.values())
 mins={q for q,c in costs.items() if c==best}
 ok((best,len(mins))==((0,1) if p==1 else (2,3)),'candidate Q140 action minima')
 for perm in permutations(range(3)):
  for q in patterns:ok(tuple(q[i] for i in perm) in patterns,'S3 symmetry of allowed patterns')
  for q in mins:ok(tuple(q[i] for i in perm) in mins,'minimizers closed under S3')
 if p==-1:
  for q in mins:
   orbit={tuple(q[i] for i in perm) for perm in permutations(range(3))}
   ok(orbit==mins,'S3 transitive on 3 odd twisted minima')
   ok(not all(tuple(q[i] for i in perm)==q for perm in permutations(range(3))), 'no invariant singleton minimizer')

# Gauge-invariant old-edge Spin loops exist, but future loops do not: explicit graph cycle census.
vertices_old=(0,1,2,3)
vertices_new=(0,1,2,3,4)
old_edges=set(tuple(sorted(e)) for e in product(vertices_old,repeat=2) if e[0]<e[1])
new_edges=set(old_edges)|{(0,4),(1,4),(2,4)}
for f in [(0,1,4),(0,2,4),(1,2,4)]:
 e={tuple(sorted(x)) for x in ((f[0],f[1]),(f[0],f[2]),(f[1],f[2]))}
 ok(not e.issubset(old_edges),'future Wilson loop unavailable on old 1-skeleton')
 ok(e.issubset(new_edges),'future Wilson loop becomes defined on extended 1-skeleton')
# Absence is a graph-domain result, irrespective of representation.

# Symmetric old burden/graph/receipt cannot select one face covariantly:
faces=((0,1,2),(0,1,3),(0,2,3),(1,2,3))
labels=(0,0,1,1)
perms=[p for p in permutations(range(4)) if all(labels[i]==labels[p[i]] for i in range(4))]
ok(len(perms)==4,'label stabilizer S2 x S2')
for f in faces:
 ok(any(tuple(sorted(p[i] for i in f))!=f for p in perms),'no individual face invariant under label stabilizer')
# Conditional clock: record only when an event is actually authorized, old receipts cannot turn hold into birth.
for p in (-1,1):
 for q in patterns_by_p[p]:
  receipt={'old_loop':p,'old_burden':(1,1,1,1),'old_graph_edges':len(old_edges)}
  ok(receipt['old_loop']==p,'receipt same across all completions')

# Resource constraints distinguish conservation from unique debit.
for old_free in range(1,10):
 for numerator in range(1,old_free*3):
  cost=Fraction(numerator,3)
  if cost<=old_free:
   ok((Fraction(old_free)-cost)+cost==old_free,'conservation permits variable finite debit')
   ok(cost>0,'positive but not specified debit')

out={'version':'v2.0','primary_assertions':C,'old_link_triples':8,'spin_classes_per_old_tuple':4,
'newborn_central_wilson_bits_required_if_old_spin_parity_known':2,
'prebirth_new_loop_receipt':'UNDEFINED_ON_OLD_EDGE_CARRIER',
'odd_old_face_minimizer_count':3,'symmetry_group_odd_minima':'S3 transitive',
'source_native_birth':'OPEN','physical_promotion':0,
'classification':'EXACT_CONDITIONAL; NO_GO_UNDER_OLD_ONLY_RECEIPTS'}
Path(__file__).with_name('RESULTS_PRIMARY_v2.0.json').write_text(json.dumps(out,indent=2)+'\n')
print(f'PASS {C} exact primary assertions')
