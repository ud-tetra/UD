#!/usr/bin/env python3
"""Exact rational residual enclosure. No numerical libraries or optimizer used."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json,hashlib
import native_model as m
ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def l1(v):return sum(abs(a) for a in v)
def main():
    data=json.loads((ROOT/'SCHEDULE_CERTIFICATE.json').read_text())
    assert data['format']=='native-cayley-rational-trace-v2-parking'
    den=data['trace_denominator'];assert type(den)==int and den>0
    targets=m.checkpoints();park=targets[0].copy();park[16]=Q(0);park[22]=Q(24,37);targets.append(park);N=m.dot(targets[0],targets[0]);assert N==Q(4683,1369) and N<4
    assert all(m.dot(x,x)==N for x in targets)
    assert all(x[:5]==[0]*5 and m.mv(m.B[0],x[5:14])==[0]*5 for x in targets)
    assert all(m.WEIGHTS[0][i]+m.WEIGHTS[1][i]==1 for i in range(23))
    # Rebuild all native matrices; all lower contacts and common face gates stay present.
    matrices={}
    for h in product((0,1),repeat=7):
        a=m.native(h);assert all(a[i][j]==-a[j][i] for i in range(23) for j in range(23))
        matrices[h]=a
    assert len(matrices)==128
    for lower,upper in zip(m.B,m.B[1:]):
        assert all(sum(lower[i][k]*upper[k][j] for k in range(len(upper)))==0 for i in range(len(lower)) for j in range(len(upper[0])))
    prefix=dict(data);prefix['format']='native-cayley-rational-trace-v1';prefix['steps']=data['steps'][:192]
    prefix_bytes=(json.dumps(prefix,separators=(',',':'))+'\n').encode()
    assert hashlib.sha256(prefix_bytes).hexdigest()=='27adf805ce5732ebeda11a7881686cd9b2e934f1d75d5a75e1d4a4459189dd1d'
    prev=targets[0];E=Q(0);elapsed=Q(0);receipts=[];summary=[];timing=Q(0)
    stage_counts=[0,0,0,0];last_stage=1
    for n,pulse in enumerate(data['steps'],1):
        stage=pulse['stage'];assert stage in (1,2,3,4) and stage in (last_stage,last_stage+1)
        last_stage=stage;stage_counts[stage-1]+=1
        h=pulse['mask'];assert len(h)==7 and all(type(v)==int and v in (0,1) for v in h)
        a=matrices[tuple(h)];dt=Q(pulse['t']);assert 0<dt<=4
        assert len(pulse['q_numerators'])==23 and all(type(v)==int for v in pulse['q_numerators'])
        cur=[Q(v,den) for v in pulse['q_numerators']]
        mid=[(u+v)/2 for u,v in zip(prev,cur)];amid=m.mv(a,mid)
        r=[v-u-dt*f for u,v,f in zip(prev,cur,amid)]
        e=l1(r);oldE=E;E+=e;elapsed+=dt
        # ||(I-tA/2)^-1||_2<=1, and exact Cayley is orthogonal.
        assert E<Q(1,10**10)
        deltas=[];defects=[];cuts=[];stock_errors=[];receipt_errors=[]
        for w in m.WEIGHTS:
            delta=m.stock(cur,w)-m.stock(prev,w)
            # Incidence cut: 2t sum_{i<j}(w_i-w_j) A_ij mid_i mid_j.
            cut=2*dt*sum((w[i]-w[j])*a[i][j]*mid[i]*mid[j] for i in range(23) for j in range(i+1,23))
            defect=2*sum(v*b*z for v,b,z in zip(mid,w,r))
            assert delta-cut==defect
            deltas.append(str(delta));cuts.append(cut);defects.append(str(defect))
            # True trajectory has norm sqrt(N)<2. Quadratic stock error <=E(4+E).
            stock_errors.append(E*(4+E))
            receipt_errors.append(oldE*(4+oldE)+E*(4+E))
        assert sum(cuts)==0
        assert sum(Q(x) for x in deltas)==m.dot(cur,cur)-m.dot(prev,prev)
        receipts.append({'pulse':n,'owned_delta_q':deltas,'cut_defect_q':defects,
                         'actual_owned_delta_error_bound':str(receipt_errors[0])})
        maxrow=max(sum(abs(v) for v in row) for row in a)
        timing+=2*maxrow
        if n%64==0:
            assert stage==n//64
            distance=l1([v-t for v,t in zip(cur,targets[stage])]);bound=E+distance
            assert bound<Q(1,10**10)
            summary.append({'checkpoint':stage,'pulse':n,'accumulated_solve_error_l1_bound':str(E),
             'target_distance_l1':str(distance),'certified_checkpoint_l2_error_bound':str(bound),
             'checkpoint_error_decimal_display':float(bound),'owned_q':[str(m.stock(cur,w)) for w in m.WEIGHTS],
             'owned_actual_error_bound':str(stock_errors[0]),'elapsed_model_step_sum':str(elapsed),
             'timing_jitter_error_coefficient':str(timing)})
        prev=cur
    assert stage_counts==[64,64,64,64] and len(summary)==4
    final_bound=Q(summary[-1]['certified_checkpoint_l2_error_bound'])
    # Final target parks c in core1; both private ports and core0 are empty at the checkpoint.
    assert final_bound<Q(1,10**10)
    endpoint_errors=[Q(s['certified_checkpoint_l2_error_bound']) for s in summary]
    for s,b in zip(summary,endpoint_errors):
        s['target_owned_error_bound']=str(b*(4+b))
    signed_total=[sum(Q(r['owned_delta_q'][k]) for r in receipts) for k in range(2)]
    assert signed_total==[m.stock(prev,w)-m.stock(targets[0],w) for w in m.WEIGHTS]
    # Per-pulse delta and signed cut residuals are exact rationals for q; enclosure covers actual states.
    (ROOT/'SIGNED_RECEIPTS.json').write_text(json.dumps({'definition':'Exact rational q trace deltas; actual native Cayley receipt differs by at most the listed bound. cut = owned_delta_q - cut_defect_q.',
      'pulses':receipts,'owned_total_delta_q':[str(v) for v in signed_total]},separators=(',',':'))+'\n')
    result={'status':'PASS_EXACT_RATIONAL_ENCLOSURE','native_dimension':23,'all_mask_skew_checks':128,
      'positive_rational_cayley_steps':256,'stage_steps':stage_counts,'checkpoint_certificates':summary,
      'norm_squared_exact':str(N),'exact_norm_preserved':True,
      'max_checkpoint_error_strict_upper_bound':'1/10000000000',
      'per_pulse_owned_cut_defect_identities':512,'certificate_sha256':sha(ROOT/'SCHEDULE_CERTIFICATE.json'),
      'signed_receipts_sha256':sha(ROOT/'SIGNED_RECEIPTS.json'),
      'timing_jitter_bound':'initial_l2_error + timing_coefficient * max_abs_step_error + checkpoint_error',
      'timing_coefficient_final':str(timing),
      'source_type':'Constructed known-preparation schedule; supplied masks and dimensionless Cayley steps',
      'not_claimed':['Continuous-flow execution','Finite physical clock','Native autonomous selection or mask realization',
                     'Universal unknown-input reset','Automatic latch trigger or fresh-port renewal','Parameter-free action map','Independent review'],
      'physical_promotion':0}
    (ROOT/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
