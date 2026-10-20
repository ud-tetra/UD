"""Postknown saved-factor box certificate, fixed Z and eigenpair proposals. No fitting."""
import argparse,hashlib,importlib.util,json,os,resource,time
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from flint import arb,fmpq,ctx
P=Path(__file__).resolve().parent
BASE='captures/2026-10-20T002112Z-codex-actual-equation-returns-c0caa77d'
OP='captures/2026-10-20T005052Z-codex-lag-operator-e5e3f0a0'
EQ='captures/2026-10-19T230959Z-codex-quality-equation-intake-a735ce68/equation'
OLD='captures/2026-10-19T222108Z-codex-uniform-phase-evidence-4a6f6bda/phase'
CASES=('null_top1_alternating','null_top2_alternating');GRID=tuple(range(20,101));ctx.prec=512

def req(x,msg):
 if not x:raise ValueError(msg)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for z in iter(lambda:f.read(1048576),b''):h.update(z)
 return h.hexdigest()
def frac(p):return F(int(p[0]),int(p[1]))
def pair(q):return [str(q.numerator),str(q.denominator)]
def aa(q):
 if not isinstance(q,F):q=frac(q)
 return arb(fmpq(q.numerator,q.denominator))
def up(x):return F(int((arb(x.upper())*(1<<180)).ceil().unique_fmpz()),1<<180)
def down(x):return F(int((arb(x.lower())*(1<<180)).floor().unique_fmpz()),1<<180)
def frob_squared(x):
 x=np.asarray(x);req(x.dtype==np.float64 and np.isfinite(x).all(),'finite float64 source required')
 values=[float(v).as_integer_ratio()for v in x.flat];b=max(d.bit_length()-1 for _,d in values)
 return F(sum((n<<(b-d.bit_length()+1))**2 for n,d in values),1<<(2*b))
def guard(arg):
 lex=Path(os.path.abspath(arg));out=lex.resolve();protect={P,P.resolve()}
 for p in (P,*P.parents):
  if(p/'MANIFEST.json').is_file():protect.update((p.absolute(),p.resolve()))
 for x in (lex,out):req(all(x!=p and p not in x.parents and x not in p.parents for p in protect),'protected output or ancestor')
 req(not out.exists(),'output must be new');return out

def bind(repo):
 f=json.loads((P/'FREEZE.json').read_text())
 for name,h in f['files'].items():req(sha(P/name)==h,'local freeze changed '+name)
 source=json.loads((P/'SOURCE_BINDINGS.json').read_text())
 for row in source['pins']:req(sha(repo/row['path'])==row['sha256'],'source changed '+row['path'])
 for capture in (BASE,OP):
  m=json.loads((repo/capture/'MANIFEST.json').read_text())
  for row in m['files']:
   p=repo/row['path'];req(p.stat().st_size==row['size_bytes']and sha(p)==row['sha256'],'prior capture changed '+row['path'])
 return f

def envelopes(c,u,v,s,t):
 req(all(x>=0 for x in (u,v,s,t)),'nonnegative typed perturbation radii required')
 return {'etaU':c['etaU']+2*c['U']*u+u*u,'etaV':c['etaV']+2*c['V']*v+v*v,
         'xi':c['xi']+c['Z']*v+c['Sigma']*u+c['U']*s+u*s,
         'sA':c['ell']+(1+c['T'])*u+c['U']*t+u*t,
         'eV':c['eV']+c['W']*t,'proposed_smin':c['smin']-s,
         'rho':c['rho'],'h':c['h'],'a':c['a']}

