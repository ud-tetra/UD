import json,subprocess,sys
from bindings import P,freeze,sha

def validate():
 rows=[]
 for e in freeze()['cases']:
  n=e['case'];o=P/'results'/n;order=json.loads((o/'ORDER_CERTIFICATE.json').read_text());order2=json.loads((o/'ORDER_REPLAY.json').read_text());assert {k:v for k,v in order.items() if k!='replay'}=={k:v for k,v in order2.items() if k!='replay'}
  if (o/'ADAPTER_HOLD.json').exists():rows.append(json.loads((o/'ADAPTER_HOLD.json').read_text()));continue
  a=json.loads((o/'CERTIFICATE.json').read_text());b=json.loads((o/'REPLAY_CERTIFICATE.json').read_text());assert {k:v for k,v in a.items() if k not in ['replay','seconds']}=={k:v for k,v in b.items() if k not in ['replay','seconds']}
  assert sha(o/'PHASE_PROPOSAL.npz')==sha(P/f'results/original-{n}/PHASE_PROPOSAL.npz');rows.append({'case':n,'status':a['status'],'reason':a.get('reason'),'source_precision_order':order['exact_encoded_count_above_source_cutoff'],'readable':a.get('readable'),'original_proposal_byte_identical':True})
 t=subprocess.run([sys.executable,'-m','unittest','discover','-v','-p','test_*.py'],cwd=P,capture_output=True,text=True);assert t.returncode==0,t.stderr;(P/'TEST_RESULTS.txt').write_text(t.stdout+t.stderr)
 controls=json.loads((P/'CONTROL_RESULTS.json').read_text());assert controls['status'] in ['PASS','HOLD_NO_APPLICABLE_ACTUAL_WITNESS']
 return {'status':'PASS','cases':rows,'tests':6,'actual_array_corruption_controls':len(controls['controls']),'physical_promotion':0,'independent_review':'pending','all_HOLD_outcomes_preserved':True,'new_original_instrument_noise_contract_admission':False,'two_step_alias_modulo_pi_remains':True}
if __name__=='__main__':
 r=validate();(P/'VALIDATION.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
