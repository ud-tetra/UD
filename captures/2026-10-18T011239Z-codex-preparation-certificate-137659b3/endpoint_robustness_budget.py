"""Exact endpoint error-budget calculator. Inputs are mathematical upper bounds.
Default zero errors are illustrative assumptions, not measurements.
"""
from fractions import Fraction as F
import argparse,json
from parity_budget import constants,sqrt_bracket

def positive_cubic_root_bracket(c,nu,beta,eta,steps=120):
 if nu==beta==0:return [F(0),F(0)]
 lo,hi=F(0),eta
 def p(x):return c*x**3-beta*x/2-nu
 assert p(hi)>=0
 for _ in range(steps):
  mid=(lo+hi)/2
  if p(mid)<=0:lo=mid
  else:hi=mid
 assert p(lo)<=0<=p(hi)
 return [lo,hi]

def budget(a=F(1),N=F(1),eta=None,A=F(0),K=F(0),common_hopping=F(0),residual_hopping=F(0),detuning=F(0),variation=F(0)):
 a,N,alpha,D,S,R,old,J,ideal2=constants(F(a),F(N));eta=R if eta is None else F(eta)
 assert 0<eta<=R
 A,K,H,G,V,T=[F(x) for x in [A,K,common_hopping,residual_hopping,detuning,variation]]
 assert all(x>=0 for x in [A,K,H,G,V,T])
 c=N/1600;B=c*eta**4;cap=c*eta**3/8;curv=cap/eta
 nu=N*(14*G+3*V);beta=A+12*N*K+24*N*H;spent=nu+eta*beta
 within=spent<=cap;time_within=within and T<=cap
 vals={'a':a,'N':N,'eta':eta,'R_cert':R,'c':c,'J':J,'B_eta':B,'delta_eta_squared':eta**4*c/J,'gradient_cap':cap,'centered_hessian_cap':curv,'generic_gradient_bound':nu,'centered_hessian_bound':beta,'gradient_budget_spent':spent,'gradient_budget_reserve':cap-spent,'cumulative_gradient_variation':T,'static_nominal_energy_upper_bound':3*B/4,'time_nominal_energy_upper_bound':7*B/8,'complex_loop_state_error_upper_bound':21*eta,'pure_magnetic_K_cap':curv/(12*N),'pure_uniform_hopping_cap':curv/(24*N),'pure_residual_hopping_cap':cap/(14*N),'pure_site_half_range_cap':cap/(3*N)}
 root=positive_cubic_root_bracket(c,nu,beta,eta) if within else None
 return {'status':'WITHIN_SUFFICIENT_BUDGET' if within else 'OUT_OF_SUFFICIENT_BUDGET','time_budget_status':'WITHIN_SUFFICIENT_BUDGET' if time_within else 'OUT_OF_SUFFICIENT_BUDGET','exact':{k:str(v) for k,v in vals.items()},'decimal_diagnostics':{k:float(v) for k,v in vals.items()},'delta_eta_rational_bracket':sqrt_bracket(vals['delta_eta_squared']),'minimizing_set_distance_cubic_root_bracket':None if root is None else [str(t) for t in root],'root_bound_scope':'Upper endpoint bounds every member of the full minimizing set; no unique shifted orbit or attraction','assumption_note':'Inputs must bound the full tube; zero defaults are assumptions, not measurements; rates use the model evolution parameter','physical_promotion':0}

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for name,default in [('a','1'),('N','1'),('eta',None),('A','0'),('K','0'),('common-hopping','0'),('residual-hopping','0'),('detuning','0'),('variation','0')]:p.add_argument('--'+name,default=default)
 x=p.parse_args();print(json.dumps(budget(F(x.a),F(x.N),None if x.eta is None else F(x.eta),F(x.A),F(x.K),F(x.common_hopping),F(x.residual_hopping),F(x.detuning),F(x.variation)),indent=2))
