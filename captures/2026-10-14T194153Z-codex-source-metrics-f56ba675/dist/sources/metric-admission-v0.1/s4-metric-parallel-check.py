#!/usr/bin/env python3
"""New constructor-team AI exact checker; does not execute archived code."""
from fractions import Fraction as Q
from itertools import combinations, permutations
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
n=15
basis=[s for k in range(1,5) for s in combinations(range(4),k)]
index={s:i for i,s in enumerate(basis)}
degree=[len(s)-1 for s in basis]
def zero(): return [[Q(0) for _ in range(n)] for _ in range(n)]
def eye(): return [[Q(i==j) for j in range(n)] for i in range(n)]
def add(a,b): return [[a[i][j]+b[i][j] for j in range(n)] for i in range(n)]
def scale(t,a): return [[t*v for v in row] for row in a]
def tr(a): return sum(a[i][i] for i in range(n))
def trans(a): return [list(c) for c in zip(*a)]
def mul(a,b):
 bt=trans(b)
 return [[sum(x*y for x,y in zip(row,col)) for col in bt] for row in a]
def rank(rows):
 a=[list(map(Q,r)) for r in rows]; r=0
 for c in range(len(a[0])):
  p=next((i for i in range(r,len(a)) if a[i][c]),None)
  if p is None: continue
  a[r],a[p]=a[p],a[r]; v=a[r][c];a[r]=[x/v for x in a[r]]
  for i in range(len(a)):
   if i!=r and a[i][c]:
    t=a[i][c];a[i]=[x-t*y for x,y in zip(a[i],a[r])]
  r+=1
  if r==len(a): break
 return r
def pmul(a,b):
 out=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b): out[i+j]+=x*y
 return out
def charpoly(a):
 # Descending coefficients of det(lambda I-a), exact Newton identities.
 powers=[];p=eye()
 for k in range(1,n+1): p=mul(p,a);powers.append(tr(p))
 c=[Q(1)]
 for k in range(1,n+1): c.append(-sum(c[k-i]*powers[i-1] for i in range(1,k+1))/k)
 return c

D=[];A=[]
for k in range(1,4):
 d=zero()
 for s in basis:
  if len(s)==k+1:
   for j in range(k+1): d[index[s[:j]+s[j+1:]]][index[s]]=Q((-1)**j)
 D.append(d);A.append(add(trans(d),scale(-1,d)))
Z=zero();I=eye();P=[scale(Q(-1,4),mul(a,a)) for a in A]
P0=add(I,scale(-1,add(add(P[0],P[1]),P[2])))
assert [rank(d) for d in D]==[3,3,1]
assert [rank(a) for a in A]==[6,6,2]
assert [rank(p) for p in [P0]+P]==[1,6,6,2]
for a in A: assert trans(a)==scale(-1,a)
for i in range(3):
 for j in range(3):
  if i!=j: assert mul(A[i],A[j])==Z
for p in [P0]+P:
 assert trans(p)==p and mul(p,p)==p
for i,p in enumerate([P0]+P):
 for j,q in enumerate([P0]+P):
  if i!=j: assert mul(p,q)==Z
assert add(add(add(P0,P[0]),P[1]),P[2])==I
for i in range(2): assert mul(D[i],D[i+1])==Z

R=[];chars=[]
for perm in permutations(range(4)):
 r=zero()
 for s in basis:
  im=tuple(perm[v] for v in s)
  inv=sum(im[i]>im[j] for i in range(len(im)) for j in range(i+1,len(im)))
  r[index[tuple(sorted(im))]][index[s]]=Q((-1)**inv)
 assert mul(trans(r),r)==I
 for d in D: assert mul(r,d)==mul(d,r)
 for a in A: assert mul(r,a)==mul(a,r)
 R.append(r);chars.append(tr(r))
assert sum(c*c for c in chars)/24==13
# Explicit equivariant basis reaches the character upper bound, exact adjoint types.
C=[P0];sym=[P0];skew=[]
for i in range(3):
 q=zero()
 for j,deg in enumerate(degree): q[j][j]=Q(deg==i)
 three=[mul(q,P[i]),mul(add(I,scale(-1,q)),P[i]),add(mul(q,A[i]),scale(-1,mul(A[i],q)))]
 C+=three+[A[i]];sym+=three;skew.append(A[i])
flat=lambda a:[v for row in a for v in row]
assert rank(list(map(flat,C)))==13
assert rank(list(map(flat,sym)))==10
assert rank(list(map(flat,skew)))==3
for c in C:
 for r in R: assert mul(c,r)==mul(r,c)
for c in sym: assert trans(c)==c
for c in skew: assert trans(c)==scale(-1,c)

