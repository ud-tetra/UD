"""All-entry deterministic CRT audit of tail-factor and tail-output Gram witnesses."""
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
PREFIX='captures/2026-10-20T195008Z-codex-adjoint-spectrum-8fcfe9c3'

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
def plan(N,Vi,E,H,bV):
 need(N.ndim==Vi.ndim==E.ndim==H.ndim==2,'matrix dimensions');m,n=N.shape;q=Vi.shape[1];need(Vi.shape==(n,q)and E.shape==H.shape==(q,q),'compatible tail shapes')
 M=maxabs(N);V=maxabs(Vi);ME=maxabs(E);MH=maxabs(H);BE=n*V*V+(1<<(2*bV))+ME;BH=m*(n*M*V)**2+MH;B=max(BE,BH);primes,product=primes_for_bound(B)
 return {'m':m,'n':n,'q':q,'bV':bV,'BE':BE,'BH':BH,'bound':B,'primes':primes,'product':product,'terms':{'N_max_abs':str(M),'V_integer_max_abs':str(V),'saved_E_max_abs':str(ME),'saved_H_max_abs':str(MH),'rows_N':m,'columns_N':n,'identity_integer_scale':str(1<<(2*bV))},'E_summands':[str(n*V*V),str(1<<(2*bV)),str(ME)],'H_summands':[str(m*(n*M*V)**2),str(MH)]}

def object_mod(x,p):return np.fromiter((int(v)%p for v in np.asarray(x).flat),dtype=np.int64,count=np.asarray(x).size).reshape(np.asarray(x).shape)
def residue_row(actual,saved,p):
 eq=actual==saved;count=int(np.count_nonzero(eq));bad=np.argwhere(~eq)
 return {'entry_count':int(actual.size),'matching_entries':count,'all_entries_match':count==actual.size,'computed_residue_int64le_sha256':hashlib.sha256(actual.astype('<i8').tobytes()).hexdigest(),'saved_residue_int64le_sha256':hashlib.sha256(saved.astype('<i8').tobytes()).hexdigest(),'first_mismatch':None if len(bad)==0 else list(map(int,bad[0]))}

def residues(N,Vi,E,H,policy):
 ps=policy['primes'];need(len(ps)==len(set(ps))and all(is_prime(p)and p<(1<<24)for p in ps),'distinct proved small primes');checks=[]
 for p in ps:
  firstbound=safe_dot_bound(policy['n'],p);secondbound=safe_dot_bound(policy['m'],p);Nm=np.remainder(N,p).astype(np.int64,copy=False);Vm=object_mod(Vi,p)
  # Each modular matrix product uses nonnegative residues and its own full safe dot bound.
  Wm=np.remainder(Nm@Vm,p);Hm=np.remainder(Wm.T@Wm,p);Em=np.remainder(Vm.T@Vm,p)
  for j in range(policy['q']):Em[j,j]-=pow(2,2*policy['bV'],p)
  Em=np.remainder(Em,p);Er=object_mod(E,p);Hr=object_mod(H,p)
  checks.append({'prime':p,'prime_proved_by_trial_division':True,'int64_limit_exclusive':str(1<<63),'N_V_and_V_Gram_dot_inner':policy['n'],'N_V_and_V_Gram_dot_max':str(firstbound),'W_Gram_dot_inner':policy['m'],'W_Gram_dot_max':str(secondbound),'modular_identity_scale':pow(2,2*policy['bV'],p),'E':residue_row(Em,Er,p),'H':residue_row(Hm,Hr,p)})
 return checks

def verify_crt(policy,checks):
 need(policy['product']==math.prod(policy['primes'])and policy['product']>2*policy['bound'],'sufficient actual CRT product required');need(policy['bound']==max(policy['BE'],policy['BH']),'common max bound required');need(len(checks)==len(policy['primes'])and[x['prime']for x in checks]==policy['primes'],'all declared primes checked')
 need(all(type(c[k]['all_entries_match'])is bool and c[k]['all_entries_match']for c in checks for k in['E','H']),'at least one exact modular E/H entry differs')

