"""One proposal and full certificate attempt per predeclared case; retain failures."""
from pathlib import Path
import subprocess,os,json,time
P=Path(__file__).resolve().parent;spec=json.loads((P/'CAMPAIGN_FREEZE.json').read_text());rows=[];env=dict(os.environ,OPENBLAS_NUM_THREADS='1')
for c in spec['cases']:
 name=c['name'];proposal=P/'results'/('proposal-'+name);certificate=P/'results'/('certificate-'+name);start=time.monotonic()
 with (P/'results'/('proposal-'+name+'.log')).open('w') as f:r=subprocess.run(['python','-u',str(P/'propose_record.py'),str(P/'records'/(name+'.i64le')),str(P/'inputs/FROZEN_CONTRACT.json'),str(proposal)],stdout=f,stderr=subprocess.STDOUT,env=env)
 info=json.loads((proposal/'PROPOSAL_REPORT.json').read_text()) if (proposal/'PROPOSAL_REPORT.json').exists() else json.loads((proposal/'HOLD.json').read_text()) if (proposal/'HOLD.json').exists() else {}
 row={'case':name,'proposal_exit':r.returncode,'proposal_status':info.get('status'),'temporal_dimension':info.get('temporal_dimension'),'proposal_seconds':info.get('seconds'),'proposal_record_sha256':info.get('input_files',{}).get('record_sha256')}
 if (proposal/'PROPOSAL.npz').exists():
  with (P/'results'/('certificate-'+name+'.log')).open('w') as f:r=subprocess.run(['python','-u',str(P/'certify_record.py'),str(P/'records'/(name+'.i64le')),str(P/'inputs/FROZEN_CONTRACT.json'),str(proposal/'PROPOSAL.npz'),str(certificate)],stdout=f,stderr=subprocess.STDOUT,env=env)
  cert=json.loads((certificate/'CERTIFICATE.json').read_text()) if (certificate/'CERTIFICATE.json').exists() else {};bench=json.loads((certificate/'BENCHMARK.json').read_text()) if (certificate/'BENCHMARK.json').exists() else {}
  row.update(certificate_exit=r.returncode,certificate_status=cert.get('status','NO_CERTIFICATE'),certificate_reason=cert.get('reason'),bounds=cert.get('readable'),certificate_seconds=bench.get('wall_seconds'),peak_rss_kib=bench.get('peak_rss_kib'))
 row['total_seconds']=time.monotonic()-start;rows.append(row);(P/'CAMPAIGN_RESULTS.json').write_text(json.dumps(rows,indent=2)+'\n');print(row,flush=True)
