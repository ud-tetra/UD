"""Conditional exact-estimator timing/preparation budget; no floating-convergence claim."""
from fractions import Fraction as F
from flint import arb,fmpq
from proof_math import up,down

def aa(x):return arb(fmpq(*x))
def frac(x):return [x.numerator,x.denominator]
def budget(c,m,p_fraction,jitter,rate,raw_delta,model_floor=True):
 p_fraction=F(p_fraction);jitter=F(jitter);rate=F(rate);raw_delta=F(raw_delta)
 assert min(p_fraction,jitter,rate,raw_delta)>=0
 gamma=aa(m['coefficient_sigma_lower']);p=aa(frac(p_fraction))*gamma;n=c['time_rows'];q=c['temporal_order'];a=aa(c['frame_Gram_lower']);b=aa(c['frame_Gram_upper'])
 assert gamma>0 and a>0 and b>=a and n>q and arb(q)<n*a
 assert aa(m['coefficient_norm_upper'])>=0 and aa(m['Omega_upper'])>=0
 out={'preparation_fraction_of_certified_gamma':frac(p_fraction),'jitter_sample_units':frac(jitter),'absolute_clock_rate_error':frac(rate),'raw_vector_error':frac(raw_delta),'model_floor_included':model_floor,'physical_promotion':0,'scope':'Conditional exact top105 SVD/least-squares estimator, declared principal-band common-clock interpolation; not arbitrary floating output or SI calibration'}
 if not p<gamma:return {**out,'status':'HOLD_EXCITATION_MARGIN','unique_phase_matching':False}
 lower=(n*a/2).sqrt()*(gamma-p)
 # Integer sum of k^2 must be exact; n*(n-1)*(2n-1) is divisible by6.
 exact_sum=n*(n-1)*(2*n-1)//6;clock=aa(frac(rate))*arb(exact_sum).sqrt()+aa(frac(jitter))*arb(n).sqrt()
 timing=aa(m['Omega_upper'])*clock*(aa(m['coefficient_norm_upper'])+p)
 additive=aa(c['noise_transfer_squared']).sqrt()*aa(frac(raw_delta))
 e=timing+additive+(aa(c['reference_model_sketch_residual_upper']) if model_floor else arb(0))
 out.update(preparation_coefficient_error_upper=up(p),model_sigma105_lower=down(lower),clock_error_vector_norm_upper=up(clock),timing_sketch_error_upper=up(timing),additive_sketch_error_upper=up(additive),total_sketch_error_upper=up(e))
 if not lower>2*e:return {**out,'status':'HOLD_SUBSPACE_SEPARATION','unique_phase_matching':False}
 sine=e/(lower-e);d=(2-2*(1-sine*sine).sqrt()).sqrt();beta=(1-arb(q)/(n*a)).sqrt();K=(b/a).sqrt()
 if not d<beta:return {**out,'status':'HOLD_DELETED_ROW_RANK','unique_phase_matching':False}
 radius=K*d*(1+K)/(beta-d);unique=bool(radius<1 and 2*radius<aa(c['minimum_chord_separation_lower']));phase=radius.asin() if radius<1 else None
 return {**out,'status':'CERTIFIED_CONDITIONAL_EXACT_ESTIMATOR_MATCHING' if unique else 'ONE_SIDED_ENCLOSURE_ONLY','unique_phase_matching':unique,'subspace_sine_upper':up(sine),'basis_distance_upper':up(d),'eigenvalue_radius_upper':up(radius),'phase_error_radians_upper':up(phase) if phase is not None else None,'readable':{'model_sigma105_lower':float(lower.lower()),'total_sketch_error_upper':float(e.upper()),'phase_error_radians_upper':float(phase.upper()) if phase is not None else None}}
