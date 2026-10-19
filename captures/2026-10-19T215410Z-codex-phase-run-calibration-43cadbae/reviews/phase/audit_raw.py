"""Independent exact input replay: residual-form Cayley rounding and rank-one noise."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,hashlib
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from flint import arb,fmpq,ctx
ctx.prec=512
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def sign(kind,x):
    if x==0:return 1
    z=arb(fmpq(x.numerator,x.denominator));v=z.sin() if kind=='sin' else z.cos()
    if v>0:return 1
    if v<0:return -1
    raise ArithmeticError('INDEPENDENT_FIXED512_SIGN_HOLD_NO_RETRY')
def temporal(case):
    if case['noise_kind']=='zero':return np.zeros(8191,np.int64)
    w=F(*case['carrier_omega']);out=[]
    for k in range(8191):
        if case['noise_kind']=='ramped_low_sine':
            amp=round(F(1127*(k-4095),4095));v=0 if amp==0 else amp*sign('sin',w*k)
        else:
            assert case['noise_kind']=='chirped_high_cosine';u=F(k,8191);v=1127*sign('cos',w*k+u*(1+u))
        out.append(v)
    return np.array(out,np.int64)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--baseline',required=True);ap.add_argument('--repo',required=True);args=ap.parse_args()
    S=Path(args.source).resolve();base=Path(args.baseline).resolve();repo=Path(args.repo).resolve();f=load(P/'RAW_AUDIT_FREEZE.json');assert sha(Path(__file__))==f['script_sha256']
    for n,h in f['producer_files'].items():assert sha(S/n)==h,n
    protocol=load(S/'PROTOCOL_FREEZE.json')
    for n,h in protocol['files'].items():assert sha(S/n)==h,n
    for n,h in protocol['repository_sources'].items():assert sha(repo/n)==h,n
    C=load(S/'CONTRACT.json');data=load(S/'DATA_FREEZE.json');assert data['estimator_calls_before_freeze']==0 and data['protocol_sha256']==sha(S/'PROTOCOL_FREEZE.json')
    assert sha(base)==C['expected_synthetic_baseline_sha256'];Y=np.memmap(base,dtype='<i8',mode='r',shape=(37,8191,62));ymax=max(abs(int(Y.min())),abs(int(Y.max())))
    old=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64);v=np.pad(np.array(load(S/'inputs/NULL_VECTOR.json')['vector'],np.int64),(0,1974));new=np.random.default_rng(184052).choice([-1.,1.],size=(2294,160)).astype(np.int64)
    A=np.column_stack((2*old,v,2*new));assert v@v==16228 and np.all(v@old==0)
    rows=[]
    for prep in C['preparations']:
        cases=[c for c in C['cases'] if c['preparation_id']==prep['id']];assert len(cases)==2
        profiles={c['case']:temporal(c) for c in cases};hs={c['case']:hashlib.sha256() for c in cases};nomh=hashlib.sha256();mx={c['case']:0 for c in cases}
        M=prep['matrix_numerator'];D=prep['denominator'];assert D==(1<<44)+1 and D%2==1
        l1=max(sum(abs(x) for x in row) for row in M);bound=(ymax*l1+D-1)//D+1128;assert bound*int(abs(A).sum(axis=0).max())<2**63
        N0=np.zeros((8191,321),np.int64)
        for a in range(37):
            active=[j for j in range(37) if M[a][j]]
            if len(active)==1:
                j=active[0];assert abs(M[a][j])==D;nom=(1 if M[a][j]>0 else -1)*np.array(Y[j],np.int64)
            else:
                assert len(active)==2;j=next(j for j in active if abs(M[a][j])==D-2);k=next(k for k in active if k!=j);assert abs(M[a][k])==1<<23
                x=(1 if M[a][j]>0 else -1)*np.array(Y[j],np.int64);y=(1 if M[a][k]>0 else -1)*np.array(Y[k],dtype=object)
                # Different algebra from producer: D*x + u, u=b*y−2*x.
                # Odd D forbids half ties, so translation by integer x is exact.
                u=(1<<23)*y-2*np.array(x,dtype=object);q=u//D;r=u-q*D;obj=np.array(x,dtype=object)+q+(2*r>D)
                assert all(-(1<<63)<int(z)<(1<<63) for z in obj.flat);nom=np.array(obj,np.int64)
            assert max(abs(int(nom.min())),abs(int(nom.max())))+1127<2**63;nomh.update(nom.astype('<i8').tobytes())
            N0+=nom@A[np.arange(62)*37+a]
            for case in cases:
                name=case['case'];sp=case['spatial'][a];wanted=sp['sign']*profiles[name];raw=nom.copy();raw[:,sp['channel']]+=wanted;diff=raw-nom
                W=np.zeros_like(diff);W[:,sp['channel']]=wanted;assert np.array_equal(diff,W)
                assert np.array_equal((diff*diff).sum(axis=1),wanted*wanted) and np.all(abs(wanted)<=case['integer_noise_absolute_max'])
                hs[name].update(raw.astype('<i8').tobytes());mx[name]=max(mx[name],abs(int(raw.min())),abs(int(raw.max())))
        for case in cases:
            name=case['case'];rec=next(r for r in data['records'] if r['case']==name);profile=profiles[name]
            assert hs[name].hexdigest()==rec['record_sha256'] and nomh.hexdigest()==rec['nominal_sha256'];assert hashlib.sha256(profile.astype('<i8').tobytes()).hexdigest()==rec['temporal_profile_sha256']
            dv=sum((sp['sign']*A[37*sp['channel']+sp['preparation']] for sp in case['spatial']),start=np.zeros(321,np.int64))
            N=N0+profile[:,None]*dv[None,:];nmax=max(abs(int(N.min())),abs(int(N.max())));assert nmax<2**53
            projection={'partial_sum_bound':mx[name]*int(abs(A).sum(axis=0).max()),'numerator_max':nmax,'integer_bytes_sha256':hashlib.sha256(N.astype('<i8').tobytes()).hexdigest(),'projection_bytes_sha256':hashlib.sha256((N.astype(float)/2.**55).astype('<f8').tobytes()).hexdigest()}
            assert projection==rec['projection']
            rows.append({'case':name,'raw_sha256':hs[name].hexdigest(),'nominal_sha256':nomh.hexdigest(),'profile_sha256':rec['temporal_profile_sha256'],'projection':projection,'scalar_differences_checked':18790154,'vector_norms_checked':303067,'projection_entries_checked':8191*321})
    result={'status':'PASS_INDEPENDENT_BIGINT_RESIDUAL_ROUNDING_RAW_AND_PROJECTION_REPLAY','utc':datetime.now(timezone.utc).isoformat(),'freeze_sha256':sha(P/'RAW_AUDIT_FREEZE.json'),'rows':rows,'raw_or_factor_files_copied':0,'persistent_raw_allocations':0,'independent_nonzero_temporal_profiles_replayed':2,'new_estimator_SVD_eigenvalue_inverse_alignment_calls':0,'scope':'Input replay only; no output phase/frame outcome inferred. Residual-form odd-denominator rounding and rank-one perturbation projection independently validate producer bytes.','external_review':'PENDING','physical_promotion':0}
    out=P/'RAW_AUDIT_RECEIPT.json';assert not out.exists();out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'receipt_sha256':sha(out)}))
if __name__=='__main__':main()
