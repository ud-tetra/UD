"""New exact rational P1 refinement and damping checks; no third-party packages."""
import sys
sys.dont_write_bytecode=True
from fractions import Fraction as F
from itertools import combinations
import json
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def tr(a):return list(map(list,zip(*a)))
def mm(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in tr(b)] for r in a]
def mv(a,x):return [sum(v*w for v,w in zip(r,x)) for r in a]
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def add(a,b,c=1):return [[x+c*y for x,y in zip(r,s)] for r,s in zip(a,b)]
def inv(a):
 n=len(a);x=[list(map(F,r))+s for r,s in zip(a,eye(n))]
 for j in range(n):
  k=next(i for i in range(j,n) if x[i][j]);x[j],x[k]=x[k],x[j];p=x[j][j];x[j]=[z/p for z in x[j]]
  for i in range(n):
   if i!=j:
    p=x[i][j];x[i]=[u-p*v for u,v in zip(x[i],x[j])]
 return [r[n:] for r in x]
def quad(a,x):return dot(x,mv(a,x))
def zeros(n,m):return [[F(0)]*m for _ in range(n)]
points=[(F(0),F(0),F(1)),(F(1,2),F(1,2),F(0)),(F(-1,2),F(1,2),F(0)),(F(-1,2),F(-1,2),F(0)),(F(1,2),F(-1,2),F(0))]
tets=[(0,1,2,3),(0,1,3,4)]
def distance(p,i,j):return sum(w*(x-y)**2 for w,x,y in zip([F(1),F(1),F(1,2)],p[i],p[j]))
def assemble(p,ts,vol):
 n=len(p);K=zeros(n,n);M=zeros(n,n)
 for t,v in zip(ts,vol):
  gram=[[F(distance(p,t[0],t[i])+distance(p,t[0],t[j])-distance(p,t[i],t[j]),2) for j in range(1,4)] for i in range(1,4)];gi=inv(gram);local=zeros(4,4)
  for i in range(1,4):
   for j in range(1,4):local[i][j]=gi[i-1][j-1]
  for i in range(1,4):local[0][i]=local[i][0]=-sum(local[i][1:])
  local[0][0]=sum(sum(r) for r in gi)
  for i,a in enumerate(t):
   for j,b in enumerate(t):K[a][b]+=v*local[i][j];M[a][b]+=v*F(1+int(i==j),20)
 return K,M
def refine(p,ts):
 q=p[:];edges=sorted({e for t in ts for e in combinations(sorted(t),2)});mid={}
 P=eye(len(p))
 for i,j in edges:
  mid[i,j]=len(q);q.append(tuple((x+y)/2 for x,y in zip(p[i],p[j])));row=[F(0)]*len(p);row[i]=row[j]=F(1,2);P.append(row)
 def m(i,j):return mid[tuple(sorted([i,j]))]
 out=[]
 for i,j,k,l in ts:
  a,b,c,d,e,f=m(i,j),m(i,k),m(i,l),m(j,k),m(j,l),m(k,l)
  out.extend([(i,a,b,c),(j,a,d,e),(k,b,d,f),(l,c,e,f),(a,f,b,c),(a,f,c,e),(a,f,e,d),(a,f,d,b)])
 return q,out,P
q,ts,P=refine(points,tets)
K,M=assemble(points,tets,[F(1)]*2);Kf,Mf=assemble(q,ts,[F(1,8)]*16)
p=[F(x) for x in [0,1,0,-1,0]];v=mv(P,p);gp=p+[F(0)]*(len(q)-5);gv=[10*x for x in mv(Mf,v)]
checks=[]
def check(name,x):
 assert x,name
 checks.append(name)

def det3(a):return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
faces={}
for ti,t in enumerate(ts):
 gram=[[F(distance(q,t[0],t[i])+distance(q,t[0],t[j])-distance(q,t[i],t[j]),2) for j in range(1,4)] for i in range(1,4)]
 check('exact child volume ratio1/8 '+str(ti),det3(gram)==F(1,128))
 for face in combinations(sorted(t),3):faces[face]=faces.get(face,0)+1
check('conforming face incidence',all(n in [1,2] for n in faces.values()))
check('24 refined exterior triangles',sum(n==1 for n in faces.values())==24)

