#!/usr/bin/env python3
"""Independent source/crosswalk inventory audit. No raw data, imports or URIs executed.

This checks the request package, not calibration truth or independent authority.
The prior task outcomes and packet content were known when this logic was frozen.
"""
import argparse
import copy
import hashlib
import json
import pathlib
import re

ORIGINAL = 'captures/2026-10-19T215410Z-codex-phase-run-calibration-43cadbae/calibration/TEMPLATE_PREFLIGHT_HOLD.json'
SOURCE_HASH = 'f3afc1218f3aa5ffda4f9fe38f36652132928ac664b4ad8cf55688ba364da2a0'
MODEL_ROLES = dict(zip([
    'family','link_amplitude','equations_parameters_domains_units','state_action_readout_map',
    'acquisition_configuration','preparation_initial_state_and_uncertainty','drive_feedback_loss_history',
    'energy_source_work_and_model_discrepancy','alternative_equations_parameters',
    'alternative_physical_justification','frozen_fit_solver_bounds_tiebreak','comparison_design',
    'fresh_validation_source','independent_unseen_lineage','heldout_scoring_and_error_allocation',
    'score_observable','selection_margin_V','margin_rationale_before_new_fit',
    'fresh_validation_calibration_and_error_budget','state_estimation_and_model_prediction_error_budget'
], ['R08','R08','R08','R09','R02','R09','R10','R10','R11','R11','R12','R12',
    'R13','R13','R12','R12','R12','R12','R13','R09']))
COMBINED = {
    'drive_feedback_loss_history': {('R10','feedback_loss_history')},
    'energy_source_work_and_model_discrepancy': {('R10','model_discrepancy')},
    'state_estimation_and_model_prediction_error_budget': {
        ('R07','prediction_solver_error'),('R10','model_discrepancy'),('R12','error_allocation')},
}

