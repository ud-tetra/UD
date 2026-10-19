import hashlib,json
from pathlib import Path
D=Path(__file__).resolve().parent
f=json.loads((D/'FREEZE_v0.2.json').read_text())
for row in f['files']:
 b=(D/row['path']).read_bytes()
 if len(b)!=row['bytes']or hashlib.sha256(b).hexdigest()!=row['sha256']:raise RuntimeError('FROZEN_INPUT_CHANGED:'+row['path'])
import controls_v2
r=controls_v2.run()
if r!=json.loads((D/'CONTROL_RESULT_v0.2.json').read_text()):raise RuntimeError('CONTROL_RESULT_CHANGED')
print(json.dumps({'status':'PASS','frozen_files':len(f['files']),'controls':r['count'],'raw_access_authorized':False,'physical_promotion':0},sort_keys=True))
