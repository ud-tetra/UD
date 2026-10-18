"""Independent Arb direct-sum spot audit of the frozen encoded timing sources."""
import json
from fractions import Fraction as F
import numpy as np
from flint import ctx,arb,acb,fmpq
from bindings import P,check_freeze,sha,checked
from make_records import timing,SHAPE
ctx.prec=512
f=check_freeze();d=json.loads((P/'DATA_FREEZE.json').read_text());assert d['campaign_sha256']==sha(P/'CAMPAIGN_FREEZE.json')
with np.load(P/'inputs/REFERENCE_PROPOSAL.npz',allow_pickle=False) as z:theta=z['theta'];B=z['coeff']
rows=[]
for e,r in zip(f['cases'],d['records']):
 path=P/f"records/{e['case']}.i64le";checked(path,r['record_sha256']);Y=np.memmap(path,dtype='<i8',mode='r',shape=SHAPE);n=0;bound=arb(fmpq(*r['evaluation_bounds']['scalar_waveform_error_upper']))
 for a in range(37):
  cols=np.arange(a,2294,37)
  for k in f['audit_time_indices']:
   o,eps,u=timing(e,a,k);t=o+(1+eps)*k+u;v=[arb(1)]
   for th in theta:
    z=acb(0,arb(int(th))*arb(fmpq(t.numerator,t.denominator))/(1<<60)).exp();v.extend([z.real,z.imag])
   for c,col in enumerate(cols):
    truth=sum(v[j]*int(B[j,col]) for j in range(105))/(1<<60);encoded=arb(int(Y[a,k,c]))/(1<<48);assert abs(truth-encoded)<bound;n+=1
 checked(path,r['record_sha256']);rows.append({'case':e['case'],'record_sha256':r['record_sha256'],'direct_Arb_waveform_readings_checked':n,'all_direct_spot_checks_within_proved_uniform_bound':True})
(P/'DIRECT_SOURCE_AUDIT.json').write_text(json.dumps({'status':'PASS','physical_promotion':0,'all_encoded_readings_vs_range_and_hash_checked':sum(r['encoded_readings_checked'] for r in d['records']),'direct_spot_checks_only':True,'records':rows},indent=2));print(json.dumps(rows,indent=2))
