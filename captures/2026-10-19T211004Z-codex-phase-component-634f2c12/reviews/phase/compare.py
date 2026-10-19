"""Post-known independent exact/directed comparison, no additive tolerance."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
from flint import arb,acb,fmpq,ctx
ctx.prec=512
ROOT=Path('/workspace/scratch/f3d1c2f040c9');P=ROOT/'directional-phase-audit-20261019';PROD=ROOT/'directional-phase-work-20261019'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
fr=lambda x:F(int(x[0]),int(x[1]));ar=lambda x:arb(fmpq(x.numerator,x.denominator))
def winding_upper(v,windings):
    dist=[abs(v+2*k*arb.pi()) for k in windings]
    j=min(range(len(dist)),key=lambda i:float(dist[i].upper()))
    assert all(dist[j].upper()<dist[k].lower() for k in range(len(dist)) if k!=j)
    return dist[j].upper()
def run():
    f=load(P/'COMPARE_FREEZE.json');assert sha(Path(__file__))==f['script_sha256']
    for n,h in f['inputs'].items():assert sha(ROOT/n)==h,n
    own=load(P/'AUDIT_V2_RECEIPT.json');pub=load(PROD/'CERTIFICATE.json');targets=load(PROD/'inputs/SOURCE_PHASE.json')['target_matches'];caps=load(PROD/'inputs/OLD_POLICY.json')['gates']
    assert len(own['rows'])==len(pub['rows'])==4
    bindings=load(P/'IMMUTABLE_SOURCE_BINDING.json')
    for b in bindings['bindings']:assert sha(ROOT/b['audited_original_path'])==sha(ROOT/b['immutable_repository_path'])==b['sha256']
    exact_rational=0;transcendental=0;arg_checks=0;assignments=0;rows=[]
    for a,b in zip(own['rows'],pub['rows']):
        assert a['case']==b['case'] and a['record_sha256']==b['record_sha256']
        assert b['status']=='CERTIFIED_FINITE_EMITTED_MATCH_AND_SAVED_NUMERICAL_QUALITY' and all(b['gates'].values()) and all(a['gates'].values())
        for n in ['exact_inverse_residual_squared','exact_eigenpair_residual_squared']:assert fr(a[n])==fr(b[n]),n
        for metric,square in [('inverse_residual','exact_inverse_residual_squared'),('eigenpair_residual','exact_eigenpair_residual_squared')]:
            v=fr(b['metrics'][metric]);assert v*v>=fr(a[square]) and v<=fr(caps[metric])
        invnorm=fr(b['metrics']['proposed_inverse_norm']);assert invnorm**2>=fr(a['proposed_inverse_norm_bound_squared']) and invnorm<=fr(caps['proposed_inverse_norm'])
        case=ROOT/'directional-admission-work-20261019/results'/a['case']
        emission=np.load(case/'PHASE_PROPOSAL.npz',allow_pickle=False)['two_step_phase']
        ev=np.load(case/'PHASE_META.npz',allow_pickle=False)['eigenvalues']
        pubmax=fr(b['observed']['maximum_circular_error_upper']);argbound=fr(b['metrics']['emitted_argument_error'])
        assert argbound<=fr(caps['emitted_argument_error']) and len(a['matching'])==len(b['observed']['rows'])==209
        for x,y in zip(a['matching'],b['observed']['rows']):
            assert x['emitted_index']==y['emitted_index'] and x['target_index']==y['target_index'] and x['target_label']==y['target_label'] and y['unique_and_within_fixed_radius']
            assignments+=1;i=x['emitted_index'];j=x['target_index'];theta=F(int(emission[i]),1<<60);d=theta-2*fr(targets[j]['omega']);ub=fr(y['circular_error_upper']);oa=fr(x['circular_error_upper'])
            assert pubmax>=ub
            # Whenever no wrap occurs the error is EXACT rational. This also
            # resolves stationary zero without transcendental cancellation.
            if abs(ar(d))<arb.pi():
                assert abs(d)<=ub and abs(d)<=oa;exact_rational+=1
            else:
                v=winding_upper(ar(d),range(-3,4));assert v<=ar(ub) and v<=ar(oa);transcendental+=1
            re=F(*float(ev[i].real).as_integer_ratio());im=F(*float(ev[i].imag).as_integer_ratio())
            if im==0 and re>0 and theta==0:
                assert argbound>=0
            else:
                v=acb(ar(re),ar(im)).arg()-ar(theta);assert winding_upper(v,[-1,0,1])<=ar(argbound)
            arg_checks+=1
        assert len({r['target_index'] for r in a['matching']})==len({r['target_index'] for r in b['observed']['rows']})==209
        rows.append({'case':a['case'],'assignment_count':209,'exact_inverse_and_eigenpair_fractions_equal':True,'all_producer_circular_upper_endpoints_validated':True,'all_producer_argument_upper_bounds_validated':True,'original_frame_status_unchanged':b['prior_frame_verdict_unchanged']})
    receipt={'status':'INDEPENDENT_ASSIGNMENT_FRACTION_AND_DIRECTED_ENDPOINT_COMPARISON_PASS','utc':datetime.now(timezone.utc).isoformat(),'freeze_sha256':sha(P/'COMPARE_FREEZE.json'),'rows':rows,'assignments_checked':assignments,'exact_rational_circular_errors':exact_rational,'wrapped_transcendental_circular_errors':transcendental,'saved_complex_argument_checks':arg_checks,'endpoint_policy':'Validate bounds directly using exact rational nonwrapped differences or directed winding intervals. No additive epsilon, no requirement of identical serialised ceilings.','new_estimator_SVD_alignment_calls':0,'external_review':'PENDING','physical_promotion':0}
    q=P/'COMPARE_RECEIPT.json';assert not q.exists();q.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'status':receipt['status'],'receipt_sha256':sha(q),'assignments':assignments}))
if __name__=='__main__':run()
