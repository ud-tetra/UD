"""Deterministic tiny ADC evidence controls; no physical data or fitted truths."""
import copy,json,hashlib,struct,zipfile,io
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent
def jb(x):return (json.dumps(x,indent=2)+'\n').encode()
def sha(b):return hashlib.sha256(b).hexdigest()
def pack(values):return struct.pack('<'+str(len(values))+'q',*values)
def base():
    channel=[]
    for ch in range(62):
        row={'coordinate':ch,'raw_channel':ch,'sign':1,'applied_gain':[32,1],'applied_offset':[0,1],'raw_min':-32768,'raw_max':32767}
        row.update({k:[0,1] for k in ['gain_error','offset_error','adc_error','processing_error','nonlinearity_error','crosstalk_error','filter_tail_error','derivative_bound']})
        row['amplitude_bound']=[4,1]
        if ch==0:row['adc_error']=[1,32]
        channel.append(row)
    cal={'coordinate_unit':'model_coordinate','time_unit':'model_time','adc_unit':'ADC_code','coverage':'deterministic_uniform','calibrator':'fixture-calibrator','constructor':'fixture-constructor','frozen_utc':'2026-10-01T00:00:00Z','valid_from_utc':'2026-10-01T00:00:00Z','valid_until_utc':'2026-10-31T00:00:00Z','source_ids':['toy-calibration-run'],'channels':channel,'filter_evidence_id':'synthetic-filter-assumption','clock':{'model_time_per_tick':[1,32],'origin_error':[0,1],'error_per_tick':[0,1],'jitter_error':[0,1],'timestamp_quantization_error':[0,1],'channel_skew_error':[0,1],'valid_tick_range':[-100,100]}}
    raw=[8 if i%62==0 else 0 for i in range(8*62)]
    prediction=[1024 if i%62==0 else 0 for i in range(8*62)]
    c={'version':'ADC_RECORD_CONTRACT_v0.1','channels':62,'preparations':2,'times':4,'coordinate_unit':'model_coordinate','time_unit':'model_time','mismatch_F_cap':[1,16],'frozen_utc':'2026-10-02T00:00:00Z','time_treatment':'acquisition_uncertainty','model_source_ids':['toy-fixed-model-run'],'prediction_denominator':4096,'nominal_tick_origins':[0,0],'nominal_tick_step':1,'frequency_band_model_radians':[[0,1],[1,1]],'band_evidence_id':'synthetic-band-assumption'}
    packet={'provenance_kind':'synthetic_fixture','acquisition_start_utc':'2026-10-03T00:00:00Z','acquisition_end_utc':'2026-10-03T00:01:00Z','data_freeze_utc':'2026-10-03T00:02:00Z','validation_source_ids':['toy-validation-run'],'unaliased_identification':False}
    cal['raw_dependency_sha256']=['1'*64];c['model_raw_dependency_sha256']=['2'*64];c['prediction_target']='frozen_saved_predictor'
    return {'cal':cal,'raw':raw,'prediction':prediction,'ticks':[0,1,2,3]*2,'contract':c,'packet':packet,'post':None,'exact_expectations':{}}
