"""Index fixed output audits and retain every PASS/HOLD; no fit or raw/factor writes."""
from pathlib import Path
import datetime,hashlib,json
P=Path(__file__).resolve().parent;W=P.parent;CASES=('boundary_pair_block','boundary_pair_rotating')
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def read(p):return json.loads(Path(p).read_text())
def main():
 f=read(P/'POST_DRIVER_FREEZE.json')
 for name,key in [('review_post.py','driver_sha256'),('post_math.py','post_math_sha256'),('metric_bindings.py','metric_bindings_sha256'),('finish_review.py','finisher_sha256')]:assert sha(P/name)==f[key]
 assert sha(W/'c15_campaign/CAMPAIGN_FREEZE.json')==f['campaign_freeze_sha256'];rows=[]
 for name in CASES:
  receipt=P/name/'POST_REVIEW_RECEIPT.json';r=read(receipt);source=W/'c15_campaign/cases'/name;raw=W/'c15_raw'/f'{name}.i64le';primary=W/'c15_primary'/name/'CERTIFICATE.json';cert=read(primary);datum=read(source/'DATA_FREEZE.json')['record']
  assert sha(source/'FREEZE.json')==f['cases'][name];assert r['new_estimator_calls']==0;assert sha(raw)==datum['record_sha256']and raw.stat().st_mode&0o222==0
  checked=r['status']=='PASS_INDEPENDENT_FRESH_RAW_BOUND_FULL_EXACT_TUPLE_AUDIT'
  if checked:
   assert r['new_raw_or_factor_copies']==0 and r['case']==name and r['actual_saved_rank_counted']==209
   assert r['source_certificate_sha256']==sha(primary)and r['record_sha256']==datum['record_sha256'];assert r['raw_unchanged_after_fit_and_audit']is True and r['post_driver_freeze_sha256']==sha(P/'POST_DRIVER_FREEZE.json')
   assert len(r['gates'])==14 and all(type(x)is bool for x in r['gates'].values());assert r['gates']==cert['row']['gates'];assert r['full_exact_matrix_entries_checked']==3*209*209
   ph=r['fresh_complex_phase_and_encoding'];assert ph['all_209_nearest_even_and_unique']is True and len(set(ph['finite_target_indices']))==209
   assert r['advertised_phase_metric_enclosures']['status']=='PASS_INDEPENDENT_ADVERTISED_PHASE_METRIC_ENCLOSURES';assert r['advertised_phase_metric_enclosures']['actual_argument_errors_compared_to_advertised_bound']==209
  else:assert r['status'].startswith(('HOLD_','RETAINED_'))
  allgates=checked and all(r['gates'].values())and cert['row']['status']=='CERTIFIED_FRESH_COMPUTATIONAL_OPERATOR_POSTERIOR_PROFILE'
  rows.append({'case':name,'status':r['status'],'producer_status_preserved':cert['row']['status'],'review_receipt_sha256':sha(receipt),'raw_sha256':datum['record_sha256'],'primary_certificate_sha256':sha(primary),'all_quality_gates_pass':allgates,'actual_saved_rank_counted':r.get('actual_saved_rank_counted'),'quality_gates_passed':sum(r.get('gates',{}).values()),'matrix_entries_checked':r.get('full_exact_matrix_entries_checked',0),'finite_phase_matches':209 if checked else 0,'advertised_metric_enclosures_pass':checked,'maximum_emitted_phase_match_error_upper':r.get('fresh_complex_phase_and_encoding',{}).get('maximum_match_error_upper'),'LS_step_distance_upper':r.get('LS',{}).get('LS_step_operator_distance_upper')})
 baseline=W/'c15_baseline_recovery/ramp_clock_stress.i64le';assert baseline.stat().st_mode&0o222==0 and sha(baseline)=='25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59'
 result={'artifact_type':'TWO_CASE_SAME_TEAM_INDEPENDENT_NUMERICAL_OUTPUT_REVIEW','status':'PASS_BOTH_FIXED_COMPUTATIONAL_OUTPUT_AUDITS'if all(x['all_quality_gates_pass']for x in rows)else'COMPLETED_FIXED_AUDITS_WITH_RETAINED_HOLDS','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'rows':rows,'new_reviewer_estimator_calls':0,'new_reviewer_raw_records_or_factor_copies':0,'total_quality_gate_passes':sum(x['quality_gates_passed']for x in rows),'total_exact_matrix_entries_checked':sum(x['matrix_entries_checked']for x in rows),'total_finite_phase_matches':sum(x['finite_phase_matches']for x in rows),'post_driver_freeze_sha256':sha(P/'POST_DRIVER_FREEZE.json'),'pure_post_control_count':27,'pure_post_controls_sha256':sha(P/'POST_CONTROLS.json'),'prospective_review_sha256':sha(P/'PRE_RUN_POST_REVIEW.json'),'source_H_fullfactor_frame_and_target_proofs':'Inherited and hash-bound, not independently rederived by this review','newcase_full_reconstruction_sigma210_lower':'NOT_EVALUATED','root_zero_fit_replay':'Separate root authority; not asserted by this reviewer aggregate','scope':'Two fixed exact saved tuples; same exposed computational model/preparations/targets. Same-team independent implementation only; no blinded validation, physical fresh lineage, uniform input/backend certification or external promotion review. Metric-enclosure hardening was frozen before new fits and does not change older campaign verdicts.','old_campaign_HOLD_and_NO_GO_statuses_unchanged':True,'new_physical_claims':False,'lane':'development — no registry entry','external_promotion_review':'PENDING','physical_promotion':0}
 with(P/'FINAL_REVIEW.json').open('x')as out:json.dump(result,out,indent=2);out.write('\n')
 public=['review_post.py','post_math.py','metric_bindings.py','finish_review.py','POST_CODE_FREEZE.json','POST_DRIVER_FREEZE.json','POST_CONTROLS.json','PRE_RUN_POST_REVIEW.json','FINAL_REVIEW.json']+[f'{n}/POST_REVIEW_RECEIPT.json'for n in CASES]
 with(P/'VERIFICATION_HASH_MANIFEST.sha256').open('x')as out:
  for name in sorted(public):out.write(f'{sha(P/name)}  {name}\n')
 print(json.dumps({'status':result['status'],'final_review_sha256':sha(P/'FINAL_REVIEW.json'),'hash_manifest_sha256':sha(P/'VERIFICATION_HASH_MANIFEST.sha256'),'explicit_public_files':len(public),'matrix_entries':result['total_exact_matrix_entries_checked'],'phase_matches':result['total_finite_phase_matches']}))
if __name__=='__main__':main()
