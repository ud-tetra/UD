"""Numerical operator-search proposal; independent residual certification follows."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np
from scipy.linalg import solve,qr
from scipy.optimize import least_squares
from pathlib import Path
import json,time
import native_model as m
edges=np.array(m.B[1],dtype=float)
qedge,_,_=qr(edges,mode='economic',pivoting=True)
U=np.zeros((23,14));U[5:14,:5]=qedge[:,:5];U[14:,5:]=np.eye(9)
p=np.zeros(23);p[14:21]=np.array(m.B[2],dtype=float)[:,1]/2
q=np.zeros(23);q[22]=1
P=np.outer(p,p)+np.outer(q,q)
J=np.outer(p,q)-np.outer(q,p)
I=np.eye(14)
all_results=[]
for which,u in enumerate([.5,-.5]):
 target23=np.eye(23)+((1-u*u)/(1+u*u)-1)*P+(2*u/(1+u*u))*J
 target=U.T@target23@U
 for attempt in range(3):
  seed=534224+which*100+attempt
  rng=np.random.default_rng(seed);count=160
  masks=rng.integers(0,2,(count,7)).tolist()
  mats=[U.T@np.array(m.native(h),dtype=float)@U for h in masks]
  class Eval:
   def __init__(self):self.last=None
   def calc(self,t):
    if self.last is not None and np.array_equal(t,self.last):return
    forward=[I];cs=[];ds=[]
    for a,dt in zip(mats,t):
     inv=solve(I-dt*a/2,I,check_finite=False)
     c=2*inv-I;cs.append(c);ds.append(inv@a@inv)
     forward.append(c@forward[-1])
    jac=np.zeros((196,count));post=I
    for k in range(count-1,-1,-1):
     jac[:,k]=(post@ds[k]@forward[k]).ravel()
     post=post@cs[k]
    self.last=t.copy();self.res=(forward[-1]-target).ravel();self.J=jac
   def fun(self,t):self.calc(t);return self.res
   def jac(self,t):self.calc(t);return self.J
  ev=Eval();start=time.time()
  sol=least_squares(ev.fun,rng.uniform(.1,1.5,count),jac=ev.jac,bounds=(.0001,4),
       max_nfev=1200,ftol=1e-13,xtol=1e-13,gtol=1e-13)
  error=float(np.linalg.norm(sol.fun))
  print('u',u,'attempt',attempt,'error',error,'evaluations',sol.nfev,'seconds',time.time()-start,flush=True)
  if error<1e-9:
   all_results.append({'u':str(m.Q(1,2) if u>0 else m.Q(-1,2)),'seed':seed,
    'masks':masks,'parameter_denominator':10**12,
    'parameter_numerators':[int(round(v*10**12)) for v in sol.x],
    'numerical_frobenius_error':error,'evaluations':sol.nfev})
   Path('WRITER_SCHEDULES.json').write_text(json.dumps({'programs':all_results},indent=2)+'\n')
   break
 else:raise RuntimeError('operator search did not converge')
