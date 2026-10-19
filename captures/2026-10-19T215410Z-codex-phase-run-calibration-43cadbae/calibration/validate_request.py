"""Typed REQUEST-METADATA checker only. Opens no evidence URI, raw record or key.
A complete declaration never authenticates evidence or admits a physical claim.
"""
import argparse
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import re

HERE=Path(__file__).resolve().parent
EXPECTED_SCHEMA_SHA256='964fa5ac8aac4ecb384198c29928d7a16fafe3297f3526f9ffcad8104c6a82dd'
_schema_bytes=(HERE/'REQUEST_SCHEMA.json').read_bytes()
if hashlib.sha256(_schema_bytes).hexdigest()!=EXPECTED_SCHEMA_SHA256:raise RuntimeError('PINNED_SCHEMA_CHANGED')
SCHEMA=json.loads(_schema_bytes)

def shape(x,s,p,errors):
    types=s.get('type',[]);types=[types] if isinstance(types,str) else types
    ok=any((t=='null' and x is None) or (t=='object' and type(x) is dict) or
        (t=='array' and type(x) is list) or (t=='string' and type(x) is str) or
        (t=='integer' and type(x) is int) or (t=='boolean' and type(x) is bool) for t in types)
    if not ok:errors.append(p+':TYPE');return
    if 'const' in s and (type(x) is not type(s['const']) or x!=s['const']):errors.append(p+':CONST')
    if 'enum' in s and x not in s['enum']:errors.append(p+':ENUM')
    if x is None:return
    if type(x) is str:
        if not x.strip() or len(x)<s.get('minLength',0) or len(x)>s.get('maxLength',100000):errors.append(p+':TEXT_LENGTH')
        if 'pattern' in s and re.fullmatch(s['pattern'],x) is None:errors.append(p+':PATTERN')
    elif type(x) is int:
        if x<s.get('minimum',x) or x>s.get('maximum',x):errors.append(p+':INTEGER_RANGE')
    elif type(x) is list:
        if len(x)<s.get('minItems',0) or len(x)>s.get('maxItems',len(x)):errors.append(p+':ARRAY_LENGTH')
        for i,v in enumerate(x):shape(v,s['items'],f'{p}[{i}]',errors)
    elif type(x) is dict:
        for k in s['required']:
            if k not in x:errors.append(p+'.'+k+':MISSING')
        for k in x:
            if k not in s['properties']:errors.append(p+'.'+k+':UNKNOWN_FIELD')
            else:shape(x[k],s['properties'][k],p+'.'+k,errors)

def walk_missing(x,p,errors,skip):
    if p in skip:return
    if x is None:errors.append(p+':UNSUPPLIED');return
    if type(x) is dict:
        for k,v in x.items():walk_missing(v,p+'.'+k,errors,skip)
    elif type(x) is list:
        for i,v in enumerate(x):walk_missing(v,f'{p}[{i}]',errors,skip)

def q(v):return Fraction(v)
def interval(v,name,errors,positive=False,strict=False):
    lo,hi=q(v['lower']),q(v['upper'])
    if lo>hi or (strict and lo==hi) or (positive and lo<=0):errors.append(name+':INTERVAL_ORDER_OR_DOMAIN')
    return lo,hi

