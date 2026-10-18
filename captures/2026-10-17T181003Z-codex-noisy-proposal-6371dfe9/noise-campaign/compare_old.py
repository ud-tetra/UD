import json,subprocess,os,time
from pathlib import Path
P=Path(__file__).resolve().parent;spec=json.loads((P/'CAMPAIGN_FREEZE.json').read_text());results=[]
for case in spec['discovery_cases']:
 out=P/'results'/('old-'+case);start=time.monotonic()
 with (P/'results'/('old-'+case+'.log')).open('w') as log:r=subprocess.run(['python','-u',str(P.parent/'observer-work/propose_record.py'),str(P/'records'/f'{case}.i64le'),str(P/'inputs/FROZEN_CONTRACT.json'),str(out)],stdout=log,stderr=subprocess.STDOUT,env=dict(os.environ,OPENBLAS_NUM_THREADS='1'))
 info=json.loads((out/'PROPOSAL_REPORT.json').read_text()) if (out/'PROPOSAL_REPORT.json').exists() else {}
 results.append({'case':case,'process_exit':r.returncode,'proposal_written':bool((out/'PROPOSAL.npz').exists()),'temporal_dimension':info.get('temporal_dimension'),'seconds':time.monotonic()-start});print(results[-1],flush=True)
(P/'OLD_PROPOSER_RESULTS.json').write_text(json.dumps(results,indent=2))
