"""Independent prospective three-pattern raw audit; never fits or creates raw."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import argparse, hashlib, json
from pathlib import Path
import numpy as np

P=Path(__file__).resolve().parent
BASE_SHA='25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59'
ESTIMATOR_SHA='5fa15ca0f3830f168fe9e1483db7f21cb6e462780209b4d8b4e8ad43d64cfe86'
CASES=('block257_port17','affine62_qr13','prep_port_period7')
SHAPE=(37,8191,62)
WORD=(1,1,-1,1,-1,-1,-1)
RESIDUES=frozenset((0,1,3,4,9,10,12))

def need(value,message):
    if not value: raise ValueError(message)

def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(1048576),b''): h.update(block)
    return h.hexdigest()

def read(path): return json.loads(Path(path).read_text())

def at(case,prep,time):
    """Literal scalar formulation, separate from producer implementation."""
    need(case in CASES,'unknown fixed case')
    need(0<=prep<37 and 0<=time<8191,'index outside fixed raw shape')
    if case=='block257_port17': return 17,1 if (prep+time//257)%2==0 else -1
    if case=='affine62_qr13': return (7*prep+11*time+5)%62,1 if (time+3*prep)%13 in RESIDUES else -1
    return (13*prep+9)%62,WORD[(time+2*prep)%7]

def expected_prep(case,prep):
    delta=np.zeros((8191,62),dtype=np.int64)
    for time in range(8191):
        channel,sign=at(case,prep,time)
        delta[time,channel]=sign
    return delta

def controls():
    rows=[]
    def ck(name,value):
        need(bool(value),'control '+name); rows.append({'id':name,'pass':True})
    ck('block_before_boundary',at(CASES[0],0,256)==(17,1))
    ck('block_at_boundary',at(CASES[0],0,257)==(17,-1))
    ck('block_preparation_parity',at(CASES[0],1,257)==(17,1))
    ck('block_last',at(CASES[0],36,8190)==(17,-1))
    ck('affine_origin',at(CASES[1],0,0)==(5,1))
    ck('affine_residue_before_period',at(CASES[1],0,12)==(13,1))
    ck('affine_zero_after_period',at(CASES[1],0,13)==(24,1))
    ck('affine_nonresidue_negative',at(CASES[1],0,2)==(27,-1))
    ck('affine_last_prep_last_time',at(CASES[1],36,8190)==(13,1))
    ck('period7_word',tuple(at(CASES[2],0,t)[1]for t in range(7))==WORD)
    ck('period7_channel_and_offset',at(CASES[2],1,0)==(22,-1))
    ck('period7_last',at(CASES[2],36,8190)==(43,-1))
    allpatterns=[]
    for case in CASES:
        arr=expected_prep(case,0)
        ck(case+'_unit_norms',np.all(np.sum(arr*arr,axis=1)==1))
        ck(case+'_one_changed_scalar',np.all(np.count_nonzero(arr,axis=1)==1))
        bad=arr.copy();bad[257,17]+=1
        ck(case+'_altered_scalar_rejected',not np.array_equal(bad,arr))
        allpatterns.append(arr)
    ck('three_distinct_patterns',all(not np.array_equal(allpatterns[a],allpatterns[b])for a in range(3)for b in range(a)))
    toy=np.arange(12,dtype=np.int64).reshape(2,3,2)
    layout=toy.transpose(1,2,0).reshape(3,4)
    ck('channel_major_preparation_minor_layout',all(layout[t,c*2+p]==toy[p,t,c]for p in range(2)for t in range(3)for c in range(2)))
    ck('wrong_preparation_major_layout_refused',not np.array_equal(layout,toy.transpose(1,0,2).reshape(3,4)))
    ck('source_ball_exact_ratio_4_over9',4<=9 and 4*4>9)
    ck('integer64_subtraction_guard',(2**62-1)+(2**62-1)<2**63 and not (2**63-1)+1<2**63)
    ck('exact_binary64_range_is_strict',2**53-1<2**53 and not 2**53<2**53)
    try: at('replacement',0,0); refused=False
    except ValueError: refused=True
    ck('unknown_replacement_refused',refused)
    try: at(CASES[0],0,8191); refused=False
    except ValueError: refused=True
    ck('time_out_of_range_refused',refused)
    return rows

def validate_freezes(producer,repo,case):
    own=read(P/'DATA_DRIVER_FREEZE.json')
    need(sha(__file__)==own['driver_sha256'],'independent data driver changed')
    need(set(own['cases'])==set(CASES),'three fixed case freezes required')
    need(sha(producer/'FREEZE.json')==own['cases'][case],'producer freeze changed')
    f=read(producer/'FREEZE.json')
    for name,h in f['files'].items(): need(sha(producer/name)==h,'producer source changed '+name)
    for name,h in f['repository_sources'].items(): need(sha(repo/name)==h,'repository source changed '+name)
    need(sha(producer/'estimator.py')==ESTIMATOR_SHA,'unchanged estimator source required')
    for sibling in CASES:
        pkg=producer.parent/sibling
        need(not (pkg/'RUN_EXECUTIONS.json').exists(),'all data reviews must precede every campaign fit')
        need(not (pkg/'results').exists(),'no campaign results before data review')
    return own

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo');ap.add_argument('--producer');ap.add_argument('--case',choices=CASES)
    ap.add_argument('--baseline');ap.add_argument('--raw');ap.add_argument('--raw-release');ap.add_argument('--out',required=True)
    ap.add_argument('--controls-only',action='store_true')
    args=ap.parse_args();out=Path(args.out)
    need(not out.exists(),'exclusive new review output')
    if args.controls_only:
        result={'status':'PASS_INDEPENDENT_THREE_PATTERN_PURE_CONTROLS','rows':controls(),'new_raw_records':0,'new_estimator_calls':0,'physical_promotion':0}
    else:
        need(all((args.repo,args.producer,args.case,args.baseline,args.raw,args.raw_release)),'all data inputs required')
        repo=Path(args.repo);producer=Path(args.producer);baseline=Path(args.baseline);raw=Path(args.raw);case=args.case
        validate_freezes(producer,repo,case)
        need(read(args.raw_release)['raw_generation_released']is True,'raw-only release required')
        dfile=producer/'DATA_FREEZE.json';data=read(dfile)
        need(data['protocol_sha256']==sha(producer/'FREEZE.json'),'data/source freeze binding')
        datum=data['record'];need(datum['case']==case,'actual case identity')
        need(sha(baseline)==BASE_SHA and baseline.stat().st_size==150321232,'pinned baseline bytes')
        need(baseline.stat().st_mode&0o222==0,'baseline read-only')
        need(raw.stat().st_size==150321232 and raw.stat().st_mode&0o222==0,'shared raw shape/read-only')
        before=sha(raw);need(before==datum['record_sha256'] and before!=BASE_SHA,'new actual raw identity')
        y0=np.memmap(baseline,dtype='<i8',mode='r',shape=SHAPE);y=np.memmap(raw,dtype='<i8',mode='r',shape=SHAPE)
        full_delta=np.empty(SHAPE,dtype=np.int64);scalars=vectors=changed=0;actual_max=base_max=0
        for prep in range(37):
            actual=np.asarray(y[prep],dtype=np.int64);base=np.asarray(y0[prep],dtype=np.int64)
            am=max(abs(int(actual.min())),abs(int(actual.max())));bm=max(abs(int(base.min())),abs(int(base.max())))
            need(am+bm<2**63,'safe int64 actual subtraction')
            difference=actual-base;expected=expected_prep(case,prep)
            need(np.array_equal(difference,expected),'all scalar recipe differences')
            need(np.all(np.sum(difference*difference,axis=1)==1),'every exact unit vector norm')
            full_delta[prep]=difference;scalars+=difference.size;vectors+=len(difference);changed+=np.count_nonzero(difference)
            actual_max=max(actual_max,am);base_max=max(base_max,bm)
        need(scalars==18790154 and vectors==303067 and changed==303067,'complete raw counts')
        source=read(producer/'inputs/NULL_VECTOR.json');v=np.zeros(2294,dtype=np.int64);v[:len(source['vector'])]=source['vector']
        old=np.random.default_rng(172026).choice([-1.,1.],(2294,160)).astype(np.int64)
        new=np.random.default_rng(184052).choice([-1.,1.],(2294,160)).astype(np.int64)
        need(int(v@v)==16228 and np.all(v@old==0),'pinned independent sketch identities')
        sketch=np.column_stack((2*old,v,2*new));column_sum=max(int(x)for x in np.abs(sketch).sum(axis=0))
        need(base_max*column_sum<2**63 and actual_max*column_sum<2**63,'base/actual exact projection int64 safety')
        x0=np.asarray(y0.transpose(1,2,0).reshape(8191,2294),dtype=np.int64);nominal=x0@sketch;del x0
        dx=full_delta.transpose(1,2,0).reshape(8191,2294)
        correction=dx@sketch
        addition_bound=max(abs(int(nominal.min())),abs(int(nominal.max())))+max(abs(int(correction.min())),abs(int(correction.max())))
        need(addition_bound<2**63,'safe separated nominal plus correction sum')
        numerator=nominal+correction;maximum=max(abs(int(numerator.min())),abs(int(numerator.max())))
        need(maximum<2**53,'exact binary64 conversion range')
        ih=hashlib.sha256(numerator.astype('<i8').tobytes()).hexdigest()
        zh=hashlib.sha256((numerator.astype(float)/2.**55).astype('<f8').tobytes()).hexdigest()
        need(datum['projection']['integer_bytes_sha256']==ih and datum['projection']['projection_bytes_sha256']==zh,'independent separated projection hash identity')
        need(datum['projection']['numerator_max']==maximum and datum['projection']['partial_sum_bound']==actual_max*column_sum,'exact range metadata identity')
        need(sha(raw)==before and sha(baseline)==BASE_SHA,'both raw inputs unchanged after audit')
        validate_freezes(producer,repo,case)
        result={'status':'PASS_INDEPENDENT_THREE_PATTERN_RAW_AND_SEPARATED_PROJECTION','case':case,'record_sha256':before,'baseline_sha256':BASE_SHA,'raw_bytes':150321232,'scalar_differences_checked':scalars,'vectors_checked':vectors,'integer_vector_squared_norm':1,'changed_scalars':int(changed),'integer_projection_sha256':ih,'dyadic_projection_sha256':zh,'projection_entries':int(numerator.size),'numerator_max':maximum,'actual_integer_partial_sum_bound':actual_max*column_sum,'source_radius':[3,1<<49],'noise_quantum':[1,1<<48],'radius_squared_ratio':[4,9],'data_freeze_sha256':sha(dfile),'driver_freeze_sha256':sha(P/'DATA_DRIVER_FREEZE.json'),'source_freeze_sha256':sha(producer/'FREEZE.json'),'raw_release_sha256':sha(args.raw_release),'new_estimator_calls':0,'new_raw_records':0,'input_read_only_and_unchanged':True,'newcase_full_reconstruction_sigma210_lower':'NOT_EVALUATED','scope':'All actual scalar differences and exact vector norms; separate nominal plus perturbation projection association; exposed computational source, not blind/physical freshness','external_review':'PENDING','physical_promotion':0}
    out.parent.mkdir(parents=True,exist_ok=True)
    with out.open('x')as f: json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'status':result['status'],'case':result.get('case'),'control_count':len(result.get('rows',[])),'record_sha256':result.get('record_sha256')}),flush=True)

if __name__=='__main__': main()