def metadata(x):
    errors=[];shape(x,SCHEMA,'request',errors)
    if errors:return outcome(errors,False)
    skip=set();cal=x['calibration'];model=x['physical_model_comparison']
    if cal is not None and cal['joint_error'] is not None:
        joint=cal['joint_error'];route=joint['route']
        if route=='DETERMINISTIC_JOINT_ENCLOSURE':
            skip.update('request.calibration.joint_error.'+v for v in ['coverage_fraction','population_and_dependence','simultaneous_coverage_proof'])
        elif route=='JUSTIFIED_STATISTICAL_SIMULTANEOUS_COVERAGE':skip.add('request.calibration.joint_error.deterministic_proof')
    if model is not None and model['comparison_design']=='RETROSPECTIVE_EXISTING_PUBLIC_ONLY':
        skip.update('request.physical_model_comparison.'+v for v in ['fresh_validation_source','independent_unseen_lineage','fresh_validation_calibration_and_error_budget'])
    walk_missing(x,'request',errors,skip)
    if errors:return outcome(errors,False)
    # Exact arithmetic on DECLARED bounds only; no statement that the evidence is true.
    try:
        channels=cal['amplitude_channels']
        if sorted(c['channel'] for c in channels)!=list(range(1,11)):errors.append('request.calibration.amplitude_channels:EXACT_CHANNEL_MAP_REQUIRED')
        amp=[]
        for c in channels:
            name='channel'+str(c['channel']);g=q(c['applied_gain_V_per_nominal_V']);b=q(c['applied_offset_V'])
            gl,gu=interval(c['gain_interval'],name+'.gain',errors)
            bl,bu=interval(c['offset_interval_V'],name+'.offset',errors)
            yl,yu=interval(c['valid_input_range_nominal_V'],name+'.input_range',errors,strict=True)
            nl=q(c['nonlinearity_bound_V_per_sample']);noise=q(c['quantization_and_noise_bound_V_per_sample'])
            if gl<=0<=gu or not gl<=g<=gu:errors.append(name+':GAIN_NONZERO_OR_APPLIED_OUTSIDE_INTERVAL')
            if min(nl,noise)<0:errors.append(name+':NEGATIVE_ERROR_BOUND')
            amp.append(max(abs(gl-g),abs(gu-g))*max(abs(yl),abs(yu))+max(abs(bl-b),abs(bu-b))+nl+noise)
        clock=cal['timebase'];rl,ru=interval(clock['rate_interval_Hz'],'timebase.rate',errors,positive=True)
        for a in ['origin_uncertainty_s','interchannel_skew_s','sample_jitter_s','warp_to_waveform_vector_error_V']:
            if q(clock[a])<0:errors.append('timebase.'+a+':NEGATIVE_ERROR_BOUND')
        aa=cal['anti_alias'];al,au=interval(aa['declared_input_band_Hz'],'anti_alias.band',errors,strict=True)
        if al<0 or 2*au>=rl:errors.append('anti_alias.band:NONNEGATIVE_BELOW_CALIBRATED_NYQUIST_REQUIRED')
        for a in ['inband_response_vector_error_V','out_of_band_alias_vector_error_V']:
            if q(aa[a])<0:errors.append('anti_alias.'+a+':NEGATIVE_ERROR_BOUND')
        joint=cal['joint_error'];eps=q(joint['epsilon_vector_V'])
        if eps<0:errors.append('joint_error.epsilon_vector_V:NEGATIVE_ERROR_BOUND')
        if joint['route']=='JUSTIFIED_STATISTICAL_SIMULTANEOUS_COVERAGE' and not 0<q(joint['coverage_fraction'])<1:errors.append('joint_error.coverage_fraction:OPEN_UNIT_INTERVAL_REQUIRED')
        other=q(clock['warp_to_waveform_vector_error_V'])+q(aa['inband_response_vector_error_V'])+q(aa['out_of_band_alias_vector_error_V'])
        remaining=eps-other
        if remaining<0 or remaining*remaining<16184*max(amp)**2:errors.append('joint_error:DECLARED_VECTOR_BUDGET_TOO_SMALL')
        for a in ['DC_error_V','RMS_error_V','spectral_amplitude_error_V']:
            if q(cal['validated_computation'][a])<0:errors.append('validated_computation.'+a+':NEGATIVE_ERROR_BOUND')
        if q(model['selection_margin_V'])<0:errors.append('physical_model_comparison.selection_margin_V:NEGATIVE_MARGIN')
    except (ValueError,ZeroDivisionError,KeyError,TypeError,OverflowError):errors.append('request:INVALID_EXACT_RATIONAL_OR_STRUCTURE')
    return outcome(errors,not errors)

def outcome(errors,complete):
    return {'status':'METADATA_COMPLETE_UNVERIFIED' if complete else 'HOLD_INCOMPLETE_OR_INVALID_REQUEST_METADATA',
        'blocking_metadata':errors,'declared_budget_arithmetic_consistent':complete,
        'calibration_evidence_content_verified':False,'independent_authority_verified':False,
        'declared_input_domain_covers_actual_samples_verified':False,
        'actual_common_timing_grid_verified':False,'anti_alias_transfer_verified':False,
        'heldout_independence_verified':False,'validated_computation_proof_verified':False,
        'physical_model_or_alternative_justification_verified':False,
        'calibrated_physical_comparison':'HOLD_NO_INDEPENDENT_CONTENT_REVIEW_OR_EXECUTION',
        'native_62_channel_intake':'HOLD_SEPARATE_INCOMPATIBLE_COMPONENT_LANE',
        'physical_admission':'HOLD','physical_promotion':0,'actual_apparatus_records_evaluated':0,
        'raw_records_opened':0,'new_fits':0,'scope':'Request declarations only. No evidence URI is opened; hashes/presence do not establish authenticity, calibration, blindness, scientific justification or hardware truth.'}

def pairs(items):
    d={}
    for k,v in items:
        if k in d:raise ValueError('DUPLICATE_JSON_KEY')
        d[k]=v
    return d

def strict_load(raw):
    return json.loads(raw,object_pairs_hook=pairs,parse_float=lambda x:(_ for _ in ()).throw(ValueError('FLOAT_JSON_REFUSED_USE_RATIONAL_STRINGS')),parse_constant=lambda x:(_ for _ in ()).throw(ValueError('NONFINITE_JSON_REFUSED')))

def output_path(path,request):
    path=Path(path);lex=Path(os.path.abspath(path));target=path.resolve()
    if lex.is_relative_to(HERE) or target.is_relative_to(HERE):raise ValueError('OUTPUT_INSIDE_IMMUTABLE_PACKAGE')
    if target==Path(request).resolve() or path.exists() or path.is_symlink():raise ValueError('OUTPUT_INPUT_OR_EXISTING')
    if not path.parent.is_dir():raise ValueError('OUTPUT_PARENT_MISSING')
    return path

def main():
    a=argparse.ArgumentParser();a.add_argument('--request',type=Path,required=True);a.add_argument('--expected-request-sha256',required=True);a.add_argument('--output',type=Path,required=True);z=a.parse_args()
    output_path(z.output,z.request)
    with z.output.open('x') as f:
        try:
            raw=z.request.read_bytes();sha=hashlib.sha256(raw).hexdigest()
            if re.fullmatch('[0-9a-f]{64}',z.expected_request_sha256) is None or sha!=z.expected_request_sha256:raise ValueError('CALLER_REQUEST_PIN_MISMATCH')
            out=metadata(strict_load(raw));out['consumed_request_sha256']=sha
        except (OSError,ValueError,UnicodeError) as e:out=outcome(['request:'+str(e)],False)
        f.write(json.dumps(out,indent=2,allow_nan=False)+'\n')

if __name__=='__main__':main()
