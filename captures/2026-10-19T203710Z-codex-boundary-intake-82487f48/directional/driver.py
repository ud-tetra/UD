"""Four frozen directional amplitudes; complete data freeze precedes ALL fits."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from common import P,sha,freeze
SHAPE=(37,8191,62);SIZE=150321232
def generate(baseline,amp,raw):
    f=freeze();assert amp in f['amplitudes'];assert sha(baseline)==f['baseline_sha256']
    Y=np.memmap(baseline,dtype='<i8',mode='r',shape=SHAPE)
    row=next(r for r in json.loads((P/'inputs/ANCHOR_DATA.json').read_text())['records'] if r['case']=='reverse_stationary')
    M=np.array(row['transform_integer_matrix'],np.int64);assert row['transform_denominator']==1
    assert np.array_equal(M@M.T,np.eye(37,dtype=np.int64)) and np.all(np.count_nonzero(M,axis=1)==1)
    assert all(i%2==j%2 for i,j in zip(*np.nonzero(M)))
    family=json.loads((P/'inputs/FAMILY_CERTIFICATE.json').read_text());assert family['delta_per_62_vector']==[1127,1<<48] and 0<=amp<=1127
    s=json.loads((P/'inputs/SPATIAL_SELECTION.json').read_text());ch=np.array(s['channels']);sg=np.array(s['signs']);assert np.all(abs(sg)==1) and np.all((0<=ch)&(ch<62))
    with Path(raw).open('r+b') as fp:fp.truncate(SIZE)
    Z=np.memmap(raw,dtype='<i8',mode='r+',shape=SHAPE);t=np.arange(8191);alt=np.where(t%2==0,1,-1);nomh=hashlib.sha256()
    for a in range(37):
        b=int(np.flatnonzero(M[a])[0]);nom=int(M[a,b])*np.array(Y[b],np.int64);nomh.update(nom.astype('<i8').tobytes());assert max(abs(int(nom.min())),abs(int(nom.max())))+amp<2**63
        nom[t,ch[a]]+=amp*sg[a]*alt;Z[a]=nom
    Z.flush();del Z;Z=np.memmap(raw,dtype='<i8',mode='r',shape=SHAPE);checked=0;maximum=0
    for a in range(37):
        b=int(np.flatnonzero(M[a])[0]);diff=np.array(Z[a])-int(M[a,b])*np.array(Y[b],np.int64);wanted=np.zeros_like(diff);wanted[t,ch[a]]=amp*sg[a]*alt
        assert np.array_equal(diff,wanted) and np.all((diff*diff).sum(axis=1)==amp**2);checked+=diff.size;maximum=max(maximum,abs(int(Z[a].min())),abs(int(Z[a].max())))
    del Y,Z;assert checked==18790154 and nomh.hexdigest()==row['nominal_sha256']
    return {'case':f'directional_amp_{amp}','integer_amplitude':amp,'record_sha256':sha(raw),'nominal_sha256':nomh.hexdigest(),'baseline_sha256':f['baseline_sha256'],'bytes':SIZE,'anchor':'reverse_stationary','anchor_nominal_hash_matched':True,'rho_distance_to_exact_anchor':[0,1],'raw_quantum':[1,1<<48],'delta_per_62_vector':[amp,1<<48],'per_vector_squared_integer_noise':amp**2,'vectors_checked':303067,'scalars_checked':checked,'max_absolute_raw_integer':maximum,'protocol_sha256':sha(P/'PROTOCOL_FREEZE.json'),'physical_promotion':0}
def memrecord(baseline,amp):
    fd=os.memfd_create(f'UD_directional_{amp}',flags=0);raw=Path('/proc/self/fd')/str(fd)
    try:r=generate(baseline,amp,raw)
    except BaseException:os.close(fd);raise
    return fd,raw,r
def freeze_data(baseline):
    f=freeze();assert not(P/'DATA_FREEZE.json').exists();rows=[]
    for amp in f['amplitudes']:
        fd,raw,r=memrecord(baseline,amp)
        try:rows.append(r);print(json.dumps({'stage':'pre_fit_raw_hash','amplitude':amp,'raw_sha256':r['record_sha256']}),flush=True)
        finally:os.close(fd)
    out={'status':'ALL_FOUR_RAW_HASHES_AND_EXACT_ELIGIBILITY_FROZEN_BEFORE_FIRST_FIT','completed_utc':datetime.now(timezone.utc).isoformat(),'records':rows,'protocol_sha256':sha(P/'PROTOCOL_FREEZE.json'),'physical_promotion':0}
    (P/'DATA_FREEZE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'stage':'all_data_frozen','sha256':sha(P/'DATA_FREEZE.json')}),flush=True)
def fit_all(baseline):
    f=freeze();d=json.loads((P/'DATA_FREEZE.json').read_text());assert d['protocol_sha256']==sha(P/'PROTOCOL_FREEZE.json') and [r['integer_amplitude'] for r in d['records']]==f['amplitudes'];assert not(P/'RUN_EXECUTIONS.json').exists()
    from estimator import estimate,project
    rows=[];projections=[]
    for record in d['records']:
        fd,raw,fresh=memrecord(baseline,record['integer_amplitude'])
        try:
            assert fresh==record
            run=estimate(raw,record);rows.append(run)
            if run['projection'] is not None:
                N,receipt=project(raw);assert receipt==run['projection'];projections.append({'case':run['case'],'projection_entries_recomputed':int(N.size),'projection':receipt,'raw_sha256':sha(raw)});del N
            else:projections.append({'case':run['case'],'status':'HOLD_NO_PROJECTION_OUTPUT','new_estimator_runs':0})
            # Per-case RUN and witnesses are already retained by unchanged estimator.
            (P/'PARTIAL_EXECUTION_RECEIPT.json').write_text(json.dumps({'completed_cases':[x['case'] for x in rows],'completed_estimator_calls':len(rows),'no_retry_or_retuning':True,'physical_promotion':0},indent=2)+'\n')
        finally:os.close(fd)
    (P/'RUN_EXECUTIONS.json').write_text(json.dumps({'status':'ALL_FOUR_FROZEN_ESTIMATOR_OUTCOMES_RETAINED','rows':rows,'planned_and_actual_estimator_runs':4,'data_freeze_sha256':sha(P/'DATA_FREEZE.json'),'physical_promotion':0},indent=2)+'\n')
    (P/'PROJECTION_REPLAYS.json').write_text(json.dumps({'rows':projections,'new_estimator_runs':0,'physical_promotion':0},indent=2)+'\n')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['generate','fit']);p.add_argument('--baseline',required=True);a=p.parse_args()
    freeze_data(a.baseline) if a.mode=='generate' else fit_all(a.baseline)
