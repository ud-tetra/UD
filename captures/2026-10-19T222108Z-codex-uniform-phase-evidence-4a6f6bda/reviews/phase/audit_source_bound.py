"""Independent integer-power and stable-angle evaluator; no producer imports."""
import hashlib,json
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from flint import arb,fmpq,fmpz_mat,ctx
ctx.prec=512
HERE=Path(__file__).resolve().parent
REPO=HERE.parent/'ud-repo'
PRODUCER=HERE.parent/'phase-uniform-20261019'
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def a(v):
    if isinstance(v,(list,tuple)):v=F(int(v[0]),int(v[1]))
    v=F(v);return arb(fmpq(v.numerator,v.denominator))
def endpoint(v,lower=False):
    n=(arb(v.lower() if lower else v.upper())*(1<<200))
    n=(n.floor() if lower else n.ceil()).unique_fmpz();assert n is not None
    return [str(n),str(1<<200)]
def run():
    fr=json.loads((HERE/'SOURCE_REVIEW_FREEZE.json').read_text())
    for p,h in fr['files'].items():assert digest(HERE/p)==h
    for p,h in fr['source_files'].items():assert digest(REPO/p)==h
    src=REPO/'captures/2026-10-19T134625Z-codex-uniform-output-73b6e18a/admission/inputs'
    U=json.loads((src/'PARENT_UNIFORM.json').read_text());M=json.loads((src/'PARENT_PHASE.json').read_text())['metrics'];O=json.loads((src/'PARENT_ORDER.json').read_text())
    null=json.loads((REPO/'captures/2026-10-19T215410Z-codex-phase-run-calibration-43cadbae/phase/inputs/NULL_VECTOR.json').read_text())['vector']
    # Matrix blocks formed independently; exact Gram uses a sum of row outer products.
    left=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64)
    right=np.random.default_rng(184052).choice([-1.,1.],size=(2294,160)).astype(np.int64)
    middle=np.zeros(2294,dtype=np.int64);middle[:len(null)]=null
    A=np.concatenate([left*2,middle[:,None],right*2],axis=1)
    assert np.all(middle@left==0) and int(middle@middle)==16228
    # Distinct accumulation from producer's single A.T@A expression.
    gram=sum((A[lo:lo+128].T@A[lo:lo+128] for lo in range(0,2294,128)),np.zeros((321,321),dtype=np.int64))
    G=fmpz_mat(gram.tolist());W=G**32
    B=max(sum(abs(int(W[i,j])) for j in range(321)) for i in range(321))
    operator=a(B).root(64)/128;C=operator*a(303067).sqrt()
    r=a(U['baseline_low_rank_residual_upper']);s=a(O['qth_sigma_lower']);eta=a([1,1<<43]);eps=a([1,1<<41]);raw=a([1,1<<34]);invres=a([1,1<<40]);inorm=a(128);eig=a([1,1<<42]);arg=a([1,1<<50]);sep=a(M['minimum_target_chord_lower'])
    baseline_eta=a(M['basis_orthogonality_upper']);invD=a(M['source_inverse_norm_upper'])/(1-a(M['source_inverse_residual_upper']));normD=a(M['source_reduction_norm_upper']);L=a(M['intertwining_residual_upper']);beta=a(U['deleted_two_rows_beta_lower']);sigma=a(U['comparison_shift_residual_upper']);normM=a(U['comparison_shift_norm_upper'])
    rows=[]
    for numerator,denominator in [(0,1),(1,1<<48),(3,1<<49),(2,1<<48),(1127,1<<48)]:
      for ideal in [True,False]:
        epsilon=arb(0) if ideal else eps;rhoU=arb(0) if ideal else eta
        leakage=r+C*a([numerator,denominator])+epsilon
        denominator_bound=s-r-leakage
        sine=leakage/denominator_bound
        distance=sine*(2/(1+(1-sine*sine).sqrt())).sqrt()
        returned_residual=arb(0) if ideal else raw/(1-rhoU).sqrt()
        difference=(sigma+returned_residual+distance*(1+normM))/(beta-distance)
        eigen_correction=arb(0) if ideal else ((1+rhoU)/(1-rhoU)).sqrt()*eig*inorm/(1-invres)
        R=invD*(L+((1+baseline_eta)/(1-baseline_eta)).sqrt()*normD*(difference+eigen_correction))
        angular=R.asin()+(arb(0) if ideal else arg)
        passed=bool(2*R<sep and 2*angular<sep)
        rows.append(dict(delta=[numerator,denominator],ideal=ideal,passes=passed,phase_upper=endpoint(angular),readable_phase_upper=float(angular.upper()),margin_lower=endpoint(sep/2-angular,True)))
    gramsha=hashlib.sha256(gram.astype('<i8').tobytes()).hexdigest()
    result=dict(status='PASS_INDEPENDENT_SOURCE_BOUND_EVALUATION',integer_power32_row_bound=str(B),Gram_sha256=gramsha,C_upper=endpoint(C),readable_C_upper=float(C.upper()),rows=rows,source_freeze_sha256=digest(HERE/'SOURCE_REVIEW_FREEZE.json'),new_estimator_SVD_eigenvalue_calls=0,external_review='PENDING',physical_promotion=0)
    assert rows[4]['passes'] and rows[5]['passes'] and not rows[6]['passes'] and not rows[7]['passes']
    (HERE/'SOURCE_BOUND_REVIEW.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status=result['status'],C=result['readable_C_upper'],rows=[(z['delta'],z['ideal'],z['passes'],z['readable_phase_upper']) for z in rows])))
if __name__=='__main__':run()
