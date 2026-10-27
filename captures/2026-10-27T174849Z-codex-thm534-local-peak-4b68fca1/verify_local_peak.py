#!/usr/bin/env python3
"""Exact native observable identities and outward rational peak enclosures."""
from fractions import Fraction as Q
from math import isqrt,factorial
from itertools import product
from pathlib import Path
import json
import native_model as m
ROOT=Path(__file__).resolve().parent
GRID=10**24
def down(x):return Q((x.numerator*GRID)//x.denominator,GRID)
def up(x):return -down(-x)
class I:
    def __init__(self,a,b=None):
        self.lo=Q(a);self.hi=Q(a if b is None else b)
        assert self.lo<=self.hi
    def __add__(self,y):
        y=as_i(y);return I(down(self.lo+y.lo),up(self.hi+y.hi))
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,y):return self+-as_i(y)
    def __rsub__(self,y):return as_i(y)+-self
    def __mul__(self,y):
        y=as_i(y);a=[x*z for x in (self.lo,self.hi) for z in (y.lo,y.hi)]
        return I(down(min(a)),up(max(a)))
    __rmul__=__mul__
    def __truediv__(self,y):
        y=as_i(y);assert y.lo*y.hi>0
        return self*I(down(1/y.hi),up(1/y.lo))
    def __pow__(self,n):
        assert type(n)==int and n>=0
        r=I(1)
        for _ in range(n):r=r*self
        return r
