"""Frozen ordered one-shot subprocess calls, no retry or case replacement."""
from pathlib import Path
import hashlib,json,subprocess,os
P=Path(__file__).resolve().parent;W=P.parent/'c14_campaign'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
f=json.loads((P/'FIT_DRIVER_FREEZE.json').read_text());assert sha(Path(__file__))==f['code_sha256'];assert sha(W/'CAMPAIGN_FREEZE.json')==f['campaign_freeze_sha256'];release=json.loads((W/'ALL_DATA_FIT_RELEASE.json').read_text());assert release['all_inputs_independently_checked']is True
with(P/'CAMPAIGN_FIT_INTENT.json').open('x')as h:json.dump({'all_data_release_sha256':sha(W/'ALL_DATA_FIT_RELEASE.json'),'case_order':f['case_order'],'maximum_estimator_calls':3,'retry_allowed':False},h,indent=2);h.write('\n')
rows=[];env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
for name in f['case_order']:
 case=W/'cases'/name
 with(P/(name+'_FIT_LOG.txt')).open('x')as h:
  r=subprocess.run(['python',str(case/'driver.py'),'fit','--repo',str(P.parent/'ud-repo'),'--raw',str(P.parent/'c14_raw'/(name+'.i64le')),'--execute-once'],env=env,stdout=h,stderr=subprocess.STDOUT)
 rows.append({'case':name,'one_subprocess_invocation':True,'returncode':r.returncode,'fit_intent_exists':(case/'FIT_INTENT.json').exists(),'run_executions_exists':(case/'RUN_EXECUTIONS.json').exists()});print(name,r.returncode,flush=True)
with(P/'CAMPAIGN_FIT_EXECUTIONS.json').open('x')as h:json.dump({'rows':rows,'retry_calls':0,'new_cases_selected':0},h,indent=2);h.write('\n')
