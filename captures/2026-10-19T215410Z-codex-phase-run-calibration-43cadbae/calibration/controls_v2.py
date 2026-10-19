"""Frozen small REQUEST-METADATA logic controls; no evidence generation/opening."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import validate_request_v2 as v

HERE=Path(__file__).resolve().parent

def filled(s):
    if 'const' in s:return s['const']
    if 'enum' in s:return next(z for z in s['enum'] if z is not None)
    t=s['type'];t=next(z for z in t if z!='null') if type(t) is list else t
    if t=='object':return {k:filled(z) for k,z in s['properties'].items()}
    if t=='array':return [filled(s['items']) for _ in range(s['minItems'])]
    if t=='integer':return s.get('minimum',1)
    if t=='boolean':return True
    if 'pattern' in s:
        return hashlib.sha256(b'SYNTHETIC_METADATA_NOT_EVIDENCE').hexdigest() if '{64}' in s['pattern'] else '1/1'
    return 'SYNTHETIC_METADATA_NOT_EVIDENCE'

def fixture():
    x=filled(v.SCHEMA);x['classification']='SYNTHETIC_METADATA_CONTROL';c=x['calibration']
    for i,z in enumerate(c['amplitude_channels']):
        z.update(channel=i+1,applied_gain_V_per_nominal_V='1/1',applied_offset_V='0/1',
            gain_interval={'lower':'999999/1000000','upper':'1000001/1000000'},
            offset_interval_V={'lower':'-1/1000000','upper':'1/1000000'},
            nonlinearity_bound_V_per_sample='1/1000000',quantization_and_noise_bound_V_per_sample='1/1000000',
            valid_input_range_nominal_V={'lower':'-2/1','upper':'2/1'})
    c['timebase'].update(rate_interval_Hz={'lower':'1953124/1','upper':'1953126/1'},origin_uncertainty_s='1/1000000000',interchannel_skew_s='1/1000000000',sample_jitter_s='1/1000000000',warp_to_waveform_vector_error_V='1/1000000')
    c['anti_alias'].update(declared_input_band_Hz={'lower':'0/1','upper':'100000/1'},inband_response_vector_error_V='1/1000000',out_of_band_alias_vector_error_V='1/1000000')
    c['joint_error'].update(epsilon_vector_V='1/1',coverage_fraction=None,population_and_dependence=None,simultaneous_coverage_proof=None)
    for k in ['DC_error_V','RMS_error_V','spectral_amplitude_error_V']:c['validated_computation'][k]='1/1000000'
    return x

def hold(x):return v.metadata(x)['status']=='HOLD_INCOMPLETE_OR_INVALID_REQUEST_METADATA'
def throws(fn):
    try:fn()
    except (ValueError,RuntimeError):return True
    return False

def checks():
    base=fixture();out={}
    out['unfilled_template_HOLD']=hold(json.loads((HERE/'REQUEST_TEMPLATE.json').read_text()))
    z=v.metadata(base)
    out['complete_deterministic_metadata_unverified']=z['status']=='METADATA_COMPLETE_UNVERIFIED' and z['physical_admission']=='HOLD' and z['physical_promotion']==0 and not z['calibration_evidence_content_verified']
    s=copy.deepcopy(base);s['calibration']['joint_error'].update(route='JUSTIFIED_STATISTICAL_SIMULTANEOUS_COVERAGE',coverage_fraction='9/10',population_and_dependence=filled(v.SCHEMA['properties']['calibration']['properties']['joint_error']['properties']['population_and_dependence']),simultaneous_coverage_proof=filled(v.SCHEMA['properties']['calibration']['properties']['joint_error']['properties']['simultaneous_coverage_proof']),deterministic_proof=None)
    z=v.metadata(s);out['statistical_route_explicit_joint_unverified']=z['status']=='METADATA_COMPLETE_UNVERIFIED' and z['physical_admission']=='HOLD'
    fresh=copy.deepcopy(base);fresh['physical_model_comparison']['comparison_design']='FRESH_INDEPENDENT_UNSEEN_SOURCE_REQUIRED';z=v.metadata(fresh)
    out['fresh_metadata_still_no_independence_admission']=z['status']=='METADATA_COMPLETE_UNVERIFIED' and not z['heldout_independence_verified'] and z['physical_admission']=='HOLD'
    def mutate(name,path,value,start=base):
        z=copy.deepcopy(start);p=z
        for a in path[:-1]:p=p[a]
        p[path[-1]]=value;out[name]=hold(z)
    mutate('null_amplitude_refused',['calibration','amplitude_channels',0,'evidence'],None)
    zero=copy.deepcopy(base)
    for c in zero['calibration']['amplitude_channels']:c['evidence']=None;c['nonlinearity_bound_V_per_sample']='0/1';c['quantization_and_noise_bound_V_per_sample']='0/1'
    out['zero_does_not_replace_missing_evidence']=hold(zero)
    mutate('wrong_raw_source_refused',['source','raw_sha256'],'0'*64)
    mutate('wrong_result_source_refused',['source','result_sha256'],'0'*64)
    mutate('native62_lane_refused',['lane'],'NATIVE_62')
    mutate('duplicate_channel_refused',['calibration','amplitude_channels',1,'channel'],1)
    mutate('boolean_channel_refused',['calibration','amplitude_channels',1,'channel'],True)
    mutate('missing_channel_refused',['calibration','amplitude_channels'],base['calibration']['amplitude_channels'][:-1])
    mutate('wrong_units_refused',['source','source_units'],'calibrated_SI')
    mutate('gain_crosszero_refused',['calibration','amplitude_channels',0,'gain_interval'],{'lower':'-1/1','upper':'1/1'})
    mutate('applied_gain_outside_refused',['calibration','amplitude_channels',0,'applied_gain_V_per_nominal_V'],'2/1')
    mutate('negative_error_refused',['calibration','amplitude_channels',0,'nonlinearity_bound_V_per_sample'],'-1/1')
    mutate('rate_nonpositive_refused',['calibration','timebase','rate_interval_Hz'],{'lower':'0/1','upper':'1/1'})
    mutate('rate_reversal_refused',['calibration','timebase','rate_interval_Hz'],{'lower':'2/1','upper':'1/1'})
    mutate('anti_alias_above_nyquist_refused',['calibration','anti_alias','declared_input_band_Hz'],{'lower':'0/1','upper':'1000000/1'})
    mutate('zero_denominator_refused',['calibration','joint_error','epsilon_vector_V'],'1/0')
    mutate('too_small_vector_allocation_refused',['calibration','joint_error','epsilon_vector_V'],'1/1000000')
    mutate('missing_rounding_proof_refused',['calibration','validated_computation','FFT_window_normalization_rounding_proof'],None)
    mutate('agreement_not_validated_rounding_role',['calibration','validated_computation','FFT_window_normalization_rounding_proof','role'],'PR246_DIRECT_DFT_AGREEMENT')
    mutate('missing_statistical_joint_proof_refused',['calibration','joint_error','simultaneous_coverage_proof'],None,start=s)
    mutate('statistical_coverage_one_refused',['calibration','joint_error','coverage_fraction'],'1/1',start=s)
    mutate('existing_exposed_test_not_confirmatory',['physical_model_comparison','claimed_confirmatory_on_existing_PR246'],True)
    mutate('fresh_missing_new_error_budget_HOLD',['physical_model_comparison','fresh_validation_calibration_and_error_budget'],None,start=fresh)
    mutate('unit_rotor_model_refused',['physical_model_comparison','link_amplitude'],'UNIT_MODULUS_ROTOR')
    mutate('missing_alternative_justification_HOLD',['physical_model_comparison','alternative_physical_justification'],None)
    mutate('missing_state_prediction_debit_HOLD',['physical_model_comparison','state_estimation_and_model_prediction_error_budget'],None)
    mutate('negative_selection_margin_refused',['physical_model_comparison','selection_margin_V'],'-1/1')
    z=copy.deepcopy(base);z['physical_promotion']=1;out['caller_cannot_promote']=hold(z) and v.metadata(z)['physical_promotion']==0
    mutate('boolean_evidence_bytecount_refused',['trusted_evidence_review','bytes'],True)
    mutate('incorrect_evidence_role_refused',['trusted_evidence_review','role'],'self_approved')
    out['duplicate_json_keys_refused']=throws(lambda:v.strict_load('{"a":1,"a":2}'))
    out['nonfinite_json_refused']=throws(lambda:v.strict_load('{"a":NaN}'))
    out['float_json_refused']=throws(lambda:v.strict_load('{"a":0.1}'))
    with tempfile.TemporaryDirectory(prefix='ud-calibration-request-control-') as td:
        td=Path(td);f=td/'request.json';f.write_text(json.dumps(base));before=hashlib.sha256(f.read_bytes()).hexdigest()
        out['existing_output_refused_unchanged']=throws(lambda:v.output_path(f,f)) and hashlib.sha256(f.read_bytes()).hexdigest()==before
        out['package_output_refused']=throws(lambda:v.output_path(HERE/'NEVER_CREATE.json',f))
        result=td/'new.json';p=subprocess.run([sys.executable,str(HERE/'validate_request_v2.py'),'--request',str(f),'--expected-request-sha256','0'*64,'--output',str(result)],capture_output=True,text=True)
        got=json.loads(result.read_text()) if result.exists() else {}
        out['caller_wrong_snapshot_pin_HOLD']=p.returncode==0 and got.get('status')=='HOLD_INCOMPLETE_OR_INVALID_REQUEST_METADATA' and any('CALLER_REQUEST_PIN_MISMATCH' in e for e in got.get('blocking_metadata',[]))
    with tempfile.TemporaryDirectory(prefix='ud-calibration-manifest-guard-') as td:
        td=Path(td);cap=td/'capture';pkg=cap/'packet';sibling=cap/'sibling';outside=td/'outside'
        pkg.mkdir(parents=True);sibling.mkdir();outside.mkdir();(cap/'MANIFEST.json').write_text('{}')
        old=v.HERE
        try:
            v.HERE=pkg
            out['manifest_ancestor_sibling_refused']=throws(lambda:v.output_path(sibling/'new.json',outside/'request.json'))
            (outside/'to_capture').symlink_to(sibling,target_is_directory=True)
            out['manifest_ancestor_resolved_symlink_refused']=throws(lambda:v.output_path(outside/'to_capture'/'new.json',outside/'request.json'))
            (cap/'to_external').symlink_to(outside,target_is_directory=True)
            out['manifest_ancestor_lexical_symlink_refused']=throws(lambda:v.output_path(cap/'to_external'/'new.json',outside/'request.json'))
        finally:v.HERE=old
        result=outside/'template-result.json';raw=(HERE/'REQUEST_TEMPLATE.json').read_bytes()
        proc=subprocess.run([sys.executable,str(HERE/'validate_request_v2.py'),'--request',str(HERE/'REQUEST_TEMPLATE.json'),'--expected-request-sha256',hashlib.sha256(raw).hexdigest(),'--output',str(result)],capture_output=True,text=True)
        z=json.loads(result.read_text()) if result.exists() else {}
        out['actual_template_cli_HOLD_no_admission']=proc.returncode==0 and z.get('status')=='HOLD_INCOMPLETE_OR_INVALID_REQUEST_METADATA' and z.get('physical_admission')=='HOLD' and z.get('physical_promotion')==0
    return {k:bool(z) for k,z in out.items()}

def main():
    freeze=json.loads((HERE/'PROTOCOL_FREEZE_v0.2.json').read_text())
    for row in freeze['files']:
        b=(HERE/row['path']).read_bytes()
        if len(b)!=row['bytes'] or hashlib.sha256(b).hexdigest()!=row['sha256']:raise RuntimeError('FROZEN_BYTES_CHANGED:'+row['path'])
    plan=json.loads((HERE/'CONTROL_PLAN_v0.2.json').read_text());got=checks()
    if set(plan['controls'])!=set(got):raise RuntimeError('CONTROL_PLAN_COVERAGE')
    out={'artifact_type':'CALIBRATION_MODEL_REQUEST_METADATA_CONTROLS','protocol_freeze_sha256':hashlib.sha256((HERE/'PROTOCOL_FREEZE_v0.2.json').read_bytes()).hexdigest(),'cases':[{'id':k,'observed':z,'expected':plan['controls'][k],'pass':z==plan['controls'][k]} for k,z in got.items()],'all_pass':all(z==plan['controls'][k] for k,z in got.items()),'actual_calibration_records':0,'raw_records_opened':0,'new_fits':0,'measurements':0,'signatures_or_keys_generated':0,'actual_apparatus_records_evaluated':0,'physical_promotion':0,'scope':'Synthetic request declarations only, no evidence truth/authenticity or physical qualification'}
    print(json.dumps(out,indent=2,allow_nan=False))
    if not out['all_pass']:raise SystemExit(1)

if __name__=='__main__':main()
