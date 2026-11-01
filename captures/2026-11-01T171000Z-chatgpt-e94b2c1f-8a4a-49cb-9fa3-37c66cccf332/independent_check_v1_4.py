#!/usr/bin/env python3
"""Independent implementation, standard library only, no primary script imports."""
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path
import json

C=0

def check(b,label):
 global C
 if not b:raise AssertionError(label)
 C+=1

vertices=(0,1,2,3)
faces=list(combinations(vertices,3))
edges=list(combinations(vertices,2))
# Build boundaries from triangle alternating omission without using SymPy.
def boundary(face):
 result={}
 for i in range(3):
  e=tuple(v for k,v in enumerate(face) if k!=i)
  result[e]=(-1)**i
 return result
D={f:boundary(f) for f in faces}
for edge in edges:
 check(sum((-1)**(3-idx)*D[f].get(edge,0) for idx,f in enumerate(faces))==0,'boundary of boundary')

# Z2 closed-surface parity: face curvatures from assignments of six edges.
counts={0:0,2:0,4:0}
for bits in product((0,1),repeat=6):
 syndrome=[]
 for f in faces:
  syndrome.append(sum(bits[edges.index(e)] for e in combinations(f,2))%2)
 n=sum(syndrome)
 check(n in counts,'even face parity')
 counts[n]+=1
 # A binary face-curvature score cannot single out precisely one strict maximum.
 check(sum(s==max(syndrome) for s in syndrome)!=1,'no strict unique maximizer')
check(counts=={0:8,2:48,4:8},'syndrome counts')

# Reconstruct source Q162 current and face scores as Fractions.
def score(rho,face):
 total=Fraction(0)
 for a,b in combinations(face,2):
  val=-(Fraction(rho[b])-Fraction(rho[a]))/4
  total+=val*val
 return total
sym=(0,0,1,1);asym=(0,1,2,4)
for f in faces:check(score(sym,f)==Fraction(1,8),'symmetric score')
ascores={f:score(asym,f) for f in faces}
check(ascores[(0,1,3)]==Fraction(13,8),'013 score')
check(ascores[(0,2,3)]==Fraction(3,2),'023 score')
check(ascores[(0,1,2)]==Fraction(3,8),'012 score')
check(ascores[(1,2,3)]==Fraction(7,8),'123 score')
check(max(ascores,key=ascores.get)==(0,1,3),'unique maximum')
for permutation in permutations(vertices):
 permrho=[0]*4
 for old,new in enumerate(permutation):permrho[new]=asym[old]
 for f in faces:
  pf=tuple(sorted(permutation[v] for v in f))
  check(score(permrho,pf)==ascores[f],'covariant score')

# Signs and source magnitudes are different types: same total sum or |rho| need not yield current.
# Two signed edge amplitude tuples with equal individual quadratic stocks produce different face orientation.
check(sum(x*x for x in (1,1,1))==sum(x*x for x in (1,-1,1))==3,'same stock')
check((1+1+1)!=(1-1+1),'different signed sums')

# A pre-birth history tag is a possible symmetry breaker but does not specify the event law.
H=[p for p in permutations(vertices) if all(sym[i]==sym[p[i]] for i in vertices)]
check(len(H)==4,'label stabilizer')
for f in faces:
 check(any(tuple(sorted(p[v] for v in f))!=f for p in H),'no fixed face')
for f in faces:
 tagged_H=[p for p in H if tuple(sorted(p[v] for v in f))==f]
 check(0<len(tagged_H)<len(H),'tag reduces stabilizer')

# Nonunique source-cost/stock reconciliations for identical prestate.
for cost in [Fraction(1,10), Fraction(1,4), Fraction(1,2), Fraction(1)]:
 donor=[Fraction(1)-cost/4]*4; child=cost
 check(sum(donor)+child==4,'uniform conservation')
 donor2=[Fraction(1)-cost, Fraction(1),Fraction(1),Fraction(1)]
 check(sum(donor2)+child==4,'concentrated conservation')
 check(donor!=donor2,'different newborn donor allocations')
 check(min(donor)>=0 and min(donor2)>=0,'nonnegative')

# Independent U1 star seam witness: flat vs twisted old-boundary preserving.
star_A=(0,0,0);star_B=(0,1,0)
check(all(x==0 for x in star_A),'flat star')
check(star_B[1]-star_B[0]!=star_A[1]-star_A[0],'different new Wilson loop')
check(star_B[2]-star_B[0]==star_A[2]-star_A[0],'same other loop')

result={'assertions':C,'pass':True,'binary_Z2_curvature_counts':counts,'source_lane':'independent pure Fraction Python', 'physical_promotion':0}
(Path(__file__).parent/'independent_results_v1_4.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS',C,'exact fraction/integer checks','Z2 syndrome counts',counts)
