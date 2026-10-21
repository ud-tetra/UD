"""Compare submitted report with SHA-pinned offline constructor baseline; no simulation execution."""
from pathlib import Path
import json, hashlib
P=Path(__file__).resolve().parent
r=(P/'REVIEW_RUN.json').read_bytes(); b=(P/'BASELINE.json').read_bytes()
assert hashlib.sha256(b).hexdigest()=='60f23c046f0577111dbc03927479f4fc41d9b95582a4bba0bc5782ff1a127783'
x=json.loads(r); y=json.loads(b)
assert x==y
assert x['status']=='PASS_REPRODUCTION_ONLY' and x['physical_promotion']==0
assert [x[k] for k in ('upstream_files_hash_checked','upstream_manifests_hash_checked','source_files_hash_checked')]==[44,6,3]
assert [(s['pr'],s['script']) for s in x['steps']]==[(350,'verify_components.py'),(352,'verify_payload.py'),(354,'verify_reduction.py'),(354,'compare_replay.py'),(355,'verify_reduction.py'),(356,'verify_certificate.py'),(358,'audit_replay.py')]
assert all(s['exit_code']==0 for s in x['steps'])
assert [s['exact_original_json_equal'] for s in x['steps']]==[True,None,True,True,True,True,True]
result={'status':'PASS_REPORT_COMPARISON','uploaded_sha256':hashlib.sha256(r).hexdigest(),'uploaded_size_bytes':len(r),'baseline_sha256':hashlib.sha256(b).hexdigest(),'parsed_json_equal':x==y,'raw_bytes_equal':r==b,'only_CRLF_difference':r.replace(b'\r\n',b'\n')==b,'reported_successful_steps':7,'reported_exact_output_comparisons':6,'reported_numerical_payload_check':'PASS','upstream_files_hash_checked_reported':44,'upstream_manifests_hash_checked_reported':6,'source_files_hash_checked_reported':3,'simulations_executed_this_intake':False,'independent_proof_review':'OPEN','physical_promotion':0}
out=json.dumps(result,indent=2)+'\n'
if (P/'VALIDATION.json').exists(): assert json.loads((P/'VALIDATION.json').read_bytes())==result
else: (P/'VALIDATION.json').write_text(out)
print(out,end='')
