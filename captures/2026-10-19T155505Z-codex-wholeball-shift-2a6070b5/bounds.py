"""Source-bound a priori shift residuals; no solver success or phase admission assumed."""
import sys
sys.dont_write_bytecode=True
import json,hashlib
from pathlib import Path
from flint import arb,fmpq,ctx
ctx.prec=512
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def a(p):return arb(fmpq(int(p[0]),int(p[1])))
def up(x):
 z=(x*(1<<180)).ceil().unique_fmpz();assert z is not None;return [int(z),1<<180]
def down(x):
 z=(x*(1<<180)).floor().unique_fmpz();assert z is not None;return [int(z),1<<180]
def freeze():
 f=json.loads((P/'FREEZE.json').read_text())
 for n,h in f['code_sha256'].items():assert sha(P/n)==h,('code',n)
 for n,h in f['input_sha256'].items():assert sha(P/'inputs'/n)==h,('input',n)
 return f
def terms(mode,delta):
 f=freeze();u=json.loads((P/'inputs/PARENT_UNIFORM.json').read_text());o=json.loads((P/'inputs/PARENT_ORDER.json').read_text());g=json.loads((P/'inputs/PR210_FREEZE.json').read_text())['gates']
 r=a(u['baseline_low_rank_residual_upper']);r2=a(u['baseline_exact_low_rank_residual_squared']);assert r*r>=r2
 C=a(u['per_vector_noise_multiplier_upper']);s0=a(o['qth_sigma_lower']);alpha=s0-r
 eta=arb(0) if mode=='ideal' else a(g['full_left_orthogonality']);eps=arb(0) if mode=='ideal' else a(g['full_SVD_error'])
 assert mode in ('ideal','returned_operator_only','returned_F_certificate') and 0<=a(delta)<=a(f['encoded_radius'])
 e2=r+C*a(delta)+eps
 ef=r+C*a(delta)+(arb(209).sqrt()*eps if mode=='returned_operator_only' else eps)
 assert alpha>2*e2 and 0<=eta<1
 t2=e2/(alpha-e2);tf=ef/(alpha-e2);c=(2/(1+(1-t2*t2).sqrt())).sqrt();p=eta/(1+(1-eta).sqrt())
 d2=c*t2+2*p;df=c*tf+2*p
 beta=a(u['deleted_two_rows_beta_lower']);sigma0=a(u['comparison_shift_residual_upper']);M0=a(u['comparison_shift_norm_upper'])
 assert beta>d2
 J=(1+eta).sqrt()*(sigma0+df*(1+M0));amin=(1-eta).sqrt()*(beta-d2)
 return {'d2':d2,'df':df,'J':J,'amin':amin,'eta':eta}
def certify(mode,delta,nu):
 t=terms(mode,delta);normal=a(nu);assert normal>=0
 bound=(t['J']**2+(normal/t['amin'])**2).sqrt()
 allowance=a(json.loads((P/'inputs/PUBLISHED_ALLOWANCE.json').read_text())['raw_shift_strict_upper_allowance_lower'])
 return {'mode':mode,'encoded_radius':delta,'normal_residual_ceiling':nu,
         'basis_operator_distance_upper':up(t['d2']),'basis_Frobenius_distance_upper':up(t['df']),
         'deleted_basis_sigma_min_lower':down(t['amin']),'exact_LS_raw_shift_upper':up(t['J']),
         'returned_raw_shift_upper':up(bound),
         'shift_bound_sufficient_for_published_allowance':bool(bound<allowance),
         'readable':{'exact_LS_raw_shift_upper':float(t['J'].upper()),'returned_raw_shift_upper':float(bound.upper()),'deleted_basis_sigma_min_lower':float(t['amin'].lower())},
         'no_uniform_floating_SVD_or_LS_success_claim':True,'physical_promotion':0}
def verify():
 f=freeze();rows=[certify(mode,delta,nu) for mode in f['modes'] for delta in f['deltas'] for nu in f['normal_ceilings']]
 return {'status':'CERTIFIED_APRIORI_BOUNDS_WITH_EXPLICIT_QUALITY_AND_NORMAL_RESIDUAL_PREMISES','rows':rows,
         'uniform_shift_admission_claimed':False,'external_review':'PENDING','physical_promotion':0}
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');a0=p.parse_args();r=verify();q=P/'APRIORI_BOUNDS.json'
 if a0.replay:assert json.loads(q.read_text())==r
 else:
  assert not q.exists();q.write_text(json.dumps(r,indent=2))
 print(json.dumps(r),flush=True)
