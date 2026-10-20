"""Aggregate independent review receipts and explicit public hashes, no model execution."""
from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent
names=['CERTIFICATE.json','COUNTERMODELS.json','PREFIX_CERTIFICATE.json','REVIEW_FREEZE.json','REVIEW_SUMMARY.md','ROOT_V2_REVIEW.json','ROOT_V3_REVIEW.json','THEOREMS_REVIEW.md','compare_root_v2.py','compare_root_v3.py','review_countermodels.py','review_partial.py','review_prefix.py','finalize_review.py']
def read(n):return json.loads((P/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
primary=read('CERTIFICATE.json');counter=read('COUNTERMODELS.json');prefix=read('PREFIX_CERTIFICATE.json');active=read('ROOT_V3_REVIEW.json')
for r,cnt in [(primary,49),(counter,19),(prefix,16)]:assert len(r['controls'])==cnt and all(x['pass']for x in r['controls'])
assert len(active['checks'])==58 and all(x['pass']for x in active['checks'])
assert primary['physical_promotion']==counter['physical_promotion']==prefix['physical_promotion']==0
for rel,h in active['root_files_sha256'].items():assert sha(P.parent/rel)==h
for n,h in active['root_primary_replay_sha256'].items():assert sha(P.parent/'c17_primary_v3'/n)==sha(P.parent/'c17_replay_v3'/n)==h
result={'status':'PASS_INDEPENDENT_ACTIVE_V3_PARTIAL_FACTOR_REVIEW','proof_review':'Valid minmax lower, rational one-sided debit, prefix all321 one-sided extension, and induced-Euclidean restricted conditioning. No mathematical error found in the proposed formulas.','reviewed_active_source':'c17_partial_v3','exact_primary_controls':49,'exact_additional_countermodel_controls':19,'exact_prefix_controls':16,'active_v3_source_comparison_checks':58,'root_logical_controls':21,'original_derived_bound_pairs_exactly_equal':10,'new_prefix_scalar_pairs_exactly_equal':6,'root_certificate_and_controls_byte_identical_to_replay':True,'premises':'Existing saved per-case Gram/equation norm certificates and nominal-tail/noise source statements inherited. Upper-wrapper square consistency independently checked; no fresh raw projection or large matrix norm validation.','finite_conclusions':['Both actual sigma209 lower bounds exceed2^-24','Inherited actual sigma210 upper is strictly below2^-24, giving cutoff count209','All321 ordered saved proposals have one-sided overstatement below2^-41','Both saved-right-span restricted condition upper bounds are below1888'],'not_established':['Absolute indexed singular-value error','Proposal underestimation bound','Two-sided B1 closure','Ambient leading-spectrum conditioning','Algebraic rank209','Uniform actual-backend completeness','All original measured gates on untested histories','Independent physical freshness or six-ratio accuracy'],'countermodels_are_actual_backend_bugs':False,'new_fits':0,'new_raw_records':0,'new_factor_copies':0,'repo_or_git_mutations_by_reviewer':False,'review_relationship':'Same-team independent derivation and Fraction implementation; not external promotion authority','lane':'development — no registry entry','external_promotion_review':'PENDING','physical_promotion':0,'reviewed_root_sha256':active['root_files_sha256'],'evidence_sha256':{n:sha(P/n)for n in names}}
with (P/'FINAL_REVIEW.json').open('x')as z:json.dump(result,z,indent=2);z.write('\n')
names.append('FINAL_REVIEW.json')
manifest=''.join(sha(P/n)+'  '+n+'\n'for n in sorted(names))
with (P/'VERIFICATION_HASH_MANIFEST.sha256').open('x')as z:z.write(manifest)
for line in manifest.splitlines():
 h,n=line.split('  ',1);assert sha(P/n)==h
print(json.dumps({'status':result['status'],'public_files_in_manifest':len(names),'final_review_sha256':sha(P/'FINAL_REVIEW.json'),'hash_manifest_sha256':sha(P/'VERIFICATION_HASH_MANIFEST.sha256')}))