def constants(repo,case,old,data,op):
 p=repo/BASE/'estimator/results'/case
 with np.load(p/'PHASE_META.npz',allow_pickle=False)as z:T=z['shift'];W=z['eigenvectors']
 with np.load(p/'SVD_META.npz',allow_pickle=False)as z:sv=z['singular']
 req(T.shape==W.shape==(209,209)and W.dtype==np.complex128,'saved factor shapes or type differ')
 req(sv.dtype==np.float64 and sv.shape==(321,)and np.isfinite(sv).all()and np.all(sv>=0),'saved diagonal invalid')
 t2=frob_squared(T);w2=frob_squared(np.r_[W.real.ravel(),W.imag.ravel()].astype(np.float64))
 measured=old['measured'];c={k:frac(measured[k])for k in ('etaU','etaV','xi')}
 c.update(U=up((1+aa(c['etaU'])).sqrt()),V=up((1+aa(c['etaV'])).sqrt()),T=up(aa(t2).sqrt()),W=up(aa(w2).sqrt()),Sigma=F(*float(max(sv[:209])).as_integer_ratio()),smin=F(*float(min(sv[:209])).as_integer_ratio()),ell=frac(op['norm']['operator_norm_upper']))
 c['Z']=up((arb(8191*321).sqrt()*arb(data['projection']['numerator_max'])/(1<<55)))
 req(c['smin']==frac(measured['proposed_smin']),'saved minimum differs from exact prior certificate')
 for own,other in [('eV','eigenpair_residual'),('rho','inverse_residual'),('h','proposed_inverse_norm'),('a','emitted_argument_error')]:c[own]=frac(old['phase']['metrics'][other])
 witness={'shift_Frobenius_squared_exact':pair(t2),'eigenbasis_Frobenius_squared_exact':pair(w2),'Z_bound_origin':'sqrt(8191*321)*prior_exact_integer_projection_max/2^55; no raw matrix loaded','projection_numerator_max':data['projection']['numerator_max'],'U_V_norm_origin':'sqrt(1+prior_exact_Gram_defect_upper)','Sigma_origin':'maximum/minimum first209 saved real diagonal entries, not exact singular values of Z','new_factor_copies':0}
 return c,witness

def source_phase(repo):
 p=repo/EQ/'certify.py';spec=importlib.util.spec_from_file_location('source_phase_for_box',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);_,ar=m.bound(repo)
 source=json.loads((repo/OLD/'primary/CERTIFICATE.json').read_text());C=ar.aa(source['sketch']['per_62_vector_noise_multiplier_upper'])
 floor_data=json.loads((repo/BASE/'estimator/inputs/PARENT_ORDER.json').read_text());floor=ar.aa(floor_data['qth_sigma_lower'])-C*ar.aa([3,1<<49])-ar.aa([1,1<<41])
 return m,ar,C,floor

def evaluate(c,k,caps,source,repo):
 e=F(1,1<<k);b=envelopes(c,e,e,e,e);m,ar,C,floor=source
 gates={name:b[name]<=frac(caps[name])for name in ('etaU','etaV','xi','sA','rho','h','eV','a')}
 gates['positive_measured_singular_floor']=bool(floor>0 and aa(b['proposed_smin'])>=floor)
 row={'k':k,'typed_common_radius':pair(e),'bounds':{n:pair(v)for n,v in b.items()},'fixed_gates':gates}
 if all(gates.values()):
  proof=m.evaluate(repo,ar,C,[3,1<<49],{n:pair(v)for n,v in b.items()})
  row['phase']=proof;row['status']='CERTIFIED_WHOLE_TYPED_FACTOR_BOX'if proof['status']=='CERTIFIED_UNIFORM_PHASE_TARGET_BIJECTION'else'HOLD_PHASE_ENVELOPE'
 else:row.update(status='HOLD_INSUFFICIENT_QUALITY_ENVELOPE',phase={'status':'NOT_EVALUATED_QUALITY_GATES_HOLD'})
 return row

