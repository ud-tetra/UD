"""Conditional feasibility bounds for the frozen native family, not a measured-run receipt."""
from pathlib import Path
from fractions import Fraction as F
import json
from spectral_certificate import a,bound,pair
ROOT=Path(__file__).resolve().parent
def build():
 p=json.loads((ROOT/'sources'/'PARENT_FREEZE_CERTIFICATE.json').read_text())
 c=json.loads((ROOT/'sources'/'FROZEN_CONTRACT.json').read_text());rule=c['spectral_rule']
 B=F(*rule['data_Hankel_operator_error_ceiling']);T=F(*rule['selection_threshold'])
 n=json.loads((ROOT/'sources'/'PARENT_NOISE_CERTIFICATE.json').read_text())['budgets']['restricted_pass_contract']
 u=F(*n['u0'])+F(1,2**20);v=F(*n['v']);M=4096
 beta2=37*(u*u+u*v*(M-1)+v*v*F(7*M*M-12*M+5,24))
 assert beta2==F(*p['Hankel_error_squared_from_parent']) and B*B>=beta2
 r=rule['target_count'];eta=F(1,2**40);zeta=B/4096;xi=F(1,2**41)
 s0=a(F(*p['nominal_min_squared_lower'])).sqrt();S0=a(F(*p['nominal_max_squared_upper'])).sqrt()
 sp=bound(s0-a(B+zeta),False);Sp=bound(S0+a(B),True)
 Emax=bound((a(r)*S0*S0).sqrt()+a(B),True)**2
 rho2=(B+zeta)**2+2*eta*Emax/(1-eta)
 L=((1-eta)*sp**2-xi)/(1+eta)
 U=((1+eta)*Sp**2+xi)/(1-eta)+rho2
 assert sp>0 and L>T*T and rho2<T*T and U<2029**2*L
 result={'status':'DERIVED_CONDITIONAL_NATIVE_FAMILY_PRECISION_CONTRACT','physical_promotion':0,
  'independent_review':'pending','protocol_sha256':p['protocol_sha256'],
  'hypotheses':{'parent_Frobenius_perturbation_upper':pair(B),
   'candidate_Gram_frobenius_defect_upper':pair(eta),
   'missed_nominal_subspace_energy_norm_upper':pair(zeta),
   'total_core_eigen_enclosure_slack_upper':pair(xi),
   'sufficient_verified_core_radius_upper':pair(xi/2)},
  'squared_retained_singular_lower':pair(L),'squared_tail_upper':pair(rho2),
  'squared_largest_singular_upper':pair(U),'condition_squared_upper':pair(U/L),
  'tail_below_frozen_threshold':True,'retained_above_frozen_threshold':True,'condition_below2029':True,
  'condition_upper_display_only':float(a(U/L).sqrt().mid()),
  'tail_over_threshold_display_only':float((a(rho2).sqrt()/a(T)).mid()),
  'scope':'Proves these sufficient candidate/core tolerances preserve the native1893-signal gate. Does not assert that a proposed basis or actual record meets them.',
  'units':'eta is candidate Gram error; zeta is missed nominal Hankel mass; xi is squared-singular-value core slack. None is a physical metric or Borel-shear tolerance.'}
 (ROOT/'NATIVE_PRECISION_CONTRACT.json').write_text(json.dumps(result,indent=2)+'\n')
 return result
if __name__=='__main__':
 d=build();print(json.dumps({k:d[k] for k in ['status','condition_upper_display_only','tail_over_threshold_display_only']}))
