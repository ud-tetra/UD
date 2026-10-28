#!/usr/bin/env python3
"""Certify a full active-sector writer using exact rational residuals.

Deterministic integer elimination only proposes grid matrices.
Every proposal is checked against the exact rational native midpoint equations.
"""
from fractions import Fraction as Q
from pathlib import Path
from itertools import product
import json,hashlib
import native_model as m
ROOT=Path(__file__).resolve().parent
N=23;K=14;GRID=10**15
def transpose(a):return list(map(list,zip(*a)))
def mul(a,b):
    out=[[Q(0)]*len(b[0]) for _ in a]
    for i,row in enumerate(a):
        for k,v in enumerate(row):
            if v:
                for j,w in enumerate(b[k]):
                    if w:out[i][j]+=v*w
    return out
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
def inverse(a):
    n=len(a);rows=[r.copy()+[Q(i==j) for j in range(n)] for i,r in enumerate(a)]
    for k in range(n):
        p=next(i for i in range(k,n) if rows[i][k]);rows[k],rows[p]=rows[p],rows[k]
        z=rows[k][k];rows[k]=[v/z for v in rows[k]]
        for i in range(n):
            if i!=k and rows[i][k]:
                z=rows[i][k];rows[i]=[v-z*w for v,w in zip(rows[i],rows[k])]
    return [r[n:] for r in rows]
def basis():
    columns=[[m.B[1][i][f] for i in range(9)] for f in range(7)]
    chosen=[]
    for f,v in enumerate(columns):
        if rank([columns[j] for j in chosen]+[v])>len(chosen):chosen.append(f)
    assert chosen==[0,1,2,3,4]
    cols=[[Q(0)]*5+columns[f]+[Q(0)]*9 for f in chosen]
    cols += [[Q(i==j) for i in range(23)] for j in range(14,23)]
    return transpose(cols),chosen
def round_div(num,den):
    if den<0:num=-num;den=-den
    assert den>0
    whole,rem=divmod(num,den)
    return whole+int(2*rem>den or (2*rem==den and whole%2))
def proposal(a,t,previous):
    # Deterministic fixed-point elimination proposes a rational-grid matrix.
    # Its accuracy is not assumed: exact residual inequalities certify it.
    precision=10**30;tn=t.numerator;td=t.denominator
    old=[[int(v*GRID) for v in row] for row in previous]
    assert all(Q(old[i][j],GRID)==previous[i][j] for i in range(N) for j in range(K))
    ai=[[int(v) for v in row] for row in a]
    rows=[]
    for i in range(N):
        lhs=[round_div((2*td*int(i==j)-tn*ai[i][j])*precision,2*td) for j in range(N)]
        rhs=[round_div((2*td*old[i][j]+tn*sum(ai[i][k]*old[k][j] for k in range(N)))*precision,2*td*GRID) for j in range(K)]
        rows.append(lhs+rhs)
    for k in range(N):
        p=max(range(k,N),key=lambda i:abs(rows[i][k]));rows[k],rows[p]=rows[p],rows[k]
        pivot=rows[k][k];assert pivot!=0
        rows[k]=[round_div(v*precision,pivot) for v in rows[k]]
        for i in range(N):
            if i!=k:
                z=rows[i][k]
                if z:rows[i]=[v-round_div(z*w,precision) for v,w in zip(rows[i],rows[k])]
    return [[Q(round_div(v*GRID,precision),GRID) for v in r[N:]] for r in rows]
