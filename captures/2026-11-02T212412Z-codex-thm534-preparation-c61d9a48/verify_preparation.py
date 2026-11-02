"""Exact rational interval certificate for a continuous native capture branch."""
import sys
sys.dont_write_bytecode=True
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
from itertools import product
import json
import native_model as m
from interval_exact import I,box,sqrt_q,sin_i,cos_i,atan_small
P=Path(__file__).resolve().parent
R=Q(1,1000);EPS=Q(1,10**6)
L=Q(79,100);U=Q(4,5)
EL=Q(1979,2500);EU=Q(39581,50000)
T=Q(1)
A=m.native([1]*7);H=m.native([0,1,0,1,0,1,0])
N=m.N
def unit(j):
    x=[Q(0)]*N;x[j]=Q(1);return x
def add(x,y):return [u+v for u,v in zip(x,y)]
def scale(a,x):return [a*v for v in x]
def imv(a,x):return [sum((v*x[j] for j,v in enumerate(row) if v),I(0)) for row in a]
def idot(x,y):return sum((u*v for u,v in zip(x,y)),I(0))
def square(x):
    if x.lo<=0<=x.hi:return I(0,max(x.lo*x.lo,x.hi*x.hi))
    return I(min(x.lo*x.lo,x.hi*x.hi),max(x.lo*x.lo,x.hi*x.hi))
def stock(x,w):return sum((square(v)*a for v,a in zip(x,w) if a),I(0))
def widen(x,e):return x+I(-e,e)
def out(x):return box(x,10**18)
def maxnorm(x):return max(max(abs(v.lo),abs(v.hi)) for v in x)
w=add(unit(3),scale(-1,unit(4)));d=m.mv(A,w)
f0=scale(-1,unit(16))
x0=add(f0,scale(R,w))
q=unit(22);n=[Q(0)]*N
for i in range(7):n[14+i]=m.B[2][i][1]
nu=add(n,unit(4))
assert m.dot(x0,x0)==1+2*R*R
assert m.dot(nu,x0)==1-R
assert all(m.WEIGHTS[0][j]+m.WEIGHTS[1][j]==1 for j in range(N))
assert m.dot(nu,nu)==5
assert m.dot(m.mv(A,nu),m.mv(A,nu))==20
assert m.mv(H,n)==[0]*N and m.mv(H,q)==[0]*N
assert m.dot(m.mv(H,nu),m.mv(H,nu))==3
assert all(sum(abs(v) for v in row)<=5 for row in A+H)
sqrt3=sqrt_q(3);sqrt5=sqrt_q(5)
def observables(t):
    u=sqrt3*t;v=sqrt5*t
    c0=(sin_i(u)/sqrt3-sin_i(v)/sqrt5)/2
    c1=(sin_i(u)/sqrt3+sin_i(v)/sqrt5)/2
    beta=(cos_i(u)+cos_i(v))/2
    bp=-(sqrt3*sin_i(u)+sqrt5*sin_i(v))/2
    ca=R*cos_i(u);cb=R*sin_i(u)/sqrt3
    return c0,c1,beta,bp,ca,cb
def guard(t):
    c0,c1,beta,bp,ca,cb=observables(t)
    return beta-ca,bp+3*cb,3*cb

# Global exclusion before L: beta decreases on [0,L], clock a <= R.
assert sqrt5.hi*U<3
assert observables(I(L))[2].lo>Q(3,1000)
assert Q(3,1000)-R-3*EPS>0
assert guard(I(EL))[0].lo>Q(1,100000)
assert guard(I(EU))[0].hi<Q(-1,50000)
assert guard(I(EL))[0].lo-3*EPS>0
assert guard(I(EU))[0].hi+3*EPS<0
slope_rows=[]
for j in range(20):
    t=I(L+(U-L)*Q(j,20),L+(U-L)*Q(j+1,20))
    g,gm,gp=guard(t)
    assert observables(t)[3].lo>-2
    assert gm.lo-5*EPS>-2 and gm.hi+5*EPS<Q(-19,10)
    assert gp.lo-2*EPS>Q(1,625)
    assert gp.hi+2*EPS<Q(1,500)
    slope_rows.append({"interval":[str(t.lo),str(t.hi)],"incoming":out(widen(gm,5*EPS)),"outgoing":out(widen(gp,2*EPS))})

# Certified nominal root; full-ball root stays in [EL,EU].
lo=EL;hi=EU
for _ in range(55):
    mid=(lo+hi)/2;g=guard(I(mid))[0]
    if g.lo>0:lo=mid
    elif g.hi<0:hi=mid
    else:break
assert hi-lo<Q(1,10**17)
nominal_root=I(lo,hi);event=I(EL,EU)
assert EPS*Q(30,19)<Q(1,500000)
assert L<EL<EU<U

