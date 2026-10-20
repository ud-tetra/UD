#!/usr/bin/env python3
"""Bind independently checked formulas and source facts to final C28 bytes."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
P=Path(__file__).resolve().parent;W=P.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_text())
root=load(W/'c28_math_v2/RESULT.json');ours=load(P/'ROOT_PROFILE_CHECKS.json');gain=load(P/'WEIGHT_GAIN_CHECKS.json');ctrl=load(P/'ROOT_CONTROLS_CHECKS.json');binding=load(W/'c28_math_v2/SOURCE_BINDINGS.json');contract=load(W/'c28_math_v2/CONDITIONAL_ERROR_CONTRACT.json')
pairs={'map_error_bound_b':'b_upper','normalized_data_error_bound':'observation_error_upper','ideal_inverse_error_upper':'ideal_error_upper','conditional_implemented_error_upper':'approximate_estimator_error_upper'}
for rootkey,ownkey in pairs.items():assert F(root['conditional_example'][rootkey])==F(ours['profile'][ownkey])
assert F(root['RMS_time_squared'])==F(11180715,8)and F(root['mean_time'])==F(4095,4)and F(root['time_variance'])==F(4096**2-1,48)
assert F(root['ideal_total_data_requirement_for_declared_tau'])==F(61,27648)*F(1,2**39)
assert root['controls_passed']==ctrl['controls_verified']==8
assert root['conditional_example']['actual_error_budget_admission']=='HOLD'and root['conditional_example']['actual_estimator_conformance']=='NOT_SUPPLIED_HOLD'
assert contract['input_evidence_status']=='UNSUPPLIED_HOLD'and all(x['evidence_receipt']is None and x['status']=='HOLD_NO_SOURCE_RECEIPT'for x in contract['error_inputs'])
assert binding['source_complex_archive_sha256']==gain['source_archive_sha256'] and binding['source_complex_JSON_sha256']==gain['complex_member_sha256']
parent=W/'ud-repo'/binding['parent_result_path'];ptheorem=W/'ud-repo'/binding['parent_theorem_path'];assert sha(parent)==binding['parent_result_sha256'] and sha(ptheorem)==binding['parent_theorem_sha256']
freeze=load(W/'c28_FINAL_FREEZE.json');assert sha(W/'c28_compute.py')==freeze['sha256']['c28_compute.py']
assert sha(W/'c28_THEOREM.md')=='946d40156db42380406f476508236beea027c734deef46680b2bc944be18106c'
files={}
for name in ['RESULT.json','SOURCE_BINDINGS.json','CONTROLS.json','CONDITIONAL_ERROR_CONTRACT.json']:
 p=W/'c28_math_v2'/name;r=W/'c28_replay'/name;assert p.read_bytes()==r.read_bytes();files[name]={'primary_sha256':sha(p),'replay_sha256':sha(r),'byte_identical':True}
out={'status':'PASS_FINAL_CONDITIONAL_MATH_SOURCE_AND_REPLAY_BINDINGS','root_checker_sha256':sha(W/'c28_compute.py'),'root_theorem_sha256':sha(W/'c28_THEOREM.md'),'scientific_output_bindings':files,'parent_conditioning_bindings':{'result_sha256':binding['parent_result_sha256'],'theorem_sha256':binding['parent_theorem_sha256']},'source_calibration_archive_sha256':gain['source_archive_sha256'],'source_calibration_complex_member_sha256':gain['complex_member_sha256'],'exact_profile_pairs_compared':4,'root_control_countermodels_checked':8,'scope':{'no_producer_execution_by_reviewer':True,'actual_input_evidence':'UNSUPPLIED_HOLD','actual_floating_estimator_conformance':'NOT_SUPPLIED_HOLD','physical_promotion':0,'external_review':'PENDING'}}
(P/'FINAL_BINDING.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checker':out['root_checker_sha256'],'theorem':out['root_theorem_sha256']}))
