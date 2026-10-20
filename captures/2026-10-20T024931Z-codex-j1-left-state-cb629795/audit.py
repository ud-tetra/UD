"""Exact candidate-state binding, two-component cover and native evaluator audit."""
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
 nodes=cover['nodes'];seen=set();leaves=[]
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
 source_checks();full,ext=[json.loads((HERE/n).read_text()) for n in ['COVER.json','EXTENSION_COVER.json']];covers=[full,ext];native=[];counts=[];controls=[]
 for component,cover in enumerate(covers):
  leaves,count=verify_tree(cover);counts.append(count);native.append(native_controls(cover,component))
  for label,mut in [('zeroed certificate',lambda d:d['nodes'][d['leaf_indices'][0]]['certificate'].update(total_radius='0')),('changed split word',lambda d:d['nodes'][0].update(cut_word=d['nodes'][0]['cut_word']+1)),('missing leaf word',lambda d:d['nodes'][d['leaf_indices'][0]]['word_box'].__setitem__(0,d['nodes'][d['leaf_indices'][0]]['word_box'][0]+1))]:
   bad=copy.deepcopy(cover);mut(bad)
   try:verify_tree(bad)
   except (AssertionError,IndexError,KeyError):controls.append('component'+str(component)+' '+label+' rejected')
   else:raise AssertionError(label+' accepted')
 contract=json.loads((HERE/'CONTRACT.json').read_text())
 for field,value in [('max_depth',0),('max_leaves',1)]:
  bad=copy.deepcopy(contract);bad['finite_algorithm_budget'][field]=value
  try:P.create_cover(bad)
  except AssertionError:controls.append(field+' exhausted -> unresolved')
  else:raise AssertionError('budget accepted')
 # The shared non-dyadic gamma cut lies strictly between consecutive represented words.
 fword=full['nodes'][0]['word_box'];eword=ext['nodes'][0]['word_box'];assert fword[3]+1==eword[2]
 assert F(full['domain']['gamma'][1])==F(ext['domain']['gamma'][0])==F(417,4000)
 assert F.from_float(frombits(fword[3]))<F(417,4000)<F.from_float(frombits(eword[2]))
 assert full['domain']['omega'][0]==ext['domain']['omega'][0] and F(ext['domain']['omega'][1])==F(9,2)<=F(full['domain']['omega'][1])
 goodw,goodg=frombits(fword[0]),frombits(fword[2]);topg=frombits(eword[3]);leftword=bits(4.5)
 bads=[('omega below',frombits(fword[0]-1),goodg),('omega above',frombits(fword[1]+1),goodg),('gamma below',goodw,frombits(fword[2]-1)),('gamma above',goodw,frombits(eword[3]+1)),('upper-right uncertified region',frombits(fword[1]),topg),('one word beyond left strip',frombits(leftword+1),topg)]
 for arg in ['omega','gamma']:
  for label,x in [('NaN',float('nan')),('infinity',float('inf')),('negative infinity',-float('inf')),('integer',1),('boolean',True),('string','0.11')]:bads.append((arg+' '+label,x if arg=='omega' else goodw,x if arg=='gamma' else goodg))
 for label,w,g in bads:
  try:ev.evaluate(w,g)
  except ValueError:controls.append(label+' rejected')
  else:raise AssertionError(label+' accepted')
 seam_checks=0
 for ww in [fword[0],leftword-1,leftword,leftword+1,fword[1]]:
  for gg in [fword[3],eword[2]]:
   w,g=frombits(ww),frombits(gg)
   if gg==eword[2] and ww>leftword:
    try:ev.evaluate(w,g)
    except ValueError:seam_checks+=1;continue
    else:raise AssertionError('uncertified seam quadrant accepted')
   component,idx=ev.select(w,g);assert component==int(gg==eword[2]);got=ev.evaluate(w,g);want=ev.evaluate_component(component,w,g);assert bits(got.real)==bits(want.real) and bits(got.imag)==bits(want.imag);seam_checks+=1
 # Exact new state/flux parameter and source bindings, including nonbinary centers.
 folder=HERE/'candidate';s=json.loads((folder/'P2_WITNESS.json').read_text());p=json.loads((folder/'P2_RESULTS.json').read_text());u=json.loads((folder/'UPPER_RESULTS.json').read_text());fw=json.loads(gzip.decompress((folder/'UPPER_WITNESS.json.gz').read_bytes()))
 assert s['omega']==p['omega']==u['omega']==fw['omega']=='8983/2000' and s['gamma']==p['gamma']==u['gamma']==fw['gamma']=='11/100'
 sh=hashlib.sha256((folder/'P2_WITNESS.json').read_bytes()).hexdigest();assert sh==fw['source_state_sha256']==u['source_state_sha256'] and s['state_payload_sha256']==u['source_state_payload_sha256']
 assert p['corrected_algebraic_precision_passed'] and p['topology_matches_original_P2'] and p['exact_source_L2_squared']==20 and u['reported_J_precision_passed']
 def forcing(path):
  tree=ast.parse(path.read_text());fn=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='main');stmt=next(x for x in fn.body if isinstance(x,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='f' for t in x.targets));return ast.dump(stmt,include_attributes=False)
 assert forcing(folder/'state.py')==forcing(REPO/'captures/2026-10-20T021151Z-codex-j1-damping-bank-d7c345d0/original/state.py')
 assert all(K.EXACT['adaptive_left'][k]!=F.from_float(K.CONSTANTS['adaptive_left'][k]) for k in ['OMEGA0','GAMMA0'])
 w,g=F(8983,2000),F(11,100);oldlower=min(K.point_formula_bounds(sid,w,g)[0] for sid in K.BANK if sid!='adaptive_left');newupper=K.point_formula_bounds('adaptive_left',w,g)[1];assert oldlower>F(1,10)>newupper
 prior=REPO/'captures/2026-10-20T023053Z-codex-j1-adaptive-cover-7993ac19/COVER.json';old=json.loads(prior.read_text());assert full['domain']['omega']==old['domain']['omega'] and F(full['domain']['gamma'][0])==F(old['domain']['gamma'][0]) and F(full['domain']['gamma'][1])>F(old['domain']['gamma'][1])
 def area(d):return (F(d['omega'][1])-F(d['omega'][0]))*(F(d['gamma'][1])-F(d['gamma'][0]))
 totalarea=area(full['domain'])+area(ext['domain']);oldarea=area(old['domain']);owners=sorted({cover['nodes'][i]['certificate']['state'] for cover in covers for i in cover['leaf_indices']});assert 'adaptive_left' in owners
 q=json.loads((HERE/'PLACEMENT_RESULTS.json').read_text())['recommended_new_state'];assert min(K.point_formula_bounds(sid,F(q['omega']),F(q['gamma']))[0] for sid in K.BANK)==F(q['minimum_formula_lower'])>F(1,10)
 assert F(q['omega'])>F(9,2) and F(q['gamma'])>F(417,4000)
 radius=max(F(x['uniform_total_radius']) for x in covers);assert radius<F(1,10)
 for x,want in [(F(1)+pow2(-53),1.0),(F(1)+3*pow2(-53),frombits(bits(1.)+2)),(pow2(-1075),0.),(3*pow2(-1075),frombits(2))]:assert bits(round64(x))==bits(want)
 result={'status':'PASS','classification':'DERIVED_CONDITIONAL_NEW_STATE_AND_JOINED_ADAPTIVE_UNION','source_sha256':{n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in ['kernel.py','planner.py','evaluator.py','BANK.json','CONTRACT.json','COVER.json','EXTENSION_COVER.json','PLACEMENT_RESULTS.json']},'full_frequency_domain':full['domain'],'left_extension_domain':ext['domain'],'component_leaf_counts':[x['leaf_count'] for x in covers],'component_depths':[x['maximum_depth'] for x in covers],'uniform_total_radius':str(radius),'component_radii':[x['uniform_total_radius'] for x in covers],'maximum_uniform_floating_radius':str(max(F(x['nodes'][i]['certificate']['floating_radius']) for x in covers for i in x['leaf_indices'])),'accepted_pair_count':sum(counts),'component_pair_counts':counts,'union_area':str(totalarea),'previous_area':str(oldarea),'area_ratio_to_previous':str(totalarea/oldarea),'active_states':owners,'native_controls':native,'seam_checks':seam_checks,'controls':controls,'candidate_state_checks':{'exact_omega':'8983/2000','exact_gamma':'11/100','state_flux_result_parameter_equality':True,'same_topology_forcing_metric_measure':True,'source_state_sha256':sh,'both_parameter_constants_have_nonzero_quantization':True,'old_four_formula_lower_at_center':str(oldlower),'new_state_model_upper_at_center':str(newupper),'actual_sparse_reported_J_radius':u['corrected_J_reported_continuum_radius'],'selected_reported_J_radius':u['selected_reported_J_radius']},'next_state_candidate':q,'scope':'Full rectangle plus left-frequency strip; upper-right region remains uncertified and is rejected. Primitive binary64 RN conditional; no output interpolation/continuity or all-platform proof. Next-state diagnostic is a lower on particular sufficient upper formulas, not actual error.','scientific_status':'OPEN','independent_review':False,'physical_promotion':0}
 P.save_or_compare('AUDIT_RESULTS.json',result);print('PASS joined leaves='+str(result['component_leaf_counts'])+' pairs='+str(sum(counts))+' native traces='+str(sum(x['sampled_input_pairs'] for x in native))+' radius='+str(float(radius))+' area ratio='+str(float(totalarea/oldarea))+' next=('+q['omega']+','+q['gamma']+')',flush=True)

if __name__=='__main__':main()
