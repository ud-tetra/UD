"""Exact matched-filter decoder for either saved optimized profile.

Y: blank-corrected[time][code][output]. Receipts/family/stability are external.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import json
ROOT=Path(__file__).resolve().parent
def parse(x):
 if isinstance(x,F):return x
 if type(x) is int or isinstance(x,str):return F(x)
 if isinstance(x,list) and len(x)==2 and all(type(y) is int for y in x):return F(*x)
 raise ValueError('Exact rational inputs required; floats are rejected')
def pair(x):return [x.numerator,x.denominator]
def spec(profile='recommended'):
 cert=json.loads((ROOT/'TRADEOFF_CERTIFICATE.json').read_text())
 if profile=='recommended':
  r=cert['recommended'];m=r['order_half'];h=parse(r['certified_power_of_two_step']);eps=parse(r['total_response_error_ceiling'])
 elif profile=='strict':
  r=cert['strict_target_variant'];m=r['order_half'];h=parse(r['step']);eps=parse(r['response_error_ceiling'])
 else:raise ValueError('Unknown profile')
 w=[2*F((-1)**(k+1),k)*F(factorial(m)**2,factorial(m-k)*factorial(m+k)) for k in range(1,m+1)]
 B=F(8,7)*F(factorial(m)**2,factorial(2*m+1))*5**(2*m+1)*h**(2*m)
 FF=F(8,7)*5*sum(abs(c)*k for k,c in enumerate(w,1))
 NN=(abs(sum(w))+sum(abs(c) for c in w))/h
 return m,h,eps,[-sum(w)]+w,B,FF,NN
def assess_epoch(Y,profile='recommended'):
 m,h,eps,w,B,FF,NN=spec(profile)
 d=json.loads((ROOT/'sources/PROBE_DESIGN.json').read_text())
 filters=json.loads((ROOT/'MATCHED_FILTER_DESIGN.json').read_text())
 colors=d['colors'];qs=d['preparation_denominators'];obs=d['observed_coordinates']
 if len(Y)!=m+1 or any(len(x)!=260 for x in Y) or any(len(v)!=189 for x in Y for v in x):
  raise ValueError('Shape mismatch for selected profile')
 row_index={r:i for i,r in enumerate(obs)};used=set();static=F(0);row_stat={}
 for rs,cols in d['readout_stencils'].items():
  r=int(rs);ri=row_index[r];ss=F(0)
  for j in cols:
   cc=colors[j];used.add((cc,ri))
   v=qs[cc]*parse(Y[0][cc][ri])-int(j==r);ss+=v*v
  static+=ss;row_stat[r]=ss
 unused=sum(parse(Y[0][cc][ri])**2 for cc in range(260) for ri in range(189) if (cc,ri) not in used)
 row_bad=[r for r,sq in row_stat.items() if sq>=(parse(filters['row_gate_factors'][str(r)])*eps)**2]
 decoded={};scores=[];rejected=[]
 for rec in filters['records']:
  r=rec['row'];ri=row_index[r];total=F(0)
  for j,sign in zip(rec['exclusive_columns'],rec['exclusive_signs']):
   key=(r,j)
   if key not in decoded:
    cc=colors[j];decoded[key]=qs[cc]*sum(c*parse(Y[k][cc][ri]) for k,c in enumerate(w))/h
   total+=sign*decoded[key]
  score=total/len(rec['exclusive_columns'])
  gate=parse(rec['mean_decode_denominator'])*(B+(parse(rec['readout_row_error_factor'])*FF+NN)*eps)
  scores.append({'row':r,'partner':rec['partner'],'score':pair(score),'gate':pair(gate)})
  if abs(score)>=gate:rejected.append([r,rec['partner']])
 accepted=static<(46*eps)**2 and unused<(17*eps)**2 and not row_bad and not rejected
 return {'decision':'CONSISTENT_WITH_RESTRICTED_BOUNDS' if accepted else 'REJECT_JOINT_CONTRACT',
  'profile':profile,'physical_promotion':0,'empirical_pass_claimed':False,
  'requires_external_family_and_error_receipts':True,'static_squared':pair(static),
  'unused_squared':pair(unused),'static_rows_rejected':row_bad,
  'filters_rejected':rejected,'scores':scores,'cause_identified':False}