# Exact spectral decomposition of the whole active input, not only core data.
a2=m.mv(A,m.mv(A,f0))
p3=scale(Q(1,2),add(a2,scale(5,f0)))
p5=add(f0,scale(-1,p3))
assert m.mv(A,m.mv(A,p3))==scale(-3,p3)
assert m.mv(A,m.mv(A,p5))==scale(-5,p5)
ap3=m.mv(A,p3);ap5=m.mv(A,p5)
def load(t):
    a=sqrt3*t;b=sqrt5*t
    ca=cos_i(a);cb=cos_i(b)
    sa=sin_i(a)/sqrt3;sb=sin_i(b)/sqrt5
    return [ca*p3[j]+cb*p5[j]+sa*ap3[j]+sb*ap5[j]+
            R*(cos_i(a)*w[j]+sin_i(a)/sqrt3*d[j]) for j in range(N)]
assert all(load(I(0))[j].lo<=x0[j]<=load(I(0))[j].hi for j in range(N))

# Post-capture Taylor enclosure for exp(H*s), with rigorous infinity-norm tail.
def exponential(a,x,s,degree,exp_upper):
    term=x;y=x
    for k in range(1,degree+1):
        term=[v*s/k for v in imv(a,term)]
        y=[a+b for a,b in zip(y,term)]
    z=5*s.hi
    assert 0<=z<=4
    # exp(1)<3; use exp(z)<9 for z<2, or <81 for z<=4.
    assert (z<2 and exp_upper>=9) or exp_upper>=81
    tail=maxnorm(x)*exp_upper*z**(degree+1)/factorial(degree+1)
    return [widen(v,tail) for v in y],tail

flow_controls=0
for t in (Q(0),L,EL,EU,U,(lo+hi)/2):
    spectral=load(I(t))
    taylor,error=exponential(A,list(map(I,x0)),I(t),56,81)
    for v,u in zip(spectral,taylor):
        assert max(v.lo,u.lo)<=min(v.hi,u.hi)
    direct=idot(list(map(I,nu)),spectral)
    reduced=guard(I(t))[0]
    assert max(direct.lo,reduced.lo)<=min(direct.hi,reduced.hi)
    flow_controls+=1

# Exact current polynomial equals derivative of original owned quadratic stock.
def polynomial(a,w):
    c={}
    for i in range(N):
        for j in range(N):
            if not a[i][j]:continue
            key=tuple(sorted((i,j)))
            c[key]=c.get(key,Q(0))+2*w[i]*a[i][j]
    return {k:v for k,v in c.items() if v}
def incidence(a,w):
    return {(i,j):2*(w[i]-w[j])*a[i][j] for i in range(N) for j in range(i+1,N) if (w[i]-w[j])*a[i][j]}
identity_cases=0;hold_cases=0
for mask in product((0,1),repeat=7):
    a=m.native(mask)
    for weights in m.WEIGHTS:
        assert polynomial(a,weights)==incidence(a,weights)
        identity_cases+=1
    if all(mask[j]==0 for j in (0,2,4,6)):
        assert m.mv(a,n)==m.mv(a,q)==[0]*N
        hold_cases+=1

at_event=load(event)
at_final,tail=exponential(H,at_event,I(T-EU,T-EL),32,9)
nomnorm=Q(1000001,1000000)
assert nomnorm*nomnorm>m.dot(x0,x0)
stock_error=(2*nomnorm+EPS)*EPS
initial_stock=[m.stock(x0,wgt) for wgt in m.WEIGHTS]
assert initial_stock==[R*R,1+R*R]
event_stock=[widen(stock(at_event,wgt),stock_error) for wgt in m.WEIGHTS]
final_stock=[widen(stock(at_final,wgt),stock_error) for wgt in m.WEIGHTS]
initial_errors=[(2*R+EPS)*EPS,stock_error]
initial_box=[widen(I(v),e) for v,e in zip(initial_stock,initial_errors)]
load_delta=[v-u for v,u in zip(event_stock,initial_box)]
hold_delta=[v-u for v,u in zip(final_stock,event_stock)]
total_delta=[v-u for v,u in zip(final_stock,initial_box)]
def antisymmetric_pair(pair):
    a,b=pair[0],-pair[1]
    c=I(max(a.lo,b.lo),min(a.hi,b.hi))
    return [c,-c]
load_delta=antisymmetric_pair(load_delta)
hold_delta=antisymmetric_pair(hold_delta)
total_delta=antisymmetric_pair(total_delta)
# Explicit signs are asserted only after their interval certificates pass.
assert load_delta[0].lo>0 and load_delta[1].hi<0
assert hold_delta[0].lo>0 and hold_delta[1].hi<0
assert total_delta[0].lo>0 and total_delta[1].hi<0

def flux(a,weights,x):
    return sum((coef*x[i]*x[j] for (i,j),coef in incidence(a,weights).items()),I(0))
# Bound errors of quadratic currents using ||W A - A W||_2 <= 10.
flux_error=10*(2*nomnorm+EPS)*EPS
before=[widen(flux(A,wgt,at_event),flux_error) for wgt in m.WEIGHTS]
after=[widen(flux(H,wgt,at_event),flux_error) for wgt in m.WEIGHTS]
before=antisymmetric_pair(before);after=antisymmetric_pair(after)
assert (before[0]+before[1]).lo<=0<=(before[0]+before[1]).hi
assert (after[0]+after[1]).lo<=0<=(after[0]+after[1]).hi
switch_jump=["0","0"]
# All switches are continuous in field, so stocks have exactly zero jump.

