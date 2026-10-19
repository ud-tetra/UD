"""Analytic predictor envelope and caller-pinned Ed25519 receipt verification."""
import json,hashlib,struct
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
from cryptography.exceptions import InvalidSignature,UnsupportedAlgorithm
from flint import arb,ctx
from base_record import verify as base_verify,digest,rational,instant,need,Hold,ar,pair,endpoint,safe_file
ctx.prec=512
PREFIX=b'UD/ACQUISITION-RECEIPT/v1\0'
ROLES=('calibration','model','acquisition','lineage')
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True,allow_nan=False).encode()
def sha(b):return hashlib.sha256(b).hexdigest()
def read_json(path):
    raw=Path(path).read_bytes()
    def pairs(rows):
        d={}
        for k,v in rows:need(k not in d,'DUPLICATE_JSON_KEY');d[k]=v
        return d
    def no_float(x):raise Hold('NONINTEGER_JSON_NUMBER')
    return json.loads(raw,object_pairs_hook=pairs,parse_float=no_float,parse_constant=no_float),sha(raw)
def hx(s,n):
    need(isinstance(s,str) and len(s)==2*n and set(s)<=set('0123456789abcdef'),'HEX_SCHEMA');return bytes.fromhex(s)
def lineage_core(contract,cal,packet):
    return {'calibration_source_ids':cal['source_ids'],'calibration_raw_dependencies':cal['raw_dependency_sha256'],
      'model_source_ids':contract['model_source_ids'],'model_raw_dependencies':contract['model_raw_dependency_sha256'],
      'validation_source_ids':packet['validation_source_ids'],'scored_raw_sha256':packet['files']['raw_adc']['sha256']}
def grid_core(c,cal):
    return {'shape':[c['preparations'],c['times'],62],'channel_order':'model_coordinate_0_to_61',
      'nominal_tick_origins':c['nominal_tick_origins'],'nominal_tick_step':c['nominal_tick_step'],
      'model_time_per_tick':cal['clock']['model_time_per_tick'],'coordinate_unit':c['coordinate_unit'],'time_unit':c['time_unit']}
def receipt_artifacts(role,c,cal,packet,admission,base_hash,packet_hash):
    if role=='calibration':return {'base_contract_sha256':base_hash,'calibration_sha256':c['calibration_sha256']}
    if role=='model':return {'base_contract_sha256':base_hash,'analytic_model_sha256':admission['analytic_model_sha256'],
      'prediction_sha256':c['prediction_sha256'],'grid_sha256':admission['grid_sha256'],'beta_F_upper':admission['beta_F_upper']}
    if role=='acquisition':return {'packet_sha256':packet_hash,'raw_adc_sha256':packet['files']['raw_adc']['sha256'],'timestamps_sha256':packet['files']['timestamps']['sha256']}
    return {'packet_sha256':packet_hash,'lineage_core_sha256':sha(canonical(lineage_core(c,cal,packet)))}
def analytic_envelope(root,c,cal,admission):
    model_path=safe_file(root,admission['analytic_model_path']);model,mhash=read_json(model_path)
    need(mhash==admission['analytic_model_sha256'],'ANALYTIC_MODEL_HASH')
    need(model['version']=='FINITE_HARMONIC_MODEL_v1' and model['model_id']==admission['analytic_target_id'],'ANALYTIC_TARGET')
    need(model['coordinate_unit']==c['coordinate_unit'] and model['time_unit']==c['time_unit'],'ANALYTIC_UNITS')
    need(sha(canonical(grid_core(c,cal)))==admission['grid_sha256'],'ANALYTIC_GRID_BINDING')
    frequencies=[rational(x,True) for x in model['frequencies']]
    need(len(set(frequencies))==len(frequencies),'DUPLICATE_ANALYTIC_FREQUENCY')
    signals={};p,t=c['preparations'],c['times']
    for row in model['signals']:
        a,ch=row['preparation'],row['channel'];need(type(a)==type(ch)==int and 0<=a<p and 0<=ch<62,'ANALYTIC_COORDINATES')
        need((a,ch) not in signals,'DUPLICATE_ANALYTIC_SIGNAL')
        const=rational(row['constant']);u=[rational(x) for x in row['cosine']];v=[rational(x) for x in row['sine']]
        need(len(u)==len(v)==len(frequencies),'ANALYTIC_COEFFICIENT_COUNT');signals[a,ch]=(const,u,v)
    pred=safe_file(root,packet_prediction_path(root));den=c['prediction_denominator']
    acc=arb(0);tick_scale=rational(cal['clock']['model_time_per_tick']);consumed=hashlib.sha256();count=0
    with pred.open('rb') as stream:
        for a in range(p):
            for k in range(t):
                b=stream.read(62*8);consumed.update(b);values=struct.unpack('<62q',b)
                time=(c['nominal_tick_origins'][a]+k*c['nominal_tick_step'])*tick_scale
                cs=[(ar(w*time).cos(),ar(w*time).sin()) for w in frequencies]
                for ch,num in enumerate(values):
                    y=arb(0)
                    if (a,ch) in signals:
                        b0,u,v=signals[a,ch];y=ar(b0)
                        for j,(co,si) in enumerate(cs):y+=ar(u[j])*co+ar(v[j])*si
                    error=y-ar(F(num,den));acc+=abs(error)**2;count+=1
    need(consumed.hexdigest()==c['prediction_sha256'],'ANALYTIC_PREDICTION_CONSUMED_HASH')
    beta=rational(admission['beta_F_upper'],True);upper=acc.sqrt()
    need(upper<=ar(beta),'ANALYTIC_ENVELOPE_EXCEEDS_PREDECLARED_BETA')
    return {'model_id':model['model_id'],'checked_scalars':count,'error_squared_upper':endpoint(acc),
      'validated_model_to_saved_predictor_F_upper':endpoint(upper),'predata_beta_F_upper':pair(beta),
      'scope':'Finite nominal-grid bound to the exact declared harmonic formula, not a theorem that the formula describes an apparatus.'},beta
