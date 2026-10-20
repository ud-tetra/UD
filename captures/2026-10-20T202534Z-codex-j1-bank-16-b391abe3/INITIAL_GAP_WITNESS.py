import sys
sys.dont_write_bytecode=True
import json,hashlib,ast
from pathlib import Path
from fractions import Fraction as F
import kernel as K
import planner as P
from rounding import bits,round64
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[1]

def main():
 old=REPO/'captures/2026-10-20T200808Z-codex-j1-central-15-e4124521'
 for name in ['BANK.json','kernel.py','rounding.py','planner.py','evaluator.py']:assert (HERE/name).read_bytes()==(old/name).read_bytes()
 # Reuse the complete source/constant/AST audit function without importing a prospective evaluator lacking a cover.
 source=(old/'audit.py').read_text();tree=ast.parse(source);fn=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='source_checks');ns=dict(globals());exec(compile(ast.Module(body=[fn],type_ignores=[]),str(old/'audit.py'),'exec'),ns);ns['source_checks']()
 q=json.loads((HERE/'SCOUT_RESULTS.json').read_text())['recommended_new_state'];w,g=map(F,[q['omega'],q['gamma']]);rw,rg=round64(w),round64(g);ew,eg=F.from_float(rw),F.from_float(rg);bounds={sid:K.point_formula_bounds(sid,ew,eg) for sid in sorted(K.BANK)};lower=min(v[0] for v in bounds.values());assert lower>F(1,10)
 certs=[K.certificate(sid,(ew,ew,eg,eg)) for sid in sorted(K.BANK)];best=min(certs,key=lambda x:(F(x['total_radius']),x['state']));assert F(best['total_radius'])>F(1,10)
 result={'status':'PASS','classification':'EXACT_CONDITIONAL_REPRESENTED_INPUT_FORMULA_OBSTRUCTION','input':{'omega':str(ew),'gamma':str(eg),'omega_hex':rw.hex(),'gamma_hex':rg.hex(),'omega_word':bits(rw),'gamma_word':bits(rg)},'rational_grid_candidate':{'omega':str(w),'gamma':str(g)},'formula_bounds_by_state':{s:list(map(str,v)) for s,v in bounds.items()},'minimum_formula_lower':str(lower),'minimum_point_total_upper':best['total_radius'],'point_best_state':best['state'],'target':'1/10','all_seventeen_formulas_above_target':True,'unchanged_bank_and_kernel_source_checks':True,'scope':'All seventeen specified transported-upper formulas exceed target at this exact represented input. The declared box bounds are monotone under box inclusion and dominate their point formulas; subdividing cannot certify this input within this family. This is not an actual-error lower, exclusion of alternate flux/dual certificates, or a physical/no-go result.','next_action':'Construct an own state/flux upper at the refined-grid rational candidate before repeating the complete-region audit. New-state precision and coverage are unproven.','scientific_status':'OPEN','independent_review':False,'physical_promotion':0};P.save_or_compare('FORMULA_GAP_WITNESS.json',result);print('PASS represented-input all17-formula lower='+str(float(lower))+' >0.1; next state=('+str(w)+','+str(g)+')',flush=True)
if __name__=='__main__':main()
