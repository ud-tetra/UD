#!/usr/bin/env python3
"""Independent full-step replay of the disclosed rotated rational proxy.
Does not import or execute the producer decoder or its reference driver.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
from flint import arb,ctx
P=Path(__file__).resolve().parent;W=P.parent;ctx.prec=192
refpath=W/'c29_ref_final/REFERENCE_RESULTS.json';op_path=W/'c29_ref_final/SMALL_OPERATOR.json'
expected=json.loads(refpath.read_text());op=json.loads(op_path.read_text())
mat=lambda a:[[F(x)for x in row]for row in a]
A=mat(op['normal_A']);Fmat=mat(op['F']);U=mat(op['U']);V=mat(op['V']);sv=[F(x)for x in op['singular_values']]
def tr(M):return list(map(list,zip(*M)))
def mv(M,v):return [sum((x*y for x,y in zip(row,v)),F(0))for row in M]
def mm(M,N):return [mv(tr(N),row)for row in M]
def norm2(v):return sum((x*x for x in v),F(0))
assert mm(tr(Fmat),Fmat)==A
I=[[F(i==j)for j in range(4)]for i in range(4)];assert mm(tr(U),U)==I and mm(tr(V),V)==I
h=[row[3]for row in V];assert mv(A,h)==[0]*4
s=F(61,27648);cap=F(1,2**67);noise=F(1,2**70);bits=96;scale=2**bits;c=(1+s*s)/2;d=(1-s*s)/2
ball=lambda x:arb(x.numerator)/x.denominator
floor=lambda x:(x.numerator*scale)//x.denominator
round_checks=0
def quant(z):
 global round_checks
 q=int((z*scale).mid().floor().unique_fmpz());assert abs(z-arb(q)/scale)<arb(1)/2**80;round_checks+=1;return q
cases=[]
for ei,(name,data,perturb)in enumerate([('weak_unit_data',[1,0,0,0],False),('rotated_hidden_and_inconsistent_data',[s/4,F(-1,6),F(1,5),F(1,7)],False),('coherent_hidden_oracle_errors',[1,0,0,0],True)]):
 data=[F(floor(x),scale)for x in mv(U,data)];assert norm2(data)<4;gtrue=mv(tr(Fmat),data);g=[F(floor(x+(noise*y if perturb else 0)),scale)for x,y in zip(gtrue,h)]
 ge=norm2([x-y for x,y in zip(g,gtrue)]);assert ge<=cap*cap
 prev=[F(0)]*4;cur=[F(quant(ball(x)/ball(c)),scale)for x in g];rho=ball(d/c);maxerr=F(0)
 for k in range(1,8192):
  exact=mv(A,cur);av=[F(floor(x-(noise*y if perturb else 0)),scale)for x,y in zip(exact,h)];maxerr=max(maxerr,norm2([x-y for x,y in zip(exact,av)]));assert maxerr<=cap*cap
  nr=1/(2*ball(c/d)-rho);assert 0<nr<1
  # Independently regrouped Chebyshev update, with exact dyadic state values.
  # This expression is algebraically identical to the momentum/residual form.
  nxt=[]
  for i in range(4):
   z=(2*nr/ball(d))*(ball(c)*ball(cur[i])-ball(av[i])+ball(g[i]))-nr*rho*ball(prev[i])
   nxt.append(F(quant(z),scale))
  prev,cur=cur,nxt;rho=nr;assert norm2(cur)<2048**2
 yi=mv(tr(U),data);target=mv(V,[x/t if t else F(0)for x,t in zip(yi,sv)]);err=norm2([x-y for x,y in zip(cur,target)]);bound=2*F(1,2**51)/s+11*F(1,2**46);assert err<bound*bound
 item=expected['full_8192_cases'][ei];assert item['name']==name
 assert ge==F(item['g_error_squared'])and maxerr==F(item['max_normal_action_error_squared'])
 assert [int(x*scale)for x in cur]==item['output_dyadic_integers']
 assert err==F(item['final_error_squared'])and target==[F(x)for x in item['reference_minimum_norm_output']]
 cases.append({'name':name,'all8192_updates_independently_recomputed':True,'normal_oracle_error_audits':8191,'final_dyadic_state_matches':True,'recorded_norms_match':True,'hidden_output_matches':sum((x*y for x,y in zip(cur,h)),F(0))==F(item['computed_hidden_component'])})
result={'status':'PASS_INDEPENDENT_ALL_THREE_ROTATED_PROXY_REPLAYS','cases':cases,'whole_coordinate_error_checks':round_checks,'normal_action_error_audits':8191*3,'reference_result_sha256':hashlib.sha256(refpath.read_bytes()).hexdigest(),'small_operator_sha256':hashlib.sha256(op_path.read_bytes()).hexdigest(),'scope':{'producer_module_or_reference_driver_not_executed':True,'reordered_equivalent_Chebyshev_update_used':True,'actual_weighted600cell_actions':'NOT_RUN_NOT_VALIDATED','no_actual_floating_estimator_conformance_claim':True,'physical_promotion':0,'external_review':'PENDING'}}
(P/'PARENT_REFERENCE_CHECKS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':result['status'],'coordinate_checks':round_checks}))
