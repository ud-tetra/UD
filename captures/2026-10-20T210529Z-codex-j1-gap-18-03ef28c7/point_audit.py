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
 old=REPO/'captures/2026-10-20T205157Z-codex-j1-gap-17-795c0022';contract=json.loads((HERE/'INITIAL_CONTRACT.json').read_text());freeze=json.loads((HERE/'PARAMETER_FREEZE.json').read_text());assert freeze['center']==['8983/2000','9/50'] and freeze['provisional_cover_goal']==contract['complete_cover_domain'] and freeze['finite_algorithm_budget']==contract['finite_algorithm_budget'];assert len(K.BANK)==20
 fn=next(x for x in ast.parse((HERE/'audit.py').read_text()).body if isinstance(x,ast.FunctionDef) and x.name=='source_checks');ns=dict(globals());exec(compile(ast.Module(body=[fn],type_ignores=[]),str(HERE/'audit.py'),'exec'),ns);ns['source_checks']()
 assert {sid:st for sid,st in K.BANK.items() if sid!='gap_18'}==json.loads((old/'BANK.json').read_text())['states']
 for name in ['kernel.py','rounding.py','evaluator.py']:assert (HERE/name).read_bytes()==(old/name).read_bytes()
 folder=HERE/'candidate';ancestor=old/'candidate';assert (folder/'state.py').read_text()==(ancestor/'state.py').read_text().replace('OMEGA=F(4624613,1024000)','OMEGA=F(8983,2000)').replace('GAMMA=F(17,100)','GAMMA=F(9,50)');assert all((folder/n).read_bytes()==(ancestor/n).read_bytes() for n in ['flux.py','curl.py','replay.py'])
 s=json.loads((folder/'P2_WITNESS.json').read_text());p=json.loads((folder/'P2_RESULTS.json').read_text());u=json.loads((folder/'UPPER_RESULTS.json').read_text());fw=json.loads(gzip.decompress((folder/'UPPER_WITNESS.json.gz').read_bytes()));assert s['omega']==p['omega']==u['omega']==fw['omega']=='8983/2000' and s['gamma']==p['gamma']==u['gamma']==fw['gamma']=='9/50'
 sh=hashlib.sha256((folder/'P2_WITNESS.json').read_bytes()).hexdigest();assert sh==fw['source_state_sha256']==u['source_state_sha256'];assert s['state_payload_sha256']==u['source_state_payload_sha256'] and p['corrected_algebraic_precision_passed'] and p['topology_matches_original_P2'] and p['exact_source_L2_squared']==20 and F(u['corrected_J_reported_continuum_radius'])<F(1,10)
 selected=json.loads((old/'PLACEMENT_RESULTS.json').read_text())['recommended_new_state'];assert [selected['omega'],selected['gamma']]==freeze['center']
 wl,wu=map(F,contract['complete_cover_domain']['omega']);gl,gu=map(F,contract['complete_cover_domain']['gamma']);wf,wt=P.word_domain(wl,wu);gf,gt=P.word_domain(gl,gu);w,g=frombits(wf),frombits(gt);ew,eg=F.from_float(w),F.from_float(g);assert F.from_float(frombits(wf-1))<wl<ew and eg<gu<F.from_float(frombits(gt+1));assert bits(K.CONSTANTS['gap_18']['OMEGA0'])==wf and bits(K.CONSTANTS['gap_18']['GAMMA0'])==gt
 cert=K.certificate('gap_18',(ew,ew,eg,eg));assert F(cert['total_radius'])<F(1,10);oldlower=min(K.point_formula_bounds(sid,ew,eg)[0] for sid in K.BANK if sid!='gap_18');assert oldlower>F(1,10)
 exact=K.EXACT['gap_18'];ref={k:F.from_float(v) for k,v in K.CONSTANTS['gap_18'].items()};ideal=dict(exact)
 for row in [ref,ideal]:row.update(omega=ew,gamma=eg)
 native=K.trace('gap_18',w,g)
 for j,(name,kind,a,b) in enumerate(K.OPS):
  rn=round64(K.op(ref[a],ref[b],kind));assert bits(rn)==bits(native[j]);ref[name]=F.from_float(rn);ideal[name]=K.op(ideal[a],ideal[b],kind);assert abs(ref[name]-ideal[name])<=F(cert['node_error_bounds'][j])
 dw2=ew**2-exact['OMEGA0']**2;di=2*(eg*ew-exact['GAMMA0']*exact['OMEGA0']);assert ideal['real']==exact['J_R']+dw2*exact['M_R']+di*exact['M_I'] and ideal['imag']==exact['J_I']+dw2*exact['M_I']-di*exact['M_R'];err=(ref['real']-ideal['real'])**2+(ref['imag']-ideal['imag'])**2;assert err<=F(cert['floating_radius'])**2
 previous=json.loads((old/'CONTRACT.json').read_text())['complete_cover_domain'];assert eg>F(previous['gamma'][1]);assert not (HERE/'COVER.json').exists()
 result={'status':'PASS','classification':'DERIVED_CONDITIONAL_ACTUAL_STATE_AND_ONE_REPRESENTED_INPUT_CERTIFICATE','center':freeze['center'],'own_reported_J_continuum_radius':u['corrected_J_reported_continuum_radius'],'phase_proxy_radius':u['phase_circle_reported_radius'],'state_defect_squared':u['defect_squared'],'exact_represented_input':{'omega':str(ew),'gamma':str(eg),'omega_hex':w.hex(),'gamma_hex':g.hex()},'represented_output_hex':[native[11].hex(),native[15].hex()],'point_certificate':cert,'old_nineteen_minimum_formula_lower_at_input':str(oldlower),'native_node_comparisons':16,'nearest_frequency_first_proposed_word':True,'nearest_damping_last_proposed_word':True,'nonbinary_center_quantization_included':True,'bank_and_source_checks':True,'current_uniform_coverage_upper_gamma':'17/100','new_uniform_guard_published':False,'scope':'New actual own-flux state plus exact represented-input continuum+floating certificate. Full proposed rectangle exhausted budget; no new uniform region/area/word count. Prospective complete-cover audit/evaluator not executed. Previous gamma<=17/100 guard remains authoritative. Old-family formula lower is not actual-error lower.','scientific_status':'OPEN','independent_review':False,'physical_promotion':0};P.save_or_compare('POINT_AUDIT_RESULTS.json',result);print('PASS own state and represented-input point certificate; radius='+str(float(F(cert['total_radius'])))+'; no uniform extension',flush=True)
if __name__=='__main__':main()
