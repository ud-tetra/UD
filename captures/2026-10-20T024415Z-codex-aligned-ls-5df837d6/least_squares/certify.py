"""Zero-fit exact normal-equation witness for two existing saved LS steps."""
import argparse,gzip,hashlib,json,os,resource,time
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from flint import fmpz_mat,arb,fmpq,ctx
ctx.prec=512
P=Path(__file__).resolve().parent
SOURCE='captures/2026-10-20T002112Z-codex-actual-equation-returns-c0caa77d'
CASES=('null_top1_alternating','null_top2_alternating')

def require(x,s):
 if not x:raise ValueError(s)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def pair(x):return [str(x.numerator),str(x.denominator)]
def aa(x):return arb(fmpq(*map(int,x)))
def upper(x):
 n=(arb(x.upper())*(1<<180)).ceil().unique_fmpz();require(n is not None,'HOLD outward upper');return F(int(n),1<<180)
def fm(x):return fmpz_mat(np.asarray(x,dtype=object).tolist())
def decode(x):
 x=np.asarray(x);require(x.dtype==np.float64 and np.isfinite(x).all(),'finite binary64 required')
 v=[float(z).as_integer_ratio()for z in x.flat];b=max(d.bit_length()-1 for _,d in v)
 return np.array([n<<(b-d.bit_length()+1)for n,d in v],dtype=object).reshape(x.shape),b

def guard(arg):
 lex=Path(os.path.abspath(arg));resolved=lex.resolve();protected={P.absolute(),P.resolve()}
 for v in (P,*P.parents):
  if(v/'MANIFEST.json').is_file():protected.update((v.absolute(),v.resolve()))
 for x in (lex,resolved):require(all(x!=a and a not in x.parents and x not in a.parents for a in protected),'protected output or ancestor')
 require(not resolved.exists(),'output must be new');return resolved

def bindings(repo):
 require(__debug__,'assertions required');f=json.loads((P/'FREEZE.json').read_text())
 for n,h in f['files'].items():require(sha(P/n)==h,'frozen source changed '+n)
 for row in json.loads((P/'SOURCE_BINDINGS.json').read_text())['pins']:require(sha(repo/row['path'])==row['sha256'],'source changed '+row['path'])
 return f

def normal_witness(A,B,T,bU,bT):
 require(A.shape==B.shape and A.ndim==2 and T.shape==(A.shape[1],A.shape[1]),'matrix shape')
 q=A.shape[1];G=fmpz_mat(q,q);N=fmpz_mat(q,q);tm=fm(T)
 for begin in range(0,len(A),512):
  end=min(len(A),begin+512);am=fm(A[begin:end]);bm=fm(B[begin:end]);G+=am.transpose()*am;D=am*tm-bm*(1<<bT);N+=am.transpose()*D
 return G,N,2*bU,2*bU+bT

def frob_squared(M,b):return F(sum(int(x)**2 for row in M.tolist()for x in row),1<<(2*b))
def summarize(G,N,bG,bN):
 require(G.nrows()==G.ncols()==N.nrows()==N.ncols()and G==G.transpose(),'symmetric square Gram')
 q=G.nrows();scale=1<<bG;E=fmpz_mat(G)
 for i in range(q):E[i,i]-=scale
 defect=frob_squared(E,bG);gersh=F(min(int(G[i,i])-sum(abs(int(G[i,j]))for j in range(q)if j!=i)for i in range(q)),scale)
 frob_lower=F(1)-upper(aa(pair(defect)).sqrt());floor=max(gersh,frob_lower);sq=frob_squared(N,bN);norm=upper(aa(pair(sq)).sqrt())
 result={'status':'HOLD_NO_POSITIVE_FULL_COLUMN_RANK_FLOOR','Gram_denominator_bits':bG,'normal_denominator_bits':bN,'Gram_minus_I_Frobenius_squared':pair(defect),'Gershgorin_lambda_min_lower':pair(gersh),'identity_minus_Frobenius_lambda_min_lower':pair(frob_lower),'gamma_squared_lower':pair(floor),'normal_Frobenius_squared':pair(sq),'normal_operator_norm_upper':pair(norm),'normal_bound_kind':'Exact dyadic Frobenius upper bounds operator norm','readable_normal_operator_norm_upper':float(norm),'readable_gamma_squared_lower':float(floor)}
 if floor>0:
  distance=upper(aa(pair(norm))/aa(pair(floor)));result.update(status='CERTIFIED_FINITE_SAVED_LS_STEP_DISTANCE',LS_step_operator_distance_upper=pair(distance),readable_LS_step_operator_distance_upper=float(distance))
 return result

