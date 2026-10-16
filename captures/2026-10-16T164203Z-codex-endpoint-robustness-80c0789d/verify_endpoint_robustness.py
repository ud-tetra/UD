"""Exact algebraic checks and rational budget examples; not independent review."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,sympy as s
from endpoint_robustness_budget import budget

def main():
 checks=[]
 def ck(name,x):
  assert bool(x),name;checks.append({'name':name,'pass':True})
 ck('static_energy_fraction',F(1,2)+F(1,4)==F(3,4)<1)
 ck('time_energy_fraction',F(1,2)+F(1,4)+F(1,8)==F(7,8)<1)
 ck('minimizing_boundary_gap',1-F(1,8)==F(7,8)>0)
 c,eta,nu,beta=s.symbols('c eta nu beta',positive=True);u,v,w=s.symbols('u v w',nonnegative=True)
 ck('generic_radius_scaling',(s.Rational(1,2))**3==s.Rational(1,8))
 ck('centered_radius_scaling',(s.Rational(1,4))**2==s.Rational(1,16))
 # u+v+w=1/8; sign of cubic at normalized d=1/2.
 expr=s.Rational(1,8)-v/4-u
 ck('mixed_cubic_half_eta',s.expand(expr.subs(u,s.Rational(1,8)-v-w)-(w+3*v/4))==0)
 ck('magnetic_hessian_incidence',4*3==12)
 M=s.Matrix([[1,2,0],[1,0,2]])
 ck('common_hopping_hessian',4*max((M*M.T).eigenvals())==24)
 ck('residual_hopping_gradient',8**2*3<14**2)
 ck('site_half_range_gradient',2**2*2<3**2)
 ck('loop_metric_constant',20**2+2**2==404<21**2)
 ck('loop_total_error_split',F(21,42)+F(1,2)==1)
 q,p,t,h,b=s.symbols('q p t h b',real=True);C=s.symbols('C',positive=True)
 generic=p*p/2+C*q**4-4*C*t**3*q
 ck('tilted_quartic_stationary',s.diff(generic,q).subs(q,t)==0)
 ck('tilted_quartic_curvature',s.diff(generic,q,2).subs(q,t)==12*C*t*t)
 centered=p*p/2+C*q**4-(4*C*t*t)*q*q/2
 ck('centered_quartic_stationary',s.diff(centered,q).subs(q,t)==0)
 ck('centered_quartic_curvature',s.diff(centered,q,2).subs(q,t)==8*C*t*t)
 ck('centered_origin_negative_curvature',s.diff(centered,q,2).subs(q,0)==-4*C*t*t)
 ck('diamond_critical_negative_shift',s.diff(1+s.cos(q),q,2).subs(q,0)==-1)
 ck('uniform_stiffness_budget',12*F(1,153600)==F(1,12800))
 ck('uniform_stiffness_shift_bound',F(12*1600,2*153600)==F(1,16))
 f=s.symbols('f',positive=True);tt=s.symbols('tt',real=True)
 Q=f*(s.sin(tt)-tt*s.cos(tt))/2;P=f*tt*s.sin(tt)/2
 ck('resonant_ode_q',s.simplify(s.diff(Q,tt)-P)==0)
 ck('resonant_ode_p',s.simplify(s.diff(P,tt)+Q-f*s.sin(tt))==0)
 ck('resonant_zero_initial',Q.subs(tt,0)==P.subs(tt,0)==0)
 n=s.symbols('n',integer=True,positive=True)
 ck('resonant_unbounded_sequence',s.simplify(Q.subs(tt,2*s.pi*n)+s.pi*f*n)==0)
 fixtures=[]
 for a,N,mode in [(F(1),F(1),'generic'),(F(1),F(1),'centered'),(F(1),F(1),'mixed'),(F(1,100000),F(1),'mixed'),(F(100),F(3),'mixed')]:
  z=budget(a,N);cap=F(z['exact']['gradient_cap']);curv=F(z['exact']['centered_hessian_cap']);et=F(z['exact']['eta'])
  Gv=cap/(3*N) if mode=='generic' else F(0)
  K=curv/(12*N) if mode=='centered' else F(0)
  if mode=='mixed':Gv=cap/(6*N);K=curv/(24*N)
  r=budget(a,N,K=K,detuning=Gv,variation=cap)
  assert r['status']==r['time_budget_status']=='WITHIN_SUFFICIENT_BUDGET'
  lo,hi=map(F,r['minimizing_set_distance_cubic_root_bracket'])
  assert lo<=hi<=et/2+et/F(2**119)
  if mode=='centered':assert hi<=et/4+et/F(2**119)
  fixtures.append({'mode':mode,**r})
 inherited=Path('FROZEN_PARITY_ENDPOINT_CERTIFICATE_v0.1.json');assert json.loads(inherited.read_text())['status']=='PASS'
 out={'status':'PASS','check_count':len(checks),'checks':checks,'claim_bin':'DERIVED_CONDITIONAL','independent_review':'PENDING','physical_promotion':0,'budget_examples':fixtures,'frozen_input_sha256':hashlib.sha256(inherited.read_bytes()).hexdigest(),'scope':'Analytic quartic barrier transfer, minimizing-set localization and coefficient proof in manuscript. Exact identities, two scalar normal forms, drift counterexample and five rational budgets checked here. Frozen PET input remains inherited conditional support; no new interval region or independent review.'}
 Path('ENDPOINT_ROBUSTNESS_CERTIFICATE_v0.1.json').write_text(json.dumps(out,indent=2)+'\n')
 Path('UNIT_MIXED_ROBUSTNESS_BUDGET_v0.1.json').write_text(json.dumps(fixtures[2],indent=2)+'\n')
 print(json.dumps({'status':'PASS','exact_checks':len(checks),'unit':fixtures[2]['decimal_diagnostics']},indent=2))
if __name__=='__main__':main()
