"""Read-only state/point and frozen failed-cover diagnostic replay."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
import json,copy,hashlib
import planner as P
import kernel as K
import own_checks
HERE=Path(__file__).resolve().parent

def main():
 f=json.loads((HERE/'DIAGNOSTIC_FREEZE.json').read_text());contract=json.loads((HERE/'CONTRACT.json').read_text());freeze=json.loads((HERE/'PARAMETER_FREEZE.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
 assert sha(HERE/'PARAMETER_FREEZE.json')==f['parent_parameter_freeze_sha256'] and sha(HERE/'SCALAR_GENERATION.log')==f['original_failure_log_sha256'] and sha(HERE/'BANK.json')==f['unchanged_bank_sha256'] and sha(HERE/'CONTRACT.json')==f['unchanged_contract_sha256']
 assert not (HERE/'COVER.json').exists() and not (HERE/'AUDIT_RESULTS.json').exists() and f['original_full_rectangle_attempt_exit_code']==1
 for dep in contract['source_dependencies']:
  p=HERE.parents[1]/dep['path'];assert p.stat().st_size==dep['size_bytes'] and sha(p)==dep['sha256']
 point=own_checks.main();observed=[]
 def trace(frame,event,arg):
  if frame.f_code.co_filename==P.__file__ and frame.f_code.co_name=='visit' and event=='exception' and isinstance(arg[1],AssertionError) and str(arg[1])=='unresolved cell at depth budget' and not observed:
   v=frame.f_locals;observed.append({k:v[k] for k in ['box','words','depth','cert']})
  return trace
 sys.settrace(trace)
 try:P.create_cover(contract)
 except AssertionError as exc:assert str(exc)=='unresolved cell at depth budget'
 else:raise AssertionError('expected frozen full cover failure did not recur')
 finally:sys.settrace(None)
 assert len(observed)==1;v=observed[0];box=v['box'];words=v['words'];assert v['depth']==contract['finite_algorithm_budget']['max_depth']==30 and F(v['cert']['total_radius'])>F(contract['target'])
 certs={s:K.certificate(s,box) for s in sorted(K.BANK)};assert v['cert']==min(certs.values(),key=lambda x:(F(x['total_radius']),x['state']))
 exact_point=((box[0]+box[1])/2,(box[2]+box[3])/2);bounds={s:K.point_formula_bounds(s,*exact_point) for s in sorted(K.BANK)}
 diag_contract=copy.deepcopy(contract);diag_contract['placement_probe_domain']=f['diagnostic_probe_domain'];assert diag_contract['placement_grid']==f['diagnostic_grid'];placement=P.placement(diag_contract);P.save_or_compare('IN_GOAL_PLACEMENT_RESULTS.json',placement);q=placement['recommended_new_state'];assert placement['formula_count']==39 and placement['probe_count']==1032 and q['all_transported_formulas_above_target'] and F(q['minimum_formula_lower'])>F(1,10)
 assert all(F(contract['complete_cover_domain'][k][0])<=x<=F(contract['complete_cover_domain'][k][1]) for k,x in zip(['omega','gamma'],exact_point))
 result={'status':'PASS_EXPECTED_FROZEN_COVER_FAILURE_REPRODUCED','classification':'OWN_STATE_PASS_FULL_RECTANGLE_UNRESOLVED','original_generation_exit_code':1,'point_certificate_passed':True,'formula_count':len(K.BANK),'full_rectangle_passed':False,'current_certified_uniform_upper_gamma':'2/5','attempted_upper_gamma':'41/100','budget_unchanged':contract['finite_algorithm_budget'],'failure':'unresolved cell at depth budget','first_unresolved':{'proof_box':list(map(str,box)),'word_box':list(words),'depth':v['depth'],'minimum_box_certificate':v['cert'],'point':list(map(str,exact_point)),'point_formula_lower_by_state':{s:str(x[0]) for s,x in bounds.items()},'minimum_point_formula_lower':str(min(x[0] for x in bounds.values())),'minimum_point_model_upper':str(min(x[1] for x in bounds.values()))},'in_goal_probe_count':placement['probe_count'],'recommended_new_state':q,'frozen_future_scout_executed':False,'source_sha256':{n:sha(HERE/n) for n in ['PARAMETER_FREEZE.json','DIAGNOSTIC_FREEZE.json','CONTRACT.json','BANK.json','SCALAR_GENERATION.log','POINT_AUDIT_RESULTS.json','IN_GOAL_PLACEMENT_RESULTS.json','diagnostic_replay.py']},'scope':'Expected algorithm failure and finite-grid particular-upper-formula obstruction only;not failure of actual error,continuum solvability,all possible certificates or all meshes. No41/100 rectangle or future coverage. Constructor verification,not independent review.','scientific_status':'OPEN','independent_review':False,'physical_promotion':0}
 P.save_or_compare('DIAGNOSTIC_RESULTS.json',result);print('PASS own point;expected full rectangle failure at depth30;selected in-goal point=('+q['omega']+','+q['gamma']+') lower='+str(float(F(q['minimum_formula_lower']))),flush=True)
if __name__=='__main__':main()
