#!/usr/bin/env python3
"""Exact budget calculator for NEB v0.1. No physical calibration is implied."""
import argparse,json,math
from fractions import Fraction as F
def budget(a,N,epsilon,target=None):
 a,N,epsilon=map(F,(a,N,epsilon))
 if not (a>0 and N>0 and 0<epsilon<=F(1,100000)):raise ValueError('Require a,N>0 and 0<epsilon<=1/100000')
 m=min(a,N*epsilon)/2;J=max(a,25*N);L=62*N;R=3*m/L
 eta=R if target is None else F(target)
 if not 0<eta<=R:raise ValueError('Target radius must satisfy 0<eta<=R')
 B=m*eta**2/2;ds=eta**2*m/(2*J)
 digits=max(30,30+(len(str(ds.denominator))-len(str(ds.numerator))+1)//2);scale=10**digits
 k=math.isqrt((ds.numerator*scale**2)//ds.denominator);lo=F(k,scale);hi=F(k+1,scale)
 assert lo**2<=ds<hi**2
 return {'theorem':'NEB v0.1; DERIVED CONDITIONAL under frozen UD action','a':str(a),'N':str(N),'epsilon':str(epsilon),'m':str(m),'J':str(J),'L':str(L),'outer_radius_R':str(R),'chosen_target_eta':str(eta),'boundary_energy_barrier_B_eta':str(B),'automatic_initial_energy_budget_B_eta_over_two':str(B/2),'exact_initial_radius_squared':str(ds),'initial_radius_sqrt_enclosure':[str(lo),str(hi)],'safe_rational_initial_radius':str(lo),'interpretation':'d_g(x0,chosen balanced orbit)<=safe_rational_initial_radius guarantees d_g(x(t),orbit)<eta for all time; all distances use the declared Frobenius/round-sphere product metric','scope':'finite rank r>=1; normalized matter norms exactly one; physical Gauss-zero restriction invariant','physical_promotion':0,'independent_review':'PENDING'}
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--a',required=True);p.add_argument('--N',required=True);p.add_argument('--epsilon',required=True);p.add_argument('--target');args=p.parse_args()
 try:print(json.dumps(budget(args.a,args.N,args.epsilon,args.target),indent=2))
 except ValueError as e:p.error(str(e))
