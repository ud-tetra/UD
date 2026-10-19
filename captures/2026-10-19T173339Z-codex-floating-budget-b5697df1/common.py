"""Pinned data-only intake; no archived code execution."""
import sys
sys.dont_write_bytecode=True
import json,hashlib,zipfile
from pathlib import Path
from flint import arb,fmpq,ctx
ctx.prec=512
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
a=lambda p:arb(fmpq(int(p[0]),int(p[1])))
def up(x):
 z=(x*(1<<180)).ceil().unique_fmpz();assert z is not None
 return [int(z),1<<180]
def down(x):
 z=(x*(1<<180)).floor().unique_fmpz();assert z is not None
 return [int(z),1<<180]
def freeze():
 f=json.loads((P/'FREEZE.json').read_text())
 for n,h in f['files'].items():assert sha(P/n)==h,('frozen',n)
 return f
def check_evidence(out):
 for r in json.loads((P/'INPUT_INDEX.json').read_text())['members']:assert sha(Path(out)/r['destination'])==r['sha256'],r['destination']
def intake(repo,out):
 freeze();repo=Path(repo);out=Path(out);out.mkdir(parents=True,exist_ok=False)
 for r in json.loads((P/'PARENT_INDEX.json').read_text()):assert sha(repo/r['path'])==r['sha256'] and sha(P/'inputs'/r['copy'])==r['sha256']
 rows=json.loads((P/'INPUT_INDEX.json').read_text())['members']
 for r in rows:
  cap=repo/'captures'/r['capture'];assert sha(cap/'MANIFEST.json')==r['manifest_sha256']
  m=json.loads((cap/'MANIFEST.json').read_text());assert any(v['path']==r['archive'] and v['sha256']==r['archive_sha256'] for v in m['files'])
  zf=repo/r['archive'];assert sha(zf)==r['archive_sha256']
  with zipfile.ZipFile(zf) as z:
   hits=[x for x in z.infolist() if x.filename==r['member']];assert len(hits)==1
   data=z.read(hits[0]);assert len(data)==r['size_bytes'] and hashlib.sha256(data).hexdigest()==r['sha256']
  q=out/r['destination'];assert q.parent==out and not q.exists();q.write_bytes(data)
 return {'members':len(rows),'bytes':sum(r['size_bytes'] for r in rows)}
