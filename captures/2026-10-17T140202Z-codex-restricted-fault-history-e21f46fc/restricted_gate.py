"""Exact local decoder/gates for one blank-corrected diagnostic epoch.

Input Y has shape6x260x189, with times0,h,...,5h. Entries must be rational
strings, integers or exact Fraction values. No binary64 tolerances are used.
Blank correction and total-error receipts are external requirements.
"""
from fractions import Fraction as F
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
def number(x):
 if isinstance(x,F):return x
 if type(x) is int or isinstance(x,str):return F(x)
 if isinstance(x,list) and len(x)==2 and all(type(v) is int for v in x):return F(*x)
 raise ValueError('Use exact rational data; floats are not accepted')
def pair(x):return [x.numerator,x.denominator]
def assess_epoch(Y):
 d=json.loads((ROOT/'sources/PROBE_DESIGN.json').read_text())
 c=json.loads((ROOT/'RESTRICTED_FAULT_CERTIFICATE.json').read_text())
 m=d['color_count'];obs=d['observed_coordinates'];color=d['colors'];q=d['preparation_denominators']
 if len(Y)!=6 or any(len(snap)!=m for snap in Y) or any(len(v)!=len(obs) for snap in Y for v in snap):
  raise ValueError('Expected6x260x189 blank-corrected readings')
 row_index={r:i for i,r in enumerate(obs)}
 static_sq=F(0);used=set()
 for rs,stencil in d['readout_stencils'].items():
  r=int(rs);ri=row_index[r]
  for j in stencil:
   cc=color[j];used.add((cc,ri))
   decoded=q[cc]*number(Y[0][cc][ri])-int(r==j)
   static_sq+=decoded*decoded
 unused_sq=sum(number(Y[0][cc][ri])**2 for cc in range(m) for ri in range(189) if (cc,ri) not in used)
 weights=[number(c['dynamic_gate']['zero_time_weight'])]+[number(v) for v in c['dynamic_gate']['positive_time_weights']]
 h=number(c['dynamic_gate']['step'])
 import numpy as np
 z=np.load(ROOT/'sources/operators.npz')
 native={r:set(map(int,z['A_indices'][z['A_indptr'][r]:z['A_indptr'][r+1]])) for r in obs}
 row_squares={}
 for rs,stencil in d['generator_row_stencils'].items():
  r=int(rs);ri=row_index[r];value=F(0)
  for j in stencil:
   if j in native[r]:continue
   cc=color[j]
   decoded=q[cc]*sum(w*number(Y[k][cc][ri]) for k,w in enumerate(weights))/h
   value+=decoded*decoded
  row_squares[r]=value
 TC=number(c['static_gate']['decoded_residual_threshold'])
 TD=number(c['dynamic_gate']['forbidden_row_residual_acceptance_ceiling'])
 TU=number(c['static_gate']['unused_static_data_Frobenius_gate'])
 bad_rows=[r for r,v in row_squares.items() if v>=TD*TD]
 passed=static_sq<TC*TC and unused_sq<TU*TU and not bad_rows
 return {'decision':'CONSISTENT_WITH_RESTRICTED_OPERATOR_BOUNDS' if passed else 'REJECT_JOINT_CONTRACT',
  'physical_promotion':0,'requires_external_error_and_family_receipts':True,
  'empirical_pass_claimed':False,'static_residual_squared':pair(static_sq),
  'unused_static_residual_squared':pair(unused_sq),
  'forbidden_row_residual_squared':{str(r):pair(v) for r,v in row_squares.items()},
  'rejected_rows':bad_rows,'cause_identified':False}
