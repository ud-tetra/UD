"""Exact own-state binding and one represented-input continuum/floating certificate."""
import sys
sys.dont_write_bytecode=True
import ast,json,hashlib,gzip
from pathlib import Path
from fractions import Fraction as F
import kernel as K
import planner as P
from rounding import bits,frombits,round64
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[1]
def main():
 assert (sys.float_info.radix,sys.float_info.mant_dig,sys.float_info.max_exp,sys.float_info.min_exp,sys.float_info.rounds)==(2,53,1024,-1021,1)
 freeze=json.loads((HERE/'PARAMETER_FREEZE.json').read_text());contract=json.loads((HERE/'CONTRACT.json').read_text());old=REPO/freeze['source_bank_capture'];uniform=REPO/freeze['previous_uniform_capture'];sid=freeze['state_key'];assert sid=='left_41' and len(K.BANK)==39
 for dep in contract['source_dependencies']:
  p=REPO/dep['path'];assert p.stat().st_size==dep['size_bytes'] and hashlib.sha256(p.read_bytes()).hexdigest()==dep['sha256']
 def fn(path,name):return next(x for x in ast.parse(path.read_text()).body if isinstance(x,ast.FunctionDef) and x.name==name)
 check=fn(HERE/'audit.py','source_checks');ns=dict(globals());exec(compile(ast.Module(body=[check],type_ignores=[]),str(HERE/'audit.py'),'exec'),ns);ns['source_checks']()
 folder=HERE/'candidate';ancestor=REPO/freeze['constructor_capture']/'candidate'
 assert (folder/'state.py').read_text()==(ancestor/'state.py').read_text().replace('GAMMA=F(9,25)','GAMMA=F(41,100)') and all((folder/n).read_bytes()==(ancestor/n).read_bytes() for n in ['flux.py','curl.py','replay.py'])
 for name in ['kernel.py','rounding.py','evaluator.py','planner.py']:assert (HERE/name).read_bytes()==(old/name).read_bytes()
 for name in ['source_checks','verify_tree','native_controls']:assert ast.dump(fn(HERE/'audit.py',name),include_attributes=False)==ast.dump(fn(old/'audit.py',name),include_attributes=False)
 oldbank=json.loads((old/'BANK.json').read_text())['states'];assert {k:v for k,v in K.BANK.items() if k!=sid}==oldbank
 s=json.loads((folder/'P2_WITNESS.json').read_text());p=json.loads((folder/'P2_RESULTS.json').read_text());u=json.loads((folder/'UPPER_RESULTS.json').read_text());fw=json.loads(gzip.decompress((folder/'UPPER_WITNESS.json.gz').read_bytes()));assert s['omega']==p['omega']==u['omega']==fw['omega']=='8983/2000' and s['gamma']==p['gamma']==u['gamma']==fw['gamma']=='41/100'
 sh=hashlib.sha256((folder/'P2_WITNESS.json').read_bytes()).hexdigest();assert sh==fw['source_state_sha256']==u['source_state_sha256'] and s['state_payload_sha256']==u['source_state_payload_sha256'] and p['corrected_algebraic_precision_passed'] and p['topology_matches_original_P2'] and p['exact_source_L2_squared']==20 and u['reported_J_precision_passed']
 assert freeze['center']==['8983/2000','41/100'] and freeze['provisional_cover_goal']==contract['complete_cover_domain'] and freeze['finite_algorithm_budget']==contract['finite_algorithm_budget']=={'max_depth':30,'max_leaves':4096} and freeze['placement_grid']==contract['placement_grid'] and freeze['placement_probe_domain']==contract['placement_probe_domain']
 assert contract['complete_cover_domain']=={'omega':['8983/2000','36193/8000'],'gamma':['1/10','41/100']}
 source=old/freeze['source_placement_file'];selection=json.loads(source.read_text());q=selection['recommended_new_state'];assert hashlib.sha256(source.read_bytes()).hexdigest()==freeze['source_placement_sha256'] and selection['formula_count']==38 and [q['omega'],q['gamma']]==freeze['center'] and q['all_transported_formulas_above_target'] and q['minimum_formula_lower']==freeze['source_selected_formula_lower']
 w,g=map(F,freeze['center']);ow,gconstant=map(float,[w,g]);assert all(freeze['binary64_centers'][key]=={'hex':x.hex(),'stored_minus_exact':str(F.from_float(x)-v)} for key,x,v in [('omega',ow,w),('gamma',gconstant,g)])
 assert all(K.EXACT[sid][key]!=F.from_float(K.CONSTANTS[sid][key]) for key in ['OMEGA0','GAMMA0'])
 exact_center_old_lower=min(K.point_formula_bounds(k,w,g)[0] for k in oldbank);newupper=K.point_formula_bounds(sid,w,g)[1];assert exact_center_old_lower==F(q['minimum_formula_lower'])>F(1,10)>newupper
 wl,wu=map(F,contract['complete_cover_domain']['omega']);gl,gu=map(F,contract['complete_cover_domain']['gamma']);wf,wt=P.word_domain(wl,wu);gf,gt=P.word_domain(gl,gu)
 og=frombits(gt);ew,eg=map(F.from_float,[ow,og]);assert bits(ow)==wf and F.from_float(frombits(wf-1))<wl==w<ew and bits(gconstant)==gt and eg<gu<F.from_float(frombits(gt+1))
 old_lower=min(K.point_formula_bounds(k,ew,eg)[0] for k in oldbank);assert old_lower>F(1,10)
 cert=K.certificate(sid,(ew,ew,eg,eg));assert F(cert['total_radius'])<F(1,10)
 exact=K.EXACT[sid];ref={k:F.from_float(v) for k,v in K.CONSTANTS[sid].items()};ideal=dict(exact)
 for row in [ref,ideal]:row.update(omega=ew,gamma=eg)
 native=K.trace(sid,ow,og)
 for j,(name,kind,a,b) in enumerate(K.OPS):
  rn=round64(K.op(ref[a],ref[b],kind));assert bits(rn)==bits(native[j]);ref[name]=F.from_float(rn);ideal[name]=K.op(ideal[a],ideal[b],kind);assert abs(ref[name]-ideal[name])<=F(cert['node_error_bounds'][j])
 dw2=ew**2-exact['OMEGA0']**2;di=2*(eg*ew-exact['GAMMA0']*exact['OMEGA0']);assert ideal['real']==exact['J_R']+dw2*exact['M_R']+di*exact['M_I'] and ideal['imag']==exact['J_I']+dw2*exact['M_I']-di*exact['M_R'];assert (ref['real']-ideal['real'])**2+(ref['imag']-ideal['imag'])**2<=F(cert['floating_radius'])**2
 assert hashlib.sha256((uniform/'COVER.json').read_bytes()).hexdigest()==freeze['previous_uniform_cover_sha256'] and json.loads((uniform/'COVER.json').read_text())['domain']['gamma'][1]=='2/5'
 result={'status':'PASS','classification':'DERIVED_CONDITIONAL_OWN_STATE_AND_REPRESENTED_INPUT_CERTIFICATE','center':freeze['center'],'formula_count':39,'source_state_sha256':sh,'source_selection_is_represented_input':False,'exact_represented_input':{'omega':str(ew),'gamma':str(eg),'omega_hex':ow.hex(),'gamma_hex':og.hex()},'represented_output_hex':[native[11].hex(),native[15].hex()],'point_certificate':cert,'own_reported_J_continuum_radius':u['corrected_J_reported_continuum_radius'],'phase_proxy_radius':u['phase_circle_reported_radius'],'state_defect_squared':u['defect_squared'],'old_38_minimum_formula_lower_at_represented_input':str(old_lower),'old_38_minimum_formula_lower_at_exact_center':str(exact_center_old_lower),'new_state_model_upper_at_exact_center':str(newupper),'nearest_frequency_first_proposed_word':True,'nearest_frequency_interior_word':False,'nearest_frequency_last_proposed_word':False,'nearest_damping_last_proposed_word':True,'nearest_damping_first_excluded_word':False,'represented_input_uses_last_accepted_damping':True,'frequency_constant_error':str(ew-w),'damping_constant_error':str(F.from_float(gconstant)-g),'native_node_comparisons':16,'prior_38_bank_entries_unchanged':True,'scientific_status':'OPEN','independent_review':False,'physical_promotion':0,'scope':'Own-state and exact represented-input certificate only. Full-cover outcome separate. Formula lower diagnostic does not lower-bound actual error.'}
 P.save_or_compare('POINT_AUDIT_RESULTS.json',result);print('PASS own left-corner state and represented-input radius='+str(float(F(cert['total_radius']))),flush=True);return result
if __name__=='__main__':main()
