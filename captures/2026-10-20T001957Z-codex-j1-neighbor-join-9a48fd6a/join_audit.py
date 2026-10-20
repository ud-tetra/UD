"""Exact interval union, selector partition and overlap diagnostics."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,ast
from math import isqrt
from rounding import bits,frombits,round64
import joined_evaluator as ev
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[1]
OLD=REPO/'captures/2026-10-19T231026Z-codex-j1-floating-band-2bbebc9d'
OLDUPPER=REPO/'captures/2026-10-19T225423Z-codex-j1-p2-projected-flux-8a5ce1f3'
OLDSTATE=REPO/'captures/2026-10-19T220433Z-codex-j1-p2-state-8d4041af'

def sqrtup(x):
 assert x>=0
 s=10**30;n=isqrt(x.numerator*s*s//x.denominator)
 if F(n*n,s*s)<x:n+=1
 return F(n,s)

def extent(lo,hi):
 a,b=bits(round64(lo)),bits(round64(hi))
 while F.from_float(frombits(a))<lo:a+=1
 while F.from_float(frombits(b))>hi:b-=1
 assert F.from_float(frombits(a-1))<lo<=F.from_float(frombits(a)) and F.from_float(frombits(b))<=hi<F.from_float(frombits(b+1))
 return a,b

def exact_at(upper,w):
 w0=F(upper['omega']);mr,mi,mc=map(F,upper['full_state_mass']);mR,mI=mr-mi,2*mc;dzr=-(w*w-w0*w0);dzi=(w-w0)/5;jr,ji=map(F,upper['J'])
 return jr-dzr*mR+dzi*mI,ji-dzr*mI-dzi*mR

def main():
 a=json.loads((OLD/'FLOATING_BAND_RESULTS.json').read_text());b=json.loads((HERE/'FLOATING_BAND_RESULTS.json').read_text());up0=json.loads((OLDUPPER/'UPPER_RESULTS.json').read_text());up1=json.loads((HERE/'UPPER_RESULTS.json').read_text())
 assert a['status']==b['status']=='PASS' and a['IEEE_model']==b['IEEE_model']
 assert up0['gamma']==up1['gamma']=='1/10' and up0['mesh']==up1['mesh']
 sw0=json.loads((OLDSTATE/'P2_WITNESS.json').read_text());sw1=json.loads((HERE/'P2_WITNESS.json').read_text());assert sw0['topology_sha256']==sw1['topology_sha256'] and sw0['omega']=='9/2' and sw1['omega']=='289/64'
 assert json.loads((HERE/'P2_RESULTS.json').read_text())['exact_source_L2_squared']==20
 assert json.loads((OLDSTATE/'P2_RESULTS.json').read_text())['checks']['exact_source_L2_squared']==20
 def source_load_ast(path):
  fn=next(x for x in ast.parse(path.read_text()).body if isinstance(x,ast.FunctionDef) and x.name=='main')
  node=next(x for x in ast.walk(fn) if isinstance(x,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='f' for t in x.targets))
  return ast.dump(node.value,include_attributes=False)
 assert source_load_ast(OLDSTATE/'p2_state.py')==source_load_ast(HERE/'neighbor_state.py'),'affine source load construction changed'
 certs=[a['records'][-1],b['records'][-1]];assert all(x['precision_passed'] for x in certs)
 lo0,hi0=map(F,certs[0]['omega_interval']);lo1,hi1=map(F,certs[1]['omega_interval']);assert lo0<lo1<hi0<hi1
 overlap=[max(lo0,lo1),min(hi0,hi1)];assert overlap[0]<ev.SWITCH<overlap[1]
 assert ev.LOWER==lo0 and ev.UPPER==hi1 and [ev.ORIGINAL.LOWER,ev.ORIGINAL.UPPER]==[lo0,hi0] and [ev.NEIGHBOR.LOWER,ev.NEIGHBOR.UPPER]==[lo1,hi1]
 e0,e1=extent(lo0,hi0),extent(lo1,hi1);first,last=extent(lo0,hi1);overlapwords=extent(*overlap);switchword=bits(round64(ev.SWITCH));assert F.from_float(frombits(switchword))==ev.SWITCH
 assert e0[0]==first and e1[1]==last and e1[0]<=switchword<e0[1] and first<=switchword<last
 n0,n1=e0[1]-e0[0]+1,e1[1]-e1[0]+1;nover=overlapwords[1]-overlapwords[0]+1;n=last-first+1
 assert n==n0+n1-nover and nover>0
 assert e0[0]<=switchword<=e0[1] and e1[0]<=switchword+1<=e1[1]
 radii=[F(x['total_actual_floating_continuum_radius']) for x in certs];joined_radius=max(radii);assert joined_radius<F(1,10)
 words={first,last,switchword-1,switchword,switchword+1,e1[0]-1,e1[0],e1[0]+1,e0[1]-1,e0[1],e0[1]+1}|{first+(last-first)*i//512 for i in range(513)};rows=[]
 for word in sorted(words):
  w=frombits(word);branch=ev.branch(w);want=ev.ORIGINAL if word<=switchword else ev.NEIGHBOR;got=ev.evaluate(w);ref=want.evaluate(w);assert bits(got.real)==bits(ref.real) and bits(got.imag)==bits(ref.imag)
  assert (branch=='original')==(word<=switchword)
  if word in [first,last,switchword-1,switchword,switchword+1]:rows.append({'input_hex':w.hex(),'branch':branch,'output_hex':[got.real.hex(),got.imag.hex()]})
 s=frombits(switchword);p0,p1=ev.ORIGINAL.evaluate(s),ev.NEIGHBOR.evaluate(s);native_sep=sqrtup((F.from_float(p0.real)-F.from_float(p1.real))**2+(F.from_float(p0.imag)-F.from_float(p1.imag))**2);q0,q1=exact_at(up0,ev.SWITCH),exact_at(up1,ev.SWITCH);exact_sep=sqrtup(sum((x-y)**2 for x,y in zip(q0,q1)));assert native_sep<=sum(radii)
 left,right=ev.evaluate(frombits(switchword)),ev.evaluate(frombits(switchword+1));jump=sqrtup((F.from_float(left.real)-F.from_float(right.real))**2+(F.from_float(left.imag)-F.from_float(right.imag))**2)
 controls=[]
 for name,w in [('below union',frombits(first-1)),('above union',frombits(last+1)),('NaN',float('nan')),('infinity',float('inf')),('integer',4),('string','4.5')]:
  try:ev.evaluate(w)
  except ValueError:controls.append(name)
  else:raise AssertionError(name+' accepted')
 # A selector outside overlap would route valid union inputs to a leaf outside its certified domain.
 badswitch=hi0+F(1,1000);bad=frombits(e0[1]+1);assert F.from_float(bad)<=badswitch and not lo0<=F.from_float(bad)<=hi0;controls.append('switch moved above overlap would select uncertified original leaf')
 result={'status':'PASS','classification':'DERIVED_CONDITIONAL_JOINED_NEIGHBOR_STATE_BINARY64_BANDS','source_original_floating_results_sha256':hashlib.sha256((OLD/'FLOATING_BAND_RESULTS.json').read_bytes()).hexdigest(),'source_neighbor_floating_results_sha256':hashlib.sha256((HERE/'FLOATING_BAND_RESULTS.json').read_bytes()).hexdigest(),'source_joined_evaluator_sha256':hashlib.sha256((HERE/'joined_evaluator.py').read_bytes()).hexdigest(),'gamma':'1/10','centers':['9/2','289/64'],'original_interval':[str(lo0),str(hi0)],'neighbor_interval':[str(lo1),str(hi1)],'overlap':[str(x) for x in overlap],'overlap_width':str(overlap[1]-overlap[0]),'joined_interval':[str(lo0),str(hi1)],'joined_width':str(hi1-lo0),'previous_width':str(hi0-lo0),'joined_to_previous_width_ratio':str((hi1-lo0)/(hi0-lo0)),'selector':{'switch':str(ev.SWITCH),'switch_hex':s.hex(),'rule':'original if exact represented omega<=577/128; neighbor otherwise','original_selected_interval':[str(lo0),str(ev.SWITCH)],'neighbor_selected_interval':['('+str(ev.SWITCH),str(hi1)+']'],'branch_selection_adds_no_numeric_error':True,'switch_strictly_inside_real_and_binary64_overlap':True},'input_count':{'original':n0,'neighbor':n1,'overlap':nover,'union':n,'first_hex':frombits(first).hex(),'last_hex':frombits(last).hex(),'exact_inclusion_exclusion':True,'consecutive_word_partition_no_gap':True},'leaf_uniform_total_radii':[str(x) for x in radii],'joined_uniform_total_radius':str(joined_radius),'target':'1/10','joined_precision_passed':True,'same_benchmark_checks':{'same_gamma':True,'same_mesh_measures_reference':True,'same_P2_topology':True,'same_externally_declared_affine_source':True,'same_source_load_expression_AST':True,'same_IEEE_model':True},'seam_diagnostics':{'native_leaf_centers_same_input_separation_upper':str(native_sep),'exact_leaf_centers_same_input_separation_upper':str(exact_sep),'joined_adjacent_input_output_jump_upper':str(jump),'common_H_triangle_bound':str(sum(radii)),'scope':'Supplemental seam diagnostics; the piecewise selector is not claimed continuous or differentiable. Each leaf certificate applies to the same continuum H on overlap.'},'selector_controls':{'inputs_checked':len(words),'boundary_seam_records':rows,'controls':controls},'proof':'For every accepted represented omega, the exact selector chooses a leaf whose certified interval contains it. Its continuum-plus-floating radius<=max of the two leaf radii<1/10. Real overlap and consecutive binary64 word partition exclude holes. Both leaf bounds target the same source/domain/gamma continuum transfer.','scope':'Fixed gamma0.1, two actual saved P2 states and frozen scalar evaluators, conditional on declared binary64 RN semantics. No interpolation, output smoothing, new frequency calibration, full audit band, independent review, finite mesh termination or native UD constitutive law.','scientific_status':'OPEN','independent_review':False,'physical_promotion':0}
 p=HERE/'JOINED_RESULTS.json'
 if p.exists():assert json.loads(p.read_text())==result;print('read-only joined interval replay matches results',flush=True)
 else:p.write_text(json.dumps(result,indent=2)+'\n')
 print('PASS joined interval '+str([float(lo0),float(hi1)])+' overlap '+str(float(overlap[1]-overlap[0]))+' total radius '+str(float(joined_radius))+' represented inputs '+str(n)+' seam same-input separation '+str(float(native_sep)),flush=True)
if __name__=='__main__':main()
