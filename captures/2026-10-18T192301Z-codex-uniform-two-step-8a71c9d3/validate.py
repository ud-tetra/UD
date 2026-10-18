import json,subprocess,sys
from bindings import P,freeze,sha
from uniform import verify

def check():
 freeze();u=json.loads((P/'UNIFORM_CERTIFICATE.json').read_text());v=json.loads((P/'UNIFORM_REPLAY.json').read_text());assert {k:x for k,x in u.items() if k!='replay'}=={k:x for k,x in v.items() if k!='replay'}
 o=P/'results/cyclic_unit'
 for a,b,ignored in [('ORDER_CERTIFICATE.json','ORDER_REPLAY.json',['replay']),('CERTIFICATE.json','REPLAY_CERTIFICATE.json',['replay','seconds'])]:
  aa=json.loads((o/a).read_text());bb=json.loads((o/b).read_text());assert {k:x for k,x in aa.items() if k not in ignored}=={k:x for k,x in bb.items() if k not in ignored}
 assert sha(o/'PHASE_PROPOSAL.npz')==sha(P/'results/original-cyclic_unit/PHASE_PROPOSAL.npz');assert json.loads((o/'CERTIFICATE.json').read_text())['status']=='CERTIFIED_ACTUAL_TWO_STEP_PHASE_MATCHING'
 corrupted=verify(corrupt=True);assert all(r['phase_status']=='HOLD_UNIFORM_IDEAL_PHASE_BOUND' for r in corrupted['rows'])
 return {'status':'PASS','physical_promotion':0,'uniform_rows':len(u['rows']),'uniform_ideal_passing_rows':sum(x['phase_status'].startswith('CERTIFIED') for x in u['rows']),'unchanged_original_instrumented_output':True,'actual_phase_replay_identical':True,'zero_factor_control':'ALL_UNIFORM_PHASE_ROWS_HOLD','uniform_actual_floating_convergence_claimed':False,'independent_review':'pending'}
if __name__=='__main__':
 r=check();(P/'VALIDATION.json').write_text(json.dumps(r,indent=2));print(json.dumps(r),flush=True)