def build():
    cases=[]
    def add(name,expected,change=None):
        x=base()
        if change:change(x)
        cases.append((name,expected,x))
    add('consistent_exact_bytes','CONDITIONAL_CONSISTENCY')
    add('one_sample_model_contradiction','CONTRACT_CONTRADICTION',lambda x:x['raw'].__setitem__(0,24))
    add('overlapping_uncertainty','HOLD_OVERLAPPING_ENCLOSURE',lambda x:x['raw'].__setitem__(0,10))
    def equal(x):
        x['raw'][0]=10;x['cal']['channels'][0]['adc_error']=[0,1]
    add('exact_cap_equality','CONDITIONAL_CONSISTENCY',equal)
    def covariance(x):
        for i in range(8):x['raw'][i*62],x['raw'][i*62+1]=x['raw'][i*62+1],x['raw'][i*62]
        x['cal']['channels'][0]['raw_channel']=1;x['cal']['channels'][1]['raw_channel']=0
    add('channel_permutation_covariance','CONDITIONAL_CONSISTENCY',covariance)
    def wrong_map(x):
        for i in range(8):x['raw'][i*62],x['raw'][i*62+1]=x['raw'][i*62+1],x['raw'][i*62]
    add('unchanged_decoder_after_permutation','CONTRACT_CONTRADICTION',wrong_map)
    def timing(x):
        x['ticks']=[1,2,3,4]*2;x['cal']['channels'][0]['derivative_bound']=[1,1]
    add('timing_error_in_acquisition_budget','HOLD_OVERLAPPING_ENCLOSURE',timing)
    def mismatchtime(x):timing(x);x['contract']['time_treatment']='model_mismatch'
    add('timing_not_double_counted_as_noise','CONDITIONAL_CONSISTENCY',mismatchtime)
    def affine(x):
        x['cal']['channels'][0].update(applied_gain=[3,2],applied_offset=[1,2],amplitude_bound=[8,1],gain_error=[1,1024],offset_error=[1,256],adc_error=[1,128],processing_error=[1,2048],nonlinearity_error=[1,4096],crosstalk_error=[1,8192],filter_tail_error=[1,16384])
        for i in range(8):x['prediction'][i*62]=5*4096
        e=8*F(685,49152)**2;x['exact_expectations']={'residual_F_squared_exact':[0,1],'acquisition_F_squared_exact':[e.numerator,e.denominator]}
    add('fractional_gain_offset_and_all_error_terms','CONDITIONAL_CONSISTENCY',affine)
    def sign(x):
        x['cal']['channels'][0]['sign']=-1
        for i in range(8):x['prediction'][i*62]=-1024
        x['exact_expectations']={'residual_F_squared_exact':[0,1],'acquisition_F_squared_exact':[1,131072]}
    add('negative_sign_covariance','CONDITIONAL_CONSISTENCY',sign)
    def varyingtime(x):
        x['ticks']=[0,2,4,6]*2;x['cal']['channels'][0]['derivative_bound']=[3,2]
        x['cal']['clock'].update(origin_error=[1,1024],error_per_tick=[1,4096],jitter_error=[1,8192],timestamp_quantization_error=[1,16384],channel_skew_error=[1,32768])
        e=2*sum((F(181+3120*k,65536)**2 for k in range(4)),F(0));v=F(9541,65536)**2
        x['exact_expectations']={'residual_F_squared_exact':[0,1],'acquisition_F_squared_exact':[e.numerator,e.denominator],'max_timing_error_exact':[3159,32768],'max_vector_error_squared_exact':[v.numerator,v.denominator]}
    add('nonconstant_clock_aggregate_exact','HOLD_OVERLAPPING_ENCLOSURE',varyingtime)
    add('duplicate_channel_refused','HOLD_INPUT_EVIDENCE',lambda x:x['cal']['channels'][1].update(raw_channel=0))
    add('negative_error_refused','HOLD_INPUT_EVIDENCE',lambda x:x['cal']['channels'][0].update(adc_error=[-1,1]))
    add('zero_gain_refused','HOLD_INPUT_EVIDENCE',lambda x:x['cal']['channels'][0].update(applied_gain=[0,1]))
    add('one_sigma_not_uniform_bound','HOLD_INPUT_EVIDENCE',lambda x:x['cal'].update(coverage='one_sigma'))
    add('wrong_calibration_units','HOLD_INPUT_EVIDENCE',lambda x:x['cal'].update(coordinate_unit='volts'))
    add('calibration_postdates_data','HOLD_INPUT_EVIDENCE',lambda x:x['cal'].update(frozen_utc='2026-10-04T00:00:00Z'))
    add('expired_calibration','HOLD_INPUT_EVIDENCE',lambda x:x['cal'].update(valid_until_utc='2026-10-02T00:00:00Z'))
    add('contract_postdates_data','HOLD_INPUT_EVIDENCE',lambda x:x['contract'].update(frozen_utc='2026-10-04T00:00:00Z'))
    add('shared_calibration_lineage','HOLD_INPUT_EVIDENCE',lambda x:x['packet'].update(validation_source_ids=['toy-calibration-run']))
    add('shared_model_lineage','HOLD_INPUT_EVIDENCE',lambda x:x['packet'].update(validation_source_ids=['toy-fixed-model-run']))
    add('same_declared_constructor_calibrator','HOLD_INPUT_EVIDENCE',lambda x:x['cal'].update(calibrator='fixture-constructor'))
    add('clipped_adc_rail','HOLD_INPUT_EVIDENCE',lambda x:x['raw'].__setitem__(0,32767))
    add('nonmonotone_timestamps','HOLD_INPUT_EVIDENCE',lambda x:x['ticks'].__setitem__(2,1))
    add('clock_outside_calibrated_domain','HOLD_INPUT_EVIDENCE',lambda x:x['ticks'].__setitem__(3,101))
    add('prediction_wrong_length','HOLD_INPUT_EVIDENCE',lambda x:x['prediction'].pop())
    add('raw_wrong_length','HOLD_INPUT_EVIDENCE',lambda x:x['raw'].pop())
    add('timestamp_wrong_length','HOLD_INPUT_EVIDENCE',lambda x:x['ticks'].pop())
    add('real_cap_unset','HOLD_INPUT_EVIDENCE',lambda x:x['contract'].update(mismatch_F_cap=None))
    add('malformed_lineage','HOLD_INPUT_EVIDENCE',lambda x:x['packet'].update(validation_source_ids='validation-string'))
    add('noninjective_alias_band','HOLD_INPUT_EVIDENCE',lambda x:(x['packet'].update(unaliased_identification=True),x['contract'].update(frequency_band_model_radians=[[0,1],[4,1]])))
    add('declared_injective_band_math_only','CONDITIONAL_CONSISTENCY',lambda x:x['packet'].update(unaliased_identification=True))
    add('invented_apparatus_receipts_still_no_physical_pass','CONDITIONAL_CONSISTENCY',lambda x:x['packet'].update(provenance_kind='apparatus_submission'))
    add('clock_rate_interval_reaches_zero','HOLD_INPUT_EVIDENCE',lambda x:x['cal']['clock'].update(error_per_tick=[1,32]))
    def huge(x):
        x['raw'][0]=1<<40;x['cal']['channels'][0].update(raw_min=-(1<<62),raw_max=1<<62,amplitude_bound=[1<<40,1])
        r=(F(1<<40,32)-F(1,4))**2;x['exact_expectations']={'residual_F_squared_exact':[r.numerator,r.denominator]}
    add('exact_squared_residual_exceeds_int64','CONTRACT_CONTRADICTION',huge)
    add('scored_raw_declared_model_ancestor','HOLD_INPUT_EVIDENCE',lambda x:x.update(post=('raw_ancestor',None)))
    add('path_escape_refused','HOLD_INPUT_EVIDENCE',lambda x:x.update(post=('path_escape',None)))
    add('unfilled_template_refused','HOLD_INPUT_EVIDENCE',lambda x:x.update(post=('template',None)))
    for key in ['raw_adc','timestamps','prediction','calibration']:
        add('hash_mutation_'+key,'HOLD_INPUT_EVIDENCE',lambda x,key=key:x.update(post=('hash',key)))
    add('frozen_model_hash_refused','HOLD_INPUT_EVIDENCE',lambda x:x.update(post=('model_hash',None)))
    add('frozen_calibration_hash_refused','HOLD_INPUT_EVIDENCE',lambda x:x.update(post=('calibration_hash',None)))
    add('frozen_contract_hash_refused','HOLD_INPUT_EVIDENCE',lambda x:x.update(post=('contract',None)))
    index=[];data={}
    for name,expected,x in cases:
        files={'adc.i64le':pack(x['raw']),'prediction.i64le':pack(x['prediction']),'timestamps.i64le':pack(x['ticks']),'CALIBRATION.json':jb(x['cal'])}
        c=x['contract'];packet=x['packet'];c['prediction_sha256']=sha(files['prediction.i64le']);c['calibration_sha256']=sha(files['CALIBRATION.json'])
        files['CONTRACT.json']=jb(c);expected_sha=sha(files['CONTRACT.json']);packet['contract_sha256']=expected_sha
        packet['files']={key:{'path':file,'sha256':sha(files[file])} for key,file in [('raw_adc','adc.i64le'),('prediction','prediction.i64le'),('timestamps','timestamps.i64le'),('calibration','CALIBRATION.json')]}
        if x['post']:
            kind,key=x['post']
            if kind=='hash':packet['files'][key]['sha256']='0'*64
            if kind=='model_hash':c['prediction_sha256']='0'*64
            if kind=='calibration_hash':c['calibration_sha256']='0'*64
            if kind=='raw_ancestor':c['model_raw_dependency_sha256']=[sha(files['adc.i64le'])]
            if kind in ['model_hash','calibration_hash','raw_ancestor']:
                files['CONTRACT.json']=jb(c);expected_sha=sha(files['CONTRACT.json']);packet['contract_sha256']=expected_sha
            if kind=='contract':expected_sha='0'*64
            if kind=='path_escape':packet['files']['raw_adc']['path']='../adc.i64le'
            if kind=='template':packet['files']=None
        files['PACKET.json']=jb(packet)
        for filename,content in files.items():data[name+'/'+filename]=content
        index.append({'id':name,'expected':expected,'expected_contract_sha256':expected_sha,'physical_expected':'HOLD_UNQUALIFIED','toy_shape':[2,4,62],'exact_expectations':x['exact_expectations']})
    return index,data
