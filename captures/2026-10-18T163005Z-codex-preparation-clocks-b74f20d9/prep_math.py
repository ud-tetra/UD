from fractions import Fraction as F
from flint import arb,fmpq
from proof_math import up,down

def aa(x):return arb(fmpq(*x))
def pair(x):x=F(x);return [x.numerator,x.denominator]
def exact_phase(c,lower,e):
 out={'model_sigma105_lower':down(lower),'total_sketch_error_upper':up(e)}
 if not lower>2*e:return {**out,'status':'HOLD_SUBSPACE_SEPARATION','unique_phase_matching':False}
 a=aa(c['frame_Gram_lower']);b=aa(c['frame_Gram_upper']);n=c['time_rows'];q=c['temporal_order'];t=e/(lower-e);d=(2-2*(1-t*t).sqrt()).sqrt();beta=(1-arb(q)/(n*a)).sqrt();K=(b/a).sqrt()
 if not d<beta:return {**out,'status':'HOLD_DELETED_ROW_RANK','unique_phase_matching':False}
 radius=K*d*(1+K)/(beta-d);unique=bool(radius<1 and 2*radius<aa(c['minimum_chord_separation_lower']));angle=radius.asin() if radius<1 else None
 return {**out,'status':'CERTIFIED_CONDITIONAL_PREPARATION_CLOCK_MATCHING' if unique else 'ONE_SIDED_ENCLOSURE_ONLY','unique_phase_matching':unique,'subspace_sine_upper':up(t),'basis_distance_upper':up(d),'eigenvalue_radius_upper':up(radius),'phase_error_radians_upper':up(angle) if angle is not None else None,'readable':{'model_sigma105_lower':float(lower.lower()),'total_sketch_error_upper':float(e.upper()),'phase_error_radians_upper':float(angle.upper()) if angle is not None else None}}

def budget(c,m,offset_box,prep_fraction,jitter,rate,raw_delta,profile_gamma=None,model_floor=True):
 offset_box=F(offset_box);prep_fraction=F(prep_fraction);jitter=F(jitter);rate=F(rate);raw_delta=F(raw_delta);assert min(offset_box,prep_fraction,jitter,rate,raw_delta)>=0
 n=c['time_rows'];gamma=aa(m['baseline_gamma_lower'] if profile_gamma is None else profile_gamma);s=aa(m['sketch_norm_upper']);omega=aa(m['Omega_upper']);f=aa(pair(prep_fraction));pblock=f*gamma/(s*arb(37).sqrt())
 prep_total=f*gamma;offset_loss=aa(m['offset_multiplier_upper'])*aa(pair(offset_box)) if profile_gamma is None else arb(0);margin=gamma-offset_loss-prep_total
 out={'offset_box_sample_units':pair(offset_box),'preparation_fraction_of_gamma':pair(prep_fraction),'jitter_sample_units':pair(jitter),'absolute_preparation_rate_error':pair(rate),'raw_vector_error':pair(raw_delta),'known_profile_margin_used':profile_gamma is not None,'model_floor_included':model_floor,'physical_promotion':0,'scope':'Conditional exact estimator; per-preparation common-across-channels clocks, principal-band interpolation, per-preparation modal error blocks, not SI or general floating convergence','per_preparation_modal_error_bound':down(pblock),'total_coefficient_preparation_loss_upper':up(prep_total),'offset_coefficient_loss_upper':up(offset_loss)}
 if not margin>0:return {**out,'status':'HOLD_EXCITATION_MARGIN','unique_phase_matching':False}
 slope=(sum((aa(L)+omega*pblock)**2 for L in m['per_preparation_Lipschitz_upper'])).sqrt();clock=aa(pair(rate))*arb(n*(n-1)*(2*n-1)//6).sqrt()+aa(pair(jitter))*arb(n).sqrt();timing=s*slope*clock
 additive=aa(c['noise_transfer_squared']).sqrt()*aa(pair(raw_delta));e=timing+additive+(aa(c['reference_model_sketch_residual_upper']) if model_floor else arb(0));lower=(n*aa(c['frame_Gram_lower'])/2).sqrt()*margin
 return {**out,'coefficient_excitation_margin_lower':down(margin),'combined_preparation_slope_upper':up(slope),'timing_sketch_error_upper':up(timing),'additive_sketch_error_upper':up(additive),**exact_phase(c,lower,e)}
