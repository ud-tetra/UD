"""Exact prefix-only budgets and a conditional catalogue clock overlap."""
from fractions import Fraction as F
from math import factorial
import json
def encode(x):
    if isinstance(x,F):return {'exact':str(x),'decimal':float(x)}
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,list):return [encode(v) for v in x]
    return x
def certificate(t0=F(1,60),age_physical=F(3,1000000),actuator_tau=F(1,1000000)):
    L=F(4);M=F(8,5);K=F(5);nu=F(3,100000);q=F(1,25000);ea=F(1,100000)
    hmin=F(999,100000);hmax=F(1001,100000);e0=m=F(1,10000);delta=F(1,100)
    tracking=K*(M*(age_physical+actuator_tau)/t0+nu)+q+ea
    total=F(3,400)+max(F(1,1000),tracking)
    eta=(e0+delta*hmax)/(1-L*hmax);B=4*(eta+e0)+16*m
    qw=2*hmin-8*hmin**2-F(11,8)*hmin**3
    qf=2*hmin-F(8,3)*hmin**3
    clock_lower=K*M*(age_physical+actuator_tau)/(F(1,400)-K*nu-q-ea)
    # Given verified operating-band L>=.85H,C>=.8mF,R<=6.6125ohm,
    # R/L<8 per sec and 1/sqrt(LC)<40 per sec: lambda<48*t0.
    clock_upper=F(1,48)
    reconstruction=max(nu,m)
    displacement=e0+M*hmax+reconstruction
    angle=e0+(F(1,50)+delta)*hmax+reconstruction
    margins={'tracking':F(1,400)-tracking,'residual':delta-total,
      'clock_lower':t0-clock_lower,'clock_upper':clock_upper-t0,
      'lower_large_coordinate':F(7,10)-displacement-F(2,3),
      'upper_large_coordinate':F(3,4)-F(71,100)-displacement,
      'small_coordinate':F(1,50)-displacement,'angle':F(1,100)-angle,
      'nominal_Gauss':(1+hmin)/100-B,'wrong_sign_Gauss':qw-B-(1+hmax)/100,
      'frozen_Gauss':qf-B-(1+hmax)/100,
      'initial_Gauss':F(1,100)-4*e0-8*m}
    warm=F(5,2)/20000+K*(F(2,20000)+nu)+q+ea
    return {'status':'PASS_CONDITIONAL_DESIGN' if all(v>0 for v in margins.values()) else 'HOLD_NOT_CERTIFIED',
      'input_kind':'supplied bounds; catalogue screen only; no measurements','physical_promotion':0,
      't0_seconds':t0,'tracking_bound':tracking,'total_residual':total,
      'local_trajectory_error':eta,'Gauss_decision_error':B,
      'clock_lower_seconds':clock_lower,'clock_upper_seconds':clock_upper,
      'startup_tracking_upper':warm,'margins':margins}
def selftest():
    z=certificate()
    assert z['status']=='PASS_CONDITIONAL_DESIGN'
    assert z['tracking_bound']==F(53,25000)
    assert z['total_residual']==F(481,50000)
    assert z['clock_lower_seconds']==F(8,575) and z['clock_upper_seconds']==F(1,48)
    assert z['startup_tracking_upper']==F(33,40000)<F(1,1000)
    assert certificate(t0=F(1,1000))['status']=='HOLD_NOT_CERTIFIED'
    assert certificate(t0=F(1,20))['status']=='HOLD_NOT_CERTIFIED'
    assert F(529,80)/F(17,20)<8
    assert F(17,20)*F(1,1250)>F(1,1600)
    assert F(7,10)**2<F(1,2)<F(71,100)**2
    assert sum(F(10**k,factorial(k)) for k in range(25))>20000
    # Conditional union bound: N<=10000, noise allowance 24ppm,
    # marginal sub-Gaussian scale <=4ppm -> exponent18.
    e18=sum(F(18**k,factorial(k)) for k in range(35))
    assert e18>10**7 and F(20000)/e18<F(1,500)
    assert F(24,35000000)<F(1,1000000)
    return {'status':'PASS','exact_controls':12,'constructor_only':True,
      'conditional_noise_union_upper':F(20000)/e18,
      'noise_tail_premise':'Every coordinate error has two-sided sub-Gaussian scale <=4ppm; not inferred from supplier RMS',
      'input_error_partition':{'deterministic':'6ppm','noise_allowance':'24ppm'},
      'input_noise_family_failure_budget':'less than 1/500; other run uncertainties need separate allocation'}
if __name__=='__main__':
    print(json.dumps(encode({'certificate':certificate(),'controls':selftest(),
      'negative_examples':{'too_fast_clock':certificate(t0=F(1,1000)),
                           'outside_plant_clock_envelope':certificate(t0=F(1,20))}}),indent=2))
