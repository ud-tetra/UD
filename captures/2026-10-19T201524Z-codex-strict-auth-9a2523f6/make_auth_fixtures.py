"""One-time synthetic signing fixtures; ephemeral private keys never serialized or logged."""
import json,copy,struct,zipfile,hashlib
from pathlib import Path
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from authenticated_record import canonical,sha,PREFIX,receipt_artifacts,grid_core
P=Path(__file__).resolve().parent
def jb(x):return (json.dumps(x,indent=2)+'\n').encode()
def load(b):return json.loads(b)
def make(out):
    out=Path(out);out.mkdir(parents=True,exist_ok=False)
    # Local synthetic fixtures only. Public keys/signatures retained; private keys die with this process.
    secret={k:Ed25519PrivateKey.generate() for k in ['cal','model','acq','lineage','rogue']}
    principals={'cal':'fixture-calibrator','model':'fixture-constructor','acq':'fixture-acquirer','lineage':'fixture-lineage-reviewer'}
    rolekey={'calibration':'cal','model':'model','acquisition':'acq','lineage':'lineage'}
    policy0={'version':'UD_TRUST_POLICY_v1','scope':'synthetic_fixture','snapshot_valid_from_utc':'2026-10-19T00:00:00Z','snapshot_valid_until_utc':'2026-10-20T00:00:00Z','constructor_principals':['fixture-constructor'],'keys':{}}
    for role,key in rolekey.items():policy0['keys'][key]={'algorithm':'Ed25519','principal':principals[key],'public_key_hex':secret[key].public_key().public_bytes_raw().hex(),'roles':[role],'valid_from_utc':'2026-10-01T00:00:00Z','valid_until_utc':'2026-10-31T00:00:00Z','revoked':False}
    cases=[]
    def add(name,expected,mode=None):cases.append((name,expected,mode or name))
    add('valid_harmonic_envelope_and_receipts','CONDITIONAL_ANALYTIC_CONSISTENCY','valid')
    add('clear_analytic_mismatch','ANALYTIC_CONTRACT_CONTRADICTION')
    add('overlap_at_saved_cap','HOLD_ANALYTIC_OVERLAP')
    add('predictor_uncertainty_changes_saved_PASS_to_HOLD','HOLD_ANALYTIC_OVERLAP')
    add('exact_constant_model_zero_beta','CONDITIONAL_ANALYTIC_CONSISTENCY')
    add('beta_too_small','HOLD_AUTH_OR_ANALYTIC_EVIDENCE')
    add('negative_beta','HOLD_AUTH_OR_ANALYTIC_EVIDENCE')
    add('wrong_analytic_grid','HOLD_AUTH_OR_ANALYTIC_EVIDENCE')
    add('unsupported_analytic_model','HOLD_AUTH_OR_ANALYTIC_EVIDENCE')
    add('wrong_analytic_units','HOLD_AUTH_OR_ANALYTIC_EVIDENCE')
    add('wrong_target_id','HOLD_AUTH_OR_ANALYTIC_EVIDENCE')
    for name in ['raw_tamper','prediction_tamper','calibration_tamper','analytic_model_tamper','signature_bitflip','signature_short','untrusted_key','wrong_domain_signed','wrong_run_signed','wrong_challenge_signed','wrong_admission_signed','receipt_predates_admission','calibration_signed_postdata','acquisition_signed_predata','future_receipt','missing_role','duplicate_role','wrong_key_role','wrong_algorithm','wrong_public_key_length','revoked_key','expired_key','not_yet_valid_key','expired_policy','caller_policy_hash_wrong','caller_admission_hash_wrong','bundle_policy_path_refused','same_principal_calibration_and_lineage','duplicate_public_key_different_principals','constructor_signs_calibration','synthetic_key_for_apparatus_refused','declared_lineage_reuse','raw_hash_in_model_ancestry','duplicate_admission_json_key','float_beta_refused','crossrun_old_receipt']:
        add(name,'HOLD_AUTH_OR_ANALYTIC_EVIDENCE')
    add('bundle_replacement_policy_ignored','CONDITIONAL_ANALYTIC_CONSISTENCY')
    for name in ['role_substring_not_a_role_list','empty_key_roles','constructor_bare_string','expired_now_despite_old_claimed_issue']:
        add(name,'HOLD_AUTH_OR_ANALYTIC_EVIDENCE')
    members={};index=[];baseline_receipts=None
    for name,expected,mode in cases:
        files={p.name:p.read_bytes() for p in (P/'inputs/base_bundle').iterdir() if p.is_file()}
        c=load(files['CONTRACT.json']);packet=load(files['PACKET.json']);cal=load(files['CALIBRATION.json']);policy=copy.deepcopy(policy0)
        model={'version':'FINITE_HARMONIC_MODEL_v1','model_id':'toy-harmonic-reference','coordinate_unit':'model_coordinate','time_unit':'model_time','frequencies':[[1,1]],'signals':[{'preparation':a,'channel':0,'constant':[1,4],'cosine':[[1,1024]],'sine':[[0,1]]} for a in range(2)]}
        beta=[1,256];grid_override=False
        if mode in ['clear_analytic_mismatch','overlap_at_saved_cap']:
            raw=list(struct.unpack('<496q',files['adc.i64le']));raw[0]=24 if mode=='clear_analytic_mismatch' else 10;files['adc.i64le']=struct.pack('<496q',*raw)
        if mode=='predictor_uncertainty_changes_saved_PASS_to_HOLD':beta=[1,16]
        if mode=='exact_constant_model_zero_beta':
            for row in model['signals']:row['cosine']=[[0,1]]
            beta=[0,1]
        if mode=='beta_too_small':beta=[0,1]
        if mode=='negative_beta':beta=[-1,256]
        if mode=='wrong_analytic_grid':grid_override=True
        if mode=='unsupported_analytic_model':model['version']='UNSUPPORTED_MODEL'
        if mode=='wrong_analytic_units':model['coordinate_unit']='volts'
        if mode=='declared_lineage_reuse':packet['validation_source_ids']=cal['source_ids']
        if mode=='raw_hash_in_model_ancestry':c['model_raw_dependency_sha256']=[sha(files['adc.i64le'])]
        if mode=='constructor_signs_calibration':cal['calibrator']='fixture-constructor';policy['keys']['cal']['principal']='fixture-constructor'
        if mode=='synthetic_key_for_apparatus_refused':packet['provenance_kind']='apparatus_submission'
        if mode=='wrong_key_role':policy['keys']['cal']['roles']=['model']
        if mode=='role_substring_not_a_role_list':policy['keys']['cal']['roles']='not_calibration'
        if mode=='empty_key_roles':policy['keys']['cal']['roles']=[]
        if mode=='constructor_bare_string':policy['constructor_principals']='fixture-constructor'
        if mode=='expired_now_despite_old_claimed_issue':policy['keys']['cal']['valid_until_utc']='2026-10-10T00:00:00Z'
        if mode=='wrong_algorithm':policy['keys']['cal']['algorithm']='UNSUPPORTED'
        if mode=='wrong_public_key_length':policy['keys']['cal']['public_key_hex']='00'*31
        if mode=='revoked_key':policy['keys']['cal']['revoked']=True
        if mode=='expired_key':policy['keys']['cal']['valid_until_utc']='2026-10-02T00:00:00Z'
        if mode=='not_yet_valid_key':policy['keys']['cal']['valid_from_utc']='2026-10-02T02:00:00Z'
        if mode=='expired_policy':policy['snapshot_valid_until_utc']='2026-10-18T00:00:00Z'
        if mode=='same_principal_calibration_and_lineage':policy['keys']['lineage']['principal']='fixture-calibrator'
        if mode=='duplicate_public_key_different_principals':
            policy['keys']['clone']=copy.deepcopy(policy['keys']['cal']);policy['keys']['clone']['principal']='different-principal'
        files['CALIBRATION.json']=jb(cal);c['calibration_sha256']=sha(files['CALIBRATION.json']);c['prediction_sha256']=sha(files['prediction.i64le']);files['CONTRACT.json']=jb(c)
        packet['contract_sha256']=sha(files['CONTRACT.json'])
        for key in packet['files']:packet['files'][key]['sha256']=sha(files[packet['files'][key]['path']])
        files['PACKET.json']=jb(packet);files['ANALYTIC_MODEL.json']=jb(model)
        admission={'version':'UD_ANALYTIC_ADMISSION_v1','run_id':'synthetic-'+name,'challenge':sha(('fixture-challenge-'+name).encode()),'frozen_utc':'2026-10-02T00:00:00Z','base_contract_sha256':sha(files['CONTRACT.json']),'analytic_model_path':'ANALYTIC_MODEL.json','analytic_model_sha256':sha(files['ANALYTIC_MODEL.json']),'analytic_target_id':model['model_id'],'beta_F_upper':beta,'coordinate_unit':'model_coordinate','norm':'Frobenius','shape':[2,4,62],'grid_sha256':'0'*64 if grid_override else sha(canonical(grid_core(c,cal)))}
        if mode=='wrong_target_id':admission['analytic_target_id']='other-target'
        files['ADMISSION.json']=jb(admission);ahash=sha(files['ADMISSION.json']);receipts=[]
        for role,kid in rolekey.items():
            issued='2026-10-02T01:00:00Z' if role in ['calibration','model'] else '2026-10-03T00:03:00Z'
            body={'version':'UD_RECEIPT_v1','domain':'UD','role':role,'key_id':kid,'run_id':admission['run_id'],'challenge':admission['challenge'],'admission_sha256':ahash,'issued_utc':issued,'artifacts':receipt_artifacts(role,c,cal,packet,admission,sha(files['CONTRACT.json']),sha(files['PACKET.json']))}
            signing=kid
            if role=='calibration':
                if mode=='untrusted_key':body['key_id']='rogue';signing='rogue'
                if mode=='wrong_domain_signed':body['domain']='MQM'
                if mode=='wrong_run_signed':body['run_id']='other-run'
                if mode=='wrong_challenge_signed':body['challenge']='0'*64
                if mode=='wrong_admission_signed':body['admission_sha256']='0'*64
                if mode=='receipt_predates_admission':body['issued_utc']='2026-10-01T00:00:00Z'
                if mode=='calibration_signed_postdata':body['issued_utc']='2026-10-03T00:04:00Z'
                if mode=='future_receipt':body['issued_utc']='2026-10-21T00:00:00Z'
            if role=='acquisition' and mode=='acquisition_signed_predata':body['issued_utc']='2026-10-02T02:00:00Z'
            sig=secret[signing].sign(PREFIX+canonical(body)).hex();receipts.append({'payload':body,'signature_hex':sig})
        if mode=='valid':baseline_receipts=copy.deepcopy(receipts)
        if mode=='crossrun_old_receipt':receipts[2]=copy.deepcopy(baseline_receipts[2])
        if mode=='missing_role':receipts.pop()
        if mode=='duplicate_role':receipts[-1]=copy.deepcopy(receipts[0])
        if mode=='signature_bitflip':receipts[0]['signature_hex']=('0' if receipts[0]['signature_hex'][0]!='0' else '1')+receipts[0]['signature_hex'][1:]
        if mode=='signature_short':receipts[0]['signature_hex']='00'*63
        files['RECEIPTS.json']=jb(receipts)
        if mode=='raw_tamper':files['adc.i64le']=bytes([files['adc.i64le'][0]^1])+files['adc.i64le'][1:]
        if mode=='prediction_tamper':files['prediction.i64le']=bytes([files['prediction.i64le'][0]^1])+files['prediction.i64le'][1:]
        if mode=='calibration_tamper':cal['channels'][0]['adc_error']=[0,1];files['CALIBRATION.json']=jb(cal)
        if mode=='analytic_model_tamper':model['signals'][0]['constant']=[1,2];files['ANALYTIC_MODEL.json']=jb(model)
        if mode=='bundle_replacement_policy_ignored':files['POLICY.json']=jb({'untrusted_bundle_key':secret['rogue'].public_key().public_bytes_raw().hex()})
        if mode=='duplicate_admission_json_key':
            files['ADMISSION.json']=files['ADMISSION.json'].replace(b'{',b'{"norm":"Frobenius",',1);ahash=sha(files['ADMISSION.json'])
        if mode=='float_beta_refused':
            admission['beta_F_upper']=[1.0,256];files['ADMISSION.json']=jb(admission);ahash=sha(files['ADMISSION.json'])
        policy_path='trust/'+name+'.json';policy_bytes=jb(policy);members[policy_path]=policy_bytes
        if mode=='bundle_policy_path_refused':files['INSIDE_POLICY.json']=policy_bytes;policy_path='bundles/'+name+'/INSIDE_POLICY.json'
        phash=sha(policy_bytes)
        if mode=='caller_policy_hash_wrong':phash='0'*64
        if mode=='caller_admission_hash_wrong':ahash='0'*64
        for filename,b in files.items():members['bundles/'+name+'/'+filename]=b
        index.append({'id':name,'expected':expected,'policy_path':policy_path,'expected_policy_sha256':phash,'expected_admission_sha256':ahash,'verification_utc':'2026-10-19T20:00:00Z','physical_expected':'HOLD_UNQUALIFIED'})
    with zipfile.ZipFile(out/'AUTH_FIXTURES.zip','w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for n,b in sorted(members.items()):
            info=zipfile.ZipInfo(n,(2026,10,19,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16;z.writestr(info,b,compresslevel=9)
    (out/'CONTROL_INDEX.json').write_bytes(jb(index))
    freeze={'status':'FROZEN_SYNTHETIC_SIGNATURE_AND_HARMONIC_FIXTURES_BEFORE_VERIFICATION','files':{n:sha((out/n).read_bytes()) for n in ['AUTH_FIXTURES.zip','CONTROL_INDEX.json']},'members':[{'path':n,'sha256':sha(b),'size_bytes':len(b)} for n,b in sorted(members.items())],'controls':len(index),'private_keys_serialized_or_retained':False,'all_signatures_are_synthetic_fixtures':True,'actual_apparatus_records':0,'physical_promotion':0}
    (out/'DATA_FREEZE.json').write_bytes(jb(freeze));print(json.dumps({'controls':len(index),'members':len(members),'zip_bytes':(out/'AUTH_FIXTURES.zip').stat().st_size,'private_keys_saved':False}))
if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);make(ap.parse_args().out)
