import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np
from scipy.linalg import solve
from scipy.optimize import least_squares
import native_model as src
import json,time
from pathlib import Path
I=np.eye(23)
x=np.zeros(23)
for edge,val in [((0,1),-1),((0,2),1),((1,2),-1)]:x[5+src.SIMP[1].index(edge)]=val
c=24/37;feed=14+src.SIMP[2].index((0,1,4));out=14+src.SIMP[2].index((0,2,4))
y=x*3/37
for f,v in [((0,1,2),-48),((0,1,3),-20),((0,2,3),20),((1,2,3),-20)]:y[14+src.SIMP[2].index(f)]=v/37
y[21]=c;z=y.copy();z[21]=0
p0=x.copy();p0[feed]=c;p1=y.copy();p1[feed]=c
p2=z.copy();p2[feed]=c;p2[out]=c;p3=x.copy();p3[out]=c
park=p0.copy();park[feed]=0;park[22]=c
states=[p3,park]
result=[]
for stage in range(1):
 for attempt in range(4):
  rng=np.random.default_rng(534521+stage*100+attempt)
  count=64
  masks=rng.integers(0,2,(count,7)).tolist()
  mats=[np.array(src.native(h),dtype=float) for h in masks]
  class Eval:
   def __init__(self):self.last=None
   def calc(self,t):
    if self.last is not None and np.array_equal(t,self.last):return
    cur=states[stage].copy();Cs=[];ds=[]
    for a,dt in zip(mats,t):
     inv=solve(I-dt*a/2,I,check_finite=False);C=2*inv-I
     nxt=C@cur;ds.append(inv@a@((cur+nxt)/2));Cs.append(C);cur=nxt
    J=np.zeros((23,count));post=I.copy()
    for k in range(count-1,-1,-1):J[:,k]=post@ds[k];post=post@Cs[k]
    self.last=t.copy();self.r=cur-states[stage+1];self.J=J
   def fun(self,t):self.calc(t);return self.r
   def jac(self,t):self.calc(t);return self.J
  ev=Eval();start=time.time()
  opt=least_squares(ev.fun,rng.uniform(.1,1.5,count),jac=ev.jac,bounds=(.0001,4),max_nfev=1000,ftol=1e-13,xtol=1e-13,gtol=1e-13)
  err=np.linalg.norm(opt.fun)
  print('stage',stage,'attempt',attempt,'error',err,'nfev',opt.nfev,'seconds',time.time()-start,flush=True)
  if err<1e-9:
   result.append({'masks':masks,'steps_numerator':[int(round(t*10**12)) for t in opt.x],'step_denominator':10**12,'search_error':err,'nfev':opt.nfev,'seed':534521+stage*100+attempt})
   Path('parking_search.json').write_text(json.dumps({'stages':result},indent=2)+'\n');break
 else:raise RuntimeError('no solution')
