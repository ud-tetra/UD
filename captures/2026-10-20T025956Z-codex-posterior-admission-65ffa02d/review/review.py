"""Independent historical admission conjunction/custody audit and metadata-only hostile tests."""
import argparse,copy,hashlib,importlib.util,json
from pathlib import Path
from fractions import Fraction as F
P=Path(__file__).resolve().parent;SHA=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();R=lambda p:json.loads(Path(p).read_text())
S='captures/2026-10-20T002112Z-codex-actual-equation-returns-c0caa77d'
PHASE={'inverse_residual','proposed_inverse_norm','eigenpair_residual','emitted_argument_error','emission_ties_even_consistency','finite_observed_bijection'}
ROUTE={'etaU','etaV','xi','sA','rho','h','eV','a','measured_singular_floor','direct_finite_phase_quality','measured_phase_implication'}
OUT={'etaU','etaV','xi','rho','h','eV','a','positive_inverse_norm','Gram_defects_below_one','inverse_residual_below_one','sA','lag_original_cap','lag_exact_trace_binding','positive_certified_singular_premise','conditional_phase_premise','source_unchanged_numerical_gates','finite_saved_phase_qualification','positive_LS_floor','finite_LS_normal_bound'}
def module(name,path):
 sp=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--producer',required=True);ap.add_argument('--primary',required=True);ap.add_argument('--release',required=True);args=ap.parse_args();repo=Path(args.repo);producer=Path(args.producer);primary=Path(args.primary);f=R(P/'DRIVER_FREEZE.json');assert SHA(__file__)==f['driver_sha256']and SHA(P/'gate_math.py')==f['gate_math_sha256'];assert SHA(producer/'FREEZE.json')==f['producer_freeze_sha256'];assert R(args.release)['admission_execution_released']is True
 for name,h in R(producer/'FREEZE.json')['files'].items():assert SHA(producer/name)==h
 m=module('independent_gate_math',P/'gate_math.py');q=m.rational;profile=R(producer/'PROFILE.json');assert profile['profile_id']=='OPERATOR_POSTERIOR_ADMISSION_v0.1'and profile['lag_route']=='PR258_Gram_Frobenius_preselected'and profile['new_LS_cutoff']is None;assert profile['scope']=='HISTORICAL_ONLY_POSTKNOWN_INHERITED_EXACT_PROOF_RECEIPTS'
 b={}
 for role,pin in profile['inputs'].items():path=repo/pin['path'];assert path.stat().st_size==pin['bytes']and SHA(path)==pin['sha256'];b[role]=R(path)
 cases=list(profile['cases']);assert cases==['null_top1_alternating','null_top2_alternating']
 for role in ['actual','runs','operator','least_squares','projection']:assert [row['case']for row in b[role]['rows']]==cases
 assert [row['case']for row in b['data']['records']]==cases
 def pin(bind,path):
  rows=[x['sha256']for x in bind['pins']if x['path']==path];assert len(rows)==1;return rows[0]
 for source in [b['operator_sources'],b['LS_sources']]:
  for path,role in [(S+'/MANIFEST.json','actual_manifest'),(S+'/estimator/RUN_EXECUTIONS.json','runs'),(S+'/estimator_primary/CERTIFICATE.json','actual')]:assert pin(source,path)==profile['inputs'][role]['sha256']
 manifest={entry['path']:entry['sha256']for entry in b['actual_manifest']['files']};assert len(manifest)==len(b['actual_manifest']['files']);caps=b['caps']['quality_caps'];assert {k:q(v)for k,v in caps.items()}=={k:q(v)for k,v in profile['original_quality_caps'].items()}
 cert=R(primary/'CERTIFICATE.json');assert cert['status']=='COMPLETE_TWO_HISTORICAL_LOGICAL_REDUCTIONS'and len(cert['rows'])==2;rows=[]
 for i,(case,result)in enumerate(zip(cases,cert['rows'])):
  old,run,op,ls=[b[k]['rows'][i]for k in ['actual','runs','operator','least_squares']];data=b['data']['records'][i];assert all(row['record_sha256']==profile['cases'][case]['record_sha256']for row in [old,run,op,ls,data,result]);assert data['projection']==run['projection']==profile['cases'][case]['projection'];assert data['baseline_sha256']==profile['baseline_sha256']
  for name,h in run['numeric_witnesses'].items():
   path=S+'/estimator/results/'+case+'/'+name;assert manifest[path]==h
   if name.startswith('U_')or name=='PHASE_META.npz':assert pin(b['LS_sources'],path)==h
  assert manifest[S+'/estimator/results/'+case+'/RUN.json']==pin(b['LS_sources'],S+'/estimator/results/'+case+'/RUN.json')
  assert old['status']==profile['original_statuses'][case]==result['original_campaign_status_preserved']==op['prior_campaign_status_preserved']==ls['old_campaign_status_preserved'];assert old['gates']==result['original_campaign_gates_preserved']==op['prior_gates_preserved']==ls['old_campaign_gates_preserved']
  route=op['new_operator_route'];imp=route['measured_implication'];ph=old['phase'];pm=ph['metrics'];obs=ph['observed'];norm=op['norm'];L=ls['LS'];metrics={k:old['measured'][k]for k in ['etaU','etaV','xi']};metrics['sA']=norm['operator_norm_upper']
  for own,name in [('rho','inverse_residual'),('h','proposed_inverse_norm'),('eV','eigenpair_residual'),('a','emitted_argument_error')]:metrics[own]=pm[name]
  assert set(route['gates'])==ROUTE and set(ph['gates'])==PHASE and all(v is True for v in route['gates'].values())and all(v is True for v in ph['gates'].values());assert norm['selected_bound']=='Gram_Frobenius'and q(norm['Gram_Frobenius_squared'])>=0 and q(norm['operator_norm_upper'])**4>=q(norm['Gram_Frobenius_squared'])and q(norm['Gram_Frobenius_squared'])<=q(caps['sA'])**4;assert q(norm['trace'])==q(old['measured']['exact_squared']['raw_lag_F'])
  assert old['gates']['measured_singular_floor']is True and q(old['required_singular_floor_lower'])==q(imp['required_proposed_singular_floor_lower']);assert q(imp['noise_radius'])==q(profile['noise_radius'])and q(imp['phase_matching_margin_lower'])>0
  assert q(L['gamma_squared_lower'])==max(q(L['Gershgorin_lambda_min_lower']),q(L['identity_minus_Frobenius_lambda_min_lower']));assert q(L['normal_operator_norm_upper'])**2>=q(L['normal_Frobenius_squared'])>=0
  conjunction=m.conjunction(metrics,caps,old['required_singular_floor_lower'],old['measured']['proposed_smin'],L['normal_operator_norm_upper'],L['gamma_squared_lower'],L['LS_step_operator_distance_upper'],imp['eigenvalue_radius_upper'],imp['phase_error_upper'],imp['source_half_chord_lower'],[r['target_index']for r in obs['rows']],ph['gates']['emission_ties_even_consistency'],True,norm['selected_bound'])
  assert conjunction['admissible'];assert set(result['gates'])==OUT and all(v is True for v in result['gates'].values());assert result['status']=='HISTORICAL_FINITE_OPERATOR_PROFILE_ADMISSIBLE'
  half=q(obs['source_minimum_chord_lower'])/2;assert len(obs['rows'])==209 and {r['emitted_index']for r in obs['rows']}==set(range(209))and all(0<=q(r['circular_error_upper'])<half and r['unique_and_within_fixed_radius']is True for r in obs['rows']);assert 0<=q(obs['maximum_circular_error_upper'])<half
  rows.append({'case':case,'status':'PASS_INDEPENDENT_HISTORICAL_GATE_CONJUNCTION_AND_SAME_FIT_BINDINGS','reported_status':result['status'],'original_campaign_status_preserved':old['status'],'all19_published_gates_present_true':True,'independent_exact_predicates':conjunction['gates']})
 # Exercise producer internal semantic guards with in-memory metadata mutants only. Full public load() hash checks are intentionally bypassed here; no matrix/factor is modified.
 producer_module=module('frozen_admission_producer',producer/'reduce.py');mutants=[]
 def mutation(label,change,identity=False):
  test=copy.deepcopy(b);change(test)
  try:
   if identity:producer_module.identity(test,profile)
   else:producer_module.one(cases[0],0,test,profile,caps)
  except Exception:mutants.append({'id':label,'rejected':True});return
  raise AssertionError('hostile internal metadata accepted '+label)
 mutation('numeric_xi_overcap_with_pass_flags',lambda x:x['actual']['rows'][0]['measured'].__setitem__('xi',[1,1]))
 mutation('strict_phase_disk_touch_with_success_status',lambda x:x['operator']['rows'][0]['new_operator_route']['measured_implication'].__setitem__('eigenvalue_radius_upper',x['operator']['rows'][0]['new_operator_route']['measured_implication']['source_half_chord_lower']))
 mutation('empty_phase_gate_dictionary',lambda x:x['actual']['rows'][0]['phase'].__setitem__('gates',{}))
 mutation('missing_route_gate_dictionary',lambda x:x['operator']['rows'][0]['new_operator_route']['gates'].pop('etaU'))
 mutation('nonpositive_LS_floor',lambda x:x['least_squares']['rows'][0]['LS'].__setitem__('gamma_squared_lower',[0,1]))
 mutation('underreported_LS_distance',lambda x:x['least_squares']['rows'][0]['LS'].__setitem__('LS_step_operator_distance_upper',[0,1]))
 mutation('same_case_record_mismatch',lambda x:x['operator']['rows'][0].__setitem__('record_sha256','0'*64))
 mutation('same_record_wrong_U_witness_pin',lambda x:next(r for r in x['LS_sources']['pins']if r['path'].endswith(cases[0]+'/U_0.npz')).__setitem__('sha256','0'*64))
 mutation('unregistered_lag_route',lambda x:x['operator']['rows'][0]['norm'].__setitem__('selected_bound','absolute_row_sum'))
 mutation('duplicate_target_indices',lambda x:[r.__setitem__('target_index',0)for r in x['actual']['rows'][0]['phase']['observed']['rows']])
 mutation('wrong_case_order',lambda x:x['runs']['rows'].reverse(),True)
 mutation('changed_original_verdict',lambda x:x['actual']['rows'][0].__setitem__('status','PASS'))
 mutation('projection_hash_mismatch',lambda x:x['projection']['rows'][0].__setitem__('exact_projected_numerator_sha256','0'*64))
 mutation('missing_argument_metric',lambda x:x['actual']['rows'][0]['phase']['metrics'].pop('emitted_argument_error'))
 target=P/'ADMISSION_REVIEW_RECEIPT.json';assert not target.exists();target.write_text(json.dumps({'status':'PASS_POSTKNOWN_HISTORICAL_REDUCER_CONJUNCTION_AND_CUSTODY_REVIEW','rows':rows,'metadata_only_hostile_controls':mutants,'independent_synthetic_gate_controls':20,'freeze_sha256':SHA(P/'DRIVER_FREEZE.json'),'source_certificate_sha256':SHA(primary/'CERTIFICATE.json'),'scope':'Inherited exact matrices/normal/eigenphase evidence consumed, not recomputed; two historical logical classifications only; foreign/fresh remains HOLD, prospective fresh workflow incomplete/unexecuted. Angle versus halfchord is conservative sufficient comparison.','new_estimator_calls':0,'new_raw_or_factor_copies':0,'old_top2_Frobenius_HOLD_immutable':True,'external_review':'PENDING','physical_promotion':0},indent=2)+'\n');print(json.dumps({'status':'PASS','rows':2,'metadata_mutants_rejected':len(mutants)}))
if __name__=='__main__':main()
