"""Same-team read-only binding and independently expressed bound review."""
import json,hashlib
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,fmpq,ctx
ctx.prec=512
P=Path(__file__).resolve().parent
W=P.parent/'uniform-output-work'
R=P.parent/'rounding-replay-work'
Q=P.parent/'record-contract-work'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
rat=lambda x:arb(fmpq(*x))
up=lambda x:[int((x*(1<<180)).ceil().unique_fmpz()),1<<180]
f=json.loads((W/'FREEZE.json').read_text());cert=json.loads((W/'UNIFORM_CERTIFICATE.json').read_text())
checks=[]
for group,base in [('code_sha256',W),('input_sha256',W/'inputs'),('helper_sha256',Q),('actual_arrays_sha256',R)]:
 for rel,h in f[group].items():
  path=base/rel;assert sha(path)==h;checks.append({'group':group,'path':str(path),'sha256':h})
for mode,h in f['actual_certificates_sha256'].items():
 path=R/'results'/mode/'CERTIFICATE.json';assert sha(path)==h;checks.append({'group':'actual_certificates_sha256','path':str(path),'sha256':h})
path=Q/'inputs/cyclic_unit/FLOAT_META.npz';assert sha(path)==f['phase_witness_sha256'];checks.append({'group':'phase_witness_sha256','path':str(path),'sha256':sha(path)})
files=[W/n for n in ['FREEZE.json','uniform.py','actual.py','THEOREMS.md','UNIFORM_CERTIFICATE.json','ACTUAL_ADMISSION.json','CONTROLS.json','FIELD_SEMANTICS.json']]
before={str(p):sha(p) for p in files}
u=json.loads((W/'inputs/PARENT_UNIFORM.json').read_text());m=json.loads((W/'inputs/PARENT_PHASE.json').read_text())['metrics'];o=json.loads((W/'inputs/PARENT_ORDER.json').read_text());g={k:rat(v) for k,v in f['gates'].items()}
noise=rat(f['encoded_vector_noise']);r=rat(u['baseline_low_rank_residual_upper']);amp=rat(u['per_vector_noise_multiplier_upper']);s0=rat(o['qth_sigma_lower']);tail=rat(o['qplus1_sigma_upper']);cut=rat(f['source_cutoff'])
e=r+amp*noise+g['full_SVD_error'];alpha=s0-r;assert alpha>2*e
t=e/(alpha-e);eta=g['full_left_orthogonality'];polar_gap=2*eta/(1+(1-eta).sqrt());aligned=(2-2*(1-t*t).sqrt()).sqrt()+polar_gap
beta=rat(u['deleted_two_rows_beta_lower']);assert beta>aligned
actual_sigma=g['raw_shift_residual']/(1-eta).sqrt();base_sigma=rat(u['comparison_shift_residual_upper']);base_norm=rat(u['comparison_shift_norm_upper']);shift=(base_sigma+actual_sigma+aligned*(1+base_norm))/(beta-aligned)
eigenpert=g['eigenpair_residual']*g['proposed_inverse_norm']/(1-g['inverse_residual'])
h=rat(m['source_inverse_norm_upper'])/(1-rat(m['source_inverse_residual_upper']));dn=rat(m['source_reduction_norm_upper']);eta0=rat(m['basis_orthogonality_upper']);base_k=((1+eta0)/(1-eta0)).sqrt();actual_k=((1+eta)/(1-eta)).sqrt()
radius=h*rat(m['intertwining_residual_upper'])+base_k*h*dn*(shift+actual_k*eigenpert);angle=radius.asin()+g['emitted_argument_error'];separation=rat(m['minimum_target_chord_lower'])
assert s0-amp*noise-g['full_SVD_error']>cut and tail+amp*noise+g['full_SVD_error']<cut
assert 2*radius<separation and 2*angle<separation
assert angle<=rat(cert['phase_error_upper']) and angle<arb(fmpq(3078138,10**13))
assert separation/2-angle>arb(fmpq(56457472493,10**18))
admission=json.loads((W/'ACTUAL_ADMISSION.json').read_text())
assert admission['new_estimator_runs']==0 and admission['new_SVD_runs']==0
assert len(admission['rows'])==2 and all(all(x['gates'].values()) for x in admission['rows'])
assert all(sha(Path(p))==h for p,h in before.items())
receipt={'status':'PASS_SAME_TEAM_MATHEMATICAL_AND_BINDING_REVIEW','reviewed_at_utc':datetime.now(timezone.utc).isoformat(),'scope':'Read-only review plus independently expressed512-bit bound arithmetic; no estimator/SVD/raw replay execution','source_bindings_checked':checks,'reviewed_file_hashes':before,'all_reviewed_files_unchanged':True,'review_code_sha256':sha(__file__),'independently_recomputed_phase_upper':up(angle),'independently_recomputed_radius_upper':up(radius),'findings':['Rank209 reference residual implies t=e/(alpha-e) without additional unproved rank claim.','Retained/full polar discrepancy bounded by2p(etaFull); principal Gram compression is valid.','Both saved shift residuals and actual eigenpair/inverse/emission terms are charged.','Actual borrowed V/H is an untrusted witness validated against returnedT and Lambda.','Both actual saved paths meet gates; array identity is not independent replication.','Three analytic negative budget controls are proof-inconclusiveness examples; zero-inverse is an exact witness gate refusal.'],'material_issues':[],'dependencies':['Pinned baseline low-rank, order, source-similarity and separation certificates.','Encoded raw eligibility and integerprojection provenance.','Separate exact parent full-factor SVD certificate replay.'],'quantifier':'Every encoded-ball returned output satisfying frozen gates; no guarantee every solver execution succeeds.','new_estimator_runs':0,'new_SVD_runs':0,'external_independent_review':'PENDING','physical_promotion':0,'lane':'development — no registry entry'}
(P/'REVIEW_RECEIPT.json').write_text(json.dumps(receipt,indent=2));print(json.dumps({k:receipt[k] for k in ['status','independently_recomputed_phase_upper','material_issues']}))
