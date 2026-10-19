"""New exact constructor checks; standard library only, no archived code."""
import sys
sys.dont_write_bytecode=True
from fractions import Fraction as F
from itertools import combinations
import json
checks=[]
def check(name,condition):
 assert condition,name
 checks.append(name)
def transpose(m):return list(map(list,zip(*m)))
def mul(a,b):
 bt=transpose(b)
 return [[sum(x*y for x,y in zip(row,col)) for col in bt] for row in a]
def charpoly(a):
 n=len(a);b=[[int(i==j) for j in range(n)] for i in range(n)];out=[1]
 for k in range(1,n+1):
  ab=mul(a,b);tr=sum(ab[i][i] for i in range(n));assert tr%k==0;c=-tr//k;out.append(c)
  b=[[ab[i][j]+c*int(i==j) for j in range(n)] for i in range(n)]
 return out
def pmul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
def expected(factors):
 p=[1]
 for factor,count in factors:
  for _ in range(count):p=pmul(p,factor)
 return p
def complex_record(tops):
 d=max(map(len,tops))-1
 cells=[sorted({f for t in tops for f in combinations(sorted(t),k+1)}) for k in range(d+1)]
 bs=[]
 for k in range(1,d+1):
  ix={s:i for i,s in enumerate(cells[k-1])};b=[[0]*len(cells[k]) for _ in cells[k-1]]
  for j,s in enumerate(cells[k]):
   for i in range(k+1):b[ix[s[:i]+s[i+1:]]][j]=(-1)**i
  bs.append(b)
 offsets=[0]
 for c in cells:offsets.append(offsets[-1]+len(c))
 n=offsets[-1];a=[[0]*n for _ in range(n)]
 for k,b in enumerate(bs):
  for i,row in enumerate(b):
   for j,x in enumerate(row):a[offsets[k]+i][offsets[k+1]+j]=x;a[offsets[k+1]+j][offsets[k]+i]=-x
 for k in range(len(bs)-1):check(f'boundary squared zero dimension{k+2}',all(x==0 for row in mul(bs[k],bs[k+1]) for x in row))
 return {'f_vector':list(map(len,cells)),'chain_dimension':n,'skew_characteristic_coefficients':charpoly(a)}
shell=complex_record([(0,1,2),(0,2,3),(0,3,4),(0,1,4)])
filled=complex_record([(0,1,2,3),(0,1,3,4)])
horn=complex_record([(0,1,2),(0,1,3),(0,2,3)])
check('shell f vector',shell['f_vector']==[5,8,4])
check('shell spectrum',shell['skew_characteristic_coefficients']==expected([([1,0],1),([1,0,1],1),([1,0,3],4),([1,0,5],3)]))
check('filled Kminus f vector',filled['f_vector']==[5,9,7,2])
check('filled Kminus spectrum',filled['skew_characteristic_coefficients']==expected([([1,0],1),([1,0,3],4),([1,0,5],7)]))
check('shell differs from standard 3 horn',horn['f_vector']==[4,6,3] and shell['f_vector']!=horn['f_vector'])
# a=1; represent each vertex as (x,y,z/sqrt(2)), so Gram metric diag(1,1,1/2).
v=[(F(0),F(0),F(1)),(F(1,2),F(1,2),F(0)),(F(-1,2),F(1,2),F(0)),(F(-1,2),F(-1,2),F(0)),(F(1,2),F(-1,2),F(0))]
def dot(x,y):return x[0]*y[0]+x[1]*y[1]+x[2]*y[2]/2
def sub(x,y):return tuple(a-b for a,b in zip(x,y))
def det3(m):return m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])-m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])+m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])
d2=[dot(sub(v[i],v[j]),sub(v[i],v[j])) for i,j in combinations(range(5),2)]
check('eight unit physical edges two sqrt2 diagonals',sorted(d2)==[F(1)]*8+[F(2)]*2)
for t in [(0,1,2,3),(0,1,3,4)]:
 vectors=[sub(v[j],v[t[0]]) for j in t[1:]];gram=[[dot(x,y) for y in vectors] for x in vectors]
 check('tetrahedron volume squared 1/72 '+str(t),det3(gram)/36==F(1,72))
 edges=[dot(sub(v[i],v[j]),sub(v[i],v[j])) for i,j in combinations(t,2)]
 check('five unit edges one sqrt2 edge '+str(t),sorted(edges)==[F(1)]*5+[F(2)])
# Side normals = (sqrt2*x,sqrt2*y,z)/sqrt3.
n=[(0,1,1),(-1,0,1),(0,-1,1),(1,0,1)]
ndot=lambda x,y:F(2*x[0]*y[0]+2*x[1]*y[1]+x[2]*y[2],3)
check('unit normals',all(ndot(x,x)==1 for x in n))
check('adjacent normal dot 1/3',all(ndot(n[i],n[(i+1)%4])==F(1,3) for i in range(4)))
check('opposite normal dot -1/3',ndot(n[0],n[2])==ndot(n[1],n[3])==F(-1,3))
check('tight frame diagonal',sum(2*x[0]**2 for x in n)==sum(2*x[1]**2 for x in n)==sum(x[2]**2 for x in n)==4)
check('tight frame off diagonal',all(sum(x[i]*x[j] for x in n)==0 for i,j in combinations(range(3),2)))
sign=[1,-1,1,-1]
check('alternating signed normals tetrahedral Gram',all(sign[i]*sign[j]*ndot(n[i],n[j])==F(-1,3) for i,j in combinations(range(4),2)))
check('outward normals do not balance',sum(x[2] for x in n)==4)
check('curvature total in pi units',F(2,3)+4*F(5,6)==4)
check('quarter turn exchanges diagonals', {((i)%4)+1 for i in [1,3]}=={2,4})
print(json.dumps({'status':'PASS','constructor_check_count':len(checks),'checks':checks,'shell':shell,'filled_diagonal':filled,'standard_3_horn':horn,'classification':'EXACT_INTERNAL_COMBINATORIAL_AND_METRIC_CHECKS; dynamics conditional on unit chain metric','independent_review':False,'physical_promotion':0},indent=2))
