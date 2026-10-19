"""Predeclared finite refusal controls, separate from primary output results."""
import json
import numpy as np
from flint import arb
from common import P,a,sha
from frame import constants,classify
from cutoff_phase import cutoff_predicate,match_emissions

def verify():
 c=constants();rows=[];cases=[('frame_interior',209,0,0,c['raw']/2,True,None),('wrong_frame_order',207,0,0,c['raw']/2,False,'order_applicability'),('Gram_above_fixed_cap',209,c['eta']*2,0,c['raw']/2,False,'retained_Gram_cap'),('normal_above_fixed_cap',209,0,c['nu']*2,c['raw']/2,False,'fixed_normal_cap'),('frame_strict_boundary',209,0,0,c['raw'],False,'frame_budget')]
 for name,q,e,n,r,want,key in cases:
  status,gates,b=classify(q,e,n,r,c);assert (not status.startswith('HOLD'))==want and(key is None or not gates[key]);rows.append(dict(control=name,status=status,passed=True))
 cut=arb(1)/(1<<24)
 for name,q,e,s,want in [('cutoff_interior',209,cut/4,2*cut,True),('cutoff_tail_equality',209,cut,3*cut,False),('cutoff_leading_equality',209,cut/4,cut*5/4,False),('cutoff_wrong_order',207,cut/4,2*cut,False)]:
  got=cutoff_predicate(q,e,s,cut);assert got==want;rows.append(dict(control=name,accepted=got,passed=True))
 with np.load(P/'inputs/PARENT_EMISSION.npz',allow_pickle=False) as z:em=z['two_step_phase']
 for name,values,want in [('saved_emission_match',em.copy(),True),('shifted_stationary_emission',em.copy(),False),('duplicated_emission',em.copy(),False)]:
  if name=='shifted_stationary_emission':values[0]+=1<<40
  if name=='duplicated_emission':values[1]=values[0]
  result=match_emissions(values);got=result['status']=='CERTIFIED_OBSERVED_TWO_STEP_EMISSION_BIJECTION';assert got==want;rows.append(dict(control=name,status=result['status'],passed=True))
 return dict(status='TWELVE_DECLARED_CONTROLS_PASS',rows=rows,scope='Five inherited frame/refusal predicates and four exact cutoff boundary controls, and three saved/emission-mutation controls. Main numeric witnesses unchanged.',physical_promotion=0)
if __name__=='__main__':
 r=verify();dest=P/'CONTROLS.json'
 if dest.exists():assert json.loads(dest.read_text())==r
 else:dest.write_text(json.dumps(r,indent=2))
 print(json.dumps(r))
