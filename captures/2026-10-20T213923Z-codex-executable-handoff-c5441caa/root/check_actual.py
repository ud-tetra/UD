from pathlib import Path
import json,hashlib
P=Path('/workspace/scratch/f3d1c2f040c9');R=P/'ud-repo'
oldnum=R/'captures/2026-10-20T204456Z-codex-reusable-verifier-3e0fa1e2'
oldid=R/'captures/2026-10-20T210354Z-codex-canonical-record-72c3a5bf'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows=[];count=0
for case in ['boundary_pair_block','boundary_pair_rotating']:
 out=P/'c22_primary'/case;roll=json.loads((out/'ROLLUP.json').read_text())
 assert roll['workflow_status']=='NUMERICAL_PASS_PROVENANCE_HOLD' and roll['reason'] is None
 assert [s['role'] for s in roll['stages_invoked']]==['identity','numerical','audit']
 assert all(s['returncode']==0 and s['timed_out'] is False for s in roll['stages_invoked'])
 assert roll['provenance_status']=='HOLD_PROVENANCE_NOT_ESTABLISHED' and roll['independent_acquisition']=='NOT_ESTABLISHED' and roll['fresh_preparation']=='NOT_ESTABLISHED' and roll['physical_promotion']==0
 expected={
 'identity/SCREEN.json':oldid/'primary'/case/'original/SCREEN.json',
 'numerical/CERTIFICATE.json':oldnum/'primary'/case/'CERTIFICATE.json',
 'numerical/WITNESS.json.gz':oldnum/'primary'/case/'WITNESS.json.gz',
 'audit/CERTIFICATE.json':oldnum/'matrix_review/primary'/case/'CERTIFICATE.json'}
 matches={}
 for rel,baseline in expected.items():
  assert (out/rel).read_bytes()==baseline.read_bytes(),(case,rel)
  assert sha(out/rel)==roll['artifacts_sha256'][rel]
  matches[rel]={'sha256':sha(out/rel),'baseline':str(baseline.relative_to(R))};count+=1
 rows.append({'case':case,'rollup_sha256':sha(out/'ROLLUP.json'),'scientific_outputs_byte_identical_to_frozen_child_baselines':matches})
seal=json.loads((P/'c22_runner/SEAL.json').read_text())
for n,h in seal['files'].items():assert sha(P/'c22_runner'/n)==h
receipt={'status':'PASS_TWO_COMPLETE_HANDOFFS_AND_EIGHT_SCIENTIFIC_BASELINE_MATCHES','cases':rows,'scientific_files_byte_identical':count,'root_regression_not_part_of_runner_decision':True,'same_two_old_records':True,'new_record_identities':0,'new_estimator_calls':0,'new_physical_acquisitions':0,'same_team_independent_review':'Separate reviewer checks workflow bindings; actual CRT child recomputes products per run','physical_promotion':0,'external_review':'PENDING'}
(P/'c22_root/ACTUAL_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n');print(receipt['status'])
