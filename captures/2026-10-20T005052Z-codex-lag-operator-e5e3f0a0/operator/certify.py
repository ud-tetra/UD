"""Separate exact saved-output lag norm refinement; never an estimator call."""
import argparse,gzip,hashlib,importlib.util,json,os,resource,time
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from flint import fmpz_mat,arb,fmpq,ctx
P=Path(__file__).resolve().parent
SOURCE='captures/2026-10-20T002112Z-codex-actual-equation-returns-c0caa77d'
EQUATION='captures/2026-10-19T230959Z-codex-quality-equation-intake-a735ce68/equation'
CASES=('null_top1_alternating','null_top2_alternating')
ctx.prec=512

def require(x,s):
 if not x:raise ValueError(s)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def pair(x):return [str(x.numerator),str(x.denominator)]
def aa(x):return arb(fmpq(*map(int,x)))
def upper(x,b=180):return [str(int((x.upper()*arb(2)**b).ceil().unique_fmpz())),str(1<<b)]
def fm(x):return fmpz_mat(np.asarray(x,dtype=object).tolist())
def decode(x):
 x=np.asarray(x);require(x.dtype==np.float64 and np.isfinite(x).all(),'finite binary64 required')
 v=[float(z).as_integer_ratio()for z in x.flat];b=max(d.bit_length()-1 for _,d in v)
 return np.array([n<<(b-d.bit_length()+1)for n,d in v],dtype=object).reshape(x.shape),b

def guard(arg):
 lex=Path(os.path.abspath(arg));resolved=lex.resolve();protect={P,P.resolve()}
 for v in (P,*P.parents):
  if(v/'MANIFEST.json').is_file():protect.update((v.absolute(),v.resolve()))
 for x in (lex,resolved):
  require(all(x!=a and a not in x.parents and x not in a.parents for a in protect),'protected output or ancestor')
 require(not resolved.exists(),'output must be new');return resolved

def check_bindings(repo):
 f=json.loads((P/'FREEZE.json').read_text())
 for name,h in f['files'].items():require(sha(P/name)==h,'frozen source changed '+name)
 s=json.loads((P/'SOURCE_BINDINGS.json').read_text())
 for row in s['pins']:require(sha(repo/row['path'])==row['sha256'],'source pin changed '+row['path'])
 m=json.loads((repo/SOURCE/'MANIFEST.json').read_text())
 for row in m['files']:
  p=repo/row['path'];require(p.stat().st_size==row['size_bytes']and sha(p)==row['sha256'],'prior capture changed '+row['path'])
 return f

def gram_direct(U,bU,T,bT):
 require(U.shape==(8191,209)and T.shape==(209,209),'saved shape differs')
 G=fmpz_mat(209,209);tm=fm(T)
 for begin in range(0,8189,512):
  end=min(8189,begin+512)
  D=fm(U[begin+2:end+2])*(1<<bT)-fm(U[begin:end])*tm
  G+=D.transpose()*D
 return G,bU+bT

def gram_equal(G,H):
 require(G==H,'provided Gram is not the exactly constructed residual Gram')

def bounds(G,b,cap=F(1,1<<34)):
 require(cap>0,'positive cap required');n=G.nrows();require(n>0 and n==G.ncols(),'square Gram required')
 require(G==G.transpose(),'Gram must be symmetric')
 require(all(G[i,i]>=0 for i in range(n)),'Gram diagonal negative')
 scale=1<<(2*b);tr=F(sum(int(G[i,i])for i in range(n)),scale)
 row=F(max(sum(abs(int(G[i,j]))for j in range(n))for i in range(n)),scale)
 sq=F(sum(int(x)**2 for z in G.tolist()for x in z),scale*scale)
 # PSD is not inferred from symmetry: caller must construct or independently match D^T D.
 candidates=[('trace',aa(pair(tr))),('absolute_row_sum',aa(pair(row))),('Gram_Frobenius',aa(pair(sq)).sqrt())]
 name,lam=candidates[0]
 for k,v in candidates[1:]:
  if v<lam:name,lam=k,v
 norm=lam.sqrt();proofs={'trace':tr<=cap*cap,'absolute_row_sum':row<=cap*cap,'Gram_Frobenius':sq<=cap**4}
 return {'status':'CERTIFIED_OPERATOR_NORM_AT_FIXED_CAP'if any(proofs.values())else'HOLD_NO_DECLARED_BOUND_MEETS_CAP','positive_cap':pair(cap),'residual_denominator_bits':b,'trace':pair(tr),'absolute_row_sum':pair(row),'Gram_Frobenius_squared':pair(sq),'squared_cap_tests':proofs,'selected_bound':name,'operator_norm_upper':upper(norm),'readable_operator_norm_upper':float(norm.upper()),'squared_Frobenius_equal_trace':pair(tr),'PSD_premise':'Verified exact construction D^T D; this function alone does not prove arbitrary input PSD'}

