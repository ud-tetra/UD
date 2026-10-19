"""Exact Gaussian-rational checks of inexact collocated output correction."""
from fractions import Fraction as F
import json
def c(a=0,b=0):return F(a),F(b)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[0],-x[1]
def sub(x,y):return add(x,neg(y))
def mul(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def scale(a,x):return a*x[0],a*x[1]
def inv(x):
 n=x[0]**2+x[1]**2;return x[0]/n,-x[1]/n
def norm2(x):return x[0]**2+x[1]**2
checks=[];fixtures=[]
def check(name,x):
 assert x,name
 checks.append(name)
check('exact flux expansion',400*F(43,3360)-40*F(1,5)+4==F(47,42))
for omega in [F(0),F(1),F(4),F(6)]:
 gamma=F(1,10);z=c(-omega**2,2*gamma*omega);a=add(c(4),scale(F(1,5),z));exact=scale(2,inv(a));H=scale(2,exact)
 beta2=4*gamma**2/(omega**2+4*gamma**2);B=1+(omega**2+2*gamma*omega)/4
 for delta in [c(F(1,100)),c(F(1,100),F(-1,200))]:
  t=add(exact,delta);output=scale(2,t);rp=sub(c(2),mul(a,t));rv=mul(rp,t);corrected=add(output,rv);error=sub(exact,t)
  eps2=norm2(rp)/4;state2=4*norm2(error)
  check('corrected bilinear identity '+str((omega,delta)),sub(H,corrected)==mul(a,mul(error,error)))
  check('raw error plus residual identity '+str((omega,delta)),sub(H,output)==add(mul(a,mul(error,error)),rv))
  check('algebraic dual norm state bound '+str((omega,delta)),state2<=eps2/beta2)
  check('raw output residual bound '+str((omega,delta)),norm2(sub(H,output))<=5*eps2/beta2)
  check('quadratic corrected output bound '+str((omega,delta)),norm2(sub(H,corrected))<=B**2*state2**2)
  half=add(exact,scale(F(1,2),delta));outh=scale(2,half);rph=sub(c(2),mul(a,half));corrh=add(outh,mul(rph,half))
  check('raw output first order scaling '+str((omega,delta)),norm2(sub(H,output))==4*norm2(sub(H,outh)))
  check('corrected output second order scaling '+str((omega,delta)),norm2(sub(H,corrected))==16*norm2(sub(H,corrh)))
  fixtures.append({'omega':omega,'gamma':gamma,'algebraic_residual_dual_norm_squared':eps2,'raw_output_error_squared':norm2(sub(H,output)),'corrected_output_error_squared':norm2(sub(H,corrected))})
print(json.dumps({'status':'PASS','classification':'EXACT_CONDITIONAL_REVIEW_RECONCILIATION_AND_ALGEBRAIC_OUTPUT_CORRECTION','check_count':len(checks),'checks':checks,'fixtures':fixtures,'provided_review_provenance':'User-supplied text; reviewer identity and nonconstructor independence not established','independent_review':False,'physical_promotion':0},indent=2,default=str))
