#!/usr/bin/env python3
import hashlib,json,os,subprocess,sys
from pathlib import Path
P=Path(__file__).resolve().parent;B=P.parent;RUN=B/'c22_runner';SRC=P/'executions/exact_q1';OUT=P/'toy_replay'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files=['ROLLUP.json','identity/SCREEN.json','numerical/CERTIFICATE.json','numerical/WITNESS.json.gz','audit/CERTIFICATE.json']
before={n:sha(SRC/n)for n in files};source={n:sha(RUN/n)for n in ['run_submission.py','SEAL.json','DEPENDENCIES.json','PROTOCOL.json']}
r=subprocess.run([sys.executable,str(RUN/'run_submission.py'),'--repo',str(B/'ud-repo'),'--manifest',str(P/'fixtures/exact_q1/manifest.json'),'--out',str(OUT)],capture_output=True,text=True,timeout=60,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1'})
assert r.returncode==0,(r.stdout,r.stderr)
rows=[]
for n,h in before.items():assert sha(SRC/n)==h and (SRC/n).read_bytes()==(OUT/n).read_bytes();rows.append({'path':n,'sha256':h,'byte_identical':True})
assert source=={n:sha(RUN/n)for n in source}
result={'status':'PASS_TOY_FULL_HANDOFF_BYTE_REPLAY','scientific_files_plus_rollup':5,'results':rows,'excluded':['PROCESS.json timing/log files','RESOURCE.json timing files'],'new_estimator_calls':0,'physical_promotion':0,'external_promotion_review':'PENDING'}
(P/'TOY_REPLAY_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':result['status'],'files':5}))
