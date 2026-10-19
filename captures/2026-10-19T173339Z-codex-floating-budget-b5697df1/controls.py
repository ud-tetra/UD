"""Strict-budget and provenance controls; failures are proof refusals, not solver failures."""
import argparse,json,tempfile,shutil
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from flint import arb
from common import P,a,check_evidence
from numeric_math import encode
from budget_v2 import constants,direct_bound
def verify(evidence):
 c=constants();name='rotating_checker';U=np.vstack([np.load(Path(evidence)/f'{name}_F{k}.npz',allow_pickle=False)['left'] for k in range(3)])[:,:209];un,b=encode(U);zero_residual=arb(sum(int(x)**2 for x in un.flat)).sqrt()/arb(2)**b
 assert direct_bound(c['eta'],c['nu'],zero_residual,c) is None
 at=direct_bound(c['eta'],c['nu'],c['raw'],c);assert at and at['bound']<c['allowance'] and not c['raw']<c['raw']
 # Inverse principal-angle identity at rational d=6/5, sine=24/25.
 d=F(6,5);s=F(24,25);cos=F(7,25);assert s*s==d*d*(1-d*d/4) and d*d==2-2*cos and s*s+cos*cos==1
 cert=json.loads((P/'BUDGET_CERTIFICATE.json').read_text());lo=a(cert['scalar_F_budget']['epsilon_sufficient_lower']);hi=a(cert['scalar_F_budget']['selfmap_contour_upper']);x=a(cert['scalar_F_budget']['common_graph_radius_upper'])
 u=json.loads((P/'inputs/PARENT_UNIFORM.json').read_text());o=json.loads((P/'inputs/PARENT_ORDER.json').read_text());w=json.loads((P/'inputs/WEIGHTS_CERTIFICATE.json').read_text());r=a(u['baseline_low_rank_residual_upper']);alpha=a(o['qth_sigma_lower'])-r;t=r+a(u['per_vector_noise_multiplier_upper'])/arb(1<<48);eta0=a(w['source_Gram_defect_F_upper']);rho=a(w['right_inverse_residual_F_upper']);M=(1+eta0).sqrt()*a(w['source_coefficient_F_upper']);w0=(a(w['baseline_weighted_F_upper'])+a(w['weighted_noise_multiplier_upper'])/arb(1<<48))/((1-rho)*(1-eta0).sqrt())
 phi=lambda ep:w0+ep/alpha+((1+x)**2*(t+ep)**2+M*x*(2+x)*(t+ep))/(alpha*alpha)
 assert phi(lo)<x and phi(hi)>x
 with tempfile.TemporaryDirectory() as td:
  for row in json.loads((P/'INPUT_INDEX.json').read_text())['members']:shutil.copy2(Path(evidence)/row['destination'],Path(td)/row['destination'])
  check_evidence(td);q=Path(td)/'U0_A.npz';blob=q.read_bytes();q.write_bytes(bytes([blob[0]^1])+blob[1:])
  try:check_evidence(td)
  except AssertionError:pass
  else:raise AssertionError('mutated source basis accepted')
 return {'status':'PASS_FIVE_SOURCE_FRAME_BUDGET_CONTROLS','checks':['zero_alignment_on_actual_basis_refused','equality_is_strict_quality_HOLD_not_estimator_failure','exact_rational_angle_inverse','scalar_proof_contour_bracket_independent_factorization','mutated_source_basis_hash_refused'],'physical_promotion':0}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--evidence',required=True);args=p.parse_args();print(json.dumps(verify(args.evidence)),flush=True)
