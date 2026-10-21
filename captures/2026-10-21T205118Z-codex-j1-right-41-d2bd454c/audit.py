"""Exact candidate-state binding, joined-extension cover and native evaluator audit."""
import sys
sys.dont_write_bytecode=True
import ast,json,hashlib,copy,gzip
from pathlib import Path
from fractions import Fraction as F
import kernel as K
import planner as P
import evaluator as ev
from rounding import bits,frombits,round64,pow2
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[1]
def source_checks():
 tree=ast.parse((HERE/'kernel.py').read_text());fn=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='trace');tail=fn.body[-17:];assert len(tail)==17
 for stmt,(name,kind,a,b) in zip(tail[:-1],K.OPS):
  assert isinstance(stmt,ast.Assign) and len(stmt.targets)==1 and isinstance(stmt.targets[0],ast.Name) and stmt.targets[0].id==name
  assert isinstance(stmt.value,ast.BinOp) and isinstance(stmt.value.left,ast.Name) and stmt.value.left.id==a and isinstance(stmt.value.right,ast.Name) and stmt.value.right.id==b and type(stmt.value.op)=={'add':ast.Add,'sub':ast.Sub,'mul':ast.Mult}[kind]
 assert isinstance(tail[-1],ast.Return) and [x.id for x in tail[-1].value.elts]==[x[0] for x in K.OPS]
 tree=ast.parse((HERE/'evaluator.py').read_text());fn=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='evaluate')
 expected=ast.parse("def evaluate(omega,gamma):\n component,idx=select(omega,gamma);nodes=kernel.trace(COVERS[component]['nodes'][idx]['certificate']['state'],omega,gamma)\n return complex(nodes[11],nodes[15])").body[0]
 assert ast.dump(fn,include_attributes=False)==ast.dump(expected,include_attributes=False)
 for sid,st in K.BANK.items():
  d=json.loads((REPO/st['source_results_path']).read_text());assert hashlib.sha256((REPO/st['source_results_path']).read_bytes()).hexdigest()==st['source_results_sha256']
  mr,mi,mc=map(F,d['full_state_mass']);exact=K.EXACT[sid]
  assert exact==dict(J_R=F(d['J'][0]),J_I=F(d['J'][1]),M_R=mr-mi,M_I=2*mc,OMEGA0=F(d['omega']),GAMMA0=F(d['gamma']),TWO=F(2))
  assert F(st['defect_squared'])==F(d['defect_squared']) and F(st['local_lift_squared'])==F(d['local_lift_budget_squared']) and F(st['full_state_L2_squared'])==mr+mi
  for k,v in exact.items():assert bits(round64(v))==bits(K.CONSTANTS[sid][k])

