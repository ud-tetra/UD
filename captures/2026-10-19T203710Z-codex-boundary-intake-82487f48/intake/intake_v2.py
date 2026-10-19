"""Fail-closed REAL-evidence intake. No signing, fitting or evidence synthesis."""
import argparse, hashlib, json, os, re, subprocess, sys
from pathlib import Path
from datetime import datetime
P=Path(__file__).resolve().parent
ROLES={'calibration','model','acquisition','lineage'}
SOURCE_BINDINGS_SHA256='58d5c39bb20ef3db8a8496e87b8e5c15f954ac3ba59bb9297c3b8f5234528c95'
class Refuse(Exception): pass
def need(ok,reason):
    if not ok: raise Refuse(reason)
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read_json(path):
    return read_snapshot(path)[0]
def read_snapshot(path):
    def pairs(xs):
        d={}
        for k,v in xs:
            need(k not in d,'DUPLICATE_JSON_KEY');d[k]=v
        return d
    def no_num(x): raise Refuse('NONINTEGER_JSON_NUMBER')
    raw=Path(path).read_bytes()
    return json.loads(raw,object_pairs_hook=pairs,parse_float=no_num,parse_constant=no_num),hashlib.sha256(raw).hexdigest()
def valid_hash(x): return isinstance(x,str) and re.fullmatch('[0-9a-f]{64}',x) is not None
def canonical_path(value,is_dir=False,base=None):
    need(isinstance(value,str) and bool(value.strip()),'PATH_REQUIRED')
    p=Path(value)
    need('..' not in p.parts,'PATH_TRAVERSAL')
    if not p.is_absolute(): p=(Path.cwd() if base is None else Path(base))/p
    need(not any(a.is_symlink() for a in [p,*p.parents]),'SYMLINK_ANCHOR')
    q=p.resolve(strict=True)
    need(q.is_dir() if is_dir else q.is_file(),'PATH_TYPE')
    return p,q
def member(root,name):
    need(isinstance(name,str) and name and not Path(name).is_absolute() and '..' not in Path(name).parts,'BUNDLE_MEMBER_PATH')
    raw,resolved=canonical_path(str(root/name))
    need(root in resolved.parents,'BUNDLE_MEMBER_ESCAPE');return resolved
def result(status,blocking,**extra):
    return {'status':status,'blocking_items':blocking,'real_records_evaluated':0,'actual_real_records_verified':0,
      'caller_classified_requests_evaluated':0,'candidate_requests_delegated':0,'delegations':0,'delegation_attempts':0,
      'actual_hardware_acquisitions_verified':0,'physical_verdict':'HOLD_UNQUALIFIED',
      'identity_or_calibration_truth':'NOT_CERTIFIED','heldout_independence':'NOT_CERTIFIED',
      'pin_independence':'CALLER_DECLARED_NOT_ESTABLISHED_BY_PATH_OR_HASH',
      'physical_promotion':0,'external_review':'PENDING',**extra}
def missing():
    return result('HOLD_MISSING_EXTERNAL_EVIDENCE',[
      'caller-provided REAL evidence request outside candidate bundle',
      'independently caller-pinned expected request SHA256',
      'complete REAL ADC/predictor/timestamp/calibration/receipt bundle',
      'external REAL public-key policy with independently pinned SHA256',
      'independently pinned analytic admission SHA256 and predata contract',
      'caller verification epoch and independent calibration/acquisition/lineage provenance'])
