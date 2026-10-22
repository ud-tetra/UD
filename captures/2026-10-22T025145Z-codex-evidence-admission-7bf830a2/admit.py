"""Fail-closed evidence packet structure checker. Never grants empirical admission.
Usage: python3 admit.py packet.json trusted_catalog.json
The catalog must come from a separate externally controlled review process.
"""
from fractions import Fraction
from pathlib import PurePosixPath,Path
import hashlib,json,re,sys
REQUIREMENTS={
 'inband_tv':('V','upper','1'), 'envelope_band':('Hz','upper','50'),
 'tail_tv':('V','upper','1/1000'), 'full_amplitude':('V','lower','1/2'),
 'tail_absolute_frequency':('Hz','upper','200000'), 'constant_baseline':('V','upper','3'),
 'noise_quantization':('V','upper','1/10000'), 'relative_gain':('1','upper','1/100000'),
 'time_error':('s','upper','1/5000000000'), 'clean_slope':('V/s','upper','250000'),
 'baseline_variation':('V','upper','1/20000'), 'input_magnitude':('V','upper','5')}
class Hold(Exception):pass
def check(condition,reason):
 if not condition:raise Hold(reason)
def digest(text):return hashlib.sha256(text.encode('utf-8')).hexdigest()
def canonical(obj):return json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=False)
def strict_load(text):
 def pairs(items):
  out={}
  for k,v in items:
   check(k not in out,'duplicate JSON key');out[k]=v
  return out
 return json.loads(text,object_pairs_hook=pairs,parse_constant=lambda _: (_ for _ in ()).throw(Hold('nonfinite JSON')))
def rational(v):
 check(isinstance(v,str) and re.fullmatch(r'-?(0|[1-9][0-9]*)(/[1-9][0-9]*)?',v) is not None,'noncanonical rational')
 check(len(v)<=160,'oversized rational');return Fraction(v)
def safe_path(p):
 check(isinstance(p,str) and p and not PurePosixPath(p).is_absolute() and '..' not in PurePosixPath(p).parts and '\\' not in p,'unsafe artifact path')
 check(str(PurePosixPath(p))==p,'noncanonical artifact path')
