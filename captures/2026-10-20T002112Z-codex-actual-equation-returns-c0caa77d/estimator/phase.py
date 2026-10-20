"""Finite emitted-list accuracy and saved eigenpair/inverse/argument diagnostics."""
import json
from pathlib import Path
import numpy as np
from flint import arb,acb
from common import P,freeze,sha,a,up,down
from numeric_math import encode,encode_complex,complex_residual,cmul
from proof_math import fm,arr

def op(r,i,b):
    R,I=fm(r),fm(i);g=arr(R.transpose()*R+I.transpose()*I);h=arr(R.transpose()*I-I.transpose()*R);tr=sum(int(g[j,j]) for j in range(g.shape[0]));row=max(sum(abs(int(g[j,k]))+abs(int(h[j,k])) for k in range(g.shape[0])) for j in range(g.shape[0]));return arb(min(tr,row)).sqrt()/(1<<b)
def circular(v):
    return min((arb(abs(v+2*k*arb.pi()).upper()) for k in [-1,0,1]),key=lambda x:float(x.upper()))
def emitted_integer(angle):
    n,d=float(angle).as_integer_ratio();q,r=divmod(n*(1<<60),d)
    return q+int(2*r>d or(2*r==d and q%2))
def target_setup():
    source=json.loads((P/'inputs/SOURCE_PHASE.json').read_text());targets=source['target_matches'];sep=a(source['metrics']['minimum_target_chord_lower']);assert len(targets)==209 and sep>0
    angles=[]
    for target in targets:
        omega=a(target['omega']);assert abs(2*omega)<4*arb.pi();angles.append(acb(0,2*omega).exp().arg())
    return targets,angles,sep
def match_emissions(em,setup=None):
    targets,target_angles,sep=target_setup() if setup is None else setup;assert em.shape==(209,) and em.dtype==np.int64;rows=[]
    for i,n in enumerate(em):
        theta=arb(int(n))/(1<<60);assert abs(theta)<arb.pi()+arb(1)/(1<<59);errors=[]
        for t in target_angles:
            distances=[abs(theta-t+2*k*arb.pi()) for k in [-1,0,1]];lo=min(z.lower() for z in distances);hi=min(z.upper() for z in distances);errors.append((arb(lo),arb(hi)))
        j=min(range(209),key=lambda k:float(errors[k][1]));err=errors[j][1];unique=all(err<errors[k][0] for k in range(209) if k!=j);ok=bool(unique and err<sep/2)
        rows.append({'emitted_index':i,'target_index':j,'target_label':targets[j]['label'],'circular_error_upper':up(err),'unique_and_within_fixed_radius':ok})
    bijective=len({r['target_index'] for r in rows})==209;passed=bijective and all(r['unique_and_within_fixed_radius'] for r in rows);maximum=a([max(r['circular_error_upper'][0] for r in rows),1<<180])
    return {'status':'CERTIFIED_FINITE_EMITTED_TWO_STEP_BIJECTION' if passed else 'HOLD_FINITE_EMITTED_MATCH','bijective':bijective,'maximum_circular_error_upper':up(maximum),'readable_maximum_circular_error_upper':float(maximum.upper()),'source_minimum_chord_lower':down(sep),'rows':rows,'scope':'Finite exact saved dyadic emitted phases against pinned TWO-STEP source targets modulo2pi; no exact spectrum(T), SI frequency, uniform-ball or unaliased primitive-frequency claim.'}
