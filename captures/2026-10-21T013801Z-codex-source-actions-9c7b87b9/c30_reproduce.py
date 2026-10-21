"""Rebuild and execute the new mathematical reference; archives are read as data."""
from pathlib import Path
import subprocess,argparse,shutil,json,hashlib
ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--integration',action='store_true');a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);here=Path(__file__).resolve().parent
run=lambda args:subprocess.run(list(map(str,args)),check=True)
run(['python',here/'c30_certify.py','--repo',a.repo,'--out',a.out/'c30_math'])
run(['c++','-O3','-std=c++17',here/'c30_action.cpp','-Wl,-l:libgmp.so.10','-o',a.out/'c30_action'])
build={'source_sha256':hashlib.sha256((here/'c30_action.cpp').read_bytes()).hexdigest(),'executable_sha256':hashlib.sha256((a.out/'c30_action').read_bytes()).hexdigest()};(a.out/'BUILD_RECEIPT.json').write_text(json.dumps(build,sort_keys=True)+'\n')
for n in ['c30_oracles.py']:shutil.copyfile(here/n,a.out/n)
S=2**96;x=[(((17*i+5)%31)-15)*S//32 for i in range(2640)];y=[(((13*i+7)%17)-8)*3*S//4 for i in range(253952)]
for n,v in [('c30_x.txt',x),('c30_x_boundary.txt',[128*t for t in x]),('c30_y.txt',y)]: (a.out/n).write_text(''.join(str(t)+'\n'for t in v))
# Root test driver binds the exact source bytes in this workspace.
shutil.copyfile(here/'c30_action.cpp',a.out/'c30_action.cpp')
for mode,src,dst in [('forward','c30_x.txt','c30_Fx.txt'),('forward','c30_x_boundary.txt','c30_Fxb.txt'),('adjoint','c30_y.txt','c30_Fty.txt')]:run([a.out/'c30_action',a.out/'c30_math/OPERATOR.txt',mode,a.out/src,a.out/dst])
run(['python',here/'c30_tests.py','--workspace',a.out,'--operator',a.out/'c30_math/OPERATOR.txt','--executable',a.out/'c30_action','--out',a.out/'tests'])
if a.integration:
 decoder=a.repo/'captures/2026-10-21T011432Z-codex-finite-decoder-cde7ea74/decoder.py'
 run(['python',here/'c30_integration.py','--workspace',a.out,'--operator',a.out/'c30_math/OPERATOR.txt','--executable',a.out/'c30_action','--build-receipt',a.out/'BUILD_RECEIPT.json','--decoder',decoder,'--out',a.out/'integration'])
print('Replay complete; compare ACTION_CONSTANTS.json, SOURCE_BINDINGS.json, OPERATOR.txt and tests/ACTION_TESTS.json against captured hashes.')
