#!/usr/bin/env python3
"""Bind frozen final producer outputs to distinct exact review results; no producer execution."""
from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent;W=P.parent
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text())
a=load(P/'FACTOR_RESULTS.json');b=load(W/'c26_math_v2/FACTOR_RESULTS.json');r=load(W/'c26_math_v2/RESULT.json');p=load(P/'FINAL_PAYLOAD_CHECKS.json');s=load(W/'c26_math_v2/SOURCE_BINDINGS.json');q=load(P/'CONDITION_CHECKS.json')
assert len(a['factor_rows'])==len(b['factors'])==30
for own,root in zip(a['factor_rows'],b['factors']):
 assert own['factor_coefficients_ascending']==root['coefficients_ascending']
 assert own['degree']==root['degree'] and own['nominal_rank_Q']==root['nominal_upper'] and own['augmented_rank_Q']==root['augmented_upper']
assert (r['nominal_top_rank'],r['weighted_top_rank'],r['augmented_space_dimension'])==(390,443,444)
assert (r['weighted_full_rank'],r['weighted_full_kernel'],r['common_old_new_kernel_dimension'],r['new_observation_rank_restricted_to_old_kernel'])==(1999,641,640,107)
assert r['conditioning']['practical_2029_gate']=='HOLD_NOT_CERTIFIED'
assert r['sampling']['rank']==1999 and r['sampling']['kernel']==641
assert q['strict_binary_exponents']['final_smallest_positive_singular_denominator']==10394665
assert p['check_count']==312 and p['upper_payload_count']==60
assert p['upper_archive_sha256']==s['evidence_sha256']['UPPER_WITNESSES.zip']==sha(W/'c26_work/UPPER_WITNESSES.zip')
assert p['lower_witness_sha256']==s['evidence_sha256']['LOWER_WITNESSES.json']==sha(W/'c26_work/LOWER_WITNESSES.json')
assert r['checks']['rational_membership_entries']==p['upper_membership_matrix_entries']==1590000
bindings={}
for name in ['RESULT.json','FACTOR_RESULTS.json','SOURCE_BINDINGS.json']:
 x=W/'c26_math_v2'/name;y=W/'c26_replay'/name
 assert x.read_bytes()==y.read_bytes()
 bindings[name]={'primary_sha256':sha(x),'replay_sha256':sha(y),'byte_identical':True}
result={'status':'PASS_FINAL_SOURCE_AND_SCIENTIFIC_OUTPUT_BINDINGS','root_checker_sha256':sha(W/'c26_compute.py'),'root_theorem_sha256':sha(W/'c26_THEOREM.md'),'scientific_outputs':bindings,'independent_all30_factor_profiles_agree':True,'compact_upper_memberships':60,'modular_nonzero_minors':3,'compact_membership_entries':1590000,'exact_payload_checks':312,'witness_bindings':s['evidence_sha256'],'scope':{'producer_not_executed_by_this_binding_script':True,'inherited_full_rank1893_and_channel_separation':True,'no_new_SVD_or_Hankel':True,'practical_conditioning':'HOLD','external_promotion_review':'PENDING','physical_promotion':0}}
(P/'FINAL_BINDING.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2))
