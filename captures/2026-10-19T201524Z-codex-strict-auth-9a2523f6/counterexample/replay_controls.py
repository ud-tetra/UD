"""Post-known-outcome supplementary raw/certificate replay and hostile controls."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,hashlib,shutil
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from common import P,sha,freeze
import minimal_frame as m

def fixture(out,name):
    f=freeze();d=out/name;d.mkdir();(d/'inputs').mkdir();(d/'results').mkdir()
    case=d/'results'/f['case'];case.mkdir()
    for n in ['ALIGNMENT.npz','ALIGNMENT_FREEZE.json','RUN_EXECUTIONS.json','DATA_FREEZE.json','PROTOCOL_FREEZE.json','minimal_frame.py']:
        shutil.copyfile(P/n,d/n)
    for n in ['SOURCE_PHASE.json','FIXED_BUDGET.json']:shutil.copyfile(P/'inputs'/n,d/'inputs'/n)
    original=P/'results'/f['case']
    for p in original.iterdir():
        if p.suffix=='.npz':os.link(p,case/p.name)
        else:shutil.copyfile(p,case/p.name)
    return d

def run_certificate(d):
    originalP=m.P;originalfreeze=m.freeze
    def isolated_freeze():
        f=freeze().copy()
        f['reference_basis_sources']={k:str(P.parent/v) for k,v in f['reference_basis_sources'].items()}
        return f
    try:
        m.P=d;m.freeze=isolated_freeze;m.certify()
        return json.loads((d/'COUNTEREXAMPLE_RESULT.json').read_text())
    finally:m.P=originalP;m.freeze=originalfreeze

def update_fixture_freeze(d):
    a=json.loads((d/'ALIGNMENT_FREEZE.json').read_text())
    for n in a['files']:a['files'][n]=sha(d/n)
    (d/'ALIGNMENT_FREEZE.json').write_text(json.dumps(a,indent=2)+'\n')

def raw_replay(baseline):
    f=freeze();assert sha(baseline)==f['baseline_sha256'];data=json.loads((P/'DATA_FREEZE.json').read_text())
    S=json.loads((P/'SPATIAL_SELECTION.json').read_text());anchor=next(r for r in json.loads((P/'inputs/ANCHOR_DATA.json').read_text())['records'] if r['case']=='reverse_stationary')
    M=np.array(anchor['transform_integer_matrix'],np.int64);assert anchor['transform_denominator']==1
    Y=np.memmap(baseline,dtype='<i8',mode='r',shape=(37,8191,62));fd=os.memfd_create('independent_raw_replay',flags=0);raw=Path('/proc/self/fd')/str(fd);os.ftruncate(fd,150321232)
    try:
        Z=np.memmap(raw,dtype='<i8',mode='r+',shape=(37,8191,62));t=np.arange(8191);alt=1-2*(t%2);nomh=hashlib.sha256();checked=0
        for a in range(37):
            b=int(np.flatnonzero(M[a])[0]);nom=(np.array(Y[b],np.int64)*int(M[a,b])).astype('<i8');nomh.update(nom.tobytes());v=nom.copy();v[:,int(S['channels'][a])]+=1127*int(S['signs'][a])*alt;Z[a]=v
        Z.flush();del Z;Z=np.memmap(raw,dtype='<i8',mode='r',shape=(37,8191,62))
        # Independent all-coordinate exact eligibility check, not merely a hash.
        for a in range(37):
            b=int(np.flatnonzero(M[a])[0]);nom=np.array(Y[b],np.int64)*int(M[a,b]);diff=np.array(Z[a])-nom
            for c in range(62):assert np.array_equal(diff[:,c],1127*int(S['signs'][a])*alt if c==int(S['channels'][a]) else np.zeros(8191,np.int64))
            assert np.all(np.sum(diff*diff,axis=1)==1127**2);checked+=diff.size
        assert checked==18790154 and nomh.hexdigest()==data['nominal_sha256'] and sha(raw)==data['record_sha256']
        from estimator import sketch
        A=sketch();X=np.empty((8191,2294),np.int64)
        for c in range(62):
            for a in range(37):X[:,37*c+a]=Z[a,:,c]
        mx=max(abs(int(X.min())),abs(int(X.max())));partial=mx*int(abs(A).sum(axis=0).max());assert partial<2**63
        N=X@A;maximum=max(abs(int(N.min())),abs(int(N.max())));assert maximum<2**53
        projection={'partial_sum_bound':partial,'numerator_max':maximum,'integer_bytes_sha256':hashlib.sha256(N.astype('<i8').tobytes()).hexdigest(),'projection_bytes_sha256':hashlib.sha256((N.astype(float)/2.**55).astype('<f8').tobytes()).hexdigest()}
        expected=json.loads((P/'PROJECTION_REPLAY.json').read_text());assert projection==expected['projection']
        return {'status':'PASS_INDEPENDENT_RAW_REGENERATION_ALL_COORDINATES_AND_PROJECTION','record_sha256':sha(raw),'raw_scalars_checked':checked,'exact_vector_norms_checked':303067,'projection_entries_recomputed':int(N.size),'projection':projection,'new_estimator_runs':0,'persistent_raw_files_written':0}
    finally:os.close(fd)

def main(out,baseline):
    f=freeze();sf=json.loads((P/'SUPPLEMENT_FREEZE.json').read_text())
    for n,h in sf['files'].items():assert sha(P/n)==h,n
    out=Path(out);out.mkdir(exist_ok=False);raw=raw_replay(baseline);(out/'RAW_REPLAY.json').write_text(json.dumps(raw,indent=2)+'\n')
    original=json.loads((P/'COUNTEREXAMPLE_RESULT.json').read_text());positive=fixture(out,'unchanged_saved_factor_replay');r=run_certificate(positive);assert r==original
    controls=[]
    d=fixture(out,'zero_alignment');np.savez_compressed(d/'ALIGNMENT.npz',alignment=np.zeros((209,209),np.float64));update_fixture_freeze(d);r=run_certificate(d);assert not r['strict_minimum_frame_obstruction'] and r['status']=='HOLD_NO_MINIMAL_FRAME_COUNTEREXAMPLE'
    controls.append({'id':'zero_alignment','expected':'HOLD_NO_MINIMAL_FRAME_COUNTEREXAMPLE','actual':r['status'],'reason':'Conservative normal correction must be subtracted; raw r-squared alone is not a lower bound.'})
    d=fixture(out,'zero_returned_basis');case=d/'results'/f['case']
    for p in case.glob('U_*.npz'):
        with np.load(p,allow_pickle=False) as z:shape=z['basis'].shape
        p.unlink();np.savez_compressed(p,basis=np.zeros(shape,np.float64))
    p=case/'PHASE_META.npz'
    with np.load(p,allow_pickle=False) as z:vals={k:z[k] for k in z.files}
    p.unlink();vals['shift']=np.zeros((209,209),np.float64);np.savez_compressed(p,**vals)
    run=json.loads((case/'RUN.json').read_text());run['numeric_witnesses']={p.name:sha(p) for p in case.glob('*.npz')};(case/'RUN.json').write_text(json.dumps(run,indent=2)+'\n');(d/'RUN_EXECUTIONS.json').write_text(json.dumps({'rows':[run]},indent=2)+'\n');np.savez_compressed(d/'ALIGNMENT.npz',alignment=np.zeros((209,209),np.float64));update_fixture_freeze(d);r=run_certificate(d)
    assert r['status']=='HOLD_NO_MINIMAL_FRAME_COUNTEREXAMPLE' and not r['retained_Gram_cap_pass']
    controls.append({'id':'zero_returned_basis','expected':'HOLD_NO_MINIMAL_FRAME_COUNTEREXAMPLE_AND_GRAM_REFUSAL','actual':r['status'],'retained_Gram_pass':r['retained_Gram_cap_pass'],'scope':'Synthetic saved-array control, not a new estimator output or input record.'})
    d=fixture(out,'alignment_hash_mismatch')
    with np.load(d/'ALIGNMENT.npz',allow_pickle=False) as z:X=z['alignment'].copy()
    X[0,0]+=1.;np.savez_compressed(d/'ALIGNMENT.npz',alignment=X)
    try:run_certificate(d)
    except AssertionError as exc:controls.append({'id':'alignment_hash_mismatch','expected':'ASSERTION_REJECTION','actual':type(exc).__name__,'message':str(exc)})
    else:raise AssertionError('hash-corruption accepted')
    for n,h in sf['files'].items():assert sha(P/n)==h,n
    freeze()
    receipt={'status':'PASS_POSTKNOWN_SUPPLEMENT_RAW_REPLAY_EXACT_SAVED_FACTOR_REPLAY_AND_THREE_HOSTILE_CONTROLS','controls':controls,'saved_factor_result_exact_equal':True,'raw_replay':raw,'all_original_frozen_and_supplement_sources_unchanged':True,'supplement_freeze_sha256':sha(P/'SUPPLEMENT_FREEZE.json'),'completed_utc':datetime.now(timezone.utc).isoformat(),'scope':'Known-outcome supplementary engineering controls, not blinded and no new estimator/SVD fit. Fixtures may mutate data only in isolated paths; original factors untouched.','external_review':'PENDING','physical_promotion':0}
    (out/'REPLAY_AND_CONTROLS.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'status':receipt['status'],'control_count':len(controls),'new_estimator_runs':0}),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',required=True);p.add_argument('--baseline',required=True);a=p.parse_args();main(a.out,a.baseline)
