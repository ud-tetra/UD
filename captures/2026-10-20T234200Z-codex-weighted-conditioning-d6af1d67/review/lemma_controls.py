#!/usr/bin/env python3
"""Small exact adversarial controls for the proof, not a physical/model certificate."""
from fractions import Fraction as F
from pathlib import Path
import json
P=Path(__file__).resolve().parent
# The full positive quotient of [0,1] has condition1. A nearly hidden
# vector's small normalized response does not give a positive singular upper.
hidden_mix_norm_sq=1000001
mix_response_sq=F(1,hidden_mix_norm_sq)
assert mix_response_sq<F(1,1000**2)
# Nonzero residual cannot be dropped even if the instantaneous C v is zero.
# B=[[0,1],[1,1]], H=[[1,1],[1,2]], C=[0,1], v=e1, lambda1.
# C v=0, C H v=1, so R exp(tK)v has nonzero third derivative1.
B=((0,1),(1,1));v=(1,0)
H=tuple(tuple(sum(B[k][i]*B[k][j]for k in range(2))for j in range(2))for i in range(2))
Cv=sum(B[0][i]*v[i]for i in range(2));Hv=tuple(sum(H[i][j]*v[j]for j in range(2))for i in range(2));CHv=sum(B[0][i]*Hv[i]for i in range(2))
assert Cv==0 and CHv==1
# Exact half-step second moment with a toy grid and the actual fixed grid.
for M in [1,2,3,7,4096]:
 direct=sum((F(j,2)**2 for j in range(M)),F(0))/M
 assert direct==F((M-1)*(2*M-1),24)
threshold=F(1,10*2029**2)
assert threshold==F(1,41168410)
r={'status':'PASS_EXACT_ADVERSARIAL_LEMMA_CONTROLS','checks':{'hidden_mass_countermodel':{'positive_quotient_condition':1,'mixed_trial_response_squared':str(mix_response_sq),'inference_without_Q_membership_invalid':True},'omitted_residual_countermodel':{'instantaneous_output':Cv,'third_output_derivative':CHv,'dropping_residual_invalid':True},'half_step_grid_moments_checked':[1,2,3,7,4096],'fixed_grid_second_moment':str(F(4095*8191,24)),'squared_response_strict_obstruction_threshold':str(threshold)},'scope':'Exact small proof controls, no candidate trajectory or numerical conditioning certificate.','physical_promotion':0,'external_review':'PENDING'}
(P/'LEMMA_CONTROLS.json').write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
print(json.dumps(r,indent=2))
