"""Source-derived sufficient quality budgets; no frozen output gate is replaced."""
import argparse,json
from fractions import Fraction as F
from flint import arb,fmpq
from common import P,freeze,a,up,down
def constants():
 freeze();u=json.loads((P/'inputs/PARENT_UNIFORM.json').read_text());o=json.loads((P/'inputs/PARENT_ORDER.json').read_text());gates=json.loads((P/'inputs/PR210_FREEZE.json').read_text())['gates'];w=json.loads((P/'inputs/WEIGHTS_CERTIFICATE.json').read_text());old=json.loads((P/'inputs/PARENT_NORMAL.json').read_text())['rows']
 normal=max((x['normal_residual_F_upper'] for x in old),key=lambda x:F(*x));eta=a(gates['full_left_orthogonality']);nu=a(normal);beta=a(u['deleted_two_rows_beta_lower']);sigma=a(u['comparison_shift_residual_upper']);M0=a(u['comparison_shift_norm_upper']);A=a(json.loads((P/'inputs/PUBLISHED_ALLOWANCE.json').read_text())['raw_shift_strict_upper_allowance_lower']);g=(1-eta).sqrt();h=(1+eta).sqrt()
 squared=A*A-(2*nu/(g*beta))**2;assert squared>0
 D=a(down((squared.sqrt()/h-sigma)/(1+M0)));assert 0<D<beta/2 and D*D<2
 sine=a(down(D*(1-D*D/4).sqrt()));raw=a(down(g*sine));assert raw>0
 # The raw ceiling is deliberately directed down. Its actual direct-bound evaluation is separately checked below.
 return {'u':u,'o':o,'weights':w,'gates':gates,'normal_pair':normal,'eta':eta,'nu':nu,'beta':beta,'sigma':sigma,'M0':M0,'allowance':A,'g':g,'h':h,'D':D,'sine':sine,'raw':raw}
def direct_bound(eta,nu,residual,c):
 assert 0<=eta<1 and nu>=0 and residual>=0
 sine=residual/(1-eta).sqrt()
 if not sine<1:return None
 distance=(2/(1+(1-sine*sine).sqrt())).sqrt()*sine
 if not distance<c['beta']:return None
 J=(1+eta).sqrt()*(c['sigma']+(1+c['M0'])*distance);amin=(1-eta).sqrt()*(c['beta']-distance);bound=(J*J+(nu/amin)**2).sqrt()
 return {'sine':sine,'distance':distance,'J':J,'amin':amin,'bound':bound}
def scalar_budget(c):
 u,o,w=c['u'],c['o'],c['weights'];r=a(u['baseline_low_rank_residual_upper']);alpha=a(o['qth_sigma_lower'])-r;eta0=a(w['source_Gram_defect_F_upper']);rho=a(w['right_inverse_residual_F_upper']);M=(1+eta0).sqrt()*a(w['source_coefficient_F_upper']);t=r+a(u['per_vector_noise_multiplier_upper'])/arb(1<<48)
 w0=(a(w['baseline_weighted_F_upper'])+a(w['weighted_noise_multiplier_upper'])/arb(1<<48))/((1-rho)*(1-eta0).sqrt());polar=c['eta']/(1+(1-c['eta']).sqrt());x=c['D']-2*polar;assert x>0
 Aq=(1+x)**2/(alpha*alpha);Bq=1/alpha+2*Aq*t+M*x*(2+x)/(alpha*alpha);Cq=w0+Aq*t*t+M*x*(2+x)*t/(alpha*alpha)-x;assert Cq<0
 root=-2*Cq/(Bq+(Bq*Bq-4*Aq*Cq).sqrt());lo=a(down(root));hi=a(up(root))
 # A single fixed graph radius certifies every epsilon<=lo by monotonicity.
 def gate(eps):
  e=t+eps;z=w0+eps/alpha+e*e/(alpha*alpha);ac=(2*M*e+2*e*e)/(alpha*alpha);bc=e*(M+e)/(alpha*alpha)
  return z+ac*x+bc*x*x,ac+2*bc*x,alpha-2*e,((alpha-e)**2-2*e*(M+e)*x)/(1+x*x)-e*e
 low=gate(lo);high=gate(hi);assert low[0]<x and high[0]>x and high[1]<1 and high[2]>0 and high[3]>0
 return {'epsilon_sufficient_lower':down(lo),'selfmap_contour_upper':up(hi),'common_graph_radius':down(x),'strict_selfmap_at_lower':True,'contraction_separation_leading_at_upper':True,'scope':'Sufficient Frobenius-helper quality envelope over the original encoded ball with stated Gram/normal caps. Upper endpoint only bounds this proof contour; exceeding it is not an actual estimator failure.','readable_epsilon_sufficient':float(lo.lower())}
