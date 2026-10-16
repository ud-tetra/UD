#!/usr/bin/env python3
"""Exact constructor checks of robustness transfer and resonant obstruction."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import json,sympy as s
from robustness_budget import robust_budget
O=Path(__file__).resolve().parent;checks=[]
def check(name,value):assert bool(value),name;checks.append(name);print('PASS',name)
nodes=[a for k in range(1,5) for a in combinations(range(4),k)]
edges=[(i,j) for i,u in enumerate(nodes) for j,v in enumerate(nodes) if len(v)==len(u)+1 and set(u)<set(v)]
diamonds=[]
for i,u in enumerate(nodes):
 for k,v in enumerate(nodes):
  if len(v)==len(u)+2 and set(u)<set(v):
   j,h=[j for j,w in enumerate(nodes) if len(w)==len(u)+1 and set(u)<set(w)<set(v)];diamonds.append([edges.index(e) for e in [(i,j),(j,k),(i,h),(h,k)]])
check('carrier_counts',len(nodes)==15 and len(edges)==28 and len(diamonds)==18)
check('maximum_node_degree_four',max(sum(i==a or i==b for a,b in edges) for i in range(15))==4)
check('maximum_edge_diamond_incidence_three',max(sum(e in d for d in diamonds) for e in range(28))==3)
check('magnetic_orbit_gradient_constant',9*28<16**2)
check('magnetic_hessian_constant',4*3==12)
check('hopping_gradient_constant',8**2*3<14**2)
check('site_detuning_gradient_constant',2**2*2<3**2)
check('local_matter_normalization_factor',2/F(1,5)==10)
check('complex_readout_Lipschitz_twenty_one',20**2+4<21**2)
check('phase_readout_L2_one_eighty',42**2*18<180**2)
check('maximum_radius_chart_safe',F(3,12400000)<F(1,10))
check('complex_readout_phase_disc_safe',21*F(3,12400000)<F(1,2))
check('real_model_noise_half_budget',F(21,1680)==F(1,80))
check('real_combined_noise_budget',F(1,80)+F(1,80)==F(1,40))
check('oriented_dynamic_bound',F(180*3,124)<5)
check('oriented_half_noise_reserve',F(1,100000)<F(1,4))
check('autonomous_error_oscillation_quarter_budget',2*F(1,16)==F(1,2)*F(1,4))
check('canonical_static_total_three_quarters',F(1,2)+F(1,4)==F(3,4))
check('canonical_drift_total_seven_eighths',F(1,2)+F(1,4)+F(1,8)==F(7,8))
check('minimizer_displacement_one_eighth',2*F(1,16)==F(1,8))
check('forced_only_work_quarter_budget',F(1,8)==F(1,2)*F(1,4))
examples=[]
for a,N,ep,real in [('1','1','1/100000',False),('1','1','1/100000',True),('2/5','2','1/1000000',False)]:
 b=robust_budget(a,N,ep,real_readout=real);m=F(b['base_budget']['m']);eta=F(b['selected_target_eta']);nu=F(b['canonical_gradient_limit_nu_star']);NN=F(N)
 # Allocate one quarter of the gradient limit to each of four error types.
 A=nu/(4*eta);K=nu/(4*NN*(1+12*eta));G=nu/(56*NN);D=nu/(12*NN)
 q=robust_budget(a,N,ep,real_readout=real,A=str(A),K=str(K),G=str(G),D=str(D),gradient_variation=str(nu))
 check('example_'+str(len(examples))+'_four_channel_allocation',F(q['coefficient_gradient_upper'])==nu and q['time_budget_status']=='WITHIN_SUFFICIENT_BUDGET')
 if real:check('real_target_budget_respected',21*eta<=F(ep)/80)
 examples.append(q)
# Exact resonant-drive counterexample: bounded instantaneous gradient is not an all-time work bound.
t,omega,force=s.symbols('t omega force',positive=True);n=s.symbols('n',integer=True,positive=True)
q=force*(s.sin(omega*t)-omega*t*s.cos(omega*t))/(2*omega**2);p=s.diff(q,t)
check('resonance_exact_forced_ODE',s.simplify(s.diff(q,t,2)+omega**2*q-force*s.sin(omega*t))==0)
check('resonance_zero_initial_state',q.subs(t,0)==0 and p.subs(t,0)==0)
check('resonance_unbounded_sample_sequence',s.simplify(q.subs(t,2*s.pi*n/omega)+s.pi*force*n/omega**2)==0 and s.simplify(p.subs(t,2*s.pi*n/omega))==0)
for name,kwargs in [('negative_error',{'G':'-1'}),('nonpositive_offset',{'epsilon':'0'})]:
 caught=False
 try:
  vals={'a':'1','N':'1','epsilon':'1/100000'};vals.update(kwargs);robust_budget(**vals)
 except ValueError:caught=True
 check(name+'_rejected',caught)
report={'status':'PASS','type':'EXACT rational/integer and symbolic constructor checks; analytic robustness proof in manuscript; inherited interval certificate retained as a dependency','check_count':len(checks),'checks':checks,'new_interval_cells':0,'inherited_NEB_checks':211,'static_gradient_limit':'nu_star=m*eta/16','static_minimizer_set_displacement':'<=eta/8','time_variation_limit':'integral rho<=nu_star together with sup nu<=nu_star','coefficient_gradient_bound':'A*eta+N*((1+12*eta)*K+14*G+3*D)','complex_loop_readout_error':'<21*eta','real_class_target':'eta<=min(R,epsilon/1680); instrument error per channel<=epsilon/80','resonance_obstruction':{'ODE':'q_ddot+omega^2*q=force*sin(omega*t)','solution':str(q),'sample_q':'-pi*force*n/omega^2','scope':'Counterexample to a general all-time bound from instantaneous forcing size alone; not a UD-specific forced-instability classification'},'examples':examples,'physical_promotion':0,'independent_review':'PENDING'}
(O/'ROBUSTNESS_EXACT_CERTIFICATE_v0.1.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'status':'PASS','checks':len(checks),'examples':len(examples)},indent=2))
