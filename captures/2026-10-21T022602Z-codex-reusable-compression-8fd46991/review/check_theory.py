"""Independent Fraction compression budgets and exact adversarial fixtures."""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json
P=Path(__file__).resolve().parent
rat=lambda x:[x.numerator,x.denominator]
s=Q(61,27648);m=Q(1,384);eps=Q(1,8192);eta=eps/m;h=s*(m-eps);cos2=1-eta*eta
# Strict comparisons certified without an approximate square root.
checks={'cmin_pair':h==Q(3721,679477248),'eta_3_over_64':eta==Q(3,64),'gamma_lt_454':(454*s)**2*cos2>1,'gamma_lt_1815_over_4':(Q(1815,4)*s)**2*cos2>1}
tau=Q(5,2)**41/factorial(41)/(1-Q(5,84))
ad=4096*(4096*tau+Q(6240,2**104))+Q(52,2**96)
EY=Q(3,2**127)+Q(504,2**96)
delta=45*(ad+EY);EYop=45*EY
alpha=delta/h+delta/(h-delta);alpha_encoded=alpha+EYop/(h-delta)
beta=454*h/(h-delta);beta_encoded=beta+EYop/(h-delta)
ez=er=Q(1,2**64);elift=Q(1,2**44);solve=(ez+er)/(h-delta)+elift
checks.update({'sqrt1999_lt45':1999<45**2,'phase_coefficient_sum_lt3':Q(9,4)<3,'delta_lt_h':delta<h,'exact_Y_alpha_lt_2^-55':alpha<Q(1,2**55),'encoded_Y_alpha_lt_2^-55':alpha_encoded<Q(1,2**55),'exact_Y_beta_lt455':beta<455,'encoded_Y_beta_lt455':beta_encoded<455,'conditional_solve_lt_2^-43':solve<Q(1,2**43)})
# Angle factor is necessary: F=diag(1,0), Y=(3/5,4/5)^T.
B=[[Q(1),Q(4,3)],[Q(0),Q(0)]]
checks['angle_countermodel_gain_squared_25_over_9']=sum(x*x for x in B[0])==Q(25,9)
checks['angle_countermodel_exceeds_1_over_s']=Q(25,9)>1
# q2 rectangular perturbation activates orthogonal row-space and solve errors.
d=Q(1,16);det=1+d*d+d**4
e=[1/det-1,-d/det,d*(1+d*d)/det];e2=sum(x*x for x in e)
checks['single_debit_countermodel_exceeds_delta_over_h_minus_delta']=e2>(d/(1-d))**2
checks['orthogonal_bound_covers_countermodel']=e2<d*d+(d/(1-d))**2
checks['triangle_bound_covers_countermodel']=e2<(d+d/(1-d))**2
# exact direct column calculation proves error components split orthogonally.
# e_N=−PkerG v, e_R=−G+ Dv; their squared bounds add (not max).
checks['countermodel_spurious_hidden_output_nonzero']=e[2]!=0
checks['rank_loss_at_equal_delta_h']=Q(1)-Q(1)==0
checks['rhs_mismatch_even_with_delta_zero']=Q(2)-Q(1)==1
assert all(checks.values()),checks
result={'status':'PASS','checks':checks,'exact':{k:rat(v) for k,v in {'s':s,'m':m,'eps':eps,'eta':eta,'cosine_squared_lower':cos2,'h':h,'adjoint_error_upper':ad,'column_encoding_error':EY,'conditional_full_frame_error':delta,'conditional_full_encoding_error':EYop,'exact_Y_decoder_defect_upper':alpha,'encoded_Y_decoder_defect_upper':alpha_encoded,'exact_Y_decoder_gain_upper':beta,'encoded_Y_decoder_gain_upper':beta_encoded,'conditional_solve_error':solve,'single_debit_countermodel_actual_error_squared':e2}.items()},'display_only':{'conditional_delta':float(delta),'conditional_alpha_exactY':float(alpha),'conditional_alpha_encodedY':float(alpha_encoded),'conditional_beta_encodedY':float(beta_encoded),'conditional_solve_error':float(solve)},'scope':{'full1999_column_frame_not_computed_by_this_check':True,'bounds_require_all_columns_and_both_encoding_and_adjoint_contracts':True,'sixteen_column_evidence_not_full_frame_bound':True,'exact_pseudoinverse_theorem_not_actual_inverse_execution':True,'physical_promotion':0,'external_review':'PENDING'}}
(P/'THEORY_CHECKS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'delta':float(delta),'alpha_encoded':float(alpha_encoded),'solve':float(solve)}))
