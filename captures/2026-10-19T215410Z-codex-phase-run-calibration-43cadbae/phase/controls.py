"""Fixed source controls only, not extra prospective records or fits."""
import json
from fractions import Fraction as F
from pathlib import Path
from common import P,freeze,sha
from verify import int_frame_verdict
from recipes import round_ratio
import phase_controls,exact_t

def run():
    freeze();phase_controls.run();rows=[]
    for name,r,n,e,c,w in [('strict_boundary',F(1),F(0),F(1),F(1),'HOLD_FRAME_INCONCLUSIVE'),('strict_below',F(1,4),F(0),F(1),F(1),'CERTIFIED_FRAME_PASS'),('strict_above',F(4),F(0),F(1),F(1),'CERTIFIED_FRAME_FAIL'),('uncertain',F(4),F(4),F(1),F(1),'HOLD_FRAME_INCONCLUSIVE')]:
        got,_=int_frame_verdict(r,n,e,c);assert got==w;rows.append({'id':name,'actual':got,'expected':w})
    for n,d,w in [(1,2,0),(3,2,2),(-1,2,0),(-3,2,-2)]:assert round_ratio(n,d)==w
    rows.append({'id':'four_exact_signed_rounding_ties','status':'PASS'})
    out={'status':'PASS_FIXED_EXACT_T_FRAME_AND_ROUNDING_CONTROLS','rows':rows,'exact_T':exact_t.controls(),'new_estimator_calls':0,'physical_promotion':0};(P/'AUXILIARY_CONTROLS.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
