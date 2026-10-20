"""Post-outcome audit index only; no estimator, numeric fitting, or raw/factor writes."""
from pathlib import Path
import datetime,hashlib,json
P=Path(__file__).resolve().parent
W=P.parent
CASES=('block257_port17','affine62_qr13','prep_port_period7')
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def read(p):return json.loads(Path(p).read_text())
def main():
 f=read(P/'POST_DRIVER_FREEZE.json')
 assert sha(P/'review_post.py')==f['driver_sha256'] and sha(P/'post_math.py')==f['post_math_sha256']
 assert sha(W/'c14_campaign/CAMPAIGN_FREEZE.json')==f['campaign_freeze_sha256']
 rows=[]
 for name in CASES:
  receipt=P/name/'POST_REVIEW_RECEIPT.json';r=read(receipt)
  source=W/'c14_campaign/cases'/name;raw=W/'c14_raw'/f'{name}.i64le';primary=W/'c14_primary'/name/'CERTIFICATE.json'
  assert sha(source/'FREEZE.json')==f['cases'][name]
  assert r['status']=='PASS_INDEPENDENT_FRESH_RAW_BOUND_FULL_EXACT_TUPLE_AUDIT'
  assert r['producer_status_preserved']=='CERTIFIED_FRESH_COMPUTATIONAL_OPERATOR_POSTERIOR_PROFILE'
  assert r['new_estimator_calls']==0 and r['new_raw_or_factor_copies']==0
  assert r['case']==name and r['actual_saved_rank_counted']==209
  assert len(r['gates'])==14 and all(type(v)is bool and v for v in r['gates'].values())
  assert r['full_exact_matrix_entries_checked']==3*209*209
  ph=r['fresh_complex_phase_and_encoding']
  assert ph['all_209_nearest_even_and_unique']is True and len(ph['finite_target_indices'])==209 and len(set(ph['finite_target_indices']))==209
  assert r['source_certificate_sha256']==sha(primary)
  assert r['record_sha256']==sha(raw) and raw.stat().st_mode&0o222==0
  assert r['raw_unchanged_after_fit_and_audit']is True
  assert r['post_driver_freeze_sha256']==sha(P/'POST_DRIVER_FREEZE.json')
  rows.append({'case':name,'status':r['status'],'producer_status_preserved':r['producer_status_preserved'],'review_receipt_sha256':sha(receipt),'raw_sha256':r['record_sha256'],'primary_certificate_sha256':sha(primary),'actual_saved_rank_counted':209,'quality_gates_passed':14,'matrix_entries_checked':r['full_exact_matrix_entries_checked'],'finite_phase_matches':209,'maximum_emitted_phase_match_error_upper':ph['maximum_match_error_upper'],'LS_step_distance_upper':r['LS']['LS_step_operator_distance_upper']})
 baseline=W/'c14_baseline_recovery/ramp_clock_stress.i64le'
 assert baseline.stat().st_mode&0o222==0 and sha(baseline)=='25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59'
 result={'artifact_type':'THREE_CASE_SAME_TEAM_INDEPENDENT_NUMERICAL_OUTPUT_REVIEW','status':'PASS_ALL_THREE_FIXED_COMPUTATIONAL_OUTPUT_AUDITS','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'rows':rows,'new_reviewer_estimator_calls':0,'new_reviewer_raw_records_or_factor_copies':0,'total_quality_gate_passes':42,'total_exact_matrix_entries_checked':393129,'total_finite_phase_matches':627,'per_case_saved_rank':209,'post_driver_freeze_sha256':sha(P/'POST_DRIVER_FREEZE.json'),'pure_post_control_count':18,'pure_post_controls_sha256':sha(P/'POST_CONTROLS.json'),'prospective_review_sha256':sha(P/'PRE_RUN_POST_REVIEW.json'),'source_H_fullfactor_frame_and_target_proofs':'Inherited and hash-bound, not independently rederived by this review','newcase_full_reconstruction_sigma210_lower':'NOT_EVALUATED','root_zero_fit_replay':'Separate root authority; not asserted by this reviewer aggregate','scope':'Three exact saved numerical tuples with source-aware computational perturbations of the same exposed nominal/model/preparations/targets. Independent implementation within the same team; not external promotion review, blinded validation, physical fresh lineage, or uniform input/backend certification.','old_campaign_HOLD_and_NO_GO_statuses_unchanged':True,'new_physical_claims':False,'lane':'development — no registry entry','external_promotion_review':'PENDING','physical_promotion':0}
 target=P/'FINAL_REVIEW.json';assert not target.exists()
 with target.open('x')as out:json.dump(result,out,indent=2);out.write('\n')
 public=['review_post.py','post_math.py','finish_review.py','POST_DRIVER_FREEZE.json','POST_CONTROLS.json','PRE_RUN_POST_REVIEW.json','FINAL_REVIEW.json']+[f'{n}/POST_REVIEW_RECEIPT.json'for n in CASES]
 manifest=P/'VERIFICATION_HASH_MANIFEST.sha256';assert not manifest.exists()
 with manifest.open('x')as out:
  for name in sorted(public):out.write(f'{sha(P/name)}  {name}\n')
 print(json.dumps({'status':result['status'],'final_review_sha256':sha(target),'hash_manifest_sha256':sha(manifest),'explicit_public_files':len(public),'matrix_entries':393129,'phase_matches':627}))
if __name__=='__main__':main()
