"""Independent norm constants, exact rational envelopes and every frozen grid row."""
import argparse,hashlib,importlib.util,json
from fractions import Fraction as F
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent
B='captures/2026-10-20T002112Z-codex-actual-equation-returns-c0caa77d';OP='captures/2026-10-20T005052Z-codex-lag-operator-e5e3f0a0';OLD='captures/2026-10-19T222108Z-codex-uniform-phase-evidence-4a6f6bda/phase'
R=lambda p:json.loads(Path(p).read_text());SHA=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();q=lambda p:F(int(p[0]),int(p[1]))

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--root-package',required=True);ap.add_argument('--root-output',required=True);ap.add_argument('--release',required=True);args=ap.parse_args();repo=Path(args.repo);root=Path(args.root_package);primary=Path(args.root_output);freeze=R(P/'DRIVER_FREEZE.json');assert SHA(__file__)==freeze['driver_sha256']and SHA(P/'math_review.py')==freeze['math_sha256'];assert SHA(root/freeze['root_freeze_file'])==freeze['root_freeze_sha256'];assert R(args.release)['factor_budget_execution_released']is True
 for path,h in R(P/'REVIEW_PLAN.json')['source_hashes'].items():assert SHA(repo/path)==h
 rf=R(root/freeze['root_freeze_file'])
 for name,h in rf['files'].items():assert SHA(root/name)==h
 for capture in [B,OP]:
  for entry in R(repo/capture/'MANIFEST.json')['files']:assert SHA(repo/entry['path'])==entry['sha256']and(repo/entry['path']).stat().st_size==entry['size_bytes']
 spec=importlib.util.spec_from_file_location('independent_budget_math',P/'math_review.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 old=R(repo/B/'estimator_primary/CERTIFICATE.json');ops=R(repo/OP/'primary/CERTIFICATE.json');data=R(repo/B/'estimator/DATA_FREEZE.json');cert=R(primary/'CERTIFICATE.json');caps=R(repo/B/'estimator/inputs/EQUATION_CAPS.json')['quality_caps'];u=R(repo/OLD/'inputs/PARENT_UNIFORM.json');pm=R(repo/OLD/'inputs/PARENT_PHASE.json')['metrics'];order=R(repo/OLD/'inputs/PARENT_ORDER.json');C=m.aa(R(repo/OLD/'primary/CERTIFICATE.json')['sketch']['per_62_vector_noise_multiplier_upper']);floor=m.aa(order['qth_sigma_lower'])-C*m.aa([3,1<<49])-m.aa([1,1<<41]);rows=[]
 assert cert['grid_k']==list(range(20,101))and len(cert['rows'])==2
 for prior,op,datum,published in zip(old['rows'],ops['rows'],data['records'],cert['rows']):
  name=prior['case'];assert name==op['case']==datum['case']==published['case'];path=repo/B/'estimator/results'/name
  z=np.load(path/'PHASE_META.npz',allow_pickle=False);T=z['shift'];W=z['eigenvectors'];s=np.load(path/'SVD_META.npz',allow_pickle=False)['singular'];t2=m.exact_frobenius_squared(T);w2=m.exact_frobenius_squared(W)
  assert t2==q(published['constant_witnesses']['shift_Frobenius_squared_exact'])and w2==q(published['constant_witnesses']['eigenbasis_Frobenius_squared_exact'])
  c={k:q(prior['measured'][k])for k in ['etaU','etaV','xi']}
  c.update(U=q(m.up((1+m.aa(c['etaU'])).sqrt())),V=q(m.up((1+m.aa(c['etaV'])).sqrt())),T=q(m.up(m.aa(t2).sqrt())),W=q(m.up(m.aa(w2).sqrt())),Sigma=max(m.scalar(v)for v in s[:209]),smin=min(m.scalar(v)for v in s[:209]),ell=q(op['norm']['operator_norm_upper']))
  c['Z']=q(m.up(m.aa(F(8191*321)).sqrt()*m.aa(F(datum['projection']['numerator_max'],1<<55))))
  for own,oldname in [('eV','eigenpair_residual'),('rho','inverse_residual'),('h','proposed_inverse_norm'),('a','emitted_argument_error')]:c[own]=q(prior['phase']['metrics'][oldname])
  assert {k:q(v)for k,v in published['constants'].items()}==c
  certified=[];phase_checked=0;assert [r['k']for r in published['all_joint_grid_rows']]==list(range(20,101))
  for row in published['all_joint_grid_rows']:
   k=row['k'];e=F(1,1<<k);assert q(row['typed_common_radius'])==e
   # Independently associated rational polynomial evaluation, no interval rounding of envelopes.
   g={key:c[key]for key in ['rho','h','a']};g.update(etaU=(c['etaU']+e*e)+(c['U']+c['U'])*e,etaV=(c['etaV']+e*e)+(c['V']+c['V'])*e,xi=c['xi']+(c['Sigma']+c['Z']+c['U'])*e+e*e,sA=c['ell']+(1+c['U']+c['T'])*e+e*e,eV=c['eV']+e*c['W'],proposed_smin=c['smin']-e)
   assert {key:q(v)for key,v in row['bounds'].items()}==g
   gates={key:g[key]<=q(caps[key])for key in ['etaU','etaV','xi','sA','rho','h','eV','a']};gates['positive_measured_singular_floor']=bool(floor>0 and m.aa(g['proposed_smin'])>=floor);assert row['fixed_gates']==gates
   if all(gates.values()):
    phase_checked+=1
    proof=m.phase({key:m.aa(v)for key,v in g.items()},C,u,pm,order);assert proof['status']==row['phase']['status']
    for key,value in proof.items():
     if key!='status':assert abs(m.aa(value)-m.aa(row['phase'][key]))<m.aa([1,1<<170]),key
    expected='CERTIFIED_WHOLE_TYPED_FACTOR_BOX'if proof['status']=='CERTIFIED_UNIFORM_PHASE_TARGET_BIJECTION'else'HOLD_PHASE_ENVELOPE'
   else:expected='HOLD_INSUFFICIENT_QUALITY_ENVELOPE';assert row['phase']['status']=='NOT_EVALUATED_QUALITY_GATES_HOLD'
   assert row['status']==expected
   if expected=='CERTIFIED_WHOLE_TYPED_FACTOR_BOX':certified.append(k)
  selected=published['joint_largest_grid_certified'];assert (selected is None)==(not certified)
  if certified:
   assert selected==published['all_joint_grid_rows'][min(certified)-20]
   before=next((r for r in published['all_joint_grid_rows']if r['k']==min(certified)-1),None)
   assert published['next_larger_grid_envelope_failures']==(None if before is None else[key for key,value in before['fixed_gates'].items()if not value])
  lagpass=[];assert [r['k']for r in published['all_lag_only_grid_rows']]==list(range(20,101));tau=F(1,1<<34);K=c['U']+c['T']+1;slack=tau-c['ell'];assert q(published['lag_slack_exact'])==slack
  for row in published['all_lag_only_grid_rows']:
   e=F(1,1<<row['k']);value=e*(K+e)+c['ell'];assert q(row['typed_lag_radius'])==e and q(row['lag_upper'])==value and row['cap_pass']==(value<=tau)
   if value<=tau:lagpass.append(row['k'])
  selectedlag=published['lag_only_largest_grid_certified'];assert (selectedlag is None)==(not lagpass)
  if lagpass:assert selectedlag==published['all_lag_only_grid_rows'][min(lagpass)-20]
  if slack>0:
   # Equivalent root expression is numerically independent at512bit precision.
   continuous=(m.aa(K*K+4*slack).sqrt()-m.aa(K))/2
   assert m.aa(published['lag_only_continuous_bound_lower'])<=continuous and continuous<=m.aa(published['lag_only_continuous_bound_upper'])
  else:assert published['lag_only_continuous_bound_lower']is None and published['lag_only_continuous_bound_upper']is None
  assert published['prior_campaign_status_preserved']==prior['status'];entry={'case':name,'status':'PASS_INDEPENDENT_EXACT_NORMS_ALL_GRID_AND_PHASE_AUDIT','exact_shift_Frobenius_squared':m.pair(t2),'exact_eigenbasis_Frobenius_squared':m.pair(w2),'constants_exactly_match':True,'joint_rows_checked':81,'lag_only_rows_checked':81,'phase_implications_checked':phase_checked,'largest_joint_k':min(certified)if certified else None,'largest_lag_only_k':min(lagpass)if lagpass else None,'old_campaign_status_preserved':prior['status'],'lag_only_continuous_interval_checked':True};rows.append(entry);print(json.dumps(entry),flush=True)
 target=P/'REVIEW_RECEIPT.json';assert not target.exists();target.write_text(json.dumps({'status':'PASS_INDEPENDENT_TWO_SAVED_FACTOR_BUDGETS','rows':rows,'total_grid_rows_checked':324,'driver_freeze_sha256':SHA(P/'DRIVER_FREEZE.json'),'root_certificate_sha256':SHA(primary/'CERTIFICATE.json'),'new_estimator_calls':0,'new_raw_or_factor_copies':0,'scope':'Deterministic proof-data perturbation boxes around fixed saved tuples; direct lists/complex data and sourceH/fullfactor proofs inherited, not backend/raw-noise robustness','old_top2_Frobenius_HOLD_immutable':True,'external_review':'PENDING','physical_promotion':0},indent=2)+'\n')
if __name__=='__main__':main()
