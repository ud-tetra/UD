"""Reconstruct the finite carrier; no archived program imports."""
from pathlib import Path
from fractions import Fraction as F
import json,numpy as np,scipy.sparse as sp

def build(root):
 D=json.loads((Path(root)/'COMPLEX_AND_ACTION.json').read_text())
 C=[[tuple(t) for t in cs] for cs in D['simplices']];ids=[{t:i for i,t in enumerate(cs)} for cs in C]
 off=np.cumsum([0]+list(map(len,C)));B=[]
 for d in [1,2,3]:
  rr=[];cc=[];vv=[]
  for j,s in enumerate(C[d]):
   for k in range(d+1):rr.append(ids[d-1][s[:k]+s[k+1:]]);cc.append(j);vv.append((-1)**k)
  B.append(sp.csc_matrix((vv,(rr,cc)),shape=(len(C[d-1]),len(C[d])),dtype=np.int64))
 B1,B2,B3=B;L=(B1@B1.T).toarray();I=np.eye(120,dtype=object);Lo=L.astype(object)
 def polymul(p,q):
  z=[0]*(len(p)+len(q)-1)
  for i,x in enumerate(p):
   for j,y in enumerate(q):z[i+j]+=x*y
  return z
 q=[1]
 for p in [[80,-20,1],[36,-18,1],[-9,1],[-12,1],[-14,1],[-15,1]]:q=polymul(q,p)
 Z=np.zeros((120,120),dtype=object);power=I.copy()
 for k in range(8):Z-=120*q[k+1]*power;power=power@Lo
 Z+=q[1]*np.ones((120,120),dtype=object);den=120*q[0]
 assert np.array_equal(Lo@Z,q[0]*(120*I-np.ones((120,120),dtype=object)))
 V=[tuple(tuple(x) for x in v) for v in D['vertices']];vid={v:i for i,v in enumerate(V)}
 neg=lambda x:(-x[0],-x[1])
 mul=lambda x,y:(x[0]*y[0]+x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
 sm=lambda xs:(sum(x[0] for x in xs),sum(x[1] for x in xs))
 def qm(x,y):
  z=[sm([mul(x[0],y[0])]+[neg(mul(x[i],y[i])) for i in [1,2,3]])]
  for i,j,k in [(1,2,3),(2,3,1),(3,1,2)]:z.append(sm([mul(x[0],y[i]),mul(x[i],y[0]),mul(x[j],y[k]),neg(mul(x[k],y[j]))]))
  assert all(a%2==b%2==0 for a,b in z)
  return tuple((a//2,b//2) for a,b in z)
 conj=lambda x:(x[0],)+tuple(neg(t) for t in x[1:])
 one=((2,0),(0,0),(0,0),(0,0));u=vid[one];g=tuple(tuple(x) for x in D['right_generator']);q0=one;H={q0}
 for _ in range(9):q0=qm(q0,g);H.add(q0)
 HH=sorted({frozenset(qm(qm(conj(v),h),v) for h in H) for v in V},key=lambda h:sorted(h));target=HH.index(frozenset(H))
 def action(q):
  vp=[vid[qm(x,q)] for x in V];rr=[];cc=[];vv=[]
  for d,cs in enumerate(C):
   for j,s in enumerate(cs):
    t=tuple(vp[k] for k in s);sign=(-1)**sum(t[i]>t[j] for i in range(len(t)) for j in range(i+1,len(t)))
    rr.append(int(off[d])+ids[d][tuple(sorted(t))]);cc.append(int(off[d])+j);vv.append(sign)
  return sp.csc_matrix((vv,(rr,cc)),shape=(2640,2640),dtype=np.int64)
 S=[sum((action(q) for q in h),sp.csc_matrix((2640,2640),dtype=np.int64)) for h in HH]
 A=sp.bmat([[None,-B1,None,None],[B1.T,None,-B2,None],[None,B2.T,None,-B3],[None,None,B3.T,None]],format='csc')
 e=ids[1][tuple(sorted((u,vid[g])))];be=B1[:,e].toarray().ravel()
 def edge_operator(edge):
  be0=B1[:,edge].toarray().ravel();rr=[];cc=[];vv=[]
  for i in np.flatnonzero(be0):rr.extend([int(i),120+edge]);cc.extend([120+edge,int(i)]);vv.extend([-int(be0[i]),int(be0[i])])
  return sp.csc_matrix((vv,(rr,cc)),shape=(2640,2640))
 Lplus=np.array(Z,dtype=float)/den
 def protected(c):
  z=c.copy();z[:120]=0;z[120:840]-=B1.T@(Lplus@(B1@z[120:840]));return z
 def scores(c):return np.array([float(c@(s@c))/10 for s in S])
 incident=[]
 for j,(a,b) in enumerate(C[1]):
  if u in (a,b):
   v=b if a==u else a;hh=next(k for k,h in enumerate(HH) if V[v] in h)
   incident.append(dict(edge=j,neighbor=v,subgroup=hh,outward_sign=-int(B1[u,j])))
 return dict(D=D,C=C,B=B,L=L,Z=Z,den=den,A=A,S=S,u=u,e=e,be=be,target=target,HH=HH,incident=incident,edge_operator=edge_operator,protected=protected,scores=scores)

def scalar_recurrence(seq):
 """Exact Berlekamp-Massey over Q; returned monic polynomial descending."""
 C=[F(1)];B=[F(1)];degree=0;age=1;pivot=F(1)
 for n in range(len(seq)):
  disc=F(seq[n])+sum(C[i]*seq[n-i] for i in range(1,degree+1))
  if disc==0:age+=1;continue
  old=C.copy();factor=-disc/pivot
  C.extend([F(0)]*max(0,len(B)+age-len(C)))
  for i,b in enumerate(B):C[i+age]+=factor*b
  if 2*degree<=n:degree=n+1-degree;B=old;pivot=disc;age=1
  else:age+=1
 return C[:degree+1]

def bareiss_det(a):
 a=[list(map(int,r)) for r in a];n=len(a);prev=1;sign=1
 for k in range(n-1):
  if a[k][k]==0:
   p=next((i for i in range(k+1,n) if a[i][k]),None)
   if p is None:return 0
   a[k],a[p]=a[p],a[k];sign=-sign
  pivot=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    value=a[i][j]*pivot-a[i][k]*a[k][j];assert value%prev==0;a[i][j]=value//prev
   a[i][k]=0
  prev=pivot
 return sign*a[-1][-1]