def phase_implication(repo,old,sA):
 path=repo/EQUATION/'certify.py';spec=importlib.util.spec_from_file_location('source_equation_refinement',path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);_,c=m.bound(repo)
 prior=json.loads((repo/'captures/2026-10-19T222108Z-codex-uniform-phase-evidence-4a6f6bda/phase/primary/CERTIFICATE.json').read_text());C=c.aa(prior['sketch']['per_62_vector_noise_multiplier_upper'])
 override={k:old['measured'][k]for k in ['etaU','etaV','xi','proposed_smin']};override['sA']=sA
 for own,other in [('rho','inverse_residual'),('h','proposed_inverse_norm'),('eV','eigenpair_residual'),('a','emitted_argument_error')]:override[own]=old['phase']['metrics'][other]
 caps=json.loads((repo/SOURCE/'estimator/inputs/EQUATION_CAPS.json').read_text())['quality_caps']
 gates={k:bool(aa(override[k])<=aa(caps[k]))for k in ['etaU','etaV','xi','sA','rho','h','eV','a']}
 gates['measured_singular_floor']=old['gates']['measured_singular_floor'];gates['direct_finite_phase_quality']=old['gates']['finite_saved_phase_quality']
 result=m.evaluate(repo,c,C,[3,1<<49],override);gates['measured_phase_implication']=result['status']=='CERTIFIED_UNIFORM_PHASE_TARGET_BIJECTION'
 return {'status':'CERTIFIED_SEPARATE_OPERATOR_ROUTE_FINITE_SAVED_OUTPUT'if all(gates.values())else'HOLD_SEPARATE_OPERATOR_ROUTE','gates':gates,'measured_implication':result,'all_other_metrics_inherited_from_prior_exact_certificate':True,'uniform_backend_success':False}

def run(repo,out):
 f=check_bindings(repo);start=time.perf_counter();out.mkdir(parents=True,exist_ok=False)
 old=json.loads((repo/SOURCE/'estimator_primary/CERTIFICATE.json').read_text());runs=json.loads((repo/SOURCE/'estimator/RUN_EXECUTIONS.json').read_text());rows=[]
 require([x['case']for x in old['rows']]==list(CASES)==[x['case']for x in runs['rows']],'fixed cases differ')
 for case,previous,run in zip(CASES,old['rows'],runs['rows']):
  require(run['execution_status']=='COMPLETED'and run['learned_order']==209,'prior fit/order not completed')
  base=repo/SOURCE/'estimator/results'/case
  for name,h in run['numeric_witnesses'].items():require(sha(base/name)==h,'saved witness changed '+name)
  U=np.vstack([np.load(base/f'U_{i}.npz',allow_pickle=False)['basis']for i in range(3)])
  with np.load(base/'PHASE_META.npz',allow_pickle=False)as z:T=z['shift']
  Ui,bU=decode(U);Ti,bT=decode(T);G,b=gram_direct(Ui,bU,Ti,bT)
  q=bounds(G,b);require(q['trace']==previous['measured']['exact_squared']['raw_lag_F'],'Gram trace differs from prior exact Frobenius residual')
  payload={'case':case,'matrix_shape':[209,209],'U_denominator_bits':bU,'T_denominator_bits':bT,'residual_denominator_bits':b,'gram_numerators':[[str(int(v))for v in row]for row in G.tolist()]}
  raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();name=case+'_GRAM.json.gz';(out/name).write_bytes(gzip.compress(raw,mtime=0))
  phase=phase_implication(repo,previous,q['operator_norm_upper'])
  row={'case':case,'record_sha256':run['record_sha256'],'prior_campaign_status_preserved':previous['status'],'prior_gates_preserved':previous['gates'],'norm':q,'new_operator_route':phase,'Gram_file':name,'Gram_file_sha256':sha(out/name),'canonical_Gram_payload_sha256':hashlib.sha256(raw).hexdigest(),'Gram_file_bytes':(out/name).stat().st_size,'new_estimator_calls':0};rows.append(row)
  print(json.dumps({'case':case,'norm_status':q['status'],'norm_upper':q['readable_operator_norm_upper'],'separate_route':phase['status'],'prior_campaign_status_preserved':previous['status']}),flush=True)
 check_bindings(repo)
 result={'artifact_type':'SEPARATE_POSTKNOWN_SAVED_LAG_OPERATOR_NORM_REFINEMENT','status':'COMPLETE_TWO_FIXED_SAVED_OUTPUT_CHECKS','freeze_sha256':sha(P/'FREEZE.json'),'source_bindings_sha256':sha(P/'SOURCE_BINDINGS.json'),'rows':rows,'known_prior_outcomes':'Both Frobenius values and finite phases known before freeze; exact residual Grams and operator bounds not computed before freeze','new_estimator_calls':0,'new_raw_records':0,'new_factor_copies':0,'old_campaign_relabelled':False,'old_reconstruction_no_go_unchanged':True,'uniform_backend_success':False,'external_review':'PENDING','physical_promotion':0}
 (out/'CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n')
 (out/'RESOURCE.json').write_text(json.dumps({'elapsed_seconds':time.perf_counter()-start,'process_max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'scope':'Host-specific exact saved Gram process, not estimator or full Hankel benchmark'},indent=2)+'\n')

def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--out',required=True);a=p.parse_args();run(Path(a.repo).resolve(),guard(a.out))
if __name__=='__main__':main()
