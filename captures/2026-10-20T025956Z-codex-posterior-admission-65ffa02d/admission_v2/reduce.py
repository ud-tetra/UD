"""Historical-only hash-pinned posterior admission integration; never numerical execution."""
import argparse,hashlib,json,os
from pathlib import Path
from fractions import Fraction as F
P=Path(__file__).resolve().parent
PROFILE='OPERATOR_POSTERIOR_ADMISSION_v0.1'
CASES=('null_top1_alternating','null_top2_alternating')
S='captures/2026-10-20T002112Z-codex-actual-equation-returns-c0caa77d'
O='captures/2026-10-20T005052Z-codex-lag-operator-e5e3f0a0'
L='captures/2026-10-20T024415Z-codex-aligned-ls-5df837d6'

def need(x,s):
 if not x:raise ValueError(s)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def rational(x):
 need(isinstance(x,list)and len(x)==2,'rational pair required')
 need(all(type(v)is int or(type(v)is str and v.lstrip('-').isdigit())for v in x),'rational integers required')
 n,d=map(int,x);need(d>0,'positive denominator required');return F(n,d)
def yes(x):return type(x)is bool and x
PHASE_GATES={'inverse_residual','proposed_inverse_norm','eigenpair_residual','emitted_argument_error','emission_ties_even_consistency','finite_observed_bijection'}
ROUTE_GATES={'etaU','etaV','xi','sA','rho','h','eV','a','measured_singular_floor','direct_finite_phase_quality','measured_phase_implication'}
def exact_gates(d,keys):return type(d)is dict and set(d)==keys and all(yes(v)for v in d.values())
def strict_disks(imp):
 radius=rational(imp['eigenvalue_radius_upper']);half=rational(imp['source_half_chord_lower'])
 return 0<=radius<1 and radius<half and 0<=rational(imp['phase_error_upper'])<half and rational(imp['phase_matching_margin_lower'])>0
def rows(x,key='rows'):
 z=x[key];need(isinstance(z,list)and len(z)==2,'two case rows required');need([r['case']for r in z]==list(CASES),'fixed unique case order required');return z
def cap(value,limit):return rational(value)>=0 and rational(value)<=rational(limit)
def digest(x):return isinstance(x,str)and len(x)==64 and all(c in '0123456789abcdef'for c in x)
def guard(arg):
 lex=Path(os.path.abspath(arg));out=lex.resolve();protected={P.absolute(),P.resolve()}
 for q in(P,*P.parents):
  if(q/'MANIFEST.json').is_file():protected.update((q.absolute(),q.resolve()))
 for q in(lex,out):need(all(q!=a and a not in q.parents and q not in a.parents for a in protected),'protected output or ancestor')
 need(not out.exists(),'new output required');return out

def frozen():
 need(__debug__,'assertions required');f=json.loads((P/'FREEZE.json').read_text())
 for n,h in f['files'].items():need(sha(P/n)==h,'frozen local source changed '+n)
 p=json.loads((P/'PROFILE.json').read_text());need(p['profile_id']==PROFILE,'profile identity');return p

def load(repo,profile):
 bundle={}
 for role,pin in profile['inputs'].items():
  path=repo/pin['path'];need(path.stat().st_size==pin['bytes']and sha(path)==pin['sha256'],'untrusted historical input '+role);bundle[role]=json.loads(path.read_text())
 return bundle

def source_pin(bindings,path):
 matches=[r['sha256']for r in bindings['pins']if r['path']==path];need(len(matches)==1 and digest(matches[0]),'unique source pin '+path);return matches[0]
def manifest_pin(manifest,path):
 matches=[r['sha256']for r in manifest['files']if r['path']==path];need(len(matches)==1 and digest(matches[0]),'unique manifest pin '+path);return matches[0]

def identity(bundle,profile):
 b=bundle;inputs=profile['inputs']
 need(b['actual']['protocol_sha256']==inputs['protocol']['sha256']==b['data']['protocol_sha256'],'protocol chain')
 need(b['actual']['data_freeze_sha256']==inputs['data']['sha256']==b['runs']['data_freeze_sha256']==b['projection']['data_freeze_sha256'],'data chain')
 need(b['actual']['run_executions_sha256']==inputs['runs']['sha256'],'run chain')
 need(b['operator']['source_bindings_sha256']==inputs['operator_sources']['sha256'],'operator sources chain');need(b['least_squares']['source_bindings_sha256']==inputs['LS_sources']['sha256'],'LS sources chain')
 for binds in[b['operator_sources'],b['LS_sources']]:
  need(source_pin(binds,S+'/MANIFEST.json')==inputs['actual_manifest']['sha256'],'same saved capture manifest')
  need(source_pin(binds,S+'/estimator/RUN_EXECUTIONS.json')==inputs['runs']['sha256'],'same exact saved execution')
  need(source_pin(binds,S+'/estimator_primary/CERTIFICATE.json')==inputs['actual']['sha256'],'same exact output certificate')
 need(b['data']['status']=='ALL_TWO_DATA_CHECKED_BEFORE_ANY_FIT'and b['projection']['status']=='ALL_TWO_INDEPENDENT_PROJECTION_HASH_MATCH','frozen independent input proof')
 for role in['actual','runs','operator','least_squares','projection']:rows(b[role])
 rows(b['data'],'records');need(b['protocol']['cases']==list(CASES),'source cases')
 caps=b['caps']['quality_caps'];need({k:rational(v)for k,v in caps.items()}=={k:rational(v)for k,v in profile['original_quality_caps'].items()},'original exact caps changed')
 return caps

