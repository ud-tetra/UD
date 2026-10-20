"""All-entry deterministic CRT audit of a retained adjoint equation witness."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,gzip,hashlib,json,math,time,resource
from pathlib import Path
from fractions import Fraction as F
import numpy as np
P=Path(__file__).resolve().parent
CASES=('boundary_pair_block','boundary_pair_rotating')
SOURCE='captures/2026-10-20T183427Z-codex-maximal-noise-e5831029'
PRIME_START=(1<<24)-1

def need(x,s):
 if not x:raise ValueError(s)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def pair(x):return[str(x.numerator),str(x.denominator)]
def rational(p):
 need(isinstance(p,list)and len(p)==2,'rational pair');need(all(type(v)is int or(type(v)is str and v.lstrip('-').isdigit())for v in p),'rational integer entries');n,d=map(int,p);need(d>0,'positive denominator');return F(n,d)
def fm_ints(x):return np.array([[int(v)for v in row]for row in x],dtype=object)
def encoded(values):
 values=np.asarray(values);need(values.dtype==np.float64 and np.isfinite(values).all(),'finite saved binary64 required')
 ratios=[float(v).as_integer_ratio()for v in values.flat]
 need(all(d>0 and d&(d-1)==0 for _,d in ratios),'dyadic binary64 ratios')
 bits=max(d.bit_length()-1 for _,d in ratios)
 # Independent direct ratio scaling, never the root encoding implementation.
 integers=np.array([(n*(1<<bits))//d for n,d in ratios],dtype=object).reshape(values.shape)
 return integers,bits

def is_prime(n):
 if n<2:return False
 if n==2:return True
 if n%2==0:return False
 return all(n%d for d in range(3,math.isqrt(n)+1,2))
def primes_for_bound(B):
 need(type(B)is int and B>=0,'nonnegative deterministic difference bound');selected=[];product=1;p=PRIME_START
 while not selected or product<=2*B:
  while p>=3 and not is_prime(p):p-=2
  need(p>=3,'prime supply exhausted');selected.append(p);product*=p;p-=2
 return selected,product

def safe_dot_bound(inner,p):
 need(type(inner)is int and inner>0 and type(p)is int and 2<=p<(1<<24),'safe modular dimensions/prime range');bound=inner*(p-1)**2;need(bound<(1<<63),'modular dot product could overflow int64');return bound

def maxabs(x):return max(abs(int(v))for v in np.asarray(x).flat)
def plan(N,Ui,Vi,si,D,bU,bV,bS,bD):
 need(N.ndim==Ui.ndim==Vi.ndim==D.ndim==2 and si.ndim==1,'matrix/vector dimensions');inner,n=N.shape;q=Ui.shape[1]
 need(Ui.shape==(inner,q)and Vi.shape==D.shape==(n,q)and si.shape==(q,),'compatible adjoint shapes')
 k=max(55+bU,bV+bS);need(bD==k,'root residual denominator is not canonical max');scale1=1<<(k-55-bU);scale2=1<<(k-bV-bS)
 terms={'inner_length':inner,'N_max_abs':maxabs(N),'U_integer_max_abs':maxabs(Ui),'V_integer_max_abs':maxabs(Vi),'S_integer_max_abs':maxabs(si),'saved_D_max_abs':maxabs(D),'Ntranspose_U_integer_scale':str(scale1),'VS_integer_scale':str(scale2)}
 term1=inner*terms['N_max_abs']*terms['U_integer_max_abs']*scale1;term2=terms['V_integer_max_abs']*terms['S_integer_max_abs']*scale2;term3=terms['saved_D_max_abs'];B=term1+term2+term3
 primes,product=primes_for_bound(B)
 return {'bits':k,'scale1':scale1,'scale2':scale2,'bound':B,'terms':terms,'term1':term1,'term2':term2,'term3':term3,'primes':primes,'product':product}

def object_mod(x,p):return np.fromiter((int(v)%p for v in np.asarray(x).flat),dtype=np.int64,count=np.asarray(x).size).reshape(np.asarray(x).shape)
def residues(N,Ui,Vi,si,D,policy):
 ps=policy['primes'];need(len(ps)==len(set(ps))and all(is_prime(p)and p<(1<<24)for p in ps),'distinct proved small primes');rows=[];inner=N.shape[0]
 for p in ps:
  bound=safe_dot_bound(inner,p);Nm=np.remainder(N,p).astype(np.int64,copy=False);Um=object_mod(Ui,p);Vm=object_mod(Vi,p);sm=object_mod(si,p);Dm=object_mod(D,p)
  # Nonnegative operands and the bound above make every dot-product partial safe.
  dot=Nm.T@Um;first=np.remainder(np.remainder(dot,p)*pow(2,policy['bits']-55-policy['bU'],p),p)
  second=np.remainder(np.remainder(Vm*sm[None,:],p)*pow(2,policy['bits']-policy['bV']-policy['bS'],p),p);actual=np.remainder(first-second,p);matched=actual==Dm;count=int(np.count_nonzero(matched));mismatches=np.argwhere(~matched)
  rows.append({'prime':p,'prime_proved_by_trial_division':True,'dot_inner_length':inner,'maximum_possible_int64_dot':str(bound),'int64_limit_exclusive':str(1<<63),'elementwise_product_upper':str((p-1)**2),'entry_count':int(D.size),'matching_entries':count,'all_entries_match':count==D.size,'computed_residue_int64le_sha256':hashlib.sha256(actual.astype('<i8').tobytes()).hexdigest(),'saved_residue_int64le_sha256':hashlib.sha256(Dm.astype('<i8').tobytes()).hexdigest(),'first_mismatch':None if len(mismatches)==0 else list(map(int,mismatches[0]))})
 return rows

def verify_crt(policy,checks):
 need(policy['product']==math.prod(policy['primes']),'CRT product differs from prime list')
 need(policy['product']>2*policy['bound'],'CRT product must exceed twice the full difference bound')
 need(len(checks)==len(policy['primes'])and[check['prime']for check in checks]==policy['primes'],'all declared primes checked')
 need(all(type(check['all_entries_match'])is bool and check['all_entries_match']for check in checks),'at least one exact modular matrix entry differs')

def exact_norm(D,bits,witness):
 squared=F(sum(int(v)**2 for v in D.flat),1<<(2*bits));need(squared==rational(witness['exact_Frobenius_squared']),'exact squared norm differs from verified integer witness');upper=rational(witness['norm_upper']);need(upper>=0 and upper*upper>=squared,'root upper does not bound verified exact norm');return {'exact_Frobenius_squared':pair(squared),'root_norm_upper':pair(upper),'root_norm_upper_squared_dominates_exact_norm':True}

def guard(arg):
 lex=Path(os.path.abspath(arg));out=lex.resolve();protected={P.absolute(),P.resolve()}
 for q in(P,*P.parents):
  if(q/'MANIFEST.json').is_file():protected.update((q.absolute(),q.resolve()))
 for q in(lex,out):need(all(q!=a and a not in q.parents and q not in a.parents for a in protected),'protected output or ancestor')
 need(not out.exists(),'new output required');return out

def bindings(repo):
 f=json.loads((P/'FREEZE.json').read_text())
 for n,h in f['files'].items():need(sha(P/n)==h,'review source changed '+n)
 for row in json.loads((P/'SOURCE_BINDINGS.json').read_text())['pins']:need(sha(repo/row['path'])==row['sha256'],'source identity changed '+row['path'])
 return f

def payload_sha(N):
 h=hashlib.sha256()
 for j in range(0,N.shape[0],512):h.update(np.asarray(N[j:j+512],dtype='<i8').tobytes())
 return h.hexdigest()

def one(repo,work,primary,case):
 base=repo/SOURCE/'campaign/cases'/case;data=json.loads((base/'DATA_FREEZE.json').read_text());runfile=json.loads((base/'RUN_EXECUTIONS.json').read_text());need(len(runfile['rows'])==1,'one captured fit tuple');run=runfile['rows'][0];need(data['record']['case']==run['case']==case and data['record']['record_sha256']==run['record_sha256'],'original record identity');need(run['execution_status']=='COMPLETED'and run['learned_order']==209,'original completed retained rank')
 witnessfile=primary/case/'ADJOINT_WITNESS.json.gz';compressed_hash=sha(witnessfile);w=json.loads(gzip.decompress(witnessfile.read_bytes()));need(w['case']==case and w['shape']==[321,209]and w['Z_denominator_bits']==55,'adjoint witness identity/shape');need(w['source_numeric_witnesses']==run['numeric_witnesses'],'root same complete captured tuple');need(w['N_integer_bytes_sha256']==run['projection']['integer_bytes_sha256']==data['record']['projection']['integer_bytes_sha256'],'inherited accepted projection payload identity')
 N=np.load(work/case/'N.npy',mmap_mode='r',allow_pickle=False);need(N.dtype==np.dtype('<i8')and N.shape==(8191,321),'exact source N dimensions/dtype');Nhash=payload_sha(N);need(Nhash==w['N_integer_bytes_sha256'],'temporary N payload hash differs')
 resultdir=base/'results'/case;used={n:sha(resultdir/n)for n in['U_0.npz','U_1.npz','U_2.npz','SVD_META.npz']}
 for n,h in used.items():need(h==run['numeric_witnesses'][n],'captured numeric source changed '+n)
 U=np.vstack([np.load(resultdir/f'U_{j}.npz',allow_pickle=False)['basis']for j in range(3)])
 with np.load(resultdir/'SVD_META.npz',allow_pickle=False)as z:V=z['right_transpose'][:209,:].T.copy();s=z['singular'][:209].copy()
 need(U.shape==(8191,209)and V.shape==(321,209)and s.shape==(209,),'saved adjoint factor dimensions');Ui,bU=encoded(U);Vi,bV=encoded(V);si,bS=encoded(s);D=fm_ints(w['integer_numerators']);need(D.shape==(321,209),'all adjoint integer entries');need([bU,bV,bS]==[w['U_denominator_bits'],w['V_denominator_bits'],w['S_denominator_bits']],'independent binary64 denominator metadata differs')
 bD=w['residual_denominator_bits'];need(type(bD)is int and bD>=0,'nonnegative residual denominator bits');policy=plan(N,Ui,Vi,si,D,bU,bV,bS,bD);policy.update(bU=bU,bV=bV,bS=bS);checks=residues(N,Ui,Vi,si,D,policy)
 row={'case':case,'status':'HOLD_MODULAR_OR_NORM_DIFFERENCE','record_sha256':run['record_sha256'],'witness_compressed_sha256':compressed_hash,'canonical_N_payload_sha256':Nhash,'source_used_numeric_witnesses':used,'independent_denominator_bits':{'U':bU,'V':bV,'S':bS,'D':bD},'entrywise_difference_bound':str(policy['bound']),'difference_bound_terms':policy['terms'],'difference_bound_summands':[str(policy['term1']),str(policy['term2']),str(policy['term3'])],'CRT_product':str(policy['product']),'CRT_product_gt_twice_difference_bound':policy['product']>2*policy['bound'],'all_prime_residue_checks':checks,'checked_matrix_entries_per_prime':D.size,'proof':'Every integer difference is divisible by each distinct prime. Their product exceeds2B while abs(difference)<=B, hence all differences are zero. This is deterministic all-entry equality, not a probabilistic sketch.'}
 try:verify_crt(policy,checks);row.update(status='PASS_DETERMINISTIC_ALL_ENTRY_ADJOINT_CRT_AND_EXACT_NORM',norm=exact_norm(D,bD,w))
 except Exception as exc:row['error']={'type':type(exc).__name__,'message':str(exc)}
 need(sha(witnessfile)==compressed_hash and payload_sha(N)==Nhash,'post-audit source/witness mutation');return row

def run(repo,work,primary,out):
 bindings(repo);start=time.perf_counter();out.mkdir(parents=True,exist_ok=False);rows=[]
 for case in CASES:
  try:row=one(repo,work,primary,case)
  except Exception as exc:row={'case':case,'status':'HOLD_SOURCE_SCHEMA_OR_ARITHMETIC_EXCEPTION','error':{'type':type(exc).__name__,'message':str(exc)}}
  rows.append(row);print(json.dumps({'case':case,'status':row['status'],'primes':len(row.get('all_prime_residue_checks',[]))}),flush=True)
 bindings(repo);result={'status':'COMPLETE_SAME_TEAM_DETERMINISTIC_ADJOINT_MATRIX_AUDIT','rows':rows,'freeze_sha256':sha(P/'FREEZE.json'),'source_bindings_sha256':sha(P/'SOURCE_BINDINGS.json'),'method':'All-entry independent binary64/dyadic encoding and bounded CRT exact equality','independent_raw_projection_claimed':False,'N_scope':'Temporary N payload/dimensions hash-matched to original accepted projection; raw recovery/projection proof inherited from root/source receipts','new_estimator_calls':0,'new_raw_records':0,'new_factor_or_matrix_copies':0,'same_team_review':True,'external_review':'PENDING','physical_promotion':0}
 with(out/'CERTIFICATE.json').open('x')as f:json.dump(result,f,indent=2);f.write('\n')
 with(out/'RESOURCE.json').open('x')as f:json.dump({'elapsed_seconds':time.perf_counter()-start,'process_max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},f,indent=2);f.write('\n')

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--work',required=True);p.add_argument('--primary',required=True);p.add_argument('--out',required=True);a=p.parse_args();run(Path(a.repo).resolve(),Path(a.work).resolve(),Path(a.primary).resolve(),guard(a.out))
