"""Postexecution evidence packaging only; no numerical gate or source edit."""
from pathlib import Path
import hashlib,json,shutil
P=Path(__file__).resolve().parent;ROOT=P.parent
sha=lambda q:hashlib.sha256(Path(q).read_bytes()).hexdigest()
freeze=json.loads((P/'RUNNER_FREEZE.json').read_text())
assert all(sha(P/n)==h for n,h in freeze['code_sha256'].items())
for mode,source in [('witness','offline-review-witness-test'),('raw','offline-review-raw-test'),('witness-v2','offline-review-witness-v2-test')]:
 source=ROOT/source;receipt=json.loads((source/'RUN_RECEIPT.json').read_text());assert receipt['status']=='PASS_CONSTRUCTOR_REPLAY_ONLY' and receipt['external_nonconstructor_review']=='PENDING' and receipt['reviewer_identity'] is None
 target=P/'executions'/mode;target.mkdir(parents=True,exist_ok=True)
 for q in [source/'RUN_RECEIPT.json',*source.glob('*.log')]:shutil.copyfile(q,target/q.name)
 for command in receipt['commands']:assert (target/command['log']).is_file() and sha(target/command['log'])==command['log_sha256'] and command['returncode']==0
 if mode=='raw':
  for name in ['baseline','cyclic_unit','dense_unit']:
   out=target/'raw-receipts'/name;out.mkdir(parents=True,exist_ok=True)
   for fn in ['RAW_REPLAY.json','PROJECTION_REPLAY.json']:
    q=source/'record-contract-raw-replay/results'/name/fn
    if q.exists():shutil.copyfile(q,out/fn)
  for src,fn in [(source/'generated-PR195-records/RAW_REGENERATION_RECEIPT.json','PR195_RAW_REGENERATION_RECEIPT.json'),(source/'uniform-two-work/records/RAW_NOISE_REGENERATION.json','PR201_RAW_REGENERATION_RECEIPT.json'),(source/'rounding-replay-work/RAW_PROJECTION_REPLAY.json','PR208_RAW_PROJECTION_REPLAY.json')]:shutil.copyfile(src,target/fn)
v2=json.loads((P/'RUNNER_V2_FREEZE.json').read_text());assert all(sha(P/n)==h for n,h in v2['code_sha256'].items())
supplement=json.loads((P/'supplemental-execution/RECEIPT.json').read_text());assert supplement['status']=='PASS_EXPLICIT_SUPPLEMENTAL_CONSTRUCTOR_REPLAY' and supplement['summary']['negative_controls']==4
summary={'status':'PASS_FROZEN_OFFLINE_RUNNER_WITNESS_AND_RAW_MODES','code_freeze_sha256':sha(P/'RUNNER_FREEZE.json'),'v2_code_freeze_sha256':sha(P/'RUNNER_V2_FREEZE.json'),'v2_tested_mode':'witness only','v1_tested_modes':['witness','raw'],'v2_raw_end_to_end_executed':False,'v1_raw_empty_phase_log':'Exit-code-only evidence; not a stand-alone phase replay attestation','strict_supplemental_phase_replay':'PASS; actual parsed2phase/1HOLD/4controls','strict_supplemental_receipt_sha256':sha(P/'supplemental-execution/RECEIPT.json'),'witness_command_count':len(json.loads((P/'executions/witness/RUN_RECEIPT.json').read_text())['commands']),'raw_command_count':len(json.loads((P/'executions/raw/RUN_RECEIPT.json').read_text())['commands']),'raw_source_records_regenerated':4,'PR195_scalar_entries_regenerated':75160616,'PR204_scalar_differences_checked':56370462,'PR204_exact_eligible_Gram_reprojections':2,'PR208_scalar_differences_checked':18790154,'PR208_integer_projection_entries_checked':2629311,'fresh_estimator_runs':0,'fresh_SVD_runs':0,'external_nonconstructor_review':'PENDING','automatic_reviewer_identity':None,'fixture_control_count':len(json.loads((P/'SAFE_INTAKE_TESTS.json').read_text())['controls']),'witness_log_guard_control_count':len(json.loads((P/'LOG_GUARD_TESTS.json').read_text())['rows']),'physical_promotion':0,'lane':'development — no registry entry','postexecution_packaging_driver':True,'raw_sources_omitted_reproducible':True}
(P/'SUMMARY.json').write_text(json.dumps(summary,indent=2))
files=[{'path':str(q.relative_to(P)),'size_bytes':q.stat().st_size,'sha256':sha(q)} for q in sorted(P.rglob('*')) if q.is_file() and q.name!='MANIFEST.json' and '__pycache__' not in q.parts]
(P/'MANIFEST.json').write_text(json.dumps({'status':summary['status'],'external_nonconstructor_review':'PENDING','physical_promotion':0,'files':files},indent=2));print(json.dumps(summary,indent=2))
