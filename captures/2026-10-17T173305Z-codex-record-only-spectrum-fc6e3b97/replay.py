#!/usr/bin/env python3
"""Fresh complete record-only replay, optionally including the two full-size controls."""
import argparse,sys,shutil,time,json,subprocess,os,resource
from pathlib import Path
P=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('destination');p.add_argument('--record',help='Optional existing raw record; otherwise restore bundled lossless input');p.add_argument('--controls',action='store_true');a=p.parse_args();D=Path(a.destination).resolve();D.mkdir(exist_ok=False,parents=True)
for n in ['propose_record.py','certify_record.py','proof_math.py','record_codec.py','perturbation_controls.py','robustness.py','test_record.py']:shutil.copy2(P/n,D/n)
shutil.copy2(P/'inputs/FROZEN_CONTRACT.json',D/'FROZEN_CONTRACT.json');env=dict(os.environ,OPENBLAS_NUM_THREADS='1');start=time.monotonic();stages=[]
def run(cmd,name):
 t=time.monotonic()
 with (D/(name+'.log')).open('w') as out:subprocess.run([sys.executable,'-u',*map(str,cmd)],stdout=out,stderr=subprocess.STDOUT,env=env,check=True)
 stages.append({'stage':name,'seconds':time.monotonic()-t});print(stages[-1],flush=True)
record=Path(a.record).resolve() if a.record else D/'normalized_history.i64le'
if not a.record:run([D/'record_codec.py','restore',P/'codec',record],'restore')
run([D/'propose_record.py',record,D/'FROZEN_CONTRACT.json',D/'output'],'propose')
run([D/'certify_record.py',record,D/'FROZEN_CONTRACT.json',D/'output/PROPOSAL.npz',D/'certified-v02'],'certify')
cert=json.loads((D/'certified-v02/CERTIFICATE.json').read_text())
if cert['status']=='CERTIFIED_NUMERIC_RECORD_SIGNATURE':
 run([D/'robustness.py',D/'certified-v02/CERTIFICATE.json',D/'FROZEN_CONTRACT.json',D/'ROBUSTNESS.json'],'robustness')
 run([D/'test_record.py','--record',record,'--contract',D/'FROZEN_CONTRACT.json','--proposal',D/'output/PROPOSAL.npz','--certificate',D/'certified-v02/CERTIFICATE.json','--result',D/'TEST_RESULTS.json'],'tests')
 if a.controls:run([D/'perturbation_controls.py',record,D/'certified-v02/CERTIFICATE.json',D/'FROZEN_CONTRACT.json',D/'controls'],'controls')
result={'status':cert['status'],'seconds':time.monotonic()-start,'peak_child_rss_kib':resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,'stages':stages,'physical_promotion':0,'independent_review':'pending'};(D/'REPLAY_RESULT.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
