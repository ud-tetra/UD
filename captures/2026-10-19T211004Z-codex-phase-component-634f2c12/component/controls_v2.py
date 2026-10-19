"""Small synthetic metadata/math controls. Never calls reference.run or opens raw data."""
import hashlib
import json
from pathlib import Path
import platform
import sys
import numpy as np
import reference_checker_v2 as r

HERE=Path(__file__).resolve().parent

def ledger():
    return [[str(r.FS),str(21000+200*i),'0','0','0',str(c)] for i in range(100) for c in range(1,11)]

def ref(fn):
    try:fn()
    except r.Refusal:return True
    return False

def checks():
    rows=ledger();keys=r.groups(rows)
    result={}
    result['metadata_valid_1000']=len(keys)==100
    result['metadata_reversed_stable']=r.groups(list(reversed(rows)))==keys
    canon=[list(a) for a in rows];canon[0][0]='1953125.000';canon[0][2]='-0.00'
    result['decimal_canonical_grouping']=r.groups(canon)==keys
    result['group_split_60_20_20']=[sum(r.split(i)==s for i in range(100)) for s in ['train','validation','test']]==[60,20,20]
    bad=[list(a) for a in rows];bad[1]=bad[0]
    result['duplicate_channel_refused']=ref(lambda:r.groups(bad))
    result['missing_row_refused']=ref(lambda:r.groups(rows[:-1]))
    result['extra_row_refused']=ref(lambda:r.groups(rows+rows[:1]))
    for name,col,value in [('wrong_rate',0,'1'),('nonzero_drive',2,'0.1'),('out_of_range',1,'41001'),('nan_metadata',1,'NaN'),('fraction_channel',5,'1.5'),('outside_channel',5,'11'),('malformed_decimal',0,'bad')]:
        z=list(rows[0]);z[col]=value
        result[name+'_refused']=ref(lambda z=z:r.metadata(z))
    result['wrong_source_hash_refused']=ref(lambda:r.identity(r.RAW_BYTES,'0'*64))
    result['wrong_source_size_refused']=ref(lambda:r.identity(1,r.RAW_SHA))
    result['exact_identity_gate']=r.identity(r.RAW_BYTES,r.RAW_SHA) is None
    f=r.features(np.full(32,0.1),start=0,fs=32)
    result['constant_decimal_zero_ac']=f['DC']==0.1 and f['AC_RMS']==0 and f['rect_dominant_Hz'] is None and f['hann_centroid_Hz'] is None
    n=32;k=3;a=np.cos(2*np.pi*k*np.arange(n)/n)
    f=r.features(a,start=0,fs=n)
    result['known_cosine_bin']=f['rect_dominant_Hz']==3
    result['rect_parseval']=abs(f['rect_positive_power']-f['AC_RMS']**2)<1e-14
    ac=a-f['DC'];w=(1-np.cos(2*np.pi*np.arange(n)/(n-1)))/2
    h=r.spectral(ac,n,'hann');dc=(np.sum(w*ac)**2)/(n*np.sum(w*w))
    result['hann_energy_normalization']=abs(h['positive_power']+dc-np.sum((w*ac)**2)/np.sum(w*w))<1e-14
    f=r.features(np.array([1.,-1.]*16),start=0,fs=32)
    result['nyquist_single_weight']=f['rect_dominant_Hz']==16 and abs(f['rect_positive_power']-1)<1e-14
    result['nonfinite_trace_refused']=ref(lambda:r.features(np.array([0.,np.nan,1.]),start=0))
    result['crop_schema_refused']=ref(lambda:r.features(np.ones(3),start=3))
    obs={(key,ch):{f:float(key[1]) for f in r.FEATURES} for key in keys for ch in range(1,11)}
    cm=r.compare(keys,obs)
    result['linear_endpoint_no_test_fit']=all(z['linear_max_abs']==(200 if z['split']=='validation' else 400) and z['linear_MAE']==(10 if z['split']=='validation' else 20) for z in cm)
    obs[(keys[99],1)]['rect_dominant_Hz']=None
    cm=r.compare(keys,obs)
    result['undefined_no_drop_or_impute']=any(z.get('status')=='HOLD_UNDEFINED_FEATURE' and z['channel']==1 and z['feature']=='rect_dominant_Hz' and z['dropped_records']==0 for z in cm)
    import tempfile
    with tempfile.TemporaryDirectory(prefix='ud-component-output-control-') as td:
        td=Path(td);existing=td/'existing';existing.write_text('KEEP');before=hashlib.sha256(existing.read_bytes()).hexdigest()
        result['output_existing_refused']=ref(lambda:r.check_output_path(existing)) and hashlib.sha256(existing.read_bytes()).hexdigest()==before
        result['output_equal_raw_refused']=ref(lambda:r.check_output_path(existing,existing))
        result['output_package_refused']=ref(lambda:r.check_output_path(HERE/'NEVER_CREATED.json'))
        result['new_external_output_allowed']=r.check_output_path(td/'new.json')==td/'new.json'
    huge={(key,ch):{f:(1e308 if i%2 else -1e308) for f in r.FEATURES} for i,key in enumerate(keys) for ch in range(1,11)}
    with np.errstate(over='ignore',invalid='ignore'):
        result['comparison_overflow_refused']=ref(lambda:r.compare(keys,huge))
    return result

def main():
    freeze=json.loads((HERE/'PROTOCOL_FREEZE_v0.2.json').read_text())
    for row in freeze['files']:
        b=(HERE/row['path']).read_bytes()
        if len(b)!=row['bytes'] or hashlib.sha256(b).hexdigest()!=row['sha256']:
            raise RuntimeError('FROZEN_BYTES_CHANGED:'+row['path'])
    got={k:bool(v) for k,v in checks().items()};plan=json.loads((HERE/'CONTROL_PLAN_v0.2.json').read_text())
    if set(got)!=set(plan['controls']):raise RuntimeError('PLAN_COVERAGE')
    out={'artifact_type':'SYNTHETIC_COMPONENT_CONTROL_RESULTS','protocol_freeze_sha256':hashlib.sha256((HERE/'PROTOCOL_FREEZE_v0.2.json').read_bytes()).hexdigest(),
         'results':[{'id':k,'observed':v,'expected':plan['controls'][k],'pass':v==plan['controls'][k]} for k,v in got.items()],
         'all_pass':all(v==plan['controls'][k] for k,v in got.items()),
         'runtime':{'python':sys.version.split()[0],'numpy':np.__version__,'platform':platform.system()},
         'new_raw_downloads':0,'new_raw_record_executions':0,'new_fits':0,'experimental_records_generated':0,
         'actual_apparatus_records_evaluated':0,'physical_promotion':0,
         'scope':'Synthetic metadata and tiny numerical formula checks only, not interval rounding or physical calibration validation'}
    print(json.dumps(out,indent=2,allow_nan=False))
    if not out['all_pass']:raise SystemExit(1)

if __name__=='__main__':main()
