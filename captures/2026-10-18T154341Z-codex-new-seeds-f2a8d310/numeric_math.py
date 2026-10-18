"""Exact dyadic encoding and residual-to-phase certificate for floating outputs."""
from fractions import Fraction as F
import numpy as np
from flint import arb,acb,fmpq
from proof_math import fm,arr,up,down

def encode(a):
 a=np.asarray(a);assert a.dtype==np.float64 and np.all(np.isfinite(a))
 ratios=[float(x).as_integer_ratio() for x in a.flat]
 bits=max(d.bit_length()-1 for _,d in ratios)
 nums=np.array([n<<(bits-(d.bit_length()-1)) for n,d in ratios],dtype=object).reshape(a.shape)
 return nums,bits

def encode_complex(a):
 a=np.asarray(a);r,br=encode(a.real.astype(np.float64));i,bi=encode(a.imag.astype(np.float64));b=max(br,bi)
 return r*(1<<(b-br)),i*(1<<(b-bi)),b

def norm2_receipt(nums,bits):
 sq=F(sum(int(x)**2 for x in np.asarray(nums).flat),1<<(2*bits))
 return arb(sq.numerator).sqrt()/arb(sq.denominator).sqrt(),[sq.numerator,sq.denominator]

def diffnorm(a,ba,b,bb):
 k=max(ba,bb);return norm2_receipt(arr(a*(1<<(k-ba))-b*(1<<(k-bb))),k)

def cmul(ar,ai,br,bi):return ar*br-ai*bi,ar*bi+ai*br

def complex_residual(a,ba,b,bb):
 k=max(ba,bb);r=arr(a[0]*(1<<(k-ba))-b[0]*(1<<(k-bb)));i=arr(a[1]*(1<<(k-ba))-b[1]*(1<<(k-bb)))
 return norm2_receipt(np.r_[r.flat[:],i.flat[:]],k)

def aa(p):return arb(fmpq(*p))

def assemble(metrics,constants):
 eta=aa(metrics['basis_orthogonality_upper']);assert eta<1,'HOLD: basis rank/polar correction'
 du=eta/(1+(1-eta).sqrt())
 tau=aa(metrics['projection_residual_upper'])+du*aa(metrics['reduction_norm_upper'])
 e=aa(metrics['reference_model_residual_upper']);alpha=aa(constants['baseline_sigma105_lower'])-aa(constants['reference_model_sketch_residual_upper'])
 sine=(e+tau)/alpha;assert sine<1,'HOLD: reference subspace distance'
 distance=(2-2*(1-sine*sine).sqrt()).sqrt()+du
 a=aa(constants['frame_Gram_lower']);b=aa(constants['frame_Gram_upper']);K=(b/a).sqrt();beta=(1-arb(105)/(8191*a)).sqrt()
 assert distance<beta,'HOLD: deleted-row rank'
 shift=(aa(metrics['shift_residual_upper'])+distance*(1+K))/(beta-distance)
 rho=aa(metrics['inverse_residual_upper']);assert rho<1,'HOLD: eigenvector inverse'
 inv=aa(metrics['inverse_norm_upper'])/(1-rho)
 eig=aa(metrics['eigenpair_residual_upper'])*inv
 radius=K*(shift+eig)
 assert radius<1,'HOLD: eigenvalue disk crosses origin'
 unique=bool(2*radius<aa(constants['minimum_chord_separation_lower']))
 angle=radius.asin()+aa(metrics['argument_output_error_upper'])
 assert 2*angle<aa(constants['minimum_chord_separation_lower']),'HOLD: emitted phase rounding/matching'
 assert unique,'HOLD: phase disks not disjoint'
 return {'status':'CERTIFIED_FLOATING_ESTIMATOR_PHASE_MATCHING','basis_polar_distance_upper':up(du),'projected_sketch_residual_upper':up(tau),'reference_subspace_sine_upper':up(sine),'aligned_basis_distance_upper':up(distance),'shift_operator_distance_upper':up(shift),'eigenvector_inverse_norm_upper':up(inv),'eigenvalue_backward_error_upper':up(eig),'returned_eigenvalue_radius_upper':up(radius),'emitted_phase_error_radians_upper':up(angle),'unique_reference_phase_matching':True,'computed_sketch_order_certified':bool(alpha-e>aa(constants['discovery_cutoff']) and e<aa(constants['discovery_cutoff'])),'physical_promotion':0,'scope':'Per-record captured floating outputs about the pinned fitted reference, not global convergence or physical frequency identification','readable':{'eigenvalue_radius_upper':float(radius.upper()),'emitted_phase_error_radians_upper':float(angle.upper())}}
