#!/usr/bin/env python3
"""Verify split bundles and restore to a new directory without replacement."""
import argparse,hashlib,json,tarfile,tempfile
from pathlib import Path
def restore(manifest,destination):
 manifest=Path(manifest).resolve();root=manifest.parents[2];dest=Path(destination).resolve()
 if dest.exists():raise ValueError('destination must not already exist')
 m=json.loads(manifest.read_text());index={x['path']:x for x in m['files']};dest.mkdir(parents=True)
 for bundle in m['bundles']:
  with tempfile.TemporaryFile() as archive:
   for rel in bundle['parts']:
    p=root/rel;x=index[rel];h=hashlib.sha256();size=0
    with p.open('rb') as f:
     for block in iter(lambda:f.read(1024*1024),b''):h.update(block);size+=len(block);archive.write(block)
    assert size==x['size_bytes'] and h.hexdigest()==x['sha256'],rel
   archive.seek(0)
   with tarfile.open(fileobj=archive,mode='r:gz') as tar:
    for item in tar:
     rel=Path(item.name)
     if rel.is_absolute() or '..' in rel.parts or not(item.isfile() or item.isdir()):raise ValueError('unsafe archive member '+item.name)
     target=dest/rel
     if item.isdir():target.mkdir(parents=True,exist_ok=True);continue
     target.parent.mkdir(parents=True,exist_ok=True)
     with target.open('xb') as out,tar.extractfile(item) as src:
      for b in iter(lambda:src.read(1024*1024),b''):out.write(b)
 return {'status':'PASS','destination':str(dest),'bundles':len(m['bundles'])}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('manifest');p.add_argument('destination');a=p.parse_args();print(json.dumps(restore(a.manifest,a.destination)))