def generate(dest):
    dest=Path(dest);dest.mkdir(parents=True,exist_ok=False);index,data=build()
    # Stable zip metadata allows byte-identical rebuilding from the frozen generator.
    with zipfile.ZipFile(dest/'FIXTURES.zip','w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for name,b in sorted(data.items()):
            zi=zipfile.ZipInfo(name,(2026,10,1,0,0,0));zi.compress_type=zipfile.ZIP_DEFLATED;zi.external_attr=0o100644<<16;z.writestr(zi,b,compresslevel=9)
    (dest/'CONTROL_INDEX.json').write_bytes(jb(index))
    (dest/'DATA_FREEZE.json').write_bytes(jb({'status':'TINY_SYNTHETIC_BYTE_FIXTURES_FROZEN_BEFORE_EVALUATION','files':{'FIXTURES.zip':sha((dest/'FIXTURES.zip').read_bytes()),'CONTROL_INDEX.json':sha((dest/'CONTROL_INDEX.json').read_bytes())},'members':[{'path':n,'sha256':sha(b),'size_bytes':len(b)} for n,b in sorted(data.items())],'controls':len(index),'physical_acquisitions':0,'new_fits':0,'physical_promotion':0}))
    print(json.dumps({'controls':len(index),'zip_bytes':(dest/'FIXTURES.zip').stat().st_size,'members':len(data),'physical_acquisitions':0}))
if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);generate(ap.parse_args().out)
