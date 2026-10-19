"""Same-team exact direct-residual audit; no estimator or producer-code import."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import hashlib, json, sys, math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
import numpy as np
from flint import fmpz_mat

ROOT=Path('/workspace/scratch/f3d1c2f040c9')
P=ROOT/'strict-family-review-20261019'
OUT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
pair=lambda f:[str(f.numerator),str(f.denominator)]
fr=lambda x:F(int(x[0]),int(x[1]))

def encode(x):
    assert x.dtype==np.float64 and np.isfinite(x).all()
    rows=[[float(v).as_integer_ratio() for v in row] for row in x]
    b=max(d.bit_length()-1 for row in rows for n,d in row)
    return [[n << (b-(d.bit_length()-1)) for n,d in row] for row in rows],b

def exact():
    f=load(P/'PROTOCOL_FREEZE.json'); r=load(P/'COUNTEREXAMPLE_RESULT.json')
    for n,h in f['files'].items(): assert sha(P/n)==h,n
    for n,h in f['source_files'].items(): assert sha(ROOT/n)==h,n
    af=load(P/'ALIGNMENT_FREEZE.json')
    for n,h in af['files'].items(): assert sha(P/n)==h,n
    run=load(P/'RUN_EXECUTIONS.json'); assert run['planned_and_actual_estimator_runs']==1
    rr=run['rows'][0]; case=P/'results'/rr['case']
    for n,h in rr['numeric_witnesses'].items(): assert sha(case/n)==h,n
    assert rr['execution_status']=='COMPLETED' and rr['learned_order']==209 and rr['rank_not_forced']
    U0=np.vstack([np.load(ROOT/f['reference_basis_sources'][k],allow_pickle=False)['basis'] for k in ['A','B']])
    U1=np.vstack([np.load(case/f'U_{k}.npz',allow_pickle=False)['basis'] for k in range(3)])
    X=np.load(P/'ALIGNMENT.npz',allow_pickle=False)['alignment']
    T=np.load(case/'PHASE_META.npz',allow_pickle=False)['shift']
    sig=np.load(case/'SVD_META.npz',allow_pickle=False)['singular']
    assert U0.shape==U1.shape==(8191,209) and X.shape==T.shape==(209,209)
    assert np.count_nonzero(sig>2.**-24)==209
    A,b0=encode(U0); B,b1=encode(U1); Xl,bx=encode(X); Tl,bt=encode(T)
    XM=fmpz_mat(Xl); TM=fmpz_mat(Tl); br=max(b1,b0+bx)
    rnum=0; nsum=fmpz_mat(209,209); G0=fmpz_mat(209,209); G1=fmpz_mat(209,209)
    # Materialize exact residual ROW BLOCKS directly, then square and contract.
    for start in range(0,8191,256):
        end=min(8191,start+256); am=fmpz_mat(A[start:end]); bm=fmpz_mat(B[start:end])
        rm=bm*(1<<(br-b1))-(am*XM)*(1<<(br-b0-bx))
        rnum+=sum(int(v)**2 for row in rm.tolist() for v in row)
        nsum+=am.transpose()*rm; G0+=am.transpose()*am; G1+=bm.transpose()*bm
    r2=F(rnum,1<<(2*br)); n2=F(sum(int(v)**2 for row in nsum.tolist() for v in row),1<<(2*(b0+br)))
    def gram_defect(g,b):
        return F(sum((int(g[i,j])-((1<<(2*b)) if i==j else 0))**2 for i in range(209) for j in range(209)),1<<(4*b))
    eta0sq=gram_defect(G0,b0);eta1sq=gram_defect(G1,b1)
    eta=fr(load(P/'inputs/SOURCE_PHASE.json')['metrics']['basis_orthogonality_upper']); ell=1-eta
    assert 0<=eta0sq<=eta**2 and ell>0
    lower=r2-n2/ell
    for key,value in [('exact_reference_Gram_defect_squared',eta0sq),('exact_alignment_residual_squared',r2),('exact_alignment_normal_residual_squared',n2),('exact_minimum_alignment_residual_squared_lower',lower)]:
        assert value==fr(r[key]),key
    lagnorm=fmpz_mat(209,209);lagnum=0
    for start in range(0,8189,256):
        end=min(8189,start+256);bm=fmpz_mat(B[start:end]);bp=fmpz_mat(B[start+2:end+2])
        dm=bp*(1<<bt)-bm*TM
        lagnum+=sum(int(v)**2 for row in dm.tolist() for v in row)
        lagnorm+=bm.transpose()*dm
    lag2=F(lagnum,1<<(2*(b1+bt)))
    nu2=F(sum(int(v)**2 for row in lagnorm.tolist() for v in row),1<<(2*(2*b1+bt)))
    assert lag2==fr(r['actual_lag2_shift_squared']) and nu2==fr(r['actual_lag2_normal_squared'])
    budget=load(P/'inputs/FIXED_BUDGET.json')['source_budget'];cap=fr(budget['allowed_raw_frame_residual_lower'])
    assert cap==fr(r['unchanged_raw_frame_cap']) and lower>cap**2
    assert eta1sq<=fr(budget['retained_Gram_cap'])**2 and nu2<=fr(budget['normal_cap'])**2
    ld=fr(r['minimum_alignment_residual_F_lower']); assert ld**2<=lower and (ld+F(1,1<<180))**2>lower
    return {'direct_alignment_residual_squared':pair(r2),'direct_normal_squared':pair(n2),'minimum_alignment_residual_squared_lower':pair(lower),'direct_lag2_residual_squared':pair(lag2),'direct_lag2_normal_squared':pair(nu2),'reference_gram_squared':pair(eta0sq),'returned_gram_squared':pair(eta1sq),'strict_obstruction':True,'gram_pass':True,'normal_pass':True,'floating_cutoff_count':209,'encoded_frame_scalings':[b0,b1,bx,bt,br]}

def raw_projection():
    f=load(P/'PROTOCOL_FREEZE.json'); data=load(P/'DATA_FREEZE.json'); S=load(P/'SPATIAL_SELECTION.json')
    row=next(r for r in load(P/'inputs/ANCHOR_DATA.json')['records'] if r['case']=='reverse_stationary')
    M=np.array(row['transform_integer_matrix'],np.int64);assert row['transform_denominator']==1
    assert np.array_equal(M@M.T,np.eye(37,dtype=np.int64)) and all(i%2==j%2 for i,j in zip(*np.nonzero(M)))
    assert np.all(np.count_nonzero(M,axis=1)==1)
    family=load(P/'inputs/FAMILY_CERTIFICATE.json')
    assert family['delta_per_62_vector']==[1127,1<<48] and family['rho']==[1,1<<20] and 'reverse_stationary' in family['anchor_cases']
    baseline=ROOT/'floating-timing-work/records/ramp_clock_stress.i64le';assert sha(baseline)==f['baseline_sha256']
    Y=np.memmap(baseline,dtype='<i8',mode='r',shape=(37,8191,62))
    ch=np.array(S['channels'],np.int64);sg=np.array(S['signs'],np.int64);assert np.all(abs(sg)==1) and np.all((ch>=0)&(ch<62))
    old=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64)
    v=np.pad(np.array(load(P/'inputs/NULL_VECTOR.json')['vector'],np.int64),(0,1974))
    new=np.random.default_rng(184052).choice([-1.,1.],size=(2294,160)).astype(np.int64)
    A=np.column_stack((old*2,v,new*2));assert v@v==16228 and np.all(v@old==0)
    meta=np.load(ROOT/'cutoff-campaign-work/results/reverse_stationary/SVD_META.npz',allow_pickle=False)
    w=((A.astype(float)/128.)@meta['right_transpose'][208]).reshape(62,37)
    expected=np.argmax(abs(w),axis=0);assert np.array_equal(ch,expected) and np.array_equal(sg,np.where(w[expected,np.arange(37)]>=0,1,-1))
    hs=hashlib.sha256(); ns=hashlib.sha256();vectors=0;scalars=0;maxraw=0
    source=[];sign=[]
    for a in range(37):
        b=int(np.flatnonzero(M[a])[0]);s=int(M[a,b]);source.append(b);sign.append(s)
        nom=s*np.array(Y[b],np.int64);ns.update(nom.astype('<i8').tobytes())
        z=nom.copy();z[np.arange(8191),ch[a]]+=1127*sg[a]*np.where(np.arange(8191)%2,-1,1)
        diff=z-nom;assert np.all(np.sum(diff*diff,axis=1)==1127**2)
        vectors+=8191;scalars+=diff.size;hs.update(z.astype('<i8').tobytes());maxraw=max(maxraw,abs(int(z.min())),abs(int(z.max())))
    assert hs.hexdigest()==data['record_sha256'] and ns.hexdigest()==data['nominal_sha256']==row['nominal_sha256']
    ih=hashlib.sha256();dh=hashlib.sha256();nmax=0
    bound=maxraw*int(abs(A).sum(axis=0).max());assert bound<2**63
    for k in range(0,8191,128):
        stop=min(8191,k+128);Z=np.stack([sign[a]*np.array(Y[source[a],k:stop],np.int64) for a in range(37)])
        for a in range(37):Z[a,np.arange(stop-k),ch[a]]+=1127*sg[a]*np.where(np.arange(k,stop)%2,-1,1)
        N=Z.transpose(1,2,0).reshape(stop-k,2294)@A
        nmax=max(nmax,abs(int(N.min())),abs(int(N.max())));assert nmax<2**53
        ih.update(N.astype('<i8').tobytes());dh.update((N.astype(float)/2.**55).astype('<f8').tobytes())
    projected={'partial_sum_bound':bound,'numerator_max':nmax,'integer_bytes_sha256':ih.hexdigest(),'projection_bytes_sha256':dh.hexdigest()}
    assert projected==load(P/'RUN_EXECUTIONS.json')['rows'][0]['projection']
    return {'raw_sha256':hs.hexdigest(),'nominal_sha256':ns.hexdigest(),'scalars_reconstructed':scalars,'vector_norms_checked':vectors,'projection_entries_checked':8191*321,'projection':projected,'preparation_anchor_distance':[0,1],'encoded_noise_per_vector':[1127,1<<48],'persistent_raw_allocations':0}

if __name__=='__main__':
    frozen=load(OUT/'AUDIT_FREEZE.json'); assert sha(Path(__file__))==frozen['script_sha256']
    for n,h in frozen['producer_files'].items():assert sha(P/n)==h,n
    r={'status':'SAME_TEAM_DIRECT_RESIDUAL_AND_STREAMED_INPUT_AUDIT_PASS','utc':datetime.now(timezone.utc).isoformat(),'audit_freeze_sha256':sha(OUT/'AUDIT_FREEZE.json'),'producer_result_sha256':sha(P/'COUNTEREXAMPLE_RESULT.json'),'raw_projection':raw_projection(),'exact':exact(),'new_estimator_calls':0,'scope':'Actual returned basis obstruction at unchanged raw frame cap. Does not assert ideal-SVD obstruction, phase failure, physical failure, or external independence.','external_review':'PENDING','physical_promotion':0}
    out=OUT/'AUDIT_RECEIPT.json';assert not out.exists();out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'status':r['status'],'new_estimator_calls':0,'receipt_sha256':sha(out)}))