def audit(d, original):
    errors = []
    def require(ok, code):
        if not ok: errors.append(code)
    profile, cross, receipt = (d[k] for k in ['RETURN_PROFILE.json','BLOCKER_RETURN_CROSSWALK.json','EXTERNAL_RETURN_RECEIPT_TEMPLATE.json'])
    artifacts = {a['id']: a for a in profile['artifacts']}
    require(len(profile['artifacts']) == 14 and set(artifacts) == {f'R{i:02d}' for i in range(1,15)}, 'role_inventory')
    es = cross['entries']
    require(len(original) == 128 and [e['original_blocker'] for e in es] == original, 'exact_ordered_128')
    require(len({e['original_path'] for e in es}) == 128, 'unique_128_paths')
    for a in artifacts.values():
        require(a['received'] is False and a['content_verified'] is False and a['actual_return_sha256'] is None, 'no_actual_return:'+a['id'])
    for e in es:
        p = e['original_path']; leaf=p.rsplit('.',1)[-1]; aid=e['requested_artifact_id']
        require(e['original_blocker'] == p+':UNSUPPLIED', 'path_suffix:'+p)
        match=re.search(r'amplitude_channels\[(\d+)\]',p)
        if match:
            expected='R03'; require(e['actual_channel_if_applicable']==int(match[1])+1,'channel:'+p)
        elif '.timebase.' in p: expected='R04'
        elif '.anti_alias.' in p: expected='R05'
        elif '.joint_error.' in p: expected='R06'
        elif '.validated_computation.' in p: expected='R07'
        elif '.physical_model_comparison.' in p: expected=MODEL_ROLES.get(leaf)
        elif leaf=='trusted_evidence_review': expected='R14'
        else: expected='R01'
        require(aid==expected,'source_category_role:'+p)
        a=artifacts.get(aid,{})
        require(e['requested_path']==a.get('requested_path') and e['requested_section'] in a.get('required_sections',[]),'role_section:'+p)
        require(e['content_review_status']=='UNSUPPLIED_UNVERIFIED' and e['qualification_closed'] is False,'unqualified:'+p)
        route='COMMON_OR_OTHER_EVIDENCE'
        if '.joint_error.' in p:
            route=('DETERMINISTIC_SIMULTANEOUS_ENCLOSURE_ONLY' if leaf=='deterministic_proof' else
                   'JUSTIFIED_STATISTICAL_SIMULTANEOUS_COVERAGE_ONLY' if leaf in ['coverage_fraction','population_and_dependence','simultaneous_coverage_proof'] else 'BOTH_JOINT_ROUTES')
        require(e['route_applicability']==route,'route:'+p)
        refs={(x['artifact_id'],x['section']) for x in e['additional_requested_sections']}
        require(COMBINED.get(leaf,set()) <= refs, 'combined_reference:'+p)
        for rid,section in refs: require(rid in artifacts and section in artifacts[rid]['required_sections'],'secondary_section:'+p)
    require(cross['original_blocker_count']==128 and cross['candidate_v0_2_null_leaf_count']==170,'distinct_inventories')
    require(cross['null_leaves_are_independent_blockers'] is False and cross['original_128_paths_are_independent_gates'] is False and profile['original_128_paths_are_independent_gates'] is False,'not_independent_gates')
    for obj in [profile,cross,receipt]:
        require(obj['physical_promotion']==0 and obj['qualification_blockers_closed']==0,'no_promotion')
    require(profile['external_review']=='PENDING' and not any(profile[k] for k in ['raw_access_authorized','hardware_operation_authorized','outreach_sent']),'no_authority')
    for k in ['source_identity','analysis_lane','reviewer_identity','reviewer_independence_and_conflicts','calibration_authority_acceptance','review_date_UTC','review_commands_versions_logs','all_outcomes_and_HOLDs_retained','limitations','attributable_verdict','custodian_ruling']:
        require(receipt[k] is None,'blank_receipt:'+k)
    require(receipt['status']=='BLANK_NOT_A_REVIEW' and receipt['raw_access_authorized_by_this_template'] is False,'blank_status')
    require([a['id'] for a in receipt['reviewed_artifacts']]==[f'R{i:02d}' for i in range(1,14)],'receipt_no_self_review')
    for a in receipt['reviewed_artifacts']:
        require(all(v is None for k,v in a.items() if k!='id'),'blank_artifact_receipt:'+a['id'])
    require(receipt['review_return_artifact']['self_hash_required'] is False and receipt['review_return_artifact']['reviewer_independent_review_of_own_statement_required'] is False,'no_recursive_self_hash')
    examples=d['EXAMPLES.json']
    require(examples['examples_are_actual_evidence'] is False and examples['physical_promotion']==0,'examples_not_evidence')
    for e in examples['examples']: require(e['physical_promotion']==0 and e['raw_access_authorized'] is False,'example_no_authority:'+e['id'])
    return sorted(set(errors))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--packet',required=True);args=ap.parse_args()
    repo=pathlib.Path(args.repo);packet=pathlib.Path(args.packet)
    d={p.name:json.loads(p.read_text()) for p in packet.glob('*.json') if p.name in ['RETURN_PROFILE.json','BLOCKER_RETURN_CROSSWALK.json','EXTERNAL_RETURN_RECEIPT_TEMPLATE.json','SOURCE_BINDINGS.json','EXAMPLES.json']}
    raw=(repo/ORIGINAL).read_bytes();original=json.loads(raw)['blocking_metadata']
    source_errors=[]
    if hashlib.sha256(raw).hexdigest()!=SOURCE_HASH:source_errors.append('original_source_hash')
    for x in d['SOURCE_BINDINGS.json']['inputs']:
        b=(repo/x['repository_path']).read_bytes()
        if len(b)!=x['bytes'] or hashlib.sha256(b).hexdigest()!=x['sha256']:source_errors.append(x['role'])
    base_errors=audit(d,original)
    mutations=[]
    def test(name,change,expected_prefix):
        m=copy.deepcopy(d);change(m);errs=audit(m,original)
        mutations.append({'id':name,'rejected':any(e.startswith(expected_prefix) for e in errs),'diagnostics':errs})
    test('missing_path',lambda m:m['BLOCKER_RETURN_CROSSWALK.json']['entries'].pop(),'exact_ordered_128')
    test('duplicate_path',lambda m:m['BLOCKER_RETURN_CROSSWALK.json']['entries'].__setitem__(1,copy.deepcopy(m['BLOCKER_RETURN_CROSSWALK.json']['entries'][0])),'unique_128_paths')
    test('wrong_channel',lambda m:m['BLOCKER_RETURN_CROSSWALK.json']['entries'][1].__setitem__('actual_channel_if_applicable',10),'channel:')
    test('wrong_role',lambda m:m['BLOCKER_RETURN_CROSSWALK.json']['entries'][1].__setitem__('requested_artifact_id','R08'),'source_category_role:')
    test('wrong_section',lambda m:m['BLOCKER_RETURN_CROSSWALK.json']['entries'][0].__setitem__('requested_section','absent'),'role_section:')
    test('both_proofs_required',lambda m:next(e for e in m['BLOCKER_RETURN_CROSSWALK.json']['entries'] if e['original_path'].endswith('.deterministic_proof')).__setitem__('route_applicability','BOTH_JOINT_ROUTES'),'route:')
    test('premature_content_verification',lambda m:m['RETURN_PROFILE.json']['artifacts'][0].__setitem__('content_verified',True),'no_actual_return:')
    test('manufactured_review_identity',lambda m:m['EXTERNAL_RETURN_RECEIPT_TEMPLATE.json'].__setitem__('reviewer_identity','UNAUTHENTICATED_FIXTURE'),'blank_receipt:')
    test('physical_promotion',lambda m:m['RETURN_PROFILE.json'].__setitem__('physical_promotion',1),'no_promotion')
    test('missing_prediction_crossreference',lambda m:next(e for e in m['BLOCKER_RETURN_CROSSWALK.json']['entries'] if e['original_path'].endswith('.state_estimation_and_model_prediction_error_budget')).__setitem__('additional_requested_sections',[]),'combined_reference:')
    result={'artifact_type':'SEPARATE_SAME_TEAM_REQUEST_INVENTORY_AUDIT_NOT_EVIDENCE_CERTIFICATE','source_binding_count':len(d['SOURCE_BINDINGS.json']['inputs']),'source_hash_failures':source_errors,'exact_original_path_count':len(original),'base_errors':base_errors,'negative_inventory_controls':mutations,'passed':not source_errors and not base_errors and all(m['rejected'] for m in mutations),'interpretation':'Request inventory and null-status checks only. Controls are mutated metadata, not actual evidence or scientific estimator tests.','actual_evidence_received':False,'qualification_blockers_closed':0,'physical_promotion':0,'external_review':'PENDING'}
    print(json.dumps(result,indent=2,sort_keys=True));return 0 if result['passed'] else 1

if __name__=='__main__':raise SystemExit(main())
