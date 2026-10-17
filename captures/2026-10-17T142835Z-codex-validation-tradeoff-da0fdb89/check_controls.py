"""Finite actual-carrier matched-filter controls; no apparatus observations."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import json
import numpy as np
from scipy.sparse import csr_matrix
from flint import arb,ctx
from optimized_gate import ROOT,spec,pair
ctx.prec=512
def a(x):return arb(x.numerator)/x.denominator
def enc(x):return {'arb_enclosure':str(x),'display_only':float(x.mid())}
d=json.loads((ROOT/'sources/PROBE_DESIGN.json').read_text());design=json.loads((ROOT/'MATCHED_FILTER_DESIGN.json').read_text())
z=np.load(ROOT/'sources/operators.npz');A=csr_matrix((z['A_data'],z['A_indices'],z['A_indptr']),shape=(2640,2640))
rec=next(x for x in design['records'] if x['row']==4 and x['partner']==0)
colors=d['colors'];qs=d['preparation_denominators'];relevant={colors[j] for j in rec['exclusive_columns']}
m,h,eps,w,B,FF,NN=spec();positive=w[1:];qmean=F(*rec['mean_decode_denominator'])
gate=qmean*(B+(F(*rec['readout_row_error_factor'])*FF+NN)*eps)
def control(rho):
 if rho:
  dd=rho.denominator;nn=rho.numerator;den=dd*dd-nn*nn
 else:dd=1;nn=0;den=1
 rows=[]
 for i in range(2640):
  terms=[(i,den)]
  if i==0:terms=[(0,dd*dd),(4,-nn*dd)]
  elif i==4:terms=[(4,dd*dd),(0,-nn*dd)]
  acc={}
  for source,coef in terms:
   for p in range(A.indptr[source],A.indptr[source+1]):
    j=int(A.indices[p]);acc[j]=acc.get(j,0)+coef*int(A.data[p])
  rows.append(acc)
 trans=[[] for _ in range(2640)]
 for i,row in enumerate(rows):
  for j,v in row.items():trans[j].append((i,v))
 x=[int(i==4) for i in range(2640)];N=40;moments=[]
 for n in range(N+1):
  sums={c:0 for c in relevant}
  for i,xx in enumerate(x):
   cc=colors[i]
   if cc in sums:sums[cc]+=xx
  moments.append(sums)
  if n<N:x=[sum(v*x[j] for j,v in row) for row in trans]
 score=F(0);tail=arb(0)
 for k,weight in enumerate(positive,1):
  t=k*h;coeff=F(1);ys={c:F(moments[0][c],qs[c]) for c in relevant}
  for n in range(1,N+1):
   coeff*=t/(den*n)
   for c in relevant:ys[c]+=coeff*moments[n][c]/qs[c]
  spatial=sum(sign*qs[colors[j]]*ys[colors[j]] for j,sign in zip(rec['exclusive_columns'],rec['exclusive_signs']))/len(rec['exclusive_columns'])
  score+=weight*spatial/h
  zz=a(5*t);tail+=a(abs(weight)*qmean/h)*zz.exp()*zz**(N+1)/factorial(N+1)
 true=-rho/(1-rho*rho) if rho else F(0)
 assert abs(a(score-true))+tail<a(qmean*B)
 if rho:
  assert abs(a(score))-tail-a(qmean*NN*eps)>a(gate)
 else:assert abs(a(score))+tail<a(gate)
 return {'rho':pair(rho),'true_score':pair(true),'finite_score':pair(score),
  'additional_Taylor_error':enc(tail),'gate':pair(gate),
  'decision':'REJECT' if rho else 'WITHIN_NULL_GATE','kind':'SYNTHETIC_ACTUAL_CARRIER_CONTROL'}
out={'status':'PASS','physical_promotion':0,'independent_review':'pending',
 'row':4,'partner':0,'decoded_positive_time_samples':m,
 'controls':[control(F(0)),control(F(1,2**42)),control(F(-1,2**42))],
 'apparatus_data':False}
(ROOT/'FINITE_CONTROLS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','finite_controls':3,'exact_Taylor_degree':40}))
