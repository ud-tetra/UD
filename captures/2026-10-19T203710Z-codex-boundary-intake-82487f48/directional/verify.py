"""Exact saved-output upper/lower frame witnesses; no new estimator fits."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
from scipy.linalg import solve
from flint import fmpz_mat,arb,fmpq,ctx
from common import P,sha,freeze
ctx.prec=512
def encode(x):
    assert x.dtype==np.float64 and np.isfinite(x).all();pairs=[float(v).as_integer_ratio() for v in x.flat];b=max(d.bit_length()-1 for _,d in pairs)
    return np.array([n<<(b-(d.bit_length()-1)) for n,d in pairs],dtype=object).reshape(x.shape),b
fm=lambda x:fmpz_mat(np.asarray(x,dtype=object).tolist())
ar=lambda x:np.array(x.tolist(),dtype=object)
fr=lambda x:F(int(x[0]),int(x[1]))
pair=lambda x:[str(x.numerator),str(x.denominator)]
def sqrt_ep(x,lower=False):
    assert x>=0;v=arb(fmpq(x.numerator,x.denominator)).sqrt()*(1<<180);n=(v.floor() if lower else v.ceil()).unique_fmpz();assert n is not None
    return [int(n),1<<180]
def int_frame_verdict(r2,n2,ell,cap):
    assert r2>=0 and n2>=0 and ell>0 and cap>0;lower=r2-n2/ell
    if r2<cap**2:return 'CERTIFIED_FRAME_PASS',lower
    if lower>cap**2:return 'CERTIFIED_FRAME_FAIL',lower
    return 'HOLD_FRAME_INCONCLUSIVE',lower
def source():
    f=freeze();U0=np.vstack([np.load(P.parent/f['reference_basis_sources'][k],allow_pickle=False)['basis'] for k in ['A','B']]);assert U0.shape==(8191,209);return U0
def cases():
    f=freeze();runs=json.loads((P/'RUN_EXECUTIONS.json').read_text());data=json.loads((P/'DATA_FREEZE.json').read_text());assert runs['data_freeze_sha256']==sha(P/'DATA_FREEZE.json') and len(runs['rows'])==len(data['records'])==4
    for amp,run,record in zip(f['amplitudes'],runs['rows'],data['records']):
        assert run['case']==record['case']==f'directional_amp_{amp}' and record['integer_amplitude']==amp and run['record_sha256']==record['record_sha256']
        d=P/'results'/run['case'];assert run==json.loads((d/'RUN.json').read_text())
        for n,h in run['numeric_witnesses'].items():assert sha(d/n)==h,n
        if run['execution_status']!='COMPLETED' or run['learned_order']!=209:yield amp,run,None,None;continue
        U=np.vstack([np.load(d/f'U_{k}.npz',allow_pickle=False)['basis'] for k in range(3)])
        with np.load(d/'PHASE_META.npz',allow_pickle=False) as z:T=z['shift']
        assert U.shape==(8191,209) and T.shape==(209,209);yield amp,run,U,T
def propose():
    freeze();assert not(P/'ALIGNMENT_FREEZE.json').exists();U0=source();d=P/'alignments';d.mkdir();rows=[]
    for amp,run,U,T in cases():
        if U is None:rows.append({'case':run['case'],'status':'HOLD_NO_APPLICABLE_FRAME'});continue
        X=solve(U0.T@U0,U0.T@U,assume_a='pos',check_finite=True);p=d/f'{run["case"]}.npz';np.savez_compressed(p,alignment=X);rows.append({'case':run['case'],'alignment':str(p.relative_to(P)),'sha256':sha(p)})
    out={'status':'ALL_APPLICABLE_AUXILIARY_X_WITNESSES_FROZEN_BEFORE_EXACT_ENDPOINT_EVALUATION','utc':datetime.now(timezone.utc).isoformat(),'rows':rows,'run_executions_sha256':sha(P/'RUN_EXECUTIONS.json'),'data_freeze_sha256':sha(P/'DATA_FREEZE.json'),'verify_code_sha256':sha(P/'verify.py'),'physical_promotion':0};(P/'ALIGNMENT_FREEZE.json').write_text(json.dumps(out,indent=2)+'\n')
def certify():
    f=freeze();af=json.loads((P/'ALIGNMENT_FREEZE.json').read_text());assert af['run_executions_sha256']==sha(P/'RUN_EXECUTIONS.json') and af['data_freeze_sha256']==sha(P/'DATA_FREEZE.json') and af['verify_code_sha256']==sha(P/'verify.py')
    for row in af['rows']:
        if 'alignment' in row:assert sha(P/row['alignment'])==row['sha256']
    U0=source();A,b0=encode(U0);G0=ar(fm(A).transpose()*fm(A));I=np.eye(209,dtype=object);e0=G0-I*(1<<(2*b0));eta0sq=F(sum(int(v)**2 for v in e0.flat),1<<(4*b0));eta0cap=fr(json.loads((P/'inputs/SOURCE_PHASE.json').read_text())['metrics']['basis_orthogonality_upper']);assert 0<=eta0sq<=eta0cap**2 and eta0cap<1;ell=1-eta0cap
    budget=json.loads((P/'inputs/FIXED_BUDGET.json').read_text())['source_budget'];cap=fr(budget['allowed_raw_frame_residual_lower']);gram=fr(budget['retained_Gram_cap']);normal=fr(budget['normal_cap']);rows=[]
    for amp,run,U,T in cases():
        base={'case':run['case'],'integer_amplitude':amp,'record_sha256':run['record_sha256'],'learned_order':run['learned_order'],'execution_status':run['execution_status'],'physical_promotion':0}
        if U is None:base.update(frame_verdict='HOLD_NO_APPLICABLE_FRAME',overall_verdict='HOLD_NO_APPLICABLE_FRAME');rows.append(base);continue
        xrow=next(x for x in af['rows'] if x['case']==run['case'])
        with np.load(P/xrow['alignment'],allow_pickle=False) as z:X=z['alignment']
        B,b1=encode(U);Xi,bx=encode(X);Ti,bt=encode(T);G1=ar(fm(B).transpose()*fm(B));H=ar(fm(A).transpose()*fm(B));GX=ar(fm(G0)*fm(Xi))
        r2=F(sum(int(G1[j,j]) for j in range(209)),1<<(2*b1))+F(sum(int(x)*int(y) for x,y in zip(Xi.flat,GX.flat)),1<<(2*b0+2*bx))-2*F(sum(int(x)*int(y) for x,y in zip(Xi.flat,H.flat)),1<<(b0+b1+bx));assert r2>=0
        bn=max(b0+b1,2*b0+bx);N=H*(1<<(bn-b0-b1))-GX*(1<<(bn-2*b0-bx));n2=F(sum(int(v)**2 for v in N.flat),1<<(2*bn));verdict,lower=int_frame_verdict(r2,n2,ell,cap)
        e1=G1-I*(1<<(2*b1));eta1sq=F(sum(int(v)**2 for v in e1.flat),1<<(4*b1));Am=fm(B[:-2]);Bm=fm(B[2:]);Gm=ar(Am.transpose()*Am);Hm=ar(Am.transpose()*Bm);GT=ar(fm(Gm)*fm(Ti));Nm=Hm*(1<<bt)-GT;nu2=F(sum(int(v)**2 for v in Nm.flat),1<<(4*b1+2*bt))
        shift2=F(sum(int(v)**2 for v in B[2:].flat),1<<(2*b1))+F(sum(int(x)*int(y) for x,y in zip(Ti.flat,GT.flat)),1<<(2*b1+2*bt))-2*F(sum(int(x)*int(y) for x,y in zip(Ti.flat,Hm.flat)),1<<(2*b1+bt));assert shift2>=0
        gp=eta1sq<=gram**2;npas=nu2<=normal**2;overall='CERTIFIED_FINITE_DIRECTIONAL_ADMISSION' if verdict=='CERTIFIED_FRAME_PASS' and gp and npas else ('CERTIFIED_STRICT_FRAME_REFUSAL' if verdict=='CERTIFIED_FRAME_FAIL' else 'HOLD_FINITE_DIRECTIONAL_ADMISSION')
        base.update(frame_verdict=verdict,overall_verdict=overall,exact_alignment_residual_squared=pair(r2),exact_alignment_normal_squared=pair(n2),exact_minimum_alignment_residual_squared_lower=pair(lower),alignment_residual_F_upper=sqrt_ep(r2),minimum_alignment_residual_F_lower=sqrt_ep(max(F(0),lower),True),retained_Gram_squared=pair(eta1sq),retained_Gram_cap_pass=gp,actual_normal_squared=pair(nu2),normal_cap_pass=npas,actual_shift_squared=pair(shift2),actual_shift_F_upper=sqrt_ep(shift2),readable={'alignment_upper':float(np.sqrt(float(r2))),'minimum_alignment_lower':float(np.sqrt(float(max(F(0),lower)))),'cap':float(cap),'Gram_F':float(np.sqrt(float(eta1sq))),'normal_F':float(np.sqrt(float(nu2)))})
        rows.append(base);print(json.dumps({'case':run['case'],'frame_verdict':verdict,'overall_verdict':overall,'readable':base['readable']}),flush=True)
    result={'status':'COMPLETE_FROZEN_FOUR_AMPLITUDE_DIRECTIONAL_ADMISSION_TABLE','rows':rows,'amplitudes':f['amplitudes'],'strict_frame_cap':pair(cap),'retained_Gram_cap':pair(gram),'fixed_normal_cap':pair(normal),'exact_reference_Gram_squared':pair(eta0sq),'reference_Gram_cap':pair(eta0cap),'reference_minimum_Gram_eigenvalue_lower':pair(ell),'protocol_freeze_sha256':sha(P/'PROTOCOL_FREEZE.json'),'data_freeze_sha256':sha(P/'DATA_FREEZE.json'),'alignment_freeze_sha256':sha(P/'ALIGNMENT_FREEZE.json'),'scope':'Finite tested directional amplitudes only. Frame PASS is existence of savedX with strict exact residual gate; FAIL is exact best-possible residual lower strictly exceeding cap. Gram/normal are separate. No monotonicity, continuum, uniform-ball, ideal-SVD or phase-error conclusion.','external_review':'PENDING','physical_promotion':0};out=P/'CERTIFICATE.json';assert not out.exists();out.write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['propose','certify']);a=p.parse_args();propose() if a.mode=='propose' else certify()
