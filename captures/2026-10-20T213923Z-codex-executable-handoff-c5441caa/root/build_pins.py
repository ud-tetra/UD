from pathlib import Path
import hashlib,json,ast
P=Path('/workspace/scratch/f3d1c2f040c9');R=P/'ud-repo';D=P/'c22_runner'
base='captures/2026-10-20T204456Z-codex-reusable-verifier-3e0fa1e2'
screen='captures/2026-10-20T210354Z-codex-canonical-record-72c3a5bf/identity_screen'
roles={
 'identity':(screen,'screen_record.py',['screen_record.py','PROTOCOL.json','KNOWN_RECORDS.json','SEAL.json']),
 'numerical':(base+'/verifier','verifier.py',['verifier.py','PROTOCOL.json','SEAL.json']),
 'audit':(base+'/matrix_review','audit.py',['audit.py','PROFILE.json','PROTOCOL.md','SOURCE_INTERFACE.json','controls.py','FREEZE.json'])}
config={'version':'1.0','roles':{}}
for name,(folder,entry,files) in roles.items():
 config['roles'][name]={'entry':folder+'/'+entry,'files':{folder+'/'+n:hashlib.sha256((R/folder/n).read_bytes()).hexdigest() for n in files}}
(D/'DEPENDENCIES.json').write_text(json.dumps(config,indent=2,sort_keys=True)+'\n')
ast.parse((D/'run_submission.py').read_text())
seal={'version':'1.0','files':{n:hashlib.sha256((D/n).read_bytes()).hexdigest() for n in ['run_submission.py','PROTOCOL.json','DEPENDENCIES.json']},'scope':'Frozen before runner/child integration execution on pre-existing known records and controlled synthetic fixtures, not blinded acquisition'}
(D/'SEAL.json').write_text(json.dumps(seal,indent=2,sort_keys=True)+'\n');print(json.dumps({'seal_sha256':hashlib.sha256((D/'SEAL.json').read_bytes()).hexdigest(),'dependency_files':sum(len(x['files']) for x in config['roles'].values())}))