def packet_prediction_path(root):return read_json(Path(root)/'PACKET.json')[0]['files']['prediction']['path']
def _verify(root,policy_path,expected_policy_hash,expected_admission_hash,verification_utc):
    root=Path(root).resolve();policy_path=Path(policy_path).resolve()
    need(root not in policy_path.parents,'POLICY_MUST_BE_CALLER_EXTERNAL')
    policy,phash=read_json(policy_path);need(phash==expected_policy_hash,'CALLER_POLICY_HASH')
    admission,ahash=read_json(root/'ADMISSION.json');need(ahash==expected_admission_hash,'CALLER_ADMISSION_HASH')
    need(policy['version']=='UD_TRUST_POLICY_v1' and admission['version']=='UD_ANALYTIC_ADMISSION_v1','VERSION')
    need(isinstance(admission['run_id'],str) and admission['run_id'].strip(),'RUN_ID_SCHEMA');hx(admission['challenge'],32)
    now=instant(verification_utc);need(instant(policy['snapshot_valid_from_utc'])<=now<=instant(policy['snapshot_valid_until_utc']),'POLICY_SNAPSHOT_VALIDITY')
    c,chash=read_json(root/'CONTRACT.json');packet,packet_hash=read_json(root/'PACKET.json')
    need(chash==admission['base_contract_sha256'],'BASE_CONTRACT_BINDING')
    start,end=instant(packet['acquisition_start_utc']),instant(packet['acquisition_end_utc'])
    need(instant(admission['frozen_utc'])<start and end<=now,'ADMISSION_OR_RUN_CHRONOLOGY')
    need(admission['coordinate_unit']==c['coordinate_unit'] and admission['norm']=='Frobenius','ADMISSION_UNITS_NORM')
    need(admission['shape']==[c['preparations'],c['times'],62],'ADMISSION_SHAPE')
    need(policy['scope'] in ['synthetic_fixture','apparatus'],'POLICY_SCOPE')
    need(policy['scope']=='apparatus' or packet['provenance_kind']=='synthetic_fixture','SYNTHETIC_KEYS_FOR_ACTUAL_APPARATUS')
    cal_path=safe_file(root,packet['files']['calibration']['path']);cal,cal_hash=read_json(cal_path)
    need(cal_hash==c['calibration_sha256'],'CALIBRATION_BINDING')
    constructor=policy['constructor_principals']
    need(isinstance(constructor,list) and constructor and all(isinstance(s,str) and s.strip() for s in constructor) and len(set(constructor))==len(constructor) and cal['constructor'] in constructor,'CONSTRUCTOR_PRINCIPAL_POLICY')
    keys=policy['keys'];need(isinstance(keys,dict) and bool(keys),'KEY_POLICY')
    seen={}
    for key in keys.values():
        pub=hx(key['public_key_hex'],32);principal=key['principal']
        need(isinstance(principal,str) and principal.strip(),'PRINCIPAL_SCHEMA')
        roles=key['roles'];need(isinstance(roles,list) and roles and all(type(role)==str and role in ROLES for role in roles) and len(set(roles))==len(roles),'KEY_ROLE_SCHEMA')
        need(pub not in seen or seen[pub]==principal,'DUPLICATE_PUBLIC_KEY_PRINCIPALS');seen[pub]=principal
    receipts,receipts_hash=read_json(root/'RECEIPTS.json');need(isinstance(receipts,list) and len(receipts)==4,'RECEIPT_COUNT')
    observed={};roles_seen=set()
    for receipt in receipts:
        body=receipt['payload'];role=body['role'];need(role in ROLES and role not in roles_seen,'ROLE_DUPLICATION_OR_UNKNOWN');roles_seen.add(role)
        kid=body['key_id'];need(kid in keys,'UNTRUSTED_KEY');key=keys[kid]
        need(key['algorithm']=='Ed25519' and role in key['roles'],'KEY_ALGORITHM_OR_ROLE')
        need(type(key['revoked'])==bool and not key['revoked'],'REVOKED_KEY')
        issued=instant(body['issued_utc']);need(instant(key['valid_from_utc'])<=issued<=instant(key['valid_until_utc']) and issued<=now,'KEY_OR_RECEIPT_TIME')
        need(instant(key['valid_from_utc'])<=now<=instant(key['valid_until_utc']),'KEY_NOT_VALID_AT_VERIFICATION')
        need(issued>=instant(admission['frozen_utc']),'RECEIPT_PREDATES_ADMISSION')
        need(issued<start if role in ['calibration','model'] else issued>=end,'ROLE_CHRONOLOGY')
        expected={'version':'UD_RECEIPT_v1','domain':'UD','role':role,'key_id':kid,'run_id':admission['run_id'],
          'challenge':admission['challenge'],'admission_sha256':expected_admission_hash,'issued_utc':body['issued_utc'],
          'artifacts':receipt_artifacts(role,c,cal,packet,admission,chash,packet_hash)}
        need(body==expected,'SIGNED_CONTEXT_OR_ARTIFACT_BINDING')
        Ed25519PublicKey.from_public_bytes(hx(key['public_key_hex'],32)).verify(hx(receipt['signature_hex'],64),PREFIX+canonical(body))
        observed[role]=key['principal']
    need(set(observed)==set(ROLES),'MISSING_ROLE')
    need(observed['calibration']==cal['calibrator'],'CALIBRATOR_POLICY_IDENTITY')
    need(observed['calibration'] not in constructor and observed['lineage'] not in constructor and observed['calibration']!=observed['lineage'],'PRINCIPAL_DUTY_SEPARATION')
    base=base_verify(root,chash);need(base['status']!='HOLD_INPUT_EVIDENCE','BASE_'+base.get('reason','EVIDENCE'))
    envelope,beta=analytic_envelope(root,c,cal,admission)
    residual=ar(rational(base['residual_F_squared_exact'])).sqrt();alpha=ar(rational(base['acquisition_F_squared_exact'])).sqrt()
    total=alpha+ar(beta);lower=max(arb(0),residual-total);upper=residual+total;cap=ar(rational(base['cap']))
    status='CONDITIONAL_ANALYTIC_CONSISTENCY' if upper<=cap else 'ANALYTIC_CONTRACT_CONTRADICTION' if lower>cap else 'HOLD_ANALYTIC_OVERLAP'
    need(digest(policy_path)==expected_policy_hash and digest(root/'ADMISSION.json')==expected_admission_hash,'TRUST_OR_ADMISSION_CHANGED')
    need(digest(root/'PACKET.json')==packet_hash and digest(root/'CONTRACT.json')==chash,'BASE_METADATA_CHANGED')
    need(digest(root/'RECEIPTS.json')==receipts_hash,'RECEIPTS_CHANGED')
    return {'status':status,'base_saved_predictor_status':base['status'],'residual_F_squared_exact':base['residual_F_squared_exact'],
      'acquisition_F_squared_exact':base['acquisition_F_squared_exact'],'analytic_envelope':envelope,
      'total_uncertainty_F_upper':endpoint(total),'analytic_mismatch_lower':endpoint(lower,True),'analytic_mismatch_upper':endpoint(upper),
      'signature_status':'VERIFIED_UNDER_CALLER_PINNED_POLICY','authorized_principals':observed,
      'verification_utc':verification_utc,'freshness':'RUN_CHALLENGE_BOUND; STATELESS_EXACT_REPLAY_IS_IDEMPOTENT',
      'calibration_truth':'NOT_CERTIFIED','heldout_independence':'NOT_CERTIFIED','physical_verdict':'HOLD_UNQUALIFIED',
      'unaliased_identification':'NOT_CERTIFIED','physical_promotion':0,
      'scope':'Mathematical harmonic-envelope and record checks under supplied calibration premises; key-to-principal identity is caller policy, not outside identity proof or physical qualification.'}
def verify(root,policy_path,expected_policy_hash,expected_admission_hash,verification_utc=None):
    verification_utc=verification_utc or datetime.now(timezone.utc).isoformat()
    try:return _verify(root,policy_path,expected_policy_hash,expected_admission_hash,verification_utc)
    except (Hold,KeyError,TypeError,ValueError,AttributeError,OSError,struct.error,InvalidSignature,UnsupportedAlgorithm) as e:
        reason=str(e) if isinstance(e,Hold) else 'INVALID_SIGNATURE' if isinstance(e,InvalidSignature) else 'MALFORMED_OR_UNSUPPORTED_AUTH_EVIDENCE'
        return {'status':'HOLD_AUTH_OR_ANALYTIC_EVIDENCE','reason':reason,'physical_verdict':'HOLD_UNQUALIFIED','physical_promotion':0}
if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('bundle');ap.add_argument('--policy',required=True);ap.add_argument('--expected-policy-sha256',required=True);ap.add_argument('--expected-admission-sha256',required=True);ap.add_argument('--verification-utc')
    x=ap.parse_args();print(json.dumps(verify(x.bundle,x.policy,x.expected_policy_sha256,x.expected_admission_sha256,x.verification_utc),indent=2))