check('14 fine nodes and16 tetrahedra',len(q)==14 and len(ts)==16)
check('exact nested stiffness',mm(tr(P),mm(Kf,P))==K)
check('exact nested mass',mm(tr(P),mm(Mf,P))==M)
check('fixed nodal port pulls back',mv(tr(P),gp)==p)
check('fixed distributed port pulls back',mv(tr(P),gv)==p)
check('same coarse port mass',mv(M,p)==[x/10 for x in p])
check('same coarse port stiffness',mv(K,p)==[2*x for x in p])
check('affine field prolonged exactly',v==[x+y for x,y,z in q])
check('fine affine field is NOT omega2 20 eigenvector',mv(Kf,v)!=[20*x for x in mv(Mf,v)])
check('fine total volume mass preserved',sum(sum(r) for r in Mf)==2)
for label,a in [('fineM',Mf),('fine pinnedK',[r[1:] for r in Kf[1:]])]:
 w=[r[:] for r in a]
 for k in range(len(w)):
  pivot=w[k][k];check(label+' positive pivot '+str(k),pivot>0)
  for i in range(k+1,len(w)):
   for j in range(k+1,len(w)):w[i][j]-=w[i][k]*w[k][j]/pivot
check('constant null mode',mv(Kf,[F(1)]*len(q))==[0]*len(q))

# Certified lower gap on the mass-orthogonal complement of constants.
w=mv(Mf,[F(1)]*len(q));U=[]
for i in range(len(q)):
 U.append([F(i==j)-F(i==0)*w[j]/w[0] for j in range(1,len(q))])
def positive_pivots(a):
 b=[r[:] for r in a];piv=[]
 for k in range(len(b)):
  p=b[k][k]
  if p<=0:return None
  piv.append(p)
  for i in range(k+1,len(b)):
   for j in range(k+1,len(b)):b[i][j]-=b[i][k]*b[k][j]/p
 return piv
gap=F(10);gap_matrix=mm(tr(U),mm(add(Kf,Mf,-gap),U));gap_pivots=positive_pivots(gap_matrix)
check('certified normalized spectral gap at least10',gap_pivots is not None)
check('mass orthogonal basis',mv(tr(U),w)==[0]*(len(q)-1))

records=[];mi=inv(Mf)
for gamma in [F(0),F(1,10),F(1)]:
 for sigma in [F(1,2),F(1),F(2)]:
  alpha=sigma*sigma+2*gamma*sigma;A=add(K,M,alpha);Af=add(Kf,Mf,alpha);Ai=inv(Af);xc=mv(inv(A),p);prolong=mv(P,xc);hc=F(20)/(alpha+20)
  check('coarse damped transfer '+str((gamma,sigma)),dot(p,xc)==hc)
  for kind,g in [('retained_point',gp),('fixed_volume',gv)]:
   residual=[x-y for x,y in zip(g,mv(Af,prolong))];hf=quad(Ai,g);error=hf-hc;exact=quad(Ai,residual);upper=quad(mi,residual)/alpha;gap_upper=quad(mi,residual)/(alpha+gap)
   check(kind+' exact error identity '+str((gamma,sigma)),error==exact)
   check(kind+' strict refinement difference '+str((gamma,sigma)),error>0)
   check(kind+' zero constant residual '+str((gamma,sigma)),sum(residual)==0)
   check(kind+' gap residual upper bound '+str((gamma,sigma)),0<error<=gap_upper<=upper)
   check(kind+' mass residual upper bound '+str((gamma,sigma)),0<error<=upper)
   # Additional passive damping at the identical force/readout port.
   for zeta in [F(0),F(1,5)]:
    gg=[[x*y for y in g] for x in g];az=add(Af,gg,zeta*sigma);hz=quad(inv(az),g)
    check(kind+' passive rank1 damping identity '+str((gamma,sigma,zeta)),hz==hf/(1+zeta*sigma*hf))
   records.append({'gamma':gamma,'sigma':sigma,'port':kind,'coarse_H':hc,'fine_H':hf,'difference':error,'residual_mass_upper_bound':upper,'certified_gap_upper_bound':gap_upper})
print(json.dumps({'status':'PASS','classification':'EXACT_CONDITIONAL_DAMPING_AND_REFINEMENT_COUNTEREXAMPLE','check_count':len(checks),'checks':checks,'gap_lower_bound':gap,'gap_positive_pivots':gap_pivots,'fine_vertices':q,'fine_tetrahedra':ts,'prolongation':P,'K_coarse':K,'M_coarse':M,'K_fine':Kf,'M_fine':Mf,'point_port':gp,'volume_port':gv,'records':records,'independent_review':False,'physical_promotion':0},indent=2,default=str))
