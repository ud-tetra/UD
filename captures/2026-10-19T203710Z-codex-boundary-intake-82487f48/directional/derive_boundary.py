"""Logical nested-ball necessary exclusion from exact finite saved-output failures."""
import json
from fractions import Fraction as F
from datetime import datetime,timezone
from common import P,sha,freeze
def main():
    freeze();f=json.loads((P/'BOUNDARY_FREEZE.json').read_text())
    for n,h in f['files'].items():assert sha(P/n)==h,n
    c=json.loads((P/'CERTIFICATE.json').read_text());d=json.loads((P/'DATA_FREEZE.json').read_text());fr=lambda p:F(*map(int,p));cap=fr(c['strict_frame_cap'])
    failures=[r for r in c['rows'] if r['frame_verdict']=='CERTIFIED_FRAME_FAIL'];assert failures
    witness=min(failures,key=lambda r:r['integer_amplitude']);amp=witness['integer_amplitude'];record=next(r for r in d['records'] if r['case']==witness['case']);lower=fr(witness['exact_minimum_alignment_residual_squared_lower'])
    assert lower>cap**2 and record['rho_distance_to_exact_anchor']==[0,1] and record['per_vector_squared_integer_noise']==amp**2 and amp>0
    radius=F(amp,1<<48);assert fr(record['delta_per_62_vector'])==radius
    result={'status':'DERIVED_NESTED_CLOSED_BALL_NECESSARY_EXCLUSION','counterexample_case':witness['case'],'counterexample_record_sha256':witness['record_sha256'],'counterexample_amplitude':amp,'counterexample_vector_noise_radius':[radius.numerator,radius.denominator],'uniform_strict_frame_admission_requires_radius_strictly_less_than':[radius.numerator,radius.denominator],'exact_minimal_residual_squared_lower':witness['exact_minimum_alignment_residual_squared_lower'],'unchanged_strict_raw_frame_cap':c['strict_frame_cap'],'source_anchor':'reverse_stationary','anchor_distance':[0,1],'closed_ball_contains_all_encoded_vectors_with_norm_at_most_radius':True,'proof':'For any delta >= witnessed per62-vector norm, this exact record belongs to the closed noise ball at the fixed source anchor. Its actual saved returned basis excludes every source alignment under the unchanged strict frame cap. Hence universal strict-frame admission by this actual frozen estimator on that ball is false. Set inclusion, not monotonicity of the estimator response, supplies the implication.','finite_frame_pass_amplitudes':[r['integer_amplitude'] for r in c['rows'] if r['frame_verdict']=='CERTIFIED_FRAME_PASS'],'finite_frame_fail_amplitudes':[r['integer_amplitude'] for r in c['rows'] if r['frame_verdict']=='CERTIFIED_FRAME_FAIL'],'finite_frame_hold_amplitudes':[r['integer_amplitude'] for r in c['rows'] if r['frame_verdict'].startswith('HOLD')],'smaller_sampled_PASS_proves_uniform_ball_sufficiency':False,'monotone_directional_response_claimed':False,'ideal_SVD_phase_or_physical_failure_claimed':False,'certificate_sha256':sha(P/'CERTIFICATE.json'),'boundary_freeze_sha256':sha(P/'BOUNDARY_FREEZE.json'),'completed_utc':datetime.now(timezone.utc).isoformat(),'external_review':'PENDING','physical_promotion':0}
    p=P/'NESTED_BALL_EXCLUSION.json';assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'necessary_radius_ceiling':result['uniform_strict_frame_admission_requires_radius_strictly_less_than']}))
if __name__=='__main__':main()
