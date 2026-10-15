"""Directed fixed-point integer intervals certify the critical quartic coefficients.
Every endpoint is an integer multiple of 10^-60. All arithmetic rounds outward.
No floating-point calculation is used in the certificate.
"""
from fractions import Fraction
from math import isqrt
Q=10**60
class I:
 def __init__(self,x=0,hi=None):
  if isinstance(x,I):self.lo,self.hi=x.lo,x.hi;return
  if hi is not None:self.lo,self.hi=int(x),int(hi);return
  f=Fraction(x);self.lo=f.numerator*Q//f.denominator;self.hi=-((-f.numerator*Q)//f.denominator)
 def __add__(a,b):
  b=I(b);return I(a.lo+b.lo,a.hi+b.hi)
 __radd__=__add__
 def __neg__(a):return I(-a.hi,-a.lo)
 def __sub__(a,b):return a+-I(b)
 def __rsub__(a,b):return I(b)+-a
 def __mul__(a,b):
  b=I(b);x=[a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi];return I(min(x)//Q,-((-max(x))//Q))
 __rmul__=__mul__
 def __truediv__(a,b):
  b=I(b);assert not b.lo<=0<=b.hi,'interval denominator includes zero'
  endpoints=[Fraction(x*Q,y) for x in [a.lo,a.hi] for y in [b.lo,b.hi]]
  lo=min(endpoints);hi=max(endpoints);return I(lo.numerator//lo.denominator,-((-hi.numerator)//hi.denominator))
 def __rtruediv__(a,b):return I(b)/a
 def __pow__(a,n):
  assert n>=0
  if n==0:return I(1)
  if n%2:return a*(a**(n-1))
  z=a**(n//2);l=0 if z.lo<=0<=z.hi else min(z.lo*z.lo,z.hi*z.hi);h=max(z.lo*z.lo,z.hi*z.hi);return I(l//Q,-((-h)//Q))
 def sqrt(a):
  assert a.lo>=0
  l=isqrt(a.lo*Q);h=isqrt(a.hi*Q)
  if h*h<a.hi*Q:h+=1
  return I(l,h)
 def bounds(a):return {'lower_numerator':str(a.lo),'upper_numerator':str(a.hi),'denominator':str(Q)}

def solve(A,b):
 A=[[I(x) for x in row] for row in A];b=[I(x) for x in b];n=len(b)
 for k in range(n):
  assert A[k][k].lo>0,'positive pivot certificate failed'
  for i in range(k+1,n):
   z=A[i][k]/A[k][k]
   for j in range(k+1,n):A[i][j]=A[i][j]-z*A[k][j]
   b[i]=b[i]-z*b[k];A[i][k]=I(0)
 out=[I(0)]*n
 for i in reversed(range(n)):out[i]=(b[i]-sum((A[i][j]*out[j] for j in range(i+1,n)),I(0)))/A[i][i]
 return out

def certificate(g):
 d=I(10).sqrt();rho=(8+2*d).sqrt();ell=16*(10+d)/9;qlevels=[I(1),rho/3,(1+d)/3,4*(1+d)/(3*rho)];q=[qlevels[len(t)-1] for t in g['simplices']]
 asum=(28+17*d)/9;bprod=(26+10*d)/3;lp=(asum+(asum**2-4*bprod).sqrt())/2;lm=(asum-(asum**2-4*bprod).sqrt())/2
 t_sum=(4+5*d)/3;t_prod=14*(d-1)/3;tp=(t_sum+(t_sum**2-4*t_prod).sqrt())/2;tm=(t_sum-(t_sum**2-4*t_prod).sqrt())/2
 # Order certificate: the standard upper root exceeds every other retained weighted root.
 assert lp.lo>(d+2).hi and (d+2).lo>tp.hi and tp.lo>lm.hi and lm.lo>tm.hi and tm.lo>0
 w0=rho/(3*ell);kc=4*w0/lp;c=(1+d)/3;h=(8-d)/3;gamma=-lp+(5+4*d)/3
 T=[[I(int(g['T'][i,j])) for j in range(15)] for i in range(15)]
 A=[[(rho if i==j else I(0))-T[i][j]+q[i]*q[j]/ell for j in range(15)] for i in range(15)]
 def quartic(a):
  x=[]
  for i,j in g['edges']:
   lo=g['simplices'][i];hi=g['simplices'][j];added=next(u for u in hi if u not in lo)
   if len(lo)==1:x.append(I(a[lo[0]]+3*a[added]))
   elif len(lo)==2:x.append(gamma*sum(a[u] for u in lo)+(2*gamma-4/c)*a[added])
   else:x.append(4*(1-c*gamma)/h*a[added])
  gg=[I(0) for _ in range(15)];edge4=I(0)
  for e,(i,j) in enumerate(g['edges']):gg[i]=gg[i]+x[e]**2*q[j];gg[j]=gg[j]+x[e]**2*q[i];edge4=edge4+q[i]*q[j]*x[e]**4
  z=solve(A,gg);gpg=sum((gg[i]*z[i] for i in range(15)),I(0))-sum((q[i]*gg[i] for i in range(15)),I(0))**2/ell
  curl4=sum((sum((int(g['C'][d,e])*x[e] for e in range(28) if g['C'][d,e]),I(0))**4 for d in range(18)),I(0))
  return -edge4/(6*ell)-gpg/(2*ell)+kc*curl4/24
 q1=quartic([1,-1,0,0]);q2=quartic([1,1,-1,-1]);A4=(q2-2*q1)/8;B4=q1/2-2*A4
 assert A4.lo>11*Q and A4.hi<12*Q
 assert B4.lo>12*Q and B4.hi<13*Q
 # Also certify improvement over the previous unweighted sufficient bound.
 safe=4*w0/(6+I(2).sqrt());assert kc.lo>safe.hi
 return {'status':'PASS','method':'Exact outward-rounded integer intervals on grid 10^-60; positive Gaussian pivots; no floating-point arithmetic','standard_upper_root':lp.bounds(),'critical_kappa_per_N':kc.bounds(),'A4':A4.bounds(),'B4':B4.bounds(),'readable_bounds':['11 < A4 < 12','12 < B4 < 13'],'critical_quartic':'N[A4*(sum a_i^2)^2+B4*sum a_i^4] with sum a_i=0','conclusion':'Strictly positive critical quartic; local nonlinear orbital stability includes equality at kappa_critical.','independent_review':'PENDING','physical_promotion':0}
