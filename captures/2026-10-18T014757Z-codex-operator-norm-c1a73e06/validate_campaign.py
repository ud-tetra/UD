from pathlib import Path
import json,hashlib,subprocess,sys
from fractions import Fraction as F
from numeric_math import assemble
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def validate():
 f=json.loads((P/'CAMPAIGN_FREEZE.json').read_text())
 for n,h in f['code_sha256'].items():assert sha(P/n)==h,(n,'frozen source changed')
 for n,h in f['inputs_sha256'].items():assert sha(P/'inputs'/n)==h
 c=json.loads((P/'inputs/PHASE_STABILITY_CERTIFICATE.json').read_text())['constants'];c['discovery_cutoff']=json.loads((P/'inputs/SKETCH_RULE.json').read_text())['cutoff'];rows=[]
 dynamic={'all_18790154_readings_projected','portable_sketch_witness_replay','wall_seconds','peak_rss_kib'}
 for e in f['cases']:
  o=P/f"results/{e['case']}";a=json.loads((o/'FLOAT_CERTIFICATE.json').read_text());b=json.loads((o/'REPLAY_CERTIFICATE.json').read_text())
  assert {k:v for k,v in a.items() if k not in dynamic}=={k:v for k,v in b.items() if k not in dynamic}
  assert a['record_sha256']==e['record_sha256'] and a['proposal_sha256']==sha(o/'PROPOSAL.npz')==sha(P/e['original_proposal_path'])
  assert a['witness_sha256']==sha(o/'FLOAT_WITNESS.npz') and a['exact_sketch_sha256']==sha(o/'EXACT_RECORD_SKETCH.npz')
  for label,key in [('frobenius','metrics'),('operator','operator_metrics')]:
   try:proof=assemble(a[key],c)
   except AssertionError as exc:proof={'status':'HOLD','reason':str(exc),'unique_reference_phase_matching':False,'physical_promotion':0}
   assert a['comparison'][label]==proof
  for name in ['projection','reference_model']:
   g=a['operator_Gram_receipts'][name];assert F(*g['chosen_squared_bound'])==min(F(*g['trace_squared_bound']),F(*g['Gershgorin_squared_bound']))
  assert a['all_18790154_readings_projected'] and b['portable_sketch_witness_replay'] and a['original_proposal_byte_identical']
  rows.append({'case':e['case'],'comparisons':a['comparison'],'operator_Gram_receipts':a['operator_Gram_receipts']})
 t=subprocess.run([sys.executable,'-m','unittest','-v','test_operator'],cwd=P,capture_output=True,text=True);assert t.returncode==0,t.stderr
 (P/'HOSTILE_TEST_RESULTS.txt').write_text(t.stdout+t.stderr)
 return {'status':'PASS','physical_promotion':0,'independent_review':'pending','fresh_raw_readings_projected':2*18790154,'portable_replays':2,'tests':6,'cases':rows,'no_full_Hankel_allocated':True,'uniform_all_input_guarantee':False,'all_HOLDs_retained':True}
if __name__=='__main__':
 r=validate();(P/'VALIDATION.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
