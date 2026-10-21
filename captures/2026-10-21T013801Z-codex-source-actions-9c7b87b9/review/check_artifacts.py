#!/usr/bin/env python3
"""Independent finite full-action consistency, prefix and integration binding."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,importlib.util
P=Path(__file__).resolve().parent;W=P.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_text());read=lambda p:list(map(int,p.read_text().split()));S=2**96
mine=load(P/'SOURCE_BOUND_CHECKS.json');C=load(W/'c30_math/ACTION_CONSTANTS.json');B=load(W/'c30_BUILD_RECEIPT.json');freeze=load(W/'c30_FINAL_FREEZE.json')
for f,h in freeze['files'].items():assert sha(W/f)==h
for key,ownkey in [('tau','Taylor_tail'),('rounding_halfstep_error_bound','summed_step_round_strict_upper'),('accumulated_state_error_bound','global4096_propagation_error_upper'),('forward_error_upper','forward_absolute_error_upper'),('adjoint_error_upper','adjoint_absolute_error_upper')]:assert F(C[key])==F(mine[ownkey])
assert C['source_operator_sha256']==mine['operator_sha256'] and B['source_sha256']==sha(W/'c30_action.cpp')and B['executable_sha256']==sha(W/'c30_action')
test=load(W/'c30_test_build/ACTION_TESTS.json');x=read(W/'c30_x.txt');xb=read(W/'c30_x_boundary.txt');y=read(W/'c30_y.txt');fx=read(W/'c30_Fx.txt');fxb=read(W/'c30_Fxb.txt');fty=read(W/'c30_Fty.txt')
assert len(x)==len(xb)==len(fty)==2640 and len(y)==len(fx)==len(fxb)==253952
assert xb==[128*v for v in x]
ef=F(C['forward_error_upper']);et=F(C['adjoint_error_upper']);dual=F(sum(a*b for a,b in zip(fx,y))-sum(a*b for a,b in zip(x,fty)),S*S);scale=F(sum((a-128*b)**2 for a,b in zip(fxb,fx)),S*S)
assert dual==F(test['duality_residual'])and abs(dual)<ef*2049+et*16
assert scale==F(test['scale128_discrepancy_squared'])and scale<(129*ef)**2
for i,(ip,op,norm)in enumerate([('c30_x.txt','c30_Fx.txt',sum(v*v for v in x)),('c30_x_boundary.txt','c30_Fxb.txt',sum(v*v for v in xb)),('c30_y.txt','c30_Fty.txt',sum(v*v for v in y))]):
 item=test['actual_full_actions'][i];assert sha(W/ip)==item['input_sha256']and sha(W/op)==item['output_sha256']and F(norm,S*S)==F(item['input_norm_squared'])
# Check actual forwardj0,1,2 against an independent internal-grid Taylor.
words=list(map(int,(W/'c30_source/OPERATOR.txt').read_text().split()));obs=words[5:67];rows=[[]for _ in range(2640)]
for j in range(68,len(words),3):i,k,v=words[j:j+3];rows[i].append((k,v))
def trunc(x,n):return (1 if x>=0 else -1)*(abs(x)//n)
def half(v):
 t=v[:];out=v[:]
 for k in range(1,41):
  t=[trunc(sum(w*t[j]for j,w in row),4*k)for row in rows];out=[a+b for a,b in zip(out,t)]
 return out
prefix=0
for seed,out in [(x,fx),(xb,fxb)]:
 state=[v*2**32 for v in seed]
 for j in range(3):
  assert [trunc(state[i],2**38)for i in obs]==out[j*62:(j+1)*62];prefix+=62
  if j<2:state=half(state)
# Actual source- and build-bound adapter failure probes; no full trajectory is run.
spec=importlib.util.spec_from_file_location('independent_adapter_probe',W/'c30_oracles.py');O=importlib.util.module_from_spec(spec);spec.loader.exec_module(O)
O.SourceActions(W/'c30_source/OPERATOR.txt',W/'c30_action',B['executable_sha256'])
bad=P/'work/changed_operator.txt';bad.write_bytes((W/'c30_source/OPERATOR.txt').read_bytes()+b'\n');neg=[]
for op,exeh in [(bad,B['executable_sha256']),(W/'c30_source/OPERATOR.txt','0'*64)]:
 try:O.SourceActions(op,W/'c30_action',exeh)
 except ValueError:neg.append(True)
 else:raise AssertionError('false binding accepted')
A=O.SourceActions(W/'c30_source/OPERATOR.txt',W/'c30_action',B['executable_sha256'])
try:A.forward([2049*S]+[0]*2639)
except ValueError:neg.append(True)
else:raise AssertionError('out of domain accepted')
# Bind the completed actual2640-stateN2 integration without calling it a convergence test.
integ=load(W/'c30_integration_final/INTEGRATION.json');out=W/'c30_integration_final/OUTPUT.txt';assert sha(out)==integ['output_sha256']==freeze['integration_output_sha256'];assert out.read_bytes()==(W/'c30_integration_results/OUTPUT.txt').read_bytes()
assert integ['executable_sha256']==sha(W/'c30_action')and integ['build_receipt_sha256']==sha(W/'c30_BUILD_RECEIPT.json')and integ['adapter_source_sha256']==sha(W/'c30_oracles.py')
assert integ['steps']==2 and integ['actual_forward_actions']==1 and integ['actual_adjoint_actions']==2 and not integ['full8192_accuracy_claim']
assert integ['decoder_receipt']['whole_step_coordinates_checked']==5280 and integ['decoder_receipt']['state_dimension']==2640 and integ['source_decoder_sha256']=='705808468795a308ee47b9f4cdb6a156307d9205ccda81975d4442ccecde5bf5'
data=[(((13*i+7)%17)-8)*3*S//4096 for i in range(253952)];assert sum(v*v for v in data)==int(integ['data_norm_squared_dyadic_numerator'])<(2*S)**2
replays={}
for p,q in [('c30_math/ACTION_CONSTANTS.json','c30_math_replay/ACTION_CONSTANTS.json'),('c30_math/SOURCE_BINDINGS.json','c30_math_replay/SOURCE_BINDINGS.json'),('c30_math/OPERATOR.txt','c30_math_replay/OPERATOR.txt'),('c30_Fxb.txt','c30_Fxb_replay.txt'),('c30_Fty.txt','c30_Fty_replay.txt'),('c30_test_build/ACTION_TESTS.json','c30_test_build_replay/ACTION_TESTS.json')]:
 assert (W/p).read_bytes()==(W/q).read_bytes();replays[p]={'sha256':sha(W/p),'byte_identical':True}
for file,output in [('c30_forward_runtime.json','c30_Fxb.txt'),('c30_adjoint_runtime.json','c30_Fty.txt')]:
 r=load(W/file);assert r['output_sha256']==sha(W/output)and r['executable_sha256']==B['executable_sha256']and r['wall_seconds']>0 and r['peak_child_rss_kib']>0
result={'status':'PASS_INDEPENDENT_ACTUAL_ACTION_CONSISTENCY_AND_INTEGRATION_BINDING','source_hashes':freeze['files'],'backend_binary_sha256':B['executable_sha256'],'build_receipt_sha256':sha(W/'c30_BUILD_RECEIPT.json'),'five_exact_error_constant_pairs_match':True,'forward_prefix_components_independently_compared':prefix,'fullsize_duality_residual':str(dual),'fullsize_scale128_discrepancy_squared':str(scale),'binding_and_domain_adapter_failure_probes':len(neg),'integration_receipt_sha256':sha(W/'c30_integration_final/INTEGRATION.json'),'integration_output_sha256':sha(out),'integration_fullstate_dimension':2640,'integration_steps':2,'integration_Arb_coordinate_checks':5280,'final_integration_output_matches_initial_numerical_run':True,'six_replay_pairs':replays,'scope':{'producer_checker_and_test_driver_not_executed_by_reviewer':True,'actual_adapter_imported_only_for_binding_and_invalid_domain_probes':True,'no_second_fulltrajectory_or_decoder_run_by_reviewer':True,'runtime_receipts_hashbound_not_independent_timing_measurement':True,'GMP_compiler_build_trust_and_stable_files_remain_assumptions':True,'full8192_decoder_accuracy':'NOT_RUN_HOLD','physical_promotion':0,'external_review':'PENDING'}}
(P/'ARTIFACT_CHECKS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':result['status'],'prefix_components':prefix,'failure_probes':len(neg),'replay_pairs':len(replays)}))
