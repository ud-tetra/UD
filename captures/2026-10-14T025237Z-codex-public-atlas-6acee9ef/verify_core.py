"""Dependency-free exact constructor check: integer incidence and Fraction rank.
Scope: unit Euclidean simplex bases, increasing-order orientation.
No physical identification or independent review is implied.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction
import json
ROOT=Path(__file__).parent
def zero(n):return [[0]*n for _ in range(n)]
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def mul(a,b):
 n=len(a);out=zero(n)
 for i in range(n):
  for k,x in enumerate(a[i]):
   if x:
    for j,y in enumerate(b[k]):
     if y:out[i][j]+=x*y
 return out
def rank(a):
 m=[[Fraction(x) for x in r] for r in a];row=0
 for col in range(len(m[0])):
  pivot=next((i for i in range(row,len(m)) if m[i][col]),None)
  if pivot is None:continue
  m[row],m[pivot]=m[pivot],m[row];v=m[row][col];m[row]=[x/v for x in m[row]]
  for i in range(row+1,len(m)):
   v=m[i][col]
   if v:m[i]=[x-v*y for x,y in zip(m[i],m[row])]
  row+=1
  if row==len(m):break
 return row
def operator(tops):
 simplices=sorted({x for top in tops for k in range(1,len(top)+1) for x in combinations(top,k)},key=lambda x:(len(x),x))
 idx={x:i for i,x in enumerate(simplices)};B=zero(len(idx))
 for x,j in idx.items():
  if len(x)>1:
   for q in range(len(x)):B[idx[x[:q]+x[q+1:]]][j]=(-1)**q
 A=[[B[j][i]-B[i][j] for j in range(len(idx))] for i in range(len(idx))]
 return simplices,B,A
def characteristic(a):
 n=len(a);b=eye(n);coeff=[1]
 for k in range(1,n+1):
  b=mul(a,b);trace=sum(b[i][i] for i in range(n));assert trace%k==0
  c=-trace//k;coeff.append(c)
  for i in range(n):b[i][i]+=c
 assert b==zero(n)
 return coeff
def polynomial(factors):
 p=[0,1]
 for value,count in factors:
  for _ in range(count):
   q=[0]*(len(p)+2)
   for i,x in enumerate(p):q[i]+=value*x;q[i+2]+=x
   p=q
 return list(reversed(p))
cases=[('filled tetrahedron',[(0,1,2,3)],[4,6,4,1],[(4,7)],'lambda*(lambda^2+4)^7'),('K-minus',[(0,1,2,3),(0,1,2,4)],[5,9,7,2],[(3,4),(5,7)],'lambda*(lambda^2+3)^4*(lambda^2+5)^7'),('K-plus',[(0,1,3,4),(0,2,3,4),(1,2,3,4)],[5,10,9,3],[(2,2),(5,11)],'lambda*(lambda^2+2)^2*(lambda^2+5)^11')]
result=[]
for name,tops,counts,factors,form in cases:
 sim,B,A=operator(tops);actual_counts=[sum(len(x)==k for x in sim) for k in range(1,5)]
 assert actual_counts==counts;assert mul(B,B)==zero(len(sim))
 assert all(A[i][j]==-A[j][i] for i in range(len(sim)) for j in range(len(sim)))
 assert characteristic(A)==polynomial(factors)
 r=rank(A);assert r==len(sim)-1
 record={'carrier':name,'maximal_simplices':tops,'f_vector':counts,'dimension':len(sim),'boundary_squared_zero':True,'skew_adjoint':True,'characteristic_polynomial':form,'rank':r}
 if name=='filled tetrahedron':
  square=mul(A,A)
  expected=[[-4*int(i==j)+int(i<4 and j<4) for j in range(15)] for i in range(15)]
  assert square==expected;assert all(sum(A[i][:4])==0 for i in range(15))
  record['single_cell_square_identity']=True
 result.append(record)
ambient=sorted({x for top in combinations(range(5),4) for k in range(1,5) for x in combinations(top,k)},key=lambda x:(len(x),x));idx={x:i for i,x in enumerate(ambient)}
def embedded(tops):
 sim,B,A=operator(tops);out=zero(30)
 for i,x in enumerate(sim):
  for j,y in enumerate(sim):out[idx[x]][idx[y]]=A[i][j]
 return out
plus=embedded(cases[2][1]);minus=embedded(cases[1][1]);delta=[[x-y for x,y in zip(a,b)] for a,b in zip(plus,minus)]
assert rank(delta)==18
out={'status':'PASS','verification':'integer Faddeev-LeVerrier characteristic polynomial and exact Fraction elimination; fresh construction from simplex deletion rule','review':'constructor verification only','physical_promotion':0,'source':'Paper I review v1.1.1 §§4.3, 6.3, 6.5','cases':result,'ambient_dimension':len(ambient),'ambient_difference_rank':18,'ambient_difference_kernel_dimension':12,'limitations':'Does not verify every assertion in all four papers, native event selection, physical units or experimental correspondence.'}
(ROOT/'dist/sources/UD_ATLAS_CORE_VERIFICATION_v0.1.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out))
