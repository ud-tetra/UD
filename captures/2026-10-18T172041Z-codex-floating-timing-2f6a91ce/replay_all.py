import json,subprocess,sys,time
from bindings import P,check_freeze
f=check_freeze();rows=[]
for e in f['cases']:
 n=e['case'];o=P/f'results/{n}'
 if (o/'HOLD.json').exists() or (o/'ADAPTER_HOLD.json').exists():rows.append({'case':n,'stage':'proposer_HOLD_receipt_and_audit_only','status':'HOLD','raw_or_proposer_reexecuted':False});continue
 t=time.monotonic()
 with (P/f'replay-{n}.log').open('x') as log:r=subprocess.run([sys.executable,'certify_span.py',n,'--replay'],cwd=P,stdout=log,stderr=subprocess.STDOUT)
 rows.append({'case':n,'stage':'complete_saved_float_residuals','returncode':r.returncode,'seconds':time.monotonic()-t});assert r.returncode==0
(P/'REPLAY_EXECUTIONS.json').write_text(json.dumps(rows,indent=2))
r=subprocess.run([sys.executable,'validate_campaign.py'],cwd=P);assert r.returncode==0
