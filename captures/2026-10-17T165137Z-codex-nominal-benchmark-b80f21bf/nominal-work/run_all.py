#!/usr/bin/env python3
"""Run every stage sequentially on an empty output directory."""
import os,time,json,subprocess,resource,platform,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
if (P/'output').exists():raise SystemExit('Output already exists. Replay in a fresh copy, preserving previous evidence.')
t=time.monotonic();env=dict(os.environ,OPENBLAS_NUM_THREADS='1');stages=[]
for name in ['benchmark_nominal.py','uniform_bounds.py','refine_certificate.py','benchmark_actions.py','test_method.py']:
 start=time.monotonic()
 with (P/(name+'.log')).open('w') as f:subprocess.run(['python','-u',str(P/name)],stdout=f,stderr=subprocess.STDOUT,env=env,check=True)
 stages.append({'stage':name,'seconds':time.monotonic()-start});print(stages[-1],flush=True)
import numpy,scipy,flint
r={'status':'PASS','total_wall_seconds':time.monotonic()-t,'peak_child_rss_kib':resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,'stages':stages,'python':platform.python_version(),'numpy':numpy.__version__,'scipy':scipy.__version__,'python_flint':flint.__version__,'openblas_threads':1,'dense_hankel_allocated':False,'executed_code_sha256':{n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in ['run_all.py']+[s['stage'] for s in stages]}}
(P/'output/PIPELINE_BENCHMARK.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2),flush=True)
