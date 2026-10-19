"""Same-team post-known-output check; exact expanded cross-Gram arithmetic only.

No imports of parent calculation code, no SVD or estimator execution, no writes
outside this review directory. Frozen before execution.
"""
import sys
sys.dont_write_bytecode = True
import hashlib, json, time
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import fmpz_mat

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
P = ROOT / 'floating-budget-work'
E = ROOT / 'floating-budget-inputs'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())

def encode(values):
    assert values.dtype == np.float64 and np.all(np.isfinite(values))
    pairs = [float(v).as_integer_ratio() for v in values.flat]
    bits = max(d.bit_length()-1 for n,d in pairs)
    rows = np.array([n << (bits-(d.bit_length()-1)) for n,d in pairs], dtype=object).reshape(values.shape)
    return fmpz_mat(rows.tolist()), bits

def frac(p):
    return Fraction(int(p[0]), int(p[1]))

def trace(M):
    return sum(int(M[k,k]) for k in range(M.nrows()))

def run():
    fr = load(HERE/'FINAL_REVIEW_FREEZE.json')
    for path,h in fr['files'].items():
        assert sha(ROOT/path)==h, path
    before = {path:sha(ROOT/path) for path in fr['files']}
    for n,h in load(P/'FREEZE.json')['files'].items():
        assert sha(P/n)==h, n
    for n,h in load(P/'REPLAY_FREEZE.json')['files'].items():
        assert sha(P/n)==h, n
    idx = load(P/'INPUT_INDEX.json')['members']
    for row in idx:
        assert sha(E/row['destination'])==row['sha256'], row['destination']
    direct = {r['case']:r for r in load(P/'DIRECT_METRICS.json')['rows']}
    normal = {r['case']:r for r in load(P/'inputs/PARENT_NORMAL.json')['rows']}
    U0 = np.vstack([np.load(E/('U0_'+n+'.npz'), allow_pickle=False)['basis'] for n in ['A','B']])
    U0n,b0 = encode(U0)
    G0 = U0n.transpose()*U0n
    rows=[]
    for case in load(P/'FREEZE.json')['cases']:
        started = time.monotonic()
        U1 = np.vstack([np.load(E/f'{case}_F{k}.npz', allow_pickle=False)['left'] for k in range(3)])[:,:209]
        X = np.load(P/'witnesses'/f'{case}.npz', allow_pickle=False)['alignment']
        assert U0.shape==U1.shape==(8191,209) and X.shape==(209,209)
        U1n,b1 = encode(U1)
        Xn,bx = encode(X)
        G1 = U1n.transpose()*U1n
        H01 = U0n.transpose()*U1n
        square_num=trace(Xn.transpose()*G0*Xn)
        cross_num=sum(int(Xn[i,j])*int(H01[i,j]) for i in range(209) for j in range(209))
        residual_squared=Fraction(trace(G1),1<<(2*b1))+Fraction(square_num,1<<(2*b0+2*bx))-2*Fraction(cross_num,1<<(b0+b1+bx))
        assert residual_squared>=0
        assert residual_squared==frac(direct[case]['alignment_residual_squared'])
        defect_squared=Fraction(sum((int(G1[i,j])-int(i==j)*(1<<(2*b1)))**2 for i in range(209) for j in range(209)),1<<(4*b1))
        assert defect_squared<=frac(direct[case]['retained_Gram_defect_F_upper'])**2<1
        assert frac(direct[case]['normal_residual_squared'])==frac(normal[case]['exact_normal_residual_squared'])
        assert frac(direct[case]['actual_raw_shift_squared'])==frac(normal[case]['exact_shift_residual_squared'])
        r={'case':case,'expanded_crossgram_exact_fraction_match':True,
           'alignment_residual_squared':[str(residual_squared.numerator),str(residual_squared.denominator)],
           'retained_Gram_defect_squared':[str(defect_squared.numerator),str(defect_squared.denominator)],
           'retained_Gram_bound_verified':True,'parent_normal_and_raw_shift_exact_fractions_match':True,
           'U0_scale_bits':b0,'U1_scale_bits':b1,'X_scale_bits':bx,
           'elapsed_seconds':time.monotonic()-started}
        rows.append(r)
        print(json.dumps({'case':case,'status':'PASS_EXPANDED_EXACT_CROSSGRAM','elapsed_seconds':r['elapsed_seconds']}),flush=True)
    after={path:sha(ROOT/path) for path in fr['files']}
    assert before==after
    result={'status':'PASS_THREE_EXPANDED_EXACT_CROSSGRAM_CHECKS','rows':rows,
            'before_after_hashes_equal':True,'freeze_sha256':sha(HERE/'FINAL_REVIEW_FREEZE.json'),
            'checked_files':before,'finished_utc':datetime.now(timezone.utc).isoformat(),
            'scope':'Same-team post-known-output independent arithmetic expression. No parent code imported, estimator/SVD/raw generation, archive code execution, or parent mutation. Original raw eligibility/fullfactor/phase certificates remain separate dependencies.',
            'physical_promotion':0,'external_review':'PENDING'}
    q=HERE/'CROSSGRAM_CHECK.json';assert not q.exists();q.write_text(json.dumps(result,indent=2))

if __name__=='__main__':run()
