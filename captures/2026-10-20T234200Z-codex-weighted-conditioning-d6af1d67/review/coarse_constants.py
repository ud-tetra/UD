#!/usr/bin/env python3
"""Independent rational closure of proposed conservative whole-map bounds."""
from fractions import Fraction as F
from pathlib import Path
import json
P=Path(__file__).resolve().parent
q=lambda k:F(1,2**k)
eta=F(1,16);beta=q(22);zeta=q(44);dmin=9*q(20)
# Replace inverse sqrt(1-eta) by2; validate by exact squares.
assert 1-eta>F(1,4)
G_lower=dmin-2*beta-zeta
assert G_lower>q(17)
assert F(1,384)**2<q(17)
assert (F(9,8))**2>1+eta
T2=F(4095*8191,24);assert T2<2048**2
E=q(24);time_error=2048*E;assert time_error==q(13)
map_lower=(F(1,384)-time_error)/F(9,8)
assert map_lower==F(61,27648)>F(1,512)
assert map_lower-F(1,512)==F(7,27648)
assert 1999*17*q(60)<q(44)
# Frame conditioning and a left eigenvector are essential to the residual route.
# Non-square V=e1 for G=diag(1,0) gives d=1 and residual0, but lambda_min G=0.
r={'status':'PASS_EXACT_CONSERVATIVE_CONSTANT_CHAIN','assumptions_not_measurements':{'etaV_strict_upper':str(eta),'etaQ_strict_upper':str(eta),'Gram_midpoint_eigenproposal_residual_F_strict_upper':str(beta),'Gram_entry_error_upper':str(17*q(60)),'Gram_midpoint_operator_error_strict_upper':str(zeta),'proposal_min_diagonal_strict_lower':str(dmin),'equation_residual_F_strict_upper':str(E)},'consequences':{'Gram_lambda_min_strict_lower':str(G_lower),'sample_mode_sigma_min_strict_lower':'1/384','Q_norm_strict_upper':'9/8','time_rms_squared':str(T2),'propagator_error_strict_upper':str(time_error),'full_positive_sigma_strict_lower':str(map_lower),'full_positive_sigma_comparison':'strictly greater than1/512','positive_condition_upper':'strictly less than512 if all declared hypotheses pass','full_domain_condition':'INFINITE inherited kernel641'},'adversarial_scope':{'square_full_frame_required_for_all_Gram_eigenvalues':True,'caps_are_not_actual_evaluations':True,'rank1999_and_skew_model_inherited':True,'no_numeric_accuracy_or_physical_gate_transfer':True},'physical_promotion':0,'external_review':'PENDING'}
(P/'COARSE_CONSTANTS.json').write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':r['status'],'strict_map_lower':str(map_lower),'strict_kappa_upper':512}))
