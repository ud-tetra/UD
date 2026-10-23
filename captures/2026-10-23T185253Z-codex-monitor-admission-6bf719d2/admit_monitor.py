"""Monitor graph v0.1: structural review only. Never grants empirical admission.
CLI: python3 admit_monitor.py PACKET CATALOG [CONFIG]
Externally controlled config and catalog are mandatory trust boundaries.
"""
from fractions import Fraction as F
from pathlib import Path,PurePosixPath
from math import isfinite,isqrt
import hashlib,json,re,sys
class Hold(Exception):pass
def need(ok,why):
 if not ok:raise Hold(why)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False)
def sha(x):return hashlib.sha256(x.encode()).hexdigest()
def strict(text):
 def pairs(items):
  d={}
  for k,v in items:need(k not in d,'duplicate JSON key');d[k]=v
  return d
 return json.loads(text,object_pairs_hook=pairs,parse_constant=lambda _:(_ for _ in ()).throw(Hold('nonfinite JSON')))
def rat(x):
 need(isinstance(x,str) and len(x)<=300 and re.fullmatch(r'-?(0|[1-9][0-9]*)(/[1-9][0-9]*)?',x) is not None,'rational encoding');return F(x)
def path(x):need(isinstance(x,str) and x and len(x)<160 and '\\' not in x and not PurePosixPath(x).is_absolute() and '..' not in PurePosixPath(x).parts and str(PurePosixPath(x))==x,'unsafe artifact path')
def shape(x,keys,why):need(isinstance(x,dict) and set(x)==set(keys.split()),why)
DEPS={'samples':[],'clock':[],'iq_path':[],'error_budget':['iq_path'],'source_class':[],'outside_tv':[],'transfer':['source_class','outside_tv','iq_path'],'computation':['samples','clock','error_budget','source_class','outside_tv','transfer'],'tail_tv':['computation']}
ORIGINS={'samples':'acquired_record','clock':'external_calibration','iq_path':'external_calibration','error_budget':'derived_bound','source_class':'independent_source_bound','outside_tv':'independent_source_bound','transfer':'external_calibration','computation':'derived_bound','tail_tv':'derived_bound'}
def gram():
 rows=[];pi=F(22,7);rho=F(1,10**8);eta=F(1,200);tau=F(1,10**8)
 for a in range(100,200):
  row=F(0)
  for b in range(100,200):
   if a==b:continue
   d=abs(a-b);q=d*rho+2*eta*(1+rho);s=1-(pi*(d+q)/1024)**2/6
   need(q<d and d+q<512 and s>0,'Gram guard');row+=q/((d-q)*s)+2*pi*(d+2*eta)*tau
  rows.append(row)
 return 1-max(rows)
