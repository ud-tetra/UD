import json,subprocess,os,time
from pathlib import Path
P=Path(__file__).resolve().parent;spec=json.loads((P/'CAMPAIGN_FREEZE.json').read_text());rows=[]
for case in spec['discovery_cases']:
 out=P/'results'/('new-'+case);start=time.monotonic()
 with (P/'results'/('new-'+case+'.log')).open('w') as log:r=subprocess.run(['python','-u',str(P/'propose_record.py'),str(P/'records'/f'{case}.i64le'),str(P/'inputs/FROZEN_CONTRACT.json'),str(out)],stdout=log,stderr=subprocess.STDOUT,env=dict(os.environ,OPENBLAS_NUM_THREADS='1'))
 info=json.loads((out/'PROPOSAL_REPORT.json').read_text()) if (out/'PROPOSAL_REPORT.json').exists() else json.loads((out/'HOLD.json').read_text())
 rows.append({'case':case,'process_exit':r.returncode,'proposal_written':(out/'PROPOSAL.npz').exists(),'temporal_dimension':info.get('temporal_dimension'),'status':info['status'],'reason':info.get('reason'),'seconds':time.monotonic()-start});print(rows[-1],flush=True)
(P/'NEW_PROPOSER_RESULTS.json').write_text(json.dumps(rows,indent=2))