def evaluate(packet,catalog,expected_profile):
 reasons=[]
 def run():
  check(set(packet)=={'format','profile','synthetic_fixture','artifacts','evidence'},'packet fields')
  check(set(catalog)=={'profile_sha256','purpose','synthetic_fixture','approved_receipt_sha256'},'catalog fields')
  approved=catalog['approved_receipt_sha256'];check(isinstance(approved,list) and all(isinstance(x,str) and re.fullmatch('[0-9a-f]{64}',x) for x in approved),'catalog hash list')
  check(packet.get('format')=='UD_QUADRATURE_EVIDENCE_1','packet version')
  check(packet.get('profile')==expected_profile,'profile mismatch')
  ph=digest(canonical(expected_profile));check(catalog.get('profile_sha256')==ph,'catalog profile mismatch')
  check(catalog.get('purpose')=='structure_review_only','catalog purpose')
  check(type(catalog.get('synthetic_fixture')) is bool,'catalog fixture designation')
  check(type(packet.get('synthetic_fixture')) is bool and packet['synthetic_fixture']==catalog['synthetic_fixture'],'fixture mismatch')
  if not packet['synthetic_fixture']:check(not expected_profile['apparatus_run'].startswith('UNRESOLVED'),'apparatus/run binding unresolved')
  objects=packet.get('artifacts');check(isinstance(objects,dict),'missing artifact map')
  for name,body in objects.items():safe_path(name);check(isinstance(body,str) and len(body)<200000,'artifact type/size')
  index=packet.get('evidence');check(isinstance(index,list) and len(index)<=100,'evidence index')
  nodes={};byrole={}
  for item in index:
   check(isinstance(item,dict) and set(item)=={'id','path','sha256'},'index fields')
   identity=item['id'];check(isinstance(identity,str) and re.fullmatch(r'[A-Za-z][A-Za-z0-9_]{0,63}',identity),'invalid id');check(identity not in nodes,'duplicate evidence id')
   safe_path(item['path']);check(item['path'] in objects,'missing artifact bytes');body=objects[item['path']]
   check(digest(body)==item['sha256'],'artifact hash mismatch');node=strict_load(body)
   check(set(node)=={'id','role','profile_sha256','bound','validity','origin','inputs','constructor_id','review_path','synthetic_fixture'},'bound fields')
   check(node['id']==identity and node['profile_sha256']==ph,'bound identity/profile mismatch')
   check(node['synthetic_fixture'] is packet['synthetic_fixture'],'bound fixture mismatch')
   role=node['role'];check(role in REQUIREMENTS,'unknown role');check(role not in byrole,'duplicate evidence role');byrole[role]=identity
   unit,direction,limit=REQUIREMENTS[role];b=node['bound'];check(isinstance(b,dict) and set(b)=={'value','unit','direction','meaning'},'bound shape')
   check(b['unit']==unit,'unit mismatch');check(b['direction']==direction,'bound direction mismatch');check(b['meaning']=='deterministic_uniform','statistical/undefined bound')
   value=rational(b['value']);check(value>=0,'negative bound');threshold=Fraction(limit)
   check(value<=threshold if direction=='upper' else value>=threshold,'requirement exceeded')
   v=node['validity'];check(isinstance(v,dict) and set(v)=={'start_s','end_s'},'validity shape')
   check(rational(v['start_s'])<=rational(expected_profile['start_s']) and rational(v['end_s'])>=rational(expected_profile['end_s']),'coverage gap')
   check(node['origin'] in ['external_calibration','independent_source_bound','derived_bound'],'unsupported/circular origin')
   check(isinstance(node['inputs'],list) and len(set(node['inputs']))==len(node['inputs']) and all(isinstance(i,str) for i in node['inputs']),'input references')
   check(node['origin']!='derived_bound' or node['inputs'],'unanchored derivation')
   check(isinstance(node['constructor_id'],str) and node['constructor_id'],'constructor missing')
   review=node['review_path'];safe_path(review);check(review in objects,'missing review receipt')
   receipt_body=objects[review];receipt_hash=digest(receipt_body);check(receipt_hash in catalog.get('approved_receipt_sha256',[]),'receipt not externally approved')
   receipt=strict_load(receipt_body)
   check(set(receipt)=={'evidence_sha256','profile_sha256','role','verdict','reviewer_id','review_basis','synthetic_fixture'},'review fields')
   check(receipt['evidence_sha256']==item['sha256'] and receipt['profile_sha256']==ph and receipt['role']==role,'review binding mismatch')
   check(receipt['verdict']=='SCOPED_BOUND_SUPPORTED' and receipt['review_basis']=='inspected_method_and_witness_bytes','insufficient review scope')
   check(isinstance(receipt['reviewer_id'],str) and receipt['reviewer_id'] and receipt['reviewer_id']!=node['constructor_id'],'constructor-only review')
   check(receipt['synthetic_fixture'] is packet['synthetic_fixture'],'receipt fixture mismatch')
   nodes[identity]=node
  missing=sorted(set(REQUIREMENTS)-set(byrole));check(not missing,'missing roles: '+','.join(missing))
  visiting=set();done=set()
  def visit(identity):
   check(identity in nodes,'unknown dependency');check(identity not in visiting,'cyclic dependencies')
   if identity in done:return
   visiting.add(identity)
   for dep in nodes[identity]['inputs']:visit(dep)
   visiting.remove(identity);done.add(identity)
  for identity in nodes:visit(identity)
  return 'STRUCTURALLY_READY_FIXTURE' if packet['synthetic_fixture'] else 'STRUCTURALLY_READY_FOR_REVIEW'
 try:status=run()
 except (Hold,ValueError,TypeError,KeyError,AttributeError,RecursionError) as exc:status='HOLD';reasons.append(str(exc) or type(exc).__name__)
 return {'status':status,'reasons':reasons,'empirical_admission':False,'physical_promotion':0,'scope':'Structure, declared bounds and externally supplied receipt allowlist only. Does not authenticate reviewers, methods, calibration truth or scientific independence.'}
if __name__=='__main__':
 try:
  profile=strict_load((Path(__file__).resolve().parent/'PROFILE.json').read_text());packet=strict_load(Path(sys.argv[1]).read_text());catalog=strict_load(Path(sys.argv[2]).read_text());result=evaluate(packet,catalog,profile)
 except (Exception,) as e:result={'status':'HOLD','reasons':[str(e)],'empirical_admission':False,'physical_promotion':0}
 print(json.dumps(result,indent=2));sys.exit(2 if result['status']=='HOLD' else 0)
