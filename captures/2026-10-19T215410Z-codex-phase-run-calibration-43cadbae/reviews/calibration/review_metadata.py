"""Same-team tiny metadata review. All complete fixtures are invented syntax exercises, NOT evidence."""
import copy,hashlib,importlib.util,json,sys
from pathlib import Path
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent

def need(ok,message):
    if not ok:raise RuntimeError(message)

def digest(path):
    b=path.read_bytes();return {'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}

def invent(schema):
    # Construct only a clearly labelled metadata fixture. No URI/file/signature is created.
    if 'const' in schema:return schema['const']
    if 'enum' in schema:return next(v for v in schema['enum'] if v is not None)
    ts=schema['type'];ts=[ts] if isinstance(ts,str) else ts;t=next(v for v in ts if v!='null')
    if t=='object':return {k:invent(v) for k,v in schema['properties'].items()}
    if t=='array':return [invent(schema['items']) for _ in range(schema['minItems'])]
    if t=='integer':return schema.get('minimum',1)
    if t=='boolean':return False
    if t=='string':
        pattern=schema.get('pattern','')
        return 'a1'*32 if '{64}' in pattern else '1/1000000' if '/' in pattern else 'SYNTHETIC_REVIEW_NOT_EVIDENCE'
    raise RuntimeError('unknown fixture type')

def complete_fixture(schema):
    x=invent(schema);x['classification']='SYNTHETIC_METADATA_CONTROL';c=x['calibration']
    for i,a in enumerate(c['amplitude_channels'],1):
        a.update(channel=i,applied_gain_V_per_nominal_V='1/1',applied_offset_V='0/1',gain_interval={'lower':'999999/1000000','upper':'1000001/1000000'},offset_interval_V={'lower':'-1/1000000','upper':'1/1000000'},valid_input_range_nominal_V={'lower':'-2/1','upper':'2/1'})
    c['timebase']['rate_interval_Hz']={'lower':'1953124/1','upper':'1953126/1'}
    c['anti_alias']['declared_input_band_Hz']={'lower':'0/1','upper':'400000/1'}
    j=c['joint_error'];j.update(route='DETERMINISTIC_JOINT_ENCLOSURE',epsilon_vector_V='1/100',coverage_fraction=None,population_and_dependence=None,simultaneous_coverage_proof=None)
    m=x['physical_model_comparison'];m.update(comparison_design='RETROSPECTIVE_EXISTING_PUBLIC_ONLY',fresh_validation_source=None,independent_unseen_lineage=None,selection_margin_V='1/10')
    return x

def assert_scope(out):
    need(out['physical_promotion']==0 and out['physical_admission']=='HOLD','physical promotion escaped metadata layer')
    need(out['raw_records_opened']==0 and out['new_fits']==0 and out['actual_apparatus_records_evaluated']==0,'unexpected data/model operation')
    need(not out['calibration_evidence_content_verified'] and not out['independent_authority_verified'] and not out['heldout_independence_verified'] and not out['validated_computation_proof_verified'] and not out['physical_model_or_alternative_justification_verified'],'declared evidence falsely verified')
    need(not out['declared_input_domain_covers_actual_samples_verified'] and not out['actual_common_timing_grid_verified'] and not out['anti_alias_transfer_verified'],'calibration-domain premise falsely verified')
    need(out['native_62_channel_intake'].startswith('HOLD') and out['calibrated_physical_comparison'].startswith('HOLD'),'native or model admission escaped')

def main():
    bind=json.loads((HERE/'INPUT_BINDINGS.json').read_text());src=Path(bind['source_dir'])
    need(digest(src/bind['freeze_path'])==bind['source_freeze'],'constructor freeze changed')
    sourcefreeze=json.loads((src/bind['freeze_path']).read_text())
    for row in sourcefreeze['files']:need(digest(src/row['path'])=={'sha256':row['sha256'],'bytes':row['bytes']},'constructor member changed:'+row['path'])
    ownfreeze=json.loads((HERE/'REVIEW_FREEZE.json').read_text())
    for row in ownfreeze['files']:need(digest(HERE/row['path'])=={'sha256':row['sha256'],'bytes':row['bytes']},'review member changed:'+row['path'])
    spec=importlib.util.spec_from_file_location('reviewed_metadata_checker',src/'validate_request.py');r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
    schema=json.loads((src/'REQUEST_SCHEMA.json').read_text());template=json.loads((src/'REQUEST_TEMPLATE.json').read_text());complete=complete_fixture(schema)
    results=[]
    def test(name,func):
        try:detail=func();results.append({'id':name,'pass':True,'detail':detail})
        except Exception as e:results.append({'id':name,'pass':False,'error':type(e).__name__+':'+str(e)})
    def check(x,ready):
        out=r.metadata(x);assert_scope(out)
        need(out['status']==('METADATA_COMPLETE_UNVERIFIED' if ready else 'HOLD_INCOMPLETE_OR_INVALID_REQUEST_METADATA'),'wrong metadata status:'+out['status'])
        return {'status':out['status'],'blocking_count':len(out['blocking_metadata']),'physical_admission':out['physical_admission'],'evidence_content_verified':out['calibration_evidence_content_verified']}
    test('missing-evidence-null-packet-HOLD',lambda:check(copy.deepcopy(template),False))
    def mutated(path,value,ready=False):
        x=copy.deepcopy(complete);target=x
        for k in path[:-1]:target=target[k]
        target[path[-1]]=value
        return check(x,ready)
    test('nominal-units-not-SI',lambda:mutated(('source','source_units'),'independently_calibrated_SI_V_and_Hz'))
    test('native62-relabel-refusal',lambda:mutated(('lane',),'NATIVE_62_CHANNEL_600CELL'))
    test('metadata-sample-rate-not-clock-calibration',lambda:mutated(('calibration','timebase','evidence'),None))
    test('anti-alias-missing-HOLD',lambda:mutated(('calibration','anti_alias','domain_and_transfer_proof'),None))
    def statistical_missing():
        x=copy.deepcopy(complete);j=x['calibration']['joint_error'];s=schema['properties']['calibration']['properties']['joint_error']['properties']
        j.update(route='JUSTIFIED_STATISTICAL_SIMULTANEOUS_COVERAGE',coverage_fraction='19/20',population_and_dependence=invent(s['population_and_dependence']),deterministic_proof=None)
        return check(x,False)
    test('covariance-only-not-simultaneous-coverage',statistical_missing)
    test('deterministic-route-not-forced-statistical-covariance',lambda:check(copy.deepcopy(complete),True))
    test('rounding-debit-absent-HOLD',lambda:mutated(('calibration','validated_computation','FFT_window_normalization_rounding_proof'),None))
    def unsupported():
        return {'unit_modulus_replacement':mutated(('physical_model_comparison','link_amplitude'),'UNIT_MODULUS_ROTOR'), 'missing_alternative_justification':mutated(('physical_model_comparison','alternative_physical_justification'),None),'exposed_data_called_confirmatory':mutated(('physical_model_comparison','claimed_confirmatory_on_existing_PR246'),True)}
    test('unsupported-physical-model-or-alternative-HOLD',unsupported)
    def placeholders():
        x=copy.deepcopy(template)
        for a in x['calibration']['amplitude_channels']:
            for k in ('nonlinearity_bound_V_per_sample','quantization_and_noise_bound_V_per_sample'):a[k]='0/1'
        out=check(x,False)
        typed=mutated(('source','known_records'),True)
        for raw in ('{"a":1,"a":2}','{"a":NaN}','{"a":0.5}'):
            try:r.strict_load(raw)
            except ValueError:continue
            raise RuntimeError('ambiguous/nonrational JSON accepted')
        return {'zero_without_evidence':out,'boolean_as_count':typed,'strict_parser_refusals':3}
    test('placeholder-zero-not-evidence',placeholders)
    def never_admission():
        deterministic=check(copy.deepcopy(complete),True)
        x=copy.deepcopy(complete);j=x['calibration']['joint_error'];s=schema['properties']['calibration']['properties']['joint_error']['properties']
        j.update(route='JUSTIFIED_STATISTICAL_SIMULTANEOUS_COVERAGE',coverage_fraction='19/20',population_and_dependence=invent(s['population_and_dependence']),simultaneous_coverage_proof=invent(s['simultaneous_coverage_proof']),deterministic_proof=None)
        statistical=check(x,True)
        return {'fixture_classification':x['classification'],'authority_strings':'invented syntax labels, not credentials or reviewers','deterministic':deterministic,'statistical':statistical}
    test('packet-complete-never-physical-promotion',never_admission)
    plan=json.loads((HERE/'REVIEW_PLAN.json').read_text());need({x['id'] for x in results}==set(plan['prospective_test_categories']),'plan coverage')
    result={'artifact_type':'SAME_TEAM_PACKET_METADATA_REVIEW_RESULTS','source_freeze':bind['source_freeze'],'review_freeze':digest(HERE/'REVIEW_FREEZE.json'),'all_pass':all(x['pass'] for x in results),'categories':len(results),'results':results,'scope':'Tiny invented metadata only; no evidence URI opened, evidence files created, private signatures/keys, raw record or model fit. Complete fixture deliberately unverified.','physical_promotion':0,'external_review':'PENDING','actual_calibration_evidence_supplied':False}
    print(json.dumps(result,indent=2,allow_nan=False))
    if not result['all_pass']:raise SystemExit(1)
if __name__=='__main__':main()
