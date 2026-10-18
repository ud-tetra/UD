from fractions import Fraction as F
import numpy as np
from flint import arb,acb,fmpq,ctx
from bindings import P
from proof_math import nearest,dyad,up,down
ctx.prec=512
BITS=96;Q=1<<BITS;SHAPE=(37,8191,62)
def rounded(n,bits):return nearest(int(n),bits)
def mul(z,w):return (rounded(z[0]*w[0]-z[1]*w[1],BITS),rounded(z[0]*w[1]+z[1]*w[0],BITS))
def phase(theta,t):
 t=F(t);angle=arb(int(theta))*arb(fmpq(t.numerator,t.denominator))/(1<<60);z=acb(0,angle).exp();r=[]
 for v in [z.real,z.imag]:
  # Unique nearest integer, including all interval uncertainty.
  n=(v*Q).mid().unique_fmpz()
  if n is None:n=int((v*Q).mid().floor().unique_fmpz())
  else:n=int(n)
  # Either n or its nearest adjacent integer; this is only proposal selection.
  opts=[n-1,n,n+1];valid=[x for x in opts if abs(v-arb(x)/Q)<=arb(1)/Q]
  assert valid,'HOLD: anchor rounding error not enclosed'
  r.append(min(valid,key=lambda x:float(abs(v-arb(x)/Q).mid())))
 return tuple(r)

def model_frame(e):
 with np.load(P/'inputs/REFERENCE_PROPOSAL.npz',allow_pickle=False) as z:theta=z['theta']
 mu=F(*e['rate']);jit=F(*e['jitter']);classes=e['classes'];q=1+104*len(classes);pp=np.empty((8191,q),np.int64);pp[:,0]=1<<60;J=np.zeros((q,q),np.int64);J[0,0]=1<<60
 targets=[{'label':'stationary','omega':[0,1]}];points=[acb(1)];col=1
 for s in classes:
  for j,t in enumerate(theta):
   step=phase(t,1+s*mu);cur=(Q,0);jp=phase(t,s*jit);jm=phase(t,-s*jit)
   for k in range(8191):
    z=mul(cur,jp if k%2==0 else jm);pp[k,col]=rounded(z[0],36);pp[k,col+1]=rounded(z[1],36);cur=mul(cur,step)
   omega=F(int(t),1<<60)*(1+s*mu);rot=acb(0,arb(fmpq(2*omega.numerator,omega.denominator))).exp();c,si=dyad(rot.real),dyad(rot.imag);assert abs(rot.real-arb(c)/(1<<60))<arb(1)/(1<<60) and abs(rot.imag-arb(si)/(1<<60))<arb(1)/(1<<60)
   J[col:col+2,col:col+2]=[[c,si],[-si,c]]
   for sign in [1,-1]:
    w=sign*omega;pt=rot if sign==1 else rot.conjugate();principal=pt.arg();lift=((2*arb(fmpq(w.numerator,w.denominator))-principal)/(2*arb.pi())).unique_fmpz();assert lift is not None
    targets.append({'label':f'j{j}:rate{s}:sign{sign}','omega':[w.numerator,w.denominator],'source_lift_integer':int(lift)});points.append(pt)
   col+=2
 assert col==q
 sepnum=2*(1<<100)
 for i in range(q):
  for j in range(i):sepnum=min(sepnum,down(abs(points[i]-points[j]))[0])
 sep=arb(sepnum)/(1<<100)
 assert sep>0
 return pp,J,targets,points,sep
