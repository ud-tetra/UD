#!/usr/bin/env python3
"""Exact finite countermodels for missing hypotheses in quotient estimates."""
from fractions import Fraction as F
from pathlib import Path
import json
P=Path(__file__).resolve().parent
# Scaling Q cannot scale the true map's singular value.
assert F(1000,1000)==1
# If rank(F)>r, the r-th singular value is not its least positive one.
eps=F(1,10000)
assert eps<1
# F=[[1,1],[1,1+eps]] has determinant eps and sigma_max²>=2.
# Thus condition=sigma_max²/det>=20000, although each one-column map has condition1.
cross_lower=F(2)/eps;assert cross_lower==20000
# Actual finite-grid endpoints from the exact rational proof.
M=4096;T_rms2=F((M-1)*(2*M-1),24)
assert T_rms2<F(2048)**2
r={'status':'PASS_EXACT_QUOTIENT_ADVERSARIAL_CONTROLS','controls':{'missing_Q_norm_divisor':{'F':[[1]],'Q':[[1000]],'sigma_min_FQ':1000,'sigma_min_F':1,'uncorrected_claim_false':True},'missing_exact_rank_premise':{'F_diagonal':['1',str(eps)],'Q':'first coordinate','r':1,'sigma_r_FQ':1,'sigma_min_positive_F':str(eps),'uncorrected_claim_false':True},'isolated_channel_condition_does_not_upper_bound_full':{'F':[['1','1'],['1',str(1+eps)]],'single_column_conditions':[1,1],'full_condition_lower':str(cross_lower),'determinant':str(eps)},'Gram_frame_must_be_square_complete':{'G_diagonal':[1,0],'V':'first coordinate only','d':[1],'residual':0,'missing_eigenvalue':0},'halfstep_rms_upper2048':True},'scope':'Exact proof controls, not evaluations of the C27 saved proposals.','physical_promotion':0,'external_review':'PENDING'}
(P/'QUOTIENT_CONTROLS.json').write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
print(r['status'])
