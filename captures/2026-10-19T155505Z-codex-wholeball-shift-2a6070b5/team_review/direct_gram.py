"""Post-known-output directed-only data certificate; exact rational final inequality.

No source frame, noise radius, SVD success, external independence or physical claim.
All mutations are confined to this review directory's new receipts/logs.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,time
import numpy as np
from flint import fmpz_mat,arb,fmpq,ctx
ctx.prec=512
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
freeze=json.loads((P/'DIRECT_GRAM_FREEZE.json').read_text());assert sha(__file__)==freeze['code_sha256']
for name,h in freeze['input_sha256'].items():assert sha(Path(name))==h
start=time.monotonic();paths=freeze['factor_paths']
U=np.vstack([np.load(Path(p),allow_pickle=False)['left'] for p in paths])[:,:209]
with np.load(Path(freeze['phase_meta_path']),allow_pickle=False) as z:T=z['shift']
assert U.shape==(8191,209) and T.shape==(209,209)
def encode(x):
 assert x.dtype==np.float64 and np.all(np.isfinite(x))
 ratios=[float(v).as_integer_ratio() for v in x.flat];bits=max(d.bit_length()-1 for n,d in ratios)
 return np.array([n<<(bits-d.bit_length()+1) for n,d in ratios],dtype=object).reshape(x.shape),bits
un,bu=encode(U);tn,bt=encode(T)
A=fmpz_mat(un[:-2].tolist());B=fmpz_mat(un[2:].tolist());tm=fmpz_mat(tn.tolist())
print('Computing actual deleted-basis exact Gram',flush=True)
G=A.transpose()*A;gn=np.array(G.tolist(),dtype=object);defect=gn-np.eye(209,dtype=object)*(1<<(2*bu))
eta2=F(sum(int(v)**2 for v in defect.flat),1<<(4*bu));assert 0<=eta2<1
eta=arb(fmpq(eta2.numerator,eta2.denominator)).sqrt();ellnum=((1-eta)*(1<<180)).floor().unique_fmpz();assert ellnum is not None
ell=F(int(ellnum),1<<180)
# This is an exact rational certificate of the proposed singularvalue-squared margin.
assert 0<ell<=1 and (1-ell)**2>=eta2
print('Computing direct exact saved residual and normal matrix',flush=True)
E=B*(1<<bt)-A*tm
s2=F(sum(int(v)**2 for row in E.tolist() for v in row),1<<(2*bu+2*bt))
N=A.transpose()*E
n2=F(sum(int(v)**2 for row in N.tolist() for v in row),1<<(4*bu+2*bt))
raw_lower=s2-n2/ell;lower=max(F(0),raw_lower);gate=F(*freeze['old_shift_gate']);flag=lower>gate*gate
parent=json.loads(Path(freeze['parent_normal_certificate']).read_text());old=next(x for x in parent['rows'] if x['case']=='directed_period4')
assert s2==F(*map(int,old['exact_shift_residual_squared'])) and n2==F(*map(int,old['exact_normal_residual_squared']))
for name,h in freeze['input_sha256'].items():assert sha(Path(name))==h
pair=lambda v:[str(v.numerator),str(v.denominator)]
lr=arb(fmpq(lower.numerator,lower.denominator)).sqrt();nl=arb(fmpq(n2.numerator,n2.denominator)).sqrt()
def down(v):return [int((v*(1<<180)).floor().unique_fmpz()),1<<180]
result={'status':'CERTIFIED_DATA_ONLY_FIXED_BASIS_OLD_GATE_OBSTRUCTION' if flag else 'HOLD_DATA_ONLY_FIXED_BASIS_OBSTRUCTION','case':'directed_period4','reviewed_at_utc':datetime.now(timezone.utc).isoformat(),'freeze_sha256':sha(P/'DIRECT_GRAM_FREEZE.json'),'code_sha256':sha(__file__),'input_sha256_before_after_equal':freeze['input_sha256'],'actual_deleted_basis_gram_defect_squared_exact':pair(eta2),'deleted_basis_sigma_min_squared_lower_exact':pair(ell),'margin_certificate_exact':{'ell_positive':ell>0,'ell_at_most_one':ell<=1,'one_minus_ell_squared_at_least_Gram_F_defect_squared':(1-ell)**2>=eta2},'direct_shift_residual_squared_exact':pair(s2),'direct_normal_residual_squared_exact':pair(n2),'LS_minimum_residual_squared_lower_before_max0_exact':pair(raw_lower),'LS_minimum_residual_squared_lower_exact':pair(lower),'old_shift_gate_squared_exact':pair(gate*gate),'strict_squared_lower_exceeds_old_gate':flag,'LS_minimum_residual_norm_lower':down(lr),'readable':{'Gram_F_defect':float(eta.mid()),'singularvalue_squared_lower':float(ell),'LS_minimum_residual_norm_lower':float(lr.lower()),'normal_residual_F':float(nl.upper())},'parent_direct_N_and_expanded_s2_exactly_agree':True,'proof':'G=A^T A; ||G-I||2<=etaF<=1-ell =>sigmamin(A)^2>=ell. ExactnormalLS Pythagoras implies min_T||B-AT||F^2>=s2-n2/ell. Finalstrictgatecomparison is rational, not floating.','scope':'Every real replacement T on THIS saved basis violates ONLY old fixedrawshiftgate ifflagtrue. No otherbasis/algorithm/truephase/v2/wholeballuniform failure claim.','source_frame_or_wholeball_bound_needed':False,'post_known_outcome_supplement':True,'new_estimator_runs':0,'new_SVD_runs':0,'new_raw_generation':False,'external_independent_review':'PENDING','physical_promotion':0,'lane':'development — no registry entry','seconds':time.monotonic()-start}
dest=P/'DIRECT_GRAM_CERTIFICATE.json';assert not dest.exists();dest.write_text(json.dumps(result,indent=2));print(json.dumps({k:result[k] for k in ['status','readable','seconds']}),flush=True)
