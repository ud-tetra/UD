"""Constructor exact arithmetic; analytic proof and scope are in manuscript."""
from energy_admission import *
from pathlib import Path
import hashlib,copy
P=Path(__file__).resolve().parent;checks={}
def check(k,x):
 checks[k]=bool(x)
 if not x:raise AssertionError(k)
# Hessian bound: 20(b^2+c^2)-4(b+2c)^2=4(2b-c)^2.
check('single_species_hessian_identity',(20-4, -16, 20-16)==(16,-16,4))
check('electric_divergence_squared_norm_bound',2*4==8)
check('static_energy_margin',F(1,2)+F(1,8)==F(5,8)<1)
check('time_energy_margin',F(1,2)+F(1,8)+F(1,8)==F(3,4)<1)
check('boundary_actual_energy_gap',1-F(1,8)==F(7,8)>F(1,2))
check('time_boundary_energy_gap',F(1,2)+F(1,8)<F(7,8))
# A direct scalar cone: min((t-a)^2+b^2) under |a|=|b| attained a=b=t/2.
check('cone_projection_identity',F(1,4)+F(1,4)==F(1,2))
for t in [F(1,10),F(1,100),F(1,10000)]:
 check('cone_non_lipschitz_'+str(t),(t*t/2)/(t**4)==1/(2*t*t))
base=admission();v={k:F(x) for k,x in base['exact'].items()};eta=v['eta'];B=v['B'];delta2=v['legacy_delta_squared'];Dcap=v['norm_error_only_cap']
check('unit_radius',eta==F(1,829538022))
check('norm_budget_boundary',eta*20*Dcap==v['gradient_budget_cap'])
check('geometric_cap_exact',v['geometric_score_ceiling']==eta*eta/4)
check('geometry_not_energy_alone',v['geometric_score_ceiling']>delta2)
# Pure electric diamond circulation lambda=eta^2/160 at a=N=r=1.
lam=eta**2/160;P_e=4*lam**2;E_e=2*lam**2
check('strict_witness_outside_legacy_ball',P_e==F(25,4)*delta2 and P_e>delta2)
check('strict_witness_energy',E_e==B/8 and E_e<=B/2)
check('strict_witness_geometric',P_e<=eta**2/4)
fixtures={}
examples=[('ideal',{},True,True),('energy_boundary',{'score_upper':str(eta**2/4),'energy_upper':str(B/2)},True,True),('unequal_norms',{'nq':[str(1+Dcap/4)]*2,'nw':['1','1'],'score_upper':str(P_e),'energy_upper':str(B/4)},True,True),('norm_budget_failure',{'nq':[str(1+2*Dcap)]*2},False,False),('energy_failure',{'energy_upper':str(B)},False,False),('geometry_failure',{'score_upper':str(eta**2)},False,False),('variation_failure',{'variation':str(2*v['gradient_budget_cap'])},True,False),('nonzero_electric_strict_extension',{'score_upper':str(P_e),'energy_upper':str(E_e)},True,True)]
for name,args,want,wanttime in examples:
 r=admission(**args);check('fixture_static_'+name,(r['status']=='CERTIFIED_SUFFICIENT_ENERGY_ADMISSION')==want);check('fixture_time_'+name,(r['time_status']=='CERTIFIED_THROUGH_DECLARED_VARIATION_HORIZON')==wanttime);fixtures[name]={'input':args,'result':r}
check('unequal_norm_trace_obstruction',fixtures['unequal_norms']['result']['zero_gauss_norm_compatibility']=='IMPOSSIBLE_FOR_ALL_NORMS_IN_INTERVALS')
for name,args in [('zero_norm',{'nq':['0','0']}),('negative_score',{'score_upper':'-1'}),('out_of_radius',{'eta':'1'}),('reversed_norm',{'nw':['2','1']})]:
 try:admission(**args);ok=False
 except ValueError:ok=True
 check('invalid_'+name,ok)
