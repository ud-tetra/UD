"""Safe byte-bound witness admission; does not run an SVD or reconstruct omitted raw."""
import json,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
w=json.loads((P/'WITNESS_INDEX.json').read_text())
for alias in w.get('aliases',[]):
 target=P/alias['path'];source=P/alias['identical_to']
 for name in [alias['path'],alias['identical_to']]:
  rel=Path(name);assert not rel.is_absolute() and '..' not in rel.parts
 assert source.is_file() and sha(source)==alias['sha256']
 if not target.exists():
  import shutil
  target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target)
 assert sha(target)==alias['sha256']
for index in ['PACKAGE_MANIFEST.json','WITNESS_INDEX.json']:
 f=json.loads((P/index).read_text())
 for x in f['files']:
  name=x['path'];rel=Path(name);assert not rel.is_absolute() and '..' not in rel.parts
  q=P/rel;assert q.is_file() and q.stat().st_size==x['size_bytes'] and sha(q)==x['sha256'],name
f=json.loads((P/'FREEZE.json').read_text())
for n,h in f['code_sha256'].items():assert sha(P/n)==h
from certify import certify
for mode in ['legacy_gemm','integer_projection']:
 r=certify(mode);assert r['status']=='CERTIFIED_ACTUAL_SVD_ORDER' and r['learned_order']==209
print('PASS: byte-bound full-factor exact dyadic SVD replay; two actual order209 certificates; raw sources omitted, no new SVD/phase claim; external review pending.',flush=True)