def floor_box(x,den=10**15):
    return [str(Q((x.numerator*den)//x.denominator,den)),
            str(Q(-((-x.numerator*den)//x.denominator),den))]
def l1(a):return sum(abs(v) for row in a for v in row)
def main():
    data=json.loads((ROOT/'WRITER_SCHEDULES.json').read_text())
    assert len(data['programs'])==2
    V,chosen=basis();assert rank(transpose(V))==14
    gram=mul(transpose(V),V);ginv=inverse(gram)
    condition=max(Q(1),max(sum(abs(v) for v in r) for r in ginv))
    assert mul(gram,ginv)==[[Q(i==j) for j in range(K)] for i in range(K)]
    # Orthogonal active projector: vertex zero, cycle edges, every face/core coordinate.
    active=mul(mul(V,ginv),transpose(V))
    assert mul(active,active)==active and active==transpose(active)
    matrices={}
    for h in product((0,1),repeat=7):
        a=m.native(h)
        assert all(a[i][j]==-a[j][i] for i in range(N) for j in range(N))
        assert max(sum(abs(v) for v in row) for row in a)==5
        assert mul(a,active)==mul(active,a)
        matrices[h]=a
    d0=m.native([0]*7)
    gradient_witnesses={3:[Q(0),Q(0),Q(0),Q(1),Q(-1)]+[Q(0)]*18,
                        5:[Q(1),Q(-1)]+[Q(0)]*21}
    for lam2,w in gradient_witnesses.items():
        dw=m.mv(d0,w)
        assert m.dot(w,w)==2 and m.dot(dw,dw)==2*lam2 and m.dot(w,dw)==0
        for a in matrices.values():
            assert m.mv(a,w)==dw
            assert m.mv(a,dw)==[-lam2*v for v in w]
    p=[Q(0)]*14+[r[1]/2 for r in m.B[2]]+[Q(0)]*2
    q=[Q(i==22) for i in range(N)]
    assert m.dot(p,p)==m.dot(q,q)==1 and m.dot(p,q)==0
    results=[];receipt_summary=[];bounds=[]
    for program in data['programs']:
        u=Q(program['u']);assert u in (Q(1,2),Q(-1,2))
        cos=(1-u*u)/(1+u*u);sin=2*u/(1+u*u)
        target=[[Q(i==j)+(cos-1)*(p[i]*p[j]+q[i]*q[j])+sin*(p[i]*q[j]-q[i]*p[j]) for j in range(N)] for i in range(N)]
        assert mul(transpose(target),target)==[[Q(i==j) for j in range(N)] for i in range(N)]
        TV=mul(target,V);prev=V;E=Q(0);total=Q(0);max_leak=Q(0);leak_at=0
        initial_q=[r[-1] for r in V];signed=[Q(0),Q(0)];identities=0;max_receipt_err=Q(0)
        gradient={3:(Q(1),Q(0)),5:(Q(1),Q(0))}
        assert len(program['masks'])==len(program['parameter_numerators'])==160
        den=program['parameter_denominator'];assert den==10**12
        for n,(h,num) in enumerate(zip(program['masks'],program['parameter_numerators']),1):
            assert all(type(v)==int and v in (0,1) for v in h) and len(h)==7
            t=Q(num,den);assert 0<t<=4
            a=matrices[tuple(h)];cur=proposal(a,t,prev)
            middle=[[(x+y)/2 for x,y in zip(r,s)] for r,s in zip(prev,cur)]
            amid=mul(a,middle)
            residual=[[y-x-t*z for x,y,z in zip(r,s,b)] for r,s,b in zip(prev,cur,amid)]
            oldE=E;E+=l1(residual);total+=t
            assert E<Q(1,10**9)
            z0=[r[-1] for r in prev];z1=[r[-1] for r in cur]
            mid=[r[-1] for r in middle];res=[r[-1] for r in residual]
            for k,w in enumerate(m.WEIGHTS):
                delta=m.stock(z1,w)-m.stock(z0,w)
                cut=2*t*sum((w[i]-w[j])*a[i][j]*mid[i]*mid[j] for i in range(N) for j in range(i+1,N))
                defect=2*sum(x*y*z for x,y,z in zip(mid,w,res))
                assert delta-cut==defect
                signed[k]+=delta;identities+=1
            err=oldE*(2+oldE)+E*(2+E)
            max_receipt_err=max(max_receipt_err,err)
            outside=m.dot(z1,z1)-m.dot(p,z1)**2-m.dot(q,z1)**2
            assert outside>=0
            lower=max(Q(0),outside-E*(2+E))
            if lower>max_leak:max_leak=lower;leak_at=n
            for lam2,(alpha,beta) in list(gradient.items()):
                denominator=1+lam2*t*t/4
                ac=(1-lam2*t*t/4)/denominator;bc=t/denominator
                gradient[lam2]=(alpha*ac-lam2*beta*bc,alpha*bc+beta*ac)
            prev=cur
        mismatch=l1([[x-y for x,y in zip(r,s)] for r,s in zip(cur,TV)])
        epsilon=condition*(E+mismatch)
        assert epsilon<Q(1,10**9)
        assert max_leak>Q(99,100) # These programs do not isolate the record during writing.
        bounds.append(epsilon)
        qfinal=[r[-1] for r in cur]
        for k,w in enumerate(m.WEIGHTS):
            assert signed[k]==m.stock(qfinal,w)-m.stock(initial_q,w)
        gradout={}
        for lam2,(alpha,beta) in gradient.items():
            assert alpha*alpha+lam2*beta*beta==1
            # Unit gradient witness: squared distance to identity = 2(1-alpha).
            deviation=2*(1-alpha)
            gradout[str(lam2)]={'cosine_interval':floor_box(alpha),'unit_witness_identity_error_squared_interval':floor_box(deviation)}
        assert any(2*(1-alpha)>Q(1,100) for alpha,beta in gradient.values())
        target_q=m.mv(target,q)
        target_owned=[m.stock(target_q,w) for w in m.WEIGHTS]
        assert target_owned==[Q(2,25),Q(23,25)]
        for w,stock_target in zip(m.WEIGHTS,target_owned):
            assert abs(m.stock(qfinal,w)-stock_target)<=mismatch*(2+mismatch)
        receipt_summary.append({'u':str(u),'input':'q=e_core1, exact unit norm',
          'signed_owned_delta_q':[str(v) for v in signed],
          'ideal_target_owned_stocks':[str(v) for v in target_owned],
          'actual_to_ideal_owned_stock_error_bound':str(epsilon*(2+epsilon)),
          'actual_final_stock_error_bound':str(E*(2+E)),
          'per_step_owned_error_max_bound':str(max_receipt_err),
          'exact_trace_cut_defect_identities':identities,
          'interpretation':'Rational proposal trace signed changes; actual unitary trajectory enclosed by residual bounds.'})
        results.append({'u':str(u),'positive_rational_steps':160,
          'sum_cayley_parameters':str(total),'rational_residual_frobenius_bound':str(E),
          'rational_final_basis_mismatch_l1':str(mismatch),
          'certified_active_operator_2_norm_error_bound':str(epsilon),
          'operator_error_decimal_display':float(epsilon),
          'intermediate_outside_record_plane_stock_lower_bound':str(max_leak),
          'intermediate_leakage_decimal_display':float(max_leak),'leakage_witness_pulse':leak_at,
          'gradient_identity_counterexamples':gradout})
    assert {r['u'] for r in results}=={'1/2','-1/2'}
    # Holding any isolating mask preserves both recorded coordinates exactly.
    holds=0
    for bits in product((0,1),repeat=3):
        h=[0,0,0,0,0,0,0]
        for f,v in zip([1,3,5],bits):h[f]=v
        a=m.native(h);assert m.mv(a,p)==m.mv(a,q)==[0]*N;holds+=1
    result={'status':'PASS_EXACT_RESIDUAL_CERTIFIED_ACTIVE_OPERATOR_WRITES',
      'field_dimension':23,'certified_sector_dimension':14,'basis_edge_face_columns':chosen,
      'basis_condition_rational_multiplier':str(condition),'mask_invariance_controls':128,'gradient_modal_witness_controls':256,
      'programs':results,'write_then_unwrite_active_error_bound':str(sum(bounds)),
      'holding_mask_controls':holds,'uniform_step_parameter_error_coefficient_per_program':800,'exact_owned_cut_defect_identities':640,
      'scope':'Two fixed preprogrammed writer angles on the active sector; not clock generation or an arbitrary-angle native controller.',
      'not_claimed':['Identity on the uncontrolled gradient sector','Isolation during writing','Continuous-flow execution',
        'Generation or recovery of omitted event time','Autonomous programme or mode source','Unknown-receipt erasure/reset','Physical clock or action map'],
      'physical_promotion':0}
    (ROOT/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    (ROOT/'SIGNED_RECEIPT_SUMMARY.json').write_text(json.dumps(receipt_summary,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
