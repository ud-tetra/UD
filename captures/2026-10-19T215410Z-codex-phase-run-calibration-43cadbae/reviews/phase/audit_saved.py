"""Independent direct dyadic frame, finite phase, and exact-T saved-output audit."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,json,hashlib,io,zipfile
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
from flint import arb,acb,fmpq,fmpz_mat,ctx
import phase_math_helpers as mh
ctx.prec=512
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();load=lambda p:json.loads(Path(p).read_text())
q=lambda x:F(int(x[0]),int(x[1]));a=lambda x:arb(fmpq(x.numerator,x.denominator));pair=lambda x:[str(x.numerator),str(x.denominator)]
def winding(v,ks):
    values=[abs(v+2*k*arb.pi()) for k in ks];j=min(range(len(values)),key=lambda k:float(values[k].upper()))
    assert all(values[j].upper()<values[k].lower() for k in range(len(values)) if k!=j)
    return values[j].upper()
def gramdef(G,b):return F(sum((int(G[i,j])-((1<<(2*b)) if i==j else 0))**2 for i in range(209) for j in range(209)),1<<(4*b))
def reference(protocol,repo):
    rows=[]
    for r in protocol['reference_basis_archives']:
        zpath=repo/r['archive'];assert sha(zpath)==r['archive_sha256']
        with zipfile.ZipFile(zpath) as z:assert z.namelist().count(r['member'])==1;blob=z.read(r['member'])
        assert hashlib.sha256(blob).hexdigest()==r['sha256']
        with np.load(io.BytesIO(blob),allow_pickle=False) as z:rows.append(z['basis'])
    U=np.vstack(rows);assert U.shape==(8191,209);return U
def frame(A,b0,eta0,case,X,T,row,budget):
    U=np.vstack([np.load(case/f'U_{k}.npz',allow_pickle=False)['basis'] for k in range(3)]);B,b1=mh.enc(U);xl,bx=mh.enc(X);tl,bt=mh.enc(T)
    XM=mh.fm(xl);TM=mh.fm(tl);br=max(b1,b0+bx);rnum=0;N=fmpz_mat(209,209);G=fmpz_mat(209,209)
    for k in range(0,8191,256):
        am=mh.fm(A[k:k+256]);bm=mh.fm(B[k:k+256]);R=bm*(1<<(br-b1))-(am*XM)*(1<<(br-b0-bx))
        rnum+=mh.ss(R);N+=am.transpose()*R;G+=bm.transpose()*bm
    r2=F(rnum,1<<(2*br));n2=F(mh.ss(N),1<<(2*(b0+br)));lower=r2-n2/(1-eta0);g2=gramdef(G,b1)
    lagN=fmpz_mat(209,209);lagnum=0
    for k in range(0,8189,256):
        end=min(8189,k+256);bm=mh.fm(B[k:end]);bp=mh.fm(B[k+2:end+2]);D=bp*(1<<bt)-bm*TM
        lagnum+=mh.ss(D);lagN+=bm.transpose()*D
    shift2=F(lagnum,1<<(2*(b1+bt)));nu2=F(mh.ss(lagN),1<<(2*(2*b1+bt)))
    for name,value in [('exact_alignment_residual_squared',r2),('exact_alignment_normal_squared',n2),('exact_minimum_alignment_residual_squared_lower',lower),('retained_Gram_squared',g2),('actual_shift_squared',shift2),('actual_normal_squared',nu2)]:assert value==q(row[name]),name
    cap=q(budget['allowed_raw_frame_residual_lower']);verdict='CERTIFIED_FRAME_PASS' if r2<cap*cap else ('CERTIFIED_FRAME_FAIL' if lower>cap*cap else 'HOLD_FRAME_INCONCLUSIVE')
    assert verdict==row['frame_verdict'];gp=g2<=q(budget['retained_Gram_cap'])**2;npas=nu2<=q(budget['normal_cap'])**2
    assert gp==row['retained_Gram_cap_pass'] and npas==row['normal_cap_pass']
    upper=q(row['alignment_residual_F_upper']);lo=q(row['minimum_alignment_residual_F_lower']);assert upper*upper>=r2 and lo*lo<=max(F(0),lower)
    return {'frame_verdict':verdict,'Gram_pass':gp,'normal_pass':npas,'direct_r_squared':pair(r2),'direct_N_squared':pair(n2),'direct_minimum_alignment_lower_squared':pair(lower)}
def phases(meta,em,pub,targets,sep,caps):
    inv2,eig2,hn2=mh.complex_metrics(meta)
    assert inv2==q(pub['exact_inverse_residual_squared']) and eig2==q(pub['exact_eigenpair_residual_squared'])
    for name,value in [('inverse_residual',inv2),('eigenpair_residual',eig2)]:v=q(pub['metrics'][name]);assert v*v>=value and v<=q(caps[name])
    h=q(pub['metrics']['proposed_inverse_norm']);assert h*h>=hn2 and h<=q(caps['proposed_inverse_norm'])
    assert pub['observed']['bijective'] and len(pub['observed']['rows'])==209 and len({r['target_index'] for r in pub['observed']['rows']})==209
    angles=meta['angles'];ev=meta['eigenvalues'];argbound=q(pub['metrics']['emitted_argument_error']);assert argbound<=q(caps['emitted_argument_error'])
    rational=0;wrapped=0
    for r in pub['observed']['rows']:
        i=r['emitted_index'];j=r['target_index'];theta=F(int(em[i]),1<<60);target=targets[j];assert r['target_label']==target['label'] and r['unique_and_within_fixed_radius']
        n,d=float(angles[i]).as_integer_ratio();z,rem=divmod(n*(1<<60),d);assert int(em[i])==z+int(2*rem>d or(2*rem==d and z%2))
        delta=theta-2*q(target['omega']);upper=q(r['circular_error_upper']);assert upper<sep/2
        if abs(a(delta))<arb.pi():assert abs(delta)<=upper;rational+=1
        else:assert winding(a(delta),range(-3,4))<=a(upper);wrapped+=1
        re=F(*float(ev[i].real).as_integer_ratio());im=F(*float(ev[i].imag).as_integer_ratio())
        if not(im==0 and re>0 and theta==0):assert winding(acb(a(re),a(im)).arg()-a(theta),[-1,0,1])<=a(argbound)
    assert q(pub['observed']['maximum_circular_error_upper'])>=max(q(r['circular_error_upper']) for r in pub['observed']['rows'])
    return {'emissions_checked':209,'rational_nonwrapped_errors':rational,'directed_wrapped_errors':wrapped,'exact_inverse_squared':pair(inv2),'exact_eigenpair_squared':pair(eig2),'inverse_norm_bound_squared':pair(hn2),'maximum_circular_error_upper':pub['observed']['maximum_circular_error_upper']}
def exactT(meta,phase,row,sep):
    centers=[(F(*float(z.real).as_integer_ratio()),F(*float(z.imag).as_integer_ratio())) for z in meta['eigenvalues']]
    s2=min((x-u)**2+(y-v)**2 for j,(x,y) in enumerate(centers) for u,v in centers[:j]);m2=min(x*x+y*y for x,y in centers)
    assert s2==q(row['minimum_center_separation_squared']) and m2==q(row['minimum_center_modulus_squared'])
    mt=phase['metrics'];rho,e,h=[q(mt[k]) for k in ['inverse_residual','eigenpair_residual','proposed_inverse_norm']];assert rho<1;R=e*h/(1-rho);assert R==q(row['radius'])
    assert s2>4*R*R and m2>R*R
    alternate=(a(R)/a(m2-R*R).sqrt()).atan();disp=q(row['phase_displacement_upper']);assert alternate.upper()<=a(disp)
    total=disp+q(mt['emitted_argument_error'])+q(phase['observed']['maximum_circular_error_upper']);assert total==q(row['exact_T_to_source_angular_upper']) and total<sep/2
    assert row['status']=='CERTIFIED_EXACT_T_SOURCE_PHASE_BIJECTION' and row['algebraic_eigenvalue_count_per_disk']==1
    return {'center_pair_checks':21736,'center_moduli_checked':209,'disk_and_origin_predicates':True,'independent_atan_validates_arcsine':True,'exact_T_source_phase_upper':pair(total)}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--repo',required=True);args=ap.parse_args();S=Path(args.source).resolve();repo=Path(args.repo).resolve();f=load(P/'SAVED_AUDIT_FREEZE.json')
    assert sha(Path(__file__))==f['script_sha256'] and sha(P/'phase_math_helpers.py')==f['helper_sha256']
    for n,h in f['producer_files'].items():assert sha(S/n)==h,n
    protocol=load(S/'PROTOCOL_FREEZE.json')
    for n,h in protocol['files'].items():assert sha(S/n)==h,n
    for n,h in protocol['repository_sources'].items():assert sha(repo/n)==h,n
    data=load(S/'DATA_FREEZE.json');runs=load(S/'RUN_EXECUTIONS.json');fr=load(S/'CERTIFICATE.json');ph=load(S/'PHASE_CERTIFICATE.json');et=load(S/'EXACT_T_CERTIFICATE.json');af=load(S/'ALIGNMENT_FREEZE.json')
    assert len(data['records'])==len(runs['rows'])==len(fr['rows'])==len(ph['rows'])==len(et['rows'])==4 and runs['planned_and_actual_estimator_runs']==4
    source=load(S/'inputs/SOURCE_PHASE.json');targets=source['target_matches'];sep=q(source['metrics']['minimum_target_chord_lower']);omega=[a(q(t['omega'])) for t in targets]
    for j in range(209):
        for k in range(j):assert 2*abs((omega[j]-omega[k]).sin())>=a(sep)
    U0=reference(protocol,repo);A,b0=mh.enc(U0);G0=fmpz_mat(209,209)
    for k in range(0,8191,256):am=mh.fm(A[k:k+256]);G0+=am.transpose()*am
    g0=gramdef(G0,b0);eta=q(source['metrics']['basis_orthogonality_upper']);assert g0<=eta*eta and eta<1 and g0==q(fr['exact_reference_Gram_squared'])
    budget=load(S/'inputs/FIXED_BUDGET.json')['source_budget'];caps=load(S/'inputs/OLD_POLICY.json')['gates'];rows=[]
    for name,record,run,Frow,prow,trow in zip(protocol['case_order'],data['records'],runs['rows'],fr['rows'],ph['rows'],et['rows']):
        assert name==record['case']==run['case']==Frow['case']==prow['case']==trow['case'];assert record['record_sha256']==run['record_sha256']==Frow['record_sha256']==prow['record_sha256']
        case=S/'results'/name;assert run==load(case/'RUN.json') and run['projection']==record['projection']
        for n,h in run['numeric_witnesses'].items():assert sha(case/n)==h,n
        if run['execution_status']!='COMPLETED' or run['learned_order']!=209:
            assert 'HOLD' in Frow['frame_verdict'] and 'HOLD' in prow['status'] and 'HOLD' in trow['status'];rows.append({'case':name,'status':'RETAINED_EXECUTION_OR_ORDER_HOLD'});continue
        with np.load(case/'PHASE_META.npz',allow_pickle=False) as z:meta={k:z[k] for k in z.files}
        emission=np.load(case/'PHASE_PROPOSAL.npz',allow_pickle=False)['two_step_phase'];sig=np.load(case/'SVD_META.npz',allow_pickle=False)['singular'];assert np.count_nonzero(sig>2.**-24)==209
        xa=next(r for r in af['rows'] if r['case']==name);assert sha(S/xa['alignment'])==xa['sha256'];X=np.load(S/xa['alignment'],allow_pickle=False)['alignment']
        row={'case':name,'frame':frame(A,b0,eta,case,X,meta['shift'],Frow,budget)}
        if prow['status']=='CERTIFIED_FINITE_EMITTED_MATCH_AND_SAVED_NUMERICAL_QUALITY':row['phase']=phases(meta,emission,prow,targets,sep,caps)
        else:assert 'HOLD' in prow['status'];row['phase']={'status':'RETAINED_PUBLISHED_PHASE_HOLD_NOT_PROMOTED'}
        if trow['status']=='CERTIFIED_EXACT_T_SOURCE_PHASE_BIJECTION':row['exact_T']=exactT(meta,prow,trow,sep)
        else:assert 'HOLD' in trow['status'];row['exact_T']={'status':'RETAINED_PUBLISHED_EXACT_T_HOLD_NOT_PROMOTED'}
        rows.append(row);print(json.dumps({'case':name,'independent_frame':row['frame']['frame_verdict'],'phase_checked':'emissions_checked' in row['phase'],'exact_T_checked':'center_pair_checks' in row['exact_T']}),flush=True)
    result={'status':'COMPLETE_INDEPENDENT_SAVED_OUTPUT_ARITHMETIC_AUDIT','utc':datetime.now(timezone.utc).isoformat(),'freeze_sha256':sha(P/'SAVED_AUDIT_FREEZE.json'),'rows':rows,'source_pairwise_chords_checked':21736,'new_estimator_SVD_eigenvalue_inverse_alignment_calls':0,'raw_or_factor_files_copied':0,'scope':'Direct exact frame/normal/Gram residuals; finite phase endpoints/encoding and complex residual fractions; exact savedT center/radius/atan phase predicates. Published HOLDs retained without promotion. No uniform-family or physical claim.','external_review':'PENDING','physical_promotion':0}
    out=P/'SAVED_AUDIT_RECEIPT.json';assert not out.exists();out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'receipt_sha256':sha(out)}))
if __name__=='__main__':main()
