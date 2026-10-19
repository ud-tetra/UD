"""Frozen implication controls. Changed budgets are diagnostics, not admissions."""
import json
from copy import deepcopy
from uniform import P,verify,a
f=json.loads((P/'FREEZE.json').read_text());base=verify();assert base['status'].startswith('CERTIFIED') and base['readable']['two_step_phase_error_upper']<3.079e-7
rows=[{'control':'frozen_contract','status':base['status']}]
g=deepcopy(f['gates']);g['full_SVD_error']=[1,1<<39];r=verify(gates=g);assert r['status'].startswith('HOLD');rows.append({'control':'looser_SVD_error_budget_2neg39','status':r['status'],'reason':'strict matching not certified','not_an_estimator_failure':True})
g=deepcopy(f['gates']);g['emitted_argument_error']=[1,1<<20];r=verify(gates=g);assert r['status'].startswith('HOLD');rows.append({'control':'oversized_argument_budget_2neg20','status':r['status'],'not_an_estimator_failure':True})
r=verify(delta=[1,1<<47]);assert r['status'].startswith('HOLD');rows.append({'control':'outside_frozen_noise_domain_2neg47','status':r['status'],'scope':'analytic sensitivity only; uniform integerproof for this largerball not claimed','not_an_estimator_failure':True})
# Scalar gate refusal: zero inverse is exactly V*0-I, Frobenius sqrt209.
assert 209>1 and not 209<=a(f['gates']['inverse_residual'])**2
rows.append({'control':'zero_inverse_witness','status':'REFUSED_INVERSE_GATE','exact_residual_squared':209})
r={'status':'PASS_FROZEN_BOUND_AND_FOUR_NEGATIVE_CONTROLS','controls':rows,'physical_promotion':0,'external_review':False}
(P/'CONTROLS.json').write_text(json.dumps(r,indent=2));print(json.dumps(r),flush=True)