def verify_tree(cover):
 assert cover['bank_sha256']==hashlib.sha256((HERE/'BANK.json').read_bytes()).hexdigest() and cover['contract_sha256']==hashlib.sha256((HERE/'CONTRACT.json').read_bytes()).hexdigest()
 nodes=cover['nodes'];seen=set();leaves=[]
 wl,wu=map(F,cover['domain']['omega']);gl,gu=map(F,cover['domain']['gamma']);wf,wt=P.word_domain(wl,wu);gf,gt=P.word_domain(gl,gu)
 assert nodes[0]['proof_box']==list(map(str,[wl,wu,gl,gu])) and nodes[0]['word_box']==[wf,wt,gf,gt] and nodes[0]['depth']==0 and F(cover['target'])==F(1,10)
 def visit(i):
  assert type(i) is int and 0<=i<len(nodes) and i not in seen;seen.add(i);n=nodes[i];box=tuple(map(F,n['proof_box']));wl,wu,gl,gu=box;wf,wt,gf,gt=n['word_box'];assert wf<=wt and gf<=gt
  assert wl<=F.from_float(frombits(wf))<=F.from_float(frombits(wt))<=wu and gl<=F.from_float(frombits(gf))<=F.from_float(frombits(gt))<=gu
  if n['kind']=='leaf':
   cert=K.certificate(n['certificate']['state'],box);assert cert==n['certificate'] and F(cert['total_radius'])<=F(cover['target']);leaves.append(i);return (wt-wf+1)*(gt-gf+1)
  assert n['kind']=='split' and n['axis']==P.split_axis(box,(wf,wt,gf,gt))
  a,b=nodes[n['left']],nodes[n['right']];cut=n['cut_word'];q=F(n['cut_rational']);assert F.from_float(frombits(cut))==q
  if n['axis']=='omega':
   assert cut==(wf+wt)//2 and a['word_box']==[wf,cut,gf,gt] and b['word_box']==[cut+1,wt,gf,gt]
   assert list(map(F,a['proof_box']))==[wl,q,gl,gu] and list(map(F,b['proof_box']))==[q,wu,gl,gu]
  else:
   assert cut==(gf+gt)//2 and a['word_box']==[wf,wt,gf,cut] and b['word_box']==[wf,wt,cut+1,gt]
   assert list(map(F,a['proof_box']))==[wl,wu,gl,q] and list(map(F,b['proof_box']))==[wl,wu,q,gu]
  assert a['depth']==b['depth']==n['depth']+1
  count=visit(n['left'])+visit(n['right']);assert count==(wt-wf+1)*(gt-gf+1);return count
 count=visit(0);assert len(seen)==len(nodes) and leaves==cover['leaf_indices'] and count==cover['accepted_pair_count']
 assert len(leaves)==cover['leaf_count'] and max(n['depth'] for n in nodes)==cover['maximum_depth']
 assert F(cover['uniform_total_radius'])==max(F(nodes[i]['certificate']['total_radius']) for i in leaves)
 return leaves,count

