"""Exact lower bound on best possible reference-frame alignment; no SVD/fit."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
from scipy.linalg import solve
from flint import fmpz_mat,arb,fmpq,ctx
from common import P,sha,freeze
ctx.prec=512
def encode(x):
    assert x.dtype==np.float64 and np.isfinite(x).all()
    pairs=[float(v).as_integer_ratio() for v in x.flat];b=max(d.bit_length()-1 for _,d in pairs)
    return np.array([n<<(b-(d.bit_length()-1)) for n,d in pairs],dtype=object).reshape(x.shape),b
fm=lambda x:fmpz_mat(np.asarray(x,dtype=object).tolist())
ar=lambda x:np.array(x.tolist(),dtype=object)
fr=lambda x:F(int(x[0]),int(x[1]))
pair=lambda x:[str(x.numerator),str(x.denominator)]
def up_sqrt(x):
    assert x>=0;v=(arb(fmpq(x.numerator,x.denominator)).sqrt()*(1<<180)).ceil().unique_fmpz();assert v is not None
    return [int(v),1<<180]
def down_sqrt(x):
    assert x>=0;v=(arb(fmpq(x.numerator,x.denominator)).sqrt()*(1<<180)).floor().unique_fmpz();assert v is not None
    return [int(v),1<<180]
def load():
    f=freeze();run=json.loads((P/'RUN_EXECUTIONS.json').read_text())['rows'][0];case=P/'results'/f['case']
    assert run==json.loads((case/'RUN.json').read_text()) and run['record_sha256']==json.loads((P/'DATA_FREEZE.json').read_text())['record_sha256']
    for n,h in run['numeric_witnesses'].items():assert sha(case/n)==h,n
    U0=np.vstack([np.load(P.parent/f['reference_basis_sources'][k],allow_pickle=False)['basis'] for k in ['A','B']])
    if run['execution_status']!='COMPLETED' or run['learned_order']!=209:return f,run,U0,None,None
    U1=np.vstack([np.load(case/f'U_{k}.npz',allow_pickle=False)['basis'] for k in range(3)])
    with np.load(case/'PHASE_META.npz',allow_pickle=False) as z:T=z['shift']
    assert U0.shape==U1.shape==(8191,209) and T.shape==(209,209)
    return f,run,U0,U1,T
def propose():
    f,run,U0,U1,T=load();assert not(P/'ALIGNMENT_FREEZE.json').exists()
    if U1 is None:
        out={'status':'HOLD_NO_APPLICABLE_209_FRAME','run':run,'physical_promotion':0};(P/'COUNTEREXAMPLE_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');return
    X=solve(U0.T@U0,U0.T@U1,assume_a='pos',check_finite=True)
    q=P/'ALIGNMENT.npz';assert not q.exists();np.savez_compressed(q,alignment=X)
    r={'status':'AUXILIARY_DYADIC_X_FROZEN_BEFORE_EXACT_LOWER_BOUND','utc':datetime.now(timezone.utc).isoformat(),'files':{'ALIGNMENT.npz':sha(q),'minimal_frame.py':sha(P/'minimal_frame.py'),'RUN_EXECUTIONS.json':sha(P/'RUN_EXECUTIONS.json'),'DATA_FREEZE.json':sha(P/'DATA_FREEZE.json'),'PROTOCOL_FREEZE.json':sha(P/'PROTOCOL_FREEZE.json')},'scope':'One auxiliary source-coordinate proposal; no estimator rerun, SVD, or choice among candidates. Exact lower witness is valid for ANY finite X.','physical_promotion':0}
    (P/'ALIGNMENT_FREEZE.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'stage':'alignment_frozen','sha256':sha(P/'ALIGNMENT_FREEZE.json')}),flush=True)
def certify():
    f,run,U0,U1,T=load();assert U1 is not None
    af=json.loads((P/'ALIGNMENT_FREEZE.json').read_text())
    for n,h in af['files'].items():assert sha(P/n)==h,n
    with np.load(P/'ALIGNMENT.npz',allow_pickle=False) as z:X=z['alignment']
    A,b0=encode(U0);B,b1=encode(U1);Xi,bx=encode(X);Ti,bt=encode(T)
    G0=ar(fm(A).transpose()*fm(A));G1=ar(fm(B).transpose()*fm(B));H=ar(fm(A).transpose()*fm(B));GX=ar(fm(G0)*fm(Xi))
    I=np.eye(209,dtype=object)
    e0=G0-I*(1<<(2*b0));e1=G1-I*(1<<(2*b1));eta0sq=F(sum(int(v)**2 for v in e0.flat),1<<(4*b0));eta1sq=F(sum(int(v)**2 for v in e1.flat),1<<(4*b1))
    source=json.loads((P/'inputs/SOURCE_PHASE.json').read_text())['metrics'];eta0cap=fr(source['basis_orthogonality_upper']);assert 0<=eta0sq<=eta0cap**2 and eta0cap<1
    ell=1-eta0cap
    r2=F(sum(int(G1[j,j]) for j in range(209)),1<<(2*b1))+F(sum(int(x)*int(y) for x,y in zip(Xi.flat,GX.flat)),1<<(2*b0+2*bx))-2*F(sum(int(x)*int(y) for x,y in zip(Xi.flat,H.flat)),1<<(b0+b1+bx));assert r2>=0
    bn=max(b0+b1,2*b0+bx);N=H*(1<<(bn-b0-b1))-GX*(1<<(bn-2*b0-bx));n2=F(sum(int(v)**2 for v in N.flat),1<<(2*bn));lower=r2-n2/ell
    # Separate actual lag-two normal/shift diagnostics, not required for frame lower proof.
    Am=fm(B[:-2]);Bm=fm(B[2:]);Gm=ar(Am.transpose()*Am);Hm=ar(Am.transpose()*Bm);GT=ar(fm(Gm)*fm(Ti));Nm=Hm*(1<<bt)-GT
    nu2=F(sum(int(v)**2 for v in Nm.flat),1<<(4*b1+2*bt))
    shift2=F(sum(int(v)**2 for v in B[2:].flat),1<<(2*b1))+F(sum(int(x)*int(y) for x,y in zip(Ti.flat,GT.flat)),1<<(2*b1+2*bt))-2*F(sum(int(x)*int(y) for x,y in zip(Ti.flat,Hm.flat)),1<<(2*b1+bt));assert shift2>=0
    budget=json.loads((P/'inputs/FIXED_BUDGET.json').read_text())['source_budget'];cap=fr(budget['allowed_raw_frame_residual_lower']);gram=fr(budget['retained_Gram_cap']);normal=fr(budget['normal_cap']);strict=lower>cap**2
    result={'status':'CERTIFIED_ACTUAL_OUTPUT_MINIMAL_FRAME_COUNTEREXAMPLE' if strict else 'HOLD_NO_MINIMAL_FRAME_COUNTEREXAMPLE','case':run['case'],'record_sha256':run['record_sha256'],'learned_order':run['learned_order'],'exact_reference_Gram_defect_squared':pair(eta0sq),'reference_Gram_cap':pair(eta0cap),'reference_Gram_min_eigenvalue_lower':pair(ell),'exact_alignment_residual_squared':pair(r2),'exact_alignment_normal_residual_squared':pair(n2),'exact_minimum_alignment_residual_squared_lower':pair(lower),'minimum_alignment_residual_F_lower':down_sqrt(max(F(0),lower)),'unchanged_raw_frame_cap':pair(cap),'strict_minimum_frame_obstruction':strict,'retained_Gram_defect_F_upper':up_sqrt(eta1sq),'retained_Gram_cap_pass':eta1sq<=gram**2,'actual_lag2_normal_squared':pair(nu2),'normal_cap_pass':nu2<=normal**2,'actual_lag2_shift_squared':pair(shift2),'actual_lag2_shift_F_upper':up_sqrt(shift2),'alignment_freeze_sha256':sha(P/'ALIGNMENT_FREEZE.json'),'data_freeze_sha256':sha(P/'DATA_FREEZE.json'),'protocol_freeze_sha256':sha(P/'PROTOCOL_FREEZE.json'),'scope':'Actual returned209-column basis cannot satisfy unchanged raw source-frame cap for ANY alignment coefficients if strict=true. Not an ideal-SVD, phase-failure, or all-algorithm no-go theorem. Separate actual diagnostics retain their own PASS/HOLD.','external_review':'PENDING','physical_promotion':0}
    q=P/'COUNTEREXAMPLE_RESULT.json';assert not q.exists();q.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'strict':strict,'lower_readable':float(np.sqrt(float(max(F(0),lower)))),'cap_readable':float(cap),'Gram_pass':result['retained_Gram_cap_pass'],'normal_pass':result['normal_cap_pass']}),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['propose','certify']);a=p.parse_args()
    propose() if a.mode=='propose' else certify()
