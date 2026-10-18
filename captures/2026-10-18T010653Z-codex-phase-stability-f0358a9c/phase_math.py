"""Conditional exact-arithmetic shift-subspace phase perturbation bound."""
from fractions import Fraction as F
from flint import arb,fmpq
from proof_math import up,down

def aa(pair):return arb(fmpq(*pair))
def bound(delta,constants):
 delta=F(delta);assert delta>=0
 c=constants
 a=aa(c['frame_Gram_lower']);b=aa(c['frame_Gram_upper']);n=c['time_rows'];q=c['temporal_order']
 assert a>0 and b>=a and n>q and arb(q)<n*a
 K=(b/a).sqrt();deleted=(1-arb(q)/(n*a)).sqrt()
 e0=aa(c['reference_model_sketch_residual_upper'])
 alpha=aa(c['baseline_sigma105_lower'])-e0
 transfer=aa(c['noise_transfer_squared']).sqrt()
 e=e0+transfer*arb(fmpq(delta.numerator,delta.denominator))
 out={'delta':[delta.numerator,delta.denominator],'scope':'Exact top105-SVD/least-squares shift estimator about the pinned fitted reference; not a certified floating implementation','physical_promotion':0}
 if not (alpha>2*e):return {**out,'status':'HOLD_SUBSPACE_BOUND','unique_phase_matching':False}
 sine=e/(alpha-e);d=(2-2*(1-sine*sine).sqrt()).sqrt()
 if not deleted>d:return {**out,'status':'HOLD_DELETED_ROW_BOUND','unique_phase_matching':False}
 radius=K*d*(1+K)/(deleted-d);unique=bool(2*radius<aa(c['minimum_chord_separation_lower']))
 phase=radius.asin() if radius<1 else None
 return {**out,'status':'CERTIFIED_UNIQUE_PHASE_MATCHING' if unique else 'ONE_SIDED_ENCLOSURE_ONLY','unique_phase_matching':unique,'model_sigma105_lower':down(alpha),'sketch_total_error_upper':up(e),'subspace_sine_upper':up(sine),'basis_distance_upper':up(d),'shift_eigenvalue_radius_upper':up(radius),'phase_error_radians_upper':up(phase) if phase is not None else None,'readable':{'radius_upper':float(radius.upper()),'phase_error_upper':float(phase.upper()) if phase is not None else None}}
