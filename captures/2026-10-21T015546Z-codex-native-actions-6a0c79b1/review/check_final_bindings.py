"""Bind final finite artifacts and independent scalar calculations, without re-executing producer drivers."""
from pathlib import Path
from fractions import Fraction as Q
import hashlib,json
P=Path(__file__).resolve().parent;W=P.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
own=json.loads((P/'BOUND_CHECKS.json').read_text());root=json.loads((W/'c31_math/NATIVE_CONSTANTS.json').read_text())
fields={'tau':'tau','step_rounding':'rounding_halfstep_error','accumulated_error':'accumulated_state_error','forward_error':'forward_error_upper','adjoint_error':'adjoint_error_upper'}
for a,b in fields.items():assert Q(*own['exact'][a])==Q(root[b])
freeze=json.loads((W/'c31_NATIVE_FREEZE.json').read_text());build=json.loads((W/'c31_BUILD_RECEIPT.json').read_text())
assert freeze['source_sha256']==build['source_sha256']==sha(W/'c31_action.cpp')
assert freeze['executable_sha256']==build['executable_sha256']==sha(W/'c31_action')
for v in ['NATIVE_CHECKS_v2.json','REJECTION_CHECKS.json']:
 r=json.loads((P/v).read_text());assert r['source_bindings']['source']==sha(W/'c31_action.cpp') and r['source_bindings']['executable']==sha(W/'c31_action')
old=(W/'c31_action_initial.cpp').read_text();new=(W/'c31_action.cpp').read_text();assert old.replace('int ne;f>>ne;if(ne!=14880)','int ne=0;if(!(f>>ne)||ne!=14880)')==new
replays=[]
for name in ['Fxb','Fty']:
 assert (W/f'c31_{name}.txt').read_bytes()==(W/f'c31_{name}_final.txt').read_bytes()
 replays.append({'name':name,'sha256':sha(W/f'c31_{name}_final.txt'),'initial_final_exact_match':True})
timing=[]
for mode in ['forward','adjoint']:
 p=W/f'c31_{mode}_final_runtime.json';r=json.loads(p.read_text());assert r['executable_sha256']==build['executable_sha256'];assert 'wait4 specific action child' in r['measurement']
 suffix='Fxb' if mode=='forward' else 'Fty';assert r['output_sha256']==sha(W/f'c31_{suffix}_final.txt')
 timing.append({'mode':mode,'receipt_sha256':sha(p),'wall_seconds_observed':r['wall_seconds'],'specific_child_peak_rss_kib':r['peak_child_rss_kib']})
integration=W/'c31_integration_results/INTEGRATION.json';r=json.loads(integration.read_text());out=W/'c31_integration_results/OUTPUT.txt';values=list(map(int,out.read_text().split()));assert len(values)==2640 and r['output_sha256']==sha(out)
assert r['status']=='PASS_ACTUAL2640_STATE_SIXTEEN_STEP_DECODER_INTEGRATION' and r['steps']==16 and r['actual_forward_actions']==15 and r['actual_adjoint_actions']==16 and r['full8192_accuracy_claim'] is False
assert r['decoder_receipt']['whole_step_coordinates_checked']==42240
assert r['executable_sha256']==build['executable_sha256'] and r['build_receipt_sha256']==sha(W/'c31_BUILD_RECEIPT.json')
assert r['adapter_source_sha256']==sha(W/'c30_oracles.py') and r['source_decoder_sha256']==sha(W/'c29_decoder.py')
y=[3*(((13*i+7)%17)-8)*2**84 for i in range(253952)]
assert sum(x*x for x in y)==int(r['data_norm_squared_dyadic_numerator']) and sum(x*x for x in y)<(2*2**96)**2
sources=['c31_action.cpp','c31_certify.py','c31_run_timed.py','c31_integration.py','c30_oracles.py','c29_decoder.py','c31_THEOREM.md']
result={'status':'PASS','source_hashes':{f:sha(W/f) for f in sources},'scalar_fraction_matches':len(fields),'final_probe_and_rejection_bindings_match':True,'reader_diagnostic_only_delta_verified':True,'complete_action_replays':replays,'final_action_timings':timing,'integration':{'receipt_sha256':sha(integration),'output_sha256':sha(out),'steps':16,'forward_actions':15,'adjoint_actions':16,'whole_step_coordinate_checks':42240,'build_source_adapter_decoder_bindings_match':True,'data_norm_rule_independently_recomputed':True},'scope':{'producer_driver_not_executed_by_this_script':True,'does_not_independently_reexecute_whole_decoder':True,'raw_large_data_not_for_capture':True,'full8192_execution_not_claimed':True,'physical_promotion':0,'external_review':'PENDING'}}
(P/'FINAL_BINDING_CHECKS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':'PASS','sources':len(sources),'integration_steps':16}))
