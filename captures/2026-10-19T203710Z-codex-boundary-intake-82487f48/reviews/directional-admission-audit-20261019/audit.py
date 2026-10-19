"""Independent direct-block exact audit of four saved outputs; zero estimator calls."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
from flint import fmpz_mat
ROOT=Path('/workspace/scratch/f3d1c2f040c9');P=ROOT/'directional-admission-work-20261019';OUT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
fr=lambda x:F(int(x[0]),int(x[1]));pair=lambda x:[str(x.numerator),str(x.denominator)]
def encode(x):
    assert x.dtype==np.float64 and np.isfinite(x).all()
    rows=[[float(v).as_integer_ratio() for v in row] for row in x]
    b=max(d.bit_length()-1 for row in rows for n,d in row)
    return [[n<<(b-(d.bit_length()-1)) for n,d in row] for row in rows],b
def sumsq(m):return sum(int(v)**2 for row in m.tolist() for v in row)
def gramdef(g,b):return F(sum((int(g[i,j])-((1<<(2*b)) if i==j else 0))**2 for i in range(209) for j in range(209)),1<<(4*b))

def raw_audit(f,data,runs):
    amps=f['amplitudes'];assert amps==[0,1,2,4]
    row=next(r for r in load(P/'inputs/ANCHOR_DATA.json')['records'] if r['case']=='reverse_stationary')
    M=np.array(row['transform_integer_matrix'],np.int64);assert row['transform_denominator']==1 and np.array_equal(M@M.T,np.eye(37,dtype=np.int64))
    assert np.all(np.count_nonzero(M,axis=1)==1) and all(i%2==j%2 for i,j in zip(*np.nonzero(M)))
    family=load(P/'inputs/FAMILY_CERTIFICATE.json');assert family['delta_per_62_vector']==[1127,1<<48] and family['rho']==[1,1<<20]
    S=load(P/'inputs/SPATIAL_SELECTION.json');ch=np.array(S['channels'],np.int64);sg=np.array(S['signs'],np.int64)
    assert np.all(abs(sg)==1) and np.all((ch>=0)&(ch<62))
    baseline=ROOT/'floating-timing-work/records/ramp_clock_stress.i64le';assert sha(baseline)==f['baseline_sha256']
    Y=np.memmap(baseline,dtype='<i8',mode='r',shape=(37,8191,62));t=np.arange(8191);alt=np.where(t%2,-1,1)
    hs={a:hashlib.sha256() for a in amps};ns=hashlib.sha256();mx={a:0 for a in amps};source=[];sign=[]
    for prep in range(37):
        b=int(np.flatnonzero(M[prep])[0]);s=int(M[prep,b]);source.append(b);sign.append(s)
        nom=s*np.array(Y[b],np.int64);ns.update(nom.astype('<i8').tobytes())
        for amp in amps:
            z=nom.copy();z[t,ch[prep]]+=amp*sg[prep]*alt;diff=z-nom
            assert np.all(np.sum(diff*diff,axis=1)==amp**2)
            hs[amp].update(z.astype('<i8').tobytes());mx[amp]=max(mx[amp],abs(int(z.min())),abs(int(z.max())))
    assert ns.hexdigest()==row['nominal_sha256']
    old=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64)
    v=np.pad(np.array(load(P/'inputs/NULL_VECTOR.json')['vector'],np.int64),(0,1974))
    new=np.random.default_rng(184052).choice([-1.,1.],size=(2294,160)).astype(np.int64)
    A=np.column_stack((2*old,v,2*new));assert v@v==16228 and np.all(v@old==0)
    assert all(mx[a]*int(abs(A).sum(axis=0).max())<2**63 for a in amps)
    # Independent linear factorization: one nominal projection plus exactly
    # projected rank-one alternating perturbation for each frozen amplitude.
    dv=sum((sg[a]*A[37*ch[a]+a] for a in range(37)),start=np.zeros(321,np.int64))
    ih={a:hashlib.sha256() for a in amps};dh={a:hashlib.sha256() for a in amps};nmax={a:0 for a in amps}
    for k in range(0,8191,128):
        stop=min(8191,k+128);z0=np.stack([sign[a]*np.array(Y[source[a],k:stop],np.int64) for a in range(37)])
        N0=z0.transpose(1,2,0).reshape(stop-k,2294)@A
        for amp in amps:
            N=N0+amp*alt[k:stop,None]*dv[None,:]
            nmax[amp]=max(nmax[amp],abs(int(N.min())),abs(int(N.max())));assert nmax[amp]<2**53
            ih[amp].update(N.astype('<i8').tobytes());dh[amp].update((N.astype(float)/2.**55).astype('<f8').tobytes())
    result=[]
    for amp,record,run in zip(amps,data['records'],runs['rows']):
        assert record['integer_amplitude']==amp and record['case']==run['case']==f'directional_amp_{amp}'
        assert hs[amp].hexdigest()==record['record_sha256']==run['record_sha256'] and ns.hexdigest()==record['nominal_sha256']
        bound=mx[amp]*int(abs(A).sum(axis=0).max());assert bound<2**63
        proj={'partial_sum_bound':bound,'numerator_max':nmax[amp],'integer_bytes_sha256':ih[amp].hexdigest(),'projection_bytes_sha256':dh[amp].hexdigest()}
        assert proj==run['projection']
        result.append({'amplitude':amp,'raw_sha256':hs[amp].hexdigest(),'nominal_sha256':ns.hexdigest(),'scalar_checks':18790154,'vector_norm_checks':303067,'projection_entries':8191*321,'projection':proj,'anchor_distance':[0,1],'noise_per_vector':[amp,1<<48]})
    return result

def exact_audit(f,certificate,runs):
    U0=np.vstack([np.load(ROOT/f['reference_basis_sources'][k],allow_pickle=False)['basis'] for k in ['A','B']]);assert U0.shape==(8191,209)
    A,b0=encode(U0);G0=fmpz_mat(209,209)
    for k in range(0,8191,256):am=fmpz_mat(A[k:k+256]);G0+=am.transpose()*am
    e0=gramdef(G0,b0);eta=fr(load(P/'inputs/SOURCE_PHASE.json')['metrics']['basis_orthogonality_upper']);assert e0<=eta**2 and eta<1
    assert e0==fr(certificate['exact_reference_Gram_squared']);ell=1-eta;assert ell==fr(certificate['reference_minimum_Gram_eigenvalue_lower'])
    budget=load(P/'inputs/FIXED_BUDGET.json')['source_budget'];cap=fr(budget['allowed_raw_frame_residual_lower']);gc=fr(budget['retained_Gram_cap']);nc=fr(budget['normal_cap'])
    assert cap==fr(certificate['strict_frame_cap']) and gc==fr(certificate['retained_Gram_cap']) and nc==fr(certificate['fixed_normal_cap'])
    alignment=load(P/'ALIGNMENT_FREEZE.json');out=[]
    for result,run in zip(certificate['rows'],runs['rows']):
        assert run['case']==result['case'];case=P/'results'/run['case']
        for n,h in run['numeric_witnesses'].items():assert sha(case/n)==h
        assert run==load(case/'RUN.json') and run['execution_status']=='COMPLETED' and run['learned_order']==209 and run['rank_not_forced']
        sig=np.load(case/'SVD_META.npz',allow_pickle=False)['singular'];assert np.count_nonzero(sig>2.**-24)==209
        U=np.vstack([np.load(case/f'U_{k}.npz',allow_pickle=False)['basis'] for k in range(3)])
        T=np.load(case/'PHASE_META.npz',allow_pickle=False)['shift']
        xa=next(x for x in alignment['rows'] if x['case']==run['case']);assert sha(P/xa['alignment'])==xa['sha256']
        X=np.load(P/xa['alignment'],allow_pickle=False)['alignment'];B,b1=encode(U);xl,bx=encode(X);tl,bt=encode(T)
        XM=fmpz_mat(xl);TM=fmpz_mat(tl);br=max(b1,b0+bx);rnum=0;N=fmpz_mat(209,209);G1=fmpz_mat(209,209)
        for k in range(0,8191,256):
            am=fmpz_mat(A[k:k+256]);bm=fmpz_mat(B[k:k+256]);R=bm*(1<<(br-b1))-(am*XM)*(1<<(br-b0-bx))
            rnum+=sumsq(R);N+=am.transpose()*R;G1+=bm.transpose()*bm
        r2=F(rnum,1<<(2*br));n2=F(sumsq(N),1<<(2*(b0+br)));lower=r2-n2/ell;g1=gramdef(G1,b1)
        Dnorm=fmpz_mat(209,209);dnum=0
        for k in range(0,8189,256):
            end=min(8189,k+256);bm=fmpz_mat(B[k:end]);bp=fmpz_mat(B[k+2:end+2]);D=bp*(1<<bt)-bm*TM
            dnum+=sumsq(D);Dnorm+=bm.transpose()*D
        d2=F(dnum,1<<(2*(b1+bt)));nu2=F(sumsq(Dnorm),1<<(2*(2*b1+bt)))
        for key,value in [('exact_alignment_residual_squared',r2),('exact_alignment_normal_squared',n2),('exact_minimum_alignment_residual_squared_lower',lower),('retained_Gram_squared',g1),('actual_normal_squared',nu2),('actual_shift_squared',d2)]:assert value==fr(result[key]),key
        upper=fr(result['alignment_residual_F_upper']);lo=fr(result['minimum_alignment_residual_F_lower'])
        assert upper**2>=r2 and (upper-F(1,1<<180))**2<r2 and lo**2<=max(F(0),lower) and (lo+F(1,1<<180))**2>max(F(0),lower)
        verdict='CERTIFIED_FRAME_PASS' if r2<cap**2 else ('CERTIFIED_FRAME_FAIL' if lower>cap**2 else 'HOLD_FRAME_INCONCLUSIVE')
        gp=g1<=gc**2;npas=nu2<=nc**2
        assert verdict==result['frame_verdict'] and gp==result['retained_Gram_cap_pass'] and npas==result['normal_cap_pass']
        expected='CERTIFIED_FINITE_DIRECTIONAL_ADMISSION' if verdict=='CERTIFIED_FRAME_PASS' and gp and npas else ('CERTIFIED_STRICT_FRAME_REFUSAL' if verdict=='CERTIFIED_FRAME_FAIL' else 'HOLD_FINITE_DIRECTIONAL_ADMISSION')
        assert expected==result['overall_verdict']
        out.append({'case':run['case'],'amplitude':result['integer_amplitude'],'frame_verdict':verdict,'overall_verdict':expected,'r_squared':pair(r2),'normal_alignment_squared':pair(n2),'minimum_residual_squared_lower':pair(lower),'reference_Gram_squared':pair(e0),'returned_Gram_squared':pair(g1),'actual_lag2_shift_squared':pair(d2),'actual_lag2_normal_squared':pair(nu2),'Gram_pass':gp,'normal_pass':npas,'floating_cutoff_count':209})
    failed=[r['amplitude'] for r in out if r['frame_verdict']=='CERTIFIED_FRAME_FAIL'];amin=min(failed) if failed else None
    return {'rows':out,'smallest_failed_sample_amplitude':amin,'nested_ball_exclusion_radius':None if amin is None else [amin,1<<48],'nested_ball_statement':'A witnessed eligible failure at this radius belongs to every larger encoded noise ball; uniform strict-frame admission is excluded for all those balls. No monotonic response or uniform small-radius success is inferred.'}

if __name__=='__main__':
    freeze=load(OUT/'AUDIT_FREEZE.json');assert sha(Path(__file__))==freeze['script_sha256']
    for n,h in freeze['producer_files'].items():assert sha(P/n)==h,n
    f=load(P/'PROTOCOL_FREEZE.json')
    for n,h in f['files'].items():assert sha(P/n)==h,n
    for n,h in f['source_files'].items():assert sha(ROOT/n)==h,n
    d=load(P/'DATA_FREEZE.json');runs=load(P/'RUN_EXECUTIONS.json');c=load(P/'CERTIFICATE.json')
    assert runs['planned_and_actual_estimator_runs']==4 and runs['data_freeze_sha256']==sha(P/'DATA_FREEZE.json')
    raw=raw_audit(f,d,runs);exact=exact_audit(f,c,runs)
    r={'status':'SAME_TEAM_FOUR_DIRECTIONAL_OUTPUT_AUDIT_PASS','utc':datetime.now(timezone.utc).isoformat(),'audit_freeze_sha256':sha(OUT/'AUDIT_FREEZE.json'),'producer_certificate_sha256':sha(P/'CERTIFICATE.json'),'raw':raw,'exact':exact,'new_estimator_calls':0,'persistent_raw_allocations':0,'scope':'Four frozen actual floating outputs; no monotonicity, uniform-small-ball success, ideal-SVD, phase-error, physical, or external independence claim. Nested-ball exclusion separately proved by set inclusion.','external_review':'PENDING','physical_promotion':0}
    p=OUT/'AUDIT_RECEIPT.json';assert not p.exists();p.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'status':r['status'],'receipt_sha256':sha(p),'smallest_failed_sample_amplitude':exact['smallest_failed_sample_amplitude']}))
