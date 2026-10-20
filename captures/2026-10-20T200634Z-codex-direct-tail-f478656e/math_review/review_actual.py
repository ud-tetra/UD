"""Independent exact two-Gram norm/scalar review; no factors or projected N loaded."""
from pathlib import Path
from fractions import Fraction as F
import argparse,gzip,hashlib,json
from scalar_reanchor import derive
P=Path(__file__).resolve().parent;W=P.parent;R=W/'ud-repo'
OLD=Path('captures/2026-10-20T195008Z-codex-adjoint-spectrum-8fcfe9c3')
SOURCE=Path('captures/2026-10-20T183427Z-codex-maximal-noise-e5831029')
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def f(x):return F(int(x[0]),int(x[1]))
def pair(x):return[str(x.numerator),str(x.denominator)]
def run(case,out):
 checks=[]
 def ck(n,b):
  assert b,n
  checks.append({'id':n,'pass':True})
 root=W/'c19_tail';freeze=read(root/'FREEZE.json')
 for n,h in freeze['code'].items():ck('root_source_pin_'+n,sha(root/n)==h)
 for n,h in freeze['sources'].items():ck('repository_pin_'+n,sha(R/n)==h['sha256'] and (R/n).stat().st_size==h['size_bytes'])
 for n,h in read(P/'THEOREM_FREEZE_v0.2.json')['proof_and_scalar_code_sha256'].items():ck('prefrozen_review_pin_'+n,sha(P/n)==h)
 d=W/'c19_primary'/case;cert=read(d/'CERTIFICATE.json');raw=gzip.decompress((d/'TAIL_WITNESS.json.gz').read_bytes());payload=json.loads(raw)
 ck('canonical_payload_bytes',json.dumps(payload,sort_keys=True,separators=(',',':')).encode()==raw)
 ck('payload_hash',hashlib.sha256(raw).hexdigest()==cert['canonical_payload_sha256'])
 ck('compressed_witness_hash',sha(d/'TAIL_WITNESS.json.gz')==cert['new_witness_sha256'])
 ck('certificate_binds_root_freeze',cert['freeze_sha256']==sha(root/'FREEZE.json'))
 ck('case_and_shape_identity',payload['case']==cert['case']==case and payload['shape']==[112,112] and payload['retained_q']==209 and payload['tail_columns']==112)
 matrices={}
 for key in ['V_gram_defect_integer_numerators','tail_output_gram_integer_numerators']:
  M=[[int(x)for x in row]for row in payload[key]]
  ck(key+'_all12544_entries_shape',len(M)==112 and all(len(row)==112 for row in M))
  ck(key+'_symmetric',all(M[i][j]==M[j][i]for i in range(112)for j in range(112)))
  matrices[key]=M
 b=int(payload['V_denominator_bits']);be=int(payload['V_gram_defect_denominator_bits']);bh=int(payload['tail_output_gram_denominator_bits'])
 ck('denominator_exponents_exact',b>=0 and be==2*b and bh==2*(55+b) and payload['Z_denominator_bits']==55)
 esq=F(sum(x*x for row in matrices['V_gram_defect_integer_numerators']for x in row),2**(2*be))
 hsq=F(sum(x*x for row in matrices['tail_output_gram_integer_numerators']for x in row),2**(2*bh))
 ck('defect_allentry_exact_F_squared',esq==f(payload['exact_V_gram_defect_F_squared']))
 ck('output_Gram_allentry_exact_F_squared',hsq==f(payload['exact_tail_output_gram_F_squared']))
 eta=f(payload['etaV_upper']);r=f(payload['tail_output_norm_upper']);step=F(1,2**180)
 for label,upper,square,power in [('eta',eta,esq,2),('outputnorm',r,hsq,4)]:
  ck(label+'_nonnegative180dyadic',upper>=0 and (upper/step).denominator==1)
  ck(label+'_correct_power_bounds_exact_sum',upper**power>=square)
  ck(label+'_minimal_180bit_ceiling',upper==0 and square==0 or upper>0 and (upper-step)**power<square)
 ck('eta_domain_full112dimensional_span',eta<1)
 ck('wrapper_pairs_match_certificate',eta==f(cert['direct_tail_eta_upper']) and r==f(cert['direct_tail_output_norm_upper']))
 old=read(R/OLD/'primary'/case/'CERTIFICATE.json')
 a,beta,forward,adjoint=[f(old[k])for k in ['inherited_left_Gram_upper','inherited_right_Gram_upper','inherited_forward_norm_upper','new_exact_adjoint_norm_upper']]
 s1=f(old['saved_s1']);sq=f(old['saved_s209']);s210=f(old['saved_s210']);tau=F(1,2**24)
 # No nominal source tail or sourceL is passed to the accuracy/cutoff function.
 answer=derive(a,beta,forward,adjoint,s1,sq,eta,r,s210,tau)
 ck('new_direct_tail_retained_matching',answer['status']=='DIRECT_TAIL_RETAINED_MATCH')
 expect={'direct_tail_upper':answer['direct_tail_upper'],'compression_upper':answer['compression_upper'],'offdiagonal_upper':answer['offdiagonal_upper'],'retained_abs_error_upper':answer['retained_abs_error_upper'],'discarded_abs_error_upper':answer['discarded_abs_error_upper'],'full321_abs_error_upper':answer['full321_abs_error_upper'],'matching_gap':answer['new_matching_gap'],'ambient_sigma209_lower':answer['ambient_sigma209_lower'],'ambient_leading_condition_upper':answer['ambient_leading_condition_upper']}
 ck('all9_derived_bound_fields_present',set(cert['bounds'])==set(expect))
 for k,v in expect.items():ck('independent_exact_bound_'+k,f(cert['bounds'][k])==v)
 for k in ['compression_upper','offdiagonal_upper','retained_abs_error_upper','ambient_leading_condition_upper']:
  ck('prior_retained_arithmetic_preserved_'+k,expect[k]==f(old['bounds'][k]))
 ck('new_matching_gap_replaces_old',expect['matching_gap']>0 and expect['matching_gap']!=f(old['bounds']['matching_gap']))
 ck('saved_s210_preserved',f(cert['saved_s210'])==s210)
 ck('prior_retained_certificate_bound',cert['prior_retained_certificate_sha256']==sha(R/OLD/'primary'/case/'CERTIFICATE.json'))
 ck('direct_tail_payload_scalar',expect['direct_tail_upper']==f(payload['tail_sigma210_upper']))
 gates={'discarded_right_factor_validated_full_rank':eta<1,'strict_matching_with_direct_tail':answer['new_matching_gap']>0,'full321_abs_error_below_2^-41':answer['full321_abs_error_upper']<F(1,2**41),'direct_tail_below_cutoff':answer['direct_tail_upper']<tau,'retained_lower_above_cutoff':answer['ambient_sigma209_lower']>tau}
 ck('all5_gates_independently_true',gates==cert['gates'] and all(gates.values()))
 ck('actual_cutoff_count209_strict',answer['strict_actual_cutoff_count209'])
 original=read(R/SOURCE/'campaign/cases'/case/'results'/case/'RUN.json')
 ck('original_projected_N_identity_bound',cert['N_integer_bytes_sha256']==payload['N_integer_bytes_sha256']==original['projection']['integer_bytes_sha256'])
 ck('source_singular_factor_file_identity_bound',payload['source_SVD_META_sha256']==original['numeric_witnesses']['SVD_META.npz'])
 ck('no_old_nominal_tail_dependency',cert['old_nominal_tail_bound_used_in_current_full321_proof']is False)
 ck('scope_zero_and_open',cert['new_raw_or_projection_reconstruction']is False and cert['new_estimator_calls']==cert['new_record_identities']==cert['new_stored_factor_copies']==cert['physical_promotion']==0 and not cert['source_retained_norms_recomputed'] and cert['all_input_backend_conformance']=='OPEN' and cert['algebraic_rank209_claimed']is False and cert['full_matrix_condition_claimed']is False and cert['external_promotion_review']=='PENDING')
 result={'case':case,'status':'PASS_INDEPENDENT_SUPPLIED_TWO_GRAM_NORMS_AND_DIRECT_REANCHOR','checks':checks,'check_count':len(checks),'supplied_entries_normsummed_per_matrix':112*112,'defect_F_squared':pair(esq),'output_Gram_F_squared':pair(hsq),'minimal180bit_eta_upper':pair(eta),'minimal180bit_output_norm_upper':pair(r),'independent_bounds':{k:pair(v)for k,v in expect.items()},'source_sha256':{str(p.relative_to(W)):sha(p)for p in [d/'CERTIFICATE.json',d/'TAIL_WITNESS.json.gz',root/'run.py',root/'THEOREM.md',root/'FREEZE.json']},'source_L_or_old_nominal_tail_passed_to_accuracy_function':False,'original_floor_gate_unchanged_and_not_reevaluated_here':True,'supplied_matrix_products_independently_recomputed_here':False,'matrix_identity_scope':'Separate all-entry deterministic modular/CRT audit required for E and H identities','retained_norms_and_projection_lineage_inherited':True,'new_fits':0,'new_raw_records':0,'new_factor_copies':0,'external_review':'PENDING','physical_promotion':0}
 with out.open('x')as z:json.dump(result,z,indent=2);z.write('\n')
 print(json.dumps({'status':result['status'],'case':case,'checks':len(checks),'eta':float(eta),'r':float(r),'tail':float(answer['direct_tail_upper']),'full321':float(answer['full321_abs_error_upper'])}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--case',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();run(a.case,a.out)
