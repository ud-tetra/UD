from pathlib import Path
import argparse,subprocess,json,hashlib
ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--replay',action='store_true');a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);P=Path(__file__).resolve().parent;O=a.out;H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();run=lambda v:subprocess.run(list(map(str,v)),check=True)
run(['python',P/'c32_certify.py','--repo',a.repo,'--out',O/'math'])
C=a.repo/'captures/2026-10-21T015546Z-codex-native-actions-6a0c79b1';build=json.loads((C/'BUILD_RECEIPT.json').read_text());assert H(C/'c31_action.cpp')==build['source_sha256'];run(['c++','-O3','-std=c++17',C/'c31_action.cpp','-Wl,-l:libgmp.so.10','-o',O/'native_action']);b={'source_sha256':H(C/'c31_action.cpp'),'executable_sha256':H(O/'native_action')};(O/'BUILD_RECEIPT.json').write_text(json.dumps(b,indent=2)+'\n')
args=['python',P/'c32_construct.py','--slice',O/'math/TRIAL_SLICE.json','--slice-sha256',H(O/'math/TRIAL_SLICE.json'),'--operator',O/'math/OPERATOR.txt','--executable',O/'native_action','--build-receipt',O/'BUILD_RECEIPT.json']
run(args+['--out',O/'frame']);run(['python',P/'c32_partial_solve.py','--frame',O/'frame','--out',O/'solve'])
if a.replay:
 run(args+['--out',O/'frame_replay'])
 for q in(O/'frame').iterdir():assert q.read_bytes()==(O/'frame_replay'/q.name).read_bytes()
print('PASS partial16 construction/solve workflow; full1999 frame and reconstruction remainHOLD')
