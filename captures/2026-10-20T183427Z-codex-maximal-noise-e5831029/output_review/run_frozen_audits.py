"""Ordered, once-only invocation of frozen independent auditors; zero estimator calls."""
from pathlib import Path
import json,time,subprocess,os,hashlib
P=Path(__file__).resolve().parent;W=P.parent;names=('boundary_pair_block','boundary_pair_rotating');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();rows=[]
with(P/'ACTUAL_AUDIT_INVOCATION_INTENT.json').open('x')as out:json.dump({'case_order':names,'new_estimator_calls':0,'audits_per_case':1,'retry_allowed':False,'frozen_driver_sha256':sha(P/'review_post.py'),'post_driver_freeze_sha256':sha(P/'POST_DRIVER_FREEZE.json')},out,indent=2);out.write('\n')
for name in names:
 primary=W/'c15_primary'/name;start=time.monotonic()
 while not all((primary/f).is_file()for f in ['CERTIFICATE.json','RESOURCE.json']):
  if time.monotonic()-start>600:raise TimeoutError('primary not complete for fixed case '+name)
  time.sleep(2)
 print('AUDIT_START',name,flush=True)
 case=W/'c15_campaign/cases'/name;log=P/(name+'_AUDIT_LOG.txt')
 with log.open('x')as out:
  cmd=['python',str(P/'review_post.py'),'--repo',str(W/'ud-repo'),'--case',name,'--producer',str(case),'--baseline',str(W/'c15_baseline_recovery/ramp_clock_stress.i64le'),'--raw',str(W/'c15_raw'/f'{name}.i64le'),'--primary',str(primary),'--fit-release',str(case/'ROOT_FIT_RELEASE.json'),'--data-review',str(W/'c15_input_review/data'/name/'DATA_REVIEW_RECEIPT.json'),'--out',str(P/name/'POST_REVIEW_RECEIPT.json')]
  r=subprocess.run(cmd,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1'),stdout=out,stderr=subprocess.STDOUT)
 rows.append({'case':name,'one_frozen_audit_invocation':True,'returncode':r.returncode,'new_estimator_calls':0,'log_sha256':sha(log)});print('AUDIT_FINISHED',name,r.returncode,flush=True)
with(P/'ACTUAL_AUDIT_INVOCATIONS.json').open('x')as out:json.dump({'rows':rows,'retry_invocations':0,'new_estimator_calls':0},out,indent=2);out.write('\n')
