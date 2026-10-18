"""Exact sufficient trapping budget at the frozen quartic endpoint.
All inputs are rational mathematical coefficients, not measured physical units.
"""
from fractions import Fraction as F
from math import isqrt
import argparse,json

def constants(a=F(1),N=F(1)):
 a,N=F(a),F(N);assert a>0 and N>0
 alpha=min(a/2,N/100);D=279*N/(4*alpha);C3=279*N;C4=1600*N;C5=10000*N
 S=F(9,2)*C3*C3*D*D/alpha+C3*D**3/6+C4*C4/(18*alpha)+5*C4*D*D+F(2,15)*C5*D+F(8,9)*C5*C5/alpha+264*N
 linear=alpha/(500000*N);root2=N/(400*S)
 # Exact rational lower radius for the potentially irrational root.
 q=1/root2;m=isqrt(q.numerator//q.denominator)
 if m*m*q.denominator<q.numerator:m+=1
 R=min(linear,F(1,m));E=N*(2177*D*D+F(800,3)*D+F(19,6))+F(1280000,9)*N*N/alpha
 old=min(alpha/(10000*N),N/(400*E));J=max(a,25*N)
 return a,N,alpha,D,S,R,old,J,min(linear*linear,root2)

def sqrt_bracket(q,digits=70):
 scale=10**digits;n=isqrt(q.numerator*scale*scale//q.denominator)
 lo,hi=F(n,scale),F(n+1,scale);assert lo*lo<=q<=hi*hi
 return [str(lo),str(hi)]

def budget(a=F(1),N=F(1),eta=None):
 a,N,alpha,D,S,R,old,J,ideal2=constants(a,N);eta=R if eta is None else F(eta)
 assert 0<eta<=R
 checks={'positive_radius':R>0,'radius_le_one':R<=1,'shift_small':D*R<F(1,2),
 'fast_absorption':F(3,8)*alpha+F(4,3)*279*N*R+17*1600*N*R**2+2*10000*N*R**3+4096*N*R**4<alpha/2,
 'quartic_absorption':S*R*R<=N/400,'distance_conversion':N*R*R/400<=alpha/2,
 'rational_radius_exceeds_50000_old':R>=50000*old,'inside_initial_ball':eta*eta*N/(1600*J)<1}
 assert all(checks.values())
 values={'a':a,'N':N,'alpha':alpha,'D':D,'S6':S,'R_cert':R,'R_ideal_squared':ideal2,'R_old':old,'radius_gain':R/old,'J':J,'eta':eta,'boundary_barrier':N*eta**4/1600,'initial_radius_squared':eta**4*N/(1600*J)}
 return {'exact':{k:str(v) for k,v in values.items()},'decimal_diagnostics':{k:float(v) for k,v in values.items()},'initial_radius_rational_bracket':sqrt_bracket(values['initial_radius_squared']),'checks':checks}

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--a',default='1');p.add_argument('--N',default='1');p.add_argument('--eta')
 args=p.parse_args();print(json.dumps(budget(F(args.a),F(args.N),None if args.eta is None else F(args.eta)),indent=2))
