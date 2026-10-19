"""Frozen tiny metadata/path controls. No signing, raw arrays, keys or fitting."""
import argparse,json,hashlib,shutil
from pathlib import Path
P=Path(__file__).resolve().parent
def jb(x):return (json.dumps(x,indent=2)+'\n').encode()
def digest(q):return hashlib.sha256(Path(q).read_bytes()).hexdigest()
PLAN=[
('absent_real_evidence','HOLD_MISSING_EXTERNAL_EVIDENCE',None),
('missing_caller_request_pin','HOLD_INTAKE_PREFLIGHT','MISSING_CALLER_REQUEST_PIN'),
('malformed_request_hash','HOLD_INTAKE_PREFLIGHT','MALFORMED_CALLER_REQUEST_HASH'),
('wrong_request_hash','HOLD_INTAKE_PREFLIGHT','CALLER_REQUEST_HASH_MISMATCH'),
('candidate_self_authorization','HOLD_INTAKE_PREFLIGHT','CANDIDATE_SELF_AUTHORIZATION'),
('request_inside_candidate','HOLD_INTAKE_PREFLIGHT','REQUEST_INSIDE_CANDIDATE'),
('policy_inside_candidate','HOLD_INTAKE_PREFLIGHT','POLICY_INSIDE_CANDIDATE'),
('symlink_request_anchor','HOLD_INTAKE_PREFLIGHT','SYMLINK_ANCHOR'),
('symlink_policy_anchor','HOLD_INTAKE_PREFLIGHT','SYMLINK_ANCHOR'),
('synthetic_policy_for_real','HOLD_INTAKE_PREFLIGHT','SYNTHETIC_OR_UNSUPPORTED_REAL_POLICY'),
('known_fixture_public_key_relabelled','HOLD_INTAKE_PREFLIGHT','KNOWN_SYNTHETIC_PUBLIC_KEY_RELABELED'),
('known_fixture_policy_pin','HOLD_INTAKE_PREFLIGHT','KNOWN_SYNTHETIC_POLICY_BYTES'),
('known_fixture_admission_pin','HOLD_INTAKE_PREFLIGHT','KNOWN_SYNTHETIC_ADMISSION_BYTES'),
('wrong_role','HOLD_INTAKE_PREFLIGHT','INCORRECT_REQUIRED_ROLES'),
('incomplete_policy_roles','HOLD_INTAKE_PREFLIGHT','INCOMPLETE_REAL_ROLE_AUTHORITY'),
('malformed_external_admission_pin','HOLD_INTAKE_PREFLIGHT','MALFORMED_EXTERNAL_POLICY_OR_ADMISSION_HASH'),
('tampered_denylist','HOLD_INTAKE_PREFLIGHT','SYNTHETIC_DENYLIST_CHANGED'),
('tampered_source_bindings','HOLD_INTAKE_PREFLIGHT','SOURCE_BINDINGS_CHANGED'),
('tampered_delegate','HOLD_INTAKE_PREFLIGHT','PINNED_DELEGATE_CHANGED'),
('complete_dummy_routes_to_unchanged_verifier','HOLD_DELEGATED_EVIDENCE',None)]
def generate(out):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);deny=json.loads((P/'KNOWN_SYNTHETIC_AUTHORITY.json').read_text());index=[]
    for name,status,reason in PLAN:
        case=out/name;bundle=case/'bundle';bundle.mkdir(parents=True)
        policy={'version':'UD_TRUST_POLICY_v1','scope':'apparatus','keys':{'metadata_only_not_a_real_key':{'public_key_hex':'ab'*32,'roles':['calibration','model','acquisition','lineage']}}}
        if name=='synthetic_policy_for_real':policy['scope']='synthetic_fixture'
        if name=='known_fixture_public_key_relabelled':policy['keys']['metadata_only_not_a_real_key']['public_key_hex']=deny['public_key_hex'][0]
        if name=='incomplete_policy_roles':policy['keys']['metadata_only_not_a_real_key']['roles']=['calibration']
        policyfile=case/'POLICY.json';policyfile.write_bytes(jb(policy))
        admission={'version':'UD_ANALYTIC_ADMISSION_v1','run_id':'caller-unqualified-routing-probe','analytic_model_path':'MODEL.json'}
        (bundle/'ADMISSION.json').write_bytes(jb(admission))
        packet={'provenance_kind':'apparatus_submission','files':{k:{'path':n} for k,n in [('raw_adc','adc.placeholder'),('prediction','prediction.placeholder'),('timestamps','timestamps.placeholder'),('calibration','CALIBRATION.json')]}}
        (bundle/'PACKET.json').write_bytes(jb(packet))
        for n in ['CONTRACT.json','RECEIPTS.json','MODEL.json','CALIBRATION.json']:(bundle/n).write_bytes(b'{}\n')
        for n in ['adc.placeholder','prediction.placeholder','timestamps.placeholder']:(bundle/n).write_bytes(b'NOT_A_MEASUREMENT\n')
        req={'version':'UD_REAL_EVIDENCE_REQUEST_v1','pin_source':'independent_caller','evidence_kind':'independently_calibrated_apparatus','roles':['calibration','model','acquisition','lineage'],'bundle_path':'bundle','policy_path':'POLICY.json','expected_policy_sha256':digest(policyfile),'expected_admission_sha256':digest(bundle/'ADMISSION.json'),'verification_utc':'2026-10-19T22:00:00Z'}
        if name=='candidate_self_authorization':req['pin_source']='candidate_bundle'
        if name=='wrong_role':req['roles']=['calibration','model','acquisition','constructor']
        if name=='known_fixture_policy_pin':req['expected_policy_sha256']=deny['policy_sha256'][0]
        if name=='known_fixture_admission_pin':req['expected_admission_sha256']=deny['admission_sha256'][0]
        if name=='malformed_external_admission_pin':req['expected_admission_sha256']='abc'
        requestfile=case/'REQUEST.json'
        if name=='request_inside_candidate':req['bundle_path']='.';req['policy_path']='../POLICY.json';requestfile=bundle/'REQUEST.json'
        if name=='policy_inside_candidate':shutil.copyfile(policyfile,bundle/'POLICY.json');req['policy_path']='bundle/POLICY.json'
        requestfile.write_bytes(jb(req));call_request=str(requestfile.relative_to(out))
        if name=='symlink_request_anchor':(bundle/'LINK_REQUEST.json').symlink_to('../REQUEST.json');call_request=str((bundle/'LINK_REQUEST.json').relative_to(out))
        if name=='symlink_policy_anchor':(case/'LINK_POLICY.json').symlink_to('POLICY.json');req['policy_path']='LINK_POLICY.json';requestfile.write_bytes(jb(req))
        expected=digest(requestfile)
        if name=='missing_caller_request_pin':expected=None
        if name=='malformed_request_hash':expected='not-a-hash'
        if name=='wrong_request_hash':expected='0'*64
        script='intake_v2.py'
        if name in ['tampered_denylist','tampered_source_bindings','tampered_delegate']:
            pkg=case/'package';pkg.mkdir();(pkg/'verifier').mkdir()
            for n in ['intake_v2.py','SOURCE_BINDINGS.json','KNOWN_SYNTHETIC_AUTHORITY.json']:shutil.copyfile(P/n,pkg/n)
            for n in ['authenticated_record.py','base_record.py']:shutil.copyfile(P/'verifier'/n,pkg/'verifier'/n)
            if name=='tampered_denylist':(pkg/'KNOWN_SYNTHETIC_AUTHORITY.json').write_bytes(b'{}\n')
            if name=='tampered_source_bindings':(pkg/'SOURCE_BINDINGS.json').write_bytes(b'{}\n')
            if name=='tampered_delegate':(pkg/'verifier'/'authenticated_record.py').write_bytes((pkg/'verifier'/'authenticated_record.py').read_bytes()+b'\n# tampered, must never execute\n')
            script=str((pkg/'intake_v2.py').relative_to(out))
        index.append({'id':name,'expected_status':status,'expected_reason':reason,'request':None if name=='absent_real_evidence' else call_request,'expected_request_sha256':None if name=='absent_real_evidence' else expected,'script':script,'expected_delegations':1 if name=='complete_dummy_routes_to_unchanged_verifier' else 0,'metadata_only':True})
    (out/'CONTROL_INDEX.json').write_bytes(jb(index));members=[]
    for f in sorted(out.rglob('*')):
        if f.is_symlink():members.append({'path':str(f.relative_to(out)),'symlink':str(f.readlink())})
        elif f.is_file():members.append({'path':str(f.relative_to(out)),'sha256':digest(f),'size_bytes':f.stat().st_size})
    (out/'DATA_FREEZE.json').write_bytes(jb({'status':'FROZEN_METADATA_AND_PATH_CONTROLS_BEFORE_EVALUATION','members':members,'controls':len(index),'actual_real_records':0,'new_signing_keys':0,'new_fits':0,'physical_promotion':0}))
    return index
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);x=ap.parse_args();generate(x.out)
