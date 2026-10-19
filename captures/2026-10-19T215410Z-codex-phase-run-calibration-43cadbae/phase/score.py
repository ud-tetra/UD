"""Frozen four-case emitted phase and optional exact-T scoring; no new solves."""
import json
import numpy as np
from fractions import Fraction as F
from common import P,freeze,sha
import phase,exact_t

def run():
    f=freeze();data=json.loads((P/'DATA_FREEZE.json').read_text());runs=json.loads((P/'RUN_EXECUTIONS.json').read_text());frames=json.loads((P/'CERTIFICATE.json').read_text());assert len(data['records'])==len(runs['rows'])==len(frames['rows'])==4 and runs['data_freeze_sha256']==sha(P/'DATA_FREEZE.json')
    setup=phase.target_setup();C=json.loads((P/'CONTRACT.json').read_text())
    assert phase.a(C['fixed_source_minimum_chord_lower'])==setup[2]
    out=[];ext=[]
    for name,rec,r,frame in zip(f['case_order'],data['records'],runs['rows'],frames['rows']):
        assert name==rec['case']==r['case']==frame['case'];assert rec['record_sha256']==r['record_sha256']==frame['record_sha256'];d=P/'results'/name;assert r==json.loads((d/'RUN.json').read_text())
        for n,h in r['numeric_witnesses'].items():assert sha(d/n)==h
        row={'case':name,'record_sha256':rec['record_sha256'],'learned_order':r['learned_order'],'strict_frame_verdict_separate':frame['frame_verdict'],'retained_Gram_cap_pass_separate':frame.get('retained_Gram_cap_pass'),'normal_cap_pass_separate':frame.get('normal_cap_pass'),'physical_promotion':0}
        e={'case':name,'physical_promotion':0}
        if r['execution_status']!='COMPLETED' or r['learned_order']!=209:
            row['status']='HOLD_EXECUTION_OR_ORDER';e['status']='HOLD_NO_QUALIFIED_PHASE_OUTPUT'
        else:
            try:row.update(phase.qualify(d/'PHASE_META.npz',d/'PHASE_PROPOSAL.npz',setup))
            except Exception as exc:row.update(status='HOLD_PHASE_VERIFICATION_EXCEPTION',error={'type':type(exc).__name__,'message':str(exc)},policy='No retry, precision, matching, gate or source changes')
            try:
                if row['status']!='CERTIFIED_FINITE_EMITTED_MATCH_AND_SAVED_NUMERICAL_QUALITY':e['status']='HOLD_NO_QUALIFIED_PHASE_OUTPUT'
                else:
                    with np.load(d/'PHASE_META.npz',allow_pickle=False) as z:s2,m2=exact_t.exact_centers(z['eigenvalues'])
                    mt=row['metrics'];rho,er,h=[exact_t.q(mt[n]) for n in ['inverse_residual','eigenpair_residual','proposed_inverse_norm']];status,R=exact_t.predicates(rho,er,h,s2,m2)
                    e.update(status=status,disk_status=status,minimum_center_separation_squared=exact_t.pair(s2),minimum_center_modulus_squared=exact_t.pair(m2),radius=None if R is None else exact_t.pair(R))
                    if status=='CERTIFIED_EXACT_T_DISK_BIJECTION':
                        displacement=exact_t.up((exact_t.a(R)/exact_t.a(m2).sqrt()).asin());total=displacement+exact_t.q(mt['emitted_argument_error'])+exact_t.q(row['observed']['maximum_circular_error_upper']);sep=F(*C['fixed_source_minimum_chord_lower']);e.update(status=exact_t.phase_predicate(total,sep),phase_displacement_upper=exact_t.pair(displacement),exact_T_to_source_angular_upper=exact_t.pair(total),fixed_source_half_chord=exact_t.pair(sep/2),algebraic_eigenvalue_count_per_disk=1,readable_exact_T_phase_upper=float(exact_t.a(total).upper()))
            except Exception as exc:e.update(status='HOLD_EXACT_T_VERIFICATION_EXCEPTION',error={'type':type(exc).__name__,'message':str(exc)})
        out.append(row);ext.append(e);print(json.dumps({'case':name,'phase_status':row['status'],'exact_T_status':e['status'],'frame':frame['frame_verdict'],'phase_error':row.get('observed',{}).get('readable_maximum_circular_error_upper')}),flush=True)
    freeze();result={'status':'COMPLETE_FROZEN_FOUR_CASE_FINITE_PHASE_QUALIFICATION','rows':out,'protocol_sha256':sha(P/'PROTOCOL_FREEZE.json'),'data_freeze_sha256':sha(P/'DATA_FREEZE.json'),'run_executions_sha256':sha(P/'RUN_EXECUTIONS.json'),'frame_certificate_sha256':sha(P/'CERTIFICATE.json'),'new_estimator_SVD_eigenvalue_inverse_alignment_calls':0,'scope':'Finite TWO-step saved emissions modulo2pi; fixed half-source-chord cap certifies identity/bijection, not2^-39 accuracy. Strict frame/Gram/normal separate, no uniform family admission, no idealSVD or physical promotion.','external_review':'PENDING','physical_promotion':0}
    for n,obj in [('PHASE_CERTIFICATE.json',result),('EXACT_T_CERTIFICATE.json',{'status':'COMPLETE_FOUR_SAVED_EXACT_T_ENCLOSURES','rows':ext,'phase_certificate_binding':'PHASE_CERTIFICATE.json','new_numerical_solvers':0,'scope':'Finite exact saved dyadic T only; no idealSVD/uniform-family/physical claim.','physical_promotion':0})]:
        p=P/n;assert not p.exists();p.write_text(json.dumps(obj,indent=2)+'\n')
if __name__=='__main__':run()
