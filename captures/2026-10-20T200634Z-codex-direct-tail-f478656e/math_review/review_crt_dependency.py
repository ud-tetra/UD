"""Distinct two-Gram CRT dependency review, scalar proof only; no matrix rerun."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,math,gzip
P=Path(__file__).resolve().parent;W=P.parent;R=W/'ud-repo'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def f(x):return F(int(x[0]),int(x[1]))
def prime(n):return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))
checks=[]
def ck(n,b):
 assert b,n
 checks.append({'id':n,'pass':True})
audit=W/'c19_matrix_review';freeze=read(audit/'FREEZE.json');cert=read(W/'c19_review_primary/CERTIFICATE.json')
for n,h in freeze['files'].items():ck('audit_source_pin_'+n,sha(audit/n)==h)
for row in read(audit/'SOURCE_BINDINGS.json')['pins']:ck('audit_repository_pin_'+row['path'],sha(R/row['path'])==row['sha256'])
ck('audit_freeze_binding',cert['freeze_sha256']==sha(audit/'FREEZE.json'))
ck('audit_source_bindings_binding',cert['source_bindings_sha256']==sha(audit/'SOURCE_BINDINGS.json'))
controls=read(W/'c19_review_controls/CONTROLS.json')
ck('audit23_controls_pass',len(controls['rows'])==23 and all(x['pass']for x in controls['rows']))
for row in cert['rows']:
 case=row['case'];mine=read(P/('BLOCK_REVIEW.json'if case.endswith('block')else'ROTATING_REVIEW.json'));d=W/'c19_primary'/case;payload=json.loads(gzip.decompress((d/'TAIL_WITNESS.json.gz').read_bytes()));root=read(d/'CERTIFICATE.json')
 ck(case+'_audit_both_matrices_pass',row['status']=='PASS_ALL_ENTRY_TAIL_E_H_CRT_AND_SCALAR_ENCLOSURES')
 ck(case+'_same_witness_audited',row['witness_compressed_sha256']==sha(d/'TAIL_WITNESS.json.gz')==root['new_witness_sha256'])
 ck(case+'_same_original_N_identity',row['canonical_N_payload_sha256']==payload['N_integer_bytes_sha256']==root['N_integer_bytes_sha256'])
 ck(case+'_same_saved_tail_factor',row['source_SVD_META_sha256']==payload['source_SVD_META_sha256'])
 ck(case+'_same_independent_denominator',row['independent_tail_denominator_bits']==payload['V_denominator_bits'])
 sc=row['scalars']
 for x,y in [('exact_V_gram_defect_F_squared','defect_F_squared'),('exact_tail_output_gram_F_squared','output_Gram_F_squared'),('etaV_upper','minimal180bit_eta_upper'),('tail_output_norm_upper','minimal180bit_output_norm_upper')]:ck(case+'_verified_scalar_'+x,f(sc[x])==f(mine[y]))
 ck(case+'_same_direct_tail',f(sc['tail_sigma210_upper'])==f(mine['independent_bounds']['direct_tail_upper']))
 terms=row['difference_bound_terms'];n=terms['columns_N'];m=terms['rows_N'];V=int(terms['V_integer_max_abs']);N=int(terms['N_max_abs']);scale=int(terms['identity_integer_scale']);ME=int(terms['saved_E_max_abs']);MH=int(terms['saved_H_max_abs']);bV=row['independent_tail_denominator_bits']
 ES=[n*V*V,scale,ME];HS=[m*(n*N*V)**2,MH];BE=sum(ES);BH=sum(HS);B=max(BE,BH)
 ck(case+'_actual_dimensions_for_bounds',n==321 and m==8191 and row['entries_per_matrix']==112*112)
 ck(case+'_integer_identity_scale',scale==2**(2*bV))
 ck(case+'_E_full_difference_bound',ES==list(map(int,row['E_difference_bound_summands'])) and BE==int(row['E_difference_bound']))
 ck(case+'_H_full_difference_bound',HS==list(map(int,row['H_difference_bound_summands'])) and BH==int(row['H_difference_bound']))
 ck(case+'_common_max_bound',B==int(row['common_difference_bound']))
 entries=row['all_prime_residue_checks'];ps=[x['prime']for x in entries];prod=math.prod(ps)
 ck(case+'_distinct_proved_small_primes',len(ps)==len(set(ps))==11 and all(prime(p)and p<2**24 for p in ps))
 ck(case+'_CRT_product_exact',prod==int(row['CRT_product']))
 ck(case+'_CRT_product_sufficient',prod>2*B>=0 and row['CRT_product_gt_twice_common_bound'])
 ck(case+'_shortest_prefix_stop',math.prod(ps[:-1])<=2*B)
 for j,x in enumerate(entries):
  p=x['prime'];ck(case+'_prime'+str(j)+'_first_product_safe',x['N_V_and_V_Gram_dot_inner']==n and int(x['N_V_and_V_Gram_dot_max'])==n*(p-1)**2<2**63)
  ck(case+'_prime'+str(j)+'_second_product_safe',x['W_Gram_dot_inner']==m and int(x['W_Gram_dot_max'])==m*(p-1)**2<2**63)
  ck(case+'_prime'+str(j)+'_identity_scale',x['modular_identity_scale']==pow(2,2*bV,p))
  for label in ['E','H']:
   e=x[label];ck(case+'_prime'+str(j)+'_all12544_'+label,e['all_entries_match'] and e['matching_entries']==e['entry_count']==112*112 and e['computed_residue_int64le_sha256']==e['saved_residue_int64le_sha256'])
ck('scope_zero_and_inherited',cert['independent_raw_projection_claimed']is False and cert['prefix_PR286_norm_proofs']=='INHERITED_NOT_RECOMPUTED' and cert['new_estimator_calls']==cert['new_raw_records']==cert['new_factor_or_matrix_copies']==cert['physical_promotion']==0 and cert['same_team_review'] and cert['external_review']=='PENDING')
result={'status':'PASS_DISTINCT_TWO_GRAM_CRT_DEPENDENCY_BINDING_AND_SCALAR_PROOF','checks':checks,'check_count':len(checks),'dependency_sha256':{str(p.relative_to(W)):sha(p)for p in [audit/'FREEZE.json',audit/'PROTOCOL.md',audit/'audit.py',audit/'controls.py',audit/'SOURCE_BINDINGS.json',W/'c19_review_primary/CERTIFICATE.json',W/'c19_review_controls/CONTROLS.json']},'matrix_audit_certificate_sha256':sha(W/'c19_review_primary/CERTIFICATE.json'),'matrix_products_or_modular_products_rerun_by_this_reviewer':False,'dependency_proof_assessment':'Sound full integer BE/BH bounds, complete all-entry congruences at distinct proved primes, and product>2*max(BE,BH) imply both exact identities. The separate dimension-specific int64 overflow bounds are sufficient.','source_raw_projection_and_retained_prefix_proofs_inherited':True,'new_fits':0,'external_review':'PENDING','physical_promotion':0}
with(P/'CRT_DEPENDENCY_REVIEW.json').open('x')as z:json.dump(result,z,indent=2);z.write('\n')
print(json.dumps({'status':result['status'],'checks':len(checks)}))