def one(case,index,b,p,caps):
 old=b['actual']['rows'][index];run=b['runs']['rows'][index];data=b['data']['records'][index];pr=b['projection']['rows'][index];op=b['operator']['rows'][index];ls=b['least_squares']['rows'][index]
 record=data['record_sha256'];need(digest(record)and all(r['record_sha256']==record for r in[old,run,op,ls]),'cross-record identity')
 need(old['status']==p['original_statuses'][case]==op['prior_campaign_status_preserved']==ls['old_campaign_status_preserved'],'old status immutable')
 need(old['gates']==op['prior_gates_preserved']==ls['old_campaign_gates_preserved'],'old gates immutable')
 need(old['execution_status']=='COMPLETED'and old['learned_order']==209==run['learned_order']and run['execution_status']=='COMPLETED','actual saved order209')
 need(run['projection']==data['projection']and pr['exact_projected_numerator_sha256']==data['projection']['integer_bytes_sha256']and yes(pr['matches_independent_review']),'exact source projection identity')
 need(record==p['cases'][case]['record_sha256']and data['projection']==p['cases'][case]['projection'],'registered source/projection identity')
 need(data['baseline_sha256']==p['baseline_sha256'],'nominal baseline identity')
 witnesses=run['numeric_witnesses'];need(set(witnesses)=={'SVD_META.npz','U_0.npz','U_1.npz','U_2.npz','PHASE_META.npz','PHASE_PROPOSAL.npz'},'complete saved witness set')
 for name,h in witnesses.items():
  path=S+'/estimator/results/'+case+'/'+name;need(digest(h)and manifest_pin(b['actual_manifest'],path)==h,'exact saved witness identity '+name)
  if name.startswith('U_')or name=='PHASE_META.npz':need(source_pin(b['LS_sources'],path)==h,'LS same U/T witness '+name)
 # PR258 verifies this complete manifest; PR263 additionally pins each U/T byte hash.
 need(manifest_pin(b['actual_manifest'],S+'/estimator/results/'+case+'/RUN.json')==source_pin(b['LS_sources'],S+'/estimator/results/'+case+'/RUN.json'),'same single-fit RUN identity')
 m=old['measured'];ph=old['phase'];pm=ph['metrics'];n=op['norm'];route=op['new_operator_route'];imp=route['measured_implication'];g={}
 for key in['etaU','etaV','xi']:g[key]=cap(m[key],caps[key])
 for key,name in[('rho','inverse_residual'),('h','proposed_inverse_norm'),('eV','eigenpair_residual'),('a','emitted_argument_error')]:g[key]=cap(pm[name],caps[key])
 g['positive_inverse_norm']=rational(pm['proposed_inverse_norm'])>0;g['Gram_defects_below_one']=all(rational(m[k])<1 for k in['etaU','etaV']);g['inverse_residual_below_one']=rational(pm['inverse_residual'])<1
 need(n['selected_bound']=='Gram_Frobenius','fixed Gram-Frobenius route only');bound=rational(n['operator_norm_upper']);squareF=rational(n['Gram_Frobenius_squared']);g['sA']=0<=squareF<=rational(caps['sA'])**4 and 0<=bound<=rational(caps['sA'])and bound**4>=squareF
 g['lag_original_cap']=rational(n['positive_cap'])==rational(caps['sA']);g['lag_exact_trace_binding']=rational(n['trace'])==rational(m['exact_squared']['raw_lag_F'])
 floor=rational(old['required_singular_floor_lower']);g['positive_certified_singular_premise']=yes(old['gates']['measured_singular_floor'])and floor>0 and rational(m['proposed_smin'])>=floor and yes(old['conditional_implication']['requires_measured_singular_floor'])and floor==rational(imp['required_proposed_singular_floor_lower'])
 g['conditional_phase_premise']=route['status']=='CERTIFIED_SEPARATE_OPERATOR_ROUTE_FINITE_SAVED_OUTPUT'and imp['status']=='CERTIFIED_UNIFORM_PHASE_TARGET_BIJECTION'and yes(imp['requires_measured_singular_floor'])and rational(imp['noise_radius'])==rational(p['noise_radius'])and strict_disks(imp)
 g['source_unchanged_numerical_gates']=exact_gates(route['gates'],ROUTE_GATES)and yes(route['all_other_metrics_inherited_from_prior_exact_certificate'])
 obs=ph['observed'];em=obs['rows'];half=rational(obs['source_minimum_chord_lower'])/2
 g['finite_saved_phase_qualification']=ph['status']=='CERTIFIED_FINITE_EMITTED_MATCH_AND_SAVED_NUMERICAL_QUALITY'and exact_gates(ph['gates'],PHASE_GATES)and obs['status']=='CERTIFIED_FINITE_EMITTED_TWO_STEP_BIJECTION'and yes(obs['bijective'])and len(em)==209 and {r['emitted_index']for r in em}==set(range(209))and {r['target_index']for r in em}==set(range(209))and all(yes(r['unique_and_within_fixed_radius'])and 0<=rational(r['circular_error_upper'])<half for r in em)and 0<=rational(obs['maximum_circular_error_upper'])<half
 q=ls['LS'];lf=rational(q['gamma_squared_lower']);normal=rational(q['normal_operator_norm_upper']);distance=rational(q['LS_step_operator_distance_upper'])
 g['positive_LS_floor']=ls['status']==q['status']=='CERTIFIED_FINITE_SAVED_LS_STEP_DISTANCE'and lf>0 and lf==max(rational(q['Gershgorin_lambda_min_lower']),rational(q['identity_minus_Frobenius_lambda_min_lower']))
 g['finite_LS_normal_bound']=normal>=0 and normal**2>=rational(q['normal_Frobenius_squared'])>=0 and distance>=0 and distance*lf>=normal
 need(all(g.values()),'posterior gate failure '+','.join(k for k,v in g.items()if not v))
 return {'case':case,'record_sha256':record,'status':'HISTORICAL_FINITE_OPERATOR_PROFILE_ADMISSIBLE','gates':g,'original_campaign_status_preserved':old['status'],'original_campaign_gates_preserved':old['gates'],'new_profile_lag_operator_upper':n['operator_norm_upper'],'reported_LS_step_distance_upper':q['LS_step_operator_distance_upper'],'saved_witness_set':witnesses,'proof_scope':'Hash-pinned independently reviewed historical exact arithmetic receipts consumed; no matrices reverified by this reducer.'}

