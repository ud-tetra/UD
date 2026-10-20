"""Independent saved-lag operator verification; quadratic identity, zero fits."""
import argparse,gzip,hashlib,importlib.util,json
from pathlib import Path
from fractions import Fraction as F
import numpy as np
P=Path(__file__).resolve().parent
SHA=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
READ=lambda p:json.loads(Path(p).read_text())
SOURCE='captures/2026-10-20T002112Z-codex-actual-equation-returns-c0caa77d'
OLD='captures/2026-10-19T222108Z-codex-uniform-phase-evidence-4a6f6bda/phase'

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--root-package',required=True);ap.add_argument('--root-output',required=True);ap.add_argument('--release',required=True);args=ap.parse_args();repo=Path(args.repo);root=Path(args.root_package);primary=Path(args.root_output);f=READ(P/'DRIVER_FREEZE.json')
 assert SHA(__file__)==f['driver_sha256']and SHA(P/'review_math_v0_2.py')==f['math_sha256'];assert SHA(root/'FREEZE.json')==f['root_freeze_sha256'];release=READ(args.release);assert release['actual_Gram_execution_released']is True
 for name,h in READ(P/'REVIEW_PLAN.json')['source_hashes'].items():assert SHA(repo/name)==h,name
 for name,h in READ(root/'FREEZE.json')['files'].items():assert SHA(root/name)==h,name
 for pin in READ(root/'SOURCE_BINDINGS.json')['pins']:assert SHA(repo/pin['path'])==pin['sha256']
 spec=importlib.util.spec_from_file_location('independent_lag_math',P/'review_math_v0_2.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 cert=READ(primary/'CERTIFICATE.json');old=READ(repo/SOURCE/'estimator_primary/CERTIFICATE.json');runs=READ(repo/SOURCE/'estimator/RUN_EXECUTIONS.json');caps=READ(repo/SOURCE/'estimator/inputs/EQUATION_CAPS.json')['quality_caps'];u=READ(repo/OLD/'inputs/PARENT_UNIFORM.json');phase=READ(repo/OLD/'inputs/PARENT_PHASE.json')['metrics'];order=READ(repo/OLD/'inputs/PARENT_ORDER.json');C=m.aa(READ(repo/OLD/'primary/CERTIFICATE.json')['sketch']['per_62_vector_noise_multiplier_upper']);rows=[]
 assert [x['case']for x in cert['rows']]==['null_top1_alternating','null_top2_alternating']
 for previous,run,result in zip(old['rows'],runs['rows'],cert['rows']):
  assert previous['case']==run['case']==result['case'];case=repo/SOURCE/'estimator/results'/run['case']
  for name,h in run['numeric_witnesses'].items():assert SHA(case/name)==h
  U=np.vstack([np.load(case/f'U_{i}.npz',allow_pickle=False)['basis']for i in range(3)])
  T=np.load(case/'PHASE_META.npz',allow_pickle=False)['shift'];assert U.shape==(8191,209)and T.shape==(209,209)
  G,b,origin=m.quadratic_gram(U,T);bounds=m.exact_bounds(G,b);assert bounds['trace']==m.fraction(previous['measured']['exact_squared']['raw_lag_F'])
  path=primary/result['Gram_file'];assert SHA(path)==result['Gram_file_sha256'];raw=gzip.decompress(path.read_bytes());assert hashlib.sha256(raw).hexdigest()==result['canonical_Gram_payload_sha256'];payload=json.loads(raw);H=m.fm([[int(x)for x in row]for row in payload['gram_numerators']]);assert payload['case']==run['case']and payload['matrix_shape']==[209,209]and payload['residual_denominator_bits']*2==b;assert G==H
  for k,our in [('trace','trace'),('absolute_row_sum','Gershgorin'),('Gram_Frobenius_squared','Gram_Frobenius_squared')]:assert m.fraction(result['norm'][k])==bounds[our],k
  assert result['norm']['selected_bound']==bounds['selected_bound'];assert abs(m.aa(result['norm']['operator_norm_upper'])-m.aa(bounds['operator_norm_upper']))<m.aa([1,1<<178])
  cap=F(1,1<<34);tests={'trace':bounds['trace']<=cap**2,'absolute_row_sum':bounds['Gershgorin']<=cap**2,'Gram_Frobenius':bounds['Gram_Frobenius_squared']<=cap**4};assert tests==result['norm']['squared_cap_tests'];admit=m.admit(G,H,b,cap,True);assert admit==any(tests.values());assert result['norm']['status']==('CERTIFIED_OPERATOR_NORM_AT_FIXED_CAP'if admit else'HOLD_NO_DECLARED_BOUND_MEETS_CAP')
  g={k:previous['measured'][k]for k in ['etaU','etaV','xi','proposed_smin']};g['sA']=result['norm']['operator_norm_upper']
  for own,other in [('rho','inverse_residual'),('h','proposed_inverse_norm'),('eV','eigenpair_residual'),('a','emitted_argument_error')]:g[own]=previous['phase']['metrics'][other]
  expr=m.expression(g,C,u,phase,order);published=result['new_operator_route'];measured=published['measured_implication']
  for k,v in expr.items():
   if k!='pointwise_disjoint_and_angle_gate':assert abs(m.aa(v)-m.aa(measured[k if k!='required_singular_floor_lower'else'required_proposed_singular_floor_lower']))<m.aa([1,1<<170]),k
  gates={k:m.fraction(g[k])<=m.fraction(caps[k])for k in ['etaU','etaV','xi','sA','rho','h','eV','a']}
  for k,value in gates.items():assert published['gates'][k]==value
  assert published['gates']['measured_singular_floor']and published['gates']['direct_finite_phase_quality']==previous['gates']['finite_saved_phase_quality'];assert published['gates']['measured_phase_implication']==expr['pointwise_disjoint_and_angle_gate']
  overall=all(gates.values())and expr['pointwise_disjoint_and_angle_gate']and previous['gates']['finite_saved_phase_quality'];assert published['status']==('CERTIFIED_SEPARATE_OPERATOR_ROUTE_FINITE_SAVED_OUTPUT'if overall else'HOLD_SEPARATE_OPERATOR_ROUTE');assert result['prior_campaign_status_preserved']==previous['status']and result['prior_gates_preserved']==previous['gates']
  row={'case':run['case'],'status':'PASS_INDEPENDENT_FULL_GRAM_OPERATOR_AND_PHASE_AUDIT','entries_checked':209**2,'Gram_denominator_power_two':b,'origin':origin,'independent_Gram_sha256':m.digest(G,b),'trace_squared_Frobenius':m.pair(bounds['trace']),'Gershgorin':m.pair(bounds['Gershgorin']),'Gram_Frobenius_squared':m.pair(bounds['Gram_Frobenius_squared']),'selected_bound':bounds['selected_bound'],'operator_norm_upper':bounds['operator_norm_upper'],'operator_cap_tests':tests,'separate_operator_route':published['status'],'prior_campaign_status_preserved':previous['status'],'phase_expression_independent':expr};rows.append(row);print(json.dumps({'case':run['case'],'review_status':row['status'],'separate_route':row['separate_operator_route']}),flush=True)
 target=P/'REVIEW_RECEIPT.json';assert not target.exists();target.write_text(json.dumps({'status':'PASS_INDEPENDENT_TWO_FULL_RESIDUAL_GRAMS_AND_SEPARATE_OPERATOR_ROUTE','rows':rows,'driver_freeze_sha256':SHA(P/'DRIVER_FREEZE.json'),'root_certificate_sha256':SHA(primary/'CERTIFICATE.json'),'root_release_sha256':SHA(args.release),'new_estimator_calls':0,'new_raw_or_factor_copies':0,'old_Frobenius_route_HOLD_immutable':True,'source_scope':'Full saved residual Grams and operator enclosures recomputed; source H/full-factor proofs and other saved metrics/direct finite phase lists inherited, hash pinned.','external_review':'PENDING','physical_promotion':0},indent=2)+'\n')
if __name__=='__main__':main()
