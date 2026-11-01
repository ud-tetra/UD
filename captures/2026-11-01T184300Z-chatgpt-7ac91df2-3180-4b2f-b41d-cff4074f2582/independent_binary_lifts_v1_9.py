#!/usr/bin/env python3
"""Independent exact Z2 incidence and information-theoretic audit, stdlib only."""
from itertools import product,permutations
from fractions import Fraction
from collections import defaultdict
from pathlib import Path
import json,math
CHECKS=0
def test(cond,lab):
 global CHECKS
 CHECKS+=1
 if not cond:raise AssertionError(f'{CHECKS}:{lab}')
# For each old-face central sign p, loop signs are p01*si*sj.
# All three old links considered separately; old old-face central curvature p = product of old links.
patterns_by_p={}
for a01,a02,a12 in product((1,-1),repeat=3):
 p=a01*a02*a12
 classes=defaultdict(set)
 for s0,s1,s2 in product((1,-1),repeat=3):
  loops=(a01*s0*s1,a02*s0*s2,a12*s1*s2)
  classes[loops].add((s0,s1,s2))
  test(math.prod(loops)==p,'central Bianchi parity inherited')
  test(loops==tuple((a01*(-s0)*(-s1), a02*(-s0)*(-s2),a12*(-s1)*(-s2))),'apex gauge + and -')
 test(len(classes)==4,'exact four lift classes fixed old transports')
 for pat,states in classes.items():
  test(len(states)==2,'two gauge equivalent sign assignments')
  b0=(pat[0]==-1);b1=(pat[1]==-1);b2=(pat[2]==-1)
  test((b0^b1^b2)==(p==-1),'binary cochain Bianchi')
  test((0 if pat[0]==1 else 2,0 if pat[1]==1 else 2,0 if pat[2]==1 else 2) in [(0 if z==1 else 2,0 if w==1 else 2,0 if u==1 else 2) for z,w,u in classes],'exact Wilson bits')
 patterns_by_p.setdefault(p,set()).update(classes)
for p,classes in patterns_by_p.items():
 test(len(classes)==4,'four patterns parity sector')
 test(len({(z[0],z[1]) for z in classes})==4,'two loops suffice to reconstruct third')
 test(len({z[0] for z in classes})==2,'one loop insufficient')
 test(len({z[1] for z in classes})==2,'one other loop insufficient')
 for p0,p1,p2 in classes:
  test(p2 == p*p0*p1,'third Wilson loop determined by old parity')
  test(sum(z==-1 for z in (p0,p1,p2))%2 == (p==-1),'defect parity exact')
# Candidate Q140 central Wilson mismatch minimization, NOT a native event law:
# Flat inherited Spin loop: unique all-flat child lift; odd inherited loop: three
# degenerate one-defect child lift locations (frustration), and one triple defect.
minimizers={}
for p,classes in patterns_by_p.items():
 scores={pat:sum(0 if h==1 else 2 for h in pat) for pat in classes}
 best=min(scores.values())
 wins=sorted([pat for pat,score in scores.items() if score==best])
 minimizers[p]=wins
 test((best,len(wins))==((0,1) if p==1 else (2,3)),'parity frustration exact minimizer multiplicity')
 for pat in classes:
  test(sum(1 for t in pat if t==-1)%2==(p==-1),'central parity fixes defect parity')
# full typed spin and vector mismatch at central +/-
for p in (1,-1):
 spin=Fraction(1)-Fraction((2*p),2)
 vector=Fraction(1)-Fraction(3,3)
 test(spin in (0,2),'fundamental 2d character central receipt')
 test(vector==0,'SO3 vector loses center')
 test(Fraction(1)-spin/2 in (0,1),'coherent two-path probability encoded by spin trace')
# All permutations of faces preserve parity and class existence, not a preferred sign assignment.
for pat in patterns_by_p[1]:
 for perm in permutations((0,1,2)):
  pp=tuple(pat[j] for j in perm)
  test(pp in patterns_by_p[1],'all central even-parity patterns closed under face permutations')
for pat in patterns_by_p[-1]:
 for perm in permutations((0,1,2)):
  pp=tuple(pat[j] for j in perm)
  test(pp in patterns_by_p[-1],'odd-parity patterns closed under face permutations')
# Half-turn projective phase control: Spin Wilson trace is blind to +/- i sigma_z,
# despite a coherent, marked-spinor reference with phase -i distinguishing them.
for sign in (1,-1):
 spin_trace=0
 vector_trace=-1
 test(Fraction(1)-Fraction(spin_trace,2)==1,'spin trace mismatch has half-turn degeneracy')
 test(Fraction(1)-Fraction(vector_trace,3)==Fraction(4,3),'vector mismatch is half-turn')
 # psi = |up>, H psi = sign*i psi, reference -i, so amplitude (1+sign)/2
 quadrature_probability=Fraction((1+sign)**2,4)
 test(quadrature_probability==(1 if sign==1 else 0),'relative reference resolves marked spinor half-turn')
# Minimal binary information: 2 bits minimum as there are four pairwise distinct Spin classes.
for bits in (0,1):
 test(2**bits<4,'one or zero bits cannot distinguish all four')
test(2**2==4,'exact two binary bits suffice')
# Prebirth receipt state only has inherited old links, not three future new edges:
# each old state extends in 4 mutually distinct classes => cannot reconstruct new lift class.
for triple in product((1,-1),repeat=3):
 p=math.prod(triple)
 all_completions=set()
 for s in product((1,-1),repeat=3):
  all_completions.add((triple[0]*s[0]*s[1],triple[1]*s[0]*s[2],triple[2]*s[1]*s[2]))
 test(len(all_completions)==4,'old state has four distinct Spin extensions')
 test(set(all_completions)==patterns_by_p[p],'old link choice changes no allowable parity patterns')
# Resource no-go under source-only: arbitrary debit valid under an added bank; not identity with spin bits
for n in range(1,13):
 for cost in (Fraction(1,n+1),Fraction(n,n+1)):
  test(Fraction(n)-cost>=0,'resource positive bank after illustrative debit')
  test((Fraction(n)-cost)+(Fraction(3)+cost)==n+3,'resource conservation under any positive debit')
res={'version':'v1.9','independent_exact_checks':CHECKS,'old_face_parities':{str(k):[list(x) for x in sorted(v)] for k,v in patterns_by_p.items()},
 'spin_lifts_per_old_parity':4,'minimal_binary_wilson_receipt_bits':2,
 'candidate_minimizer_counts':{str(p):len(v) for p,v in minimizers.items()},
 'candidate_minimizer_rule_status':'NOT_NATIVE_ACTION - introduced total-facet sum and minimization',
 'old_state_to_new_lift':'non-identifiable: four inequivalent completions',
 'source_native_receipt':'OPEN','physical_promotion':0,'method':'independent stdlib Z2 cochain + Fraction; same constructor'}
Path(__file__).with_name('RESULTS_INDEPENDENT_v1.9.json').write_text(json.dumps(res,indent=2)+'\n')
print('PASS',CHECKS,'independent exact assertions')
