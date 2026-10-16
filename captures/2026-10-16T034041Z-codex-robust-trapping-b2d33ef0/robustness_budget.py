#!/usr/bin/env python3
"""RHT v0.1 exact sufficient budgets; no physical calibration implied."""
import argparse,json
from fractions import Fraction as F
from barrier_budget import budget
def robust_budget(a,N,epsilon,target=None,real_readout=False,A='0',K='0',G='0',D='0',gradient_variation='0'):
 base=budget(a,N,epsilon,target);a,N,epsilon=map(F,(a,N,epsilon));eta=F(base['chosen_target_eta'])
 if real_readout:eta=min(eta,epsilon/1680);base=budget(a,N,epsilon,str(eta))
 m=F(base['m']);J=F(base['J']);B=F(base['boundary_energy_barrier_B_eta']);nu=m*eta/16
 A,K,G,D,variation=map(F,(A,K,G,D,gradient_variation))
 if min(A,K,G,D,variation)<0:raise ValueError('All error bounds must be nonnegative')
 coeff=A*eta+N*((1+12*eta)*K+14*G+3*D)
 return {'theorem':'RHT v0.1; DERIVED CONDITIONAL under frozen action and stated error class','input_provenance':'Supplied mathematical upper bounds; zero defaults are illustrative assumptions, not measurements. For time variation A,K,G,D must bound the whole interval.','reported_limits_scope':'Reference limits are sufficient; guarantees require the stated conditions. Separate forcing-only limits do not combine automatically with Hamiltonian errors.','base_budget':base,'selected_target_eta':str(eta),'canonical_gradient_limit_nu_star':str(nu),'autonomous_potential_oscillation_limit':str(B/4),'maximum_minimizer_set_displacement_bound':str(eta/8),'time_integrated_gradient_rate_limit':str(nu),'coefficient_error_inputs':{'A_max_absolute_kinetic_error':str(A),'K_max_diamond_error_divided_by_rN':str(K),'G_max_relative_incidence_hopping_error':str(G),'D_half_range_of_scalar_site_detunings':str(D)},'coefficient_gradient_upper':str(coeff),'coefficient_budget_status':'WITHIN_SUFFICIENT_BUDGET' if coeff<=nu else 'OUTSIDE_SUFFICIENT_BUDGET','gradient_variation_input':str(variation),'time_budget_status':'WITHIN_SUFFICIENT_BUDGET' if coeff<=nu and variation<=nu else 'OUTSIDE_SUFFICIENT_BUDGET','forcing_only_cumulative_metric_displacement_limit':str(m*eta/(8*J)),'forcing_only_scope':'Separate nominal-H flow plus tangent external forcing, with no simultaneous V assumed; bound integral ||Y_t||_g by this value','readout':{'real_readout_target_cap_applied':bool(real_readout),'complex_loop_model_error_upper':str(21*eta),'real_instrument_error_per_channel_allowed':str(epsilon/80) if real_readout else None,'real_total_error_per_channel_upper':str(epsilon/40) if real_readout else None,'oriented_phase_model_error_L2_upper':str(180*eta),'oriented_instrument_phase_L2_allowed':'(5/2)*sqrt(epsilon)','class_scope':'Real channels identify one of three family classes; oriented phases identify the inherited 26 labels; physical readout map remains unprovided'},'limits':['Exact equal norms and gauge/species-phase invariant Hamiltonian errors','Time-dependent conclusion lasts only while cumulative variation budget holds','No unique displaced stationary orbit or retained branch degeneracy claimed','Outside a sufficient budget is not proof of instability','No physical units or empirical result'],'physical_promotion':0,'independent_review':'PENDING'}
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for n in ['a','N','epsilon']:p.add_argument('--'+n,required=True)
 p.add_argument('--target');p.add_argument('--real-readout',action='store_true')
 for n in ['A','K','G','D','gradient-variation']:p.add_argument('--'+n,default='0')
 args=p.parse_args()
 try:print(json.dumps(robust_budget(args.a,args.N,args.epsilon,args.target,args.real_readout,args.A,args.K,args.G,args.D,args.gradient_variation),indent=2))
 except ValueError as e:p.error(str(e))
