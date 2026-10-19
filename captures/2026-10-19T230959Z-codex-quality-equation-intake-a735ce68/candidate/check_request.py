"""Candidate request metadata checker. No URI/raw/key access and stdout only.
Schema interpretation is adapted from source-bound PR250 validate_request_v2.shape.
No result of this checker authorizes raw acquisition or physical promotion.
"""
import argparse,hashlib,json,re
from pathlib import Path
HERE=Path(__file__).resolve().parent
EXPECTED_SCHEMA_SHA256='9275319244885a01ce3dd884fc598d694d5ef7564ff3d4cfc5cfe7c034f02714'
def load_schema():
    b=(HERE/'REQUEST_SCHEMA_v0.1.json').read_bytes()
    if hashlib.sha256(b).hexdigest()!=EXPECTED_SCHEMA_SHA256:raise ValueError('HOLD_SCHEMA_DIGEST_MISMATCH')
    return json.loads(b)

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
        if 'items' in s:
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
    absent=missing(x)
    return {'artifact_type':'SOURCE_SPECIFIC_PRE_RAW_REQUEST_CHECK','status':'HOLD_INVALID_REQUEST_METADATA' if errors else 'HOLD_INCOMPLETE_UNVERIFIED_REQUEST' if absent else 'DECLARATIONS_COMPLETE_EXTERNAL_REVIEW_REQUIRED','schema_errors':errors,'unsupplied_count':len(absent),'unsupplied':absent,'candidate_confirmatory_designation':'REFUSED_PUBLIC_OUTCOME_AND_PARAMETER_EXPOSURE','raw_access_authorized':False,'calibration_verified':False,'evidence_authenticity_verified':False,'physical_model_verified':False,'physical_promotion':0,'qualification_blockers_closed':0,'scope':'Schema and missingness only. No evidence URI, key, notebook output or raw is opened. Even complete metadata declarations are unverified. Unknown counts and raw SHA are intentionally null until a separately authorized response.'}

def main():
    a=argparse.ArgumentParser();a.add_argument('request',type=Path);a.add_argument('--sha256',required=True);args=a.parse_args()
    b=args.request.read_bytes()
    if hashlib.sha256(b).hexdigest()!=args.sha256:raise SystemExit('HOLD_REQUEST_DIGEST_MISMATCH')
    try:x=json.loads(b)
    except (ValueError,UnicodeError):raise SystemExit('HOLD_INVALID_JSON')
    print(json.dumps(evaluate(x),indent=2,sort_keys=True))
if __name__=='__main__':main()
