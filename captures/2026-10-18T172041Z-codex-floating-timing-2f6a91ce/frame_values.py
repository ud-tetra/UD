"""Validated dyadic values of a fixed real temporal frame."""
import numpy as np
from flint import acb,arb
from proof_math import dyad

def values(theta,n=8191):
 assert theta.shape==(52,) and np.all(theta>0) and np.all(np.diff(theta)>0)
 pp=np.zeros((n,105),np.int64);pp[:,0]=1<<60;gate=arb(1)/(1<<60)
 for j,t in enumerate(theta):
  assert arb(int(t))/(1<<60)<arb.pi()
  for k in range(n):
   z=acb(0,arb(int(t))*k/(1<<60)).exp();r,i=dyad(z.real),dyad(z.imag)
   assert abs(z.real-arb(r)/(1<<60))<gate and abs(z.imag-arb(i)/(1<<60))<gate
   pp[k,2*j+1]=r;pp[k,2*j+2]=i
 return pp

def constants(theta,n=8191):
 from proof_math import up,down
 freq=[arb(0)]+[sign*arb(int(t))/(1<<60) for t in theta for sign in [1,-1]]
 rows=[];seps=[]
 for i,u in enumerate(freq):
  row=arb(0)
  for j,w in enumerate(freq):
   if i==j:continue
   d=w-u;den=acb(0,d).exp()-1;assert abs(den)>0
   row+=abs((acb(0,n*d).exp()-1)/(n*den))
   if j>i:seps.append(down(abs(den)))
  rows.append(up(row))
 maximum=max(x[0] for x in rows);den=1<<100;minimum=min(x[0] for x in seps)
 return {'time_rows':n,'temporal_order':len(freq),'frame_Gram_lower':[den-maximum,den],'frame_Gram_upper':[den+maximum,den],'minimum_chord_separation_lower':[minimum,den]}
