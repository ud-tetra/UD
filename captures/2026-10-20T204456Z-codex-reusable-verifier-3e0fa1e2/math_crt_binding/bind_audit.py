"""Independent scalar CRT-bound/identity binding; no modular matrix products."""
from pathlib import Path
from fractions import Fraction as F
import gzip,hashlib,json,math
import numpy as np
P=Path(__file__).resolve().parent;W=P.parent;AUD=W/'c20_matrix_review';OLD=W/'c20_math_review'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def frac(x):return F(int(x[0]),int(x[1]))
def isprime(p):return p>=2 and all(p%d for d in range(2,math.isqrt(p)+1))
def own_prefix(count):
 result=[];p=2**24-1
 while len(result)<count:
  if isprime(p):result.append(p)
  p-=1
 return result

def bits_and_max(arrays):
 bits=0;largest=0.0
 for a in arrays:
  assert a.dtype==np.float64 and np.isfinite(a).all()
  bits=max(bits,max(float(x).as_integer_ratio()[1].bit_length()-1 for x in a.flat))
  largest=max(largest,abs(float(a.min())),abs(float(a.max())))
 value=F.from_float(largest)*2**bits
 assert value.denominator==1
 return bits,value.numerator

def run():
 checks=[]
 def ck(n,b):
  assert b,n
  checks.append({'id':n,'pass':True})
 freeze=read(AUD/'FREEZE.json');interface=read(AUD/'SOURCE_INTERFACE.json');seal=read(AUD/'FINAL_REVIEW_RECEIPT.json');manifest=read(AUD/'FINAL_REVIEW_MANIFEST.json')
 for name,h in freeze['files'].items():ck('audit_frozen_source_'+name,sha(AUD/name)==h)
 dirs={'review_source':AUD,'review_primary':W/'c20_review_primary','review_controls':W/'c20_review_controls'}
 for row in manifest['files']:
  path=dirs[row['bundle_label']]/row['path_within_directory'];ck('audit_manifest_'+row['bundle_label']+'_'+row['path_within_directory'],sha(path)==row['sha256']and path.stat().st_size==row['size_bytes'])
 ck('final_seal_source_freeze',seal['source_freeze_sha256']==sha(AUD/'FREEZE.json'))
 ck('final_seal_source_interface',seal['source_interface_sha256']==sha(AUD/'SOURCE_INTERFACE.json'))
 for key,name in [('producer_protocol_sha256','PROTOCOL.json'),('producer_seal_sha256','SEAL.json'),('producer_source_sha256','verifier.py')]:ck('active_producer_binding_'+key,interface[key]==sha(W/'c20_verifier'/name))
 ck('audit_contract_is_active_protocol',sha(AUD/'PROFILE.json')==interface['producer_protocol_sha256'])
 controls=read(W/'c20_review_controls/CONTROLS.json');ck('all31_frozen_controls_pass',len(controls['rows'])==31 and all(x['pass']for x in controls['rows'])and seal['controls_sha256']==sha(W/'c20_review_controls/CONTROLS.json'))
 counts=[];all_entries=all_comparisons=0;ps11=own_prefix(11)
 for case,label in [('boundary_pair_block','block'),('boundary_pair_rotating','rotating')]:
  reportpath=W/'c20_review_primary'/case/'CERTIFICATE.json';report=read(reportpath);prod=W/'c20_primary_v1_1'/case;producer=read(prod/'CERTIFICATE.json');own=read(OLD/('BLOCK_REVIEW_v1_1.json'if label=='block'else'ROTATING_REVIEW_v1_1.json'));mp=W/('c20_block_manifest.json'if label=='block'else'c20_rotating_manifest.json');spec=read(mp)
  ck(case+'_complete_audit_pass',report['status']=='PASS_ALL_SIX_EXACT_CRT_AND_FRESH_SCALAR_CERTIFICATE')
  ck(case+'_audit_bound_to_our_active_scalar_review',report['producer_certificate_sha256']==sha(prod/'CERTIFICATE.json')and report['witness_sha256']==sha(prod/'WITNESS.json.gz')and own['source_sha256'][str((prod/'CERTIFICATE.json').relative_to(W))]==report['producer_certificate_sha256'])
  ck(case+'_explicit_manifest_identity',report['manifest_sha256']==sha(mp)==producer['manifest_sha256'])
  ck(case+'_audit_frozen_source_identity',report['audit_freeze_sha256']==sha(AUD/'FREEZE.json'))
  for row in [spec['record'],spec['svd'],*spec['left_chunks']]:ck(case+'_explicit_input_'+row['path'],sha(mp.parent/row['path'])==row['sha256'])
  N=np.load(mp.parent/spec['record']['path'],allow_pickle=False,mmap_mode='r');m,n=N.shape;x=max(abs(int(N.min())),abs(int(N.max())))
  with np.load(mp.parent/spec['svd']['path'],allow_pickle=False)as z:s=z['singular'];vt=z['right_transpose']
  sf=[F.from_float(float(x))for x in s];q=sum(x>F(1,2**24)for x in sf)
  ck(case+'_strict_saved_order_and_dimensions',sf==sorted(sf,reverse=True)and min(sf)>=0 and F(1,2**24)not in sf and 1<=q<n<=m and report['dimensions']=={'m':m,'n':n,'q':q})
  blocks=[]
  for row in spec['left_chunks']:
   with np.load(mp.parent/row['path'],allow_pickle=False)as z:blocks.append(z['basis'])
  bU,u=bits_and_max(blocks);del blocks
  bV,v=bits_and_max([vt[:q].T]);bD,d=bits_and_max([vt[q:].T]);bS,_=bits_and_max([s[:q]])
  ck(case+'_independent_all_encoding_exponents',report['exponents']=={'bN':spec['record']['dyadic_exponent'],'bU':bU,'bV':bV,'bD':bD,'bS':bS})
  witness=json.loads(gzip.decompress((prod/'WITNESS.json.gz').read_bytes()));mats=witness['matrices'];maxima={key:max(abs(int(x))for x in val['values'])for key,val in mats.items()}
  true={'M':m*x*x,'K':m*x*u,'A':m*u*u,'B':n*v*v,'E':n*d*d+2**(2*bD),'H':n*n*maxima['M']*d*d};shapes={'M':(n,n),'K':(n,q),'A':(q,q),'B':(q,q),'E':(n-q,n-q),'H':(n-q,n-q)};statcounts={}
  ck(case+'_all6_statistic_reports_present',set(report['matrix_checks'])==set(true))
  for key,t in true.items():
   row=report['matrix_checks'][key];ps=row['primes'];B=t+maxima[key];Pprod=math.prod(ps);entry_count=math.prod(shapes[key]);expected_inner=[m]if key in('M','K','A')else([n,n]if key=='H'else[n])
   ck(case+'_'+key+'_true_bound_from_fresh_input_maxima',int(row['true_entry_absolute_bound'])==t and int(row['saved_entry_max_abs'])==maxima[key] and int(row['difference_bound'])==B)
   ck(case+'_'+key+'_full_magnitude_possible',row['magnitude_possible']and maxima[key]<=t)
   ck(case+'_'+key+'_own_deterministic_prime_prefix',ps==ps11[:len(ps)]and len(ps)==len(set(ps))and all(isprime(p)and p<2**24 for p in ps))
   ck(case+'_'+key+'_sufficient_shortest_prefix_product',Pprod==int(row['CRT_product'])and Pprod>2*B and(len(ps)==1 or math.prod(ps[:-1])<=2*B))
   ck(case+'_'+key+'_all_selected_primes_checked',[z['prime']for z in row['checks']]==ps)
   ck(case+'_'+key+'_exact_crt_status',row['status']=='PASS_EXACT_ALL_ENTRY_CRT')
   if key=='H':ck(case+'_H_non_circular_M_dependency',row['bound_dependency']=='M exact CRT identity required'and report['matrix_checks']['M']['status']=='PASS_EXACT_ALL_ENTRY_CRT')
   for i,z in enumerate(row['checks']):
    p=z['prime'];ck(case+'_'+key+'_prime'+str(i)+'_every_entry_matches',z['entries']==z['matching_entries']==entry_count and z['all_entries_match']and z['computed_residue_sha256']==z['supplied_residue_sha256'])
    ck(case+'_'+key+'_prime'+str(i)+'_full_dot_overflow_guards',z['dot_inner_lengths']==expected_inner and list(map(int,z['maximum_int64_dot_sums']))==[length*(p-1)**2 for length in expected_inner]and all(length*(p-1)**2<2**63 for length in expected_inner))
   all_entries+=entry_count;all_comparisons+=entry_count*len(ps);statcounts[key]={'entries':entry_count,'primes':len(ps),'comparisons':entry_count*len(ps)}
  scalar=report['scalar_checks']
  for key,val in own['independent_exact_norms'].items():ck(case+'_fresh_exact_norm_'+key,frac(scalar['exact'][key])==frac(val))
  for key,val in own['independent_metrics'].items():ck(case+'_minimal_metric_'+key,frac(scalar['metrics'][key])==frac(val))
  for key,val in own['independent_bounds'].items():ck(case+'_derived_bound_'+key,frac(scalar['bounds'][key])==frac(val))
  ck(case+'_all8_gates_and_finite_status',scalar['gates']==producer['gates']and all(scalar['gates'].values())and scalar['independently_derived_status']=='CERTIFIED_FINITE_SUPPLIED_RECORD'and scalar['minimal180bit_root_bounds_verified'])
  ck(case+'_freshness_and_scoped_flags',report['prior_certificate_mathematical_premises']==report['new_estimator_calls']==report['new_raw_records']==report['new_factor_or_matrix_copies']==report['physical_promotion']==0 and report['same_team_review']and report['external_review']=='PENDING')
  summary=next(z for z in seal['rows']if z['bundle_label']==case);ck(case+'_final_audit_seal_binding',summary['audit_certificate_sha256']==sha(reportpath)and summary['producer_certificate_sha256']==sha(prod/'CERTIFICATE.json')and summary['producer_witness_sha256']==sha(prod/'WITNESS.json.gz'))
  counts.append({'case':case,'statistics':statcounts})
 ck('total565160_distinct_matrix_entries',all_entries==565160==seal['total_exact_full_matrix_entries'])
 ck('total3441361_full_modular_comparisons',all_comparisons==3441361==seal['total_modular_entry_comparisons'])
 ck('allinput_and_physical_scope_preserved',seal['all_input_backend_conformance']=='OPEN'and seal['physical_promotion']==seal['prior_certificate_mathematical_premises']==0 and seal['same_team_review']and seal['external_review']=='PENDING'and'not prove an atomic snapshot'in seal['stable_input_premise'])
 prior=OLD/'FINAL_REVIEW.json';ck('prior_scoped_pending_receipt_preserved',sha(prior)=='92696cf3d53f08279da444dcf16f37b78cc7d00d7652e9e967d7752418f5e915'and read(prior)['actual_matrix_product_identity_audit'].startswith('PENDING_'))
 deps=[AUD/'FREEZE.json',AUD/'PROTOCOL.md',AUD/'SOURCE_INTERFACE.json',AUD/'PROFILE.json',AUD/'audit.py',AUD/'controls.py',AUD/'FINAL_REVIEW_RECEIPT.json',AUD/'FINAL_REVIEW_MANIFEST.json',W/'c20_review_controls/CONTROLS.json',W/'c20_review_primary/boundary_pair_block/CERTIFICATE.json',W/'c20_review_primary/boundary_pair_rotating/CERTIFICATE.json',prior,OLD/'BLOCK_REVIEW_v1_1.json',OLD/'ROTATING_REVIEW_v1_1.json']
 result={'status':'PASS_FINITE_SIX_MATRIX_IDENTITY_DEPENDENCY_DISCHARGED_FOR_BOTH_SUPPLIED_BUNDLES','checks':checks,'check_count':len(checks),'counts':counts,'exact_distinct_matrix_entries':all_entries,'modular_entry_comparisons':all_comparisons,'separate_audit_controls':31,'matrix_products_or_modular_products_rerun_by_this_reviewer':False,'independent_input_maxima_exponents_and_all_bound_products_checked':True,'H_verified_M_dependency_non_circular':True,'prior_scoped_pending_receipt_unchanged_sha256':sha(prior),'closure_scope':'Closes only the previously pending finite exact-product dependency for these two supplied fixed bundles. Does not modify the earlier review or establish any all-input/backend/race/whole-program guarantee.','fresh_numeric_premises':'All6 matrix identities and their fresh scalar norm/trace consequences verified; no prior certificate numerical premises','stable_input_premise':'Inputs fixed during reads/computation; endpoint hashes are not universal immutable-snapshot or modify-and-restore race proof','acquisition_projection_authenticity':'SUPPLIED_BYTES_ONLY; separate and not established','all_input_backend_conformance':'OPEN','universal_race_or_program_correctness_established':False,'external_promotion_review':'PENDING','same_team_review':True,'physical_promotion':0,'new_fits':0,'new_raw_records':0,'new_factor_or_matrix_copies':0,'source_sha256':{str(p.relative_to(W)):sha(p)for p in deps}}
 with(P/'BINDING_ADDENDUM.json').open('x')as z:json.dump(result,z,indent=2);z.write('\n')
 print(json.dumps({'status':result['status'],'checks':len(checks),'entries':all_entries,'modular_comparisons':all_comparisons}))
if __name__=='__main__':run()
