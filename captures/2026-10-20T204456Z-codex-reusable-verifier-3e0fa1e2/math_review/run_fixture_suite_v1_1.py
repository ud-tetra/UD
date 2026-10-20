"""Independent subprocess intake tests and exact small-matrix witness checks."""
from pathlib import Path
from fractions import Fraction as F
import gzip,hashlib,json,os,resource,subprocess,sys,time
import numpy as np
P=Path(__file__).resolve().parent;W=P.parent;ROOT=W/'c20_verifier';EX=P/'executions_v1_1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def f(x):return F(int(x[0]),int(x[1]))
def pair(x):return[str(x.numerator),str(x.denominator)]
def T(A):return list(map(list,zip(*A)))
def mm(A,B):return[[sum(x*y for x,y in zip(row,col))for col in zip(*B)]for row in A]
def norm2(A):return sum(x*x for row in A for x in row)
def sub(A,B):return[[x-y for x,y in zip(ar,br)]for ar,br in zip(A,B)]
def diagR(A,s):return[[x*y for x,y in zip(row,s)]for row in A]
def eye(n):return[[int(i==j)for j in range(n)]for i in range(n)]
def unpack(j):
 r,c=j['shape'];v=iter(map(int,j['values']));A=[[0]*c for _ in range(r)]
 for i in range(r):
  for k in range(i if j['storage']=='upper'else 0,c):
   x=next(v);A[i][k]=x
   if j['storage']=='upper':A[k][i]=x
 try:next(v)
 except StopIteration:pass
 else:raise AssertionError('extra packed values')
 return A

def verify_positive(case,out):
 manifest=read(P/case['manifest']);base=(P/case['manifest']).parent
 N=np.load(base/manifest['record']['path'],allow_pickle=False);Ni=[[int(x)for x in row]for row in N.tolist()]
 with np.load(base/manifest['svd']['path'],allow_pickle=False)as z:s=[F.from_float(float(x))for x in z['singular']];vt=z['right_transpose']
 q=sum(x>F(1,2**24)for x in s);U=[]
 for row in manifest['left_chunks']:
  with np.load(base/row['path'],allow_pickle=False)as z:U.extend(z['basis'].tolist())
 Ui=[[int(x)for x in row]for row in U];Vi=[[int(x)for x in row]for row in vt[:q].T.tolist()];Di=[[int(x)for x in row]for row in vt[q:].T.tolist()]
 assert all(F.from_float(float(x)).denominator==1 for row in U for x in row)
 assert all(F.from_float(float(x)).denominator==1 for row in vt.tolist()for x in row)
 M=mm(T(Ni),Ni);K=mm(T(Ni),Ui);A=mm(T(Ui),Ui);B=mm(T(Vi),Vi);E=sub(mm(T(Di),Di),eye(len(s)-q));H=mm(mm(T(Di),M),Di)
 stats={'M':M,'K':K,'A':A,'B':B,'E':E,'H':H};payload=gzip.decompress((out/'WITNESS.json.gz').read_bytes());w=json.loads(payload);cert=read(out/'CERTIFICATE.json')
 checks=[]
 def ck(n,b):
  assert b,(case['case'],n)
  checks.append({'id':n,'pass':True})
 for key,value in stats.items():ck('direct_small_integer_matrix_'+key,unpack(w['matrices'][key])==value)
 ck('canonical_witness',json.dumps(w,sort_keys=True,separators=(',',':')).encode()==payload)
 bN=manifest['record']['dyadic_exponent'];Z=[[F(x,2**bN)for x in row]for row in Ni];Uq=[[F(x)for x in row]for row in Ui];Vq=[[F(x)for x in row]for row in Vi];Dq=[[F(x)for x in row]for row in Di]
 Fr=sub(mm(Z,Vq),diagR(Uq,s[:q]));Gr=sub(mm(T(Z),Uq),diagR(Vq,s[:q]));Wd=mm(Z,Dq)
 exact={'a_squared':norm2(sub(A,eye(q))),'b_squared':norm2(sub(B,eye(q))),'eta_squared':norm2(E),'r_fourth':norm2(mm(T(Wd),Wd)),'f_squared':norm2(Fr),'g_squared':norm2(Gr)}
 for key,value in exact.items():ck('direct_rational_norm_'+key,f(w['exact'][key])==value)
 for key,eq,power in [('a','a_squared',2),('b','b_squared',2),('eta','eta_squared',2),('r','r_fourth',4),('f','f_squared',2),('g','g_squared',2)]:
  upper=f(cert['metrics'][key]);step=F(1,2**180);sq=exact[eq]
  ck('minimal_dyadic_metric_'+key,upper==f(w['metrics'][key]) and upper>=0 and (upper/step).denominator==1 and upper**power>=sq and(upper==0 and sq==0 or upper>0 and(upper-step)**power<sq))
 ck('expected_full_bound',f(cert['bounds']['full_abs_error_upper'])==f(case['expected_bounds']['full_error']))
 if 'condition'in case['expected_bounds']:ck('expected_condition',f(cert['bounds']['ambient_leading_condition_upper'])==f(case['expected_bounds']['condition']))
 if case['case']=='small_retained_residual':
  eps=F(1,2**47);ck('nonzero_retained_condition',(2+eps)/(2-eps)==f(cert['bounds']['ambient_leading_condition_upper']))
 ck('all_fresh_metric_gates_true',all(cert['gates'].values()))
 ck('supplied_bytes_scope',cert['prior_certificate_inputs']==0 and cert['new_estimator_calls']==0 and cert['input_authenticity'].startswith('SUPPLIED_BYTES_ONLY') and cert['all_input_backend_conformance']=='OPEN' and cert['physical_promotion']==0)
 ck('manifest_and_payload_identity',cert['manifest_sha256']==sha(P/case['manifest']) and cert['record_payload_sha256']==manifest['record']['payload_sha256'])
 ck('source_seal_binding',cert['seal_sha256']==sha(ROOT/'SEAL.json') and cert['protocol_sha256']==sha(ROOT/'PROTOCOL.json'))
 ck('witness_hash_binding',cert['witness_sha256']==sha(out/'WITNESS.json.gz'))
 return checks

