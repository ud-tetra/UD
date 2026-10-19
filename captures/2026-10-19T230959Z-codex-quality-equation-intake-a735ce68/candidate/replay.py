"""Verify source/operational freeze then replay exact metadata controls to stdout."""
import hashlib,json
from pathlib import Path
D=Path(__file__).resolve().parent
f=json.loads((D/'FREEZE.json').read_text())
for row in f['files']:
    b=(D/row['path']).read_bytes()
    if len(b)!=row['bytes'] or hashlib.sha256(b).hexdigest()!=row['sha256']:raise RuntimeError('FROZEN_INPUT_CHANGED:'+row['path'])
import controls
result=controls.run()
expected=json.loads((D/'CONTROL_RESULT.json').read_text())
if result!=expected:raise RuntimeError('CONTROL_RESULT_CHANGED')
print(json.dumps({'status':'PASS','frozen_files':len(f['files']),'controls':result['count'],'raw_access_authorized':False,'physical_promotion':0},sort_keys=True))
