#!/usr/bin/env python3
"""Independent uniform dyadic error gates, avoiding maxima of overlapping balls."""
import json,gzip,time
from pathlib import Path
import numpy as np
from flint import arb,acb,arb_mat,ctx,fmpq
ctx.prec=512
P=Path(__file__).resolve().parent;O=P/'output';t=time.monotonic();r=json.loads((P/'sources/REFINED_ROOT_INTERVALS.json').read_text());co=json.loads((P/'sources/ANNIHILATOR_COEFFICIENTS.json').read_text())['qL_coefficients_descending'];f=np.load(O/'MODAL_FACTORS.npz');phase=np.load(O/'PHASES.npy');coeff=f['coeff']
with gzip.open(P/'sources/CROSS_MOMENTS.json.gz','rt') as z:m=json.load(z)
Gs=[arb_mat(g) for g in m['G']];Js=[arb_mat(g) for g in m['J']];dc=[(53-i)*co[i] for i in range(53)];gate=arb(1)/(1<<60);temporal_gate=arb(1)/(1<<51);freq=[arb(0)]
def iv(rr):
 a,b=arb(fmpq(*rr['a'])),arb(fmpq(*rr['b']));return (a+b)/2+arb(0,((b-a)/2).upper())
def dyad(v,b=52):
 z=v.mid()*(1<<b);n=z.unique_fmpz();return int(n) if n is not None else int((z+arb('.5')).floor().unique_fmpz())
for j,rr in enumerate(r):
 mu=iv(rr);cc=[arb(1)]
 for c in co[1:-1]:cc.append(arb(c)+mu*cc[-1])
 d=arb(0)
 for c in dc:d=d*mu+c
 gg=arb_mat(62,37);jj=arb_mat(62,37)
 for k in range(53):gg+=Gs[52-k]*cc[k];jj+=Js[52-k]*cc[k]
 gg/=d*52
 channels=[(0,gg)] if j==0 else [(2*j-1,gg),(2*j,jj/(d*52*mu.sqrt()))]
 for row,matrix in channels:
  for c in range(62):
   for a in range(37):assert abs(matrix[c,a]-arb(int(coeff[row,c*37+a]))/(1<<60))<gate
 if j:
  w=mu.sqrt();freq.extend([w,-w]);step=acb(0,w/2).exp();z=acb(1)
  for k in range(8191):
   z=acb(0,w*k/2).exp()
   assert abs(z.real-arb(int(phase[k,2*j-1]))/(1<<60))<gate, (j,k,str(z.real),int(phase[k,2*j-1]),str(gate))
   assert abs(z.imag-arb(int(phase[k,2*j]))/(1<<60))<gate
assert np.all(phase[:,0]==1<<60) and np.all(np.abs(coeff)<=1<<60)
for i in range(105):
 for j in range(i+1,105):
  d=(freq[j]-freq[i])/2;z=(acb(0,4096*d).exp()-1)/(acb(0,d).exp()-1)/4096
  assert abs(z.real-arb(dyad(z.real))/(1<<52))+abs(z.imag-arb(dyad(z.imag))/(1<<52))<temporal_gate
trL=0;trR=0
for j in range(53):
 mult=1 if j==0 else 2
 trL+=mult*sum(int(v)**2 for k in [0,1] for v in f[f'{j}_{k}'].flat)
 trR+=mult*sum(int(v)**2 for k in [2,3] for v in f[f'{j}_{k}'].flat)
# For the full cross-factor Gram, Frobenius norm <= trace; all arithmetic exact.
el=2*(temporal_gate*arb(trL)/(1<<120)+arb(1893)/(1<<52));er=temporal_gate*arb(trR)/(1<<120)+arb(1893)/(1<<52)
scalar=210*gate+arb(1)/(1<<49);de=arb(37*62).sqrt()*scalar
result={'status':'PASS','coefficient_entries_checked':105*62*37,'phase_components_checked':52*8191*2,'temporal_pairs_checked':5460,'uniform_coefficient_error':[1,1<<60],'uniform_phase_error':[1,1<<60],'uniform_temporal_complex_error':[1,1<<51],'left_gram_error_upper':str(el.upper()),'right_gram_error_upper':str(er.upper()),'scalar_error_upper':str(scalar.upper()),'trajectory_hankel_error_upper':str(de.upper()),'seconds':time.monotonic()-t}
(O/'UNIFORM_BOUNDS.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
