"""Constructor checks. Imports no archived code; numerical checks are labelled."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json, math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq
from flint import fmpz_mat, fmpz_poly

R=Path(__file__).resolve().parent
checks=[]
def ck(name,condition,scope='EXACT',**data):
    assert condition, (name,data)
    checks.append(dict(name=name,status='PASS',scope=scope,**data))
states=list(product([0,1],repeat=2))
for before,after in product(states,repeat=2):
    old=before[0]*before[1];new=after[0]*after[1]
    assert (old==1 and new==0)==(before==(1,1) and after!=(1,1))
    assert (old==0 and new==1)==(before!=(1,1) and after==(1,1))
ck('all_16_boolean_transitions',True)
ck('closed_state_has_three_factor_completions',sum(c*t==0 for c,t in states)==3)
ck('closure_receipt_conjunction',all(min(r)==math.prod(r) for r in product([0,1],repeat=3)))
capacity=F(7,768)
ck('historical_capacity_boundary_convention',[int(b<=capacity) for b in [F(1,128),capacity,F(1,96)]]==[1,1,0])
# Same initial open factors, two lawful histories in the supplied product-only theory.
hold=[(1,1)]*4;pulse=[(1,1),(0,1),(0,1),(1,1)]
ck('product_only_update_nonidentifiability',hold[0]==pulse[0] and [c*t for c,t in hold]!=[c*t for c,t in pulse])
# An isolated endpoint pair: z'=-2*kappa*h*z. Closing freezes z.
kappa=F(1,4);z=F(2);ell=F(1)
ck('isolated_closed_overload_cannot_self_clear',-2*kappa*0*z==0 and z>ell)
# Equal stocks need not give equal signed readiness; B=(1,-1).
ck('stocks_do_not_select_signed_readiness',1**2+1**2==1**2+(-1)**2 and (1-1)**2!=(1-(-1))**2)
D=json.loads((R/'COMPLEX_AND_ACTION.json').read_text())
V=D['vertices'];edges=[tuple(e) for e in D['simplices'][1]];n=len(V)
B=np.zeros((n,len(edges)),dtype=np.int64)
for j,(u,v) in enumerate(edges):B[u,j]=-1;B[v,j]=1
e=598;u,v=edges[e];be=B[:,e];L=B@B.T;Lc=L-np.outer(be,be)
ck('600_cell_graph_dimensions',B.shape==(120,720))
ck('regular_degree_twelve',np.all(np.diag(L)==12))
ck('one_edge_cut_rank_one_laplacian',np.array_equal(Lc,B[:,[j for j in range(720) if j!=e]]@B[:,[j for j in range(720) if j!=e]].T))
ck('cut_still_has_constant_kernel',np.array_equal(Lc@np.ones(n,dtype=np.int64),np.zeros(n,dtype=np.int64)))
seen={u};todo=[u]
while todo:
    i=todo.pop()
    for j in np.flatnonzero(Lc[i]<0):
        if int(j) not in seen:seen.add(int(j));todo.append(int(j))
ck('alternate_paths_keep_graph_connected',len(seen)==120)
site_b=[F(1,128)]*n;site_b[u]=F(1,96)
admit=[int(b<=capacity) for b in site_b]
edge_h=[admit[i]*admit[j] for i,j in edges]
ck('capacity_veto_on_every_incident_edge_strands_overload',all(edge_h[j]==0 for j,(i,k) in enumerate(edges) if u in (i,k)) and sum(F(int(B[u,j]))*(-kappa*edge_h[j]*(site_b[k]-site_b[i])) for j,(i,k) in enumerate(edges))==0)
p=fmpz_poly([0,1])
expected=p*((p-10)**2-20)**9*((p-9)**2-45)**4*(p-9)**16*(p-14)**36*(p-15)**16*(p-12)**25
actual=fmpz_mat(L.tolist()).charpoly()
ck('exact_full_vertex_laplacian_characteristic_polynomial',actual==expected,polynomial=str(expected))
# sqrt(5) in (2236/1000,2237/1000); these rational inequalities certify
# 9-3sqrt(5)>2; the smallest remaining candidate is 10-2sqrt(5).
slo=F(2236,1000);shi=F(2237,1000)
ck('exact_spectral_order_and_positive_cut_lower_bound',slo*slo<5<shi*shi and 9-3*shi>2 and 10-2*shi>9-3*slo and 10+2*shi<15 and 9+3*shi<16 and 9+3*shi>15)
# The maximum is 9+3sqrt(5). Use a safe exact bound 16 below.
ck('safe_exact_laplacian_upper_bound_sixteen',9+3*shi<16 and 10+2*shi<16)
ck('edge_vector_norm_and_cut_initial_rate',int(be@be)==2 and int(be@Lc@be)==22)
ck('gate_metric_jump_at_fixed_amplitude',all((hp-hm)*F(9,4)==(hp*F(3,2))**2-(hm*F(3,2))**2 for hm,hp in product([0,1],repeat=2)))
beta=7-3*math.sqrt(5);q0=2.;ellf=1.
def q(t):return float((q0/2)*be@expm(-.25*t*Lc)@be)
upper=math.log(q0/ellf)/(.25*beta);lower=math.log(q0/ellf)/4
tau=brentq(lambda t:q(t)-ellf,0,upper,xtol=1e-12)
ck('cut_recovery_crossing_and_bracket',lower<=tau<=upper and abs(q(tau)-ellf)<1e-9,'NUMERICAL',tau=tau,lower_bound=lower,upper_bound=upper)
times=np.linspace(0,tau,9);vals=[q(t) for t in times]
ck('aligned_recovery_curve_and_exponential_bounds',all(vals[i]>vals[i+1] for i in range(8)) and all(q0*math.exp(-4*t)-1e-10<=w<=q0*math.exp(-.25*beta*t)+1e-10 for t,w in zip(times,vals)),'NUMERICAL')
# Strict upper-bound compatibility with the previous Taylor selection window.
tstar=1/math.sqrt(8640)
ck('factor_two_hysteresis_exceeds_certified_window',lower>tstar,'NUMERICAL',selection_window_upper=tstar,lower_recovery_bound=lower)
ck('no_op_at_constant_mask_and_fixed_state',F(0)*F(9,4)==0)
out={'checks':checks,'exact_count':sum(c['scope']=='EXACT' for c in checks),'numerical_count':sum(c['scope']=='NUMERICAL' for c in checks),'physical_promotion':0,'status':'DEVELOPMENT_NO_REGISTRY_ENTRY','candidate_recovery':{'edge':e,'endpoints':[u,v],'kappa':str(kappa),'q0':q0,'ell':ellf,'tau':tau,'beta':beta},'scope':'Finite algebra and conditional recovery model only; no native trigger, burden-to-factor map, physical clock, or independent review.'}
(R/'NATIVE_GATE_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='checks'},indent=2))
