"""Exact own-state and one represented-input certificate; no new uniform guard."""
import sys
sys.dont_write_bytecode=True
import ast,json,hashlib,gzip
from pathlib import Path
from fractions import Fraction as F
import kernel as K
import planner as P
from rounding import bits,frombits,round64,pow2
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[1]
def main():
 assert (sys.float_info.radix,sys.float_info.mant_dig,sys.float_info.max_exp,sys.float_info.min_exp,sys.float_info.rounds)==(2,53,1024,-1021,1)
 old=REPO/'captures/2026-10-21T000423Z-codex-j1-bank-24-11c33657';contract=json.loads((HERE/'CONTRACT.json').read_text());assert len(K.BANK)==28
 def fn(path,name):return next(x for x in ast.parse(path.read_text()).body if isinstance(x,ast.FunctionDef) and x.name==name)
 check=fn(HERE/'audit.py','source_checks');ns=dict(globals());exec(compile(ast.Module(body=[check],type_ignores=[]),str(HERE/'audit.py'),'exec'),ns);ns['source_checks']()
 freeze=json.loads((HERE/'PARAMETER_FREEZE.json').read_text());ancestor=REPO/freeze['constructor_capture']/'candidate';folder=HERE/'candidate';sid='left_25'
 assert (folder/'state.py').read_text()==(ancestor/'state.py').read_text().replace('OMEGA=F(158523806250434577,35184372088832000)','OMEGA=F(8983,2000)').replace('GAMMA=F(23,100)','GAMMA=F(1,4)')
 assert all((folder/n).read_bytes()==(ancestor/n).read_bytes() for n in ['flux.py','curl.py','replay.py'])
 for name in ['kernel.py','rounding.py','evaluator.py','planner.py']:assert (HERE/name).read_bytes()==(old/name).read_bytes()
 for name in ['source_checks','verify_tree','native_controls']:assert ast.dump(fn(HERE/'audit.py',name),include_attributes=False)==ast.dump(fn(old/'audit.py',name),include_attributes=False)
 s=json.loads((folder/'P2_WITNESS.json').read_text());p=json.loads((folder/'P2_RESULTS.json').read_text());u=json.loads((folder/'UPPER_RESULTS.json').read_text());fw=json.loads(gzip.decompress((folder/'UPPER_WITNESS.json.gz').read_bytes()));assert s['omega']==p['omega']==u['omega']==fw['omega']=='8983/2000' and s['gamma']==p['gamma']==u['gamma']==fw['gamma']=='1/4'
 sh=hashlib.sha256((folder/'P2_WITNESS.json').read_bytes()).hexdigest();assert sh==fw['source_state_sha256']==u['source_state_sha256'] and s['state_payload_sha256']==u['source_state_payload_sha256'];assert p['corrected_algebraic_precision_passed'] and p['topology_matches_original_P2'] and p['exact_source_L2_squared']==20 and u['reported_J_precision_passed']
 assert K.EXACT[sid]['OMEGA0']!=F.from_float(K.CONSTANTS[sid]['OMEGA0']) and K.EXACT[sid]['GAMMA0']==F.from_float(K.CONSTANTS[sid]['GAMMA0'])
 assert freeze['center']==['8983/2000','1/4'] and freeze['state_key']==sid and freeze['provisional_cover_goal']==contract['complete_cover_domain'] and freeze['finite_algorithm_budget']==contract['finite_algorithm_budget'] and freeze['placement_grid']==contract['placement_grid'] and freeze['placement_probe_domain']==contract['placement_probe_domain'] and contract['placement_probe_domain']['gamma']==['1/4','13/50']
 selection=json.loads((old/'PLACEMENT_RESULTS.json').read_text());selected=selection['recommended_new_state'];assert selection['formula_count']==27 and selected['all_transported_formulas_above_target'] and freeze['source_selected_formula_lower']==selected['minimum_formula_lower'] and [selected['omega'],selected['gamma']]==freeze['center'];assert hashlib.sha256((old/'PLACEMENT_RESULTS.json').read_bytes()).hexdigest()==freeze['source_placement_sha256']
 w,g=map(F,freeze['center']);assert all(freeze['binary64_centers'][key]=={'hex':K.CONSTANTS[sid][name].hex(),'stored_minus_exact':str(F.from_float(K.CONSTANTS[sid][name])-x)} for key,name,x in [('omega','OMEGA0',w),('gamma','GAMMA0',g)]);oldlower=min(K.point_formula_bounds(k,w,g)[0] for k in K.BANK if k!=sid);newupper=K.point_formula_bounds(sid,w,g)[1];assert oldlower==F(selected['minimum_formula_lower'])>F(1,10)>newupper
 oldbank=json.loads((old/'BANK.json').read_text())['states'];assert {k:st for k,st in K.BANK.items() if k!=sid}==oldbank

 wl,wu=map(F,contract['complete_cover_domain']['omega']);gl,gu=map(F,contract['complete_cover_domain']['gamma']);wf,wt=P.word_domain(wl,wu);gf,gt=P.word_domain(gl,gu)
 assert F.from_float(frombits(wf-1))<wl<F.from_float(frombits(wf)) and bits(K.CONSTANTS[sid]['OMEGA0'])==wf
 assert F.from_float(frombits(gt))==gu==g<F.from_float(frombits(gt+1)) and bits(K.CONSTANTS[sid]['GAMMA0'])==gt
 ow,og=frombits(wf),frombits(gt);ew,eg=map(F.from_float,[ow,og]);cert=K.certificate(sid,(ew,ew,eg,eg));assert F(cert['total_radius'])<F(1,10);old_point_lower=min(K.point_formula_bounds(k,ew,eg)[0] for k in K.BANK if k!=sid);assert old_point_lower>F(1,10)
 exact=K.EXACT[sid];ref={k:F.from_float(v) for k,v in K.CONSTANTS[sid].items()};ideal=dict(exact)
 for row in [ref,ideal]:row.update(omega=ew,gamma=eg)
 native=K.trace(sid,ow,og)
 for j,(name,kind,a,b) in enumerate(K.OPS):
  rn=round64(K.op(ref[a],ref[b],kind));assert bits(rn)==bits(native[j]);ref[name]=F.from_float(rn);ideal[name]=K.op(ideal[a],ideal[b],kind);assert abs(ref[name]-ideal[name])<=F(cert['node_error_bounds'][j])
 dw2=ew**2-exact['OMEGA0']**2;di=2*(eg*ew-exact['GAMMA0']*exact['OMEGA0']);assert ideal['real']==exact['J_R']+dw2*exact['M_R']+di*exact['M_I'] and ideal['imag']==exact['J_I']+dw2*exact['M_I']-di*exact['M_R'];err=(ref['real']-ideal['real'])**2+(ref['imag']-ideal['imag'])**2;assert err<=F(cert['floating_radius'])**2
 pc=json.loads((old/'COVER.json').read_text());assert freeze['previous_uniform_capture']==str(old.relative_to(REPO)) and hashlib.sha256((old/'COVER.json').read_bytes()).hexdigest()==freeze['previous_uniform_cover_sha256'];assert pc['domain']['gamma'][1]==freeze['previous_uniform_upper_gamma']=='6/25' and F(pc['domain']['gamma'][1])<eg and not (HERE/'COVER.json').exists()
 diagnostic=json.loads((HERE/'DIAGNOSTIC_RESULTS.json').read_text());assert diagnostic['status']=='UNRESOLVED_FROZEN_BUDGET' and diagnostic['formula_count']==28 and diagnostic['goal']==freeze['provisional_cover_goal'] and diagnostic['finite_algorithm_budget']==freeze['finite_algorithm_budget'] and not diagnostic['partial_leaves_published_as_coverage']
 local=json.loads((HERE/'LOCAL_SCOUT_RESULTS.json').read_text());lf=json.loads((HERE/'LOCAL_SCOUT_FREEZE.json').read_text());assert local['probe_count']==lf['frequency_samples']==257 and local['formula_count']==len(K.BANK) and set(local['selected_formula_bounds_by_state'])==set(K.BANK) and all(row['formula_count']==len(K.BANK) and row['all_transported_formulas_above_target']==(F(row['minimum_formula_lower'])>F(1,10)) for row in local['rows']);assert local['formula_obstruction'] and F(local['selected']['minimum_formula_lower'])>F(1,10)
 result={'status':'PASS','classification':'DERIVED_CONDITIONAL_ACTUAL_STATE_AND_ONE_REPRESENTED_INPUT_CERTIFICATE','center':freeze['center'],'formula_count':len(K.BANK),'source_state_sha256':sh,'own_reported_J_continuum_radius':u['corrected_J_reported_continuum_radius'],'phase_proxy_radius':u['phase_circle_reported_radius'],'state_defect_squared':u['defect_squared'],'exact_represented_input':{'omega':str(ew),'gamma':str(eg),'omega_hex':ow.hex(),'gamma_hex':og.hex()},'represented_output_hex':[native[11].hex(),native[15].hex()],'point_certificate':cert,'old_twenty_seven_minimum_formula_lower_at_input':str(old_point_lower),'old_twenty_seven_minimum_formula_lower_at_center':str(oldlower),'new_state_model_upper_at_center':str(newupper),'native_node_comparisons':16,'nearest_frequency_first_proposed_word':True,'nearest_damping_last_proposed_word':True,'damping_center_exactly_binary64':True,'frequency_constant_error':str(F.from_float(K.CONSTANTS[sid]['OMEGA0'])-w),'damping_constant_error':'0','bank_and_source_checks':True,'current_uniform_coverage_upper_gamma':'6/25','new_uniform_guard_published':False,'constructor_capture':freeze['constructor_capture'],'placement_bank_uniform_capture':freeze['source_placement_capture'],'scope':'New actual own-flux state plus exact represented-input continuum+floating certificate. Full proposed rectangle exhausted frozen budget;no new uniform region/area/word count. Prospective complete-cover audit/evaluator not executed as global API. Previous gamma<=6/25 guard remains authoritative. Old-family and local formula lowers are not actual-error lowers.','scientific_status':'OPEN','independent_review':False,'physical_promotion':0}
 P.save_or_compare('POINT_AUDIT_RESULTS.json',result);print('PASS own state and represented-input point certificate; radius='+str(float(F(cert['total_radius'])))+'; no uniform extension',flush=True)
if __name__=='__main__':main()
