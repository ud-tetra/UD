from fractions import Fraction as F
from pathlib import Path
import json
p=Path(__file__).resolve().parent
A=(1,2,-1);M=(1,0,0)
cases=[('length_time',[(0,1,0),(0,0,1)],None,(1,0,0)),('energy_time',[(1,2,-2),(0,0,1)],(1,1),None),('direct_action',[A],(1,),None),('base_units',[(1,0,0),(0,1,0),(0,0,1)],A,None),('dimensionless_only',[(0,0,0)],None,(1,0,0))]
results=[]
for name,W,c,v in cases:
 if c is not None:
  assert tuple(sum(F(c[j])*W[j][i] for j in range(len(W))) for i in range(3))==A
  results.append({'case':name,'action':'IDENTIFIED_CONDITIONAL','certificate':list(c)})
 else:
  assert all(sum(x*y for x,y in zip(w,v))==0 for w in W)
  assert sum(x*y for x,y in zip(A,v))!=0
  for s in (F(1,2),F(2),F(3)):
   assert all(s**sum(x*y for x,y in zip(w,v))==1 for w in W)
   assert s**sum(x*y for x,y in zip(A,v))!=1
  results.append({'case':name,'action':'NONIDENTIFIED','ambiguity':list(v)})
# A0 fixed under (B,a,tau)->(B/s^2,s*a,tau), while mass changes.
v=(-2,1,0)
assert sum(x*y for x,y in zip(A,v))==0
assert sum(x*y for x,y in zip(M,v))!=0
wrong=(1,0)
assert tuple(sum(wrong[j]*cases[1][1][j][i] for j in range(2)) for i in range(3))!=A
r=json.loads((p/'REGISTRATION_CANDIDATE.json').read_text())
required=['native_predictor','species_assignment','dimensional_map','heldout_dataset','scoring_rule','uncertainty_rule','reviewer','custodian_ruling']
missing=[k for k in required if r[k] is None]
assert len(missing)==8 and r['target_release_authorized'] is False
out={'verification':'PASS_SCOPED','exact_anchor_cases':results,'negative_controls':['wrong energy-only certificate rejected','action does not fix mass','incomplete registration refused'],'missing_release_fields':missing,'registration':'HOLD','physical_promotion':0}
print(json.dumps(out,indent=2))