def limit_process():
 resource.setrlimit(resource.RLIMIT_AS,(2*2**30,2*2**30))
 resource.setrlimit(resource.RLIMIT_CPU,(15,15))

def main():
 EX.mkdir(exist_ok=False);seal=read(ROOT/'SEAL.json')
 for n,h in seal['files'].items():assert sha(ROOT/n)==h
 root_hashes={n:sha(ROOT/n)for n in ['verifier.py','PROTOCOL.json','SEAL.json']}
 index=read(P/'FIXTURES.json');frozen=read(P/'FIXTURE_FREEZE.json');rows=[];env=os.environ.copy();env.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
 for case in index['cases']:
  name=case['case'];manifest=P/case['manifest'];out=EX/name/'result';out.parent.mkdir()
  sentinel=None
  if name=='existing_output_sentinel':out.mkdir();sentinel=out/'KEEP.bin';sentinel.write_bytes(b'UNCHANGED_REVIEW_SENTINEL')
  elif name=='output_is_input_directory':out=manifest.parent
  elif name=='output_is_input_file':out=manifest.parent/'N.npy'
  before={str(x.relative_to(manifest.parent)):sha(x)for x in manifest.parent.rglob('*')if x.is_file()and not x.is_symlink()}
  start=time.perf_counter();cp=subprocess.run([sys.executable,str(ROOT/'verifier.py'),'--manifest',str(manifest),'--out',str(out)],capture_output=True,text=True,timeout=20,env=env,preexec_fn=limit_process)
  messages=[]
  for line in cp.stdout.splitlines():
   try:messages.append(json.loads(line))
   except json.JSONDecodeError:pass
  status=messages[-1].get('status')if messages else None
  after={str(x.relative_to(manifest.parent)):sha(x)for x in manifest.parent.rglob('*')if x.is_file()and not x.is_symlink()}
  unchanged=before==after and(sentinel is None or sentinel.read_bytes()==b'UNCHANGED_REVIEW_SENTINEL')
  expected=case['expected'];checks=[]
  if expected=='CERTIFIED':
   passed=cp.returncode==0 and status=='CERTIFIED_FINITE_SUPPLIED_RECORD'
   if passed:checks=verify_positive(case,out)
  elif expected=='NUMERICAL_HOLD':passed=cp.returncode==2 and status=='HOLD_NUMERICAL'and(out/'CERTIFICATE.json').is_file()and(out/'WITNESS.json.gz').is_file()
  else:passed=cp.returncode==2 and status=='HOLD_INTAKE_OR_INPUT_IO'and(expected=='OUTPUT_REJECTION'or not out.exists())
  passed=passed and unchanged
  row={'case':name,'expected':expected,'returncode':cp.returncode,'status':status,'pass':passed,'input_and_sentinel_bytes_unchanged':unchanged,'output_exists':out.exists(),'positive_checks':checks,'stdout':cp.stdout,'stderr':cp.stderr,'elapsed_seconds':time.perf_counter()-start}
  rows.append(row);print(json.dumps({k:row[k]for k in ['case','expected','returncode','status','pass']}),flush=True)
 for row in frozen['rows']:
  path=P/row['path']
  if'sha256'in row:assert sha(path)==row['sha256'],str(path)
  else:assert path.is_symlink()and os.readlink(path)==row['symlink_target']
 for n,h in root_hashes.items():assert sha(ROOT/n)==h
 result={'status':'PASS_FROZEN38_FIXTURES'if all(x['pass']for x in rows)else'FINDINGS_FROZEN38_FIXTURES','root_package_sha256':root_hashes,'fixture_freeze_sha256':sha(P/'FIXTURE_FREEZE.json'),'cases':rows,'case_count':len(rows),'passed':sum(x['pass']for x in rows),'positive_exact_checks':sum(len(x['positive_checks'])for x in rows),'all_frozen_input_bytes_and_root_source_unchanged':True,'scope':'Finite independent synthetic intake and small exact witness tests, not universal program or backend proof','new_fits':0,'actual_saved_arrays_copied':False,'physical_promotion':0}
 with(P/'FIXTURE_RESULTS_v1_1.json').open('x')as z:json.dump(result,z,indent=2);z.write('\n')
 print(json.dumps({k:result[k]for k in ['status','case_count','passed','positive_exact_checks']}),flush=True)
if __name__=='__main__':main()
