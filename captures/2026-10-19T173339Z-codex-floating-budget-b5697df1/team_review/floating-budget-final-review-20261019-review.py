"""Independent expression replay of the small numerical source-frame budget."""
from pathlib import Path
from fractions import Fraction
import hashlib,json
from flint import arb,fmpq,ctx
ctx.prec=512
P=Path(__file__).resolve().parent
SRC=P.parent/'floating-budget-work'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def a(x): return arb(fmpq(int(x[0]),int(x[1])))
def dyad(x,upper=False):
 n=(x*(1<<180)).ceil().unique_fmpz() if upper else (x*(1<<180)).floor().unique_fmpz()
 assert n is not None
 return [int(n),1<<180]
f=json.loads((P/'REVIEW_FREEZE.json').read_text())
assert f['code_sha256']==sha(Path(__file__))
assert f['inputs_sha256']=={n:sha(SRC/n) for n in f['inputs_sha256']}
j=json.loads((SRC/'BUDGET_CERTIFICATE.json').read_text())
u=json.loads((SRC/'inputs/PARENT_UNIFORM.json').read_text())
order=json.loads((SRC/'inputs/PARENT_ORDER.json').read_text())
weights=json.loads((SRC/'inputs/WEIGHTS_CERTIFICATE.json').read_text())
normal=json.loads((SRC/'inputs/PARENT_NORMAL.json').read_text())['rows']
gates=json.loads((SRC/'inputs/PR210_FREEZE.json').read_text())['gates']
metrics=json.loads((SRC/'DIRECT_METRICS.json').read_text())['rows']
nu_pair=max((r['normal_residual_F_upper'] for r in normal),key=lambda x:Fraction(int(x[0]),int(x[1])))
nu=a(nu_pair);eta=a(gates['full_left_orthogonality'])
beta=a(u['deleted_two_rows_beta_lower']);sig=a(u['comparison_shift_residual_upper']);M0=a(u['comparison_shift_norm_upper'])
A=a(json.loads((SRC/'inputs/PUBLISHED_ALLOWANCE.json').read_text())['raw_shift_strict_upper_allowance_lower'])
g=(1-eta).sqrt();h=(1+eta).sqrt()
D=a(dyad(((A*A-(2*nu/(g*beta))**2).sqrt()/h-sig)/(1+M0)))
S=a(dyad(D*(1-D*D/4).sqrt()));raw=a(dyad(g*S))
assert dyad(raw)==j['source_budget']['allowed_raw_frame_residual_lower']
assert dyad(S)==j['source_budget']['allowed_sine_F_lower']

# Distances use a different equivalent expression from the production c(s)*s.
def direct(ee,nn,rr):
 s=rr/(1-ee).sqrt();dist=(2-2*(1-s*s).sqrt()).sqrt()
 J=(1+ee).sqrt()*(sig+(1+M0)*dist)
 amin=(1-ee).sqrt()*(beta-dist)
 out=(J*J+nn*nn/(amin*amin)).sqrt()
 return s,dist,J,amin,out

cases=[]
for m,r in zip(metrics,j['rows']):
 assert m['case']==r['case']
 ee=a(m['retained_Gram_defect_F_upper']);nn=a(m['normal_F_upper']);rr=a(m['alignment_residual_F_upper'])
 s,d,J,amin,out=direct(ee,nn,rr)
 assert ee<=eta and nn<=nu and rr<raw and out<A
 checks={
  'normalized_sine_F_upper':dyad(s,True),
  'aligned_basis_distance_F_upper':dyad(d,True),
  'exact_LS_source_bound_upper':dyad(J,True),
  'deleted_sigma_lower':dyad(amin),
  'actual_returned_shift_source_bound_upper':dyad(out,True),
 }
 assert all(r[k]==v for k,v in checks.items())
 assert a(m['actual_raw_shift_squared']).sqrt()<=out
 cases.append({'case':m['case'],'status':'PASS_IDENTICAL_INDEPENDENT_EXPRESSION','shift_upper':checks['actual_returned_shift_source_bound_upper']})

# Re-derive the fixed-radius scalar-F proof contour with the ordinary quadratic
# formula, and verify its polynomial signs rather than the expanded Riccati map.
r0=a(u['baseline_low_rank_residual_upper']);alpha=a(order['qth_sigma_lower'])-r0
eta0=a(weights['source_Gram_defect_F_upper']);rho=a(weights['right_inverse_residual_F_upper'])
M=(1+eta0).sqrt()*a(weights['source_coefficient_F_upper'])
t=r0+a(u['per_vector_noise_multiplier_upper'])/(1<<48)
w=(a(weights['baseline_weighted_F_upper'])+a(weights['weighted_noise_multiplier_upper'])/(1<<48))/((1-rho)*(1-eta0).sqrt())
x=a(dyad(D-2*eta/(1+(1-eta).sqrt())))
aa=(1+x)**2/alpha**2
bb=1/alpha+2*aa*t+M*x*(2+x)/alpha**2
cc=w+aa*t*t+M*x*(2+x)*t/alpha**2-x
root=((bb*bb-4*aa*cc).sqrt()-bb)/(2*aa)
lo=a(dyad(root));hi=a(dyad(root,True))
assert dyad(lo)==j['scalar_F_budget']['epsilon_sufficient_lower']
assert dyad(hi,True)==j['scalar_F_budget']['selfmap_contour_upper']
assert aa*lo*lo+bb*lo+cc<0 and aa*hi*hi+bb*hi+cc>0
e=t+hi
ac=(2*M*e+2*e*e)/alpha**2;bc=e*(M+e)/alpha**2
assert ac+2*bc*x<1 and alpha>2*e
assert (alpha*alpha-2*(alpha+M*x)*e-(2*x+x*x)*e*e)/(1+x*x)>0
assert all(a(m['full_SVD_F_error_upper'])>lo for m in metrics)

out={'status':'PASS_INDEPENDENT_EXPRESSION_SMALL_BUDGET_REPLAY','cases':cases,
 'source_budget_identical':True,'scalar_F_contour_identical':True,
 'generic_scalar_F_route_retains_HOLD_for_all_three':True,
 'no_large_matrix_or_basis_residual_replay_claimed':True,
 'no_new_estimator_or_all_other_gates_execution':True,
 'source_displacement_includes_input_noise_and_numerics':True,
 'same_team_review_not_external_independent_review':True,
 'input_sha256':f['inputs_sha256'],'physical_promotion':0}
(P/'REVIEW_CERTIFICATE.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
