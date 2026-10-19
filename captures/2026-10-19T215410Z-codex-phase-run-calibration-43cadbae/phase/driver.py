"""PR246 exact four-case recipes. Global full-data freeze precedes every fit."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from common import P,sha,freeze
import recipes
SHAPE=(37,8191,62);SIZE=150321232

def nominal(Y,M,D,a,start,stop):
    # Object-array entries and coefficients are Python arbitrary-precision ints.
    # This is exactly sum_j M[a,j]*int(Y[j,k,c]), followed by ONE round_ratio.
    active=[j for j in range(37) if M[a][j]];assert 1<=len(active)<=2
    N=sum(int(M[a][j])*np.array(Y[j,start:stop],dtype=object) for j in active)
    assert all(isinstance(x,int) for x in N.flat)
    Q=N//int(D);R=N-Q*int(D);V=Q+((2*R>D)|((2*R==D)&(Q%2!=0)))
    assert all(-(1<<63)<int(x)<(1<<63) for x in V.flat)
    return np.array(V,dtype=np.int64)

def profile(case):
    # noise_value depends on a only through the frozen channel/sign table.
    s=int(case['spatial'][0]['sign']);out=[]
    for k in range(8191):
        c,v=recipes.noise_value(case,0,k);assert c==case['spatial'][0]['channel'];out.append(int(v)*s)
    return np.array(out,np.int64)

def generate(baseline,case,raw):
    f=freeze();C=json.loads((P/'CONTRACT.json').read_text());assert sha(baseline)==C['expected_synthetic_baseline_sha256'];assert Path(baseline).stat().st_size==SIZE
    Y=np.memmap(baseline,dtype='<i8',mode='r',shape=SHAPE);prep=next(r for r in C['preparations'] if r['id']==case['preparation_id']);M=prep['matrix_numerator'];D=prep['denominator'];assert D==(1<<44)+1
    assert recipes.matmul(M,[list(x) for x in zip(*M)])==[[D*D*int(i==j) for j in range(37)] for i in range(37)]
    assert all(i%2==j%2 for i in range(37) for j in range(37) if M[i][j])
    assert case==next(r for r in C['cases'] if r['case']==case['case']);limit=int(case['integer_noise_absolute_max']);assert limit in [0,1127]
    T=profile(case);assert np.all(abs(T)<=limit);assert case['case'] in f['case_order']
    with Path(raw).open('r+b') as fp:fp.truncate(SIZE)
    Z=np.memmap(raw,dtype='<i8',mode='r+',shape=SHAPE);nomh=hashlib.sha256();checked=0;vectors=0;maximum=0;normmax=0
    for a in range(37):
        row=case['spatial'][a];assert row['preparation']==a and row['sign'] in [-1,1] and 0<=row['channel']<62
        for start in range(0,8191,128):
            stop=min(start+128,8191);N=nominal(Y,M,D,a,start,stop);nomh.update(N.astype('<i8').tobytes());assert max(abs(int(N.min())),abs(int(N.max())))+1127<2**63
            V=N.copy();wanted=int(row['sign'])*T[start:stop];V[:,row['channel']]+=wanted;Z[a,start:stop]=V
            # Check the bytes actually stored, every scalar and every vector.
            diff=np.array(Z[a,start:stop],np.int64)-N;W=np.zeros_like(diff);W[:,row['channel']]=wanted;assert np.array_equal(diff,W)
            sq=(diff*diff).sum(axis=1);assert np.array_equal(sq,wanted*wanted) and np.all(sq<=limit**2)
            checked+=diff.size;vectors+=len(sq);normmax=max(normmax,int(sq.max()));maximum=max(maximum,abs(int(V.min())),abs(int(V.max())))
    Z.flush();del Y,Z;assert checked==18790154 and vectors==303067
    from estimator import project
    N,pr=project(raw);del N
    return {'case':case['case'],'preparation_id':case['preparation_id'],'noise_kind':case['noise_kind'],'record_sha256':sha(raw),'nominal_sha256':nomh.hexdigest(),'baseline_sha256':C['expected_synthetic_baseline_sha256'],'bytes':SIZE,'raw_quantum':[1,1<<48],'noise_reference':'ONE-rounded NEW exact rational preparation, not old anchor','delta_per_62_vector_upper':case['per62_vector_noise_norm_upper'],'maximum_squared_integer_vector_noise':normmax,'temporal_profile_sha256':hashlib.sha256(T.astype('<i8').tobytes()).hexdigest(),'vectors_checked':vectors,'scalars_checked':checked,'max_absolute_raw_integer':maximum,'projection':pr,'protocol_sha256':sha(P/'PROTOCOL_FREEZE.json'),'physical_promotion':0}

def memrecord(baseline,case):
    fd=os.memfd_create('UD_'+case['case'],flags=0);raw=Path('/proc/self/fd')/str(fd)
    try:r=generate(baseline,case,raw)
    except BaseException:os.close(fd);raise
    return fd,raw,r

def freeze_data(baseline):
    f=freeze();C=json.loads((P/'CONTRACT.json').read_text());assert not(P/'DATA_FREEZE.json').exists();rows=[]
    assert [c['case'] for c in C['cases']]==f['case_order'] and len(C['cases'])==4
    try:
        for case in C['cases']:
            fd,raw,r=memrecord(baseline,case)
            try:rows.append(r);print(json.dumps({'stage':'pre_fit_complete_raw_and_projection','case':r['case'],'raw_sha256':r['record_sha256']}),flush=True)
            finally:os.close(fd)
    except Exception as exc:
        hold={'status':'GLOBAL_DATA_HOLD_ZERO_FITS','completed_records':rows,'error':{'type':type(exc).__name__,'message':str(exc)},'estimator_calls':0,'physical_promotion':0};(P/'DATA_HOLD.json').write_text(json.dumps(hold,indent=2)+'\n');raise
    assert rows[0]['nominal_sha256']==rows[1]['nominal_sha256'] and rows[2]['nominal_sha256']==rows[3]['nominal_sha256']
    out={'status':'ALL_FOUR_RAW_HASHES_FULL_ELIGIBILITY_AND_EXACT_PROJECTIONS_FROZEN_BEFORE_FIRST_FIT','completed_utc':datetime.now(timezone.utc).isoformat(),'records':rows,'protocol_sha256':sha(P/'PROTOCOL_FREEZE.json'),'estimator_calls_before_freeze':0,'physical_promotion':0}
    (P/'DATA_FREEZE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'stage':'all_data_frozen','sha256':sha(P/'DATA_FREEZE.json')}),flush=True)

def fit_all(baseline):
    f=freeze();assert not(P/'DATA_HOLD.json').exists();d=json.loads((P/'DATA_FREEZE.json').read_text());C=json.loads((P/'CONTRACT.json').read_text());assert d['protocol_sha256']==sha(P/'PROTOCOL_FREEZE.json') and [r['case'] for r in d['records']]==f['case_order'] and len(d['records'])==4;assert not(P/'RUN_EXECUTIONS.json').exists()
    from estimator import estimate
    rows=[]
    for case,record in zip(C['cases'],d['records']):
        fd,raw,fresh=memrecord(baseline,case)
        try:
            assert fresh==record;run=estimate(raw,record);rows.append(run)
            assert run['projection'] is None or run['projection']==record['projection']
            for n in run['numeric_witnesses']:assert (P/'results'/run['case']/n).stat().st_size<10*1024*1024
            (P/'PARTIAL_EXECUTION_RECEIPT.json').write_text(json.dumps({'completed_cases':[x['case'] for x in rows],'completed_estimator_calls':len(rows),'no_retry_or_retuning':True,'physical_promotion':0},indent=2)+'\n')
        finally:os.close(fd)
    (P/'RUN_EXECUTIONS.json').write_text(json.dumps({'status':'ALL_FOUR_FROZEN_ESTIMATOR_OUTCOMES_RETAINED','rows':rows,'planned_and_actual_estimator_runs':4,'data_freeze_sha256':sha(P/'DATA_FREEZE.json'),'physical_promotion':0},indent=2)+'\n')

def replay_raw(baseline):
    f=freeze();d=json.loads((P/'DATA_FREEZE.json').read_text());C=json.loads((P/'CONTRACT.json').read_text());assert len(C['cases'])==len(d['records'])==4;rows=[]
    for case,record in zip(C['cases'],d['records']):
        fd,raw,fresh=memrecord(baseline,case)
        try:assert fresh==record;rows.append({'case':record['case'],'raw_nominal_eligibility_and_projection_exactly_reproduced':True,'projection_entries_checked':8191*321,'scalar_differences_checked':18790154,'vector_norms_checked':303067})
        finally:os.close(fd)
    out={'status':'PASS_FULL_FOUR_RECORD_REGENERATION_AND_EXACT_PROJECTION_REPLAY','rows':rows,'new_estimator_calls':0,'data_freeze_sha256':sha(P/'DATA_FREEZE.json'),'physical_promotion':0};(P/'RAW_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['generate','fit','replay']);p.add_argument('--baseline',required=True);x=p.parse_args();{'generate':freeze_data,'fit':fit_all,'replay':replay_raw}[x.mode](x.baseline)
