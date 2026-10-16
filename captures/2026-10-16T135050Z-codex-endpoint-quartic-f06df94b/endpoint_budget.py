"""Standard-library exact endpoint budget calculator; no physical units assumed."""
from fractions import Fraction as F
from math import isqrt
import argparse,json

def budget(a=F(1),N=F(1),eta=None):
 a,N=F(a),F(N);assert a>0 and N>0
 alpha=min(a/2,N/100);D=279*N/(4*alpha)
 E=N*(2177*D*D+F(800,3)*D+F(19,6))+F(1280000,9)*N*N/alpha
 R=min(alpha/(10000*N),N/(400*E));c=N/1600;J=max(a,25*N)
 eta=R if eta is None else F(eta);assert 0<eta<=R
 checks={'radius_le_one':R<=1,'shift_small':D*R<F(1,2),
 'fast_error_absorbed':alpha/8+2177*N*R<alpha/2,
 'quartic_error_absorbed':E*R<=N/400,
 'quartic_distance_conversion':3*c<=N/400,
 'fast_distance_conversion':4*c*R*R<=alpha/2,
 'initial_inside':eta*eta*c/J<1}
 assert all(checks.values())
 exact={'a':a,'N':N,'alpha':alpha,'D':D,'E':E,'R_star':R,'c':c,'J':J,'eta':eta,
        'boundary_barrier':c*eta**4,'initial_radius_squared':eta**4*c/J}
 return {'exact':{k:str(v) for k,v in exact.items()},'decimal_diagnostics':{k:float(v) for k,v in exact.items()},'checks':checks}

def sqrt_bracket(q,digits=70):
 scale=10**digits;n=isqrt(q.numerator*scale*scale//q.denominator)
 lo=F(n,scale);hi=F(n+1,scale)
 assert lo*lo<=q<=hi*hi
 return [str(lo),str(hi)]

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--a',default='1');p.add_argument('--N',default='1');p.add_argument('--eta')
 args=p.parse_args();out=budget(F(args.a),F(args.N),None if args.eta is None else F(args.eta))
 out['initial_radius_rational_bracket']=sqrt_bracket(F(out['exact']['initial_radius_squared']))
 print(json.dumps(out,indent=2))
