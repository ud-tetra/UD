import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import argparse,json
import numpy as np
from flint import ctx
from bindings import P,load_case
from frame_values import values
from frame_math import span_residual,assemble_span
from numeric_math import encode,diffnorm
from proof_math import fm,up
ctx.prec=512
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');args=p.parse_args();_,_,o,_=load_case('coherent_dc')
 base=json.loads((o/'SPAN_CERTIFICATE.json').read_text());c=json.loads((P/'inputs/PHASE_STABILITY_CERTIFICATE.json').read_text())['constants']
 with np.load(o/'FLOAT_WITNESS.npz',allow_pickle=False) as z:U=z['basis'];T=z['shift']
 with np.load(o/'FRAME_REDUCTION.npz',allow_pickle=False) as z:D=z['reduction']
 with np.load(P/'inputs/REFERENCE_PROPOSAL.npz',allow_pickle=False) as z:pp=values(z['theta'])
 badD=D.copy();badD[0,0]+=1.;r,receipt=span_residual(pp,U,badD)
 badT=T.copy();badT[0,0]+=1./64.;un,bu=encode(U);tn,bt=encode(badT);tr,tr2=diffnorm(fm(un[1:]),bu,fm(un[:-1])*fm(tn),bu+bt)
 rows=[]
 for name,key,bound,proof in [('frame_reduction_plus_one','frame_span_residual_upper',up(r),receipt),('shift_entry_plus_1_over_64','shift_residual_upper',up(tr),{'exact_squared_shift_residual':tr2})]:
  m=base['metrics'].copy();m[key]=bound
  try:result=assemble_span(m,c)
  except AssertionError as exc:result={'status':'HOLD','reason':str(exc)}
  assert result['status']=='HOLD','Frozen corruption control unexpectedly certified'
  rows.append({'control':name,'altered_metric':key,'validated_upper':bound,'receipt':proof,'result':result})
 dest=P/('REPLAY_REFUSAL_RESULTS.json' if args.replay else 'REFUSAL_RESULTS.json');assert not dest.exists();dest.write_text(json.dumps({'status':'PASS','physical_promotion':0,'controls':rows},indent=2));print('Both frozen actual-array corruption controls HOLD')
