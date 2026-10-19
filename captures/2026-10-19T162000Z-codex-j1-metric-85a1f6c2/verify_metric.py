"""Exact conditional P1 scalar-wave benchmark. New code, standard library."""
import sys
sys.dont_write_bytecode=True
from fractions import Fraction as F
from itertools import combinations
import json
def mat(n,m):return [[F(0) for _ in range(m)] for _ in range(n)]
def tr(a):return list(map(list,zip(*a)))
def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in tr(b)] for row in a]
def add(a,b,scale=1):return [[x+scale*y for x,y in zip(r,s)] for r,s in zip(a,b)]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def inv(a):
 n=len(a);x=[list(map(F,r))+s for r,s in zip(a,eye(n))]
 for j in range(n):
  pivot=next(i for i in range(j,n) if x[i][j]);x[j],x[pivot]=x[pivot],x[j];v=x[j][j];x[j]=[z/v for z in x[j]]
  for i in range(n):
   if i!=j:
    v=x[i][j];x[i]=[u-v*w for u,w in zip(x[i],x[j])]
 return [r[n:] for r in x]
def cp(a):
 b=eye(len(a));out=[F(1)]
 for k in range(1,len(a)+1):
  ab=mm(a,b);c=-sum(ab[i][i] for i in range(len(a)))/k;out.append(c);b=add(ab,eye(len(a)),c)
 return out
def mv(a,x):return [sum(v*w for v,w in zip(r,x)) for r in a]
def quad(a,x):return sum(v*w for v,w in zip(x,mv(a,x)))
def model(tets,dist,vol,n):
 K=mat(n,n);M=mat(n,n)
 for t,v in zip(tets,vol):
  g=[[F(dist(t[0],t[i])+dist(t[0],t[j])-dist(t[i],t[j]),2) for j in range(1,4)] for i in range(1,4)];gi=inv(g)
  local=mat(4,4)
  for i in range(1,4):
   for j in range(1,4):local[i][j]=gi[i-1][j-1]
  for i in range(1,4):local[i][0]=local[0][i]=-sum(local[i][1:])
  local[0][0]=sum(sum(r) for r in gi)
  for i,a in enumerate(t):
   for j,b in enumerate(t):K[a][b]+=v*local[i][j];M[a][b]+=v*F(1+int(i==j),20)
 return K,M
# Coordinates (x,y,z*sqrt2): exact Euclidean Gram diag(1,1,1/2); a=1.
pts=[(0,0,1),(F(1,2),F(1,2),0),(F(-1,2),F(1,2),0),(F(-1,2),F(-1,2),0),(F(1,2),F(-1,2),0),(0,0,0)]
def dist(i,j):return sum(F(w)*(x-y)**2 for w,x,y in zip([1,1,F(1,2)],pts[i],pts[j]))
def regdist(i,j):return F(0) if i==j else F(8,3) if {i,j}=={2,4} else F(1)
tA=[(0,1,2,3),(0,1,3,4)];tB=[(0,1,2,4),(0,2,3,4)];tC=[(0,5,1,2),(0,5,2,3),(0,5,3,4),(0,5,4,1)]
models={'j1_diag13':model(tA,dist,[F(1)]*2,5),'j1_diag24':model(tB,dist,[F(1)]*2,5),'regular_kminus':model(tA,regdist,[F(1)]*2,5),'j1_center':model(tC,dist,[F(1,2)]*4,6)}
# All integrals divided by V_ref=sqrt2/12; it cancels in frequencies.
checks=[]
def check(name,x):
 assert x,name
 checks.append(name)
def schur(a):
 return [[a[i][j]-a[i][5]*a[5][j]/a[5][5] for j in range(5)] for i in range(5)]
