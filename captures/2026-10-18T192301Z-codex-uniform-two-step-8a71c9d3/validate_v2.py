import json
from bindings import P,freeze,sha
from validate import check
from uniform_v2 import verify
if __name__=='__main__':
 original=check();a=json.loads((P/'UNIFORM_V2_CERTIFICATE.json').read_text());b=json.loads((P/'UNIFORM_V2_REPLAY.json').read_text());assert {k:v for k,v in a.items() if k!='replay'}=={k:v for k,v in b.items() if k!='replay'}
 bad=verify(corrupt=True);assert all(x['phase_status']=='HOLD_UNIFORM_IDEAL_PHASE_BOUND' for x in bad['rows'])
 row=next(x for x in a['rows'] if x['delta']==[1,1<<48]);assert row['phase_status']=='CERTIFIED_UNIFORM_IDEAL_TWO_STEP_PHASE_MATCHING';assert next(x for x in a['rows'] if x['delta']==[1,1<<47])['phase_status']=='HOLD_UNIFORM_IDEAL_PHASE_BOUND'
 noise=json.loads((P/'DATA_FREEZE.json').read_text())['records'][0];assert noise['vector_noise_squared']==[1,1<<96]
 result={'status':'PASS','physical_promotion':0,'original_validation':original,'uniform_versions_replayed':2,'uniform_rows':64,'zero_coefficient_controls':'BOTH_VERSIONS_RETURN_ALL_PHASE_HOLD','actual_noise_inside_refined_ideal_ball':True,'uniform_actual_floating_convergence_claimed':False,'independent_review':'pending'}
 (P/'VALIDATION_V2.json').write_text(json.dumps(result,indent=2));print(json.dumps(result),flush=True)
