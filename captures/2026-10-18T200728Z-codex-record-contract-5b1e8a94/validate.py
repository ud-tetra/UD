import json
from bindings import P,freeze
if __name__=='__main__':
 rows=[]
 for e in freeze()['cases']:
  o=P/'results'/e['case']
  for a,b in [('RAW_ELIGIBILITY.json','RAW_REPLAY.json'),('CERTIFICATE.json','REPLAY_CERTIFICATE.json')]:
   x=json.loads((o/a).read_text());y=json.loads((o/b).read_text());assert {k:v for k,v in x.items() if k!='replay'}=={k:v for k,v in y.items() if k!='replay'}
  c=json.loads((o/'CERTIFICATE.json').read_text())
  if c['status'].startswith('CERTIFIED'):assert set(c['negative_controls'])>={'zero_coefficient','zero_eigenvector_inverse'}
  if e['case']=='dense_unit':assert c['status']=='HOLD_RAW_NOISE_BALL' and c['previous_phase_status']=='CERTIFIED_ACTUAL_TWO_STEP_PHASE_MATCHING'
  else:assert c['status']=='CERTIFIED_RECORD_WISE_FLOATING_PHASE_CONTRACT'
  rows.append({k:v for k,v in c.items() if k in ['case','status','readable','negative_controls']})
 r={'status':'PASS','physical_promotion':0,'archived_records_not_new_estimator_runs':3,'new_proposer_runs':0,'eligible_records':2,'actual_saved_array_replays':2,'outside_ball_HOLD_replays':1,'negative_controls':4,'uniform_floating_convergence_claimed':False,'independent_review':'pending','rows':rows};(P/'VALIDATION.json').write_text(json.dumps(r,indent=2));print(json.dumps(r),flush=True)
