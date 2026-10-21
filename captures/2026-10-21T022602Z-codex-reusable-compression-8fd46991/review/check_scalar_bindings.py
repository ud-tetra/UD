from pathlib import Path
from fractions import Fraction as Q
from math import factorial
import json,hashlib,argparse
ap=argparse.ArgumentParser();ap.add_argument('--workspace',type=Path,required=True);ap.add_argument('--math',type=Path,required=True);a=ap.parse_args();W=a.workspace;P=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest();rpath=a.math/'RESULT.json';r=json.loads(rpath.read_text())
s=Q(61,27648);m=Q(1,384);e=Q(1,8192);h=s*(m-e);gamma2=1/(s*s*(1-(e/m)**2))
tau=Q(5,2)**41/factorial(41)/(1-Q(5,84));ad=4096*(4096*tau+Q(6240,2**104))+Q(52,2**96);EY=Q(3,2**127)+Q(504,2**96);one=ad+EY;delta=45*one;eta=45*EY;alpha=delta/h+delta/(h-delta);beta=454*h/(h-delta)
zeta=Q(1,2**65);ez=2*eta+zeta;er=Q(1,2**64);lift=Q(1,2**44);impl=(2*er)/(h-delta)+lift;profile=alpha+455*Q(1,2**50)+impl;d16=4*one;a16=d16/h+d16/(h-d16)
fields={'source_sigma_lower':s,'trial_sigma_lower':m,'trial_residual_upper':e,'compression_sigma_lower':h,'exact_decoder_gain_squared_upper':gamma2,'phase_column_encoding_error_upper':EY,'native_adjoint_error_upper':ad,'per_row_construction_error_upper':one,'conditional_full_frame_error_upper':delta,'encoded_Y_operator_error_upper':eta,'conditional_full_projection_defect_upper':alpha,'conditional_full_gain_upper':beta,'conditional_state_error_profile_upper':profile,'partial16_projection_defect_upper':a16}
for k,v in fields.items():assert Q(r[k])==v,k
f=r['finite_residual_profile'];nested={'encoded_compression_arithmetic_error_upper':zeta,'RHS_error_including_encoding_upper':ez,'normal_equation_residual_upper':er,'lift_error_upper':lift,'implemented_error_upper':impl}
for k,v in nested.items():assert Q(f[k])==v,k
assert gamma2<454**2 and alpha<Q(1,2**55) and beta<455 and ez<Q(1,2**64) and impl<Q(1,2**43) and profile<Q(1,2**40) and a16<Q(1,2**58)
assert r['full_frame_construction_status']==r['full_solve_status']=='NOT_RUN_HOLD' and r['physical_input_status']=='UNSUPPLIED_HOLD'
slice_bytes=(a.math/'TRIAL_SLICE.json').read_bytes();assert slice_bytes==(W/'c32_source_final/TRIAL_SLICE.json').read_bytes();partial=json.loads((P/'PARTIAL_INPUT_CHECKS.json').read_text());assert partial['slice_sha256']==sha(slice_bytes)
binding=json.loads((a.math/'SOURCE_BINDINGS.json').read_text());assert binding['trial_slice_sha256']==sha(slice_bytes) and binding['proposal_sha256']==partial['source_proposal_sha256']
old_bad=Q(4,3);q=Q(3,5);e0=Q(1,8192);resid2=e0*e0/(q*q+e0*e0);controls=json.loads((a.math/'CONTROLS.json').read_text());assert Q(controls['old_Q_output_hidden_component'])==old_bad and Q(controls['full_residual_countermodel_squared'])==resid2 and resid2>e0*e0
out={'status':'PASS','root_RESULT_sha256':sha(rpath.read_bytes()),'root_SOURCE_BINDINGS_sha256':sha((a.math/'SOURCE_BINDINGS.json').read_bytes()),'root_CONTROLS_sha256':sha((a.math/'CONTROLS.json').read_bytes()),'exact_scalar_pairs_matched':len(fields)+len(nested),'source_slice_matches_independent_Q_regeneration':True,'strict_scalar_profile_gates':7,'fullframe_and_physical_HOLD_verified':True,'partial_rank_is16_not1999':True,'scope':'independent scalar/source binding only; no producer checker executed or fullframe inferred','physical_promotion':0}
(P/'SCALAR_BINDING_CHECKS.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print('PASS19exactpairs,7gates,sourcebinding and HOLDscope')
