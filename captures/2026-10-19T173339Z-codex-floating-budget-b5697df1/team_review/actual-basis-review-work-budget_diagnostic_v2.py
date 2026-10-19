"""Independent stdlib Decimal expression check, not new enclosure authority.

140-digit Decimal square roots, monotone bisection of the scalar contour, and
factorized equations differ from the parent Arb quadratic evaluation.
"""
import json,hashlib
from pathlib import Path
from decimal import Decimal as D,localcontext,ROUND_FLOOR
from fractions import Fraction

HERE=Path(__file__).resolve().parent
P=HERE.parent/'floating-budget-work'
load=lambda p:json.loads(Path(p).read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()

def run():
 fr=load(HERE/'DIAGNOSTIC_V2_FREEZE.json')
 for p,h in fr['files'].items():assert sha(HERE.parent/p)==h,p
 pair=lambda p:D(int(p[0]))/D(int(p[1]))
 with localcontext() as ctx:
  ctx.prec=140
  scale=D(2)**180
  dyadfloor=lambda x:int((x*scale).to_integral_value(rounding=ROUND_FLOOR))
  u=load(P/'inputs/PARENT_UNIFORM.json');o=load(P/'inputs/PARENT_ORDER.json');w=load(P/'inputs/WEIGHTS_CERTIFICATE.json');old=load(P/'inputs/PARENT_NORMAL.json')['rows'];gate=load(P/'inputs/PR210_FREEZE.json')['gates'];published=load(P/'inputs/PUBLISHED_ALLOWANCE.json');cert=load(P/'BUDGET_CERTIFICATE.json');direct=load(P/'DIRECT_METRICS.json')
  eta=pair(gate['full_left_orthogonality']);nu=max(pair(x['normal_residual_F_upper']) for x in old);beta=pair(u['deleted_two_rows_beta_lower']);sig=pair(u['comparison_shift_residual_upper']);m=pair(u['comparison_shift_norm_upper']);allow=pair(published['raw_shift_strict_upper_allowance_lower']);g=(1-eta).sqrt();h=(1+eta).sqrt()
  distance_unrounded=((allow*allow-(2*nu/(g*beta))**2).sqrt()/h-sig)/(1+m)
  dist=D(dyadfloor(distance_unrounded))/scale
  sine=D(dyadfloor(dist*(1-dist*dist/4).sqrt()))/scale
  raw=D(dyadfloor(g*sine))/scale
  for k,v in [('allowed_aligned_distance_lower',dist),('allowed_sine_F_lower',sine),('allowed_raw_frame_residual_lower',raw)]:assert v==pair(cert['source_budget'][k]),k
  polar=eta/(1+(1-eta).sqrt());x=D(dyadfloor(dist-2*polar))/scale
  assert x==pair(cert['scalar_F_budget']['common_graph_radius_upper'])
  r=pair(u['baseline_low_rank_residual_upper']);alpha=pair(o['qth_sigma_lower'])-r;t=r+pair(u['per_vector_noise_multiplier_upper'])/D(2)**48;eta0=pair(w['source_Gram_defect_F_upper']);rho=pair(w['right_inverse_residual_F_upper']);M=(1+eta0).sqrt()*pair(w['source_coefficient_F_upper']);w0=(pair(w['baseline_weighted_F_upper'])+pair(w['weighted_noise_multiplier_upper'])/D(2)**48)/((1-rho)*(1-eta0).sqrt())
  # Factorized graph map; do not use the parent's Aq/Bq/Cq quadratic or root formula.
  def phi(ep):
   e=t+ep
   return w0+ep/alpha+((1+x)**2*e*e+M*x*(2+x)*e)/(alpha*alpha)
  left=D(0);right=D(2)**-40
  assert phi(left)<x<phi(right)
  for _ in range(400):
   mid=(left+right)/2
   if phi(mid)<x:left=mid
   else:right=mid
  assert dyadfloor(left)==dyadfloor(right)
  assert dyadfloor(left)==int(cert['scalar_F_budget']['epsilon_sufficient_lower'][0])
  ep_lo=pair(cert['scalar_F_budget']['epsilon_sufficient_lower']);ep_hi=pair(cert['scalar_F_budget']['selfmap_contour_upper'])
  assert phi(ep_lo)<x<phi(ep_hi)
  assert Fraction(*cert['scalar_F_budget']['selfmap_contour_upper'])-Fraction(*cert['scalar_F_budget']['epsilon_sufficient_lower'])==Fraction(1,2**180)
  e=t+ep_hi
  contraction=(2*M*e+2*e*e+2*e*(M+e)*x)/(alpha*alpha)
  leading=((alpha-e)**2-2*e*(M+e)*x)/(1+x*x)-e*e
  assert contraction<1 and alpha>2*e and leading>0
  rows=[]
  for dr,cr in zip(direct['rows'],cert['rows']):
   assert dr['case']==cr['case']
   et=pair(dr['retained_Gram_defect_F_upper']);normal=pair(dr['normal_F_upper']);resid=pair(dr['alignment_residual_F_upper']);s=resid/(1-et).sqrt();d=(2/(1+(1-s*s).sqrt())).sqrt()*s;j=(1+et).sqrt()*(sig+(1+m)*d);amin=(1-et).sqrt()*(beta-d);bound=(j*j+(normal/amin)**2).sqrt()
   assert bound<pair(cr['actual_returned_shift_source_bound_upper'])<allow
   assert bound>pair(cr['actual_returned_shift_source_bound_upper'])-D(2)**-180
   assert resid<raw
   rows.append({'case':dr['case'],'returned_bound_diagnostic':str(bound),'budget_pass':True,'scalar_route_pass':pair(dr['full_SVD_F_error_upper'])<ep_lo})
  result={'status':'PASS_INDEPENDENT_DECIMAL_EXPRESSION_DIAGNOSTIC','precision_digits':140,'scalar_contour_method':'400-step monotone bisection of factorized graph equation','distance_budget_exact_dyadic_match':True,'sine_budget_exact_dyadic_match':True,'raw_frame_budget_exact_dyadic_match':True,'fixed_graph_radius_exact_dyadic_match':True,'scalar_contour_exact_dyadic_bracket_match':True,'rows':rows,'scope':'Expression diagnostic only; authoritative enclosures remain frozen parent Arb certificates and exact integer checks. Same-team post-known-output work, no estimator execution.','external_review':'PENDING','physical_promotion':0}
  out=HERE/'BUDGET_DIAGNOSTIC.json';assert not out.exists();out.write_text(json.dumps(result,indent=2));print(json.dumps(result),flush=True)

if __name__=='__main__':run()
