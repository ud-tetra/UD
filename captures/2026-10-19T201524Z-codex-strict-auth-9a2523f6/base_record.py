"""Stream exact ADC/predictor/timestamp evidence; conditional arithmetic, never physical promotion."""
import hashlib,json,struct,math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime
from flint import arb,fmpq,ctx
ctx.prec=512
class Hold(Exception): pass
def need(ok,reason):
    if not ok: raise Hold(reason)
def digest(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        while b:=f.read(1<<20):h.update(b)
    return h.hexdigest()
def rational(x,nonnegative=False):
    need(isinstance(x,list) and len(x)==2 and all(type(z)==int for z in x) and x[1]>0,'RATIONAL_SCHEMA')
    y=F(*x);need(not nonnegative or y>=0,'NEGATIVE_BUDGET');return y
def ids(x):
    need(isinstance(x,list) and bool(x) and all(isinstance(s,str) and s.strip() for s in x),'LINEAGE_SCHEMA')
    need(len(set(x))==len(x),'DUPLICATE_LINEAGE');return set(x)
def instant(s):
    need(isinstance(s,str),'CHRONOLOGY_SCHEMA')
    d=datetime.fromisoformat(s.replace('Z','+00:00'));need(d.tzinfo is not None,'TIMEZONE_REQUIRED');return d
def ar(f):return arb(fmpq(f.numerator,f.denominator))
def pair(f):return [f.numerator,f.denominator]
def endpoint(x,lower=False):
    z=((x*(1<<160)).floor() if lower else (x*(1<<160)).ceil()).unique_fmpz()
    need(z is not None,'UNRESOLVED_ENCLOSURE');return [int(z),1<<160]
def safe_file(root,name):
    need(isinstance(name,str),'PATH_SCHEMA');p=(root/name).resolve()
    need(root in p.parents and p.is_file(),'PATH_OR_MISSING_FILE');return p
def _verify(root,expected_contract_sha):
    root=Path(root).resolve();cp=root/'CONTRACT.json';cb=cp.read_bytes()
    need(hashlib.sha256(cb).hexdigest()==expected_contract_sha,'FROZEN_CONTRACT_HASH')
    c=json.loads(cb); packet_bytes=(root/'PACKET.json').read_bytes();packet=json.loads(packet_bytes)
    need(packet['contract_sha256']==expected_contract_sha,'PACKET_CONTRACT_BINDING')
    need(c['version']=='ADC_RECORD_CONTRACT_v0.1' and c['channels']==62,'CONTRACT_SCHEMA')
    p,t=c['preparations'],c['times'];need(type(p)==type(t)==int and p>0 and t>=3,'SHAPE_SCHEMA')
    nvec=p*t;unit=c['coordinate_unit'];need(unit=='model_coordinate' and c['time_unit']=='model_time','UNITS')
    cap=rational(c['mismatch_F_cap'],True)
    need(c['prediction_target']=='frozen_saved_predictor','PREDICTION_TARGET_SCOPE')
    start,end=instant(packet['acquisition_start_utc']),instant(packet['acquisition_end_utc'])
    need(start<end and instant(c['frozen_utc'])<start,'CONTRACT_CHRONOLOGY')
    need(c['time_treatment'] in ['acquisition_uncertainty','model_mismatch'],'TIME_ALLOCATION')
    paths={}
    for key in ['raw_adc','timestamps','prediction','calibration']:
        e=packet['files'][key];f=safe_file(root,e['path']);need(digest(f)==e['sha256'],'FILE_HASH_'+key);paths[key]=f
    need(packet['files']['prediction']['sha256']==c['prediction_sha256'],'PREDICTION_FREEZE')
    need(packet['files']['calibration']['sha256']==c['calibration_sha256'],'CALIBRATION_FREEZE')
    need(instant(packet['data_freeze_utc'])>=end,'DATA_FREEZE_CHRONOLOGY')
    cal_bytes=paths['calibration'].read_bytes()
    need(hashlib.sha256(cal_bytes).hexdigest()==packet['files']['calibration']['sha256'],'CALIBRATION_SNAPSHOT_HASH')
    cal=json.loads(cal_bytes)
    need(cal['coordinate_unit']==unit and cal['time_unit']==c['time_unit'] and cal['adc_unit']=='ADC_code','CALIBRATION_UNITS')
    need(cal['coverage']=='deterministic_uniform','UNSUPPORTED_COVERAGE')
    need(isinstance(cal['calibrator'],str) and bool(cal['calibrator'].strip()) and isinstance(cal['constructor'],str) and bool(cal['constructor'].strip()) and cal['calibrator']!=cal['constructor'],'DECLARED_DUTIES')
    need(instant(cal['frozen_utc'])<start,'CALIBRATION_CHRONOLOGY')
    need(instant(cal['valid_from_utc'])<=start and instant(cal['valid_until_utc'])>=end,'CALIBRATION_VALIDITY')
    calibration_ids=ids(cal['source_ids']);validation_ids=ids(packet['validation_source_ids'])
    model_ids=ids(c['model_source_ids'])
    need(not validation_ids&(calibration_ids|model_ids),'HELDOUT_LINEAGE')
    ancestor_hashes=[]
    for dependencies in [cal['raw_dependency_sha256'],c['model_raw_dependency_sha256']]:
        need(isinstance(dependencies,list) and dependencies and all(isinstance(h,str) and len(h)==64 and set(h)<=set('0123456789abcdef') for h in dependencies),'DEPENDENCY_HASH_SCHEMA')
        ancestor_hashes+=dependencies
    need(packet['files']['raw_adc']['sha256'] not in ancestor_hashes,'SCORED_RAW_IN_CALIBRATION_OR_MODEL_ANCESTRY')
    need(packet['provenance_kind'] in ['synthetic_fixture','apparatus_submission'],'PROVENANCE_KIND')
    need(type(packet['unaliased_identification'])==bool,'ALIAS_REQUEST_SCHEMA')
    if packet['unaliased_identification']:
        band=c['frequency_band_model_radians'];width=rational(band[1])-rational(band[0])
        need(width>0 and ar(width)<arb.pi(),'NONINJECTIVE_ALIAS_BAND')
        need(cal['filter_evidence_id'] and c['band_evidence_id'],'ALIAS_EVIDENCE_MISSING')
    need(paths['raw_adc'].stat().st_size==paths['prediction'].stat().st_size==nvec*62*8,'RAW_OR_PREDICTION_LENGTH')
    need(paths['timestamps'].stat().st_size==nvec*8,'TIMESTAMP_LENGTH')
    channels=cal['channels'];need(isinstance(channels,list) and len(channels)==62,'CHANNEL_COUNT')
    need(all(type(row['coordinate'])==type(row['raw_channel'])==int for row in channels),'CHANNEL_SCHEMA')
    need({row['coordinate'] for row in channels}==set(range(62)) and {row['raw_channel'] for row in channels}==set(range(62)),'CHANNEL_BIJECTION')
    channels=sorted(channels,key=lambda x:x['coordinate'])
    denom=c['prediction_denominator'];need(type(denom)==int and denom>0,'PREDICTION_DENOMINATOR')
    configs=[];base2=F(0);baseL=F(0);L2=F(0)
    for row in channels:
        need(type(row['sign'])==int and row['sign'] in [-1,1],'CHANNEL_SIGN')
        g=rational(row['applied_gain']);b=rational(row['applied_offset']);need(g>0,'APPLIED_GAIN')
        bounds={k:rational(row[k],True) for k in ['gain_error','amplitude_bound','offset_error','adc_error','processing_error','nonlinearity_error','crosstalk_error','filter_tail_error','derivative_bound']}
        base=(bounds['gain_error']*bounds['amplitude_bound']+bounds['offset_error']+bounds['adc_error'])/g+sum((bounds[k] for k in ['processing_error','nonlinearity_error','crosstalk_error','filter_tail_error']),F(0))
        derivative=bounds['derivative_bound'] if c['time_treatment']=='acquisition_uncertainty' else F(0)
        base2+=base*base;baseL+=base*derivative;L2+=derivative*derivative
        aa=F(row['sign'],1)/g;bb=-row['sign']*b/g;scale=math.lcm(aa.denominator,bb.denominator,denom)
        need(type(row['raw_min'])==type(row['raw_max'])==int and row['raw_min']<row['raw_max'],'ADC_RANGE_SCHEMA')
        configs.append((row['raw_channel'],int(aa*scale),int(bb*scale),scale//denom,scale,row['raw_min'],row['raw_max'],bounds['amplitude_bound'],base,derivative,aa,bb))
    clock=cal['clock'];tick_scale=rational(clock['model_time_per_tick']);need(tick_scale>0,'CLOCK_SCALE')
    origin_error=rational(clock['origin_error'],True);rate_error=rational(clock['error_per_tick'],True)
    need(rate_error<tick_scale,'CLOCK_RATE_INTERVAL_NOT_POSITIVE')
    jitter=rational(clock['jitter_error'],True);quant=rational(clock['timestamp_quantization_error'],True)
    skew=rational(clock['channel_skew_error'],True)
    origins=c['nominal_tick_origins'];step=c['nominal_tick_step']
    need(isinstance(origins,list) and len(origins)==p and all(type(z)==int for z in origins) and type(step)==int and step>0,'NOMINAL_TIMING')
    vlo,vhi=clock['valid_tick_range'];need(type(vlo)==type(vhi)==int and vlo<vhi,'CLOCK_DOMAIN_SCHEMA')
    sums=[0]*62;sumdt=F(0);sumdt2=F(0);maxdt=F(0);last=None
    consumed={key:hashlib.sha256() for key in ['raw_adc','prediction','timestamps']}
    with paths['raw_adc'].open('rb') as raw,paths['prediction'].open('rb') as pred,paths['timestamps'].open('rb') as ts:
        for index in range(nvec):
            prep,k=divmod(index,t);tb=ts.read(8);consumed['timestamps'].update(tb);tick=struct.unpack('<q',tb)[0]
            need(vlo<=tick<=vhi,'CLOCK_DOMAIN');need(k==0 or tick>last,'NONMONOTONE_TIMESTAMPS');last=tick
            dt=abs(tick-(origins[prep]+k*step))*tick_scale+origin_error+abs(tick)*rate_error+jitter+quant+skew
            sumdt+=dt;sumdt2+=dt*dt;maxdt=max(maxdt,dt)
            rb=raw.read(62*8);pb=pred.read(62*8);consumed['raw_adc'].update(rb);consumed['prediction'].update(pb)
            z=struct.unpack('<62q',rb);prediction=struct.unpack('<62q',pb)
            for ch,conf in enumerate(configs):
                j,aa,bb,dd,scale,lo,hi,A,base,L,af,bf=conf
                need(lo<z[j]<hi,'ADC_RAIL_OR_RANGE')
                need(abs(af*z[j]+bf)<=A+base+L*dt,'AMPLITUDE_DOMAIN_INCONSISTENT')
                rn=aa*z[j]+bb-dd*prediction[ch];sums[ch]+=rn*rn
    r2=sum((F(s,conf[4]**2) for s,conf in zip(sums,configs)),F(0))
    alpha2=nvec*base2+2*baseL*sumdt+L2*sumdt2
    vector2=base2+2*baseL*maxdt+L2*maxdt*maxdt
    r=ar(r2).sqrt();alpha=ar(alpha2).sqrt();lo=r-alpha;hi=r+alpha
    lower=max(arb(0),lo)
    status='CONDITIONAL_CONSISTENCY' if hi<=ar(cap) else 'CONTRACT_CONTRADICTION' if lower>ar(cap) else 'HOLD_OVERLAPPING_ENCLOSURE'
    # Files must remain byte-identical across the numerical scan.
    for key,h in consumed.items():need(h.hexdigest()==packet['files'][key]['sha256'],'CONSUMED_BYTES_HASH_'+key)
    for key,f in paths.items():need(digest(f)==packet['files'][key]['sha256'],'INPUT_CHANGED_DURING_SCAN')
    need(digest(cp)==expected_contract_sha and (root/'PACKET.json').read_bytes()==packet_bytes,'METADATA_CHANGED_DURING_SCAN')
    return {'status':status,'raw_scalar_readings_checked':nvec*62,'timestamp_vectors_checked':nvec,
        'residual_F_squared_exact':pair(r2),'acquisition_F_squared_exact':pair(alpha2),
        'max_vector_error_squared_exact':pair(vector2),'max_timing_error_exact':pair(maxdt),
        'mismatch_lower':endpoint(lower,True),'mismatch_upper':endpoint(hi),'cap':pair(cap),
        'physical_verdict':'HOLD_UNQUALIFIED','physical_promotion':0,
        'calibration_authenticity':'NOT_AUTHENTICATED','declared_lineage_only':True,
        'heldout_independence':'NOT_CERTIFIED','unaliased_identification':'NOT_CERTIFIED',
        'provenance_kind':packet['provenance_kind'], 'source_family_membership':'NOT_CERTIFIED',
        'prediction_target':'frozen_saved_predictor_not_ideal_analytic_source',
        'scope':'Exact record arithmetic conditional on supplied deterministic calibration/domain/chronology/lineage premises. Not empirical calibration truth, external review or physical qualification.'}
def verify(root,expected_contract_sha):
    try:return _verify(root,expected_contract_sha)
    except (Hold,KeyError,TypeError,ValueError,AttributeError,ZeroDivisionError,OSError,struct.error) as e:
        reason=str(e) if isinstance(e,Hold) else 'MALFORMED_OR_MISSING_EVIDENCE'
        return {'status':'HOLD_INPUT_EVIDENCE','reason':reason,'physical_verdict':'HOLD_UNQUALIFIED','physical_promotion':0}
if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('bundle');ap.add_argument('--expected-contract-sha256',required=True)
    args=ap.parse_args();print(json.dumps(verify(args.bundle,args.expected_contract_sha256),indent=2))