def permute(a,p):return [[a[p[i]][p[j]] for j in range(len(p))] for i in range(len(p))]
rotation=[0,2,3,4,1];p=[F(0),F(1),F(0),F(-1),F(0)]
records={}
for name,(K,M) in models.items():
 n=len(K);check(name+' symmetric K/M',K==tr(K) and M==tr(M));check(name+' constant zero stiffness',mv(K,[1]*n)==[0]*n)
 check(name+' total mass',sum(sum(r) for r in M)==2)
 check(name+' nullity one',cp(mm(inv(M),K))[-1]==0 and cp(mm(inv(M),K))[-2]!=0)
 # Exact LDL positivity of M, and K with constant mode pinned.
 for label,a in [('M',M),('pinnedK',[row[1:] for row in K[1:]])]:
  work=[r[:] for r in a]
  for k in range(len(work)):
   pivot=work[k][k];check(name+' '+label+' positive pivot '+str(k),pivot>0)
   for i in range(k+1,len(work)):
    for j in range(k+1,len(work)):work[i][j]-=work[i][k]*work[k][j]/pivot
 records[name]={'K':K,'M':M,'squared_frequency_polynomial':cp(mm(inv(M),K))}
 if n==5:
  records[name]['fixed_readout']={'port':[str(x) for x in p],'static_compliance':quad(inv(add(K,[[F(1,n*n) for _ in range(n)] for _ in range(n)])),p),'initial_port_acceleration':-quad(mm(inv(M),K),p),'rayleigh_quotient':quad(K,p)/quad(M,p)}
check('quarter turn covariance K',permute(models['j1_diag13'][0],rotation)==models['j1_diag24'][0])
check('quarter turn covariance M',permute(models['j1_diag13'][1],rotation)==models['j1_diag24'][1])
check('diagonal spectra equal',records['j1_diag13']['squared_frequency_polynomial']==records['j1_diag24']['squared_frequency_polynomial'])
check('metric distinguishes regular Kminus',records['j1_diag13']['squared_frequency_polynomial']!=records['regular_kminus']['squared_frequency_polynomial'])
centerK,centerM=models['j1_center'];check('center D4 K',permute(centerK,rotation+[5])==centerK);check('center D4 M',permute(centerM,rotation+[5])==centerM)
records['center_static_condensation']={'K_boundary':schur(centerK),'fixed_port_compliance':quad(inv(add(schur(centerK),[[F(1,25) for _ in range(5)] for _ in range(5)])),p)}
# For q=x and q=y, P1 interpolation is exact in every cell, including center.
for name,(K,M) in models.items():
 if name=='regular_kminus':continue
 for axis in [0,1]:
  x=[q[axis] for q in pts[:len(K)]]
  check(name+' affine gradient energy '+str(axis),quad(K,x)==2)
  check(name+' affine volume mass '+str(axis),quad(M,x)==F(1,10))
check('diagonal A fixed port compliance',records['j1_diag13']['fixed_readout']['static_compliance']==F(1))

def polyroots(roots):
 out=[F(1)]
 for root in roots:
  nxt=[F(0)]*(len(out)+1)
  for i,c in enumerate(out):nxt[i]+=c;nxt[i+1]-=root*c
  out=nxt
 return out
for name,roots in [('j1_diag13',[0,20,20,40,80]),('j1_diag24',[0,20,20,40,80]),('regular_kminus',[0,15,40,40,40]),('j1_center',[0,20,20,40,40,160])]:
 check(name+' factored squared spectrum',records[name]['squared_frequency_polynomial']==polyroots(roots))
 records[name]['squared_frequencies']=roots
 K,M=models[name];n=len(K);port=p+([F(0)] if n==6 else []);omega2=40 if name=='regular_kminus' else 20
 check(name+' exact port mass',mv(M,port)==[v/10 for v in port])
 check(name+' exact port stiffness',mv(K,port)==[F(omega2,10)*v for v in port])
 check(name+' zero-sum port',sum(port)==0)
 records[name]['port_transfer']={'force':'p*u','readout':'y=p^T*q','H_s':'20/(s^2+'+str(omega2)+')','static_compliance':str(F(20,omega2))}
 for z in [-1,1,7,19,21]:
  resolvent=inv(add(K,M,-z))
  check(name+' exact driven resolvent at squared parameter '+str(z),quad(resolvent,port)==F(20,omega2-z))
 if name!='regular_kminus':
  other=[F(0),F(0),F(1),F(0),F(-1)]+([F(0)] if n==6 else [])
  check(name+' second square-port mode',mv(K,other)==[2*v for v in other] and mv(M,other)==[v/10 for v in other])
  for z in [1,7]:check(name+' zero cross-port transfer '+str(z),sum(x*y for x,y in zip(other,mv(inv(add(K,M,-z)),port)))==0)

print(json.dumps({'status':'PASS','classification':'EXACT_CONDITIONAL_P1_SCALAR_WAVE_BENCHMARK','check_count':len(checks),'checks':checks,'records':records,'physical_promotion':0,'independent_review':False},indent=2,default=str))
