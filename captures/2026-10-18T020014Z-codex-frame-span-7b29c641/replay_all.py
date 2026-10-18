from pathlib import Path
import json,subprocess,sys,time
P=Path(__file__).resolve().parent;f=json.loads((P/'CAMPAIGN_FREEZE.json').read_text());runs=[]
for e in f['cases']:
 t=time.monotonic()
 with (P/f"replay-{e['case']}.log").open('x') as log:r=subprocess.run([sys.executable,'certify_span.py',e['case'],'--replay'],cwd=P,stdout=log,stderr=subprocess.STDOUT)
 runs.append({'case':e['case'],'returncode':r.returncode,'seconds':time.monotonic()-t});(P/'REPLAY_EXECUTIONS.json').write_text(json.dumps(runs,indent=2));assert r.returncode==0
r=subprocess.run([sys.executable,'run_refusals.py','--replay'],cwd=P);assert r.returncode==0
r=subprocess.run([sys.executable,'validate_campaign.py'],cwd=P);assert r.returncode==0
