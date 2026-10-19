"""Compare independent cross-Grams and expanded normal equations with certificate.

Saved factors only; no raw projection or estimator invocation. Main certificate
is untrusted until exact scalar comparisons below. Frozen before execution.
"""
import sys
sys.dont_write_bytecode=True
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
from flint import fmpz_mat,arb,fmpq,ctx
ctx.prec=512
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
P=ROOT/'prospective-frame-work'
load=lambda p:json.loads(Path(p).read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
fraction=lambda x:F(int(x[0]),int(x[1]))
asarb=lambda x:arb(fmpq(x.numerator,x.denominator))

def encode(x):
 assert x.dtype==np.float64 and np.all(np.isfinite(x))
 pairs=[float(v).as_integer_ratio() for v in x.flat];b=max(d.bit_length()-1 for n,d in pairs)
 n=np.array([v<<(b-(d.bit_length()-1)) for v,d in pairs],dtype=object).reshape(x.shape)
 return fmpz_mat(n.tolist()),b

def sumsq(M):return sum(int(x)**2 for row in M.tolist() for x in row)
def inner(M,N):return sum(int(M[i,j])*int(N[i,j]) for i in range(M.nrows()) for j in range(M.ncols()))

def run():
 fr=load(HERE/'OUTCOME_COMPARE_FREEZE.json')
 for p,h in fr['files'].items():assert sha(ROOT/p)==h,p
 cert=load(P/'CERTIFICATE.json');measure=load(HERE/'CROSSGRAM_OUTCOME.json');pr=load(P/'PROTOCOL_FREEZE.json');budget=load(P/'inputs/FIXED_BUDGET.json')['source_budget'];u=load(P/'inputs/PARENT_UNIFORM.json')
 assert budget==pr['fixed_budget'] and cert['protocol_sha256']==sha(P/'PROTOCOL_FREEZE.json') and cert['budget_sha256']==sha(P/'inputs/FIXED_BUDGET.json')
 assert sha(P/'inputs/FIXED_BUDGET.json')==sha(ROOT/'floating-budget-work/BUDGET_CERTIFICATE.json')
 beta=asarb(fraction(u['deleted_two_rows_beta_lower']));sigma=asarb(fraction(u['comparison_shift_residual_upper']));m=asarb(fraction(u['comparison_shift_norm_upper']));allow=asarb(fraction(budget['allowance_lower']))
 rows=[]
 for own,main in zip(measure['rows'],cert['rows']):
  assert own['case']==main['case'] and own['record_sha256']==main['record_sha256'] and own['learned_order']==main['learned_order']
  if own['execution_status']!='COMPLETED' or own['learned_order']!=209:
   assert main['status'].startswith('HOLD');rows.append({'case':own['case'],'retained_HOLD':main['status']});continue
  case=P/'results'/own['case'];U=np.vstack([np.load(case/f'U_{k}.npz',allow_pickle=False)['basis'] for k in range(3)]);T=np.load(case/'PHASE_META.npz',allow_pickle=False)['shift'];un,b=encode(U);tn,bt=encode(T)
  # Recover row-deleted A/B by indexing exact stored integers, then use
  # an expanded normal-residual norm, unlike the parent's explicit N array.
  raw=un.tolist();A=fmpz_mat(raw[:-2]);B=fmpz_mat(raw[2:]);G=A.transpose()*A;H=A.transpose()*B;GT=G*tn
  n2=F(sumsq(H),1<<(4*b))+F(sumsq(GT),1<<(4*b+2*bt))-2*F(inner(H,GT),1<<(4*b+bt))
  shift=B*(1<<bt)-A*tn;s2=F(sumsq(shift),1<<(2*b+2*bt))
  r2=fraction(own['alignment_residual_squared']);eta2=fraction(own['retained_Gram_defect_squared'])
  assert r2==fraction(main['alignment_residual_squared'])
  assert n2==fraction(main['normal_residual_squared']) and s2==fraction(main['actual_raw_shift_squared']) and n2>=0 and s2>=0
  assert eta2<=fraction(main['retained_Gram_defect_F_upper'])**2
  eta=asarb(eta2).sqrt();nu=asarb(n2).sqrt();r=asarb(r2).sqrt();s=r/(1-eta).sqrt();assert s<1
  # Alternate principal-angle expression, distinct from parent's rationalization.
  d=(2-2*(1-s*s).sqrt()).sqrt();J=(1+eta).sqrt()*(sigma+(1+m)*d);amin=(1-eta).sqrt()*(beta-d);assert amin>0
  bound=(J*J+(nu/amin)**2).sqrt()
  gates={'order_applicability':True,'retained_Gram_cap':eta2<=fraction(budget['retained_Gram_cap'])**2,'fixed_normal_cap':n2<=fraction(budget['normal_cap'])**2,'frame_budget':r2<fraction(budget['allowed_raw_frame_residual_lower'])**2,'source_bound_strict_allowance':bool(bound<allow)}
  assert gates==main['gates']
  expected='CERTIFIED_FRESH_MEASURED_SOURCE_FRAME_SHIFT' if all(gates.values()) else 'HOLD_'+'_AND_'.join(k for k,v in gates.items() if not v).upper()
  assert main['status']==expected
  boundpair=fraction(main['direct_bound']['shift']);assert bound<=asarb(boundpair) and asarb(boundpair)-bound<arb(1)/(1<<180)
  assert asarb(s2).sqrt()<=bound
  row={'case':own['case'],'status':expected,'all_main_gates_independently_matched':True,'crossgram_alignment_squared_exact_match':True,'expanded_normal_squared_exact_match':True,'direct_shift_squared_exact_match':True,'retained_Gram_upper_verified':True,'readable_direct_source_shift_upper':float(bound.upper()),'gates':gates}
  rows.append(row);print(json.dumps(row),flush=True)
 for p,h in fr['files'].items():assert sha(ROOT/p)==h,p
 result={'status':'PASS_SAME_TEAM_EXACT_FRESH_FRAME_OUTCOME_REVIEW','rows':rows,'main_certificate_sha256':sha(P/'CERTIFICATE.json'),'comparison_freeze_sha256':sha(HERE/'OUTCOME_COMPARE_FREEZE.json'),'crossgram_measurement_sha256':sha(HERE/'CROSSGRAM_OUTCOME.json'),'all_pinned_hashes_before_after_equal':True,'completed_utc':datetime.now(timezone.utc).isoformat(),'scope':'Independent arithmetic expressions over saved binary64 dyadics. No parent code imported or estimator/SVD/raw-projection run. Parent raw-generation/reprojection and original source proofs are separate dependencies. All main certificate HOLDs retained; no old raw-ball/fullfactor/phase/uniform solver/external claim.','external_review':'PENDING','physical_promotion':0}
 out=HERE/'OUTCOME_REVIEW.json';assert not out.exists();out.write_text(json.dumps(result,indent=2))

if __name__=='__main__':run()
