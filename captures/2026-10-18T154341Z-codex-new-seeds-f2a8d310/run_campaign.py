from pathlib import Path
import json,subprocess,sys,time
from bindings import P,sha,check_freeze
f=check_freeze();assert (P/'DATA_FREEZE.json').exists();runs=[];outcomes=[]
for e in f['cases']:
 n=e['case'];record=P/f'records/{n}.i64le';r=next(r for r in json.loads((P/'DATA_FREEZE.json').read_text())['records'] if r['case']==n);assert sha(record)==r['record_sha256']
 for stage,script,args in [('original','propose_complementary.py',[str(record),str(P/'inputs/FROZEN_CONTRACT.json'),str(P/f'results/original-{n}')]),('actual','instrumented_proposer.py',[str(record),str(P/'inputs/FROZEN_CONTRACT.json'),str(P/f'results/{n}')])]:
  t=time.monotonic()
  with (P/f'{stage}-{n}.log').open('x') as log:x=subprocess.run([sys.executable,script,*args],cwd=P,stdout=log,stderr=subprocess.STDOUT)
  runs.append({'case':n,'stage':stage,'returncode':x.returncode,'seconds':time.monotonic()-t});(P/'RUN_EXECUTIONS.json').write_text(json.dumps(runs,indent=2));assert x.returncode==0
 o=P/f'results/{n}';original=P/f'results/original-{n}'
 assert sha(record)==r['record_sha256']
 if (o/'HOLD.json').exists():
  h=json.loads((o/'HOLD.json').read_text());assert h==json.loads((original/'HOLD.json').read_text());outcomes.append({'case':n,'stage':'proposer','status':'HOLD','reason':h['reason'],'original_and_instrumented_verdict_equal':True})
 else:
  assert sha(o/'PROPOSAL.npz')==sha(original/'PROPOSAL.npz')
  for stage,script in [('reduction','propose_reduction.py'),('span_verifier','certify_span.py')]:
   t=time.monotonic()
   with (P/f'{stage}-{n}.log').open('x') as log:x=subprocess.run([sys.executable,script,n],cwd=P,stdout=log,stderr=subprocess.STDOUT)
   runs.append({'case':n,'stage':stage,'returncode':x.returncode,'seconds':time.monotonic()-t});(P/'RUN_EXECUTIONS.json').write_text(json.dumps(runs,indent=2));assert x.returncode==0
  a=json.loads((o/'SPAN_CERTIFICATE.json').read_text());outcomes.append({'case':n,'stage':'phase_certificate','status':a['status'],'reason':a.get('reason'),'readable':a.get('readable'),'original_proposal_byte_identical':True})
 (P/'OUTCOMES.json').write_text(json.dumps(outcomes,indent=2))
print(json.dumps(outcomes,indent=2))
