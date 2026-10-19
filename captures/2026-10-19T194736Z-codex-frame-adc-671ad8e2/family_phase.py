"""Directed family frame/phase bounds; ideal and explicitly conditional floating lanes."""
import json,hashlib
from pathlib import Path
from flint import arb,fmpq,ctx
ctx.prec=512
P=Path(__file__).resolve().parent
load=lambda p:json.loads(Path(p).read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
a=lambda p:arb(fmpq(int(p[0]),int(p[1])))
def ep(x,lower=False):
 n=((x*(1<<180)).floor() if lower else (x*(1<<180)).ceil()).unique_fmpz();assert n is not None
 return [int(n),1<<180]
def certify():
 family=load(P/'inputs/FAMILY_CERTIFICATE.json')
 generation=load(P/'inputs/BASE_GENERATION.json')['row']
 phase=load(P/'inputs/SOURCE_PHASE.json')['metrics']
 u=load(P/'inputs/PARENT_UNIFORM.json')
 policy=load(P/'inputs/OLD_POLICY.json')['gates']
 fixed=load(P/'inputs/FIXED_BUDGET.json')['source_budget']
 q=209;n=family['nscalar'];v=family['nvector'];assert n==18790154 and v==303067
 quantum=arb(1)/(1<<48);rho=a(family['rho']);delta=a(family['delta_per_62_vector']);cut=arb(1)/(1<<24)
 k=a(family['sketch_F_squared']).sqrt();F0=a(family['baseline_F_squared']).sqrt();g=a(family['anchor_min_lower']);d0=a(generation['evaluation_bounds']['scalar_waveform_error_upper']);sn=arb(n).sqrt();sv=arb(v).sqrt()
 eta0=a(phase['basis_orthogonality_upper']);spanop=a(phase['source_frame_span_residual_upper']);hD=a(phase['source_inverse_norm_upper'])/(1-a(phase['source_inverse_residual_upper']))
 rankmargin=(1-eta0).sqrt()-spanop*hD;assert rankmargin>0
 t0op=spanop*hD/(1-eta0).sqrt();t0F=arb(q).sqrt()*t0op
 beta=a(u['deleted_two_rows_beta_lower']);sigma=a(u['comparison_shift_residual_upper']);M0=a(u['comparison_shift_norm_upper']);K=((1+eta0)/(1-eta0)).sqrt()*hD*a(phase['source_reduction_norm_upper']);L=hD*a(phase['intertwining_residual_upper']);sep=a(phase['minimum_target_chord_lower'])
 raw_frame_cap=a(fixed['allowed_raw_frame_residual_lower']);shift_cap=a(fixed['allowance_lower'])
 def tail(d):return k*((d0+quantum/2)*sn+d*sv)
 def gam(r,d):return g-k*(F0*r+quantum*sn+(d+quantum)*sv)
 def align(t2,tF):
  assert 0<=t2<1 and tF>=0
  c=(2/(1+(1-t2*t2).sqrt())).sqrt()
  return c*t2,c*tF
 def ideal(name,r,d,gamma):
  tau=tail(d);assert gamma>tau>0
  t=tau/gamma;t2=t+t0op;tF=t+t0F;d2,dF=align(t2,tF);assert beta>dF
  JF=sigma+(1+M0)*dF
  # Conservative common Frobenius-frame transport, matching parent theorem.
  b=(sigma+JF+dF*(1+M0))/(beta-dF);R=L+K*b;assert 0<R<1
  angle=R.asin();unique=bool(2*R<sep and 2*angle<sep)
  return {'case':name,'rho':ep(r),'delta':ep(d),'gamma_lower':ep(gamma,True),'source_error_F_upper':ep(tau),'source_sine_F_upper':ep(t),'reference_plus_source_sine2_upper':ep(t2),'reference_plus_source_sineF_upper':ep(tF),'aligned_distance2_upper':ep(d2),'aligned_distanceF_upper':ep(dF),'optimal_raw_alignment_residual_upper':ep(tF),'ideal_LS_shift_F_upper':ep(JF),'deleted_row_margin_lower':ep(beta-dF,True),'source_eigenvalue_radius_upper':ep(R),'nearest_some_target_phase_error_upper':ep(angle),'strict_unique_target_bound_pass':unique,'old_raw_frame_sufficiency_pass':bool(tF<raw_frame_cap),'published_shift_allowance_sufficiency_pass':bool(JF<shift_cap),'scope':'Exact leading-SVD orthonormal basis and exact lag-two LS only; some-target phase enclosure, not a target permutation when unique=false.','readable':{'source_error_F_upper':float(tau.upper()),'aligned_distance_F_upper':float(dF.upper()),'ideal_LS_shift_F_upper':float(JF.upper()),'eigenvalue_radius_upper':float(R.upper()),'nearest_some_target_phase_error_upper':float(angle.upper())}}
 ideal_rows=[ideal('PR233_wide_exact_ideal',rho,delta,a(family['sigma209_lower'])),ideal('one_quantum_same_rho_exact_ideal',rho,quantum,gam(rho,quantum)),ideal('zero_noise_zero_rho_coarse_floor',arb(0),arb(0),gam(arb(0),arb(0)))]
 eta=a(policy['full_left_orthogonality']);eps2=a(policy['full_SVD_error']);nu=a(fixed['normal_cap']);eigdelta=a(policy['eigenpair_residual'])*a(policy['proposed_inverse_norm'])/(1-a(policy['inverse_residual']));arg=a(policy['emitted_argument_error']);tau=tail(delta);gamma=a(family['sigma209_lower']);assert gamma>eps2
 floating=[]
 for name,epsF in [('qualified_full_factor_F_bound',eps2),('operator_only_projected_F_inflation',arb(q).sqrt()*eps2)]:
  t2=(tau+eps2)/(gamma-eps2)+t0op;tF=(tau+epsF)/(gamma-eps2)+t0F;d2,dF=align(t2,tF);polar=eta/(1+(1-eta).sqrt());d2+=2*polar;dF+=2*polar;assert beta>dF
  rstar=(1+eta).sqrt()*(tF+2*polar);JF=(1+eta).sqrt()*(sigma+(1+M0)*dF);amin=(1-eta).sqrt()*(beta-dF);shift=(JF*JF+(nu/amin)**2).sqrt();b=(sigma+shift/(1-eta).sqrt()+dF*(1+M0))/(beta-dF);R=L+K*(b+((1+eta)/(1-eta)).sqrt()*eigdelta);assert 0<R<1;angle=R.asin()+arg
  floating.append({'case':name,'data_factor_quality_premise_required':True,'full_factor_Gram_premise_required':True,'normal_eigenpair_inverse_argument_gates_required':True,'sineF_upper':ep(tF),'aligned_distanceF_upper':ep(dF),'optimal_raw_alignment_residual_upper':ep(rstar),'returned_raw_shift_F_upper':ep(shift),'source_eigenvalue_radius_upper':ep(R),'nearest_some_target_emitted_phase_error_upper':ep(angle),'strict_unique_target_bound_pass':bool(2*R<sep and 2*angle<sep),'old_raw_frame_sufficiency_pass':bool(rstar<raw_frame_cap),'published_shift_allowance_sufficiency_pass':bool(shift<shift_cap),'readable':{'aligned_distance_F_upper':float(dF.upper()),'returned_shift_F_upper':float(shift.upper()),'eigenvalue_radius_upper':float(R.upper()),'nearest_some_target_emitted_phase_error_upper':float(angle.upper())}})
 result={'status':'DERIVED_NONUNIQUE_FAMILY_PHASE_ENCLOSURES_AND_FIXED_GATE_SUFFICIENCY_HOLD','ideal_rows':ideal_rows,'conditional_floating_rows':floating,'source_reference_offset':{'source_span_metric_norm':'operator only; no Frobenius upgrade','source_rank_margin_lower':ep(rankmargin,True),'source_to_baseline_sine2_upper':ep(t0op),'source_to_baseline_sineF_upper':ep(t0F),'sqrt209_F_inflation_explicit':True},'source_minimum_target_chord_lower':ep(sep,True),'raw_frame_cap':ep(raw_frame_cap),'published_shift_allowance':ep(shift_cap),'source_error_is_Frobenius_by_explicit_PR233_model_bound_not_by_sigma210_alone':True,'no_narrower_PASS_from_this_coarse_zero_floor':not ideal_rows[-1]['strict_unique_target_bound_pass'],'new_records_fits_or_phase_output_evaluations':0,'source_provenance_sha256':sha(P/'INPUT_PROVENANCE.json'),'scope':'All exact ideal family members get nearest-some-source eigenvalue/phase bounds. Old frame/unique-target sufficiency HOLD is not a failure counterexample. Conditional floating rows require verified data/factor and output gates; no uniform library convergence or physical/SI claim.','external_review':'PENDING','physical_promotion':0}
 return result
