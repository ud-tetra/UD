#!/usr/bin/env python3
"""Independent exact signed-division probes of the actual compiled half-step."""
from pathlib import Path
import subprocess,json,hashlib
P=Path(__file__).resolve().parent;W=P.parent;work=P/'work';work.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();op=W/'c30_source/OPERATOR.txt';exe=W/'c30_action';cpp=W/'c30_action.cpp';bound=json.loads((P/'SOURCE_BOUND_CHECKS.json').read_text());assert sha(op)==bound['operator_sha256'];initial=(sha(exe),sha(cpp),sha(op))
nums=list(map(int,op.read_text().split()));assert nums[:5]==[2640,62,4096,40,128];rows=[[]for _ in range(2640)]
for k in range(68,len(nums),3):i,j,c=nums[k:k+3];rows[i].append((j,c))
def divzero(x,d):return x//d if x>=0 else -((-x)//d)
def exact_step(inp,sign):
 term=[x*2**32 for x in inp];out=term[:]
 for k in range(1,41):
  term=[divzero(sign*sum(w*term[j]for j,w in row),4*k)for row in rows]
  out=[x+y for x,y in zip(out,term)]
 return [divzero(x,2**32)for x in out]
scale=2**96;zero=[0]*2640;dense=[(((i*i*73+19*i+5)%129)-64)*2**84 for i in range(2640)];boundary=[0]*2640;boundary[2040]=2048*scale
cases=[];abi=set()
for name,seed in [('zero',zero),('dense_signed',dense),('selected_tetrahedron_domain_boundary',boundary)]:
 assert sum(x*x for x in seed)<=(2048*scale)**2
 inp=work/f'{name}.txt';inp.write_text(''.join(f'{x}\n'for x in seed))
 for sign,mode in [(1,'step+'),(-1,'step-')]:
  outpath=work/f'{name}_{sign}.txt';proc=subprocess.run([str(exe),str(op),mode,str(inp),str(outpath)],text=True,capture_output=True,check=False)
  assert proc.returncode==0 and f'PASS {mode}'in proc.stdout
  assert 'GMP 6.3.0 longbits=64'in proc.stderr;abi.add(proc.stderr.strip())
  actual=list(map(int,outpath.read_text().split()));expected=exact_step(seed,sign);assert actual==expected and len(actual)==2640
  cases.append({'name':name,'mode':mode,'output_components_compared':len(actual),'all_exact_match':True,'input_sha256':sha(inp),'output_sha256':sha(outpath)})
assert initial==(sha(exe),sha(cpp),sha(op))
result={'status':'PASS_ACTUAL_COMPILED_HALFSTEP_INDEPENDENT_PYTHON_BIGINT_PROBES','cases':cases,'actual_output_components_compared':2640*len(cases),'independent_Python_reference_term_divisions_evaluated':40*2640*len(cases),'backend_binary_sha256':initial[0],'backend_source_sha256':initial[1],'operator_sha256':initial[2],'abi_runtime_probe':sorted(abi),'stable_source_and_binary_endpoint_hashes_match':True,'scope':{'actual_compiled_backend_executed_on_own_synthetic_seeds':True,'producer_python_test_or_prepare_script_not_executed':True,'Python_integer_division_uses_explicit_truncation_toward_zero':True,'actual_Cplusplus_intermediate_terms_not_exported_or_claimed_compared':True,'finite_backend_tests_not_universal_ABI_or_all_input_formal_proof':True,'full8192_decoder_not_run':True,'physical_promotion':0,'external_review':'PENDING'}}
(P/'BACKEND_CHECKS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':result['status'],'actual_components':result['actual_output_components_compared']}))
