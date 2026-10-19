"""Small exact logical controls for strict endpoint classification, no data/fit."""
import json
from fractions import Fraction as F
from common import P,freeze
from verify import int_frame_verdict
def run():
    freeze();rows=[]
    cases=[('zero',F(0),F(0),'CERTIFIED_FRAME_PASS'),('strict_equality',F(1),F(0),'HOLD_FRAME_INCONCLUSIVE'),('above_cap',F(4),F(0),'CERTIFIED_FRAME_FAIL'),('normal_correction_required',F(4),F(4),'HOLD_FRAME_INCONCLUSIVE')]
    for name,r2,n2,expected in cases:
        verdict,lower=int_frame_verdict(r2,n2,F(1),F(1));assert verdict==expected
        rows.append({'id':name,'expected':expected,'actual':verdict,'exact_lower':[str(lower.numerator),str(lower.denominator)]})
    try:int_frame_verdict(F(-1),F(0),F(1),F(1))
    except AssertionError:rows.append({'id':'negative_squared_residual','actual':'ASSERTION_REJECTION'})
    else:raise AssertionError('invalid input accepted')
    result={'status':'PASS_FIVE_EXACT_ENDPOINT_LOGIC_CONTROLS','rows':rows,'new_estimator_runs':0,'physical_promotion':0};p=P/'CONTROLS.json';assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'controls':len(rows)}),flush=True)
if __name__=='__main__':run()