def verify():
 c=constants();s=scalar_budget(c);rows=[];d=json.loads((P/'DIRECT_METRICS.json').read_text())['rows'];eta_cap=c['gates']['full_left_orthogonality']
 for row in d:
  eta=a(row['retained_Gram_defect_F_upper']);nu=a(row['normal_F_upper']);residual=a(row['alignment_residual_F_upper']);b=direct_bound(eta,nu,residual,c);assert b is not None
  caps=bool(eta<=c['eta'] and nu<=c['nu']);within=bool(residual<c['raw']);bound_pass=bool(b['bound']<c['allowance']);assert a(row['actual_raw_shift_squared']).sqrt()<=b['bound']
  scalar_pass=bool(a(row['full_SVD_F_error_upper'])<a(s['epsilon_sufficient_lower']))
  rows.append({'case':row['case'],'record_sha256':row['record_sha256'],'status':'CERTIFIED_ACTUAL_SOURCE_FRAME_SHIFT_BUDGET' if caps and within and bound_pass else 'HOLD_SOURCE_FRAME_BUDGET','same_output_caps_verified':caps,'source_frame_budget_satisfied':within,'source_bound_strict_shift_allowance_satisfied':bound_pass,'generic_scalar_F_route_sufficient':scalar_pass,'normalized_sine_F_upper':up(b['sine']),'aligned_basis_distance_F_upper':up(b['distance']),'exact_LS_source_bound_upper':up(b['J']),'deleted_sigma_lower':down(b['amin']),'actual_returned_shift_source_bound_upper':up(b['bound']),'alignment_residual_to_budget_ratio_upper':up(residual/c['raw']),'readable':{'alignment_residual_F_upper':float(residual.upper()),'raw_frame_budget_lower':float(c['raw'].lower()),'direct_returned_shift_upper':float(b['bound'].upper()),'full_SVD_F_error_upper':float(a(row['full_SVD_F_error_upper']).upper()),'scalar_F_budget_lower':s['readable_epsilon_sufficient']},'physical_promotion':0})
 at_ceiling=direct_bound(c['eta'],c['nu'],c['raw'],c);assert at_ceiling and at_ceiling['bound']<c['allowance']
 return {'status':'CERTIFIED_SOURCE_DERIVED_BUDGET_AND_MEASURED_FLOATING_OUTPUTS','source_budget':{'retained_Gram_cap':eta_cap,'normal_cap':c['normal_pair'],'normal_cap_scope':'Maximum verified upper over the three named archived outputs; no future solver guarantee','allowed_aligned_distance_lower':down(c['D']),'allowed_sine_F_lower':down(c['sine']),'allowed_raw_frame_residual_lower':down(c['raw']),'returned_shift_bound_at_raw_ceiling_upper':up(at_ceiling['bound']),'allowance_lower':up(c['allowance']),'readable_raw_frame_budget_lower':float(c['raw'].lower())},'scalar_F_budget':s,'rows':rows,'scope':'Direct source-frame displacement includes admitted input noise and numerical error. These three measured outputs only; no library-wide forward-error bound or new raw eligibility/all-other-gates execution.','old_gates_radius_and_phase_target_changed':False,'external_review':'PENDING','physical_promotion':0}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');args=p.parse_args();r=verify();q=P/'BUDGET_CERTIFICATE.json'
 if args.replay:assert json.loads(q.read_text())==r
 else:assert not q.exists();q.write_text(json.dumps(r,indent=2))
 print(json.dumps({'status':r['status'],'budget':r['source_budget'],'scalar_F_budget':r['scalar_F_budget'],'rows':[{'case':x['case'],'status':x['status'],'scalar_sufficient':x['generic_scalar_F_route_sufficient'],'readable':x['readable']} for x in r['rows']]}),flush=True)
