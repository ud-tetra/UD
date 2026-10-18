"""Exact sufficient cumulative work/leakage contract.
Every input is an externally certified upper bound, not a measurement inferred here.
work_upper must bound EVERY PREFIX of signed defect work, not terminal net work.
"""
from fractions import Fraction as F
from parity_budget import constants,sqrt_bracket
import json,argparse

def interval(x,N):
 if x is None:return N,N
 if len(x)!=2:raise ValueError('two norm endpoints required')
 lo,hi=map(F,x)
 if not 0<lo<=hi:raise ValueError('positive ordered initial norm interval required')
 return lo,hi

def budget(a='1',N='1',eta=None,nq0=None,nw0=None,leakage_q='0',leakage_w='0',parameter_variation='0',defect_length='0',work_upper=None,score_upper='0',energy_upper='0',nu='0',beta_other='0',g0_upper=None,source_integral_upper=None,norm_gain_q=None,norm_gain_w=None):
 a,N=F(a),F(N)
 if a<=0 or N<=0:raise ValueError('positive a,N required')
 _,_,_,_,_,R,_,J,_=constants(a,N);eta=R if eta is None else F(eta)
 if not 0<eta<=R:raise ValueError('eta outside inherited certified radius')
 qL,qU=interval(nq0,N);wL,wU=interval(nw0,N)
 Lq,Lw,T,Ly,P,F0,nu,bo=map(F,[leakage_q,leakage_w,parameter_variation,defect_length,score_upper,energy_upper,nu,beta_other])
 if min(Lq,Lw,T,Ly,P,nu,bo)<0:raise ValueError('nonnegative upper bounds required except relative energy')
 Gq=Lq if norm_gain_q is None else F(norm_gain_q);Gw=Lw if norm_gain_w is None else F(norm_gain_w)
 if min(Gq,Gw)<0:raise ValueError('negative positive-variation bound')
 Lplus=min(Gq,Lq)+min(Gw,Lw)
 Ln=Lq+Lw;D0=max(abs(qL-N),abs(qU-N))+max(abs(wL-N),abs(wU-N));D=D0+Ln
 beta=bo+20*D;c=N/1600;B=c*eta**4;cap=c*eta**3/8
 KH=(J+beta)*eta+nu;speed_work=KH*Ly
 if work_upper is None:W=speed_work
 else:
  Wdirect=F(work_upper)
  if Wdirect<0:raise ValueError('prefix work bound must be nonnegative')
  W=min(Wdirect,speed_work)
 KG2=16*eta**2+8+4*(qU+Lq)**2+4*(wU+Lw)**2;KGupper=F(sqrt_bracket(KG2)[1]);S=KGupper*Ly+Ln
 if source_integral_upper is not None:
  source_integral_upper=F(source_integral_upper)
  if source_integral_upper<0:raise ValueError('negative source integral bound')
  S=min(S,source_integral_upper)
 g0=None if g0_upper is None else F(g0_upper)
 if g0 is not None and g0<0:raise ValueError('negative initial Gauss norm bound')
 spent=eta*T+10*eta**2*Lplus+W
 gates={'positive_norm_floor':qL>Lq and wL>Lw,'mixed_amplitude':nu+eta*beta<=cap,'initial_geometry':P<=eta**2/4,'initial_actual_energy':F0<=B/2,'cumulative_work':spent<=B/4}
 vals={'a':a,'N':N,'eta':eta,'J':J,'c':c,'B':B,'initial_norm_error_sum_upper':D0,'norm_total_variation_upper':Ln,'norm_error_envelope_upper':D,'q_norm_floor':qL-Lq,'w_norm_floor':wL-Lw,'q_norm_ceiling':qU+Lq,'w_norm_ceiling':wU+Lw,'beta_total':beta,'generic_gradient_upper':nu,'mixed_amplitude_cap':cap,'mixed_amplitude_spent':nu+eta*beta,'parameter_gradient_variation_upper':T,'defect_path_length_upper':Ly,'energy_gradient_tube_upper':KH,'defect_work_from_speed_upper':speed_work,'defect_prefix_work_upper_used':W,'norm_positive_variation_upper':Lplus,'norm_variation_work_upper':10*eta**2*Lplus,'parameter_variation_work_upper':eta*T,'total_work_upper':spent,'work_allowance':B/4,'work_reserve':B/4-spent,'actual_relative_energy_upper':F0+spent,'boundary_actual_energy_lower':B-nu*eta-beta*eta**2/2,'gauss_derivative_squared_constant':KG2,'gauss_derivative_constant_upper':KGupper,'gauss_source_integral_upper_used':S,'norm_variation_only_amplitude_cap':N*eta**2/256000,'defect_length_only_cap':(B/4)/(J*eta),'parameter_variation_only_cap':c*eta**3/4}
 return {'status':'CERTIFIED_THROUGH_DECLARED_HORIZON' if all(gates.values()) else 'NOT_CERTIFIED_BY_THIS_BOUND','gates':gates,'exact':{k:str(v) for k,v in vals.items()},'decimal_diagnostics':{k:float(v) for k,v in vals.items()},'gauss_norm_upper':None if g0 is None else str(g0+S),'gauss_scope':'Source increment upper is conditional on the admitted tube and certified input bounds. Exact zero-source constraint requires S_i=0 pointwise and G_i(0)=0; a small bound is not repair.','input_scope':'Guaranteed joint coverage; parameter variation includes explicit and norm-parameter derivatives of other errors. Prefix signed-work bound or speed bound is required. Defaults are illustrative assumptions.','physical_promotion':0}

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('input');x=p.parse_args()
 with open(x.input) as f:r=json.load(f)
 print(json.dumps(budget(**r),indent=2))
