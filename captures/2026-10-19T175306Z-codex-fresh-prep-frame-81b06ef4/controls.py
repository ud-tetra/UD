"""Predetermined finite acceptance/refusal controls, without estimating a new cap."""
import json
from common import P,sha
from validate import constants,classify

def verify():
 c=constants();tests=[('interior',209,0,0,c['raw']/2,True,None),('wrong_order',207,0,0,c['raw']/2,False,'order_applicability'),('Gram_above_fixed_cap',209,c['eta']*2,0,c['raw']/2,False,'retained_Gram_cap'),('normal_above_fixed_cap',209,0,c['nu']*2,c['raw']/2,False,'fixed_normal_cap'),('frame_boundary_strict',209,0,0,c['raw'],False,'frame_budget')];rows=[]
 for name,q,e,n,r,want,key in tests:
  status,gates,b=classify(q,e,n,r,c);passed=not status.startswith('HOLD');assert passed==want and(key is None or not gates[key]);rows.append(dict(control=name,status=status,expected_acceptance=want,gates=gates,passed=True))
 return dict(status='ALL_FIVE_PREDECLARED_CONTROLS_PASSED',rows=rows,budget_sha256=sha(P/'inputs/FIXED_BUDGET.json'),physical_promotion=0)
if __name__=='__main__':
 r=verify();dest=P/'CONTROLS.json'
 if dest.exists():assert json.loads(dest.read_text())==r
 else:dest.write_text(json.dumps(r,indent=2))
 print(json.dumps(r))
