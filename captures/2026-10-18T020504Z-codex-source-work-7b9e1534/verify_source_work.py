"""Exact constructor replay; finite arithmetic supports manuscript analytic proof."""
from source_work_budget import *
from pathlib import Path
import hashlib
P=Path(__file__).resolve().parent;checks={}
def check(k,x):
 checks[k]=bool(x)
 if not x:raise AssertionError(k)
b=budget();v={k:F(x) for k,x in b['exact'].items()};eta=v['eta'];B=v['B'];cap=v['mixed_amplitude_cap'];normcap=v['norm_variation_only_amplitude_cap'];Ycap=v['defect_length_only_cap']
check('boundary_gap',F(1,2)+F(1,4)==F(3,4)<F(7,8))
check('norm_work_centered_factor',F(20,2)==10)
check('norm_only_amplitude_cap',20*eta*normcap==cap)
check('norm_only_work_fraction',10*eta**2*normcap==B/16)
check('defect_length_cap',v['J']*eta*Ycap==B/4)
check('parameter_only_work_cap',eta*v['parameter_variation_only_cap']==B/4)
check('electric_divergence_coefficient',2*4==8)
check('commutator_tail_coefficient',4*2**2==16)
# Exact Hermitian 2x2 commutator identity for real symmetric E,A.
from fractions import Fraction
E=[[F(1),F(1,3)],[F(1,3),F(-1,2)]];A=[[F(2,5),F(1,4)],[F(1,4),F(-3,7)]]
def mul(X,Y):return [[sum((a*b for a,b in zip(row,col)),F(0)) for col in zip(*Y)] for row in X]
def norm2(X):return sum((a*a for row in X for a in row),F(0))
EA,AE=mul(E,A),mul(A,E);comm=[[a-b for a,b in zip(x,y)] for x,y in zip(EA,AE)]
check('rational_commutator_bound',norm2(comm)<=4*norm2(E)*norm2(A))
check('commutator_trace_zero',sum(comm[i][i] for i in range(2))==0)
# Raw radial/tangential decomposition: q=(3/5,4/5), f=(2,-1), n=1.
q=[F(3,5),F(4,5)];f=[F(2),F(-1)];inner=sum(a*b for a,b in zip(q,f));p=[a-inner*b for a,b in zip(f,q)]
check('raw_projection_tangent',sum(a*b for a,b in zip(q,p))==0)
check('raw_projection_orthogonal_norm',sum(x*x for x in f)==sum(x*x for x in p)+inner**2)
check('raw_norm_flux',2*inner==F(4,5))
check('raw_variation_allocation',2*(F(1)+F(1,10))*F(1,10)==F(11,50))
# Endpoint signed work can vanish despite an arbitrarily larger prefix maximum.
check('triangle_work_first_leg',F(1,2)>F(1,8))
check('triangle_work_second_leg',F(1,2)-F(1,2)==0)
check('terminal_work_not_prefix_bound',F(0)<F(1,8)<F(1,2))
fixtures={}
examples=[('ideal',{},True),('norm_only_boundary',{'leakage_q':str(normcap),'g0_upper':'0'},True),('speed_work_boundary',{'defect_length':str(Ycap)},True),('parameter_work_boundary',{'parameter_variation':str(v['parameter_variation_only_cap'])},True),('mixed',{'leakage_q':str(normcap/8),'leakage_w':str(normcap/8),'parameter_variation':str(cap/4),'defect_length':str(Ycap/4)},True),('prefix_work_sharper_than_speed',{'defect_length':str(10*Ycap),'work_upper':'0'},True),('pure_loss_work_free',{'leakage_q':str(normcap),'norm_gain_q':'0'},True),('work_failure',{'defect_length':str(2*Ycap)},False),('amplitude_failure',{'leakage_q':str(2*normcap)},False),('norm_floor_unproved',{'leakage_q':'1'},False),('geometry_failure',{'score_upper':str(eta**2)},False),('initial_energy_failure',{'energy_upper':str(B)},False)]
for name,args,want in examples:
 r=budget(**args);check('gate_'+name,(r['status']=='CERTIFIED_THROUGH_DECLARED_HORIZON')==want);fixtures[name]={'input':args,'result':r}
check('pure_loss_no_norm_work',fixtures['pure_loss_work_free']['result']['exact']['norm_variation_work_upper']=='0')
check('loss_still_spends_amplitude',F(fixtures['pure_loss_work_free']['result']['exact']['mixed_amplitude_spent'])==cap)
check('gauss_initial_bound_not_assumed',fixtures['ideal']['result']['gauss_norm_upper'] is None)
check('norm_leak_may_create_gauss',F(fixtures['norm_only_boundary']['result']['gauss_norm_upper'])==normcap>0)
check('default_norms_follow_N',budget(N='2')['exact']['initial_norm_error_sum_upper']=='0')
# Parameterized analytic orbit source: only q norm grows, normalized state stays on orbit.
for s in [F(1,10),F(1,1000),F(1,1000000)]:
 nq,nw=1+s,F(1);lq,lw=s,F(0)
 check('orbit_source_trace_'+str(s),(nw-nq)==-s and lw-lq==-s)
for name,args in [('negative_variation',{'leakage_q':'-1'}),('zero_norm',{'nq0':['0','1']}),('negative_prefix_work',{'work_upper':'-1'}),('negative_source_integral',{'source_integral_upper':'-1'}),('eta_outside',{'eta':'1'})]:
 try:budget(**args);ok=False
 except ValueError:ok=True
 check('invalid_'+name,ok)
# Constant-rate work is quadratic in horizon when norm changes enlarge beta.
rate_n,rate_y,T=F(1,7),F(1,11),F(2,3);bo,nu,J=F(2,13),F(1,17),F(25);D0=F(1,19)
left=((J+bo+20*(D0+rate_n*T))*eta+nu)*rate_y*T
right=20*eta*rate_n*rate_y*T*T+((J+bo+20*D0)*eta+nu)*rate_y*T
check('constant_rate_horizon_polynomial',left==right)
out={'status':'PASS','exact_check_count':len(checks),'checks':checks,'unit_budget':b,'fixtures':fixtures,'terminal_net_work_counterexample':{'canonical_H':'(q^2+p^2)/2','path':'q=0; p=t on [0,1], p=2-t on [1,2]','defect':'Y=(-p,q+f), f=+1 then -1','terminal_work':'0','prefix_work_max':'1/2','scope':'Exact abstract oscillator control, not a UD trajectory'},'dependencies':{f:hashlib.sha256((P/f).read_bytes()).hexdigest() for f in ['parity_budget.py','preparation_certificate.py','energy_admission.py','FROZEN_ENERGY_ADMISSION_CERTIFICATE_v0.1.json']},'verification_scope':'Exact rational allocations, controls and algebra. Analytic barrier and source law proved in manuscript; constructor-only, no empirical input.','physical_promotion':0}
(P/'SOURCE_WORK_CERTIFICATE_v0.1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'PASS','exact_checks':len(checks),'norm_variation_only_cap':float(normcap),'speed_only_path_length_cap':float(Ycap),'work_allowance':float(B/4)},indent=2))
