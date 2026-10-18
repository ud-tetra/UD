import json
from fractions import Fraction as F
import numpy as np
from flint import arb,acb,fmpq
from proof_math import fm,arr,dyad
from bindings import P

def source():
 with np.load(P/'inputs/REFERENCE_PROPOSAL.npz',allow_pickle=False) as z:theta=z['theta'];B=z['coeff']
 assert theta.shape==(52,) and B.shape==(105,2294)
 W=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64);v=np.pad(np.array(json.loads((P/'inputs/NULL_VECTOR.json').read_text())['vector'],np.int64),(0,1974));A=np.column_stack((2*W,v));assert int(v@v)==16228 and np.all(v@W==0)
 assert sum(int(x)**2 for x in A.flat)==1484388
 return theta,B,A

def rotate(theta,B,offsets):
 assert len(offsets)==37;co=np.empty((52,37),np.int64);si=np.empty((52,37),np.int64);gate=arb(1)/(1<<60)
 for j,t in enumerate(theta):
  for a,o in enumerate(offsets):
   o=F(*o);angle=arb(int(t))*arb(fmpq(o.numerator,o.denominator))/(1<<60);z=acb(0,angle).exp();c,s=dyad(z.real),dyad(z.imag)
   assert abs(z.real-arb(c)/(1<<60))<gate and abs(z.imag-arb(s)/(1<<60))<gate
   co[j,a]=c;si[j,a]=s
 out=np.empty(B.shape,dtype=object);out[0]=B[0].astype(object)*(1<<60)
 for j in range(52):
  for a in range(37):
   cols=np.arange(a,2294,37);x=B[2*j+1,cols].astype(object);y=B[2*j+2,cols].astype(object);c=int(co[j,a]);s=int(si[j,a]);out[2*j+1,cols]=c*x+s*y;out[2*j+2,cols]=-s*x+c*y
 return out,co,si

def coefficients(B,A):return arr(fm(B)*fm(A))
