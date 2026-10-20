import sys
sys.dont_write_bytecode=True
from pathlib import Path
import json,hashlib
from fractions import Fraction as F
import planner as P
HERE=Path(__file__).resolve().parent

def main():
 f=json.loads((HERE/'SCOUT_FREEZE.json').read_text());assert hashlib.sha256((HERE/'BANK.json').read_bytes()).hexdigest()==f['bank_sha256'];result=P.placement(f);assert result['probe_count']==1032;result['classification']='POST_STATE_FINITE_GRID_FORMULA_DIAGNOSTIC';P.save_or_compare('SCOUT_RESULTS.json',result);q=result['recommended_new_state'];print('PASS post-state scout selected=('+q['omega']+','+q['gamma']+') lower='+str(float(F(q['minimum_formula_lower'])))+' all20 above='+str(q['all_twenty_transported_formulas_above_target']),flush=True)
if __name__=='__main__':main()
