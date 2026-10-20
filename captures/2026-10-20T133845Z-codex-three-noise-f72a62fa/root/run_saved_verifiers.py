"""Fixed per-case exact saved-tuple verification or zero-fit replay, no estimation."""
from pathlib import Path
import argparse,hashlib,json,subprocess,os
P=Path(__file__).resolve().parent;W=P.parent/'c14_campaign';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
a=argparse.ArgumentParser();a.add_argument('stage',choices=['primary','replay']);mode=a.parse_args().stage
f=json.loads((P/'VERIFIER_DRIVER_FREEZE.json').read_text());assert sha(Path(__file__))==f['code_sha256'];assert sha(W/'CAMPAIGN_FREEZE.json')==f['campaign_freeze_sha256'];rows=[]
with(P/(mode.upper()+'_VERIFIER_INTENT.json')).open('x')as h:json.dump({'stage':mode,'case_order':f['case_order'],'new_estimator_calls':0,'no_retry':True},h,indent=2);h.write('\n')
for name in f['case_order']:
 case=W/'cases'/name;out=P.parent/('c14_'+mode)/name;out.parent.mkdir(exist_ok=True)
 with(P/(name+'_'+mode.upper()+'_LOG.txt')).open('x')as h:r=subprocess.run(['python',str(case/'certify.py'),'--repo',str(P.parent/'ud-repo'),'--raw',str(P.parent/'c14_raw'/(name+'.i64le')),'--out',str(out)],env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1'),stdout=h,stderr=subprocess.STDOUT)
 rows.append({'case':name,'stage':mode,'returncode':r.returncode,'certificate_sha256':sha(out/'CERTIFICATE.json')if(out/'CERTIFICATE.json').exists()else None});print(name,mode,r.returncode,flush=True)
with(P/(mode.upper()+'_VERIFIER_EXECUTIONS.json')).open('x')as h:json.dump({'rows':rows,'new_estimator_calls':0,'no_retries':True},h,indent=2);h.write('\n')
