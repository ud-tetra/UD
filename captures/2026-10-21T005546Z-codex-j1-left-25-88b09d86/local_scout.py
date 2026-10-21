import sys
sys.dont_write_bytecode=True
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
import kernel as K
import planner as P
from rounding import bits,frombits,round64
HERE=Path(__file__).resolve().parent

def main():
 f=json.loads((HERE/'LOCAL_SCOUT_FREEZE.json').read_text());assert hashlib.sha256((HERE/'BANK.json').read_bytes()).hexdigest()==f['bank_sha256'];assert hashlib.sha256((HERE/'DIAGNOSTIC_RESULTS.json').read_bytes()).hexdigest()==f['source_diagnostic_sha256'];assert len(K.BANK)==28;wl,wu=map(F,f['omega']);upper=F(f['exact_gamma_upper']);g=round64(upper)
 if F.from_float(g)>upper:g=frombits(bits(g)-1)
 eg=F.from_float(g);assert eg<=upper<F.from_float(frombits(bits(g)+1));rows=[]
 for i in range(f['frequency_samples']):
  w=wl+(wu-wl)*i/(f['frequency_samples']-1);ew=F.from_float(round64(w));bounds={sid:K.point_formula_bounds(sid,ew,eg) for sid in sorted(K.BANK)};lo=min(v[0] for v in bounds.values());hi=min(v[1] for v in bounds.values());rows.append({'formula_count':len(K.BANK),'rational_omega':str(w),'represented_omega':str(ew),'minimum_formula_lower':str(lo),'minimum_model_upper':str(hi),'all_transported_formulas_above_target':lo>F(1,10)})
 assert len(rows)==257 and all(row['formula_count']==len(K.BANK) and row['all_transported_formulas_above_target']==(F(row['minimum_formula_lower'])>F(1,10)) for row in rows)
 q=min(rows,key=lambda r:(-F(r['minimum_formula_lower']),F(r['rational_omega'])));ew=F(q['represented_omega']);lo=F(q['minimum_formula_lower']);bounds={sid:list(map(str,K.point_formula_bounds(sid,ew,eg))) for sid in sorted(K.BANK)};assert F(8983,2000)<=ew<=F(36193,8000) and F(6,25)<eg<=F(1,4)
 result={'status':'PASS','classification':'EXACT_CONDITIONAL_LOCAL_FINITE_GRID_FORMULA_DIAGNOSTIC','formula_count':len(K.BANK),'probe_count':len(rows),'rows':rows,'selected':q,'represented_gamma':str(eg),'represented_gamma_hex':g.hex(),'selected_formula_bounds_by_state':bounds,'formula_obstruction':lo>F(1,10),'recommended_new_state':{'omega':q['rational_omega'],'gamma':'1/4'},'scope':'Finite257-frequency local grid only. If minimum lower>1/10, all28 declared transported-upper formulas fail target at this inside-goal represented input; monotone box bounds cannot fix that input by subdivision alone. Never an actual-error lower or exclusion of alternate flux/dual certificates.','scientific_status':'OPEN','independent_review':False,'physical_promotion':0};P.save_or_compare('LOCAL_SCOUT_RESULTS.json',result);print('PASS local257 scout lower='+str(float(lo))+' obstruction='+str(result['formula_obstruction'])+' next=('+q['rational_omega']+',1/4)',flush=True)
if __name__=='__main__':main()
