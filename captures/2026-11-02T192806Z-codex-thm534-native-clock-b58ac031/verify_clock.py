"""Exact native-clock controls; Python standard library only."""
import sys
sys.dont_write_bytecode=True
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
from native_model import B, N, native, mv, dot, SIMP, WEIGHTS

def unit(i):
    x=[Q(0)]*N;x[i]=Q(1);return x
def lin(a,x,b,y):return [a*v+b*w for v,w in zip(x,y)]
def read(x):
    return [x[3],sum(B[0][3][j]*x[5+j] for j in range(9))/3]
def rank(rows):
    a=[list(map(Q,r)) for r in rows];k=0
    for j in range(len(a[0])):
        p=next((i for i in range(k,len(a)) if a[i][j]),None)
        if p is None:continue
        a[k],a[p]=a[p],a[k];v=a[k][j];a[k]=[x/v for x in a[k]]
        for i in range(len(a)):
            if i!=k:
                v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[k])]
        k+=1
    return k
def cayley(a,b,t):
    den=1+3*t*t/4
    c=(1-3*t*t/4)/den;s=t/den
    return [c*a-3*s*b,s*a+c*b]

w=lin(1,unit(3),-1,unit(4))
D=native([0]*7);d=mv(D,w)
assert dot(w,w)==2 and dot(d,d)==6 and dot(w,d)==0
assert mv(D,d)==[-3*v for v in w]
active=[]
for j in range(5):
    z=[Q(0)]*N
    for i in range(9):z[5+i]=B[1][i][j]
    active.append(z)
active += [unit(i) for i in range(14,23)]
assert rank(active)==14
assert read(w)==[1,0] and read(d)==[0,1]
assert all(read(z)==[0,0] for z in active)
R=[unit(3),[Q(0)]*N]
for j in range(9):R[1][5+j]=B[0][3][j]/3
assert dot(R[0],R[0])==1 and dot(R[1],R[1])==Q(1,3)
assert dot(R[0],R[1])==0
# After scaling the second readout by sqrt(3), both rows are orthonormal.
mask_checks=0;hold_checks=0;owned_checks=0
n=[Q(0)]*N
for i in range(7):n[14+i]=B[2][i][1]
q=unit(22)
for mask in product((0,1),repeat=7):
    A=native(mask)
    assert mv(A,w)==d and mv(A,d)==[-3*v for v in w]
    for z in active:
        az=mv(A,z)
        assert read(az)==[0,0]
    assert all(A[i][j]==-A[j][i] for i in range(N) for j in range(N))
    mask_checks+=1
    if all(mask[i]==0 for i in (0,2,4,6)):
        assert mv(A,n)==[0]*N and mv(A,q)==[0]*N
        # No such hold mask parks a nonzero clock: speed norm = 3 * clock norm.
        for a,b in ((Q(1),Q(0)),(Q(0),Q(1)),(Q(2,3),Q(-4,5))):
            c=lin(a,w,b,d);v=mv(A,c)
            assert dot(v,v)==3*dot(c,c)>0
        hold_checks+=1
for weights in WEIGHTS:
    assert dot([v*t for v,t in zip(w,weights)],w)==1
    assert dot([v*t for v,t in zip(d,weights)],d)==3
    assert dot([v*t for v,t in zip(w,weights)],d)==0
    for z in active:
        assert dot([v*t for v,t in zip(w,weights)],z)==0
        assert dot([v*t for v,t in zip(d,weights)],z)==0
        owned_checks+=2

# Local clock closure fails outside the stated preparation sector.
bad=unit(0)
assert read(bad)==[0,0] and read(mv(D,bad))==[0,Q(-1,3)]

# Exact clock-mode Cayley residual in the original 23 coordinates.
cayley_checks=0
for mask in product((0,1),repeat=7):
    A=native(mask)
    for t in (Q(1,7),Q(1,2),Q(1),Q(4)):
        a,b=Q(2,3),Q(-1,5);a1,b1=cayley(a,b,t)
        c=lin(a,w,b,d);c1=lin(a1,w,b1,d)
        residual=lin(1,c1,-1,c)
        amid=mv(A,lin(Q(1,2),c1,Q(1,2),c))
        assert residual==[t*v for v in amid]
        assert a1*a1+3*b1*b1==a*a+3*b*b
        cayley_checks+=1
one=cayley(Q(1),Q(0),Q(1))
half=cayley(*cayley(Q(1),Q(0),Q(1,2)),Q(1,2))
assert one==[Q(1,7),Q(4,7)]
assert half==[Q(-23,361),Q(208,361)] and one!=half

