#!/usr/bin/env python3
"""Independent Fraction check of the disclosed root conditional profile."""
from pathlib import Path
from fractions import Fraction as F
import json
P=Path(__file__).resolve().parent
pow2=lambda k:F(1,2**k)
X=F(1);p=pow2(52);xi=pow2(66);rho=pow2(53);eta=pow2(56);nu=enc=pow2(53)
b=rho+2048*xi+(5+xi)*eta
delta=p+(X+p)*b+nu+enc
alpha=pow2(42);beta=F(512);alg=pow2(42);err=alpha*X+beta*delta+alg
assert delta<pow2(50) and err<pow2(40)<pow2(39)
clock=pow2(58)+2048*pow2(70)+pow2(58)
assert clock==5*pow2(59)<pow2(56)
ideal=F(27648,61)*delta;assert ideal<pow2(40)
# Exact right inverse / forward-fit evidence does not establish decoder conformance.
Q=(F(3,5),F(4,5));assert sum(v*v for v in Q)==1
FQ=Q[0];B=tuple(v/FQ for v in Q);assert B==(F(1),F(4,3))
FB=B[0];BFQ=tuple(v*FQ for v in B)
assert FB==1 and BFQ==Q
alpha_defect=F(4,3);assert alpha_defect>1
result={'status':'PASS_ROOT_CONDITIONAL_PROFILE_AND_DECODER_COUNTERMODEL','profile':{'X':str(X),'p':str(p),'xi':str(xi),'rho_rms':str(rho),'eta_rms':str(eta),'nu':str(nu),'enc':str(enc),'T_rms_upper':'2048','b_upper':str(b),'observation_error_upper':str(delta),'observation_error_strict_below':'2^-50','ideal_error_upper':str(ideal),'alpha':str(alpha),'beta':str(beta),'eps_alg':str(alg),'approximate_estimator_error_upper':str(err),'approx_error_strict_below':'2^-40','observable_chain_target':'2^-39','target_is_not_six_ratio_parameter_contract':True},'optional_clock_profile':{'offset_upper':str(pow2(58)),'relative_drift_upper':str(pow2(70)),'jitter_RMS_upper':str(pow2(58)),'eta_RMS_upper':str(clock),'strict_below_profile_eta':True},'decoder_countermodel':{'F':[['1','0']],'P':[['1','0'],['0','0']],'Q':[str(v)for v in Q],'K_and_J':'zero','Q_unit':True,'equation_residual':0,'Gram':'9/25','naive_B':[str(v)for v in B],'F_B':'1','B_F_Q':[str(v)for v in BFQ],'full_operator_defect_norm':'4/3','spurious_hidden_output_for_x_e1':'4/3','forward_fit_and_right_inverse_do_not_certify_nominal_pseudoinverse':True},'scope':{'all_profile_inputs_are_conditional_not_measured':True,'no_actual_floating_estimator_or_acquisition_test':True,'no_new_protocol_caps':True,'external_review':'PENDING','physical_promotion':0}}
(P/'ROOT_PROFILE_CHECKS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':result['status'],'delta_float_display':float(delta),'ideal_error_float_display':float(ideal),'approx_error_float_display':float(err),'clock_float_display':float(clock)}))