def canonical_payload(case,G,N,bG,bN):
 return json.dumps({'case':case,'matrix_shape':[G.nrows(),G.ncols()],'Gram_denominator_bits':bG,'normal_denominator_bits':bN,'Gram_integer_numerators':[[str(int(v))for v in row]for row in G.tolist()],'normal_integer_numerators':[[str(int(v))for v in row]for row in N.tolist()]},sort_keys=True,separators=(',',':')).encode()

def run(repo,out):
 bindings(repo);start=time.perf_counter();out.mkdir(parents=True,exist_ok=False)
 prior=json.loads((repo/SOURCE/'estimator_primary/CERTIFICATE.json').read_text());runs=json.loads((repo/SOURCE/'estimator/RUN_EXECUTIONS.json').read_text());require([r['case']for r in runs['rows']]==list(CASES)==[r['case']for r in prior['rows']],'fixed case order');rows=[]
 for case,run,old in zip(CASES,runs['rows'],prior['rows']):
  row={'case':case,'record_sha256':run['record_sha256'],'old_campaign_status_preserved':old['status'],'old_campaign_gates_preserved':old['gates'],'new_estimator_calls':0}
  try:
   require(run['execution_status']=='COMPLETED'and run['learned_order']==209,'completed retained order209 required');base=repo/SOURCE/'estimator/results'/case
   for n,h in run['numeric_witnesses'].items():require(sha(base/n)==h,'saved factor changed '+n)
   U=np.vstack([np.load(base/f'U_{i}.npz',allow_pickle=False)['basis']for i in range(3)])
   with np.load(base/'PHASE_META.npz',allow_pickle=False)as z:T=z['shift']
   require(U.shape==(8191,209)and T.shape==(209,209),'saved factor shapes');Ui,bU=decode(U);Ti,bT=decode(T);G,N,bG,bN=normal_witness(Ui[:-2],Ui[2:],Ti,bU,bT);result=summarize(G,N,bG,bN)
   payload=canonical_payload(case,G,N,bG,bN);name=case+'_NORMAL_WITNESS.json.gz';body=gzip.compress(payload,mtime=0)
   with(out/name).open('xb')as f:f.write(body)
   row.update(status=result['status'],LS=result,witness_file=name,witness_file_sha256=sha(out/name),witness_file_bytes=len(body),canonical_payload_sha256=hashlib.sha256(payload).hexdigest(),U_denominator_bits=bU,T_denominator_bits=bT)
  except Exception as exc:row.update(status='HOLD_SAVED_LS_CERTIFICATION_EXCEPTION',error={'type':type(exc).__name__,'message':str(exc)},policy='Retain exception; no precision or norm-route retry/replacement')
  rows.append(row);print(json.dumps({'case':case,'status':row['status'],'LS_distance_upper':row.get('LS',{}).get('readable_LS_step_operator_distance_upper')}),flush=True)
 bindings(repo);receipt={'artifact_type':'FINITE_POSTERIOR_SAVED_FLOATING_LS_STEP_CERTIFICATE','status':'COMPLETE_TWO_FIXED_SAVED_OUTPUT_CHECKS','freeze_sha256':sha(P/'FREEZE.json'),'source_bindings_sha256':sha(P/'SOURCE_BINDINGS.json'),'rows':rows,'theorem':'For A full column rank and Tstar=A^dagger B: (A^T A)(T-Tstar)=N=A^T(AT-B), so ||T-Tstar||2 <= ||N||2/lambda_min(A^T A).','new_estimator_calls':0,'new_raw_records':0,'new_factor_copies':0,'known_before_freeze':'Prior U/T, phase and lag bounds already known; actual saved normals/Gamma and LS distances not computed before freeze.','old_campaign_relabelled':False,'universal_backend_rounding_guarantee':False,'exact_T_spectrum_claimed':False,'physical_promotion':0,'external_review':'PENDING'}
 with(out/'CERTIFICATE.json').open('x')as f:json.dump(receipt,f,indent=2);f.write('\n')
 with(out/'RESOURCE.json').open('x')as f:json.dump({'elapsed_seconds':time.perf_counter()-start,'process_max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'scope':'Exact saved-normal witness process; no estimator benchmark'},f,indent=2);f.write('\n')

def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--out',required=True);a=p.parse_args();run(Path(a.repo).resolve(),guard(a.out))
if __name__=='__main__':main()
