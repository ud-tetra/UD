"""Rational sufficient energy admission in the ambient Hamiltonian model.
Input upper bounds and norm enclosures require external certified joint coverage.
Nonzero Gauss levels are not zero-source constrained-action solutions.
"""
from fractions import Fraction as F
from parity_budget import constants,sqrt_bracket
import argparse,json

def interval(x):
 lo,hi=map(F,x)
 if not 0<lo<=hi:raise ValueError('positive ordered norm interval required')
 return lo,hi

def admission(a=F(1),N=F(1),eta=None,nq=('1','1'),nw=('1','1'),score_upper=F(0),energy_upper=F(0),nu=F(0),beta_other=F(0),variation=F(0)):
 a,N=F(a),F(N)
 if a<=0 or N<=0:raise ValueError('positive a,N required')
 _,_,_,_,_,R,_,J,_=constants(a,N);eta=R if eta is None else F(eta)
 if not 0<eta<=R:raise ValueError('eta outside frozen certified radius')
 qL,qU=interval(nq);wL,wU=interval(nw)
 P,F0,nu,beta_other,T=map(F,[score_upper,energy_upper,nu,beta_other,variation])
 if min(P,nu,beta_other,T)<0:raise ValueError('nonnegative bounds required except relative energy')
 D=max(abs(qL-N),abs(qU-N))+max(abs(wL-N),abs(wU-N))
 beta_norm=20*D;beta=beta_other+beta_norm;c=N/1600;B=c*eta**4;cap=c*eta**3/8
 centered=nu+eta*beta<=cap;geom=P<=eta**2/4;energy=F0<=B/2
 static=centered and geom and energy;timed=static and T<=cap
 # Trace = n_w-n_q, so every possible norm pair is imbalanced only if intervals disjoint.
 traceL=wL-qU;traceU=wU-qL;trace_abs_lower=max(F(0),traceL,-traceU)
 # g <= D+sqrt(8+4*nq^2+4*nw^2)*d. Squared safe upper avoids radicals.
 G2=2*D**2+2*(8+4*qU*qU+4*wU*wU)*P
 vals={'a':a,'N':N,'eta':eta,'J':J,'B':B,'legacy_delta_squared':c*eta**4/J,'geometric_score_ceiling':eta**2/4,'initial_relative_energy_ceiling':B/2,'norm_error_sum_bound':D,'norm_centered_hessian_bound':beta_norm,'total_centered_hessian_bound':beta,'generic_gradient_bound':nu,'gradient_budget_cap':cap,'gradient_budget_spent':nu+eta*beta,'cumulative_gradient_variation':T,'static_nominal_energy_upper':F0+nu*eta+beta*eta**2/2,'time_nominal_energy_upper':F0+nu*eta+beta*eta**2/2+eta*T,'gauss_squared_upper_from_score':G2,'global_trace_lower':traceL,'global_trace_upper':traceU,'global_trace_abs_lower':trace_abs_lower,'norm_error_only_cap':N*eta**2/256000,'geometric_ceiling_over_legacy_score_ceiling':(eta**2/4)/(c*eta**4/J)}
 return {'status':'CERTIFIED_SUFFICIENT_ENERGY_ADMISSION' if static else 'NOT_CERTIFIED_BY_THIS_BOUND','time_status':'CERTIFIED_THROUGH_DECLARED_VARIATION_HORIZON' if timed else 'NOT_CERTIFIED_BY_THIS_BOUND','gates':{'mixed_error':centered,'geometric':geom,'energy':energy,'variation':T<=cap},'exact':{k:str(v) for k,v in vals.items()},'decimal_diagnostics':{k:float(v) for k,v in vals.items()},'zero_gauss_norm_compatibility':'IMPOSSIBLE_FOR_ALL_NORMS_IN_INTERVALS' if trace_abs_lower>0 else 'NOT_ESTABLISHED_BY_NORM_INTERVALS','gauss_upper_bracket':sqrt_bracket(G2),'scope':'Ambient temporal-gauge Hamiltonian trapping; requires guaranteed enclosures and all frozen model premises. No constraint repair, data realizability or physical admissibility inferred. Norms are constant in this theorem.','physical_promotion':0}

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('input');x=p.parse_args()
 with open(x.input) as f:record=json.load(f)
 print(json.dumps(admission(**record),indent=2))
