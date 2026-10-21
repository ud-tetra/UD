from fractions import Fraction as F
from itertools import combinations,permutations
import json
N=15
simp=[tuple(combinations(range(4),k+1)) for k in range(4)]
flat=sum((list(s) for s in simp),[]);index={s:i for i,s in enumerate(flat)}
def zero():return [[F(0) for _ in range(N)] for _ in range(N)]
def mul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
def scale(c,A):return [[c*x for x in row] for row in A]
def add(*As):return [[sum(A[i][j] for A in As) for j in range(N)] for i in range(N)]
def tr(A):return sum(A[i][i] for i in range(N))
def transpose(A):return list(map(list,zip(*A)))
I=zero()
for i in range(N):I[i][i]=F(1)
Z=zero();G=[]
for k in range(1,4):
 A=zero()
 for s in simp[k]:
  for j in range(k+1):
   face=s[:j]+s[j+1:];lo=index[face];hi=index[s]
   A[hi][lo]=F((-1)**j);A[lo][hi]=-F((-1)**j)
 assert transpose(A)==scale(-1,A)
 G.append(A)
P=[scale(F(-1,4),mul(A,A)) for A in G]
assert [tr(X) for X in P]==[6,6,2]
for j in range(3):
 assert mul(P[j],P[j])==P[j]
 for k in range(3):
  if j!=k:assert mul(G[j],G[k])==Z and mul(P[j],P[k])==Z
P0=add(I,scale(-1,add(*P)))
assert mul(P0,P0)==P0 and tr(P0)==1
for g in permutations(range(4)):
 R=zero()
 for s in flat:
  raw=[g[x] for x in s];inv=sum(raw[i]>raw[j] for i in range(len(raw)) for j in range(i+1,len(raw)))
  R[index[tuple(sorted(raw))]][index[s]]=F((-1)**inv)
 for A in G:assert mul(R,A)==mul(A,R)
records=[]
for abc in [(1,1,1),(1,2,3),(2,4,6),(1,1,2)]:
 A=add(*(scale(c,B) for c,B in zip(abc,G)));L=scale(-1,mul(A,A))
 assert L==add(*(scale(4*c*c,B) for c,B in zip(abc,P)))
 moment=tr(mul(L,L))/tr(L)**2
 formula=F(sum(r*c**4 for r,c in zip((3,3,1),abc)),2*sum(r*c*c for r,c in zip((3,3,1),abc))**2)
 assert moment==formula
 records.append({'rates':abc,'dimensionless_moment':str(moment),'positive_frequency_squared_and_multiplicity':[[4*c*c,r] for c,r in zip(abc,(3,3,1))]})
assert records[0]['dimensionless_moment']=='1/14'
assert records[1]['dimensionless_moment']=='11/96'
assert records[1]['dimensionless_moment']==records[2]['dimensionless_moment']
assert records[0]['dimensionless_moment']!=records[1]['dimensionless_moment']
# Source algebra for the conditional Pachner response eigenvalues; no 30D projector replay.
sum_roots=F(230,80);prod_roots=F(115**2-8065,80**2)
assert sum_roots==F(23,8) and prod_roots==F(129,160)
assert F(115**2)>8065>0
assert F(33,40)*5==F(33,8)
print(json.dumps({'status':'PASS_SCOPED','carrier':'nonaugmented filled tetrahedron; oriented unit chains; dimension 15','boundary_channel_projector_ranks':[6,6,2],'harmonic_rank':1,'signed_S4_permutations':24,'generator_equivariance_checks':72,'rate_cases':records,'controls':['nonunique common-scale-free moment','common scaling leaves moment unchanged','canonical unit case reproduces sole nonzero frequency 2'],'response_scalar_checks':{'sum':str(sum_roots),'product':str(prod_roots),'clock_scale_squared':'33/40'},'limits':['No physical particle assignment','No action or mass calibration','Pachner 30D projector not recomputed','No general native-source absence theorem'],'physical_promotion':0},indent=2))
