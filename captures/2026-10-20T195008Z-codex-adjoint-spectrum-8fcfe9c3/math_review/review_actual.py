"""Independent norm-square/scalar review of supplied adjoint payload; no factors/fits."""
from pathlib import Path
from fractions import Fraction as F
import argparse,gzip,hashlib,json
from scalar_theorem import derive
P=Path(__file__).resolve().parent;W=P.parent;R=W/'ud-repo'
BASE=Path('captures/2026-10-20T183427Z-codex-maximal-noise-e5831029')
PARTIAL=Path('captures/2026-10-20T192205Z-codex-partial-factor-ae052f03/primary/CERTIFICATE.json')
BACKEND=Path('captures/2026-10-20T190406Z-codex-backend-contract-a14abe64/primary/CERTIFICATE.json')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def f(x):return F(int(x[0]),int(x[1]))
def pair(x):return [str(x.numerator),str(x.denominator)]
def run(case,out):
 checks=[]
 def ck(n,b):
  assert b,n
  checks.append({'id':n,'pass':True})
 freeze=read(W/'c18_adjoint/FREEZE.json')
 for n,h in freeze['code'].items():ck('root_source_pin_'+n,sha(W/'c18_adjoint'/n)==h)
 for n,h in freeze['sources'].items():ck('repository_pin_'+n,sha(R/n)==h['sha256'] and (R/n).stat().st_size==h['size_bytes'])
 for n,h in read(P/'THEOREM_FREEZE.json')['proof_and_scalar_code_sha256'].items():ck('independent_prefrozen_pin_'+n,sha(P/n)==h)
 d=W/'c18_primary'/case;cert=read(d/'CERTIFICATE.json');reconstruction=read(d/'RECONSTRUCTION.json')
 raw=gzip.decompress((d/'ADJOINT_WITNESS.json.gz').read_bytes());payload=json.loads(raw)
 ck('payload_canonical_bytes',json.dumps(payload,sort_keys=True,separators=(',',':')).encode()==raw)
 ck('payload_hash',hashlib.sha256(raw).hexdigest()==cert['canonical_payload_sha256'])
 ck('gzip_hash',sha(d/'ADJOINT_WITNESS.json.gz')==cert['witness_sha256'])
 ck('certificate_freeze_hash',cert['freeze_sha256']==sha(W/'c18_adjoint/FREEZE.json'))
 ck('case_identity',payload['case']==cert['case']==reconstruction['case']==case)
 D=[[int(x)for x in row]for row in payload['integer_numerators']]
 ck('all67089_payload_entries_shape',payload['shape']==[321,209] and len(D)==321 and all(len(x)==209 for x in D))
 bits=int(payload['residual_denominator_bits'])
 ck('residual_denominator_recipe',bits==max(55+int(payload['U_denominator_bits']),int(payload['V_denominator_bits'])+int(payload['S_denominator_bits'])) and payload['Z_denominator_bits']==55)
 square=F(sum(sum(x*x for x in row) for row in D),2**(2*bits));g=f(payload['norm_upper']);step=F(1,2**180)
 ck('supplied_allentry_norm_square_matches_payload',square==f(payload['exact_Frobenius_squared']))
 ck('supplied_norm_square_matches_certificate',square==f(cert['new_exact_adjoint_norm_squared']))
 ck('wrapper_matches_certificate',g==f(cert['new_exact_adjoint_norm_upper']))
 ck('wrapper_nonnegative_180dyadic',g>=0 and (g/step).denominator==1)
 ck('wrapper_upper_proven_by_squaring',g*g>=square)
 ck('wrapper_minimal_180dyadic',g==0 and square==0 or g>0 and (g-step)**2<square)
 old=read(R/BASE/'primary'/case/'CERTIFICATE.json');m=old['row']['measured']
 a,b,forward=[f(m[k])for k in ['etaU','etaV','xi']]
 for val,key in [(a,'left_Gram_F'),(b,'right_Gram_F'),(forward,'singular_equation_F')]:ck('inherited_square_wrapper_'+key,val>=0 and val*val>=f(m['exact_squared'][key]))
 oldpartial=next(x for x in read(R/PARTIAL)['records']if x['case']==case)
 backend=read(R/BACKEND);source_lower=f(backend['data_singular_enclosures']['s209_lower']);tail=f(backend['data_singular_enclosures']['s210_upper'])
 s1=f(oldpartial['saved_s1']);sq=f(oldpartial['saved_s209']);nextp=f(oldpartial['saved_s210'])
 for k,v in [('inherited_forward_norm_upper',forward),('inherited_left_Gram_upper',a),('inherited_right_Gram_upper',b),('inherited_source_tail_upper',tail),('saved_s1',s1),('saved_s209',sq),('saved_s210',nextp)]:ck('certificate_source_scalar_'+k,f(cert[k])==v)
 v=derive(a,b,forward,g,s1,sq,tail,nextp)
 ck('strict_leading_block_match',v['status']=='STRICT_LEADING_BLOCK_MATCH')
 expected={'compression_upper':v['compression'],'offdiagonal_upper':v['offdiagonal'],'retained_abs_error_upper':v['retained_abs_error'],'all321_abs_error_upper':v['all_abs_error'],'matching_gap':v['gap_margin'],'ambient_sigma1_upper':v['actual_s1_upper'],'ambient_sigma209_lower':v['actual_sq_lower'],'ambient_leading_condition_upper':v['ambient_leading_condition'],'qth_proposal_minus_original_floor_lower':sq-source_lower+F(1,2**41),'sufficient_adjoint_upper_for_retained_2^-41':(F(1,2**41)-v['compression'])*(1-a)}
 ck('all10_derived_bound_fields_present',set(cert['bounds'])==set(expected))
 for k,x in expected.items():ck('independent_exact_bound_'+k,f(cert['bounds'][k])==x)
 gates={'strict_leading_block_matching':v['gap_margin']>0,'retained209_absolute_error_below_2^-41':v['retained_abs_error']<F(1,2**41),'all321_absolute_error_below_2^-25':v['all_abs_error']<F(1,2**25),'ambient_leading_condition_below_reporting1888':v['ambient_leading_condition']<1888,'original_source_floor_for_actual_proposal':sq>=source_lower-F(1,2**41)}
 ck('all5_gates_independently_true',gates==cert['gates'] and all(gates.values()))
 ck('source_cutoff_strict_actual_count209',tail<F(1,2**24)<v['actual_sq_lower'])
 ck('full2neg41_not_established_by_this_envelope',v['all_abs_error']>=F(1,2**41) and cert['all321_abs_below_2^-41_established']is False)
 ck('measured_adjoint_within_prefrozen_sufficient_budget',g<=expected['sufficient_adjoint_upper_for_retained_2^-41'])
 saved=read(R/BASE/'campaign/cases'/case/'results'/case/'RUN.json')
 ck('original_raw_identity_matches_reconstruction',reconstruction['record_sha256']==saved['record_sha256']==old['row']['record_sha256'])
 ck('original_projection_identity_matches_reconstruction',reconstruction['projection']==saved['projection'])
 ck('original_integer_projection_identity_matches_payload',payload['N_integer_bytes_sha256']==saved['projection']['integer_bytes_sha256'])
 ck('numeric_witness_identity_set_matches_payload',payload['source_numeric_witnesses']==saved['numeric_witnesses'])
 ck('baseline_identity_bound',reconstruction['baseline_sha256']==freeze['baseline_sha256'])
 ck('scope_zero_and_open',cert['new_estimator_calls']==cert['new_record_identities']==cert['new_factor_archive_copies']==cert['physical_promotion']==0 and cert['all_input_backend_conformance']=='OPEN' and not cert['forward_and_Gram_norms_recomputed'] and cert['external_promotion_review']=='PENDING')
 result={'case':case,'status':'PASS_INDEPENDENT_SUPPLIED_ADJOINT_NORM_AND_SCALAR_REVIEW','checks':checks,'check_count':len(checks),'supplied_payload_entries_normsummed':321*209,'norm_square':pair(square),'minimal_180dyadic_norm_upper':pair(g),'independent_bounds':{k:pair(x)for k,x in expected.items()},'source_files_sha256':{str(p.relative_to(W)):sha(p)for p in [d/'CERTIFICATE.json',d/'ADJOINT_WITNESS.json.gz',d/'RECONSTRUCTION.json',W/'c18_adjoint/run.py',W/'c18_adjoint/THEOREM.md',W/'c18_adjoint/FREEZE.json']},'matrix_product_numerators_independently_rederived_here':False,'matrix_identity_audit_scope':'Separate deterministic all-entry modular/CRT audit, not this norm-square/scalar review','inherited_original_forward_Gram_and_source_premises':True,'new_fits':0,'new_raw_records':0,'new_factor_copies':0,'actual_all_input_backend_conformance':'OPEN','external_promotion_review':'PENDING','physical_promotion':0}
 with out.open('x')as z:json.dump(result,z,indent=2);z.write('\n')
 print(json.dumps({'status':result['status'],'case':case,'checks':len(checks),'g':float(g),'retained_abs':float(v['retained_abs_error']),'all_abs':float(v['all_abs_error']),'ambient_leading_condition':float(v['ambient_leading_condition'])}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--case',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();run(a.case,a.out)
