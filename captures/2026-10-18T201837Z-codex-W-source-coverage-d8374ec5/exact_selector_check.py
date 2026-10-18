from fractions import Fraction as F
from itertools import combinations,permutations
import json,time
def tr(a): return list(map(list,zip(*a)))
def z(n,m=None): return [[F(0) for _ in range(m or n)] for _ in range(n)]
def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def add(a,b): return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(a,c): return [[x*c for x in r] for r in a]
def mul(a,b):
 out=z(len(a),len(b[0]))
 for i,r in enumerate(a):
  for k,x in enumerate(r):
   if x:
    for j,y in enumerate(b[k]):
     if y:out[i][j]+=x*y
 return out
def trace(a):return sum(a[i][i] for i in range(len(a)))
def parity(seq):return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
SIM=[s for k in range(1,5) for s in combinations(range(5),k)];IDX={s:i for i,s in enumerate(SIM)};N=len(SIM)
def operator(tets):
 keep={s for t in tets for k in range(1,5) for s in combinations(t,k)};a=z(N)
 for s in keep:
  if len(s)==1:continue
  col=IDX[s]
  for j in range(len(s)):
   row=IDX[s[:j]+s[j+1:]];v=F((-1)**j);a[row][col]=v;a[col][row]=-v
 return a
def representation(p):
 image=[];sign=[]
 for s in SIM:
  seq=tuple(p[x] if x<4 else 4 for x in s);image.append(IDX[tuple(sorted(seq))]);sign.append(parity(seq))
 return image,sign
def conj(a,rep):
 image,sign=rep;out=z(N)
 for i in range(N):
  for j in range(N):out[image[i]][image[j]]=a[i][j]*sign[i]*sign[j]
 return out
def verify():
 a=operator(list(combinations(range(5),4)));am=operator([(0,1,2,3),(0,1,2,4)]);ap=operator([(0,1,3,4),(0,2,3,4),(1,2,3,4)])
 d=add(scale(mul(ap,ap),-1),mul(am,am));pstd=z(N);dbar=z(N);reps=[]
 for perm in permutations(range(4)):
  rep=representation(perm);reps.append(rep);chi=sum(i==perm[i] for i in range(4))-1
  for j,(i,s) in enumerate(zip(*rep)):pstd[i][j]+=F(chi,8)*s
  dbar=add(dbar,scale(conj(d,rep),F(1,24)))
 assert mul(pstd,pstd)==pstd and trace(pstd)==12
 rr=mul(mul(pstd,dbar),pstd)
 c=scale(add(rr,scale(mul(mul(tr(a),rr),a),F(1,5))),F(1,2))
 poly=add(add(mul(c,c),scale(c,-F(23,8))),scale(pstd,F(129,160)))
 assert poly==z(N),'source selector polynomial mismatch'
 assert mul(c,a)==mul(a,c)
 # P=P0+sqrt(8065)*P1, without numerical approximation.
 p0=scale(pstd,F(1,2));p1=scale(add(scale(pstd,F(115,2)),scale(c,-40)),F(1,8065))
 assert add(mul(p0,p0),scale(mul(p1,p1),8065))==p0
 assert add(mul(p0,p1),mul(p1,p0))==p1
 assert trace(p0)==6 and trace(p1)==0
 a2=mul(a,a)
 for p in [p0,p1]:
  assert mul(p,a)==mul(a,p)
  assert mul(a2,p)==scale(p,-5)
  assert all(conj(p,r)==p for r in reps)
 v=z(N)
 for i in range(4):
  for j in range(4):v[i][j]=F(i==j)-F(1,4)
 assert mul(mul(v,p0),v)==scale(v,F(1,2))
 assert mul(mul(v,p1),v)==scale(v,F(89,2*8065))
 iso0=add(mul(mul(p0,a),p0),scale(mul(mul(p1,a),p1),8065))
 iso1=add(mul(mul(p0,a),p1),mul(mul(p1,a),p0))
 assert mul(mul(v,iso0),v)==z(N) and mul(mul(v,iso1),v)==z(N)
 return {'status':'PASS','ambient_dimension':N,'standard_rank':12,'selected_rank':6,'field':'Q(sqrt(8065)) via rational coefficient pairs','selector_polynomial':'C^2-(23/8)C+(129/160)P_std=0','vertex_projection':'alpha=(1+89/sqrt(8065))/2','isotropy':'P0 P_evt A P_evt P0=0','scope':'exact finite carrier/selector construction;lower-response selection principle supplied'},(a,p0,p1)
if __name__=='__main__': print(json.dumps(verify()[0]))