# At a strict rational peak q, the active switch differential is rank 13.
# Same prepared clock at every input: common-T clock derivative is zero.
A=native([1]*7);H=native([0,1,0,1,0,1,0])
f=mv(A,q);g=mv(H,q);speed=dot(n,f)
assert speed==-4 and dot(n,g)==0
Scols=[lin(1,z,dot(n,z)/speed,lin(1,g,-1,f)) for z in active]
assert rank(Scols)==13
kernel=lin(1,f,-1,g)
assert dot(kernel,kernel)>0 and read(kernel)==[0,0]
assert lin(1,kernel,dot(n,kernel)/speed,lin(1,g,-1,f))==[0]*N
# Event clock tangent D*c is nonzero and restores this direction.
assert dot(d,d)>0
augmented=[]
for z,scol in zip(active,Scols):
    dt=-dot(n,z)/speed
    augmented.append(scol+[dt]) # one nonzero clock tangent suffices locally
assert rank(augmented)==14

# Revised local guard beta_1 + v_4 = 0. At q + b*d with b=1/3,
# the incoming/outgoing normal speeds are -3 and 1: determinant -1/3.
normal=lin(1,n,1,unit(4))
zg=lin(1,q,Q(1,3),d)
assert dot(normal,zg)==0
incoming=mv(A,zg);outgoing=mv(H,zg)
assert dot(normal,incoming)==-3 and dot(normal,outgoing)==1
saltation=[]
for j in range(N):
    z=unit(j)
    saltation.append(lin(1,z,dot(normal,z)/dot(normal,incoming),
                         lin(1,outgoing,-1,incoming)))
assert rank(saltation)==23
assert 1+dot(normal,lin(1,outgoing,-1,incoming))/dot(normal,incoming)==Q(-1,3)
# Both private-star readouts recover the same clock coordinates.
def read4(x):
    return [-x[4],-sum(B[0][4][j]*x[5+j] for j in range(9))/3]
assert read4(w)==[1,0] and read4(d)==[0,1]
assert all(read4(z)==[0,0] for z in active)
# The guard stores a(clock_event) in beta_1; an exact rational event-family.
# Choose a(clock)=a, arbitrary rational b>0, and event active q + (a/4)*n.
# Then beta_1=a. All 8 holding masks freeze it and the core exactly.
guard_cases=0
for a in (Q(-1,10),Q(0),Q(1,10)):
    for b in (Q(1,5),Q(1,3),Q(2,5)):
        event=lin(1,lin(1,q,a/4,n),1,lin(a,w,b,d))
        assert dot(normal,event)==0
        fm=mv(A,event)
        assert dot(normal,fm)==-4+3*b<0
        for mask in product((0,1),repeat=7):
            if not all(mask[i]==0 for i in (0,2,4,6)):continue
            fh=mv(native(mask),event)
            assert dot(n,fh)==0 and dot(q,fh)==0
            assert dot(normal,fh)==3*b>0
            # Saltation determinant is nonzero; no tangent guard after capture.
            assert dot(normal,fh)/dot(normal,fm)!=0
            guard_cases+=1
result={
 "status":"PASS","arithmetic":"fractions.Fraction; no numerical solver",
 "mask_mode_and_active_readout_checks":mask_checks,
 "native_cayley_clock_checks":cayley_checks,
 "holding_masks_no_clock_freeze":hold_checks,
 "cell_owned_cross_term_checks":owned_checks,
 "clock_plane_norm":"2*a^2+6*b^2",
 "each_cell_clock_owned_stock":"a^2+3*b^2",
 "active_peak_common_time_rank":13,"active_event_plus_clock_rank":14,
 "revised_guard_full_carrier_rank":23,
 "revised_guard_rational_determinant":"-1/3",
 "revised_guard_event_hold_controls":guard_cases,
 "revised_guard_local_support":["vertex 4","face 012","face 014","face 024","face 124"],
 "local_readout_support":["vertex 3","edge 03","edge 13","edge 23"],
 "equal_parameter_sum_partition_control":{"one_step":list(map(str,one)),"two_steps":list(map(str,half))},
 "preparation_contamination_counterexample":"vertex 0: readout (0,0), derivative (0,-1/3)",
 "physical_promotion":0,
 "scope":"Exact finite matrix controls support the analytic proof; constructor verification only."
}
text=json.dumps(result,indent=2,sort_keys=True)+"\n"
Path(__file__).with_name("RESULTS.json").write_text(text)
print(text,end="")
