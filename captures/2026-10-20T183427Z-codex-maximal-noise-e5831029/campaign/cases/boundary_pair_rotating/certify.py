"""Full exact saved-output verifier for one new computational one-shot tuple."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,gzip,hashlib,importlib.util,json,resource,time
from pathlib import Path
import numpy as np
from common import P,CASE,repo,freeze,sha,need,a,up,down,write_new,guard,shared_raw
import estimator,phase,exact_math as e

def theorem():
 path=repo()/'captures/2026-10-19T230959Z-codex-quality-equation-intake-a735ce68/equation/certify.py';spec=importlib.util.spec_from_file_location('fresh_fixed_phase_theorem',path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);_,c=m.bound(repo());old=repo()/'captures/2026-10-19T222108Z-codex-uniform-phase-evidence-4a6f6bda/phase/primary/CERTIFICATE.json';C=c.aa(json.loads(old.read_text())['sketch']['per_62_vector_noise_multiplier_upper']);return m,c,C

def qualify(raw):
 f=freeze();d=shared_raw(raw);runfile=json.loads((P/'RUN_EXECUTIONS.json').read_text());need(runfile['protocol_sha256']==sha(P/'FREEZE.json')and runfile['data_freeze_sha256']==sha(P/'DATA_FREEZE.json')and len(runfile['rows'])==1,'one run chain');r=runfile['rows'][0];need(r['case']==CASE and r['record_sha256']==d['record']['record_sha256'],'actual record identity');row={'case':CASE,'record_sha256':r['record_sha256'],'execution_status':r['execution_status'],'learned_order':r.get('learned_order'),'status':'HOLD_EXECUTION_OR_ORDER','no_prior_campaign_status_changed':True}
 if r['execution_status']!='COMPLETED'or r.get('learned_order')!=209:return row,None
 case=P/'results'/CASE;need(json.loads((case/'RUN.json').read_text())==r,'saved execution identity');need(set(r['numeric_witnesses'])=={'SVD_META.npz','U_0.npz','U_1.npz','U_2.npz','PHASE_META.npz','PHASE_PROPOSAL.npz'},'complete tuple')
 for name,h in r['numeric_witnesses'].items():need(sha(case/name)==h,'saved tuple hash '+name)
 N,projection=estimator.project(raw);need(projection==d['record']['projection']==r['projection'],'exact fresh projection identity')
 with np.load(case/'SVD_META.npz',allow_pickle=False)as z:s=z['singular'];vt=z['right_transpose']
 actual_rank=e.saved_rank(s);need(actual_rank==209==r['learned_order'],'independent exact saved rank must match209 and actual proposer order')
 U=np.vstack([np.load(case/f'U_{i}.npz',allow_pickle=False)['basis']for i in range(3)])
 with np.load(case/'PHASE_META.npz',allow_pickle=False)as z:T=z['shift']
 measured,payload=e.measure(N,U,s,vt,T);del N;ph=phase.qualify(case/'PHASE_META.npz',case/'PHASE_PROPOSAL.npz');caps=json.loads((P/'inputs/EQUATION_CAPS.json').read_text())['quality_caps'];overrides={k:measured[k]for k in['etaU','etaV','xi','sA','proposed_smin']}
 for own,other in[('rho','inverse_residual'),('h','proposed_inverse_norm'),('eV','eigenpair_residual'),('a','emitted_argument_error')]:overrides[own]=ph['metrics'][other]
 gates={k:bool(0<=a(overrides[k])<=a(caps[k]))for k in['etaU','etaV','xi','sA','rho','h','eV','a']};m,c,C=theorem();floor=a(json.loads((P/'inputs/PARENT_ORDER.json').read_text())['qth_sigma_lower'])-C*a([3,1<<49])-a(caps['singular_floor_debit']);gates['positive_proposed_singular_floor']=bool(floor>0 and a(measured['proposed_smin'])>=floor);imp=m.evaluate(repo(),c,C,[3,1<<49],overrides)
 gates['conditional_phase_implication']=imp['status']=='CERTIFIED_UNIFORM_PHASE_TARGET_BIJECTION'
 if gates['conditional_phase_implication']:gates['strict_eigenvalue_disks']=bool(0<=a(imp['eigenvalue_radius_upper'])<1 and a(imp['eigenvalue_radius_upper'])<a(imp['source_half_chord_lower'])and a(imp['phase_matching_margin_lower'])>0)
 else:gates['strict_eigenvalue_disks']=False
 expected={'inverse_residual','proposed_inverse_norm','eigenpair_residual','emitted_argument_error','emission_ties_even_consistency','finite_observed_bijection'};gates['finite_phase_and_encoding']=ph['status']=='CERTIFIED_FINITE_EMITTED_MATCH_AND_SAVED_NUMERICAL_QUALITY'and set(ph['gates'])==expected and all(type(v)is bool and v for v in ph['gates'].values());gates['finite_LS_posterior']=measured['LS']['status']=='CERTIFIED_FINITE_SAVED_LS_STEP_DISTANCE';gates['fixed_lag_route']=measured['lag']['route']=='PRESELECTED_GRAM_FROBENIUS_ONLY';shared_raw(raw)
 row.update(independent_saved_rank=actual_rank,saved_rank_cutoff=[1,1<<24],status='CERTIFIED_FRESH_COMPUTATIONAL_OPERATOR_POSTERIOR_PROFILE'if all(gates.values())else'HOLD_FRESH_COMPUTATIONAL_POSTERIOR_GATE',gates=gates,measured=measured,phase=ph,conditional_implication=imp,required_singular_floor_lower=down(floor),saved_witness_set=r['numeric_witnesses']);payload.update(case=CASE,record_sha256=r['record_sha256'],saved_witness_set=r['numeric_witnesses']);return row,payload

def run(raw,out):
 freeze();start=time.perf_counter();out.mkdir(parents=True,exist_ok=False)
 try:
  row,payload=qualify(raw)
  if payload is not None:
   body=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();name='EXACT_MATRIX_WITNESS.json.gz'
   with(out/name).open('xb')as f:f.write(gzip.compress(body,mtime=0))
   row.update(matrix_witness_file=name,matrix_witness_sha256=sha(out/name),matrix_witness_bytes=(out/name).stat().st_size,canonical_matrix_payload_sha256=hashlib.sha256(body).hexdigest())
 except Exception as exc:row={'case':CASE,'status':'HOLD_EXACT_FRESH_CERTIFICATION_EXCEPTION','error':{'type':type(exc).__name__,'message':str(exc)},'policy':'No precision/cap/rank/route/data/estimator retry or fallback'}
 freeze();result={'status':'ONE_COMPUTATIONAL_FRESH_OUTPUT_CHECK_COMPLETE','profile':'OPERATOR_POSTERIOR_ADMISSION_FRESH_NUMERICAL_v0.1','row':row,'protocol_sha256':sha(P/'FREEZE.json'),'data_freeze_sha256':sha(P/'DATA_FREEZE.json'),'run_executions_sha256':sha(P/'RUN_EXECUTIONS.json'),'new_estimator_calls_in_verifier':0,'new_raw_records_in_verifier':0,'new_factor_copies':0,'fixed_lag_route':'Gram_Frobenius','new_LS_distance_cutoff':None,'lineage':'New computational out-of-fit perturbation only; same exposed nominal model and phase targets; no blinded or independent physical fresh lineage','uniform_backend_success':False,'exact_spectrum_T_claimed':False,'newcase_full_reconstruction_and_sigma210_lower':'NOT_EVALUATED','old_campaign_statuses_unchanged':True,'external_review':'PENDING','physical_promotion':0};write_new(out/'CERTIFICATE.json',result);write_new(out/'RESOURCE.json',{'elapsed_seconds':time.perf_counter()-start,'process_max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'scope':'Host-specific exact fresh verifier; not full Hankel or estimator benchmark'});print(json.dumps({'status':row['status'],'gates':row.get('gates'),'readable':row.get('measured',{}).get('readable')}),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--raw',required=True);p.add_argument('--out',required=True);q=p.parse_args();os.environ['UD_REPO']=str(Path(q.repo).resolve());run(Path(q.raw).resolve(),guard(q.out))
