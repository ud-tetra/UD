"""Read-only saved-outcome/parent-log review after separate source-only crosscheck."""
from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
import hashlib,json
import mpmath as mp
mp.mp.dps=160
P=Path(__file__).resolve().parent;W=P.parent/'source-shift-work';C=P.parent/'source-shift-parent-replay'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
f=json.loads((W/'FREEZE.json').read_text());checked={}
for group,base in [('code_sha256',W),('input_sha256',W/'inputs')]:
 for n,h in f[group].items():assert sha(base/n)==h;checked[str(base/n)]=h
receipt=json.loads((C/'REPLAY_RECEIPT.json').read_text());assert receipt['status']=='PASS_COMPLETE_CAMPAIGN_REPLAY' and receipt['cases']==3 and receipt['admitted']==2 and receipt['HOLD']==1 and receipt['helper_hashes_before_after_verified'] and receipt['new_SVD_or_estimator_runs']==0
for r in receipt['logs']:
 assert r['exit_code']==0 and sha(C/(r['tag']+'.log'))==r['log_sha256'];checked[str(C/(r['tag']+'.log'))]=r['log_sha256']
prior=C/'adversarial-admission-work'
for n in ['GATE_RESULTS.json','EXACT_SHIFT_EXCEEDANCE.json']:
 assert sha(prior/n)==f['input_sha256'][n]
parentfreeze=json.loads((prior/'PROTOCOL_FREEZE.json').read_text())
for n,h in parentfreeze['helper_sha256'].items():assert sha(C/'record-contract-work'/n)==h;checked[str(C/'record-contract-work'/n)]=h
act=json.loads((W/'ACTUAL_V2.json').read_text());old=json.loads((W/'inputs/GATE_RESULTS.json').read_text());allow=json.loads((W/'SOURCE_ALLOWANCE.json').read_text());assert act['parent_replay_receipt_sha256']==sha(C/'REPLAY_RECEIPT.json')
assert act['source_allowance']==allow and act['no_new_estimator_SVD_or_raw_generation'] and act['known_record_posthoc_certificate']
source=json.loads((P/'FINAL_SOURCE_REVIEW.json').read_text());coef=mp.mpf(source['source_affine_slope']);intercept=mp.mpf(source['source_affine_intercept']);q=lambda x:mp.mpf(x[0])/x[1]
policy=json.loads((W/'inputs/PR210_FREEZE.json').read_text())['gates'];arg=q(policy['emitted_argument_error']);sep=q(json.loads((W/'inputs/PARENT_PHASE.json').read_text())['metrics']['minimum_target_chord_lower'])
rows=[]
for r,o in zip(act['rows'],old['rows']):
 assert r['case']==o['case'] and r['record_sha256']==o['record_sha256'] and r['original_PR210_policy_status']==o['status'] and r['original_policy_status_unchanged']
 assert r['status']=='CERTIFIED_RETURNED_OUTPUT_V2' and all(r['checks'].values()) and not r['failed']
 for name,gate in allow['other_seven_gates'].items():assert Fraction(*o['metrics'][name])<=Fraction(*gate)
 assert Fraction(*o['metrics']['raw_shift_residual'])<Fraction(*allow['raw_shift_strict_upper_allowance_lower'])
 radius=intercept+coef*q(o['metrics']['raw_shift_residual']);angle=mp.asin(radius)+arg
 assert radius<=q(r['radius_upper']) and angle<=q(r['phase_error_upper_if_certified']) and 2*angle<sep and Fraction(*r['matching_margin_lower'])>0
 rows.append({'case':r['case'],'old_policy_status':o['status'],'v2_status':r['status'],'independently_crosschecked_phase':mp.nstr(angle,100),'phase_upper':r['phase_error_upper_if_certified']})
assert len(rows)==3 and rows[-1]['old_policy_status']=='HOLD_OUTPUT_GATES'
controls=json.loads((W/'CONTROLS.json').read_text());assert controls['status']=='PASS_FINITE_V2_BOUNDARIES' and len(controls['controls'])==13 and controls['synthetic_metric_controls_not_actual_estimator_runs']
byname={r['name']:r for r in controls['controls']}
assert byname['equality_to_lower_allowance_is_HOLD']['status']=='HOLD_V2' and byname['one_dyadic_unit_below_allowance']['status']=='CERTIFIED_RETURNED_OUTPUT_V2'
assert all(byname['exceeded_'+n]['status']=='HOLD_V2' for n in allow['other_seven_gates'])
assert all(sha(Path(p))==h for p,h in checked.items())
result={'status':'PASS_SAME_TEAM_SAVED_OUTCOME_AND_PARENT_REPLAY_REVIEW','reviewed_at_utc':datetime.now(timezone.utc).isoformat(),'review_code_sha256':sha(__file__),'source_only_review_sha256':sha(P/'FINAL_SOURCE_REVIEW.json'),'verified_hashes_before_after':checked,'parent_replay_receipt_sha256':sha(C/'REPLAY_RECEIPT.json'),'actual_v2_sha256':sha(W/'ACTUAL_V2.json'),'controls_sha256':sha(W/'CONTROLS.json'),'rows':rows,'synthetic_metric_controls':13,'scope':'Read-only hash/log/retained-policy checks and independent-expression numerical diagnostic. Primary validated outward authority remains frozen Arb certificates. No new estimator/SVD/raw generation.','findings':['Fresh complete parent replay and every log hash verify.','All seven old maxima unchanged and checked; v2 strict source allowance holds for all three saved metric upperbounds.','Directed v1HOLD remains retained alongside distinct v2PASS.','Peroutput phasebounds are separately computed; v1numerical promise is not reused.','All13synthetic boundary/refusal controls retained; no claim of new solver/physical trials.'],'material_issues':[],'new_estimator_runs':0,'new_SVD_runs':0,'new_raw_generation':False,'external_independent_review':'PENDING','physical_promotion':0,'lane':'development — no registry entry'}
(P/'FINAL_OUTCOME_REVIEW.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:result[k] for k in ['status','material_issues']}))