def as_i(x):return x if isinstance(x,I) else I(x)
def sqrt_q(x):
    x=Q(x);assert x>=0
    s=isqrt((x.numerator*GRID*GRID)//x.denominator)
    return I(Q(s,GRID),Q(s+1,GRID))
def sqrt_i(x):return I(sqrt_q(x.lo).lo,sqrt_q(x.hi).hi)
def atan_small(q,n):
    q=Q(q);assert 0<q<1
    a=sum((-1)**j*q**(2*j+1)/Q(2*j+1) for j in range(n))
    b=a+(-1)**n*q**(2*n+1)/Q(2*n+1)
    return I(down(min(a,b)),up(max(a,b)))
def sin_i(x):
    x=as_i(x);r=I(0);n=14
    for j in range(n):r+=(-1)**j*(x**(2*j+1))/factorial(2*j+1)
    err=max(abs(x.lo),abs(x.hi))**(2*n+1)/factorial(2*n+1)
    return r+I(-err,err)
def cos_i(x):
    x=as_i(x);r=I(0);n=14
    for j in range(n):r+=(-1)**j*(x**(2*j))/factorial(2*j)
    err=max(abs(x.lo),abs(x.hi))**(2*n)/factorial(2*n)
    return r+I(-err,err)
def box(x,den=10**15):
    return [str(Q((x.lo.numerator*den)//x.lo.denominator,den)),
            str(Q(-((-x.hi.numerator*den)//x.hi.denominator),den))]
def matmul(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def tr(a):return list(map(list,zip(*a)))
def reduced_cayley(t,beta0,beta1):
    z=t*t;d=1+2*z+Q(15,16)*z*z
    u=1+z;v=z/4
    core=[t*(u*beta0+v*beta1)/d,t*(v*beta0+u*beta1)/d]
    beta=[2*(u*beta0+v*beta1)/d-beta0,2*(v*beta0+u*beta1)/d-beta1]
    return core+beta
def solve(a,b):
    a=[list(row)+[v] for row,v in zip(a,b)]
    for k in range(len(b)):
        p=next(i for i in range(k,len(b)) if a[i][k]);a[k],a[p]=a[p],a[k]
        z=a[k][k];a[k]=[v/z for v in a[k]]
        for i in range(len(b)):
            if i!=k and a[i][k]:
                z=a[i][k];a[i]=[v-z*w for v,w in zip(a[i],a[k])]
    return [row[-1] for row in a]
def main():
    b3=m.B[2];K=matmul(tr(b3),b3);assert K==[[4,-1],[-1,4]]
    assert matmul(m.B[1],b3)==[[0,0] for _ in range(9)]
    R=[[Q(i==j) for i in range(23)] for j in [21,22]]
    R += [[Q(0)]*14+[b3[f][j] for f in range(7)]+[Q(0)]*2 for j in range(2)]
    red=[[0,0,1,0],[0,0,0,1],[-4,1,0,0],[1,-4,0,0]]
    allon=m.native([1]*7)
    assert matmul(R,allon)==matmul(red,R)
    kinv=[[Q(4,15),Q(1,15)],[Q(1,15),Q(4,15)]]
    assert matmul(K,kinv)==[[1,0],[0,1]]
    projector=matmul(matmul(b3,kinv),tr(b3))
    assert matmul(projector,projector)==projector and projector==tr(projector)
    g=[[Q(0)]*4 for _ in range(4)]
    g[0][0]=g[1][1]=1
    for i in range(2):
        for j in range(2):g[2+i][2+j]=kinv[i][j]
    lhs=matmul(tr(red),g);rhs=matmul(g,red)
    assert all(lhs[i][j]+rhs[i][j]==0 for i in range(4) for j in range(4))
    assert projector[2][2]==Q(4,15)
    # Output-cell aggregate cancellation holds for every choice of the other three gates.
    incident=[0,2,4,6];free=[1,3,5]
    local=0;hold=0
    for bits in product((0,1),repeat=3):
        h=[1]*7
        for f,v in zip(free,bits):h[f]=v
        a=m.native(h)
        assert matmul([R[3]],a)==[[Q(i==21)-4*Q(i==22) for i in range(23)]]
        for f in incident:h[f]=0
        assert m.native(h)[22]==[0]*23
        local+=1;hold+=1
    rational_controls=0
    for t in [Q(1,4),Q(1),Q(3,2),Q(2)]:
        for v in [Q(-2),Q(1,3),Q(1)]:
            x=[Q(0)]*23;x[16]=-v
            ax=m.mv(allon,x)
            y=solve([[Q(i==j)-t*allon[i][j]/2 for j in range(23)] for i in range(23)],
                    [u+t*w/2 for u,w in zip(x,ax)])
            assert m.mv(R,y)==reduced_cayley(t,Q(0),v)
            assert m.dot(y,y)==m.dot(x,x)
            rational_controls+=1
    # Machin identity verified algebraically for tangent(4 atan(1/5)-atan(1/239)).
    a=Q(1,5);twice=2*a/(1-a*a);four=2*twice/(1-twice*twice)
    assert (four-Q(1,239))/(1+four*Q(1,239))==1
    pi=16*atan_small(Q(1,5),24)-4*atan_small(Q(1,239),6)
    s3=sqrt_q(3);s5=sqrt_q(5);star=pi/(s3+s5)
    L=Q(79,100);U=Q(4,5);assert L<star.lo<star.hi<U
    def cont(t):
        a=s3*t;b=s5*t
        c0=(sin_i(a)/s3-sin_i(b)/s5)/2
        c1=(sin_i(a)/s3+sin_i(b)/s5)/2
        beta=(cos_i(a)+cos_i(b))/2
        deriv=-(s3*sin_i(a)+s5*sin_i(b))/2
        return c0,c1,beta,deriv
    left=cont(I(L))[2];right=cont(I(U))[2]
    assert left.lo>Q(3,1000) and right.hi<Q(-3,200)
    cmins=[];dmins=[];dmaxs=[]
    for j in range(20):
        interval=I(L+(U-L)*Q(j,20),L+(U-L)*Q(j+1,20))
        _,c,b,d=cont(interval)
        assert c.lo>Q(49,100)
        assert d.hi<Q(-193,100) and d.lo>-2
        cmins.append(c.lo);dmins.append(d.lo);dmaxs.append(d.hi)
    rho=Q(1,10000)
    assert left.lo-2*rho>0 and right.hi+2*rho<0
    assert max(dmaxs)+5*rho<Q(-19,10)
    c0,peak,beta,d=cont(star)
    assert peak.lo>0 and peak.hi<Q(51,100)
    continuous_ratio=peak*peak
    # Unique positive cubic root giving the first/global Cayley-parameter peak.
    def p(z):return 16+16*z-13*z*z-15*z*z*z
    lo=Q(1);hi=Q(2);assert p(lo)>0 and p(hi)<0
    for _ in range(80):
        mid=(lo+hi)/2
        if p(mid)>0:lo=mid
        else:hi=mid
    z=I(lo,hi);step=sqrt_i(z);den=1+2*z+Q(15,16)*z*z
    cayley_peak=step*(1+z)/den
    endpoint_beta=(1-Q(15,16)*z*z)/den
    cayley_ratio=cayley_peak*cayley_peak
    assert Q(2582,10000)<cayley_ratio.lo<cayley_ratio.hi<Q(2583,10000)
    assert endpoint_beta.hi<Q(-1,100)
    assert continuous_ratio.hi<cayley_ratio.lo
    c=Q(24,37)
    t0=Q(1033341848074,10**12)
    assert max(abs(step.lo-t0),abs(step.hi-t0))<Q(1,10**12)
    initial=m.checkpoints()[0];ax=m.mv(allon,initial)
    loaded=solve([[Q(i==j)-t0*allon[i][j]/2 for j in range(23)] for i in range(23)],
                 [u+t0*w/2 for u,w in zip(initial,ax)])
    assert m.dot(initial,initial)==m.dot(loaded,loaded)==Q(4683,1369)
    assert m.mv(R,loaded)==reduced_cayley(t0,Q(0),-c)
    middle=[(u+v)/2 for u,v in zip(initial,loaded)]
    receipts=[]
    for w in m.WEIGHTS:
        delta=m.stock(loaded,w)-m.stock(initial,w)
        cut=2*t0*sum((w[i]-w[j])*allon[i][j]*middle[i]*middle[j] for i in range(23) for j in range(i+1,23))
        assert delta==cut
        receipts.append(str(delta))
    h=[0,1,0,1,0,1,0];held=loaded
    for dt in [Q(1,4),Q(1),Q(2)]:
        a=m.native(h);ax=m.mv(a,held)
        held=solve([[Q(i==j)-dt*a[i][j]/2 for j in range(23)] for i in range(23)],
                   [u+dt*w/2 for u,w in zip(held,ax)])
        assert held[22]==loaded[22] and m.dot(held,held)==Q(4683,1369)
    receipt={'load_parameter':str(t0),'initial':[str(v) for v in initial],
       'loaded':[str(v) for v in loaded],'norm_squared':'4683/1369','signed_owned_load_receipts':receipts,
       'retained_core_amplitude':str(loaded[22]),'retained_core_stock':str(loaded[22]**2),
       'hold_mask':h,'hold_test_steps':['1/4','1','2'],'hold_tests':3,'physical_promotion':0}
    (ROOT/'ONE_STEP_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    out={'status':'PASS_EXACT_CONDITIONAL_PEAK_GUARDS_AND_CAYLEY_ROOT',
      'dimension':23,'native_core_gram':[[int(v) for v in r] for r in K],'reduced_observable_dimension':4,
      'inherited_observable_metric':[[str(v) for v in row] for row in g],
      'uniform_loading_source_budget_ratio':'4/15',
      'complementary_initial_face_budget_ratio':'11/15',
      'native_allon_observable_intertwining':True,'local_guard_mask_cases':local,
      'isolating_hold_mask_cases':hold,'full_native_rational_cayley_controls':rational_controls,
      'guard':'beta1 = 0 and c1*(4*c1-c0) > 0; load mode only',
      'guard_amplitude_read_count':6,'loading_mask':[1]*7,'hold_mask':[0,1,0,1,0,1,0],
      'extra_mode_record':'one supplied binary load/hold record; irreversible latch; source/reset OPEN',
      'continuous_first_peak_parameter_interval':box(star),
      'continuous_core_gain_amplitude_interval':box(peak),
      'continuous_core_stock_gain_ratio_interval':box(continuous_ratio),
      'continuous_root_bracket':[str(L),str(U)],
      'uniform_beta_derivative_interval':[str(min(dmins)),str(max(dmaxs))],
      'relative_preparation_ball_radius':str(rho),
      'perturbed_root_shift_bound':str(Q(20,19)*rho),
      'pure_event_parameter_error_amplitude_bound':'sigma^2 * abs(v) within the certified bracket',
      'cayley_optimal_z_polynomial':'16+16*z-13*z^2-15*z^3',
      'cayley_optimal_parameter_interval':box(step),
      'cayley_peak_stock_gain_ratio_interval':box(cayley_ratio),
      'cayley_endpoint_beta_over_v_interval':box(endpoint_beta),
      'historical_face_feed_amplitude':str(c),
      'historical_continuous_held_stock_interval':box(continuous_ratio*c*c),
      'historical_cayley_held_stock_interval':box(cayley_ratio*c*c),
      'scope':'First-peak capture objective, chosen output core and supplied mode; does not complete the v2.21 full-feed/restoration objective.',
      'one_step_rational_parameter':str(t0),'rational_parameter_error_bound':'1/1000000000000',
      'rational_native_load_and_hold_controls':4,'physical_promotion':0}
    (ROOT/'RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
