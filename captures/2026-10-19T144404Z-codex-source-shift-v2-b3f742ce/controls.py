"""Finite boundary/refusal tests; synthetic metrics are not new estimator outputs."""
import copy,json
from source_math import P,a,derive,evaluate,up,freeze
freeze()
g=derive();limit=g['raw_shift_strict_upper_allowance_lower']
m=copy.deepcopy(g['other_seven_gates']);m['raw_shift_residual']=[0,1]
tests=[]
def test(name,metrics,eligible,expect):
    r=evaluate(metrics,eligible);assert (r['status']=='CERTIFIED_RETURNED_OUTPUT_V2') is expect,name
    tests.append({'name':name,'status':r['status'],'failed':r['failed']})
test('zero_shift_other_gates_at_frozen_maxima',m,True,True)
m['raw_shift_residual']=limit;test('equality_to_lower_allowance_is_HOLD',m,True,False)
m['raw_shift_residual']=[limit[0]-1,limit[1]];test('one_dyadic_unit_below_allowance',m,True,True)
m['raw_shift_residual']=[limit[0]+1,limit[1]];test('one_dyadic_unit_above_allowance',m,True,False)
m['raw_shift_residual']=[1,1<<30];test('large_shift_HOLD',m,True,False)
m['raw_shift_residual']=[0,1];test('ineligible_record_HOLD',m,False,False)
for n,v in g['other_seven_gates'].items():
    bad=copy.deepcopy(m);bad[n]=[2*v[0],v[1]];test('exceeded_'+n,bad,True,False)
result={'status':'PASS_FINITE_V2_BOUNDARIES','controls':tests,
        'synthetic_metric_controls_not_actual_estimator_runs':True,'physical_promotion':0}
dest=P/'CONTROLS.json'
if dest.exists():assert json.loads(dest.read_text())==result
else:dest.write_text(json.dumps(result,indent=2))
print(json.dumps(result),flush=True)
