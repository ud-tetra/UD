"""Amplitude-independent reference-frame to captured-basis phase certificate."""
from flint import arb
from proof_math import up,down,fm,arr
from numeric_math import aa,encode
from operator_bounds import gram_norm

def span_residual(pp,U,D):
 un,bu=encode(U);dn,bd=encode(D);bits=max(60,bu+bd)
 residual=arr(fm(pp)*(1<<(bits-60))-(fm(un)*fm(dn))*(1<<(bits-bu-bd)))
 norm,receipt=gram_norm(residual,bits)
 phase=arb(pp.shape[0]*(pp.shape[1]-1)).sqrt()/(1<<60)
 return norm+phase,{'dyadic_residual_Gram':receipt,'reference_phase_approximation_upper':up(phase),'exact_binary_scale_bits':{'basis':bu,'frame_reduction':bd}}

def assemble_span(m,c):
 n=c['time_rows'];q=c['temporal_order'];a=aa(c['frame_Gram_lower']);b=aa(c['frame_Gram_upper'])
 assert a>0 and b>=a,'HOLD: reference frame constants'
 eta=aa(m['basis_orthogonality_upper']);assert eta<1,'HOLD: basis rank/polar correction'
 du=eta/(1+(1-eta).sqrt());lower=(n*a/2).sqrt()
 sine=aa(m['frame_span_residual_upper'])/lower;assert sine<1,'HOLD: reference frame span'
 distance=(2-2*(1-sine*sine).sqrt()).sqrt()+du
 K=(b/a).sqrt();beta=(1-arb(q)/(n*a)).sqrt();assert distance<beta,'HOLD: deleted-row rank'
 shift=(aa(m['shift_residual_upper'])+distance*(1+K))/(beta-distance)
 rho=aa(m['inverse_residual_upper']);assert rho<1,'HOLD: eigenvector inverse'
 inv=aa(m['inverse_norm_upper'])/(1-rho);eig=aa(m['eigenpair_residual_upper'])*inv;radius=K*(shift+eig)
 assert radius<1,'HOLD: eigenvalue disk crosses origin'
 unique=bool(2*radius<aa(c['minimum_chord_separation_lower']))
 angle=radius.asin()+aa(m['argument_output_error_upper'])
 assert unique and 2*angle<aa(c['minimum_chord_separation_lower']),'HOLD: emitted phase rounding/matching'
 return {'status':'CERTIFIED_FRAME_SPAN_PHASE_MATCHING','basis_polar_distance_upper':up(du),'reference_real_frame_sigma_lower':down(lower),'reference_subspace_sine_upper':up(sine),'aligned_basis_distance_upper':up(distance),'shift_operator_distance_upper':up(shift),'eigenvector_inverse_norm_upper':up(inv),'eigenvalue_backward_error_upper':up(eig),'returned_eigenvalue_radius_upper':up(radius),'emitted_phase_error_radians_upper':up(angle),'unique_reference_phase_matching':True,'physical_promotion':0,'scope':'Captured floating outputs about fixed fitted-reference phases; amplitude-independent span proof, not physical phases or a uniform error-ball guarantee','readable':{'eigenvalue_radius_upper':float(radius.upper()),'emitted_phase_error_radians_upper':float(angle.upper())}}
