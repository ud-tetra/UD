#!/usr/bin/env python3
"""Exact field-map rank, receipt capacity and native write-obstruction audit."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
from math import isqrt
import json,hashlib
import native_model as m
from exact_intervals import I,sqrt_q,atan_small,sin_i,box
ROOT=Path(__file__).resolve().parent
N=23
def eye():return [[Q(i==j) for j in range(N)] for i in range(N)]
def outer(a,b):return [[x*y for y in b] for x in a]
def add(a,b,scale=Q(1)):return [[x+scale*y for x,y in zip(r,s)] for r,s in zip(a,b)]
def mul(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def trans(a):return list(map(list,zip(*a)))
def rank(rows):
    piv={}
    for row in rows:
        v=list(row)
        for p,r in sorted(piv.items()):
            if v[p]:
                z=v[p];v=[x-z*y for x,y in zip(v,r)]
        p=next((i for i,x in enumerate(v) if x),None)
        if p is not None:
            z=v[p];piv[p]=[x/z for x in v]
    return len(piv)
def det(a):
    a=[r.copy() for r in a];value=Q(1)
    for k in range(len(a)):
        p=next((i for i in range(k,len(a)) if a[i][k]),None)
        if p is None:return Q(0)
        if p!=k:a[p],a[k]=a[k],a[p];value=-value
        pivot=a[k][k];value*=pivot
        for i in range(k+1,len(a)):
            z=a[i][k]/pivot
            if z:
                for j in range(k+1,len(a)):a[i][j]-=z*a[k][j]
                a[i][k]=Q(0)
    return value
def state(seed):
    return [Q(((i+1)*(seed+3))%17-8,11) for i in range(N)]
def matrix_hash(a):
    return hashlib.sha256(json.dumps([[str(v) for v in r] for r in a],separators=(',',':')).encode()).hexdigest()
def main():
    load=m.native([1]*7);hold_mask=[0,1,0,1,0,1,0];hold=m.native(hold_mask)
    q=[Q(i==22) for i in range(N)]
    p=[Q(0)]*14+[row[1]/2 for row in m.B[2]]+[Q(0)]*2
    n=[2*v for v in p]
    n0=[Q(0)]*14+[row[0] for row in m.B[2]]+[Q(0)]*2
    assert m.dot(p,p)==m.dot(q,q)==1 and m.dot(p,q)==0
    guard_cases=0;augmented_cases=0
    for bits in product((0,1),repeat=3):
        h=hold_mask.copy()
        for f,v in zip([1,3,5],bits):h[f]=v
        b=m.native(h)
        assert m.mv(b,p)==m.mv(b,q)==[0]*N
        assert m.mv(trans(b),n)==[0]*N
        for seed in range(8):
            z=state(seed)
            beta=m.dot(n,z);z=[v-beta*w/4 for v,w in zip(z,n)]
            z[22]=1+Q(seed%3,3);z[21]=Q((seed%5)-2,3)
            fm=m.mv(load,z);fp=m.mv(b,z);d=m.dot(n,fm)
            assert m.dot(n,z)==0 and d==z[21]-4*z[22]<0
            assert m.dot(n,fp)==0
            diff=[u-v for u,v in zip(fm,fp)]
            salt=add(eye(),outer([v-u for u,v in zip(fm,fp)],n),1/d)
            assert rank(salt)==22
            assert m.mv(salt,diff)==[0]*N
            assert m.mv(trans(salt),n)==[0]*N
            assert m.dot(z,diff)==0
            event=add(eye(),outer(fm,n),-1/d)
            assert rank(event)==22 and m.mv(event,fm)==[0]*N
            augmented=event+[[-v/d for v in n]]
            assert rank(augmented)==23
            guard_cases+=1;augmented_cases+=1
    # At z=e_core1, the saltation matrix is an exact rank-22 orthogonal projector.
    z=q.copy();fm=m.mv(load,z);fp=m.mv(hold,z);d=m.dot(n,fm)
    salt=add(eye(),outer([v-u for u,v in zip(fm,fp)],n),1/d)
    projector=add(eye(),outer(n,n),Q(-1,4))
    assert salt==projector and mul(salt,salt)==salt and trans(salt)==salt and det(salt)==0
    assert rank(hold)==20
    uniform=[Q(i<5) for i in range(N)]
    assert rank([uniform,p,q])==3
    assert m.mv(hold,uniform)==[0]*N
    # A native neighboring-core peak guard is transverse after the same hold switch.
    z=[Q(0)]*N;z[21]=1;z[22]=2
    fm=m.mv(load,z);fp=m.mv(hold,z);dm=m.dot(n0,fm);dp=m.dot(n0,fp)
    assert m.dot(n0,z)==0 and dm==-2 and dp==-3
    neighbor=add(eye(),outer([v-u for u,v in zip(fm,fp)],n0),1/dm)
    assert rank(neighbor)==23 and det(neighbor)==Q(3,2)
    # Native plane has storage capacity, but its pure write generator breaks the shared-star constraint.
    writer=add(outer(p,q),outer(q,p),Q(-1))
    assert m.mv(writer,q)==p and m.mv(writer,p)==[-v for v in q]
    assert trans(writer)==[[-v for v in r] for r in writer]
    def shared_constraint(a):return a[14][21]+a[14][22]
    for h in product((0,1),repeat=7):assert shared_constraint(m.native(h))==0
    assert shared_constraint(writer)==Q(1,2)
    # Rational phase receipts and exact inverse in the existing protected plane.
    code_cases=0
    for seed in range(3):
        z=state(seed)
        beta=m.dot(p,z);z=[v-beta*w for v,w in zip(z,p)]
        oldq=m.dot(q,z);r=Q(seed+1,2);z=[v+(r-oldq)*w for v,w in zip(z,q)]
        complement=[v-r*w for v,w in zip(z,q)]
        for j in range(17):
            tau=Q(79,100)+Q(j,1600);omega=Q(1)
            u=omega*tau;cos=(1-u*u)/(1+u*u);sin=2*u/(1+u*u)
            y=[v+r*(cos*a+sin*b) for v,a,b in zip(complement,q,p)]
            a=m.dot(q,y);b=m.dot(p,y);radius2=a*a+b*b
            rn=isqrt(radius2.numerator);rd=isqrt(radius2.denominator)
            assert rn*rn==radius2.numerator and rd*rd==radius2.denominator
            radius=Q(rn,rd);recovered_tau=b/(omega*(radius+a))
            recovered_z=[v-a*s-b*t+radius*s for v,s,t in zip(y,q,p)]
            assert recovered_tau==tau and recovered_z==z and m.dot(y,y)==m.dot(z,z)
            assert a*a+b*b==r*r
            code_cases+=1
    # Fixed positive-radius external record alternative: two amplitudes preserve norm and encode phase.
    codes=[]
    for j in range(33):
        tau=Q(j,32);u=tau
        code=((1-u*u)/(1+u*u),2*u/(1+u*u))
        assert code[0]*code[0]+code[1]*code[1]==1
        assert code[1]/(1+code[0])==tau
        codes.append(code)
    assert len(set(codes))==33
    # Analytic canonical neighboring-peak comparison, using rational enclosures.
    a=sqrt_q(3);b=sqrt_q(5)
    pi=16*atan_small(Q(1,5),24)-4*atan_small(Q(1,239),6)
    tn=2*pi/(a+b)
    c0=(sin_i(a*tn)/a-sin_i(b*tn)/b)/2
    c1=(sin_i(a*tn)/a+sin_i(b*tn)/b)/2
    ratio=(3*c0)/(4*c0-c1)
    assert Q(3,4)<ratio.lo<ratio.hi<Q(4,5)
    squared=ratio*ratio;assert squared.lo<Q(3,5)<squared.hi
    retained=c1*c1;assert 0<retained.lo<retained.hi<Q(1,1000)
    out={'status':'PASS_EXACT_EVENT_INFORMATION_AND_NATIVE_CLOCK_CAPACITY_AUDIT',
      'field_dimension':23,'peak_saltation_rank':22,'peak_saltation_determinant':0,
      'transverse_peak_and_hold_cases':guard_cases,'augmented_event_plus_time_full_rank_cases':augmented_cases,
      'simple_projector_sha256':matrix_hash(salt),'hold_kernel_dimension':3,
      'hold_active_protected_plane_dimension':2,
      'protected_plane_coordinates':'q=c1; p=beta1/2',
      'clock_writer_native_shared_constraint_violation':str(shared_constraint(writer)),
      'writer_status':'Not in instantaneous linear span of native masks; finite controlled compilation not ruled out.',
      'native_plane_clock_encode_decode_cases':code_cases,
      'external_unit_radius_phase_code_cases':len(codes),
      'unchanged_field_map_record_bound':'At least one continuous event-time coordinate; finite alphabet insufficient on an open phase family.',
      'separate_euclidean_record_bound':'Zero prepared stock stores no receipt; one fixed-norm real amplitude gives only two values; two prepared amplitudes suffice kinematically.',
      'neighbor_guard_rational_witness_saltation_determinant':'3/2',
      'canonical_neighbor_event_parameter_interval':box(tn),
      'canonical_neighbor_saltation_determinant_exact':'sqrt(3/5)',
      'canonical_neighbor_saltation_determinant_interval':box(ratio),
      'canonical_neighbor_capture_stock_over_feed_stock_interval':box(retained),
      'source_scope':'Continuous event-triggered capture. Fixed-parameter Cayley loading remains injective on its prepared mode slice.',
      'remaining':['Native clock generation and writing law','Output observable selection','Full reversible controller/mode and reset','Capture quality versus retained information','Geometric gate realization and physical action map'],
      'physical_promotion':0}
    (ROOT/'RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