# Concrete peak comparison for the nominal loading preparation.
tangent=Q(1,5);twice=2*tangent/(1-tangent*tangent)
four=2*twice/(1-twice*twice)
assert (four-Q(1,239))/(1+four*Q(1,239))==1
pi=16*atan_small(Q(1,5),24)-4*atan_small(Q(1,239),6)
assert pi.lo>3 and pi.hi<Q(22,7)
star=pi/(sqrt3+sqrt5)
assert EU<star.lo
offset=star-nominal_root
assert offset.lo>Q(1,10000) and offset.hi<Q(11,100000)
# |beta'|<2, shift<11/100000: amplitude penalty < shift^2.
penalty_amplitude=Q(11,100000)**2
assert observables(star)[1].hi<Q(51,100)
penalty_stock=(Q(102,100)+penalty_amplitude)*penalty_amplitude
core=widen(observables(event)[1],EPS)
assert core.lo>Q(1,2)
retained_stock=square(core)
assert retained_stock.lo>Q(1,4)

# Output-noise inverse on the broad branch, for known common T=1.
SIGMA=Q(1,10**7)
assert Q(1,625)-2*SIGMA>Q(1,1000)
assert (EL-L)*Q(1,625)>3*SIGMA
assert (U-EU)*Q(1,625)>3*SIGMA

receipts={
 "status":"PASS","ownership":"Original Q177 equal-top-star weights",
 "initial_nominal_owned_stock":list(map(str,initial_stock)),
 "initial_full_ball_owned_stock":list(map(out,initial_box)),
 "event_owned_stock":list(map(out,event_stock)),
 "common_T_1_owned_stock":list(map(out,final_stock)),
 "signed_load_integral_receipts":list(map(out,load_delta)),
 "signed_hold_integral_receipts":list(map(out,hold_delta)),
 "signed_total_integral_receipts":list(map(out,total_delta)),
 "instantaneous_owned_rate_before_switch":list(map(out,before)),
 "instantaneous_owned_rate_after_switch":list(map(out,after)),
 "switch_stock_jump":switch_jump,
 "receipt_pair_constraint":"Delta O_1 = -Delta O_0 exactly; paired intervals are correlated",
 "rounded_receipt_table":{
     "load":[box(v,10**6) for v in load_delta],
     "hold":[box(v,10**6) for v in hold_delta],
     "total":[box(v,10**6) for v in total_delta]},
 "hold_matrix_exponential_tail_inf":str(tail),
 "quadratic_stock_perturbation_padding":str(stock_error),
 "quadratic_flux_perturbation_padding":str(flux_error),
 "interpretation":"Signed integrals certified by the exact native continuity identity and endpoint enclosures; no independent quadrature is claimed.",
 "physical_promotion":0}
(P/'SIGNED_CELL_RECEIPTS.json').write_text(json.dumps(receipts,indent=2,sort_keys=True)+"\n")
result={
 "status":"PASS_EXACT_CONDITIONAL","version":"THM-534 v2.26",
 "preparation":"-e_face014 + (1/1000)*(e_vertex3-e_vertex4) + eta",
 "full_23_dimensional_preparation_ball_radius":str(EPS),
 "nominal_norm_squared":str(m.dot(x0,x0)),
 "broad_branch":[str(L),str(U)],"first_event_interval":[str(EL),str(EU)],
 "nominal_event_interval":out(nominal_root),
 "incoming_guard_speed_open_interval":["-2","-19/10"],
 "outgoing_guard_speed_open_interval":["1/625","1/500"],
 "switch_determinant_open_interval":["-1/950","-1/1250"],
 "root_shift_bound_from_preparation":"30*||eta||/19",
 "retained_core_stock":out(retained_stock),
 "nominal_exact_peak_interval":out(star),"nominal_early_capture_offset":out(offset),
 "nominal_core_amplitude_penalty_upper":str(penalty_amplitude),
 "nominal_core_stock_penalty_upper":str(penalty_stock),
 "full_ball_core_stock_lower":"1/4",
 "output_noise_ball_radius":str(SIGMA),
 "full_output_inverse_time_error_bound":"3000*||readout_error||",
 "all_mask_signed_continuity_polynomial_checks":identity_cases,
 "independent_spectral_vs_Taylor_load_controls":flow_controls,
 "hold_invariant_masks":hold_cases,"branch_subintervals":len(slope_rows),
 "branch_slope_certificates":slope_rows,
 "open_dependencies":["clock preparation","sticky mode and ideal crossing detector","renewal/reset","physical correspondence"],
 "arithmetic":"Fraction outward intervals on grid 10^24; analytic trig remainders; no float solver",
 "physical_promotion":0}
(P/'RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
print(json.dumps({k:v for k,v in result.items() if k!="branch_slope_certificates"},indent=2,sort_keys=True))
