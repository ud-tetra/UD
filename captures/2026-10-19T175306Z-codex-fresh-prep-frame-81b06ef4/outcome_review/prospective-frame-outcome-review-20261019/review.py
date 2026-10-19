"""Read-only same-team outcome audit; no raw generation or estimator execution."""
import hashlib,json,datetime
from fractions import Fraction as F
from pathlib import Path
from flint import arb,fmpq,ctx
ctx.prec=512
P=Path(__file__).resolve().parent;S=P.parent/'prospective-frame-work'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
a=lambda v:arb(fmpq(int(v[0]),int(v[1])))
def up(v):
 n=(v*(1<<180)).ceil().unique_fmpz();assert n is not None
 return [int(n),1<<180]
freeze=json.loads((P/'REVIEW_FREEZE.json').read_text())
assert sha(Path(__file__))==freeze['code_sha256']
assert freeze['inputs_sha256']=={n:sha(S/n) for n in freeze['inputs_sha256']}
protocol=json.loads((S/'PROTOCOL_FREEZE.json').read_text())
assert all(sha(S/n)==h for n,h in protocol['files'].items())
prefinal=json.loads((P.parent/'prospective-frame-review-20261019/FINAL_REVIEW_METADATA.json').read_text())
assert all(sha(S/n)==h for n,h in prefinal['reviewed_source_hashes'].items())
data=json.loads((S/'DATA_FREEZE.json').read_text());runs=json.loads((S/'RUN_EXECUTIONS.json').read_text())['rows']
align=json.loads((S/'ALIGNMENT_FREEZE.json').read_text());cert=json.loads((S/'CERTIFICATE.json').read_text())
budget=json.loads((S/'inputs/FIXED_BUDGET.json').read_text())['source_budget']
uniform=json.loads((S/'inputs/PARENT_UNIFORM.json').read_text())
assert protocol['fixed_budget']==budget
assert data['protocol_sha256']==sha(S/'PROTOCOL_FREEZE.json')
assert align['data_freeze_sha256']==sha(S/'DATA_FREEZE.json')
assert align['run_executions_sha256']==sha(S/'RUN_EXECUTIONS.json')
assert all(sha(S/n)==h for n,h in align['files'].items())
for key,name in [('budget_sha256','inputs/FIXED_BUDGET.json'),('protocol_sha256','PROTOCOL_FREEZE.json'),('data_freeze_sha256','DATA_FREEZE.json'),('alignment_freeze_sha256','ALIGNMENT_FREEZE.json')]:assert cert[key]==sha(S/name)
base=json.loads((S/'inputs/BASE_GENERATION.json').read_text())
d0=F(*next(r for r in base['records'] if r['record_sha256']==protocol['baseline_sha256'])['evaluation_bounds']['scalar_waveform_error_upper']);qraw=F(1,1<<48)
beta=a(uniform['deleted_two_rows_beta_lower']);sig=a(uniform['comparison_shift_residual_upper']);M=a(uniform['comparison_shift_norm_upper'])
rows=[]
assert len(protocol['cases'])==len(data['records'])==len(runs)==len(cert['rows'])==3
for recipe,record,run,row in zip(protocol['cases'],data['records'],runs,cert['rows']):
 n=recipe['case'];assert n==record['case']==run['case']==row['case']
 assert record['recipe']==recipe and record['record_sha256']==run['record_sha256']==row['record_sha256']
 assert run==json.loads((S/'results'/n/'RUN.json').read_text())
 assert all(sha(S/'results'/n/k)==v for k,v in run['numeric_witnesses'].items())
 assert run['learned_order']==209 and run['execution_status']=='COMPLETED' and run['execution_error'] is None
 assert run['rank_not_forced'] and not run['source_phases_loaded_by_estimator'] and not run['full_SVD_certificate_executed']
 assert record['old_original_baseline_ball_eligibility_claimed'] is False and record['new_physical_data'] is False
 assert record['readings_checked']==18790154 and record['per_new_nominal_vector_integer_error_squared_max']==1
 mat=record['transform_integer_matrix'];den=record['transform_denominator']
 assert len(mat)==37 and all(len(z)==37 for z in mat)
 assert all(not mat[i][j] or i%2==j%2 for i in range(37) for j in range(37))
 assert all(sum(mat[i][k]*mat[j][k] for k in range(37))==(den*den if i==j else 0) for i in range(37) for j in range(37))
 dnom=F(7,5)*d0+F(2,5)*qraw if recipe['kind']=='rational_pair' else d0
 assert F(*record['source_error_bounds']['fresh_nominal_scalar_source_error'])==dnom
 assert F(*record['source_error_bounds']['fresh_vector_squared_source_error'])==62*dnom*dnom+2*dnom*qraw+qraw*qraw
 eta=a(row['retained_Gram_defect_F_upper']);nu=a(row['normal_F_upper']);r=a(row['alignment_residual_F_upper'])
 sine=r/(1-eta).sqrt();dist=(2-2*(1-sine*sine).sqrt()).sqrt()
 J=(1+eta).sqrt()*(sig+(1+M)*dist);amin=(1-eta).sqrt()*(beta-dist)
 returned=(J*J+nu*nu/(amin*amin)).sqrt()
 # Production cert evaluates directly from exact squares, not their rounded
 # display uppers. Reusing display uppers here can only weaken the bound.
 assert eta<=a(budget['retained_Gram_cap']) and nu<=a(budget['normal_cap']) and r<a(budget['allowed_raw_frame_residual_lower'])
 assert returned<a(budget['allowance_lower'])
 assert a(row['actual_raw_shift_squared']).sqrt()<=returned
 assert all(row['gates'].values()) and row['status']=='CERTIFIED_FRESH_MEASURED_SOURCE_FRAME_SHIFT'
 rows.append({'case':n,'status':'PASS_SCOPED_OUTCOME_AUDIT','record_sha256':record['record_sha256'],'independent_upper_from_display_bounds':up(returned),'readable_shift_upper':float(returned.upper())})
assert cert['certified']==3 and cert['held']==0 and cert['external_review']=='PENDING' and cert['physical_promotion']==0
controls=json.loads((S/'CONTROLS.json').read_text());assert len(controls['rows'])==5 and all(r['passed'] for r in controls['rows'])
chron={n:datetime.datetime.fromtimestamp((S/n).stat().st_mtime,datetime.timezone.utc).isoformat() for n in ['PROTOCOL_FREEZE.json','DATA_FREEZE.json','RUN_EXECUTIONS.json','ALIGNMENT_FREEZE.json','CERTIFICATE.json']}
times=list(chron.values());assert times==sorted(times)
out={'status':'PASS_SCOPED_SAME_TEAM_FRESH_OUTCOME_REVIEW','rows':rows,'frozen_code_and_caps_unchanged_since_prefreeze_review':True,'hash_chronology_bindings_verified':True,'local_mtime_sequence':chron,'local_chronology_not_external_registration':True,'new_nominal_onequantum_domain_distinct_from_old_ball':True,'full_SVD_exact_order_phase_all_gates_claimed':False,'new_raw_generation_or_estimator_runs_by_review':0,'large_matrix_residual_or_full_raw_replay_claimed_by_review':False,'external_review':'PENDING','physical_promotion':0,'input_sha256':freeze['inputs_sha256']}
(P/'OUTCOME_REVIEW.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