def energy(record):
 shape(record,'synthetic_fixture samples','sample format');need(type(record['synthetic_fixture']) is bool,'sample fixture type');need(isinstance(record['samples'],list) and len(record['samples'])==1024,'sample count');e=F(0)
 for pair in record['samples']:
  need(isinstance(pair,list) and len(pair)==2 and all(isinstance(v,str) and len(v)<40 for v in pair),'sample encoding');v=[float.fromhex(x) for x in pair];need(all(isfinite(x) for x in v),'nonfinite sample');need(all(float.hex(x)==s for x,s in zip(v,pair)),'noncanonical sample hex');e+=sum(F(x)**2 for x in v)
 e/=1024;scale=10**12;r=isqrt(e.numerator*scale**2//e.denominator)
 if r*r*e.denominator<e.numerator*scale**2:r+=1
 return e,F(r,scale)
def evaluate(packet,catalog,config):
 result={'status':'HOLD','reasons':[],'empirical_admission':False,'physical_promotion':0,'independent_review':'PENDING','tail_proposal':None,'scope':'Structural bindings, exact arithmetic and external receipt allowlist only. Does not authenticate reviewers, methods, calibration truth or scientific independence.'}
 try:
  need(config.get('validator_sha256')==hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'validator source mismatch');shape(packet,'format synthetic_fixture binding artifacts evidence','packet fields');shape(catalog,'config_sha256 purpose synthetic_fixture approved_receipt_sha256','catalog fields');need(packet['format']=='UD_MONITOR_GRAPH_1','packet version');fixture=packet['synthetic_fixture'];need(type(fixture) is bool and catalog['synthetic_fixture'] is fixture,'fixture mismatch');need(catalog['purpose']=='structure_review_only' and catalog['config_sha256']==sha(canonical(config)),'catalog/config mismatch')
  allow=catalog['approved_receipt_sha256'];need(isinstance(allow,list) and len(allow)<=100 and all(isinstance(h,str) and re.fullmatch('[0-9a-f]{64}',h) for h in allow),'catalog allowlist');need(packet['binding']==config['binding'],'run/channel/epoch/units/kernel/source binding mismatch');binding=packet['binding'];bh=sha(canonical(binding))
  if not fixture:need(not binding['apparatus_run'].startswith(('UNRESOLVED','SYNTHETIC')),'apparatus/run binding unresolved')
  objects=packet['artifacts'];need(isinstance(objects,dict) and len(objects)<=50,'artifact map')
  for name,body in objects.items():path(name);need(isinstance(body,str) and len(body.encode())<=200000,'artifact type/size')
  def load_art(name,h):
   path(name);need(name in objects,'missing witness bytes');need(sha(objects[name])==h,'witness hash mismatch');return strict(objects[name])
  index=packet['evidence'];need(isinstance(index,list) and len(index)<=30,'evidence index');nodes={};roles={};usedpaths=set()
  for item in index:
   shape(item,'id path sha256','index fields');identity=item['id'];need(isinstance(identity,str) and re.fullmatch('[a-z][a-z0-9_]{0,40}',identity),'invalid id');need(identity not in nodes,'duplicate id');need(item['path'] not in usedpaths,'duplicate bound path');usedpaths.add(item['path']);n=load_art(item['path'],item['sha256']);shape(n,'id role binding_sha256 validity origin inputs constructor_id review_path synthetic_fixture payload','node fields');need(n['id']==identity and n['binding_sha256']==bh,'node binding mismatch');need(n['synthetic_fixture'] is fixture,'node fixture mismatch');role=n['role'];need(role in DEPS and role not in roles,'unknown/duplicate role');roles[role]=identity
   shape(n['validity'],'start_s end_s','validity fields');need(rat(n['validity']['start_s'])<=rat(config['coverage']['start_s']) and rat(n['validity']['end_s'])>=rat(config['coverage']['end_s']),'coverage gap');need(isinstance(n['inputs'],list) and all(isinstance(i,str) for i in n['inputs']) and len(set(n['inputs']))==len(n['inputs']),'dependency list');need(isinstance(n['constructor_id'],str) and n['constructor_id'],'constructor missing');path(n['review_path']);need(n['review_path'] in objects,'missing review receipt');rb=objects[n['review_path']];need(sha(rb) in allow,'unapproved review receipt');r=strict(rb)
   shape(r,'node_sha256 binding_sha256 role verdict reviewer_id review_basis witness_sha256 synthetic_fixture','review fields');need(r['node_sha256']==item['sha256'] and r['binding_sha256']==bh and r['role']==role,'review binding mismatch');need(r['verdict']=='SCOPED_BOUND_SUPPORTED' and r['review_basis']=='inspected_method_and_witness_bytes','review scope');need(isinstance(r['reviewer_id'],str) and r['reviewer_id'] and r['reviewer_id']!=n['constructor_id'],'constructor-only review');need(r['synthetic_fixture'] is fixture,'review fixture mismatch')
   refs=n['payload'].get('witnesses',{}) if isinstance(n['payload'],dict) else None;need(isinstance(refs,dict) and refs,'missing method/witness bytes');need(r['witness_sha256']==refs,'review witness mismatch')
   for wp,wh in refs.items():path(wp);need(wp in objects and sha(objects[wp])==wh,'witness hash mismatch')
   nodes[identity]=n
  need(set(roles)==set(DEPS),'missing monitor roles');active=set();done=set()
  def walk(i):
   need(i in nodes,'unknown dependency');need(i not in active,'cyclic dependencies')
   if i in done:return
   active.add(i)
   for d in nodes[i]['inputs']:walk(d)
   active.remove(i);done.add(i)
  for i in nodes:walk(i)
  for role,i in roles.items():
   n=nodes[i];need(n['origin']==ORIGINS[role],'unsupported/circular origin');need(set(n['inputs'])=={roles[d] for d in DEPS[role]},'required dependency set')
  def payload(role,keys):
   p=nodes[roles[role]]['payload'];shape(p,keys+' witnesses',role+' payload fields');return p
  p=payload('samples','path sha256 indices unit reference');need(p['indices']==list(range(1024)) and all(type(i) is int for i in p['indices']),'sample indices');need(p['unit']=='V' and p['reference']=='signed_complex_full_tail_residual','sample unit/reference');rec=load_art(p['path'],p['sha256']);need(p['witnesses'].get(p['path'])==p['sha256'],'unreviewed sample bytes');need(rec['synthetic_fixture'] is fixture,'sample fixture mismatch');e,rms=energy(rec);need(e<=F(11,200000)**2,'digital RMS exceeded')
  p=payload('clock','path sha256 affine_error relative_affine_bound residual_bound_s epoch_s');need(abs(rat(p['affine_error']))<=rat(p['relative_affine_bound'])<=F(1,10**8) and 0<=rat(p['residual_bound_s'])<=F(1,10**8),'clock bounds');need(p['epoch_s']==binding['monitor_epoch_s'],'epoch mismatch');times=load_art(p['path'],p['sha256']);need(p['witnesses'].get(p['path'])==p['sha256'],'unreviewed timestamp bytes');need(isinstance(times,list) and len(times)==1024,'timestamp count')
  for j,t in enumerate(times):
   t=rat(t);need(abs(t-rat(p['epoch_s'])-(1+rat(p['affine_error']))*F(j,1024))<=rat(p['residual_bound_s']),'sample timestamp residual');need(rat(config['coverage']['start_s'])<=t<=rat(config['coverage']['end_s']),'timestamp coverage')
  p=payload('iq_path','operator_error raw_vector_V output_error_V response_scope');need(0<=rat(p['operator_error'])<=F(1,10**6) and 0<=rat(p['raw_vector_V'])<=5,'IQ matrix bounds');need(rat(p['operator_error'])*rat(p['raw_vector_V'])<=rat(p['output_error_V'])<=F(1,200000),'IQ accounting');need(p['response_scope']=='entire_declared_path_frequency_voltage_loading_conditioning_extraction','IQ response scope');iq=rat(p['output_error_V'])
  p=payload('error_budget','shares_V meaning');need(p['meaning']=='deterministic_complex_sample_RMS_triangle_budget','error meaning');shape(p['shares_V'],'acquisition_quantization quadrature_matrix baseline numerical','allocation roles');limits={'acquisition_quantization':F(1,100000),'quadrature_matrix':F(1,200000),'baseline':F(3,10**6),'numerical':F(1,500000)};shares={k:rat(v) for k,v in p['shares_V'].items()};need(all(0<=shares[k]<=v for k,v in limits.items()),'allocation exceeded');need(shares['quadrature_matrix']>=iq,'IQ allocation undercharged');eps=sum(shares.values());need(eps<=F(1,50000),'total error exceeded')
  p=payload('source_class','modes T0_s per_mode_error_Hz common_frequency_Hz coefficient_scope completeness_basis');need(p['modes']==list(range(100,200)) and all(type(i) is int for i in p['modes']) and p['T0_s']=='1','mode family');need(0<=rat(p['per_mode_error_Hz'])<=F(1,200),'frequency error');rat(p['common_frequency_Hz']);need(p['coefficient_scope']=='fixed_coefficients_and_frequencies_on_entire_coverage','nonstationary source');need(p['completeness_basis']=='independent_preparation_and_residual_bound','unsupported source completeness')
  p=payload('outside_tv','value unit direction meaning evidence_basis');need(p['unit']=='V' and p['direction']=='upper' and p['meaning']=='complex_spectral_measure_total_variation','outside TV type');out=rat(p['value']);need(0<=out<=F(1,100000),'outside TV exceeded');need(p['evidence_basis']=='independent_of_acquisition_and_monitor_sample_output','circular outside evidence')
  p=payload('transfer','profile_sha256 acquisition_interval monitor_interval relation coverage_basis');need(p['profile_sha256']==binding['acquisition_profile_sha256'],'transfer profile mismatch');need(p['acquisition_interval']==config['acquisition_interval'] and p['monitor_interval']==config['coverage'],'transfer interval mismatch');need(p['relation']=='same_residual_complex_spectral_measure_on_entire_coverage','transfer reference mismatch');need(p['coverage_basis']=='reviewed_simultaneous_same_preparation_same_epoch','unproven historical transfer');a=config['acquisition_interval'];need(rat(config['coverage']['start_s'])<=rat(a['start_s'])<=rat(a['end_s'])<=rat(config['coverage']['end_s']),'acquisition outside coverage')
  lam=gram();need(lam>=F(9,10) and F(211,20)**2*F(9,10)>=100,'Gram floor');tail=F(211,20)*(F(11,200000)+eps+out)+out;need(tail<=F(1,1000),'tail target exceeded')
  p=payload('computation','method_sha256 contract_sha256 theorem_sha256 exact_energy_V2 rms_ceiling_V lambda_floor norm_factor tail_ceiling_V');need({k:p[k] for k in ['method_sha256','contract_sha256','theorem_sha256']}==config['computation_hashes'],'computation source mismatch');need(rat(p['exact_energy_V2'])==e and rat(p['rms_ceiling_V'])==rms,'digital computation mismatch');need(p['lambda_floor']=='9/10' and p['norm_factor']=='211/20' and rat(p['tail_ceiling_V'])==tail,'Gram/tail computation mismatch')
  p=payload('tail_tv','value unit direction meaning');need(p['unit']=='V' and p['direction']=='upper' and p['meaning']=='deterministic_uniform' and rat(p['value'])==tail,'tail export mismatch')
  result.update(status='STRUCTURALLY_READY_FIXTURE' if fixture else 'STRUCTURALLY_READY_FOR_REVIEW',tail_proposal={'format':'UD_UNSIGNED_MONITOR_TAIL_PROPOSAL_1','status':'AWAITING_INDEPENDENT_REVIEW_NOT_V01_ADMISSION','synthetic_fixture':fixture,'acquisition_profile_sha256':binding['acquisition_profile_sha256'],'binding_sha256':bh,'packet_sha256':sha(canonical(packet)),'config_sha256':sha(canonical(config)),'bound':{'value':str(tail),'unit':'V','direction':'upper','meaning':'deterministic_uniform'},'dependency_roles':sorted(roles),'validity':config['acquisition_interval'],'empirical_admission':False,'physical_promotion':0})
 except (Hold,ValueError,TypeError,KeyError,AttributeError,RecursionError,OverflowError,ZeroDivisionError) as ex:result['reasons']=[str(ex) or type(ex).__name__]
 return result
if __name__=='__main__':
 try:
  p=Path(__file__).resolve().parent;cfg=strict(Path(sys.argv[3]).read_text()) if len(sys.argv)>3 else strict((p/'CONFIG.json').read_text());res=evaluate(strict(Path(sys.argv[1]).read_text()),strict(Path(sys.argv[2]).read_text()),cfg)
 except Exception as ex:res={'status':'HOLD','reasons':[str(ex)],'empirical_admission':False,'physical_promotion':0}
 print(json.dumps(res,indent=2));sys.exit(2 if res['status']=='HOLD' else 0)