def norm_squared(M,bits):return F(sum(int(v)**2 for v in M.flat),1<<(2*bits))
def scalar_bounds(E,H,bV,w):
 ES=norm_squared(E,2*bV);HS=norm_squared(H,2*(55+bV));need(ES==rational(w['exact_V_gram_defect_F_squared']),'verified exact E square differs');need(HS==rational(w['exact_tail_output_gram_F_squared']),'verified exact H square differs');eta=rational(w['etaV_upper']);r=rational(w['tail_output_norm_upper']);sigma=rational(w['tail_sigma210_upper'])
 need(0<=eta<1 and eta*eta>=ES,'eta is not a positive-rank Gram-defect enclosure');need(r>=0 and r**4>=HS,'tail norm is not a fourth-root enclosure');need(sigma>=0 and sigma*(1-eta)>=r,'sigma210 scalar quotient is not enclosed')
 return {'exact_V_gram_defect_F_squared':pair(ES),'exact_tail_output_gram_F_squared':pair(HS),'etaV_upper':pair(eta),'tail_output_norm_upper':pair(r),'tail_sigma210_upper':pair(sigma),'eta_squared_dominates_E_square':True,'tail_norm_fourth_power_dominates_H_square':True,'positive_rank_eta_below_one':True,'sigma_times_one_minus_eta_dominates_tail_norm':True,'scope':'Verified scalar enclosures; minimal180-bit wrappers and downstream theorem/prefix receipts reviewed separately'}

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
 base=repo/SOURCE/'campaign/cases'/case;data=json.loads((base/'DATA_FREEZE.json').read_text());runfile=json.loads((base/'RUN_EXECUTIONS.json').read_text());need(len(runfile['rows'])==1,'one captured tuple');run=runfile['rows'][0];need(data['record']['case']==run['case']==case and data['record']['record_sha256']==run['record_sha256'],'source record identity');need(run['execution_status']=='COMPLETED'and run['learned_order']==209,'accepted source retained order209')
 wf=primary/case/'TAIL_WITNESS.json.gz';wh=sha(wf);w=json.loads(gzip.decompress(wf.read_bytes()));need(w['case']==case and w['shape']==[112,112]and w['retained_q']==209 and w['tail_columns']==112 and w['Z_denominator_bits']==55,'tail witness identity/shape');need(w['N_integer_bytes_sha256']==run['projection']['integer_bytes_sha256']==data['record']['projection']['integer_bytes_sha256'],'inherited accepted N identity')
 N=np.load(work/case/'N.npy',mmap_mode='r',allow_pickle=False);need(N.dtype==np.dtype('<i8')and N.shape==(8191,321),'source N dtype/shape');Nh=payload_sha(N);need(Nh==w['N_integer_bytes_sha256'],'temporary N payload differs')
 sf=base/'results'/case/'SVD_META.npz';Sh=sha(sf);need(Sh==w['source_SVD_META_sha256']==run['numeric_witnesses']['SVD_META.npz'],'same exact saved right factors')
 with np.load(sf,allow_pickle=False)as z:vt=z['right_transpose']
 need(vt.dtype==np.float64 and vt.shape==(321,321),'full saved right factor dimensions');Vi,bV=encoded(vt[209:321,:].T.copy());need(w['V_denominator_bits']==bV and w['V_gram_defect_denominator_bits']==2*bV and w['tail_output_gram_denominator_bits']==2*(55+bV),'independently encoded tail denominator metadata')
 E=fm_ints(w['V_gram_defect_integer_numerators']);H=fm_ints(w['tail_output_gram_integer_numerators']);need(E.shape==H.shape==(112,112),'complete E/H shapes');policy=plan(N,Vi,E,H,bV);checks=residues(N,Vi,E,H,policy)
 row={'case':case,'status':'HOLD_TAIL_MATRIX_OR_SCALAR_CHECK','record_sha256':run['record_sha256'],'witness_compressed_sha256':wh,'canonical_N_payload_sha256':Nh,'source_SVD_META_sha256':Sh,'independent_tail_denominator_bits':bV,'E_difference_bound':str(policy['BE']),'H_difference_bound':str(policy['BH']),'common_difference_bound':str(policy['bound']),'difference_bound_terms':policy['terms'],'E_difference_bound_summands':policy['E_summands'],'H_difference_bound_summands':policy['H_summands'],'CRT_product':str(policy['product']),'CRT_product_gt_twice_common_bound':policy['product']>2*policy['bound'],'all_prime_residue_checks':checks,'entries_per_matrix':int(E.size),'proof':'Each integer E/H entry difference has absolute value<=its full bound<=common B and is divisible by every distinct prime. Product>2B implies exact equality of every entry.'}
 try:verify_crt(policy,checks);row.update(status='PASS_ALL_ENTRY_TAIL_E_H_CRT_AND_SCALAR_ENCLOSURES',scalars=scalar_bounds(E,H,bV,w))
 except Exception as exc:row['error']={'type':type(exc).__name__,'message':str(exc)}
 need(sha(wf)==wh and payload_sha(N)==Nh and sha(sf)==Sh,'post-audit witness/source mutation');return row

def run(repo,work,primary,out):
 bindings(repo);start=time.perf_counter();out.mkdir(parents=True,exist_ok=False);rows=[]
 for case in CASES:
  try:row=one(repo,work,primary,case)
  except Exception as exc:row={'case':case,'status':'HOLD_SOURCE_SCHEMA_OR_ARITHMETIC_EXCEPTION','error':{'type':type(exc).__name__,'message':str(exc)}}
  rows.append(row);print(json.dumps({'case':case,'status':row['status'],'primes':len(row.get('all_prime_residue_checks',[]))}),flush=True)
 bindings(repo);result={'status':'COMPLETE_SAME_TEAM_DETERMINISTIC_TAIL_MATRIX_AUDIT','rows':rows,'freeze_sha256':sha(P/'FREEZE.json'),'source_bindings_sha256':sha(P/'SOURCE_BINDINGS.json'),'method':'Independent binary64 ratio encoding; all-entry bounded CRT with independent two-stage modular H composition','independent_raw_projection_claimed':False,'N_scope':'Temporary N payload/dimensions hash-match accepted original projection; raw recovery/projection proof inherited','prefix_PR286_norm_proofs':'INHERITED_NOT_RECOMPUTED','new_estimator_calls':0,'new_raw_records':0,'new_factor_or_matrix_copies':0,'same_team_review':True,'external_review':'PENDING','physical_promotion':0}
 with(out/'CERTIFICATE.json').open('x')as f:json.dump(result,f,indent=2);f.write('\n')
 with(out/'RESOURCE.json').open('x')as f:json.dump({'elapsed_seconds':time.perf_counter()-start,'process_max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},f,indent=2);f.write('\n')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--work',required=True);p.add_argument('--primary',required=True);p.add_argument('--out',required=True);a=p.parse_args();run(Path(a.repo).resolve(),Path(a.work).resolve(),Path(a.primary).resolve(),guard(a.out))
