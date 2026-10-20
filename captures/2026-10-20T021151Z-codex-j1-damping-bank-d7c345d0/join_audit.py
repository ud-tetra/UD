"""Hash-gated old/new replay, exact Cartesian word partition and four-leaf join."""
import sys
sys.dont_write_bytecode=True
import ast,json,hashlib,gzip,subprocess,os
from pathlib import Path
from fractions import Fraction as F
import shifted_audit as A
import joined_evaluator as ev
from rounding import bits,frombits
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[1]
BASE=ev.BASE_PATH.parent

def main():
 base=json.loads((BASE/'RECTANGLE_RESULTS.json').read_text());new=json.loads((HERE/'RECTANGLE_RESULTS.json').read_text())
 assert base['status']==new['status']=='PASS'
 # Re-run prior all-input proof and constructor controls without modifying its capture.
 p=subprocess.run([sys.executable,str(BASE/'audit.py')],cwd=BASE,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,check=True)
 log=HERE/'BASELINE_REPLAY.log'
 if log.exists():assert log.read_text()==p.stdout
 else:log.write_text(p.stdout)
 # Verify immutable parameter binding, including the historic label correction evidence.
 source_comparisons={}
 for leaf,wc in [('original',F(9,2)),('neighbor',F(289,64))]:
  folder=HERE/leaf;s=json.loads((folder/'P2_WITNESS.json').read_text());pr=json.loads((folder/'P2_RESULTS.json').read_text());u=json.loads((folder/'UPPER_RESULTS.json').read_text());fw=json.loads(gzip.decompress((folder/'UPPER_WITNESS.json.gz').read_bytes()))
  assert s['omega']==pr['omega']==u['omega']==fw['omega']==str(wc)
  assert s['gamma']==pr['gamma']==u['gamma']==fw['gamma']=='101/1000'
  sh=hashlib.sha256((folder/'P2_WITNESS.json').read_bytes()).hexdigest();assert sh==u['source_state_sha256']==fw['source_state_sha256']
  assert u['source_state_payload_sha256']==s['state_payload_sha256'] and pr['exact_source_L2_squared']==20
  assert pr['topology_matches_original_P2'] and pr['corrected_algebraic_precision_passed'] and u['checks']['projected_mass_cross_term'] and u['checks']['P2_J_reproduced']
  old_source=REPO/'captures/2026-10-20T001957Z-codex-j1-neighbor-join-9a48fd6a/neighbor_state.py'
  def forcing(path):
   tree=ast.parse(path.read_text());fn=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='main')
   stmt=next(x for x in fn.body if isinstance(x,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='f' for t in x.targets))
   return ast.dump(stmt,include_attributes=False)
  assert forcing(folder/'state.py')==forcing(old_source)
  source_comparisons[leaf]={'omega':str(wc),'gamma':'101/1000','state_flux_result_parameters_equal':True,'state_hash_binding_checked':True,'same_topology_source_metric_measure':True,'same_forcing_AST':True,'state_topology_sha256':s['topology_sha256'],'flux_defect_squared':u['defect_squared'],'local_lift_squared':u['local_lift_budget_squared']}
 correction=json.loads((HERE/'PROVENANCE_CORRECTION.json').read_text());oldp=REPO/correction['source_path'];assert hashlib.sha256(oldp.read_bytes()).hexdigest()==correction['source_sha256']
 oldw=json.loads(gzip.decompress(oldp.read_bytes()));olds=json.loads((oldp.parent/'P2_WITNESS.json').read_text());oldu=json.loads((oldp.parent/'UPPER_RESULTS.json').read_text())
 assert oldw['omega']=='9/2' and olds['omega']==oldu['omega']=='289/64' and oldw['source_state_sha256']==hashlib.sha256((oldp.parent/'P2_WITNESS.json').read_bytes()).hexdigest()
 assert base['join']['frequency_interval']==new['join']['frequency_interval']==[str(ev.LOWER),str(ev.UPPER)]
 assert base['join']['switch']==new['join']['switch']=='577/128'
 oldlo,oldhi=map(F,base['join']['gamma_interval']);newlo,newhi=map(F,new['join']['gamma_interval'])
 assert oldlo==ev.GAMMA_LOWER and newhi==ev.GAMMA_UPPER and newlo<ev.GAMMA_SWITCH<oldhi
 overlap=A.word_domain(newlo,oldhi);oldgd=A.word_domain(oldlo,oldhi);newgd=A.word_domain(newlo,newhi);union=A.word_domain(oldlo,newhi)
 assert union['count']==oldgd['count']+newgd['count']-overlap['count']
 cut=bits(float(ev.GAMMA_SWITCH));assert F.from_float(frombits(cut))==ev.GAMMA_SWITCH
 assert oldgd['first_word']==union['first_word']<=cut<=oldgd['last_word']
 assert newgd['first_word']<=cut+1<=union['last_word']==newgd['last_word']
 selected={'baseline':cut-union['first_word']+1,'shifted':union['last_word']-cut};assert sum(selected.values())==union['count']
 wd=A.word_domain(ev.LOWER,ev.UPPER);assert wd['count']==base['accepted_input_domains']['joined_frequency']['count']==new['accepted_input_domains']['joined_frequency']['count']
 tree=ast.parse((HERE/'joined_evaluator.py').read_text());fn=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='evaluate')
 expected=ast.parse("def evaluate(omega,gamma):\n return BASELINE.evaluate(omega,gamma) if band(omega,gamma)=='baseline' else SHIFTED.evaluate(omega,gamma)").body[0]
 assert ast.dump(fn,include_attributes=False)==ast.dump(expected,include_attributes=False)
 fn=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='band');tail=fn.body[-1]
 assert ast.dump(tail,include_attributes=False)==ast.dump(ast.parse("return 'baseline' if g<=GAMMA_SWITCH else 'shifted'").body[0],include_attributes=False)
 samples={(w,g) for w in [wd['first_word'],wd['last_word'],bits(float(F(577,128)))-1,bits(float(F(577,128))),bits(float(F(577,128)))+1] for g in [union['first_word'],union['last_word'],cut-1,cut,cut+1]}
 seed=0x4a316761
 for i in range(512):
  seed=(1664525*seed+1013904223)%(2**32);w=wd['first_word']+(wd['last_word']-wd['first_word'])*seed//(2**32)
  seed=(1664525*seed+1013904223)%(2**32);g=union['first_word']+(union['last_word']-union['first_word'])*seed//(2**32);samples.add((w,g))
 for w,g in samples:
  omega,gamma=frombits(w),frombits(g);name=ev.band(omega,gamma);leaf=ev.BASELINE if g<=cut else ev.SHIFTED
  assert name==('baseline' if g<=cut else 'shifted')
  got=ev.evaluate(omega,gamma);want=leaf.evaluate(omega,gamma)
  assert bits(got.real)==bits(want.real) and bits(got.imag)==bits(want.imag)
 controls=[];goodw=frombits(wd['first_word']);goodg=frombits(union['first_word'])
 bads=[('omega below',frombits(wd['first_word']-1),goodg),('omega above',frombits(wd['last_word']+1),goodg),('gamma below',goodw,frombits(union['first_word']-1)),('gamma above',goodw,frombits(union['last_word']+1))]
 for arg in ['omega','gamma']:
  for label,x in [('NaN',float('nan')),('infinity',float('inf')),('negative infinity',-float('inf')),('integer',1),('boolean',True),('string','0.101')]:bads.append((arg+' '+label,x if arg=='omega' else goodw,x if arg=='gamma' else goodg))
 for name,w,g in bads:
  try:ev.evaluate(w,g)
  except ValueError:controls.append(name+' rejected')
  else:raise AssertionError(name+' accepted')
 badcut=newlo-F(1,10000);assert not newlo<=badcut<=oldhi;controls.append('damping selector outside overlap fails leaf containment')
 radius=max(F(base['join']['uniform_total_radius']),F(new['join']['uniform_total_radius']));assert radius<F(1,10)
 growth=(newhi-oldlo)/(oldhi-oldlo);assert growth==3
 result={'status':'PASS','classification':'DERIVED_CONDITIONAL_FOUR_STATE_TWO_PARAMETER_JOIN','source_baseline_results_sha256':hashlib.sha256((BASE/'RECTANGLE_RESULTS.json').read_bytes()).hexdigest(),'source_shifted_results_sha256':hashlib.sha256((HERE/'RECTANGLE_RESULTS.json').read_bytes()).hexdigest(),'source_joined_evaluator_sha256':hashlib.sha256((HERE/'joined_evaluator.py').read_bytes()).hexdigest(),'parameter_state_flux_checks':source_comparisons,'historic_metadata_correction_checked':True,'frequency_interval':[str(ev.LOWER),str(ev.UPPER)],'gamma_interval':[str(oldlo),str(newhi)],'gamma_overlap_interval':[str(newlo),str(oldhi)],'gamma_overlap_width':str(oldhi-newlo),'damping_switch':str(ev.GAMMA_SWITCH),'frequency_switch':'577/128','damping_width_ratio':str(growth),'accepted_gamma_domain':union,'accepted_frequency_domain':wd,'selected_gamma_word_counts':selected,'number_of_joined_binary64_pairs':union['count']*wd['count'],'partition_proof':'Consecutive exact gamma word indices partition into baseline<=cut and shifted>cut; both frequency-word partitions cover identical frequency union. Cartesian products cover every accepted pair without a hole.','uniform_total_radius':str(radius),'baseline_radius':base['join']['uniform_total_radius'],'shifted_radius':new['join']['uniform_total_radius'],'precision_target':'1/10','precision_passed':True,'actual_selector_pair_controls':len(samples),'controls':controls,'scope':'Each exact selector delegates unchanged inputs. No new output arithmetic, interpolation, output continuity, all-platform proof or physical parameter calibration. IEEE RN primitive semantics conditional.','scientific_status':'OPEN','independent_review':False,'physical_promotion':0}
 p=HERE/'JOINED_RESULTS.json'
 if p.exists():assert json.loads(p.read_text())==result;print('read-only joined rectangle replay matches saved results',flush=True)
 else:p.write_text(json.dumps(result,indent=2)+'\n')
 print('PASS four-state joined rectangle radius='+str(float(radius))+' damping width ratio='+str(growth)+' pairs='+str(union['count']*wd['count'])+' selector controls='+str(len(samples)),flush=True)

if __name__=='__main__':main()