def verify_request(request_path=None,expected_request_sha256=None):
    attempts=0
    if request_path is None and expected_request_sha256 is None:return missing()
    try:
        need(request_path is not None,'MISSING_REQUEST_PATH');need(expected_request_sha256 is not None,'MISSING_CALLER_REQUEST_PIN')
        need(valid_hash(expected_request_sha256),'MALFORMED_CALLER_REQUEST_HASH')
        request_raw,request_file=canonical_path(request_path)
        request,request_hash=read_snapshot(request_file);need(request_hash==expected_request_sha256,'CALLER_REQUEST_HASH_MISMATCH')
        need(request['version']=='UD_REAL_EVIDENCE_REQUEST_v1','REQUEST_VERSION')
        need(request['pin_source']=='independent_caller','CANDIDATE_SELF_AUTHORIZATION')
        need(request['evidence_kind']=='independently_calibrated_apparatus','NONREAL_REQUEST_CLASSIFICATION')
        roles=request['roles'];need(isinstance(roles,list) and len(roles)==4 and all(type(x)==str for x in roles) and set(roles)==ROLES,'INCORRECT_REQUIRED_ROLES')
        bundle_raw,bundle=canonical_path(request['bundle_path'],True,request_file.parent)
        need(bundle_raw not in request_raw.parents and bundle not in request_file.parents,'REQUEST_INSIDE_CANDIDATE')
        policy_raw,policy=canonical_path(request['policy_path'],False,request_file.parent)
        need(bundle_raw not in policy_raw.parents and bundle not in policy.parents,'POLICY_INSIDE_CANDIDATE')
        ph,ah=request['expected_policy_sha256'],request['expected_admission_sha256']
        need(valid_hash(ph) and valid_hash(ah),'MALFORMED_EXTERNAL_POLICY_OR_ADMISSION_HASH')
        bindings,binding_hash=read_snapshot(P/'SOURCE_BINDINGS.json');need(binding_hash==SOURCE_BINDINGS_SHA256,'SOURCE_BINDINGS_CHANGED')
        deny,deny_hash=read_snapshot(P/'KNOWN_SYNTHETIC_AUTHORITY.json');need(deny_hash==bindings['known_synthetic_authority_sha256'],'SYNTHETIC_DENYLIST_CHANGED')
        need(ph not in deny['policy_sha256'],'KNOWN_SYNTHETIC_POLICY_BYTES')
        need(ah not in deny['admission_sha256'],'KNOWN_SYNTHETIC_ADMISSION_BYTES')
        pol,policy_hash=read_snapshot(policy);need(policy_hash==ph,'EXTERNAL_POLICY_HASH_MISMATCH')
        need(pol['version']=='UD_TRUST_POLICY_v1' and pol['scope']=='apparatus','SYNTHETIC_OR_UNSUPPORTED_REAL_POLICY')
        need(isinstance(pol['keys'],dict) and bool(pol['keys']),'EMPTY_REAL_KEY_POLICY')
        covered=set()
        for key in pol['keys'].values():
            pub=key['public_key_hex'];need(isinstance(pub,str) and re.fullmatch('[0-9a-f]{64}',pub) is not None,'PUBLIC_KEY_SCHEMA')
            need(pub not in deny['public_key_hex'],'KNOWN_SYNTHETIC_PUBLIC_KEY_RELABELED')
            rs=key['roles'];need(isinstance(rs,list) and rs and all(type(x)==str and x in ROLES for x in rs),'INCORRECT_POLICY_ROLE')
            covered.update(rs)
        need(covered==ROLES,'INCOMPLETE_REAL_ROLE_AUTHORITY')
        admission=member(bundle,'ADMISSION.json');ad,admission_hash=read_snapshot(admission);need(admission_hash==ah,'EXTERNAL_ADMISSION_HASH_MISMATCH')
        need(ad['version']=='UD_ANALYTIC_ADMISSION_v1','ADMISSION_VERSION')
        runid=ad['run_id'];need(isinstance(runid,str) and runid.strip(),'REAL_RUN_ID_REQUIRED')
        need(not any(x in runid.lower() for x in ['synthetic','fixture','toy']),'SYNTHETIC_RUN_CLASSIFICATION')
        packet_path=member(bundle,'PACKET.json');packet,packet_hash=read_snapshot(packet_path);need(packet['provenance_kind']=='apparatus_submission','SYNTHETIC_OR_UNCLASSIFIED_PACKET')
        for name in ['CONTRACT.json','RECEIPTS.json']:member(bundle,name)
        for role in ['raw_adc','prediction','timestamps','calibration']:member(bundle,packet['files'][role]['path'])
        model_path=ad['analytic_model_path'];member(bundle,model_path)
        now=request['verification_utc'];need(isinstance(now,str),'VERIFICATION_EPOCH_REQUIRED')
        instant=datetime.fromisoformat(now.replace('Z','+00:00'));need(instant.tzinfo is not None,'VERIFICATION_EPOCH_TIMEZONE')
        for name,h in bindings['delegate_files_sha256'].items():need(sha(P/'verifier'/name)==h,'PINNED_DELEGATE_CHANGED')
        # Child script directory is the pinned verifier directory, never a candidate path.
        env=dict(os.environ);env.pop('PYTHONPATH',None);env['PYTHONDONTWRITEBYTECODE']='1'
        command=[sys.executable,str(P/'verifier'/'authenticated_record.py'),str(bundle),'--policy',str(policy),'--expected-policy-sha256',ph,'--expected-admission-sha256',ah,'--verification-utc',now]
        need(sha(request_file)==request_hash and sha(policy)==policy_hash and sha(admission)==admission_hash and sha(packet_path)==packet_hash,'REQUEST_OR_PINNED_INPUT_CHANGED')
        attempts=1
        completed=subprocess.run(command,cwd=P/'verifier',env=env,capture_output=True,text=True,check=False)
        need(sha(request_file)==request_hash and sha(policy)==policy_hash and sha(admission)==admission_hash and sha(packet_path)==packet_hash,'REQUEST_OR_PINNED_INPUT_CHANGED')
        need(completed.returncode==0,'PINNED_VERIFIER_PROCESS_FAILED');delegated=json.loads(completed.stdout)
        need(delegated['physical_verdict']=='HOLD_UNQUALIFIED' and delegated['physical_promotion']==0,'UNEXPECTED_DELEGATE_SCOPE')
        status='HOLD_DELEGATED_EVIDENCE' if delegated.get('status','').startswith('HOLD') else 'DELEGATED_CONDITIONAL_EVIDENCE_RESULT'
        return result(status,[],caller_classified_requests_evaluated=1,candidate_requests_delegated=1,delegations=1,delegation_attempts=attempts,
          delegated_result=delegated,scope='Complete caller-classified request only. No authenticated physical identity, calibration truth or hardware qualification follows.')
    except (Refuse,KeyError,TypeError,ValueError,AttributeError,OSError) as e:
        return result('HOLD_INTAKE_PREFLIGHT',[str(e) if isinstance(e,Refuse) else 'MALFORMED_OR_MISSING_EXTERNAL_EVIDENCE'],delegation_attempts=attempts)
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--request');ap.add_argument('--expected-request-sha256');ap.add_argument('--out')
    args=ap.parse_args();value=verify_request(args.request,args.expected_request_sha256)
    text=json.dumps(value,indent=2)+'\n'
    if args.out:
        with Path(args.out).open('x') as f:f.write(text)
    else:print(text,end='')
