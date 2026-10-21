from pathlib import Path
import subprocess,argparse,json,hashlib,shutil
p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--integration',action='store_true');p.add_argument('--benchmark',action='store_true');a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False);here=Path(__file__).resolve().parent;O=a.out;run=lambda v:subprocess.run(list(map(str,v)),check=True);H=lambda q:hashlib.sha256(q.read_bytes()).hexdigest();parent=a.repo/'captures/2026-10-21T013801Z-codex-source-actions-9c7b87b9'
run(['python',here/'c31_certify.py','--repo',a.repo,'--out',O/'c31_math'])
for n in ['c31_action.cpp','c31_run_timed.py']:shutil.copyfile(here/n,O/n)
shutil.copyfile(parent/'c30_oracles.py',O/'c30_oracles.py');assert H(parent/'c30_action.cpp')=='c8bc21ef9edef1d60e98e48bb61044afae4a7d283700c4523969bb6f9755de27'
for src,exe in [(parent/'c30_action.cpp','c30_action'),(here/'c31_action.cpp','c31_action')]:run(['c++','-O3','-std=c++17',src,'-Wl,-l:libgmp.so.10','-o',O/exe])
(O/'c30_math').mkdir();shutil.copyfile(parent/'ACTION_CONSTANTS.json',O/'c30_math/ACTION_CONSTANTS.json')
S=2**96;x=[(((17*i+5)%31)-15)*4*S for i in range(2640)];y=[(((13*i+7)%17)-8)*3*S//4 for i in range(253952)]
for n,v in [('c30_x_boundary.txt',x),('c30_y.txt',y)]:(O/n).write_text(''.join(str(t)+'\n'for t in v))
for mode,inp,base,native0,native1 in [('forward','c30_x_boundary.txt','c30_Fxb.txt','c31_Fxb.txt','c31_Fxb_final.txt'),('adjoint','c30_y.txt','c30_Fty.txt','c31_Fty.txt','c31_Fty_final.txt')]:
 for exe,out in [('c30_action',base),('c31_action',native0),('c31_action',native1)]:run([O/exe,O/'c31_math/OPERATOR.txt',mode,O/inp,O/out])
build={'source_sha256':H(O/'c31_action.cpp'),'executable_sha256':H(O/'c31_action')};(O/'c31_BUILD_RECEIPT.json').write_text(json.dumps(build,sort_keys=True)+'\n')
run(['python',here/'c31_tests.py','--workspace',O,'--out',O/'conformance'])
if a.integration:run(['python',here/'c31_integration.py','--workspace',O,'--operator',O/'c31_math/OPERATOR.txt','--executable',O/'c31_action','--build-receipt',O/'c31_BUILD_RECEIPT.json','--decoder',a.repo/'captures/2026-10-21T011432Z-codex-finite-decoder-cde7ea74/decoder.py','--out',O/'integration'])
if a.benchmark:run(['python',here/'c31_benchmark.py','--workspace',O,'--out',O/'benchmark'])
print('Replay complete; compare exact bounds, conformance/output hashes. Build/time provenance may differ.')
