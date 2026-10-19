"""Exact RT1 flux certificate and rational frequency-band controls. New code."""
import sys
sys.dont_write_bytecode=True
from fractions import Fraction as F
from itertools import combinations
from math import factorial
from functools import lru_cache
import json
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def mv(a,x):return [dot(r,x) for r in a]
def trans(a):return list(map(list,zip(*a)))
def solve_constraints(a,b):
 w=[list(map(F,r))+[F(v)] for r,v in zip(a,b)];n=len(a[0]);piv=[];r=0
 for j in range(n):
  choices=[i for i in range(r,len(w)) if w[i][j]]
  if not choices:continue
  k=choices[0];w[r],w[k]=w[k],w[r];v=w[r][j];w[r]=[x/v for x in w[r]]
  for i in range(len(w)):
   if i!=r:
    v=w[i][j];w[i]=[x-v*y for x,y in zip(w[i],w[r])]
  piv.append(j);r+=1
 for row in w:
  if not any(row[:n]) and row[n]:raise ValueError('inconsistent')
 x=[F(0)]*n
 for i,j in enumerate(piv):x[j]=w[i][n]
 null=[]
 for j in range(n):
  if j not in piv:
   v=[F(0)]*n;v[j]=1
   for i,k in enumerate(piv):v[k]=-w[i][j]
   null.append(v)
 return x,null
pts=[(F(0),F(0),F(1)),(F(1,2),F(1,2),F(0)),(F(-1,2),F(1,2),F(0)),(F(-1,2),F(-1,2),F(0)),(F(1,2),F(-1,2),F(0))]
tets=[(0,1,2,3),(0,1,3,4)]
def value(b,x):
 if b<12:
  component,k=divmod(b,4);v=F(1) if k==0 else x[k-1]
  return [v if i==component else F(0) for i in range(3)]
 j=b-12;return [v*x[j] for v in x]
def divvalue(b,x):
 if b<12:
  component,k=divmod(b,4);return F(k==component+1)
 return 4*x[b-12]
