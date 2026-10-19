"""Prospective apparatus-intake and mismatch arithmetic. Never physical certification."""
import json, hashlib
from pathlib import Path
from fractions import Fraction as F
P=Path(__file__).resolve().parent
def q(x):
    assert isinstance(x,list) and len(x)==2 and all(type(z)==int for z in x)
    assert x[1]>0
    return F(*x)
def packet_hash(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def inverse_gain_scalar_bound(gain_error, amplitude, offset_error, adc_error, gain_min, processing, derivative, time_error):
    """z=g*y+b+n, decoder denominator |ghat|>=gain_min>0; deterministic bounds."""
    args=[gain_error,amplitude,offset_error,adc_error,processing,derivative,time_error]
    assert all(x>=0 for x in args) and gain_min>0
    return (gain_error*amplitude+offset_error+adc_error)/gain_min+processing+derivative*time_error
def decision(residual_lower,residual_upper,alpha,cap):
    assert 0<=residual_lower<=residual_upper and alpha>=0 and cap>=0
    lo=max(F(0),residual_lower-alpha); hi=residual_upper+alpha
    return ('CONDITIONAL_CONSISTENCY' if hi<=cap else 'CONTRACT_CONTRADICTION' if lo>cap else 'HOLD'),lo,hi
def _verify(packet,contract):
    reasons=[]
    if packet.get('contract_sha256')!=packet_hash(contract): reasons.append('CONTRACT_HASH')
    if packet.get('lane')!='temporal209': reasons.append('WRONG_LANE')
    if packet.get('units')!=contract['coordinate_unit']: reasons.append('UNITS')
    ch=packet.get('channel_map',[])
    if not isinstance(ch,list) or len(ch)!=62 or any(type(i)!=int for i in ch) or set(ch)!=set(range(62)): reasons.append('CHANNEL_MAP')
    if packet.get('missing_samples',1)!=0 or packet.get('clipped_samples',1)!=0: reasons.append('RAW_COVERAGE')
    if packet.get('uncertainty_kind')!='deterministic_uniform': reasons.append('UNSUPPORTED_COVERAGE')
    for field in ['calibration_source_ids','validation_source_ids']:
        value=packet.get(field)
        if not isinstance(value,list) or not value or any(not isinstance(i,str) or not i.strip() for i in value): reasons.append('LINEAGE_SCHEMA')
    calibration=set(packet.get('calibration_source_ids',[])); validation=set(packet.get('validation_source_ids',[]))
    if not calibration or not validation or calibration&validation: reasons.append('HELDOUT_LINEAGE')
    required=contract['required_receipts']
    for name in required:
        r=packet.get('receipts',{}).get(name)
        # Receipts here are content-addressed supplied objects, not proof of their truth.
        if not isinstance(r,dict) or not r.get('body') or r.get('sha256')!=packet_hash(r['body']): reasons.append('RECEIPT_'+name)
    if packet.get('unaliased_identification',False) and packet.get('alias_band_injective') is not True: reasons.append('ALIAS_BAND')
    if packet.get('prediction_frozen_before_validation') is not True: reasons.append('PREDICTION_FREEZE')
    if packet.get('provenance_kind') not in ['synthetic_fixture','apparatus_submission']: reasons.append('PROVENANCE_KIND')
    try:
        cap=q(packet['mismatch_cap']); alpha=q(packet['acquisition_F_upper']); rlo=q(packet['residual_F_lower']); rhi=q(packet['residual_F_upper'])
        if cap!=q(contract['synthetic_control_cap']) and packet['provenance_kind']=='synthetic_fixture': reasons.append('CAP_MUTATION')
        assert alpha>=0 and 0<=rlo<=rhi and cap>=0
        if packet['provenance_kind']=='apparatus_submission':
            # Actual residual/budget validation is not implemented by these small controls.
            reasons.append('APPARATUS_NUMERIC_EVIDENCE_NOT_IMPLEMENTED')
        status,lo,hi=decision(rlo,rhi,alpha,cap)
    except (KeyError,AssertionError,TypeError,ValueError):
        reasons.append('INVALID_NUMERIC_ENCLOSURE');status='HOLD';lo=hi=None
    if reasons: status='HOLD'
    return {'mathematical_status':status,'hold_reasons':reasons,
        'mismatch_lower':None if lo is None else [lo.numerator,lo.denominator],
        'mismatch_upper':None if hi is None else [hi.numerator,hi.denominator],
        'physical_verdict':'HOLD_UNQUALIFIED', 'physical_promotion':0,
        'scope':'Synthetic protocol logic only; receipt hashes neither validate calibration nor authenticate an external reviewer.'}
def verify(packet,contract):
    try:
        return _verify(packet,contract)
    except (AttributeError,KeyError,TypeError,ValueError,AssertionError,ZeroDivisionError):
        return {'mathematical_status':'HOLD','hold_reasons':['MALFORMED_PACKET'],
                'mismatch_lower':None,'mismatch_upper':None,
                'physical_verdict':'HOLD_UNQUALIFIED','physical_promotion':0,
                'scope':'Malformed inputs rejected before any apparatus qualification.'}
