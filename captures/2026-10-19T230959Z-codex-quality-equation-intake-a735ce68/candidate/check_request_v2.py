"""Candidate request metadata checker. No URI/raw/key access and stdout only.
Version0.2: deep typed const/enum equality, strict JSON, per-channel evidence and candidate scope.
Schema interpretation is adapted from source-bound PR250 validate_request_v2.shape.
No result of this checker authorizes raw acquisition or physical promotion.
"""
import argparse,hashlib,json,re
from pathlib import Path
HERE=Path(__file__).resolve().parent
EXPECTED_SCHEMA_SHA256='59d6787cd2e31666e774ac8ae8b526556e9d20d4f7702c8fb480b4ffd6991386'
def load_schema():
    b=(HERE/'REQUEST_SCHEMA_v0.2.json').read_bytes()
    if hashlib.sha256(b).hexdigest()!=EXPECTED_SCHEMA_SHA256:raise ValueError('HOLD_SCHEMA_DIGEST_MISMATCH')
    return json.loads(b)

def deep_equal(x,y):
    if type(x) is not type(y):return False
    if type(x) is dict:return x.keys()==y.keys() and all(deep_equal(x[k],y[k]) for k in x)
    if type(x) is list:return len(x)==len(y) and all(deep_equal(a,b) for a,b in zip(x,y))
    return x==y

def strict_object(pairs):
    d={}
    for k,v in pairs:
        if k in d:raise ValueError('DUPLICATE_JSON_KEY:'+k)
        d[k]=v
    return d

def reject_constant(token):raise ValueError('NONFINITE_JSON_NUMBER:'+token)
def strict_loads(b):return json.loads(b,object_pairs_hook=strict_object,parse_constant=reject_constant)

def shape(x,s,p,errors):
    types=s.get('type',[]);types=[types] if isinstance(types,str) else types
    ok=any((t=='null' and x is None) or (t=='object' and type(x) is dict) or
        (t=='array' and type(x) is list) or (t=='string' and type(x) is str) or
        (t=='integer' and type(x) is int) or (t=='boolean' and type(x) is bool) for t in types)
    if not ok:errors.append(p+':TYPE');return
    if 'const' in s and not deep_equal(x,s['const']):errors.append(p+':CONST')
    if 'enum' in s and not any(deep_equal(x,v) for v in s['enum']):errors.append(p+':ENUM')
    if x is None:return
    if type(x) is str:
        if not x.strip() or len(x)<s.get('minLength',0) or len(x)>s.get('maxLength',100000):errors.append(p+':TEXT_LENGTH')
        if 'pattern' in s and re.fullmatch(s['pattern'],x) is None:errors.append(p+':PATTERN')
    elif type(x) is int:
        if x<s.get('minimum',x) or x>s.get('maximum',x):errors.append(p+':INTEGER_RANGE')
    elif type(x) is list:
        if len(x)<s.get('minItems',0) or len(x)>s.get('maxItems',len(x)):errors.append(p+':ARRAY_LENGTH')
        if 'prefixItems' in s:
            for i,v in enumerate(x):
                if i<len(s['prefixItems']):shape(v,s['prefixItems'][i],f'{p}[{i}]',errors)
                else:errors.append(f'{p}[{i}]:EXTRA_TUPLE_ITEM')
        elif type(s.get('items')) is dict:
            for i,v in enumerate(x):shape(v,s['items'],f'{p}[{i}]',errors)
    elif type(x) is dict:
        for k in s.get('required',[]):
            if k not in x:errors.append(p+'.'+k+':MISSING')
        for k in x:
            if k not in s.get('properties',{}):errors.append(p+'.'+k+':UNKNOWN_FIELD')
            else:shape(x[k],s['properties'][k],p+'.'+k,errors)

def missing(x,p='request'):
    if x is None:return [p]
    if type(x)is dict:return sum((missing(v,p+'.'+k) for k,v in x.items()),[])
    if type(x)is list:return sum((missing(v,f'{p}[{i}]') for i,v in enumerate(x)),[])
    return []

def evaluate(x,schema=None):
    schema=load_schema() if schema is None else schema
    errors=[];shape(x,schema,'request',errors)
    if not errors:
        scope=x['calibration']['joint_error']['scope'] if x['calibration'] is not None and x['calibration']['joint_error'] is not None else None
        if scope is not None:
            n=scope['record_count'];g=scope['group_count'];ns=scope['samples_per_record'];lo=scope['crop_start_inclusive'];hi=scope['crop_stop_exclusive']
            if all(v is not None for v in [ns,lo,hi]) and not 0<=lo<hi<=ns:errors.append('request.calibration.joint_error.scope:CROP_DOMAIN_INCONSISTENT')
            if n is not None and g is not None and g>n:errors.append('request.calibration.joint_error.scope:GROUP_COUNT_EXCEEDS_RECORDS')
            if n is not None and x['known_records'] is not None and n!=x['known_records']:errors.append('request:RECORD_COUNT_CUSTODY_DECLARATIONS_DISAGREE')
            if g is not None and x['known_groups'] is not None and g!=x['known_groups']:errors.append('request:GROUP_COUNT_CUSTODY_DECLARATIONS_DISAGREE')
    absent=missing(x)
    return {'artifact_type':'SOURCE_SPECIFIC_PRE_RAW_REQUEST_CHECK','status':'HOLD_INVALID_REQUEST_METADATA' if errors else 'HOLD_INCOMPLETE_UNVERIFIED_REQUEST' if absent else 'DECLARATIONS_COMPLETE_EXTERNAL_REVIEW_REQUIRED','schema_errors':errors,'unsupplied_count':len(absent),'unsupplied':absent,'candidate_confirmatory_designation':'REFUSED_PUBLIC_OUTCOME_AND_PARAMETER_EXPOSURE','raw_access_authorized':False,'calibration_verified':False,'evidence_authenticity_verified':False,'physical_model_verified':False,'physical_promotion':0,'qualification_blockers_closed':0,'scope':'Schema and missingness only. No evidence URI, key, notebook output or raw is opened. Even complete metadata declarations are unverified. Candidate counts and crop must be independently source-bound. No 1000-record or16184-sample domain is inherited. Declarations never establish authenticity or numerical budget validity.'}

def main():
    a=argparse.ArgumentParser();a.add_argument('request',type=Path);a.add_argument('--sha256',required=True);args=a.parse_args()
    b=args.request.read_bytes()
    if hashlib.sha256(b).hexdigest()!=args.sha256:raise SystemExit('HOLD_REQUEST_DIGEST_MISMATCH')
    try:x=strict_loads(b)
    except (ValueError,UnicodeError):raise SystemExit('HOLD_INVALID_JSON')
    print(json.dumps(evaluate(x),indent=2,sort_keys=True))
if __name__=='__main__':main()
