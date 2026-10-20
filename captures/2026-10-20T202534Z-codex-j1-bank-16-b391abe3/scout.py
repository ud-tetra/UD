import sys
sys.dont_write_bytecode=True
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
import kernel as K
import planner as P
HERE=Path(__file__).resolve().parent

def main():
 f=json.loads((HERE/'SCOUT_FREEZE.json').read_text());assert hashlib.sha256((HERE/'BANK.json').read_bytes()).hexdigest()==f['bank_sha256'];wl,wu=map(F,f['omega']);gl,gu=map(F,f['gamma']);rows=[]
 for i in range(f['omega_samples']):
  w=wl+(wu-wl)*i/(f['omega_samples']-1)
  for j in range(1,f['gamma_subdivisions']+1):
   g=gl+(gu-gl)*j/f['gamma_subdivisions'];bounds={sid:K.point_formula_bounds(sid,w,g) for sid in sorted(K.BANK)};lo=min(v[0] for v in bounds.values());hi=min(v[1] for v in bounds.values());rows.append({'omega':str(w),'gamma':str(g),'minimum_formula_lower':str(lo),'minimum_model_upper':str(hi),'all_seventeen_formulas_above_target':lo>F(1,10)})
 assert len(rows)==f['expected_probes'];q=min(rows,key=lambda x:(-F(x['minimum_formula_lower']),F(x['omega']),F(x['gamma'])));full={sid:list(map(str,K.point_formula_bounds(sid,F(q['omega']),F(q['gamma'])))) for sid in sorted(K.BANK)}
 result={'status':'PASS','classification':'EXACT_CONDITIONAL_FINITE_GRID_FORMULA_DIAGNOSTIC','probe_count':len(rows),'above_target_probe_count':sum(x['all_seventeen_formulas_above_target'] for x in rows),'rows':rows,'recommended_new_state':q,'selected_formula_bounds_by_state':full,'scope':f['ranking'],'physical_promotion':0};P.save_or_compare('SCOUT_RESULTS.json',result);print('PASS refined scout probes='+str(len(rows))+' formula-gap probes='+str(result['above_target_probe_count'])+' selected=('+q['omega']+','+q['gamma']+') lower='+str(float(F(q['minimum_formula_lower']))),flush=True)
if __name__=='__main__':main()
