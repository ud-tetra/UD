"""Bind distinct all-entry audit and check its scalar CRT proof, no matrix rerun."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,math,gzip
P=Path(__file__).resolve().parent;W=P.parent;R=W/'ud-repo'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def f(x):return F(int(x[0]),int(x[1]))
def prime(n):
 if n<2:return False
 return all(n%d for d in range(2,math.isqrt(n)+1))
rows=[]
def ck(n,v):
 assert v,n
 rows.append({'id':n,'pass':True})
audit=W/'c18_matrix_review';freeze=read(audit/'FREEZE.json');cert=read(W/'c18_review_primary/CERTIFICATE.json')
for n,h in freeze['files'].items():ck('audit_source_pin_'+n,sha(audit/n)==h)
ck('audit_certificate_binds_freeze',cert['freeze_sha256']==sha(audit/'FREEZE.json'))
ck('audit_certificate_binds_sources',cert['source_bindings_sha256']==sha(audit/'SOURCE_BINDINGS.json'))
for pin in read(audit/'SOURCE_BINDINGS.json')['pins']:ck('audit_repository_pin_'+pin['path'],sha(R/pin['path'])==pin['sha256'])
controls=read(W/'c18_review_controls/CONTROLS.json')
ck('audit19_synthetic_controls_pass',len(controls['rows'])==19 and all(x['pass']for x in controls['rows']))
for row in cert['rows']:
 case=row['case'];stem='block'if case.endswith('block')else'rotating';mine=read(P/('BLOCK_REVIEW.json'if stem=='block'else'ROTATING_REVIEW.json'))
 actual=W/'c18_primary'/case;w=read(actual/'CERTIFICATE.json');payload=json.loads(gzip.decompress((actual/'ADJOINT_WITNESS.json.gz').read_bytes()));reconstruction=read(actual/'RECONSTRUCTION.json')
 ck(case+'_matrix_audit_pass',row['status']=='PASS_DETERMINISTIC_ALL_ENTRY_ADJOINT_CRT_AND_EXACT_NORM')
 ck(case+'_same_witness_audited',row['witness_compressed_sha256']==sha(actual/'ADJOINT_WITNESS.json.gz')==w['witness_sha256'])
 ck(case+'_same_source_N',row['canonical_N_payload_sha256']==payload['N_integer_bytes_sha256']==reconstruction['projection']['integer_bytes_sha256'])
 ck(case+'_same_original_record',row['record_sha256']==reconstruction['record_sha256'])
 for k,pkey in [('U','U_denominator_bits'),('V','V_denominator_bits'),('S','S_denominator_bits'),('D','residual_denominator_bits')]:ck(case+'_independent_bits_'+k,row['independent_denominator_bits'][k]==payload[pkey])
 ck(case+'_same_norm_squared',f(row['norm']['exact_Frobenius_squared'])==f(mine['norm_square']))
 ck(case+'_same_norm_upper',f(row['norm']['root_norm_upper'])==f(mine['minimal_180dyadic_norm_upper']))
 terms=row['difference_bound_terms'];summands=[int(terms['inner_length'])*int(terms['N_max_abs'])*int(terms['U_integer_max_abs'])*int(terms['Ntranspose_U_integer_scale']),int(terms['V_integer_max_abs'])*int(terms['S_integer_max_abs'])*int(terms['VS_integer_scale']),int(terms['saved_D_max_abs'])]
 B=int(row['entrywise_difference_bound']);ck(case+'_full_difference_bound_summed',summands==list(map(int,row['difference_bound_summands'])) and sum(summands)==B)
 entries=row['all_prime_residue_checks'];ps=[x['prime']for x in entries];product=math.prod(ps)
 ck(case+'_six_distinct_proved_primes',len(ps)==len(set(ps))==6 and all(prime(x)and x<2**24 for x in ps))
 ck(case+'_CRT_product_exact',product==int(row['CRT_product']))
 ck(case+'_CRT_product_strictly_dominates2B',product>2*B>=0)
 ck(case+'_prefix_stops_first_sufficient_product',math.prod(ps[:-1])<=2*B)
 for j,x in enumerate(entries):
  p=x['prime'];inner=x['dot_inner_length'];bound=inner*(p-1)**2
  ck(case+'_prime'+str(j)+'_overflow_safe',inner==8191 and bound==int(x['maximum_possible_int64_dot'])<2**63 and int(x['elementwise_product_upper'])==(p-1)**2<2**63)
  ck(case+'_prime'+str(j)+'_all_entries_match',x['all_entries_match'] and x['matching_entries']==x['entry_count']==321*209 and x['computed_residue_int64le_sha256']==x['saved_residue_int64le_sha256'])
 ck(case+'_all67089_entries_audited',row['checked_matrix_entries_per_prime']==67089)
ck('scope_no_independent_source_projection',cert['independent_raw_projection_claimed']is False and cert['new_estimator_calls']==cert['new_raw_records']==cert['new_factor_or_matrix_copies']==cert['physical_promotion']==0 and cert['same_team_review'] and cert['external_review']=='PENDING')
result={'status':'PASS_DISTINCT_CRT_DEPENDENCY_BINDING_AND_SCALAR_PROOF_REVIEW','checks':rows,'check_count':len(rows),'dependency_sha256':{str(p.relative_to(W)):sha(p)for p in [audit/'FREEZE.json',audit/'PROTOCOL.md',audit/'audit.py',audit/'controls.py',audit/'SOURCE_BINDINGS.json',W/'c18_review_primary/CERTIFICATE.json',W/'c18_review_controls/CONTROLS.json']},'reviewed_dependency_certificate_sha256':sha(W/'c18_review_primary/CERTIFICATE.json'),'dependency_method':'Distinct same-team all-entry CRT audit; supplied N projection identity inherited and hash-bound','matrix_products_or_modular_products_rerun_by_this_reviewer':False,'proof_assessment':'Sound exact integer difference bound plus complete entrywise congruences at distinct primes whose product exceeds2B imply exact equality. Overflow bounds are sufficient for the int64 residue computations.','external_review':'PENDING','physical_promotion':0}
with(P/'CRT_DEPENDENCY_REVIEW.json').open('x')as z:json.dump(result,z,indent=2);z.write('\n')
print(json.dumps({'status':result['status'],'checks':len(rows)}))
