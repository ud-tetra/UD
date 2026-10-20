"""Independent GammaT-Cross audit of both saved finite LS posterior certificates."""
import argparse,gzip,hashlib,importlib.util,json
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent
B='captures/2026-10-20T002112Z-codex-actual-equation-returns-c0caa77d'
SHA=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();R=lambda p:json.loads(Path(p).read_text())
def main():
 q=argparse.ArgumentParser();q.add_argument('--repo',required=True);q.add_argument('--producer',required=True);q.add_argument('--primary',required=True);q.add_argument('--release',required=True);args=q.parse_args();repo=Path(args.repo);producer=Path(args.producer);primary=Path(args.primary);f=R(P/'LS_DRIVER_FREEZE.json');assert SHA(__file__)==f['driver_sha256']and SHA(P/'review_math.py')==f['math_sha256'];assert SHA(producer/'FREEZE.json')==f['producer_freeze_sha256'];assert R(args.release)['least_squares_execution_released']is True
 for path,h in R(P/'REVIEW_PLAN.json')['source_hashes'].items():assert SHA(repo/path)==h
 for name,h in R(producer/'FREEZE.json')['files'].items():assert SHA(producer/name)==h
 for row in R(producer/'SOURCE_BINDINGS.json')['pins']:assert SHA(repo/row['path'])==row['sha256']
 sp=importlib.util.spec_from_file_location('independent_aligned_math',P/'review_math.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);cert=R(primary/'CERTIFICATE.json');old=R(repo/B/'estimator_primary/CERTIFICATE.json');rows=[]
 assert [x['case']for x in cert['rows']]==['null_top1_alternating','null_top2_alternating']
 for prior,result in zip(old['rows'],cert['rows']):
  case=result['case'];assert case==prior['case'];assert result['old_campaign_status_preserved']==prior['status']and result['old_campaign_gates_preserved']==prior['gates']
  if result['status']=='HOLD_SAVED_LS_CERTIFICATION_EXCEPTION':rows.append({'case':case,'status':'RETAINED_PRODUCER_EXCEPTION_NO_ARITHMETIC_CERTIFICATION'});continue
  path=repo/B/'estimator/results'/case;U=np.vstack([np.load(path/f'U_{k}.npz',allow_pickle=False)['basis']for k in range(3)]);T=np.load(path/'PHASE_META.npz',allow_pickle=False)['shift'];assert U.shape==(8191,209)and T.shape==(209,209)
  G,bG,N,bN,scales=m.normal_identity(U,T);p=primary/result['witness_file'];assert SHA(p)==result['witness_file_sha256'];raw=gzip.decompress(p.read_bytes());assert hashlib.sha256(raw).hexdigest()==result['canonical_payload_sha256'];payload=json.loads(raw);assert payload['case']==case and payload['matrix_shape']==[209,209]and payload['Gram_denominator_bits']==bG and payload['normal_denominator_bits']==bN
  assert G==m.fm([[int(x)for x in row]for row in payload['Gram_integer_numerators']]);assert N==m.fm([[int(x)for x in row]for row in payload['normal_integer_numerators']]);assert scales['U_bits']==result['U_denominator_bits']and scales['T_bits']==result['T_denominator_bits']
  independent=m.ls_bound(G,bG,N,bN);ls=result['LS']
  for own,pub in [('Gamma_Gershgorin_lower','Gershgorin_lambda_min_lower'),('Gamma_identity_defect_squared','Gram_minus_I_Frobenius_squared'),('Gamma_identity_lower','identity_minus_Frobenius_lambda_min_lower'),('Gamma_chosen_lower','gamma_squared_lower'),('normal_squared','normal_Frobenius_squared')]:assert m.frac(independent[own])==m.frac(ls[pub]),pub
  normal_up=m.up(m.aa(independent['normal_squared']).sqrt());assert m.frac(normal_up)==m.frac(ls['normal_operator_norm_upper'])
  distance=m.up(m.aa(normal_up)/m.aa(independent['Gamma_chosen_lower']));assert m.frac(distance)==m.frac(ls['LS_step_operator_distance_upper']);assert m.frac(independent['LS_distance_upper'])<=m.frac(distance)
  assert result['status']==ls['status']=='CERTIFIED_FINITE_SAVED_LS_STEP_DISTANCE';row={'case':case,'status':'PASS_INDEPENDENT_EXACT_GAMMA_NORMAL_POSTERIOR_AUDIT','Gamma_entries_checked':209**2,'normal_entries_checked':209**2,'Gram_denominator_bits':bG,'normal_denominator_bits':bN,'independent':independent,'published_conservative_LS_distance_upper':distance,'old_campaign_status_preserved':prior['status']};rows.append(row);print(json.dumps({'case':case,'status':row['status']}),flush=True)
 out=P/'LS_REVIEW_RECEIPT.json';assert not out.exists();out.write_text(json.dumps({'status':'COMPLETE_INDEPENDENT_SAVED_LS_POSTERIOR_AUDIT','rows':rows,'total_entries_checked':sum(x.get('Gamma_entries_checked',0)+x.get('normal_entries_checked',0)for x in rows),'freeze_sha256':SHA(P/'LS_DRIVER_FREEZE.json'),'source_certificate_sha256':SHA(primary/'CERTIFICATE.json'),'new_estimator_calls':0,'new_raw_or_factor_copies':0,'scope':'Finite saved tuple posterior LS distance, not uniform backend rounding or exact-spectrum(T) guarantee; raw lag can be nonzero at exact LS optimum','old_top2_Frobenius_HOLD_immutable':True,'external_review':'PENDING','physical_promotion':0},indent=2)+'\n')
if __name__=='__main__':main()
