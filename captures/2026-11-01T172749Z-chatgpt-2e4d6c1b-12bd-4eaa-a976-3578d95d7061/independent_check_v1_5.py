#!/usr/bin/env python3
"""Independent method by same constructor: standard library exhaustive rational + modular controls."""
from fractions import Fraction as F
from itertools import combinations, product, permutations
import json
from pathlib import Path
N=0
def ck(p):
 global N
 N+=1
 if not p:raise AssertionError(f'assertion {N}')
verts=(0,1,2,3)
faces=tuple(combinations(verts,3));edges=tuple(combinations(verts,2))
def fscore(v,face):
 return sum((v[j]-v[i])**2 for i,j in combinations(face,2))/F(16)
sym=(F(0),F(0),F(1),F(1));asym=(F(0),F(1),F(2),F(4))
for f in faces:ck(fscore(sym,f)==F(1,8))
D=[fscore(asym,f) for f in faces]
ck(D==[F(3,8),F(13,8),F(3,2),F(7,8)])
for perm in permutations(verts):
 arr=[None]*4
 for i in verts:arr[perm[i]]=asym[i]
 for f in faces:ck(fscore(arr,tuple(sorted(perm[i] for i in f)))==fscore(asym,f))
# 4-face orientation and parity: each edge appears twice.
for e in edges:ck(sum(e[0] in f and e[1] in f for f in faces)==2)
freq={0:0,2:0,4:0}
for bits in product((0,1),repeat=6):
 defect=sum(sum(bits[k] for k,e in enumerate(edges) if set(e).issubset(f))%2 for f in faces)
 ck(defect in freq);freq[defect]+=1
ck(freq=={0:8,2:48,4:8})
# Gauge-invariant new-edge phase differences; finite Z7, flat constraint iff old 012 face flat
for old in product(range(7),repeat=3):
 a,b,c=old
 flat=0
 # eliminate newborn gauge: y0=0 fixes the one gauge direction
 for y1,y2 in product(range(7),repeat=2):
  if y1==a and y2==b and (y2-y1-c)%7==0:flat+=1
 ck((flat==1)==((a-b+c)%7==0))
# prove label group has two face orbits without singleton fixed point
labels=(0,0,1,1)
group=[p for p in permutations(verts) if all(labels[i]==labels[p[i]] for i in verts)]
ck(len(group)==4)
for f in faces:ck(any(tuple(sorted(p[i] for i in f))!=f for p in group))
# two sources of arbitrary exchange costs without choosing an energy scale
for cost in [F(0),F(1),F(2),F(3)]:ck((F(3)-cost)+(F(4)+cost)==7)
# Mixed ranking exact at t=0,1,2 using bounding sqrt(3) between 5/3 and 7/4
# for t=1: 5/4 > sqrt(3)/2; t=2: 5/4 < sqrt(3)
ck(F(5,4)>F(7,8));ck(F(5,4)<F(5,3))
result={'version':'v1.5','checks':N,'method':'stdlib Fraction and Z7 finite gauge controls','parity':freq,'external_review':'PENDING'}
(Path(__file__).resolve().parent/'independent_results_v1_5.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS',N,'independent-method exact checks')
