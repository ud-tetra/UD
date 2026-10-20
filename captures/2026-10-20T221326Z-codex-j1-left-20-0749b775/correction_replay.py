"""Check the scout-label correction without changing any scientific number."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
import planner as P
HERE=Path(__file__).resolve().parent
OLD='all_twenty_two_transported_formulas_above_target'
NEW='all_twenty_three_transported_formulas_above_target'
def normalize(x):
 if isinstance(x,dict):return {(NEW if k==OLD else k):normalize(v) for k,v in x.items()}
 if isinstance(x,list):return [normalize(v) for v in x]
 if isinstance(x,str):return x.replace('twenty-two particular','twenty-three particular')
 return x
def read(n):return json.loads((HERE/n).read_text())
def main():
 initial=read('PLACEMENT_RESULTS.json');final=read('PLACEMENT_RESULTS_v0_2.json');assert normalize(initial)==final
 assert len(final['rows'])==1032 and len(P.K.BANK)==23
 for row in final['rows']:
  assert set(row['formula_lower_by_state'])==set(P.K.BANK)
  assert row[NEW]==(F(row['minimum_formula_lower'])>F(1,10))
 a=read('AUDIT_RESULTS.json');b=read('AUDIT_RESULTS_v0_2.json');assert normalize({k:v for k,v in a.items() if k!='source_sha256'})=={k:v for k,v in b.items() if k!='source_sha256'}
 for name in ['kernel.py','evaluator.py','BANK.json','CONTRACT.json','COVER.json']:assert a['source_sha256'][name]==b['source_sha256'][name]
 src=(HERE/'INITIAL_planner.py').read_text().replace(OLD,NEW).replace('twenty-two particular','twenty-three particular').replace('PLACEMENT_RESULTS.json','PLACEMENT_RESULTS_v0_2.json');assert src==(HERE/'planner.py').read_text()
 src=(HERE/'INITIAL_audit.py').read_text().replace("(HERE/'PLACEMENT_RESULTS.json')","(HERE/'PLACEMENT_RESULTS_v0_2.json')").replace("'COVER.json','PLACEMENT_RESULTS.json'","'COVER.json','PLACEMENT_RESULTS_v0_2.json'").replace("P.save_or_compare('AUDIT_RESULTS.json'","P.save_or_compare('AUDIT_RESULTS_v0_2.json'");assert src==(HERE/'audit.py').read_text()
 result={'status':'PASS','classification':'EXACT_NUMERICAL_EQUIVALENCE_OF_SCOUT_LABEL_CORRECTION','states_checked':23,'probe_count':1032,'per_state_formula_rows_checked':23*1032,'all_coordinates_bounds_flags_selected_point_unchanged':True,'all_non_source_hash_audit_data_unchanged':True,'cover_bytes_hash_unchanged':True,'source_changes_exactly_declared':True,'source_sha256':{n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in ['INITIAL_planner.py','INITIAL_audit.py','planner.py','audit.py','correction_replay.py','PLACEMENT_RESULTS.json','PLACEMENT_RESULTS_v0_2.json','AUDIT_RESULTS.json','AUDIT_RESULTS_v0_2.json','COVER.json']},'found_by':'construction','independent_review':False,'physical_promotion':0}
 P.save_or_compare('CORRECTION_REPLAY_RESULTS.json',result);print('PASS scout-label correction:23736 per-state rows and all scientific audit data unchanged',flush=True)
if __name__=='__main__':main()