def historical(repo,profile):
 b=load(repo,profile);caps=identity(b,profile);out=[]
 for i,case in enumerate(CASES):
  try:out.append(one(case,i,b,profile,caps))
  except Exception as exc:out.append({'case':case,'status':'HOLD_POSTERIOR_SCHEMA_CUSTODY_OR_GATE','error':{'type':type(exc).__name__,'message':str(exc)},'original_campaign_status_preserved':profile['original_statuses'][case]})
 return out

def run(repo,out,mode):
 result={'artifact_type':'POSTKNOWN_HISTORICAL_OPERATOR_PROFILE_REDUCTION','profile_id':PROFILE,'historical_outcomes_known_before_freeze':True,'new_estimator_calls':0,'new_raw_records':0,'new_factor_copies':0,'independent_matrix_reverification':False,'fresh_numerical_verifier_implemented':False,'fresh_protocol_status':'INCOMPLETE_UNEXECUTED','old_campaign_relabelled':False,'universal_backend_success':False,'physical_promotion':0}
 try:
  p=frozen()
  if mode!='historical':result.update(status='HOLD_FOREIGN_OR_UNVERIFIED_FRESH_BUNDLE',reason='Historical registry only; fresh actual numerical verification and release absent')
  else:result.update(status='COMPLETE_TWO_HISTORICAL_LOGICAL_REDUCTIONS',rows=historical(repo,p),freeze_sha256=sha(P/'FREEZE.json'),profile_sha256=sha(P/'PROFILE.json'))
 except Exception as exc:result.update(status='HOLD_PROFILE_SCHEMA_OR_CUSTODY',error={'type':type(exc).__name__,'message':str(exc)})
 out.mkdir(parents=True,exist_ok=False)
 with(out/'CERTIFICATE.json').open('x')as f:json.dump(result,f,indent=2);f.write('\n')
 print(json.dumps({'status':result['status'],'rows':[{k:r[k]for k in['case','status']}for r in result.get('rows',[])]}),flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--out',required=True);ap.add_argument('--mode',default='historical');a=ap.parse_args()
 try:run(Path(a.repo).resolve(),guard(a.out),a.mode)
 except Exception as exc:print(json.dumps({'status':'HOLD_UNSAFE_OUTPUT_OR_IO','error':{'type':type(exc).__name__,'message':str(exc)}}),flush=True)
