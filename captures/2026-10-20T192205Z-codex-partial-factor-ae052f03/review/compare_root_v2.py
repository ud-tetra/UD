"""Byte/pin checks and independent rational cross-comparison; no producer import."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
P=Path(__file__).resolve().parent
W=P.parent;repo=W/'ud-repo'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def f(p):return F(int(p[0]),int(p[1]))
root=W/'c17_partial_v2';freeze=read(root/'FREEZE.json');mine=read(P/'CERTIFICATE.json');theirs=read(W/'c17_primary_v2/CERTIFICATE.json')
checks=[]
def ck(k,v):
 assert v,k
 checks.append({'id':k,'pass':True})
for path,h in freeze['code'].items():ck('active_code_pin_'+path,sha(root/path)==h)
for path,v in freeze['sources'].items():
 p=repo/path;ck('source_pin_'+path,sha(p)==v['sha256'] and p.stat().st_size==v['size_bytes'])
ck('root_certificate_binds_source_freeze',theirs['source_freeze_sha256']==sha(root/'FREEZE.json'))
prior=read(repo/'captures/2026-10-20T190406Z-codex-backend-contract-a14abe64/primary/CERTIFICATE.json')
C=f(prior['source_constants']['C']);direct=read(repo/'captures/2026-10-19T222108Z-codex-uniform-phase-evidence-4a6f6bda/phase/primary/CERTIFICATE.json')
ck('C_matches_independent_earlier_source',C==f(direct['sketch']['per_62_vector_noise_multiplier_upper'])==f(freeze['inherited_noise_multiplier_upper']))
field_map={'inherited_etaU':'inherited_a','inherited_etaV':'inherited_b','inherited_equation_upper':'inherited_r','saved_s209':'saved_sq','saved_s1':'saved_s1','inherited_tail_upper':'inherited_sigma_qplus1_upper_after_perturbation'}
bound_map={'lower':'actual_sigma_q_lower','upper':'restricted_sigma_max_upper','debit':'qth_proposal_overstatement_debit_upper','condition':'restricted_condition_upper'}
for me,them in zip(mine['rows'],theirs['records']):
 name=me['case'];ck(name+'_row_identity',name==them['case'] and me['q']==them['q']==209)
 for x,y in field_map.items():ck(name+'_'+x,f(them[x])==f(me[y]))
 for x,y in bound_map.items():ck(name+'_'+x,f(them['exact_rational_bounds'][x])==f(me[y]))
 ck(name+'_inverse',f(them['exact_rational_bounds']['inverse_restriction_upper'])==1/f(me['actual_sigma_q_lower']))
 order=read(repo/'captures/2026-10-20T183427Z-codex-maximal-noise-e5831029/campaign/cases'/name/'inputs/PARENT_ORDER.json')
 source_lower=f(order['qth_sigma_lower'])-C*F(3,1<<49)
 ck(name+'_inherited_source_lower',f(them['inherited_source_lower'])==source_lower==f(prior['data_singular_enclosures']['s209_lower']))
 ck(name+'_inherited_tail',f(them['inherited_tail_upper'])==f(prior['data_singular_enclosures']['s210_upper']))
 ck(name+'_all_six_declared_consequences',all(them['gates'].values()) and len(them['gates'])==6)
 ck(name+'_report1888_only',f(me['restricted_condition_upper'])<1888)
 ck(name+'_scope_retained',them['retained_norm_certificate_is_inherited'] and not them['fresh_matrix_norm_recomputation'] and not them['ambient_condition_certified'] and not them['all_indexed_singular_values_two_sided_accuracy_certified'])
controls=read(W/'c17_primary_v2/CONTROLS.json')
ck('root_controls21_all_pass',controls['count']==21 and len(controls['rows'])==21 and all(x['pass'] for x in controls['rows']))
replay={}
for name in ['CERTIFICATE.json','CONTROLS.json']:
 a=W/'c17_primary_v2'/name;b=W/'c17_replay_v2'/name
 ck('root_replay_byte_identical_'+name,a.read_bytes()==b.read_bytes());replay[name]=sha(a)
ck('root_provenance_zero_and_open',theirs['new_estimator_calls']==theirs['new_raw_records']==theirs['new_factor_copies']==theirs['physical_promotion']==0 and theirs['uniform_backend_conformance']=='OPEN' and not theirs['two_sided_B1_closed'] and theirs['external_promotion_review']=='PENDING')
result={'status':'PASS_INDEPENDENT_ACTIVE_ROOT_V2_COMPARISON','checks':checks,'check_count':len(checks),'exact_bound_pairs_compared':10,'additional_exact_source_scalar_pairs_compared':16,'root_primary_replay_sha256':replay,'root_files_sha256':{str(p.relative_to(W)):sha(p)for p in [root/'derive.py',root/'THEOREMS.md',root/'FREEZE.json',W/'c17_primary_v2/CERTIFICATE.json',W/'c17_primary_v2/CONTROLS.json']},'imported_or_executed_producer_code':False,'new_fits':0,'physical_promotion':0}
with (P/'ROOT_V2_REVIEW.json').open('x') as z:json.dump(result,z,indent=2);z.write('\n')
print(json.dumps({'status':result['status'],'checks':len(checks),'replay_byte_identical':True}))
