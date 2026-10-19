"""Independent-expression same-team source-only numerical crosscheck (mpmath160digits)."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import mpmath as mp
mp.mp.dps=160
P=Path(__file__).resolve().parent;W=P.parent/'source-shift-work'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
f=json.loads((W/'FREEZE.json').read_text());checked={}
for group,root in [('code_sha256',W),('input_sha256',W/'inputs')]:
 for n,h in f[group].items():assert sha(root/n)==h;checked[str(root/n)]=h
assert sha(W/'THEOREMS.md')==f['derivation_sha256'];checked[str(W/'THEOREMS.md')]=f['derivation_sha256']
assert sha(P/'DESIGN_REVIEW.json')==f['design_review_sha256']
cert=json.loads((W/'SOURCE_ALLOWANCE.json').read_text());checked[str(W/'SOURCE_ALLOWANCE.json')]=sha(W/'SOURCE_ALLOWANCE.json')
rat=lambda p:mp.mpf(p[0])/p[1]
load=lambda n:json.loads((W/'inputs'/n).read_text())
policy=load('PR210_FREEZE.json');g=policy['gates'];u=load('PARENT_UNIFORM.json');m=load('PARENT_PHASE.json')['metrics'];o=load('PARENT_ORDER.json')
eta=rat(g['full_left_orthogonality']);eps=rat(g['full_SVD_error']);r=rat(u['baseline_low_rank_residual_upper']);C=rat(u['per_vector_noise_multiplier_upper']);delta=rat(policy['encoded_vector_noise']);s0=rat(o['qth_sigma_lower']);alpha=s0-r;e=r+C*delta+eps;t=e/(alpha-e)
# Stable algebraically equivalent Procrustes term, independent of original subtraction.
d=mp.sqrt(2)*t/mp.sqrt(1+mp.sqrt(1-t*t))+2*eta/(1+mp.sqrt(1-eta))
beta=rat(u['deleted_two_rows_beta_lower']);sig=rat(u['comparison_shift_residual_upper']);M=rat(u['comparison_shift_norm_upper']);eta0=rat(m['basis_orthogonality_upper']);rho=rat(g['inverse_residual']);gamma=mp.sqrt(1-eta)
hD=rat(m['source_inverse_norm_upper'])/(1-rat(m['source_inverse_residual_upper']));K=mp.sqrt((1+eta0)/(1-eta0))*hD*rat(m['source_reduction_norm_upper']);L=hD*rat(m['intertwining_residual_upper']);ka=mp.sqrt((1+eta)/(1-eta));E=rat(g['eigenpair_residual'])*rat(g['proposed_inverse_norm'])/(1-rho);sep=rat(m['minimum_target_chord_lower']);arg=rat(g['emitted_argument_error']);Rlim=mp.sin(sep/2-arg)
# Independently collect affine intercept and slope, then invert the affine equation.
slope=K/(gamma*(beta-d));intercept=L+K*((sig+d*(1+M))/(beta-d)+ka*E);allowance=(Rlim-intercept)/slope
assert alpha>2*e and beta>d and K>0 and 0<sep/2-arg<mp.pi/2 and 0<Rlim<sep/2 and allowance>0
assert rat(cert['raw_shift_strict_upper_allowance_lower'])<=allowance<=rat(cert['raw_shift_allowance_upper'])
assert abs(intercept+slope*allowance-Rlim)<mp.mpf('1e-150')
assert {k:v for k,v in g.items() if k!='raw_shift_residual'}==cert['other_seven_gates']
assert all(sha(Path(p))==h for p,h in checked.items())
receipt={'status':'PASS_SAME_TEAM_SOURCE_ALLOWANCE_CODE_AND_THEOREM_REVIEW','reviewed_at_utc':datetime.now(timezone.utc).isoformat(),'scope':'Read-only frozen source/math/control review plus source-only independent-expression mpmath crosscheck; no case outcome evaluation','review_code_sha256':sha(__file__),'source_hashes_before_after_equal':checked,'crosscheck_precision_decimal_digits':mp.mp.dps,'source_affine_slope':mp.nstr(slope,140),'source_affine_intercept':mp.nstr(intercept,140),'independently_crosschecked_allowance':mp.nstr(allowance,140),'allowance_within_published_outward_interval':True,'formal_outward_certificate':'Primary512-bit Arb source certificate; mpmath is a diagnostic crosscheck, not a replacement rigorous enclosure.','findings':['Affine inversion and all inequality signs are correct.','Rlim=sin(sep/2-argumentGate) suffices for strict disk and angular inequalities on checked principal branch.','Actual rawshift upper is compared strictly to outward-certified dyadic allowance lower; equality/inconclusiveHOLD.','Other seven maxima unchanged; fullpolar/retainedspan, actualshift, inverse, eigenpair and emittedquantization terms retained.','No measured case residual enters allowance derivation.','New peroutput angle bound does not silently reuse v1 numerical promise.','Boundarycontrols are syntheticmetrics, not solver outputs; known-outcome development disclosure preserved.'],'material_issues':[],'dependencies':['Complete fresh byte-bound parent savedfactor replay and helper/shape/projection checks before actualcase admission.','Pinned baseline lowrank/order/source-similarity/targetseparation certificates.'],'case_outcomes_evaluated':False,'new_estimator_runs':0,'new_SVD_runs':0,'new_raw_generation':False,'old_receipts_unchanged':True,'external_independent_review':'PENDING','physical_promotion':0,'lane':'development — no registry entry'}
(P/'FINAL_SOURCE_REVIEW.json').write_text(json.dumps(receipt,indent=2));print(json.dumps({k:receipt[k] for k in ['status','source_affine_slope','independently_crosschecked_allowance','material_issues']}))