examples=[(Q(1),Q(1),Q(1),Q(1)),(Q(1),Q(4),Q(9),Q(16)),(Q(2),Q(3),Q(5),Q(7)),(Q(3,2),Q(2,3),Q(5,7),Q(11,13))]
metric_results=[]
for gs in examples:
 g=[gs[k] for k in degree];ag=zero()
 for d in D:
  # Weighted adjoint = G^-1 d^T G; signed boundary stays unchanged.
  dag=[[d[j][i]*g[j]/g[i] for j in range(n)] for i in range(n)]
  ag=add(ag,add(dag,scale(-1,d)))
 assert [[g[i]*ag[i][j]+ag[j][i]*g[j] for j in range(n)] for i in range(n)]==Z
 for r in R: assert mul(ag,r)==mul(r,ag)
 ratios=[gs[i]/gs[i+1] for i in range(3)]
 expected=[Q(1),Q(0)]
 for rat,m in zip(ratios,[3,3,1]):
  for _ in range(m): expected=pmul(expected,[Q(1),Q(0),4*rat])
 assert charpoly(ag)==expected
 assert mul(ag,ag)==scale(-4,add(add(scale(ratios[0],P[0]),scale(ratios[1],P[1])),scale(ratios[2],P[2])))
 metric_results.append({'g_by_degree':list(map(str,gs)),'frequency_squared':list(map(str,[4*r for r in ratios]))})

def exact_partition_radius(M):
 # Sorted centers admit ordered contiguous assignment. Enumerate all zero prefixes
 # and all <=3 nonempty subsequent contiguous groups; optimal free group center
 # is its endpoint midpoint. Fixed zero cost is 2*h.
 best=None;partitions=0;witness=None
 for h in range(M+1):
  rest=M-h
  groups_options=[()] if rest==0 else []
  for k in range(1,min(3,rest)+1):
   for cuts in combinations(range(1,rest),k-1):
    ends=(0,)+cuts+(rest,)
    groups_options.append(tuple(ends[i+1]-ends[i] for i in range(k)))
  for sizes in groups_options:
   partitions+=1
   radius=max([Q(2*h)]+[Q(s-1) for s in sizes])
   if best is None or radius<best:
    best=radius;witness=(h,sizes)
 return best,witness,partitions

cover=[];partition_count=0
for M in range(1,65):
 radius,witness,count=exact_partition_radius(M);partition_count+=count
 r=next(i for i in range(2*M+1) if M<=i//2+3*(i+1))
 assert radius==r
 assert M>(r-1)//2+3*r if r else True
 cover.append({'M':M,'radius':str(radius),'zero_prefix':witness[0],'free_group_sizes':list(witness[1])})
centers=[Q(0),Q(3),Q(7),Q(10)]
assert max(min(abs(Q(x)-c) for c in centers) for x in range(0,11,2))==1
assert cover[4]['radius']=='1'
out={'schema':'UD_S4_METRIC_PARALLEL_CHECK_v0.1','status':'PASS','provenance':'new constructor-team AI verification; not external human review','physical_promotion':0,'basis':list(map(list,basis)),'signed_actions':len(R),'boundary_ranks':[3,3,1],'skew_channel_ranks':[6,6,2],'projector_ranks':[1,6,6,2],'commutant_dimensions':{'full':13,'symmetric':10,'skew':3},'equivariance_checks':{'boundary':72,'skew_basis':72,'full_commutant_basis':312,'weighted_examples':96},'metric_examples':metric_results,'cover_partition_checks':partition_count,'cover_target_sizes_checked':64,'cover_formula':'least integer r>=0 with M<=floor(r/2)+3(r+1)','cover_results':cover,'default_relaxation':{'M':5,'positive_targets':[2,4,6,8,10],'free_centers':[3,7,10],'fixed_center':0,'radius':1,'scope':'unconstrained spectral cover only; not source-selected metric'},'exact_embedding_no_go':'even n>=8: n/2>=4 distinct positive clock bands cannot embed into at most three positive bands of one degree-isotropic tetrahedron or identical uncoupled copies with a common rate','excluded_inferences':['Heterogeneous copies can introduce more bands; no general no-go claimed.','Arbitrary S4-invariant metrics may mix repeated irreducible copies; degree-isotropic family is a restricted subclass.','Frequency-cover mismatch is not an endpoint error lower bound.','No native coefficients, SI time, energy, locality, capture or physical realization selected.']}
path=HERE/'s4-metric-parallel-results.json';path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','signed_actions','commutant_dimensions','cover_partition_checks','cover_target_sizes_checked','default_relaxation']},indent=2))
