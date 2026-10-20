"""Exact discarded-right-subspace operator certificate; no estimator calls.

N is the original projected integer matrix retained after PR286, hash-bound to
the original accepted projection. Source raw/projection lineage is inherited.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,gzip,hashlib,json,math,platform,resource,time
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from flint import fmpz_mat

SOURCE='captures/2026-10-20T183427Z-codex-maximal-noise-e5831029'
RETAINED='captures/2026-10-20T195008Z-codex-adjoint-spectrum-8fcfe9c3'
CASES=('boundary_pair_block','boundary_pair_rotating')

def sha(p):
    h=hashlib.sha256()
    with p.open('rb')as f:
        for x in iter(lambda:f.read(1048576),b''):h.update(x)
    return h.hexdigest()
def pair(x):return[str(x.numerator),str(x.denominator)]
def rat(p):return F(int(p[0]),int(p[1]))
def write(p,j):
    with p.open('x')as f:f.write(json.dumps(j,indent=2,sort_keys=True)+'\n')
def encode(x):
    assert x.dtype==np.float64 and np.isfinite(x).all()
    ratios=[float(v).as_integer_ratio()for v in x.flat]
    b=max(d.bit_length()-1 for _,d in ratios)
    return np.array([n<<(b-d.bit_length()+1)for n,d in ratios],dtype=object).reshape(x.shape),b
def root_upper(x,power,bits=180):
    assert x>=0 and power in (2,4)
    n=x.numerator<<(power*bits);d=x.denominator
    k=math.isqrt(n//d)
    if power==4:k=math.isqrt(k)
    if k**power*d<n:k+=1
    y=F(k,1<<bits)
    assert y**power>=x and (k==0 or F(k-1,1<<bits)**power<x)
    return y
def squared(M,b):return F(sum(int(v)**2 for row in M.tolist()for v in row),1<<(2*b))

def derived(eta,r,a,b,f,g,s1,sq,s210):
    assert 0<=eta<1 and r>=0 and 0<=a<1 and 0<=b<1 and f>=0 and g>=0 and s1>=sq>0 and s210>=0
    tail=r/(1-eta)
    compression=(s1*(a/(2-a)+b/(2-b))+f)/(1-b)
    cross=max(f/(1-b),g/(1-a));eps=compression+cross
    gap=sq-compression-tail-cross
    if gap<=0:return {'status':'HOLD_NO_NEW_DIRECT_TAIL_MATCHING_GAP','direct_tail_upper':tail,'matching_gap':gap}
    assert sq-eps>0
    return {'status':'DIRECT_TAIL_LEADING_BLOCK_MATCHED',
      'direct_tail_upper':tail,'compression_upper':compression,'offdiagonal_upper':cross,
      'retained_abs_error_upper':eps,'discarded_abs_error_upper':max(tail,s210),
      'full321_abs_error_upper':max(eps,tail,s210),'matching_gap':gap,
      'ambient_sigma209_lower':sq-eps,'ambient_leading_condition_upper':(s1+eps)/(sq-eps)}

def main(repo,projected,case,out):
    start=time.perf_counter();here=Path(__file__).resolve().parent
    freeze=json.loads((here/'FREEZE.json').read_text())
    for n,h in freeze['code'].items():assert sha(here/n)==h,('code',n)
    for n,row in freeze['sources'].items():
        p=repo/n;assert p.stat().st_size==row['size_bytes']and sha(p)==row['sha256'],('source',n)
    out.mkdir(parents=True,exist_ok=False)
    runpath=repo/SOURCE/'campaign/cases'/case/'results'/case/'RUN.json';run=json.loads(runpath.read_text())
    assert run['case']==case and run['learned_order']==209 and run['execution_status']=='COMPLETED'
    N=np.load(projected,mmap_mode='r',allow_pickle=False)
    assert N.dtype==np.dtype('<i8')and N.shape==(8191,321)
    nhash=hashlib.sha256(np.asarray(N,dtype='<i8').tobytes()).hexdigest()
    assert nhash==run['projection']['integer_bytes_sha256']
    svpath=runpath.parent/'SVD_META.npz';assert sha(svpath)==run['numeric_witnesses']['SVD_META.npz']
    with np.load(svpath,allow_pickle=False)as z:
        V=z['right_transpose'][209:321,:].T.copy();s=z['singular']
    assert V.shape==(321,112)and s.shape==(321,)and s.dtype==np.float64
    assert np.isfinite(s).all()and np.all(s>=0)and np.all(s[:-1]>=s[1:])
    sv=[F(*float(x).as_integer_ratio())for x in s]
    tau=F(1,1<<24);assert tau not in sv and sum(x>tau for x in sv)==209
    Vi,bV=encode(V);vm=fmpz_mat(Vi.tolist());E=vm.transpose()*vm
    for j in range(112):E[j,j]-=1<<(2*bV)
    H=fmpz_mat(112,112)
    for begin in range(0,8191,512):
        stop=min(8191,begin+512)
        W=fmpz_mat(N[begin:stop].astype(object).tolist())*vm
        H+=W.transpose()*W
    esq=squared(E,2*bV);hsq=squared(H,2*(55+bV))
    eta=root_upper(esq,2);r=root_upper(hsq,4)
    # No alternate operator route or precision retry is selected if this fails.
    assert eta<1,'HOLD discarded factor lacks validated full column rank'
    tail=r/(1-eta)
    witness={'case':case,'shape':[112,112],'retained_q':209,'tail_columns':112,
      'Z_denominator_bits':55,'V_denominator_bits':bV,
      'V_gram_defect_denominator_bits':2*bV,'tail_output_gram_denominator_bits':2*(55+bV),
      'V_gram_defect_integer_numerators':[[str(int(x))for x in row]for row in E.tolist()],
      'tail_output_gram_integer_numerators':[[str(int(x))for x in row]for row in H.tolist()],
      'exact_V_gram_defect_F_squared':pair(esq),'exact_tail_output_gram_F_squared':pair(hsq),
      'etaV_upper':pair(eta),'tail_output_norm_upper':pair(r),'tail_sigma210_upper':pair(tail),
      'N_integer_bytes_sha256':nhash,'source_SVD_META_sha256':sha(svpath)}
    body=json.dumps(witness,sort_keys=True,separators=(',',':')).encode()
    with(out/'TAIL_WITNESS.json.gz').open('xb')as f:f.write(gzip.compress(body,mtime=0))
    print(json.dumps({'stage':'exact_tail_Grams','case':case,'eta':float(eta),'tail_upper':float(tail)}),flush=True)
    old=json.loads((repo/RETAINED/'primary'/case/'CERTIFICATE.json').read_text())
    a,b,f,g=map(rat,[old['inherited_left_Gram_upper'],old['inherited_right_Gram_upper'],old['inherited_forward_norm_upper'],old['new_exact_adjoint_norm_upper']])
    answer=derived(eta,r,a,b,f,g,sv[0],sv[208],sv[209])
    matched=answer['status']=='DIRECT_TAIL_LEADING_BLOCK_MATCHED'
    if matched:
        for key in ['compression_upper','offdiagonal_upper','retained_abs_error_upper','ambient_leading_condition_upper']:
            assert answer[key]==rat(old['bounds'][key]),('unchanged retained arithmetic',key)
    gates={'discarded_right_factor_validated_full_rank':eta<1,'strict_matching_with_direct_tail':matched,
      'full321_abs_error_below_2^-41':matched and answer['full321_abs_error_upper']<F(1,1<<41),
      'direct_tail_below_cutoff':tail<tau,
      'retained_lower_above_cutoff':matched and answer['ambient_sigma209_lower']>tau}
    output={'status':'CERTIFIED_FINITE_FULL321_ABSOLUTE_ERROR_BELOW_2^-41'if all(gates.values())else'HOLD_FINITE_FULL321_TARGET',
      'case':case,'gates':gates,'direct_tail_eta_upper':pair(eta),'direct_tail_output_norm_upper':pair(r),
      'bounds':{k:pair(v)for k,v in answer.items()if isinstance(v,F)},
      'readable':{k:float(v)for k,v in answer.items()if isinstance(v,F)},
      'saved_s210':pair(sv[209]),'prior_retained_certificate_sha256':sha(repo/RETAINED/'primary'/case/'CERTIFICATE.json'),
      'new_witness_sha256':sha(out/'TAIL_WITNESS.json.gz'),'canonical_payload_sha256':hashlib.sha256(body).hexdigest(),
      'freeze_sha256':sha(here/'FREEZE.json'),'N_integer_bytes_sha256':nhash,
      'old_nominal_tail_bound_used_in_current_full321_proof':False,
      'inherited_premises':['Original projected input lineage','Original retained forward/Gram bounds','PR286 exact adjoint bound and its independent CRT audit'],
      'new_raw_or_projection_reconstruction':False,'new_estimator_calls':0,'new_record_identities':0,
      'new_stored_factor_copies':0,'source_retained_norms_recomputed':False,'all_input_backend_conformance':'OPEN',
      'algebraic_rank209_claimed':False,'full_matrix_condition_claimed':False,
      'external_promotion_review':'PENDING','physical_promotion':0}
    write(out/'CERTIFICATE.json',output)
    write(out/'RESOURCE.json',{'elapsed_seconds':time.perf_counter()-start,'process_peak_RSS_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'python':platform.python_version(),'numpy':np.__version__,'scope':'Exact discarded factor/output Gram computation; not full pipeline/Hankel benchmark'})
    assert hashlib.sha256(np.asarray(N,dtype='<i8').tobytes()).hexdigest()==nhash
    print(json.dumps({'stage':'full321_tail_certificate','case':case,'status':output['status'],'gates':gates,'readable':output['readable']}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--projected',required=True)
    p.add_argument('--case',choices=CASES,required=True);p.add_argument('--out',required=True);q=p.parse_args()
    main(Path(q.repo).resolve(),Path(q.projected).resolve(),q.case,Path(q.out).resolve())