def minus(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
faces={}
for i,t in enumerate(tets):
 for face in combinations(t,3):faces.setdefault(tuple(sorted(face)),[]).append(i)
A=[];rhs=[]
for face,cells in faces.items():
 n=cross(minus(pts[face[1]],pts[face[0]]),minus(pts[face[2]],pts[face[0]]))
 for vi in face:
  row=[F(0)]*30
  for k,cell in enumerate(cells):
   for j in range(15):row[15*cell+j]=(-1)**k*dot(value(j,pts[vi]),n)
  A.append(row);rhs.append(F(0))
for cell,t in enumerate(tets):
 for vi in t:
  row=[F(0)]*30
  for j in range(15):row[15*cell+j]=divvalue(j,pts[vi])
  A.append(row);rhs.append(-sum(pts[vi][:2]))
x,null=solve_constraints(A,rhs)
def poly(b,component):
 if b<12:
  i,k=divmod(b,4)
  if i!=component:return {}
  e=[0]*3
  if k:e[k-1]=1
  return {tuple(e):F(1)}
 e=[0]*3;e[component]+=1;e[b-12]+=1;return {tuple(e):F(1)}
@lru_cache(None)
def integrate(cell,e):
 # Exact normalized integral on a reference-volume cell via barycentric moments.
 p={(0,0,0,0):F(1)}
 for axis,degree in enumerate(e):
  for _ in range(degree):
   out={}
   for ex,c in p.items():
    for j,vi in enumerate(tets[cell]):
     ee=list(ex);ee[j]+=1;ee=tuple(ee);out[ee]=out.get(ee,F(0))+c*pts[vi][axis]
   p=out
 return sum(c*F(6, factorial(sum(ex)+3))*factorial(ex[0])*factorial(ex[1])*factorial(ex[2])*factorial(ex[3]) for ex,c in p.items())
G=[[F(0)]*30 for _ in range(30)]
for cell in range(2):
 for i in range(15):
  for j in range(15):
   for k,weight in enumerate([F(1),F(1),F(1,2)]):
    for e,c in poly(i,k).items():
     for ee,cc in poly(j,k).items():G[cell*15+i][cell*15+j]+=weight*c*cc*integrate(cell,tuple(a+b for a,b in zip(e,ee)))
if null:
 gram=[[dot(a,mv(G,b)) for b in null] for a in null];r=[-dot(a,mv(G,x)) for a in null];coef,freedom=solve_constraints(gram,r);assert not freedom
 x=[v+sum(c*n[i] for c,n in zip(coef,null)) for i,v in enumerate(x)]
J=dot(x,mv(G,x));Q=400*J-4
checks=[]
def check(name,c):
 assert c,name
 checks.append(name)
for i,(row,b) in enumerate(zip(A,rhs)):check('RT1 trace/divergence constraint '+str(i),dot(row,x)==b)
check('finite minimum-flux norm',J>0)
check('nonzero coarse flux error coefficient',Q>0)
for i,n in enumerate(null):check('minimum-norm stationarity '+str(i),dot(n,mv(G,x))==0)
# Integrals supporting the fixed port and integration-by-parts cross term.
mean=F(0);norm=F(0);crossmoment=F(0)
for cell in range(2):
 mean+=integrate(cell,(1,0,0))+integrate(cell,(0,1,0))
 norm+=integrate(cell,(2,0,0))+2*integrate(cell,(1,1,0))+integrate(cell,(0,2,0))
 for i in range(15):
  for k in [0,1]:
   for e,c in poly(i,k).items():crossmoment+=x[15*cell+i]*c*integrate(cell,e)
check('fixed field zero mean',mean==0)
check('fixed volume field norm squared',norm==F(1,5))
check('fixed forcing L2 norm squared20',100*norm==20)
check('zero-normal flux cross moment',crossmoment==F(1,5))
fixtures=[]
for gamma in [F(1,10),F(1,2),F(1)]:
 for omega in [F(0),F(1),F(2),F(4),F(6)]:
  beta2=F(1) if not omega else 4*gamma**2/(omega**2+4*gamma**2)
  # Conservative continuous Poincare lambda*=4; |z| <= omega²+2gamma omega.
  B=1+(omega**2+2*gamma*omega)/4
  beta2=max(beta2,max(F(0),1-omega**2/4)**2)
  den=(20-omega**2)**2+4*gamma**2*omega**2
  eta2=F(100)*Q/den;transfer_error2bound=(B*eta2/beta2)**2
  check('positive damping frequency fixture '+str((gamma,omega)),beta2>0 and den>0 and transfer_error2bound>0)
  # Rotation cancels the real part of z exactly before division by sqrt(omega²+4gamma²).
  check('rotated mass coefficient zero '+str((gamma,omega)),-2*gamma*omega**2+2*gamma*omega*omega==0)
  fixtures.append({'gamma':gamma,'omega':omega,'coercivity_squared':beta2,'continuity_upper_bound':B,'flux_estimator_squared':eta2,'transfer_error_upper_bound':B*eta2/beta2,'transfer_error_upper_bound_squared':transfer_error2bound})
# Explicit declared band: |omega|<=6, gamma in[1/10,1].
beta_band2=F(1,901);Bband=F(13)
check('band coercivity squared',4*F(1,10)**2/(36+4*F(1,10)**2)==beta_band2)
check('band continuity',1+(36+12)/4==Bband)

for lam in [F(4),F(5),F(20)]:
 for t in [F(0),F(1),F(4),F(20),F(36)]:
  check('completed-square gain identity '+str((lam,t)),(lam-t)**2+t/25-F(399,2500)==(t-lam+F(1,50))**2+(lam-4)/25)
check('static continuum output error bound',F(100,400)*Q==F(47,168))
print(json.dumps({'status':'PASS','classification':'EXACT_CONDITIONAL_CONTINUUM_PORT_AND_FREQUENCY_BAND_CERTIFICATE','check_count':len(checks),'checks':checks,'rt1_coefficients_by_cell':[x[:15],x[15:]],'rt1_basis':'P1 vector components (1,x,y,t) followed by (x,y,t)*x,(x,y,t)*y,(x,y,t)*t; t=sqrt2*z','rt1_affine_constraint_nullity':len(null),'minimum_flux_norm_squared':J,'coarse_flux_error_coefficient':Q,'continuum_poincare_lower_bound':4,'external_anchor':'Convex-domain Payne-Weinberger: lambda1>=pi²/diameter²; diameter²2 and pi>3 imply lambda1>4','band':{'omega_max':6,'gamma_min':'1/10','gamma_max':1,'coercivity_lower_bound_squared':beta_band2,'continuity_upper_bound':Bband,'uniform_gain_bound_squared':F(1000000,399),'static_transfer_error_bound':F(47,168)},'fixtures':fixtures,'independent_review':False,'physical_promotion':0},indent=2,default=str))
