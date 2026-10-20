"""Zero-fit exact adjoint residual on two unchanged computational records.

Replay original raw bytes only in RAM, check the original raw/projection hashes,
then certify Z.T U - V S using integer matrix arithmetic. Original forward and
Gram norm statements and source tail are inherited, not recomputed here.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import argparse
import gzip
import hashlib
import json
import math
import platform
import resource
import time
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from flint import fmpz_mat

SOURCE='captures/2026-10-20T183427Z-codex-maximal-noise-e5831029'
PRIOR='captures/2026-10-20T190406Z-codex-backend-contract-a14abe64'
BASE_SHA='25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59'
CASES=('boundary_pair_block','boundary_pair_rotating')

def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()

def pair(x):return [str(x.numerator),str(x.denominator)]
def rat(x):return F(int(x[0]),int(x[1]))
def write(path,x):
    with path.open('x') as f:f.write(json.dumps(x,indent=2,sort_keys=True)+'\n')

def root_upper(x,bits=180):
    assert x>=0
    n=x.numerator<<(2*bits);d=x.denominator;k=math.isqrt(n//d)
    if k*k*d<n:k+=1
    result=F(k,1<<bits)
    assert result*result>=x and (k==0 or F(k-1,1<<bits)**2<x)
    return result

def encode(x):
    assert x.dtype==np.float64 and np.isfinite(x).all()
    ratios=[float(v).as_integer_ratio()for v in x.flat]
    b=max(d.bit_length()-1 for _,d in ratios)
    integers=np.array([n<<(b-(d.bit_length()-1))for n,d in ratios],dtype=object).reshape(x.shape)
    return integers,b

def sketch(path):
    A0=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64)
    vector=np.array(json.loads(path.read_text())['vector'],dtype=np.int64)
    v=np.pad(vector,(0,1974));assert v.shape==(2294,)
    A1=np.random.default_rng(184052).choice([-1.,1.],size=(2294,160)).astype(np.int64)
    assert int(v@v)==16228 and np.all(v@A0==0)
    return np.column_stack((2*A0,v,2*A1))

def reconstruct(repo,baseline,case,work,saved):
    assert baseline.stat().st_size==150321232 and sha(baseline)==BASE_SHA
    Y=np.memmap(baseline,dtype='<i8',mode='r',shape=(37,8191,62))
    X=np.empty((8191,2294),dtype=np.int64);t=np.arange(8191,dtype=np.int64);raw_hash=hashlib.sha256()
    for p in range(37):
        old=np.array(Y[p],dtype=np.int64,copy=True)
        assert int(old.min())>-(1<<63)+1 and int(old.max())<(1<<63)-2
        if case=='boundary_pair_block':
            c=np.full(8191,17,dtype=np.int64);d=np.full(8191,48,dtype=np.int64)
            s=np.where((p+t//257)%2==0,1,-1);u=np.where((t//31)%2==0,1,-1)
        elif case=='boundary_pair_rotating':
            c=(7*p+11*t+5)%62;d=(c+31)%62
            s=np.where(np.isin((t+3*p)%13,[0,1,3,4,9,10,12]),1,-1)
            u=np.array([1,1,-1,1,-1,-1,-1],np.int64)[(t+2*p)%7]
        else:raise ValueError('unfrozen case')
        assert np.all(c!=d) and np.all(abs(s)==1) and np.all(abs(u)==1)
        old[t,c]+=s;old[t,d]+=u
        raw_hash.update(old.astype('<i8').tobytes())
        X[:,p::37]=old
    del Y
    assert raw_hash.hexdigest()==saved['record_sha256']
    A=sketch(repo/SOURCE/'campaign/cases'/case/'inputs/NULL_VECTOR.json')
    mx=max(abs(int(X.min())),abs(int(X.max())))
    partial=mx*int(np.abs(A).sum(axis=0).max())
    assert partial<2**63
    N=X@A;del X,A
    maximum=max(abs(int(N.min())),abs(int(N.max())))
    assert maximum<2**53
    projection={'partial_sum_bound':partial,'numerator_max':maximum,
      'integer_bytes_sha256':hashlib.sha256(N.astype('<i8').tobytes()).hexdigest(),
      'projection_bytes_sha256':hashlib.sha256((N.astype(np.float64)/2.**55).astype('<f8').tobytes()).hexdigest()}
    assert projection==saved['projection']
    assert sha(baseline)==BASE_SHA
    np.save(work/'N.npy',N,allow_pickle=False)
    receipt={'status':'ORIGINAL_RECORD_AND_INTEGER_PROJECTION_REPLAY_IDENTICAL','case':case,
      'baseline_sha256':BASE_SHA,'record_sha256':raw_hash.hexdigest(),'projection':projection,
      'N_shape':[8191,321],'N_denominator_bits':55,'temporary_N_npy_sha256':sha(work/'N.npy'),
      'new_estimator_calls':0,'new_record_identities':0,'temporary_replay_records_in_RAM':1,
      'raw_replay_file_written':False,'physical_promotion':0}
    return N,receipt

def consequences(a,b,f,g,s1,sq,tail,s210,source_lower):
    assert 0<=a<1 and 0<=b<1 and f>=0 and g>=0 and s1>=sq>0 and 0<=tail and s210>=0
    polar=s1*(a/(2-a)+b/(2-b))
    compression=(polar+f)/(1-b)
    cross=max(f/(1-b),g/(1-a))
    epsilon=compression+cross
    gap=sq-compression-tail-cross
    if gap<=0:return {'status':'HOLD_NO_STRICT_LEADING_BLOCK_GAP','matching_gap':gap}
    lower=sq-epsilon;assert lower>0
    return {'status':'CERTIFIED_FINITE_RETAINED_TWO_SIDED_ERROR',
      'compression_upper':compression,'offdiagonal_upper':cross,
      'retained_abs_error_upper':epsilon,'all321_abs_error_upper':max(epsilon,tail,s210),
      'matching_gap':gap,'ambient_sigma1_upper':s1+epsilon,'ambient_sigma209_lower':lower,
      'ambient_leading_condition_upper':(s1+epsilon)/lower,
      'qth_proposal_minus_original_floor_lower':sq-(source_lower-F(1,1<<41)),
      'sufficient_adjoint_upper_for_retained_2^-41':(F(1,1<<41)-compression)*(1-a)}

def main(repo,baseline,case,work,out):
    started=time.perf_counter();here=Path(__file__).resolve().parent
    freeze=json.loads((here/'FREEZE.json').read_text())
    for n,h in freeze['code'].items():assert sha(here/n)==h,('code',n)
    for n,pin in freeze['sources'].items():
        path=repo/n;assert path.stat().st_size==pin['size_bytes'] and sha(path)==pin['sha256'],('source',n)
    assert case in CASES;work.mkdir(parents=True,exist_ok=False);out.mkdir(parents=True,exist_ok=False)
    casepath=repo/SOURCE/'campaign/cases'/case
    saved=json.loads((casepath/'results'/case/'RUN.json').read_text())
    for n,h in saved['numeric_witnesses'].items():assert sha(casepath/'results'/case/n)==h
    N,reconstruction=reconstruct(repo,baseline,case,work,saved)
    write(out/'RECONSTRUCTION.json',reconstruction)
    print(json.dumps({'stage':'original_projection_replayed','case':case}),flush=True)
    with np.load(casepath/'results'/case/'SVD_META.npz',allow_pickle=False)as data:
        s=data['singular'];V=data['right_transpose'][:209,:].T.copy()
    U=np.vstack([np.load(casepath/'results'/case/f'U_{i}.npz',allow_pickle=False)['basis']for i in range(3)])
    assert U.shape==(8191,209)and V.shape==(321,209)and s.shape==(321,)
    assert np.isfinite(s).all()and np.all(s>=0)and np.all(s[:-1]>=s[1:])
    sv=[F(*float(x).as_integer_ratio())for x in s]
    assert F(1,1<<24)not in sv and sum(x>F(1,1<<24)for x in sv)==209
    Ui,bU=encode(U);Vi,bV=encode(V);si,bS=encode(s[:209])
    del U,V
    product=fmpz_mat(321,209)
    for begin in range(0,8191,512):
        end=min(8191,begin+512)
        left=fmpz_mat(N[begin:end].astype(object).tolist())
        right=fmpz_mat(Ui[begin:end].tolist())
        product+=left.transpose()*right
    bits=max(55+bU,bV+bS)
    vs=fmpz_mat((Vi*si[None,:]).tolist())
    D=product*(1<<(bits-55-bU))-vs*(1<<(bits-bV-bS))
    nums=[[str(int(v))for v in row]for row in D.tolist()]
    square=F(sum(int(v)**2 for row in nums for v in row),1<<(2*bits))
    upper=root_upper(square)
    payload={'case':case,'shape':[321,209],'Z_denominator_bits':55,
      'U_denominator_bits':bU,'V_denominator_bits':bV,'S_denominator_bits':bS,
      'residual_denominator_bits':bits,'integer_numerators':nums,
      'exact_Frobenius_squared':pair(square),'norm_upper':pair(upper),
      'N_integer_bytes_sha256':saved['projection']['integer_bytes_sha256'],
      'source_numeric_witnesses':saved['numeric_witnesses']}
    body=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
    with(out/'ADJOINT_WITNESS.json.gz').open('xb')as f:f.write(gzip.compress(body,mtime=0))
    print(json.dumps({'stage':'exact_adjoint_measured','case':case,'norm_upper':float(upper)}),flush=True)
    cert=json.loads((repo/SOURCE/'primary'/case/'CERTIFICATE.json').read_text())
    m=cert['row']['measured'];a,b,f=map(rat,[m['etaU'],m['etaV'],m['xi']])
    for value,key in [(a,'left_Gram_F'),(b,'right_Gram_F'),(f,'singular_equation_F')]:
        assert value*value>=rat(m['exact_squared'][key])and value>=0
    prior=json.loads((repo/PRIOR/'primary/CERTIFICATE.json').read_text())
    tail=rat(prior['data_singular_enclosures']['s210_upper'])
    source_lower=rat(prior['data_singular_enclosures']['s209_lower'])
    result=consequences(a,b,f,upper,sv[0],sv[208],tail,sv[209],source_lower)
    valid=result['status']=='CERTIFIED_FINITE_RETAINED_TWO_SIDED_ERROR'
    metrics={k:pair(v)for k,v in result.items()if isinstance(v,F)}
    gates={'strict_leading_block_matching':valid,
      'retained209_absolute_error_below_2^-41':valid and result['retained_abs_error_upper']<F(1,1<<41),
      'all321_absolute_error_below_2^-25':valid and result['all321_abs_error_upper']<F(1,1<<25),
      'ambient_leading_condition_below_reporting1888':valid and result['ambient_leading_condition_upper']<1888,
      'original_source_floor_for_actual_proposal':sv[208]>=source_lower-F(1,1<<41)}
    output={'case':case,'status':result['status'] if all(gates.values())else'HOLD_FINITE_RETAINED_CERTIFICATE_GATE',
      'new_exact_adjoint_norm_squared':pair(square),'new_exact_adjoint_norm_upper':pair(upper),
      'inherited_forward_norm_upper':pair(f),'inherited_left_Gram_upper':pair(a),'inherited_right_Gram_upper':pair(b),
      'inherited_source_tail_upper':pair(tail),'saved_s1':pair(sv[0]),'saved_s209':pair(sv[208]),'saved_s210':pair(sv[209]),
      'bounds':metrics,'gates':gates,'readable':{k:float(v)for k,v in result.items()if isinstance(v,F)},
      'witness_sha256':sha(out/'ADJOINT_WITNESS.json.gz'),'canonical_payload_sha256':hashlib.sha256(body).hexdigest(),
      'freeze_sha256':sha(here/'FREEZE.json'),
      'all321_abs_below_2^-41_established':False,'all_input_backend_conformance':'OPEN',
      'scope':'Finite actual saved computational outputs; new exact adjoint, inherited forward/Gram/source tail premises. No exact spectrum(T) or physical units.',
      'new_estimator_calls':0,'new_record_identities':0,'temporary_replay_record_in_RAM':1,
      'new_factor_archive_copies':0,'forward_and_Gram_norms_recomputed':False,
      'old_output_verdicts_changed':False,'external_promotion_review':'PENDING','physical_promotion':0}
    write(out/'CERTIFICATE.json',output)
    write(out/'RESOURCE.json',{'elapsed_seconds':time.perf_counter()-started,
      'process_peak_RSS_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
      'python':platform.python_version(),'numpy':np.__version__,'scope':'Host-specific original-projection replay and exact adjoint product; no full Hankel or floating fit benchmark'})
    assert sha(baseline)==BASE_SHA
    print(json.dumps({'stage':'finite_retained_certificate','case':case,'status':output['status'],'gates':gates,'readable':output['readable']}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--baseline',required=True)
    p.add_argument('--case',choices=CASES,required=True);p.add_argument('--work',required=True);p.add_argument('--out',required=True)
    q=p.parse_args();main(Path(q.repo).resolve(),Path(q.baseline).resolve(),q.case,Path(q.work).resolve(),Path(q.out).resolve())
