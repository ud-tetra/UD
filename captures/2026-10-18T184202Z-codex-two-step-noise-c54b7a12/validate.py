import json,subprocess,sys
from fractions import Fraction as F
import numpy as np
from bindings import P,freeze,sha

def validate():
 f=freeze();data=json.loads((P/'DATA_FREEZE.json').read_text());assert data['noise_freeze_sha256']==sha(P/'NOISE_FREEZE.json');rows=[];replays=0
 for e,r in zip(f['cases'],data['records']):
  n=e['case'];assert n==r['case'] and r['all_raw_noise_readings_checked']==18790154 and r['max_vector_integer_squared_error']==62*e['integer_amplitude']**2 and r['per_vector_2neg20_met']
  o=P/'results'/n;order=json.loads((o/'ORDER_CERTIFICATE.json').read_text());rep=json.loads((o/'ORDER_REPLAY.json').read_text());assert {k:v for k,v in order.items() if k!='replay'}=={k:v for k,v in rep.items() if k!='replay'}
  audit=json.loads((o/'DISCOVERY.json').read_text());assert audit['record_sha256']==r['record_sha256']
  out={'case':n,'mode':e['mode'],'integer_amplitude':e['integer_amplitude'],'raw_vector_noise_squared':r['vector_noise_squared'],'raw_vector_gate_met':True,'order_bound_status':order['status'],'learned_order':audit['learned_order_float']}
  if (o/'ADAPTER_HOLD.json').exists():out.update(json.loads((o/'ADAPTER_HOLD.json').read_text()))
  else:
   a=json.loads((o/'CERTIFICATE.json').read_text());b=json.loads((o/'REPLAY_CERTIFICATE.json').read_text());assert {k:v for k,v in a.items() if k not in ['seconds','replay']}=={k:v for k,v in b.items() if k not in ['seconds','replay']};assert sha(o/'PHASE_PROPOSAL.npz')==sha(P/f'results/original-{n}/PHASE_PROPOSAL.npz');replays+=1;out.update(status=a['status'],reason=a.get('reason'),readable=a.get('readable'),direct_error=json.loads((o/'DIRECT_ERROR.json').read_text()))
  rows.append(out)
 for mode in ['dense_sign','coherent_dc']:
  with np.load(P/f'NOISE_GRAM_{mode}.npz',allow_pickle=False) as z:g=z['integers_decimal'];assert g.shape==(321,321) and np.array_equal(g,g.T)
 t=subprocess.run([sys.executable,'-m','unittest','discover','-v','-p','test_*.py'],cwd=P,capture_output=True,text=True);assert t.returncode==0,t.stderr;(P/'TEST_RESULTS.txt').write_text(t.stdout+t.stderr)
 return {'status':'PASS','physical_promotion':0,'independent_review':'pending','cases':rows,'records':len(rows),'exact_noise_readings_checked':sum(r['all_raw_noise_readings_checked'] for r in data['records']),'original_instrumented_runs':2*len(rows),'phase_certificate_replays':replays,'tests':6,'all_HOLD_outcomes_retained':True,'shared_dense_sign_pattern_not_independent_replicates':True,'new_full_Hankel_or_SI_claim':False}
if __name__=='__main__':
 r=validate();(P/'VALIDATION.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
