#!/usr/bin/env python3
"""Independent final source, scalar consequence and five-file replay binding."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
P=Path(__file__).resolve().parent;W=P.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_text())
source_names=['c29_decoder.py','c29_certify.py','c29_reference_tests.py','c29_THEOREM.md'];src={n:sha(W/n)for n in source_names};freeze=load(W/'c29_INTERFACE_FREEZE.json')
assert all(src[n]==freeze['files'][n]for n in source_names[:3])
cert=load(W/'c29_math/RESULT.json');witness=load(W/'c29_math/POLYNOMIAL_WITNESS.json');refs=load(W/'c29_ref_final/REFERENCE_RESULTS.json');mine=load(P/'PARENT_REFERENCE_CHECKS.json');const=load(P/'REFERENCE_CHECKS.json')
assert src['c29_decoder.py']==refs['decoder_source_sha256']
assert mine['reference_result_sha256']==sha(W/'c29_ref_final/REFERENCE_RESULTS.json') and mine['small_operator_sha256']==sha(W/'c29_ref_final/SMALL_OPERATOR.json')
s=F(61,27648);N=8192;num=2*27587**N;den=27709**N
h=lambda x:hashlib.sha256(x.to_bytes((x.bit_length()+7)//8,'big')).hexdigest()
assert num*2**51<den and h(num)==witness['numerator_sha256_big_endian'] and h(den)==witness['denominator_sha256_big_endian']
assert num.bit_length()==witness['numerator_2_times_power_bits']and den.bit_length()==witness['denominator_power_bits']
assert F(cert['s'])==s and F(cert['a'])==s*s and F(cert['c'])==(1+s*s)/2 and F(cert['d'])==(1-s*s)/2
assert F(cert['Green_full_space_uniform_bound'].split('<')[0])==(1+s)**2/(2*s)
assert (1+F(1,2**51))/s<512 and 4/s+F(1,2**42)<2048
assert 2048+F(1,2**68)<2049 and 2640*F(1,2**160)<F(1,2**134)
parents=load(W/'c29_math/SOURCE_BINDINGS.json')
for item in parents.values():assert sha(W/'ud-repo'/item['path'])==item['sha256']
error=load(W/'ud-repo'/parents['error_result']['path']);D=F(error['conditional_example']['normalized_data_error_bound']);total=F(1,2**51)+512*D+11*F(1,2**46)
assert total==F(cert['conditional_C28_profile_total_upper']) and total<F(1,2**40)
assert cert['actual_600cell_decoder_execution']=='NOT_RUN_HOLD' and cert['factorized_action_contract']['actual_600cell_action_status']=='NOT_VALIDATED_HOLD'
replays={}
for folder,replay,names in [('c29_math','c29_math_replay',['RESULT.json','POLYNOMIAL_WITNESS.json','SOURCE_BINDINGS.json']),('c29_ref_final','c29_ref_replay',['REFERENCE_RESULTS.json','SMALL_OPERATOR.json'])]:
 for name in names:
  a=W/folder/name;b=W/replay/name;assert a.read_bytes()==b.read_bytes();replays[f'{folder}/{name}']={'primary_sha256':sha(a),'replay_sha256':sha(b),'byte_identical':True}
out={'status':'PASS_FINAL_SOURCE_CONSTANT_AND_FIVE_FILE_REPLAY_BINDING','root_source_sha256':src,'replay_bindings':replays,'parent_receipts_pinned_and_verified':parents,'conditional_C28_composed_error_upper':str(total),'independent_proxy_replay_receipt_sha256':sha(P/'PARENT_REFERENCE_CHECKS.json'),'scope':{'no_producer_or_reference_module_execution_by_reviewer':True,'full_actual600cell_decoder_or_oracles':'NOT_RUN_NOT_VALIDATED_HOLD','conditional_profile_inputs':'UNSUPPLIED_HOLD','physical_promotion':0,'external_review':'PENDING'}}
(P/'FINAL_BINDING.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'sources':src,'C28_total_float_display':float(total)}))
