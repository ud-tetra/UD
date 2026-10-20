#!/usr/bin/env python3
"""Exact adversarial controls and an explicitly conditional dyadic budget."""
from fractions import Fraction as F
from pathlib import Path
import json
P=Path(__file__).resolve().parent;M=4096;C=F(27648,61)
# No state-amplitude factor: R=1,E=1/10,x=100 gives error10, not1/10.
rho=F(1,10);X=100;assert rho*X==10>rho
# No preparation/mismatch mixed term: x=0,p=1,E=1 =>actualerror2>p.
assert 1+1>1
# Omitting xi*eta: K=4J,Delta=2J,theta1/100, t0=0.
# Output sin(6/100)>5/100 by its degree3 Taylor lower bound.
z=F(6,100);assert z-z**3/6>F(5,100)
# Coherent noise and codec errors need not add by RSS.
assert F(2)**2>1+1
T2=F((M-1)*(2*M-1),24);mu=F(M-1,4);v=F(M*M-1,48);assert T2==mu**2+v
for offset,drift in [(F(1,8),F(1,32)),(F(-1,8),F(1,32)),(F(0),F(1,2**40))]:
 raw=offset**2+2*offset*drift*mu+drift**2*T2
 centered=(offset+drift*mu)**2+drift**2*v
 assert raw==centered
assert T2>1 # relative drift must be multiplied by grid time RMS.
# An arbitrarily small hidden/visible skew coupling has nonzero response.
# For eps=2^-k at h1/2, sin(eps*h)>=z-z^3/6>0, k>=1.
for k in [1,20,40,100]:
 z=F(1,2**(k+1));assert z-z**3/6>0
# Perfect conditioning F=1 does not imply B=0 reconstructs x=1.
assert abs(0*1-1)==1
# Illustrative mathematical assumptions only: none measured/certified here.
u=F(1,2**53);xi=F(1,2**64);eta=u;rho=u;p=u;X=F(1);nu_noise=u;enc=u
b=rho+2048*xi+(5+xi)*eta
delta=p+(X+p)*b+nu_noise+enc
ideal=C*delta
alpha=F(1,2**43);beta=F(512);alg=F(1,2**43)
approx=alpha*X+beta*delta+alg;gate=F(1,2**39)
assert ideal<gate and approx<gate
# A stable nominal quotient lower does not force unchanged complete kernel.
# In a two-plane model with nominal K0,R=[1,0], the two-sample determinant
# is nonzero after arbitrary epsilon coupling, so rank rises1to2.
r={'status':'PASS_EXACT_ERROR_BOUND_CONTROLS_AND_CONDITIONAL_EXAMPLE','adversarial_controls':{'state_amplitude_required':True,'preparation_mismatch_mixed_term_required':True,'generator_timing_mixed_term_required':True,'coherent_sources_cannot_be_combined_by_unjustified_RSS':True,'relative_drift_requires_grid_time_scale':True,'arbitrarily_weak_skew_coupling_can_expose_old_hidden_line':True,'conditioning_does_not_certify_actual_estimator':True},'grid_moments':{'mean':str(mu),'second_moment':str(T2),'variance':str(v)},'conditional_dyadic_example':{'status':'ILLUSTRATIVE_ASSUMPTIONS_ONLY_NO_MEASURED_OR_IMPLEMENTATION_CERTIFICATE','X':str(X),'p':str(p),'rho_rms':str(rho),'xi':str(xi),'eta_rms':str(eta),'noise_rms':str(nu_noise),'codec_rms':str(enc),'T_rms_conservative_upper':'2048','b_upper':str(b),'observation_error_upper':str(delta),'ideal_reconstruction_error_upper':str(ideal),'alpha':str(alpha),'beta':str(beta),'eps_alg':str(alg),'approximate_estimator_error_upper':str(approx),'comparison_gate':str(gate),'ideal_strict_gate':True,'approximate_estimator_strict_gate':True},'scope':{'conditional_example_not_new_protocol_caps':True,'no_actual_floating_estimator_or_acquisition_validation':True,'same_team_development_no_registry_entry':True,'external_review':'PENDING','physical_promotion':0}}
(P/'CONTROLS_AND_EXAMPLE.json').write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':r['status'],'ideal_error_float_for_display':float(ideal),'approx_error_float_for_display':float(approx),'gate':float(gate)}))
