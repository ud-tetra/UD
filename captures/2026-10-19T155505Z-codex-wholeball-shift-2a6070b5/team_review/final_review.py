"""Read-only whole-ball/fixed-basis same-team review and independent-expression diagnostic."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json
import mpmath as mp
mp.mp.dps=160
P=Path(__file__).resolve().parent;W=P.parent/'wholeball-shift-work';E=P.parent/'prospective-v2-work'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
f=load(W/'FREEZE.json');checked={}
for group,base in [('code_sha256',W),('input_sha256',W/'inputs')]:
 for n,h in f[group].items():assert sha(base/n)==h;checked[str(base/n)]=h
assert sha(W/'THEOREMS.md')==f['theorems_sha256'];checked[str(W/'THEOREMS.md')]=f['theorems_sha256']
assert sha(P/'DESIGN_REVIEW.json')==f['design_review_sha256']
for n,h in f['evidence_indices_sha256'].items():
 assert sha(E/n)==h
 for row in load(E/n)['files']:
  path=E/row['path'];assert path.is_file() and path.stat().st_size==row['size_bytes'] and sha(path)==row['sha256']
q=lambda p:mp.mpf(p[0])/p[1]
u=load(W/'inputs/PARENT_UNIFORM.json');o=load(W/'inputs/PARENT_ORDER.json');g=load(W/'inputs/PR210_FREEZE.json')['gates'];allow=load(W/'inputs/PUBLISHED_ALLOWANCE.json')
assert F(*u['baseline_low_rank_residual_upper'])**2>=F(*u['baseline_exact_low_rank_residual_squared'])
r=q(u['baseline_low_rank_residual_upper']);C=q(u['per_vector_noise_multiplier_upper']);alpha=q(o['qth_sigma_lower'])-r;beta=q(u['deleted_two_rows_beta_lower']);sigma=q(u['comparison_shift_residual_upper']);M=q(u['comparison_shift_norm_upper'])
def diagnostic(mode,delta):
 eta=mp.mpf(0) if mode=='ideal' else q(g['full_left_orthogonality']);eps=mp.mpf(0) if mode=='ideal' else q(g['full_SVD_error'])
 e2=r+C*q(delta)+eps;ef=r+C*q(delta)+(mp.sqrt(209)*eps if mode=='returned_operator_only' else eps)
 assert alpha>2*e2 and 0<=eta<1
 t2=e2/(alpha-e2);tf=ef/(alpha-e2);fac=mp.sqrt(2/(1+mp.sqrt(1-t2*t2)));p=eta/(1+mp.sqrt(1-eta));d2=fac*t2+2*p;df=fac*tf+2*p
 amin=mp.sqrt(1-eta)*(beta-d2);J=mp.sqrt(1+eta)*(sigma+df*(1+M));assert amin>0
 return J,amin
apriori=load(W/'APRIORI_BOUNDS.json');diag=[]
for row in apriori['rows']:
 J,amin=diagnostic(row['mode'],row['encoded_radius']);nu=q(row['normal_residual_ceiling']);returned=mp.sqrt(J*J+(nu/amin)**2)
 assert J<=q(row['exact_LS_raw_shift_upper']) and returned<=q(row['returned_raw_shift_upper']) and amin>=q(row['deleted_basis_sigma_min_lower'])
 sufficient=returned<q(allow['raw_shift_strict_upper_allowance_lower']);assert sufficient==row['shift_bound_sufficient_for_published_allowance']
 diag.append({'mode':row['mode'],'delta':row['encoded_radius'],'normal_ceiling':row['normal_residual_ceiling'],'independent_J':mp.nstr(J,100),'independent_amin':mp.nstr(amin,100),'sufficient':bool(sufficient)})
normal=load(W/'NORMAL_CERTIFICATES.json');supp=load(E/'SUPPLEMENT_RESULTS.json');J,amin=diagnostic('returned_F_certificate',f['encoded_radius']);nr=[]
for row,sr in zip(normal['rows'],supp['rows']):
 assert row['case']==sr['case'];s2=F(*map(int,row['exact_shift_residual_squared']));n2=F(*map(int,row['exact_normal_residual_squared']))
 assert s2==F(*map(int,sr['exact_raw_shift_residual_squared']))
 ss=mp.mpf(s2.numerator)/s2.denominator;nn=mp.mpf(n2.numerator)/n2.denominator;s=mp.sqrt(ss);nu=mp.sqrt(nn);gap=nu/amin;lower=mp.sqrt(max(mp.mpf(0),ss-gap*gap))
 assert nu<=q(row['normal_residual_F_upper']) and gap<=q(row['LS_residual_component_gap_upper'])
 assert q(row['exact_LS_minimum_residual_lower'])<=lower and s<=q(row['exact_LS_minimum_residual_upper'])
 assert mp.sqrt(J*J+gap*gap)<=q(row['conditional_wholeball_returned_shift_upper'])
 assert (lower>q(g['raw_shift_residual']))==row['every_shift_on_this_saved_basis_violates_v1_gate']
 nr.append({'case':row['case'],'expanded_and_direct_residual_squared_agree':True,'independent_fixed_basis_lower':mp.nstr(lower,100),'normal_norm_exceeds_illustrative_2neg45_ceiling':bool(n2>F(1,1<<90)),'old_gate_obstruction':row['every_shift_on_this_saved_basis_violates_v1_gate']})
assert [x['old_gate_obstruction'] for x in nr]==[False,False,True]
controls=load(W/'CONTROLS.json');assert controls['status']=='PASS_FOUR_EXACT_AND_SOURCE_REFUSAL_CONTROLS' and len(controls['controls'])==4
for c in controls['controls'][:2]:assert F(c['residual_squared'])-F(c['normal_residual_squared'])/(F(c['sigma_min'])**2)==9
assert all(sha(Path(p))==h for p,h in checked.items())
out={'status':'PASS_SAME_TEAM_WHOLEBALL_CODE_NORM_AND_FIXED_BASIS_REVIEW','reviewed_at_utc':datetime.now(timezone.utc).isoformat(),'review_code_sha256':sha(__file__),'reviewed_sources_before_after_equal':checked,'source_only_arithmetic_diagnostics':diag,'saved_basis_diagnostics':nr,'diagnostic_precision_decimal_digits':mp.mp.dps,'arithmetic_authority':'Primary validated bounds remain512-bit Arb plus exactdyadic/rational receipts; mpmath160digit recomputation is an independent-expression diagnostic.','findings':['Genericop lane correctlyuses sqrt209epsilon; F lane justified by actual F-norm Gram/reconstruction certificate proof.','One common alignment, Frobenius baseline sigma and fullpositive deleted-row singularmargin retained.','Exactnormal numerator/denominator and expanded s_squared scaling are correct; s_squared agrees exactly with earlier directdifference proof.','Fixedbasis lower uses exact s_squared minus upper normalcomponent and positive lower singularmargin; no residualupper used aslower.','Allfull-radius apriori proofbounds exceed publishedallowance, so sufficiencyHOLD is reported without actualfailureclaim.','Directed-only fixedbasis oldgate obstruction is valid and does not negate its v2PASS or constrain other bases/algorithms.','Actual normalnorms exceed illustrative nu2^-45; no claim theymeetthatfrozenceiling shouldbe made.'],'material_issues':[],'report_hashes':{n:sha(W/n) for n in ['FREEZE.json','THEOREMS.md','APRIORI_BOUNDS.json','NORMAL_CERTIFICATES.json','CONTROLS.json']},'new_estimator_runs':0,'new_SVD_runs':0,'new_raw_generation':False,'exact_normal_matrix_reexecution_by_reviewer':False,'dependencies':['Clean composed proof replay remains separate from this read-only review.','Pinned fullfactor/source/encodedrecord certificate dependencies remain explicit.'],'external_independent_review':'PENDING','physical_promotion':0,'lane':'development — no registry entry'}
(P/'FINAL_REVIEW.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:out[k] for k in ['status','material_issues']}))
