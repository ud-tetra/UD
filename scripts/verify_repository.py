#!/usr/bin/env python3
"""Check immutable capture paths, event coverage and SHA-256 inventory."""
import argparse,hashlib,json,subprocess
from pathlib import Path
def verify(root,base=None):
 root=Path(root);count=0;manifests=list(root.glob('captures/*/MANIFEST.json'))
 assert manifests,'no capture manifests'
 covered=set()
 for p in manifests:
  covered.add(p.relative_to(root).as_posix())
  m=json.loads(p.read_text());assert m['capture_id']==p.parent.name
  assert m['physical_promotion']==0
  for x in m['files']:
   rel=Path(x['path']);assert not rel.is_absolute() and '..' not in rel.parts
   assert rel.parts[:2]==('captures',p.parent.name),'manifest crosses capture boundary'
   assert rel.as_posix() not in covered,'duplicate manifest path'
   covered.add(rel.as_posix())
   f=root/rel;assert f.is_file(),str(f)
   assert f.stat().st_size==x['size_bytes'],str(f)+' size'
   h=hashlib.sha256()
   with f.open('rb') as stream:
    for b in iter(lambda:stream.read(1024*1024),b''):h.update(b)
   assert h.hexdigest()==x['sha256'],str(f)+' SHA-256'
   count+=1
 actual={p.relative_to(root).as_posix() for p in (root/'captures').rglob('*') if p.is_file()}
 assert actual==covered,'unmanifested capture files: '+str(sorted(actual-covered))
 events=[json.loads(p.read_text()) for p in root.glob('events/*.json')]
 assert all(any(e.get('capture_id')==p.parent.name for e in events) for p in manifests),'missing capture event'
 if base and set(base)!={'0'}:
  diff=subprocess.run(['git','diff','--name-status',base,'HEAD'],cwd=root,check=True,capture_output=True,text=True).stdout
  additions=[];new_events=[]
  for line in diff.splitlines():
   status,path=line.split('\t',1)
   if path.startswith(('captures/','events/','state/','manuscripts/')):assert status=='A','immutable path changed: '+line
   if status=='A' and path.startswith('captures/'):additions.append(path)
   if status=='A' and path.startswith('events/') and path.endswith('.json'):new_events.append(json.loads((root/path).read_text()))
  if diff.strip():assert new_events,'repository change needs a new event'
  for capture in {path.split('/')[1] for path in additions}:
   assert any(e.get('capture_id')==capture for e in new_events),'new capture needs its own new event'
 return {'status':'PASS','manifests':len(manifests),'checked_files':count,'events':len(events)}
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--base');args=a.parse_args();print(json.dumps(verify(Path(__file__).resolve().parents[1],args.base)))
