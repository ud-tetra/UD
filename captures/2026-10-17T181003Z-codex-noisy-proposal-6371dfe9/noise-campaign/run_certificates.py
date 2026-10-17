#!/usr/bin/env python3
"""Independent numerical jobs, two at a time; every record receives a full proof."""
from pathlib import Path
import concurrent.futures,json,subprocess,os,time,hashlib
P=Path(__file__).resolve().parent;spec=json.loads((P/'CAMPAIGN_FREEZE.json').read_text());code=['certify_record.py','proof_math.py','propose_record.py'];freeze={'status':'CONSTRUCTOR_IMPLEMENTATION_FREEZE','code_sha256':{n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in code},'case_order':spec['new_full_certificate_cases'],'acceptance_rule_changed':False,'independent_review':False};(P/'IMPLEMENTATION_FREEZE.json').write_text(json.dumps(freeze,indent=2));start=time.monotonic()
def run(case):
 t=time.monotonic();out=P/'results'/('certificate-'+case)
 with (P/'results'/('certificate-'+case+'.log')).open('w') as log:r=subprocess.run(['python','-u',str(P/'certify_record.py'),str(P/'records'/f'{case}.i64le'),str(P/'inputs/FROZEN_CONTRACT.json'),str(P/'results'/('new-'+case)/'PROPOSAL.npz'),str(out)],stdout=log,stderr=subprocess.STDOUT,env=dict(os.environ,OPENBLAS_NUM_THREADS='1'))
 cert=json.loads((out/'CERTIFICATE.json').read_text()) if (out/'CERTIFICATE.json').exists() else {};bench=json.loads((out/'BENCHMARK.json').read_text()) if (out/'BENCHMARK.json').exists() else {}
 return {'case':case,'exit':r.returncode,'status':cert.get('status','NO_CERTIFICATE'),'seconds':time.monotonic()-t,'peak_rss_kib':bench.get('peak_rss_kib'),'bounds':cert.get('readable'),'record_sha256':cert.get('input_sha256',{}).get('record')}
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
 for row in ex.map(run,spec['new_full_certificate_cases']):rows.append(row);(P/'FULL_CERTIFICATE_RESULTS.json').write_text(json.dumps({'rows':rows,'total_wall_seconds':time.monotonic()-start},indent=2));print(row,flush=True)
assert all(r['status']=='CERTIFIED_NUMERIC_RECORD_SIGNATURE' for r in rows),'At least one fresh noisy proposal did not certify'
