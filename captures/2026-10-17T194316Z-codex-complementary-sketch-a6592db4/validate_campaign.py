"""Source, proof-replay and full-certificate receipt checks; no nominal operator."""
import json,hashlib,subprocess,sys
from pathlib import Path
from fractions import Fraction as F
from replay_sketch import run as replay
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def validate():
 freeze=json.loads((P/'CAMPAIGN_FREEZE.json').read_text())
 for n,h in freeze['code_sha256'].items():assert sha(P/n)==h,(n,'Frozen code changed')
 assert sha(P/'inputs/FROZEN_CONTRACT.json')==freeze['contract_sha256']
 assert sha(P/'inputs/SKETCH_RULE.json')==freeze['rule_sha256']
 assert sha(P/'inputs/NULL_VECTOR.json')==freeze['witness_sha256']
 assert sha(P/'proof_math.py')=='78a5e376e9f9d347f98a780ba514b67ba9d8fa6dc24fa29df4847b87db387072'
 assert sha(P/'certify_record.py')=='1f2f036018cd0de46a26c1db7d0232032f4fc5b5dd862e351eb0dbad8e36334b'
 small=replay();assert sorted(small['exact_small_Gram_replays'].values())==[105,105,105,105,106]
 for case in freeze['cases']:
  n=case['case'];d=P/('results/sketch-clean-v1' if n=='clean' else f'results/sketch-{n}')
  cert=json.loads((d/'SKETCH_CERTIFICATE.json').read_text());audit=json.loads((P/f'results/proposal-{n}/DISCOVERY_AUDIT.json').read_text())
  assert cert['record_sha256']==case['record_sha256']==audit['record_sha256']
  assert audit['temporal_dimension']==cert['above_cutoff_count']
  assert cert['input_identity_stable'] and cert['all_eigenvalues_classified']
  if n=='strong_null_alternating':
   assert audit['temporal_dimension']==106
   assert json.loads((P/f'results/proposal-{n}/HOLD.json').read_text())['status']=='HOLD'
   assert not (P/f'results/proposal-{n}/PROPOSAL.npz').exists()
  else:
   report=json.loads((P/f'results/proposal-{n}/PROPOSAL_REPORT.json').read_text())
   assert report['temporal_dimension']==105 and report['proposal_sha256']==sha(P/f'results/proposal-{n}/PROPOSAL.npz')
 full=P/'results/full-certificate-bounded_null_impulse';cert=json.loads((full/'CERTIFICATE.json').read_text());rule=json.loads((P/'inputs/FROZEN_CONTRACT.json').read_text())['spectral_rule'];T=F(*rule['selection_threshold'])
 assert cert['status']=='CERTIFIED_NUMERIC_RECORD_SIGNATURE'
 assert cert['target_count']==1893 and F(*cert['sigma_r_lower'])>T>F(*cert['sigma_r_plus1_upper'])
 assert F(*cert['condition_upper'])<2029
 assert cert['input_sha256']['proposal']==sha(P/'results/proposal-bounded_null_impulse/PROPOSAL.npz') and cert['input_identity_stable']
 res=json.loads((full/'RECORD_RESIDUAL.json').read_text());assert res['scalar_readings_checked']==18790154 and res['input_sha256']==cert['input_sha256']
 b=json.loads((full/'BENCHMARK.json').read_text());assert not b['dense_hankel_allocated']
 assert b['executed_code_sha256']=={n:sha(P/n) for n in ['certify_record.py','proof_math.py','residual_preflight.py']}
 r=subprocess.run([sys.executable,'-m','unittest','-v','test_complement'],cwd=P,capture_output=True,text=True);assert r.returncode==0,r.stderr
 (P/'HOSTILE_TEST_RESULTS.txt').write_text(r.stdout+r.stderr)
 return {'status':'PASS','exact_sketch_replays':5,'controls_discovery_counts':[105,105,105,106,105],'hostile_exact_tests':4,'fresh_full_Hankel_certificates':1,'new_full_Hankel_readings_checked':18790154,'code_freeze_preserved':True,'full_verifier_unchanged_from_PR182':True,'physical_promotion':0,'independent_review':'pending'}
if __name__=='__main__':
 r=validate();(P/'VALIDATION.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
