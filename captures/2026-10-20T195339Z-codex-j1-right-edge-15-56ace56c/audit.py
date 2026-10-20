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
 source_checks();contract=json.loads((HERE/'CONTRACT.json').read_text());names=['COVER.json','EXTENSION_COVER.json','RIGHT_EXTENSION_COVER.json'];covers=[json.loads((HERE/n).read_text()) for n in names];full,left,right=covers
 assert len(K.BANK)==16 and [co['domain'] for co in covers]==[contract[k] for k in ['complete_cover_domain','extension_cover_domain','right_extension_cover_domain']]
 counts=[];native=[];controls=[];seam_checks=0
 for component,cover in enumerate(covers):
  leaves,count=verify_tree(cover);counts.append(count);native.append(native_controls(cover,component));assert cover['maximum_depth']<=contract['finite_algorithm_budget']['max_depth'] and cover['leaf_count']<=contract['finite_algorithm_budget']['max_leaves']
  mutations=[('zero uniform radius',lambda d:d.update(uniform_total_radius='0')),('zeroed certificate',lambda d:d['nodes'][d['leaf_indices'][0]]['certificate'].update(total_radius='0')),('changed split word',lambda d:d['nodes'][0].update(cut_word=d['nodes'][0]['cut_word']+1)) if cover['nodes'][0]['kind']=='split' else ('changed root bound',lambda d:d['nodes'][0]['proof_box'].__setitem__(0,str(F(d['nodes'][0]['proof_box'][0])+pow2(-53)))),('missing leaf word',lambda d:d['nodes'][d['leaf_indices'][0]]['word_box'].__setitem__(0,d['nodes'][d['leaf_indices'][0]]['word_box'][0]+1)),('changed bank hash',lambda d:d.update(bank_sha256='0'*64))]
  for label,mut in mutations:
   bad=copy.deepcopy(cover);mut(bad)
   try:verify_tree(bad)
   except (AssertionError,IndexError,KeyError):controls.append(str(component)+' '+label+' rejected')
   else:raise AssertionError(label+' accepted')
  def descendants(i):
   n=cover['nodes'][i]
   return {i} if n['kind']=='leaf' else descendants(n['left'])|descendants(n['right'])
  for n in cover['nodes']:
   if n['kind']!='split':continue
   x0,x1,y0,y1=n['word_box'];other=[y0,(y0+y1)//2,y1] if n['axis']=='omega' else [x0,(x0+x1)//2,x1]
   for side in ['left','right']:
    word=n['cut_word']+int(side=='right');allowed=descendants(n[side])
    for q in other:
     w,g=(frombits(word),frombits(q)) if n['axis']=='omega' else (frombits(q),frombits(word));comp,idx=ev.select(w,g);assert comp==component and idx in allowed;got=ev.evaluate(w,g);want=ev.evaluate_component(component,w,g);assert bits(got.real)==bits(want.real) and bits(got.imag)==bits(want.imag);seam_checks+=1
 old=REPO/'captures/2026-10-20T193711Z-codex-j1-left-edge-15-95891767'
 def fn(path,name):return next(x for x in ast.parse(path.read_text()).body if isinstance(x,ast.FunctionDef) and x.name==name)
 for name in ['validated','select_component','evaluate_component']:assert ast.dump(fn(HERE/'evaluator.py',name),include_attributes=False)==ast.dump(fn(old/'evaluator.py',name),include_attributes=False)
 expected=ast.parse("def select(omega,gamma):\n w,g=validated(omega,gamma)\n if not LOWER<=w<=UPPER or not GAMMA_LOWER<=g<=GAMMA_UPPER or (g>GAMMA_SWITCH and LEFT_UPPER<w<RIGHT_LOWER):raise ValueError('input outside certified union')\n component=0 if g<=GAMMA_SWITCH else (1 if w<=LEFT_UPPER else 2)\n return component,select_component(component,omega,gamma)").body[0];assert ast.dump(fn(HERE/'evaluator.py','select'),include_attributes=False)==ast.dump(expected,include_attributes=False)
 assert [ev.LOWER,ev.UPPER,ev.GAMMA_LOWER,ev.GAMMA_SWITCH]==list(map(F,full['nodes'][0]['proof_box'])) and ev.GAMMA_SWITCH==F(37,250) and ev.GAMMA_UPPER==F(3,20) and ev.LEFT_UPPER==F(143989,32000) and ev.RIGHT_LOWER==F(144511,32000)
 for field,value in [('max_depth',0),('max_leaves',1)]:
  bad=copy.deepcopy(contract);bad['finite_algorithm_budget'][field]=value
  try:P.create_cover(bad)
  except AssertionError:controls.append(field+' exhausted -> unresolved')
  else:raise AssertionError('budget accepted')
 wf,wt,gf,gt=full['nodes'][0]['word_box'];lwf,lwt,lgf,lgt=left['nodes'][0]['word_box'];rwf,rwt,rgf,rgt=right['nodes'][0]['word_box']
 assert lwf==wf and rwt==wt and lwt==P.word_domain(ev.LOWER,ev.LEFT_UPPER)[1] and rwf==P.word_domain(ev.RIGHT_LOWER,ev.UPPER)[0] and lwt+1<rwf and lgf==rgf==gt+1 and lgt==rgt
 assert F.from_float(frombits(gt))<ev.GAMMA_SWITCH<F.from_float(frombits(lgf)) and F.from_float(frombits(lwt))<ev.LEFT_UPPER<F.from_float(frombits(lwt+1)) and F.from_float(frombits(rwf-1))<ev.RIGHT_LOWER<F.from_float(frombits(rwf))
 goodw,goodg=frombits(wf),frombits(gf);topg=frombits(lgt);bads=[('omega below',frombits(wf-1),goodg),('omega above',frombits(wt+1),goodg),('gamma below',goodw,frombits(gf-1)),('gamma above',goodw,frombits(lgt+1)),('upper-center gap',frombits((lwt+rwf)//2),topg),('one word beyond left strip',frombits(lwt+1),topg),('one word before right strip',frombits(rwf-1),topg)]
 for arg in ['omega','gamma']:
  for label,x in [('NaN',float('nan')),('infinity',float('inf')),('negative infinity',-float('inf')),('integer',1),('boolean',True),('string','0.13')]:bads.append((arg+' '+label,x if arg=='omega' else goodw,x if arg=='gamma' else goodg))
 for label,w,g in bads:
  try:ev.evaluate(w,g)
  except ValueError:controls.append(label+' rejected')
  else:raise AssertionError(label+' accepted')
 component_seams=0
 for ww in [wf,lwt-1,lwt,lwt+1,rwf-1,rwf,rwf+1,wt]:
  for gg in [gt,lgf,lgt]:
   w,g=frombits(ww),frombits(gg)
   if gg>=lgf and lwt<ww<rwf:
    try:ev.evaluate(w,g)
    except ValueError:component_seams+=1;continue
    else:raise AssertionError('uncertified central seam accepted')
   comp,idx=ev.select(w,g);assert comp==(0 if gg<=gt else (1 if ww<=lwt else 2));got=ev.evaluate(w,g);want=ev.evaluate_component(comp,w,g);assert bits(got.real)==bits(want.real) and bits(got.imag)==bits(want.imag);component_seams+=1
 folder=HERE/'candidate';ancestor=old/'candidate';assert (folder/'state.py').read_text()==(ancestor/'state.py').read_text().replace('OMEGA=F(8983,2000)','OMEGA=F(36193,8000)')
 assert all((folder/n).read_bytes()==(ancestor/n).read_bytes() for n in ['flux.py','curl.py','replay.py'])
 s=json.loads((folder/'P2_WITNESS.json').read_text());p=json.loads((folder/'P2_RESULTS.json').read_text());u=json.loads((folder/'UPPER_RESULTS.json').read_text());fw=json.loads(gzip.decompress((folder/'UPPER_WITNESS.json.gz').read_bytes()));assert s['omega']==p['omega']==u['omega']==fw['omega']=='36193/8000' and s['gamma']==p['gamma']==u['gamma']==fw['gamma']=='3/20'
 sh=hashlib.sha256((folder/'P2_WITNESS.json').read_bytes()).hexdigest();assert sh==fw['source_state_sha256']==u['source_state_sha256'] and s['state_payload_sha256']==u['source_state_payload_sha256'];assert p['corrected_algebraic_precision_passed'] and p['topology_matches_original_P2'] and p['exact_source_L2_squared']==20 and u['reported_J_precision_passed']
 assert all(K.EXACT['right_edge_15'][k]!=F.from_float(K.CONSTANTS['right_edge_15'][k]) for k in ['OMEGA0','GAMMA0'])
 preflight=json.loads((HERE/'PREGEN_PREFLIGHT.json').read_text());assert preflight['probe_count']==132==len(preflight['rows']) and preflight['source_bank_sha256']==hashlib.sha256((old/'BANK.json').read_bytes()).hexdigest()
 for row in preflight['rows']:
  bounds=[K.point_formula_bounds(sid,F(row['omega']),F(row['gamma'])) for sid in K.BANK if sid!='right_edge_15'];assert F(row['minimum_formula_lower'])==min(x[0] for x in bounds) and F(row['minimum_formula_upper'])==min(x[1] for x in bounds)
 freeze=json.loads((HERE/'PARAMETER_FREEZE.json').read_text());assert freeze['center']==['36193/8000','3/20'] and list(freeze['provisional_cover_goals'].values())==[contract[k] for k in ['complete_cover_domain','extension_cover_domain','right_extension_cover_domain']];selected=json.loads((old/'PLACEMENT_RESULTS.json').read_text())['recommended_new_state'];assert [selected['omega'],selected['gamma']]==freeze['center']
 w,g=F(36193,8000),F(3,20);oldlower=min(K.point_formula_bounds(sid,w,g)[0] for sid in K.BANK if sid!='right_edge_15');newupper=K.point_formula_bounds('right_edge_15',w,g)[1];assert oldlower>F(1,10)>newupper
 priorfull=json.loads((old/'COVER.json').read_text());priorleft=json.loads((old/'EXTENSION_COVER.json').read_text());pwf,pwt,pgf,pgt=priorfull['nodes'][0]['word_box'];plwf,plwt,plgf,plgt=priorleft['nodes'][0]['word_box'];assert (pwf,pwt,pgf)==(wf,wt,gf) and pgt<gt and (plwf,plwt,plgt)==(lwf,lwt,lgt) and plgf==pgt+1<lgf
 # Prior left strip is retained through the new full component and the raised left component. Novel full-span words exclude that already-covered left strip.
 oldcount=priorfull['accepted_pair_count']+priorleft['accepted_pair_count'];newfull=(wt-lwt)*(gt-pgt);newright=(rwt-rwf+1)*(rgt-rgf+1);assert sum(counts)==oldcount+newfull+newright
 def area(d):return (F(d['omega'][1])-F(d['omega'][0]))*(F(d['gamma'][1])-F(d['gamma'][0]))
 totalarea=sum(area(co['domain']) for co in covers);oldarea=area(priorfull['domain'])+area(priorleft['domain']);assert totalarea/oldarea==F(196,185);owners=sorted({co['nodes'][i]['certificate']['state'] for co in covers for i in co['leaf_indices']});assert 'right_edge_15' in owners
 placement=json.loads((HERE/'PLACEMENT_RESULTS.json').read_text());assert placement['probe_count']==56;q=placement['recommended_new_state'];assert min(K.point_formula_bounds(sid,F(q['omega']),F(q['gamma']))[0] for sid in K.BANK)==F(q['minimum_formula_lower']) and ev.LEFT_UPPER<F(q['omega'])<ev.RIGHT_LOWER and F(q['gamma'])>ev.GAMMA_SWITCH
 radius=max(F(co['uniform_total_radius']) for co in covers);assert radius<F(1,10)
 for x,want in [(F(1)+pow2(-53),1.0),(F(1)+3*pow2(-53),frombits(bits(1.)+2)),(pow2(-1075),0.),(3*pow2(-1075),frombits(2))]:assert bits(round64(x))==bits(want)
 result={'status':'PASS','classification':'DERIVED_CONDITIONAL_RIGHT_EDGE_15_STATE_AND_THREE_COMPONENT_COVER','source_sha256':{n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in ['kernel.py','planner.py','evaluator.py','audit.py','BANK.json','CONTRACT.json',*names,'PLACEMENT_RESULTS.json']},'full_frequency_domain':full['domain'],'left_extension_domain':left['domain'],'right_extension_domain':right['domain'],'component_leaf_counts':[co['leaf_count'] for co in covers],'component_depths':[co['maximum_depth'] for co in covers],'uniform_total_radius':str(radius),'component_radii':[co['uniform_total_radius'] for co in covers],'maximum_uniform_floating_radius':str(max(F(co['nodes'][i]['certificate']['floating_radius']) for co in covers for i in co['leaf_indices'])),'accepted_pair_count':sum(counts),'component_pair_counts':counts,'previous_accepted_pair_count':oldcount,'new_full_span_outside_prior_left_pairs':newfull,'new_right_extension_pairs':newright,'union_area':str(totalarea),'previous_area':str(oldarea),'area_ratio_to_previous':str(totalarea/oldarea),'active_states':owners,'native_controls':native,'internal_seam_checks':seam_checks,'component_seam_checks':component_seams,'controls':controls,'candidate_state_checks':{'exact_omega':'36193/8000','exact_gamma':'3/20','source_state_sha256':sh,'state_flux_result_parameter_equality':True,'same_topology_forcing_metric_measure':True,'both_parameter_constants_have_nonzero_quantization':True,'old_fifteen_formula_lower_at_center':str(oldlower),'new_state_model_upper_at_center':str(newupper),'actual_sparse_reported_J_radius':u['corrected_J_reported_continuum_radius'],'selected_reported_J_radius':u['selected_reported_J_radius']},'next_state_candidate':q,'scope':'Full rectangle through37/250 and left/right quarter strips to3/20; upper-center gap rejected. Primitive binary64 RN conditional; no interpolation or all-platform formal verification. Formula diagnostics are not actual-error lowers.','scientific_status':'OPEN','independent_review':False,'physical_promotion':0}
 P.save_or_compare('AUDIT_RESULTS.json',result);print('PASS sixteen-state union leaves='+str(result['component_leaf_counts'])+' radius='+str(float(radius))+' native traces='+str(sum(x['sampled_input_pairs'] for x in native))+' area ratio='+str(totalarea/oldarea)+' next=('+q['omega']+','+q['gamma']+')',flush=True)

if __name__=='__main__':main()
