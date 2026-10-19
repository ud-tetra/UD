"""Uniform conditional returned-output bound; no claim every solver run meets gates."""
import json,hashlib
from pathlib import Path
from flint import arb,fmpq,ctx
ctx.prec=512
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
a=lambda x:arb(fmpq(*x))
def up(x):
 z=(x*(1<<180)).ceil().unique_fmpz();assert z is not None
 return [int(z),1<<180]
def down(x):
 z=(x*(1<<180)).floor().unique_fmpz();assert z is not None
 return [int(z),1<<180]
def verify(gates=None,delta=None):
 f=json.loads((P/'FREEZE.json').read_text())
 for n,h in f['code_sha256'].items():assert sha(P/n)==h
 for n,h in f['input_sha256'].items():assert sha(P/'inputs'/n)==h
 g=f['gates'] if gates is None else gates;noise=a(f['encoded_vector_noise'] if delta is None else delta)
 uniform=json.loads((P/'inputs/PARENT_UNIFORM.json').read_text());mt=json.loads((P/'inputs/PARENT_PHASE.json').read_text())['metrics'];order=json.loads((P/'inputs/PARENT_ORDER.json').read_text())
 eta=a(g['full_left_orthogonality']);eps=a(g['full_SVD_error']);assert eta<1
 p=lambda v:v/(1+(1-v).sqrt())
 r=a(uniform['baseline_low_rank_residual_upper']);C=a(uniform['per_vector_noise_multiplier_upper']);s0=a(order['qth_sigma_lower']);tail0=a(order['qplus1_sigma_upper']);cut=a(f['source_cutoff'])
 e=r+C*noise+eps;alpha=s0-r
 eta0=a(mt['basis_orthogonality_upper']);assert eta0<1
 beta=a(uniform['deleted_two_rows_beta_lower']);sigma0=a(uniform['comparison_shift_residual_upper']);M0=a(uniform['comparison_shift_norm_upper'])
 orderok=bool(s0-C*noise-eps>cut and tail0+C*noise+eps<cut)
 result={'status':'HOLD_UNIFORM_CONDITIONAL_OUTPUT_BOUND','encoded_vector_noise':f['encoded_vector_noise'] if delta is None else delta,'order209_guaranteed_for_admitted_outputs':orderok,'gates':g,'physical_promotion':0,'uniform_solver_success_claimed':False,'external_review':'PENDING','lane':'development — no registry entry'}
 if not alpha>2*e:result['reason']='subspace_gap';return result
 t=e/(alpha-e);distance=(2-2*(1-t*t).sqrt()).sqrt()+2*p(eta)
 if not beta>distance:result['reason']='deleted_row_margin';return result
 sigmaa=a(g['raw_shift_residual'])/(1-eta).sqrt();rho=a(g['inverse_residual']);assert rho<1
 deltaeig=a(g['eigenpair_residual'])*a(g['proposed_inverse_norm'])/(1-rho)
 b=(sigma0+sigmaa+distance*(1+M0))/(beta-distance)
 hD=a(mt['source_inverse_norm_upper'])/(1-a(mt['source_inverse_residual_upper']));dD=a(mt['source_reduction_norm_upper']);Lj=a(mt['intertwining_residual_upper']);k0=((1+eta0)/(1-eta0)).sqrt();ka=((1+eta)/(1-eta)).sqrt()
 R=hD*Lj+k0*hD*dD*(b+ka*deltaeig);sep=a(mt['minimum_target_chord_lower'])
 result.update(subspace_distance_upper=up(distance),shift_distance_upper=up(b),eigenvalue_radius_upper=up(R),target_chord_lower=down(sep),exact_model_order_guaranteed=bool(s0-C*noise>cut and tail0+C*noise<cut))
 if R<1:
  angle=R.asin()+a(g['emitted_argument_error']);passed=orderok and 2*R<sep and 2*angle<sep
  result.update(phase_error_upper=up(angle),strict_matching_margin_lower=down(sep/2-angle),readable={'subspace_distance_upper':float(distance.upper()),'eigenvalue_radius_upper':float(R.upper()),'two_step_phase_error_upper':float(angle.upper()),'half_target_chord_lower':float((sep/2).lower()),'matching_margin_lower':float((sep/2-angle).lower())})
  if passed:result['status']='CERTIFIED_UNIFORM_CONDITIONAL_RETURNED_OUTPUT_PHASE_BOUND'
 return result
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');args=p.parse_args();r=verify()
 if args.replay:assert json.loads((P/'UNIFORM_CERTIFICATE.json').read_text())==r
 else:
  assert not (P/'UNIFORM_CERTIFICATE.json').exists();(P/'UNIFORM_CERTIFICATE.json').write_text(json.dumps(r,indent=2))
 print(json.dumps(r),flush=True)
