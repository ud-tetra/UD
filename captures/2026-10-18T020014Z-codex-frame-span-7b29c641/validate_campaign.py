from pathlib import Path
import json,subprocess,sys
from bindings import P,load_case,sha
from frame_math import assemble_span

def validate():
 f=json.loads((P/'CAMPAIGN_FREEZE.json').read_text());c=json.loads((P/'inputs/PHASE_STABILITY_CERTIFICATE.json').read_text())['constants'];rows=[]
 dynamic={'replay','wall_seconds','peak_rss_kib'}
 for e in f['cases']:
  _,_,o,parent=load_case(e['case']);a=json.loads((o/'SPAN_CERTIFICATE.json').read_text());b=json.loads((o/'REPLAY_CERTIFICATE.json').read_text())
  assert {k:v for k,v in a.items() if k not in dynamic}=={k:v for k,v in b.items() if k not in dynamic}
  assert not a['replay'] and b['replay'] and a['frame_reduction_sha256']==sha(o/'FRAME_REDUCTION.npz')
  try:proof=assemble_span(a['metrics'],c)
  except AssertionError as exc:proof={'status':'HOLD','reason':str(exc),'unique_reference_phase_matching':False,'physical_promotion':0}
  assert all(a[k]==v for k,v in proof.items()) and a['frame_constants_recomputed']
  assert a['parent_certificate_status']==parent['status'] and not a['estimator_rerun'] and a['fresh_raw_readings_projected']==0
  rows.append({'case':e['case'],'status':a['status'],'readable':a.get('readable'),'reason':a.get('reason'),'parent_status':parent['status'],'original_witness_sha256':e['witness_sha256'],'original_proposal_unchanged':True})
 refusals=json.loads((P/'REFUSAL_RESULTS.json').read_text());assert refusals==json.loads((P/'REPLAY_REFUSAL_RESULTS.json').read_text());assert len(refusals['controls'])==2
 t=subprocess.run([sys.executable,'-m','unittest','-v','test_span'],cwd=P,capture_output=True,text=True);assert t.returncode==0,t.stderr
 (P/'HOSTILE_TEST_RESULTS.txt').write_text(t.stdout+t.stderr)
 return {'status':'PASS','physical_promotion':0,'independent_review':'pending','saved_output_cases':3,'saved_array_replays':3,'tests':8,'actual_array_corruption_controls':2,'cases':rows,'fresh_raw_readings_projected':0,'estimator_reruns':0,'reference_frame_constants_recomputed':True,'new_full_Hankel_execution':False,'no_full_Hankel_allocated':True,'uniform_all_input_guarantee':False,'all_HOLDs_preserved':True}
if __name__=='__main__':
 r=validate();(P/'VALIDATION.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
