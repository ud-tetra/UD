"""One source-selected encoded family member; no retry or parameter search."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from common import P,sha,freeze
SHAPE=(37,8191,62);SIZE=150321232;NAME='reverse_weakmode_alternating_1127'
BASE_SHA='25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59'

def prepare():
    """Freeze the chosen source-derived spatial table BEFORE any new raw record."""
    f=json.loads((P/'CODE_FREEZE.json').read_text())
    for n,h in f['files'].items():assert sha(P/n)==h,n
    for n,h in f['source_files'].items():assert sha(P.parent/n)==h,n
    from estimator import sketch
    with np.load(P.parent/f['right_factor_source'],allow_pickle=False) as z:
        s=z['singular'];vt=z['right_transpose'];assert vt.shape==(321,321) and s.shape==(321,)
        assert np.count_nonzero(s>2.**-24)==209;v=vt[208].copy()
    A=sketch();w=(A.astype(float)/128.)@v;grid=w.reshape(62,37)
    ch=np.argmax(abs(grid),axis=0);sg=np.where(grid[ch,np.arange(37)]>=0,1,-1)
    selection={'selection_rule':'binary64 (A/128)@saved_v209, max absolute per preparation, smallest-channel argmax, sign nonnegative -> +1',
               'channels':list(map(int,ch)),'signs':list(map(int,sg)),
               'time_sign':'(-1)^k; k=0..8190','integer_amplitude':1127,
               'right_factor_source':f['right_factor_source'],'known_outcomes':'Prior one-quantum finite outputs known; this amplified record and fit have never been generated; no success assumption.'}
    out=P/'SPATIAL_SELECTION.json';assert not out.exists();out.write_text(json.dumps(selection,indent=2)+'\n')
    sources=f['source_files'];files={**f['files'],'SPATIAL_SELECTION.json':sha(out),'CODE_FREEZE.json':sha(P/'CODE_FREEZE.json')}
    protocol={'status':'ONE_SOURCE_SELECTED_RECIPE_FROZEN_BEFORE_NEW_RAW_AND_SINGLE_ESTIMATOR_RUN',
              'frozen_utc':datetime.now(timezone.utc).isoformat(),'files':files,'source_files':sources,
              'reference_basis_sources':f['reference_basis_sources'],
              'baseline_sha256':BASE_SHA,'case':NAME,'anchor':'reverse_stationary','integer_amplitude':1127,
              'cutoff':[1,1<<24],'planned_estimator_runs':1,'no_retry_retuning_or_selection':True,
              'counterexample_target':'unchanged strict source-frame admission, not phase failure or all-estimator impossibility',
              'external_review':'PENDING','physical_promotion':0}
    q=P/'PROTOCOL_FREEZE.json';assert not q.exists();q.write_text(json.dumps(protocol,indent=2)+'\n')
    print(json.dumps({'status':protocol['status'],'protocol_sha256':sha(q),'selection_sha256':sha(out)}),flush=True)

def generate(baseline,raw):
    f=freeze();assert sha(baseline)==BASE_SHA;raw=Path(raw)
    family=json.loads((P/'inputs/FAMILY_CERTIFICATE.json').read_text())
    assert family['delta_per_62_vector']==[1127,1<<48] and family['rho']==[1,1<<20]
    memory_file=str(raw).startswith('/proc/self/fd/')
    assert memory_file or not raw.exists()
    if not memory_file:
        fs=os.statvfs(raw.parent);assert fs.f_bfree*fs.f_frsize>250_000_000,'HOLD insufficient root filesystem capacity before generation'
    Y=np.memmap(baseline,dtype='<i8',mode='r',shape=SHAPE)
    anchors=json.loads((P/'inputs/ANCHOR_DATA.json').read_text())['records'];row=next(r for r in anchors if r['case']=='reverse_stationary')
    M=np.array(row['transform_integer_matrix'],np.int64);assert row['transform_denominator']==1
    assert np.array_equal(M@M.T,np.eye(37,dtype=np.int64));assert all(i%2==j%2 for i,j in zip(*np.nonzero(M)))
    assert np.all(np.count_nonzero(M,axis=1)==1)
    S=json.loads((P/'SPATIAL_SELECTION.json').read_text());ch=np.array(S['channels']);sg=np.array(S['signs']);assert np.all(abs(sg)==1) and np.all((0<=ch)&(ch<62))
    t=np.arange(8191);time=np.where(t%2==0,1,-1);maximum=0;nomsha=hashlib.sha256()
    with raw.open('r+b' if memory_file else 'xb') as fp:fp.truncate(SIZE)
    Z=np.memmap(raw,dtype='<i8',mode='r+',shape=SHAPE)
    for a in range(37):
        b=int(np.flatnonzero(M[a])[0]);nom=int(M[a,b])*np.array(Y[b],np.int64);nomsha.update(nom.astype('<i8').tobytes())
        nominal_max=max(abs(int(nom.min())),abs(int(nom.max())));assert nominal_max+1127<2**63
        nom[t,ch[a]]+=1127*sg[a]*time;Z[a]=nom
    Z.flush();del Z
    Z=np.memmap(raw,dtype='<i8',mode='r',shape=SHAPE);checked=0
    for a in range(37):
        b=int(np.flatnonzero(M[a])[0]);nom=int(M[a,b])*np.array(Y[b],np.int64);diff=np.array(Z[a])-nom
        wanted=np.zeros_like(diff);wanted[t,ch[a]]=1127*sg[a]*time
        assert np.array_equal(diff,wanted) and np.all((diff*diff).sum(axis=1)==1127**2)
        checked+=diff.size;maximum=max(maximum,abs(int(Z[a].min())),abs(int(Z[a].max())))
    del Y,Z;assert checked==18790154 and nomsha.hexdigest()==row['nominal_sha256']
    receipt={'case':NAME,'record_sha256':sha(raw),'nominal_sha256':nomsha.hexdigest(),'bytes':SIZE,
             'baseline_sha256':BASE_SHA,'anchor':'reverse_stationary','anchor_nominal_hash_matched':True,
             'integer_amplitude':1127,'per_vector_squared_integer_noise':1127**2,'vectors_checked':303067,
             'scalars_checked':checked,'max_absolute_raw_integer':maximum,'rho_distance_to_exact_anchor':[0,1],
             'delta_per_62_vector':[1127,1<<48],'raw_quantum':[1,1<<48],
             'protocol_sha256':sha(P/'PROTOCOL_FREEZE.json'),'physical_promotion':0}
    out=P/'DATA_FREEZE.json';assert not out.exists();out.write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({'status':'COMPLETE_RAW_HASH_AND_EXACT_FAMILY_ELIGIBILITY_FROZEN_BEFORE_FIT','record_sha256':receipt['record_sha256'],'data_freeze_sha256':sha(out)}),flush=True)

def fit(raw):
    freeze();r=json.loads((P/'DATA_FREEZE.json').read_text());assert r['protocol_sha256']==sha(P/'PROTOCOL_FREEZE.json') and sha(raw)==r['record_sha256']
    from estimator import estimate
    out=estimate(raw,r);target=P/'RUN_EXECUTIONS.json';assert not target.exists();target.write_text(json.dumps({'rows':[out],'planned_and_actual_estimator_runs':1,'physical_promotion':0},indent=2)+'\n')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['prepare','generate','fit','campaign']);ap.add_argument('--baseline');ap.add_argument('--raw');args=ap.parse_args()
    if args.mode=='prepare':prepare()
    elif args.mode=='generate':generate(args.baseline,args.raw)
    elif args.mode=='fit':fit(args.raw)
    else:
        # One RAM-backed reproducible raw record; DATA_FREEZE is written before fit.
        fd=os.memfd_create(NAME,flags=0);raw=Path('/proc/self/fd')/str(fd)
        try:
            generate(args.baseline,raw);fit(raw)
            from estimator import project
            N,receipt=project(raw)
            run=json.loads((P/'RUN_EXECUTIONS.json').read_text())['rows'][0]
            assert receipt==run['projection']
            out={'status':'EXACT_FULL_PROJECTION_REPLAY_AFTER_SINGLE_FIT','record_sha256':sha(raw),'projection':receipt,'projection_entries_recomputed':int(N.size),'new_estimator_runs':0,'raw_storage':'anonymous RAM memfd; reconstructible from frozen baseline/selection','physical_promotion':0}
            (P/'PROJECTION_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n')
        finally:os.close(fd)
