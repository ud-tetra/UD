#!/usr/bin/env python3
"""Fresh exact Gram-family checker; does not execute archived code."""
from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
basis=[s for k in range(1,5) for s in combinations(range(4),k)]
ix={s:i for i,s in enumerate(basis)};n=15
def zero():return [[F(0) for _ in range(n)] for _ in range(n)]
def eye():return [[F(i==j) for j in range(n)] for i in range(n)]
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def pmul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
def charpoly(a):
 powers=[];p=eye()
 for k in range(1,n+1):p=mul(p,a);powers.append(sum(p[i][i] for i in range(n)))
 c=[F(1)]
 for k in range(1,n+1):c.append(-sum(c[k-i]*powers[i-1] for i in range(1,k+1))/k)
 return c
def determinant(a):
 a=[list(map(F,row)) for row in a];d=F(1)
 for i in range(len(a)):
  pivot=next((k for k in range(i,len(a)) if a[k][i]),None)
  if pivot is None:return F(0)
  if pivot!=i:a[i],a[pivot]=a[pivot],a[i];d=-d
  v=a[i][i];d*=v
  for k in range(i+1,len(a)):
   t=a[k][i]/v
   for j in range(i,len(a)):a[k][j]-=t*a[i][j]
 return d
def gram_ratios(r):
 pts=[(1,1,r),(1,-1,-r),(-1,1,-r),(-1,-1,r)]
 result=[]
 for s in basis:
  if len(s)==1:result.append(F(1));continue
  es=[tuple(F(pts[v][i]-pts[s[0]][i]) for i in range(3)) for v in s[1:]]
  gram=[[sum(x*y for x,y in zip(e,f)) for f in es] for e in es]
  result.append(determinant(gram)/{1:8,2:48,3:256}[len(s)-1])
 return result

d=zero()
for s in basis:
 if len(s)>1:
  for j in range(len(s)):d[ix[s[:j]+s[j+1:]]][ix[s]]=F((-1)**j)
assert mul(d,d)==zero()
samples=[]
for r in [F(1),F(2),F(3,2),F(1,3)]:
 q=r*r
 for p in [1,2]:
  a=((1+q)/2)**p;b=((2*q+1)/3)**p;c=q**p
  g=[v**p for v in gram_ratios(r)]
  assert g==[F(1)]*4+[a,a,F(1),F(1),a,a]+[b]*4+[c]
  A=[[d[j][i]*g[j]/g[i]-d[i][j] for j in range(n)] for i in range(n)]
  assert all(g[i]*A[i][j]+A[j][i]*g[j]==0 for i in range(n) for j in range(n))
  u=4/a;v=2+2/a;x=4*a/b;y=2*(a+1)/b;z=4*b/c
  assert u/v+x/y==2
  expected=[F(1),F(0)]
  for val,m in [(u,1),(v,2),(x,1),(y,2),(z,1)]:
   for _ in range(m):expected=pmul(expected,[F(1),F(0),val])
  assert charpoly(A)==expected
  # Direct exact Laplacian blocks verify the declared eigenvalue multiplicities.
  L=[[-v for v in row] for row in mul(A,A)]
  ranges=[(0,4),(4,10),(10,14),(14,15)]
  roots=[[F(0),u,v,v],[u,v,v,x,y,y],[x,y,y,z],[z]]
  for (start,end),vals in zip(ranges,roots):
   for val in set(vals):
    mat=[[L[i][j]-val*F(i==j) for j in range(start,end)] for i in range(start,end)]
    # Compute rank independently by exact Gaussian elimination.
    rank=0
    for j in range(len(mat)):
     k=next((k for k in range(rank,len(mat)) if mat[k][j]),None)
     if k is None:continue
     mat[rank],mat[k]=mat[k],mat[rank];w=mat[rank][j];mat[rank]=[t/w for t in mat[rank]]
     for k in range(rank+1,len(mat)):
      w=mat[k][j];mat[k]=[s-w*t for s,t in zip(mat[k],mat[rank])]
     rank+=1
    assert len(mat)-rank==vals.count(val)
  samples.append({'r':str(r),'q':str(q),'rule':('A' if p==1 else 'B'),'p':p,'a':str(a),'b':str(b),'c':str(c),'positive_frequency_squared':dict(zip(['u','v','x','y','z'],map(str,[u,v,x,y,z]))),'distinct_positive_bands':len(set([u,v,x,y,z]))})

target=[1,4,9,16,25];rows=[]
for U,V,X,Y in permutations(target,4):
 gap=F(U,V)+F(X,Y)-2
 rows.append({'U':U,'V':V,'X':X,'Y':Y,'invariant_gap':str(gap),'absolute_gap':str(abs(gap))})
assert len(rows)==120
assert all(F(row['invariant_gap'])!=0 for row in rows)
minimum=min(F(row['absolute_gap']) for row in rows)
assert minimum==F(1,144)
witness=[row for row in rows if F(row['absolute_gap'])==minimum]
result={'schema':'UD_GRAM_FIVE_BAND_PARALLEL_v0.1','status':'PASS','provenance':'fresh constructor-team AI exact algebra; not independent human review','physical_promotion':0,'primary_source':'C0173 geometric inner-product interface','boundary_chain_identity':True,'geometry_metric_samples':samples,'characteristic_and_block_spectrum_samples':len(samples),'target_positive_squares':target,'ordered_distinct_assignments_checked':len(rows),'satisfying_assignments':0,'minimum_absolute_invariant_gap':str(minimum),'minimum_gap_witnesses':witness,'assignments':rows,'no_go_scope':'No exact full-generator clock n=10 embedding into one C0173 Gram-rule tetrahedron or identical uncoupled copies under common rate; valid for any a,b,c>0 in this diagonal family, stronger than only q>0,p in {1,2}.','exclusions':['Not an endpoint-error bound.','Not a metric-selection theorem.','Not a no-go for heterogeneous copies, inter-copy coupling or other geometry classes.','Finite invariant gap is not by itself an operator residual lower bound.']}
(HERE/'gram-five-band-parallel-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','characteristic_and_block_spectrum_samples','ordered_distinct_assignments_checked','satisfying_assignments','minimum_absolute_invariant_gap','minimum_gap_witnesses']},indent=2))