def run(repo,out):
 bind(repo);out.mkdir(parents=True,exist_ok=False);started=time.perf_counter();old=json.loads((repo/BASE/'estimator_primary/CERTIFICATE.json').read_text());data=json.loads((repo/BASE/'estimator/DATA_FREEZE.json').read_text());ops=json.loads((repo/OP/'primary/CERTIFICATE.json').read_text());caps=json.loads((repo/BASE/'estimator/inputs/EQUATION_CAPS.json').read_text())['quality_caps'];source=source_phase(repo);rows=[];tau=F(1,1<<34)
 req([r['case']for r in old['rows']]==[r['case']for r in data['records']]==[r['case']for r in ops['rows']]==list(CASES),'fixed cases changed')
 for case,previous,datum,op in zip(CASES,old['rows'],data['records'],ops['rows']):
  c,witness=constants(repo,case,previous,datum,op);grid=[evaluate(c,k,caps,source,repo)for k in GRID]
  passed=[r for r in grid if r['status']=='CERTIFIED_WHOLE_TYPED_FACTOR_BOX'];req(bool(passed),'no grid box certified; retain HOLD outputs')
  lag_grid=[]
  for k in GRID:
   e=F(1,1<<k);lag=c['ell']+(1+c['T']+c['U'])*e+e*e;lag_grid.append({'k':k,'typed_lag_radius':pair(e),'lag_upper':pair(lag),'cap_pass':lag<=tau})
  lag_pass=[r for r in lag_grid if r['cap_pass']];req(bool(lag_pass),'no lag grid box certified')
  slack=tau-c['ell'];K=1+c['T']+c['U'];req(slack>0,'positive lag margin required');root=2*aa(slack)/(aa(K)+(aa(K*K+4*slack)).sqrt())
  selected=passed[0];lag_selected=lag_pass[0];prior=next((r for r in grid if r['k']==selected['k']-1),None)
  entry={'case':case,'source_record_sha256':previous['record_sha256'],'prior_campaign_status_preserved':previous['status'],'constants':{n:pair(v)for n,v in c.items()},'constant_witnesses':witness,'lag_slack_exact':pair(slack),'lag_only_continuous_bound_lower':pair(down(root)),'lag_only_continuous_bound_upper':pair(up(root)),'lag_only_largest_grid_certified':lag_selected,'joint_largest_grid_certified':selected,'next_larger_grid_envelope_failures':None if prior is None else[n for n,v in prior['fixed_gates'].items()if not v],'all_joint_grid_rows':grid,'all_lag_only_grid_rows':lag_grid,'all_other_metrics_source_premises_inherited':True,'fixed_eigenpair_and_emission_proposals':True,'raw_noise_tolerance_claimed':False}
  rows.append(entry);print(json.dumps({'case':case,'joint_k':selected['k'],'lag_only_k':lag_selected['k'],'next_larger_envelope_failures':entry['next_larger_grid_envelope_failures'],'phase_bound':selected['phase'].get('readable_phase_error_upper')}),flush=True)
 bind(repo)
 result={'artifact_type':'POSTKNOWN_SOURCE_BOUND_SAVED_FACTOR_BOX_BUDGET','status':'COMPLETE_TWO_FIXED_SAVED_FACTOR_BUDGETS','freeze_sha256':sha(P/'FREEZE.json'),'source_bindings_sha256':sha(P/'SOURCE_BINDINGS.json'),'rows':rows,'scope':'Z and W,Lambda,H,emitted phases fixed; real diagonal Sigma changes and operator-norm changes of U,V,T only; all points in typed box covered conditionally','grid_k':list(GRID),'new_estimator_calls':0,'new_raw_records':0,'new_factor_copies':0,'actual_perturbed_factors_generated':0,'raw_noise_to_solver_map_proved':False,'uniform_backend_success':False,'old_campaign_relabelled':False,'old_reconstruction_no_go_unchanged':True,'external_review':'PENDING','physical_promotion':0}
 (out/'CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n');(out/'RESOURCE.json').write_text(json.dumps({'elapsed_seconds':time.perf_counter()-started,'process_max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'scope':'Host-specific exact saved-factor norm and envelope-grid verification; no estimator or full Hankel benchmark'},indent=2)+'\n')

def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--out',required=True);a=p.parse_args();run(Path(a.repo).resolve(),guard(a.out))
if __name__=='__main__':main()