def qualify(meta,proposal,setup=None):
    with np.load(meta,allow_pickle=False) as z:T=z['shift'];ev=z['eigenvalues'];angles=z['angles'];V=z['eigenvectors'];H=z['inverse']
    with np.load(proposal,allow_pickle=False) as z:em=z['two_step_phase']
    assert T.shape==V.shape==H.shape==(209,209) and ev.shape==angles.shape==em.shape==(209,)
    tn,bt=encode(T);vr,vi,bv=encode_complex(V);ir,ii,bi=encode_complex(H);lr,li,bl=encode_complex(ev);vf=(fm(vr),fm(vi));ident=(fm(np.eye(209,dtype=object)),fm(np.zeros((209,209),dtype=object)))
    rho,rho2=complex_residual(cmul(*vf,fm(ir),fm(ii)),bv+bi,ident,0);hinv=op(ir,ii,bi)
    eigres,eig2=complex_residual((fm(tn)*vf[0],fm(tn)*vf[1]),bt+bv,(fm(vr*lr[None,:]-vi*li[None,:]),fm(vr*li[None,:]+vi*lr[None,:])),bv+bl)
    argnums=[];ties=True
    for j in range(209):
        ties=ties and int(em[j])==emitted_integer(angles[j]);zz=acb(arb(int(lr[j]))/(1<<bl),arb(int(li[j]))/(1<<bl));assert abs(zz)>0
        argnums.append(up(circular(zz.arg()-arb(int(em[j]))/(1<<60)))[0])
    arg=a([max(argnums),1<<180]);caps=json.loads((P/'inputs/OLD_POLICY.json').read_text())['gates'];metrics={'inverse_residual':rho,'proposed_inverse_norm':hinv,'eigenpair_residual':eigres,'emitted_argument_error':arg};gates={n:bool(v<=a(caps[n])) for n,v in metrics.items()};gates['emission_ties_even_consistency']=bool(ties)
    observed=match_emissions(em,setup);gates['finite_observed_bijection']=observed['status']=='CERTIFIED_FINITE_EMITTED_TWO_STEP_BIJECTION'
    delta=eigres*hinv/(1-rho) if rho<1 else None
    return {'status':'CERTIFIED_FINITE_EMITTED_MATCH_AND_SAVED_NUMERICAL_QUALITY' if all(gates.values()) else 'HOLD_FINITE_PHASE_QUALIFICATION','gates':gates,'metrics':{n:up(v) for n,v in metrics.items()},'exact_inverse_residual_squared':[str(x) for x in rho2],'exact_eigenpair_residual_squared':[str(x) for x in eig2],'nearby_diagonalizable_correction_distance_upper':None if delta is None else up(delta),'observed':observed,'readable':{n:float(v.upper()) for n,v in metrics.items()},'scope':'Direct finite emission-list accuracy plus four unchanged saved-output numerical gates and exact encoding. The distance bound is to VLambdaV^-1, not a certified exact-spectrum(T) forward error. No frame-transport or full oldeight-gate admission is inferred.','physical_promotion':0}
def run():
    f=freeze();index=json.loads((P/'SOURCE_INDEX.json').read_text());base=P.parent;runfile=base/index['run_executions'];data=json.loads((base/index['data_freeze']).read_text());runs=json.loads(runfile.read_text())['rows'];frames=json.loads((base/index['frame_certificate']).read_text())['rows'];setup=target_setup();rows=[]
    assert len(index['cases'])==len(data['records'])==len(runs)==len(frames)==4
    assert [r['integer_amplitude'] for r in data['records']]==f['amplitudes']==[0,1,2,4]
    for row,record,run,frame in zip(index['cases'],data['records'],runs,frames):
        assert row['case']==record['case']==run['case']==frame['case'] and record['record_sha256']==run['record_sha256']==frame['record_sha256'];saved=json.loads((base/row['run']).read_text());assert saved==run
        for name in ['PHASE_META.npz','PHASE_PROPOSAL.npz']:assert sha(base/row['directory']/name)==run['numeric_witnesses'][name]
        entry={'case':row['case'],'integer_amplitude':record['integer_amplitude'],'record_sha256':record['record_sha256'],'learned_order':run['learned_order'],'prior_frame_verdict_unchanged':frame['frame_verdict'],'prior_Gram_cap_pass_unchanged':frame['retained_Gram_cap_pass'],'prior_normal_cap_pass_unchanged':frame['normal_cap_pass'],'physical_promotion':0}
        if run['execution_status']!='COMPLETED' or run['learned_order']!=209:entry.update(status='HOLD_EXECUTION_OR_ORDER',execution_status=run['execution_status'])
        else:
            try:entry.update(qualify(base/row['directory']/'PHASE_META.npz',base/row['directory']/'PHASE_PROPOSAL.npz',setup))
            except Exception as exc:entry.update(status='HOLD_VERIFICATION_EXCEPTION',error={'type':type(exc).__name__,'message':str(exc)},policy='Retain exception, no precision/gate/target retry or replacement')
        rows.append(entry);print(json.dumps({'case':entry['case'],'status':entry['status'],'prior_frame':entry['prior_frame_verdict_unchanged'],'phase_error_upper':entry.get('observed',{}).get('readable_maximum_circular_error_upper')}),flush=True)
    freeze();result={'status':'COMPLETE_ALL_FOUR_FROZEN_SAVED_PHASE_QUALIFICATIONS','rows':rows,'amplitudes':f['amplitudes'],'source_index_sha256':sha(P/'SOURCE_INDEX.json'),'protocol_sha256':sha(P/'PROTOCOL_FREEZE.json'),'new_estimator_SVD_alignment_fits':0,'scope':'Finite saved outputs only; quality and matching results separate from unchanged prior strictframe verdicts. No emitted-list target or numerical cap changes, full oldphase/eightgate admission, ideal eigenvalue identification or physical promotion.','external_review':'PENDING','physical_promotion':0};p=P/'CERTIFICATE.json';assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':run()