def native_controls(cover,component):
 samples=set();expected={};seed=0x4a316164
 # Endpoints, cell centers, center-state words when inside, and deterministic interior controls.
 for idx in cover['leaf_indices']:
  n=cover['nodes'][idx];wf,wt,gf,gt=n['word_box'];pairs={(w,g) for w in [wf,wt,(wf+wt)//2] for g in [gf,gt,(gf+gt)//2]}
  sid=n['certificate']['state'];wc=bits(K.CONSTANTS[sid]['OMEGA0']);gc=bits(K.CONSTANTS[sid]['GAMMA0'])
  pairs|={(w,g) for w in [wc-1,wc,wc+1] for g in [gc-1,gc,gc+1] if wf<=w<=wt and gf<=g<=gt}
  for j in range(128):
   seed=(1664525*seed+1013904223)%(2**32);w=wf+(wt-wf)*seed//(2**32)
   seed=(1664525*seed+1013904223)%(2**32);g=gf+(gt-gf)*seed//(2**32);pairs.add((w,g))
  for pair in pairs:assert pair not in expected;expected[pair]=idx;samples.add(pair)
 maxerr=F(0);node_comparisons=0
 for ww,gg in sorted(samples):
  w,g=frombits(ww),frombits(gg);idx=ev.select_component(component,w,g);assert idx==expected[(ww,gg)];n=cover['nodes'][idx];sid=n['certificate']['state'];native=K.trace(sid,w,g);exact=K.EXACT[sid];ideal=dict(exact);ref={k:F.from_float(x) for k,x in K.CONSTANTS[sid].items()}
  for x in [ideal,ref]:x['omega']=F.from_float(w);x['gamma']=F.from_float(g)
  for j,(name,kind,a,b) in enumerate(K.OPS):
   rn=round64(K.op(ref[a],ref[b],kind));assert bits(rn)==bits(native[j]);ref[name]=F.from_float(rn);ideal[name]=K.op(ideal[a],ideal[b],kind)
   assert abs(ref[name]-ideal[name])<=F(n['certificate']['node_error_bounds'][j]);node_comparisons+=1
  dw2=ideal['omega']**2-exact['OMEGA0']**2;di=2*(ideal['gamma']*ideal['omega']-exact['GAMMA0']*exact['OMEGA0'])
  assert ideal['real']==exact['J_R']+dw2*exact['M_R']+di*exact['M_I'] and ideal['imag']==exact['J_I']+dw2*exact['M_I']-di*exact['M_R']
  got=ev.evaluate_component(component,w,g);global_got=ev.evaluate(w,g);assert bits(got.real)==bits(global_got.real) and bits(got.imag)==bits(global_got.imag);assert bits(got.real)==bits(native[11]) and bits(got.imag)==bits(native[15]);err=(F.from_float(got.real)-ideal['real'])**2+(F.from_float(got.imag)-ideal['imag'])**2
  assert err<=F(n['certificate']['floating_radius'])**2;maxerr=max(maxerr,err)
 return {'sampled_input_pairs':len(samples),'node_comparisons':node_comparisons,'closed_estimator_checks':len(samples),'max_observed_floating_error_upper':str(K.roots(maxerr)[1])}

def main():
 assert (sys.float_info.radix,sys.float_info.mant_dig,sys.float_info.max_exp,sys.float_info.min_exp,sys.float_info.rounds)==(2,53,1024,-1021,1)
 source_checks();contract=json.loads((HERE/'CONTRACT.json').read_text());cover=json.loads((HERE/'COVER.json').read_text());assert len(K.BANK)==40 and cover['domain']==contract['complete_cover_domain'];leaves,count=verify_tree(cover);native=native_controls(cover,0);controls=[]
 assert cover['maximum_depth']<=contract['finite_algorithm_budget']['max_depth'] and cover['leaf_count']<=contract['finite_algorithm_budget']['max_leaves']
 old=REPO/'captures/2026-10-21T024059Z-codex-j1-bank-30-7fcf86a1'
 def fn(path,name):return next(x for x in ast.parse(path.read_text()).body if isinstance(x,ast.FunctionDef) and x.name==name)
 for name in ['validated','select_component','evaluate_component']:assert ast.dump(fn(HERE/'evaluator.py',name),include_attributes=False)==ast.dump(fn(old/'evaluator.py',name),include_attributes=False)
 expected=ast.parse("def select(omega,gamma):\n w,g=validated(omega,gamma)\n if not LOWER<=w<=UPPER or not GAMMA_LOWER<=g<=GAMMA_UPPER:raise ValueError('input outside certified rectangle')\n return 0,select_component(0,omega,gamma)").body[0];assert ast.dump(fn(HERE/'evaluator.py','select'),include_attributes=False)==ast.dump(expected,include_attributes=False)
 assert [ev.LOWER,ev.UPPER,ev.GAMMA_LOWER,ev.GAMMA_UPPER]==list(map(F,cover['nodes'][0]['proof_box']))
 mutations=[('zero uniform radius',lambda d:d.update(uniform_total_radius='0')),('zeroed certificate',lambda d:d['nodes'][d['leaf_indices'][0]]['certificate'].update(total_radius='0')),('changed split word',lambda d:d['nodes'][0].update(cut_word=d['nodes'][0]['cut_word']+1)),('missing leaf word',lambda d:d['nodes'][d['leaf_indices'][0]]['word_box'].__setitem__(0,d['nodes'][d['leaf_indices'][0]]['word_box'][0]+1)),('changed domain',lambda d:d['domain']['gamma'].__setitem__(1,'8/25')),('changed bank hash',lambda d:d.update(bank_sha256='0'*64))]
 for label,mut in mutations:
  bad=copy.deepcopy(cover);mut(bad)
  try:verify_tree(bad)
  except (AssertionError,IndexError,KeyError):controls.append(label+' rejected')
  else:raise AssertionError(label+' accepted')
 for field,value in [('max_depth',0),('max_leaves',1)]:
  bad=copy.deepcopy(contract);bad['finite_algorithm_budget'][field]=value
  try:P.create_cover(bad)
  except AssertionError:controls.append(field+' exhausted -> unresolved')
  else:raise AssertionError('budget accepted')
 wf,wt,gf,gt=cover['nodes'][0]['word_box'];goodw,goodg=frombits(wf),frombits(gf);bads=[('omega below',frombits(wf-1),goodg),('omega above',frombits(wt+1),goodg),('gamma below',goodw,frombits(gf-1)),('gamma above',goodw,frombits(gt+1))]
 for arg in ['omega','gamma']:
  for label,x in [('NaN',float('nan')),('infinity',float('inf')),('negative infinity',-float('inf')),('integer',1),('boolean',True),('string','0.13')]:bads.append((arg+' '+label,x if arg=='omega' else goodw,x if arg=='gamma' else goodg))
 for label,w,g in bads:
  try:ev.evaluate(w,g)
  except ValueError:controls.append(label+' rejected')
  else:raise AssertionError(label+' accepted')
 def descendants(i):
  n=cover['nodes'][i]
  return {i} if n['kind']=='leaf' else descendants(n['left'])|descendants(n['right'])
 seam_checks=0
 for n in cover['nodes']:
  if n['kind']!='split':continue
  x0,x1,y0,y1=n['word_box'];other=[y0,(y0+y1)//2,y1] if n['axis']=='omega' else [x0,(x0+x1)//2,x1]
  for side in ['left','right']:
   word=n['cut_word']+int(side=='right');allowed=descendants(n[side])
   for q in other:
    w,g=(frombits(word),frombits(q)) if n['axis']=='omega' else (frombits(q),frombits(word));comp,idx=ev.select(w,g);assert comp==0 and idx in allowed;got=ev.evaluate(w,g);want=ev.evaluate_component(0,w,g);assert bits(got.real)==bits(want.real) and bits(got.imag)==bits(want.imag);seam_checks+=1
 import own_checks
 point=own_checks.main();freeze=json.loads((HERE/'PARAMETER_FREEZE.json').read_text());sid=freeze['state_key'];w,g=map(F,freeze['center'])
 uniform=REPO/freeze['previous_uniform_capture'];pc=json.loads((uniform/'COVER.json').read_text());assert hashlib.sha256((uniform/'COVER.json').read_bytes()).hexdigest()==freeze['previous_uniform_cover_sha256']
 a,b,d,e=map(F,pc['nodes'][0]['proof_box']);p0,p1,p2,p3=pc['nodes'][0]['word_box'];assert [ev.LOWER,ev.UPPER,ev.GAMMA_LOWER]==[a,b,d] and e==F(2,5)<ev.GAMMA_UPPER==F(41,100) and [wf,wt,gf]==[p0,p1,p2]
 novel=(wt-wf+1)*(gt-p3);assert novel>0 and count==pc['accepted_pair_count']+novel
 extension_controls=0
 for ww in [wf,(wf+wt)//2,wt]:
  for gg in [p3,p3+1,gt]:
   comp,idx=ev.select(frombits(ww),frombits(gg));assert comp==0;ev.evaluate(frombits(ww),frombits(gg));extension_controls+=1
 ow,og=float(w),frombits(gt);assert bits(ow)==wt and F.from_float(ow)<w<F.from_float(frombits(wt+1)) and bits(float(g))==gt and F.from_float(og)<g<F.from_float(frombits(gt+1))
 comp,idx=ev.select(ow,og);assert comp==0 and cover['nodes'][idx]['certificate']['state']==sid;ev.evaluate(ow,og)
 def area(x):return (F(x['omega'][1])-F(x['omega'][0]))*(F(x['gamma'][1])-F(x['gamma'][0]))
 totalarea=area(cover['domain']);oldarea=area(pc['domain']);assert totalarea/oldarea==F(31,30);owners=sorted({cover['nodes'][i]['certificate']['state'] for i in leaves});assert sid in owners and 'left_41' in owners
 failed=REPO/freeze['failed_full_goal_capture'];assert hashlib.sha256((failed/'SCALAR_GENERATION.log').read_bytes()).hexdigest()==freeze['failed_full_goal_log_sha256'] and hashlib.sha256((failed/'DIAGNOSTIC_RESULTS.json').read_bytes()).hexdigest()==freeze['failed_diagnostic_results_sha256']
 priorfreeze=json.loads((failed/'PARAMETER_FREEZE.json').read_text());assert priorfreeze['provisional_cover_goal']==freeze['provisional_cover_goal'] and priorfreeze['finite_algorithm_budget']==freeze['finite_algorithm_budget'] and not (failed/'COVER.json').exists()
 placement=json.loads((HERE/'PLACEMENT_RESULTS.json').read_text());assert placement['probe_count']==1032 and placement['formula_count']==len(K.BANK)==40 and all(row['formula_count']==40 and set(row['formula_lower_by_state'])==set(K.BANK) and row['all_transported_formulas_above_target']==(F(row['minimum_formula_lower'])>F(contract['target'])) for row in placement['rows'])
 q=placement['recommended_new_state'];assert min(K.point_formula_bounds(k,F(q['omega']),F(q['gamma']))[0] for k in K.BANK)==F(q['minimum_formula_lower']) and ev.LOWER<=F(q['omega'])<=ev.UPPER and F(q['gamma'])>ev.GAMMA_UPPER
 radius=F(cover['uniform_total_radius']);assert radius<F(1,10)
 for x,want in [(F(1)+pow2(-53),1.0),(F(1)+3*pow2(-53),frombits(bits(1.)+2)),(pow2(-1075),0.),(3*pow2(-1075),frombits(2))]:assert bits(round64(x))==bits(want)
 result={'status':'PASS','classification':'DERIVED_CONDITIONAL_NEW_PAIRED_CORNER_STATE_COMPLETE_RECTANGLE_41','domain':cover['domain'],'formula_count':len(K.BANK),'leaf_count':len(leaves),'maximum_depth':cover['maximum_depth'],'uniform_total_radius':str(radius),'maximum_uniform_floating_radius':str(max(F(cover['nodes'][i]['certificate']['floating_radius']) for i in leaves)),'accepted_pair_count':count,'previous_accepted_pair_count':pc['accepted_pair_count'],'newly_accepted_upper_strip_pairs':novel,'union_area':str(totalarea),'previous_area':str(oldarea),'area_ratio_to_previous':str(totalarea/oldarea),'active_states':owners,'native_controls':native,'internal_seam_checks':seam_checks,'extension_boundary_controls':extension_controls,'controls':controls,'own_point_audit':point,'old_family_obstacle_owner':sid,'nearest_frequency_is_first_accepted_word':False,'nearest_frequency_is_interior_word':False,'nearest_frequency_is_last_accepted_word':True,'nearest_damping_is_last_accepted_word':True,'nearest_damping_is_first_excluded_word':False,'next_state_candidate':q,'source_sha256':{n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in ['kernel.py','planner.py','evaluator.py','audit.py','own_checks.py','PARAMETER_FREEZE.json','BANK.json','CONTRACT.json','COVER.json','PLACEMENT_RESULTS.json']},'scope':'Full41/100 rectangle with prior2/5 rectangle and represented right-corner formula obstruction included. Primitive binary64 RN conditional;not independent review,all-platform proof,rate,termination,native UD or physical identification. Formula diagnostics are not actual-error lowers.','scientific_status':'OPEN','independent_review':False,'physical_promotion':0}
 P.save_or_compare('AUDIT_RESULTS.json',result);print('PASS40-state full rectangle leaves='+str(len(leaves))+' radius='+str(float(radius))+' native traces='+str(native['sampled_input_pairs'])+' area ratio='+str(totalarea/oldarea)+' next=('+q['omega']+','+q['gamma']+')',flush=True)
if __name__=='__main__':main()
