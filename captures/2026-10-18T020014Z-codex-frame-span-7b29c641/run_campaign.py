from pathlib import Path
import json,subprocess,sys,time
P=Path(__file__).resolve().parent;f=json.loads((P/'CAMPAIGN_FREEZE.json').read_text());runs=[]
for e in f['cases']:
 for stage,script in [('auxiliary_reduction','propose_reduction.py'),('exact_span_verifier','certify_span.py')]:
  t=time.monotonic()
  with (P/f"{stage}-{e['case']}.log").open('x') as log:r=subprocess.run([sys.executable,script,e['case']],cwd=P,stdout=log,stderr=subprocess.STDOUT)
  runs.append({'case':e['case'],'stage':stage,'returncode':r.returncode,'seconds':time.monotonic()-t});(P/'RUN_EXECUTIONS.json').write_text(json.dumps(runs,indent=2));assert r.returncode==0
print(json.dumps(runs,indent=2))
r=subprocess.run([sys.executable,'run_refusals.py'],cwd=P);assert r.returncode==0
