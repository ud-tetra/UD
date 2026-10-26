#!/usr/bin/env python3
"""Exact native stopping, core-isolation and local observation audit."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
import native_model as m
ROOT=Path(__file__).resolve().parent
def rank(rows):
    piv={}
    for row in rows:
        v=list(row)
        for p,r in sorted(piv.items()):
            if v[p]:
                a=v[p];v=[x-a*y for x,y in zip(v,r)]
        p=next((i for i,x in enumerate(v) if x),None)
        if p is not None:
            a=v[p];piv[p]=[x/a for x in v]
    return len(piv)
def solve(a,b):
    rows=[list(r)+[v] for r,v in zip(a,b)]
    for k in range(len(b)):
        p=next(i for i in range(k,len(b)) if rows[i][k])
        rows[k],rows[p]=rows[p],rows[k]
        z=rows[k][k];rows[k]=[v/z for v in rows[k]]
        for i in range(len(b)):
            if i!=k and rows[i][k]:
                z=rows[i][k];rows[i]=[x-z*y for x,y in zip(rows[i],rows[k])]
    return [r[-1] for r in rows]
def cayley(a,t,x):
    mat=[[Q(i==j)-t*a[i][j]/2 for j in range(23)] for i in range(23)]
    ax=m.mv(a,x)
    return solve(mat,[v+t*w/2 for v,w in zip(x,ax)])
def main():
    xs=m.checkpoints();c=Q(24,37);old=xs[3]
    parked=xs[0].copy();parked[16]=0;parked[22]=c
    incident=[f for f,row in enumerate(m.B[2]) if row[1]]
    assert incident==[0,2,4,6]
    good=[];speeds=[];base=m.native([0]*7)
    for h in product((0,1),repeat=7):
        a=m.native(h)
        speed=m.mv(a,old);s=m.dot(speed,speed);speeds.append(s)
        assert s==Q(22263,1369)+h[4]*c*c
        assert speed[18]==1
        row_zero=all(v==0 for v in a[22])
        assert row_zero==all(h[f]==0 for f in incident)
        if row_zero:good.append(h)
        assert max(sum(abs(v) for v in r) for r in a)==5
    assert len(good)==8 and min(speeds)>16
    a0rank=rank(base);assert a0rank==18
    rows=base.copy()
    for f in range(7):
        a=m.native([int(f==j) for j in range(7)])
        rows.extend([[x-y for x,y in zip(r,s)] for r,s in zip(a,base)])
    assert rank(rows)==22
    uniform=[Q(i<5) for i in range(23)]
    assert all(m.mv(m.native(h),uniform)==[0]*23 for h in product((0,1),repeat=7))
    exact_hold_controls=0
    for h in good:
        a=m.native(h)
        for t in [Q(1,4),Q(1),Q(3)]:
            for j in range(3):
                x=[Q(((i+1)*(j+2))%11-5,7) for i in range(23)]
                y=cayley(a,t,x)
                assert y[22]==x[22] and m.dot(y,y)==m.dot(x,x)
                exact_hold_controls+=1
    assert exact_hold_controls==72
    reopen_controls=0
    for f in incident:
        h=[0]*7;h[f]=1
        x=[Q(0)]*23;x[14+f]=1
        y=cayley(m.native(h),Q(1),x)
        assert y[22]!=0
        reopen_controls+=1
    # A concrete all-off positive step does not retain the old face-output state.
    one=cayley(base,Q(1),old)
    assert one!=old and one[18]!=old[18]
    # Selected core output is invariant, while the restored worker is not stationary.
    apark=m.mv(base,parked);assert apark[22]==0 and any(apark)
    pnext=cayley(base,Q(1),parked)
    assert pnext[22]==c and pnext!=parked
    # Exact endpoint observation alias on all 15 coordinates of the first tetrahedron.
    worker=[m.OFF[k]+i for k,ss in enumerate(m.SIMP) for i,s in enumerate(ss) if set(s)<=set(m.CELLS[0])]
    assert len(worker)==15
    assert [xs[0][i] for i in worker]==[old[i] for i in worker]==[parked[i] for i in worker]
    data=json.loads((ROOT/'SCHEDULE_CERTIFICATE.json').read_text())
    results=json.loads((ROOT/'RESULTS.json').read_text())
    bound=Q(results['checkpoint_certificates'][-1]['certified_checkpoint_l2_error_bound'])
    assert bound<Q(1,10**10)
    # A naive 'core nonzero => close its four gates' fires after the FIRST pulse.
    pulse=data['steps'][0];t=Q(pulse['t']);a=m.native(pulse['mask'])
    q=[Q(v,data['trace_denominator']) for v in pulse['q_numerators']]
    mid=[(v+w)/2 for v,w in zip(xs[0],q)]
    r=[v-u-t*f for u,v,f in zip(xs[0],q,m.mv(a,mid))]
    e=sum(abs(v) for v in r)
    assert q[22]-e>Q(1,10) and q[22]+e<Q(13,100)
    assert q[22]+e<c
    out={'status':'PASS_EXACT_CONDITIONAL_NATIVE_CORE_LATCH','original_dimension':23,
      'output_core_index':22,'incident_face_indices':incident,
      'incident_faces':[m.SIMP[2][i] for i in incident],
      'all_mask_isolation_equivalence_controls':128,'isolating_masks':8,
      'finite_cayley_hold_and_norm_controls':exact_hold_controls,
      'single_gate_reopen_counterexamples':reopen_controls,
      'old_face_output_min_generator_speed_squared':str(min(speeds)),
      'old_face_output_instantaneous_derivative':1,
      'old_face_output_after_unit_alloff_cayley':str(one[18]),
      'alloff_kernel_dimension':23-a0rank,'allmask_common_kernel_dimension':1,
      'common_kernel':'uniform vertex amplitude only; orthogonal to nonzero active-sector states',
      'worker_local_observation_coordinates':worker,'ideal_start_end_alias':True,
      'parking_checkpoint_error_bound':str(bound),
      'parked_core_stock_target':'576/1369',
      'parked_core_target_stock_error_bound':str(bound*(2*c+bound)),
      'early_nonzero_trigger_core_interval':[str(q[22]-e),str(q[22]+e)],
      'gate_error_exposure_bound':'abs(core change) <= 2 * sum(t_n * count_open_incident_faces_n) at fixed total norm 4683/1369',
      'open':['Autonomous latch trigger and clock','Core/output role selection','Geometric mask realization','Output isolation while supplying future loading','Fresh feed and renewal'],
      'physical_promotion':0}
    (ROOT/'LATCH_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