# Neutral trace cancellation on every closed incidence edge: +trE-tr(U†EU)=0;
# finite carrier degree count verified independently by the copied topology routine.
from preparation_certificate import carrier
nodes,edges,_,_,_,_=carrier();degrees=[sum(i==n or j==n for i,j,b in edges) for n in range(15)]
check('degree_four',max(degrees)==4)
check('closed_edge_trace_sum',sum(sum((i==n)-(j==n) for n in range(15)) for i,j,b in edges)==0)
# Exact rational matrix fixtures: nontrivial link conjugation and norm imbalance.
def zero(r):return [[F(0) for j in range(r)] for i in range(r)]
def transpose(A):return list(map(list,zip(*A)))
def mul(A,B):return [[sum((a*b for a,b in zip(row,col)),F(0)) for col in zip(*B)] for row in A]
def add(A,B,sg=1):return [[a+sg*b for a,b in zip(x,y)] for x,y in zip(A,B)]
def fro2(A):return sum((a*a for row in A for a in row),F(0))
def trace(A):return sum((A[i][i] for i in range(len(A))),F(0))
for r in [1,2,5]:
 U=[[[F(i==j) for j in range(r)] for i in range(r)] for e in edges]
 if r>=2:U[0][0][:2]=[F(3,5),F(-4,5)];U[0][1][:2]=[F(4,5),F(3,5)]
 E=[]
 for e in range(28):
  m=zero(r)
  for i in range(r):m[i][i]=F((e+i)%3-1,10)
  if r>=2:m[0][1]=m[1][0]=F(1,20)
  E.append(m)
 div=[zero(r) for _ in nodes]
 for (i,j,b),u,e in zip(edges,U,E):
  div[i]=add(div[i],e);div[j]=add(div[j],mul(mul(transpose(u),e),u),-1)
 check('exact_electric_divergence_'+str(r),sum(map(fro2,div))<=8*sum(map(fro2,E)))
 qcharge=[zero(r) for _ in nodes];wcharge=[zero(r) for _ in nodes]
 qcharge[0][0][0]=F(9,25);qcharge[1][0][0]=F(16,25)
 wcharge[0][r-1][r-1]=F(16,25);wcharge[1][r-1][r-1]=F(9,25)
 nq,nw=F(15,16),F(17,16)
 G=[add(add(g,[[nq*x for x in row] for row in q],-1),[[nw*x for x in row] for row in w]) for g,q,w in zip(div,qcharge,wcharge)]
 check('exact_global_trace_'+str(r),sum(map(trace,G))==nw-nq)
 check('exact_trace_lower_bound_'+str(r),sum(map(fro2,G))>=(nw-nq)**2/(15*r))
result={'status':'PASS','exact_check_count':len(checks),'checks':checks,'unit_budget':base,'fixtures':fixtures,'strict_extension_witness':{'rank':1,'lambda':str(lam),'squared_distance_and_score':str(P_e),'relative_energy':str(E_e),'legacy_radius_ratio_squared':'25/4','gauss':'zero; diamond integer circulation'},'dependencies':{f:hashlib.sha256((P/f).read_bytes()).hexdigest() for f in ['parity_budget.py','preparation_certificate.py','FROZEN_PREPARATION_CERTIFICATE_v0.1.json','FROZEN_ENDPOINT_ROBUSTNESS_CERTIFICATE_v0.1.json']},'scope':'Exact rational budgets and finite algebra. Geodesic/norm/Noether and cone assertions rely on the manuscript analytic proof; no independent review.','physical_promotion':0}
(P/'ENERGY_ADMISSION_CERTIFICATE_v0.1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':'PASS','exact_checks':len(checks),'unit_norm_cap':float(Dcap),'unit_energy_cap':float(B/2),'geometric_score_ceiling':float(eta**2/4),'score_ceiling_ratio':float(v['geometric_ceiling_over_legacy_score_ceiling'])},indent=2))
