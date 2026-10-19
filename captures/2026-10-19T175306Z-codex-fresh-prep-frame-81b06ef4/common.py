"""Frozen contract, source data and exact dyadic enclosures."""
import sys
sys.dont_write_bytecode=True
import json,hashlib,zipfile
from pathlib import Path
from flint import arb,fmpq,ctx
ctx.prec=512
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
a=lambda x:arb(fmpq(int(x[0]),int(x[1])))
def up(x):
 v=(x*(1<<180)).ceil().unique_fmpz();assert v is not None
 return [int(v),1<<180]
def down(x):
 v=(x*(1<<180)).floor().unique_fmpz();assert v is not None
 return [int(v),1<<180]
def freeze():
 f=json.loads((P/'PROTOCOL_FREEZE.json').read_text())
 for n,h in f['files'].items():assert sha(P/n)==h,('freeze',n)
 return f
def intake(repo,dest):
 freeze();repo=Path(repo);dest=Path(dest);dest.mkdir(parents=True,exist_ok=False)
 rows=json.loads((P/'INPUT_INDEX.json').read_text())['members']
 for r in rows:
  cap=repo/'captures'/r['capture'];assert sha(cap/'MANIFEST.json')==r['manifest_sha256'];manifest=json.loads((cap/'MANIFEST.json').read_text());assert any(x['path']==r['archive'] and x['sha256']==r['archive_sha256'] for x in manifest['files'])
  zf=repo/r['archive'];assert sha(zf)==r['archive_sha256']
  with zipfile.ZipFile(zf) as z:
   hit=[x for x in z.infolist() if x.filename==r['member']];assert len(hit)==1;data=z.read(hit[0]);assert len(data)==r['size_bytes'] and hashlib.sha256(data).hexdigest()==r['sha256']
  q=dest/r['destination'];assert q.parent==dest;q.write_bytes(data)
 return {'members':len(rows),'bytes':sum(r['size_bytes'] for r in rows)}
def check_source(dest):
 for r in json.loads((P/'INPUT_INDEX.json').read_text())['members']:assert sha(Path(dest)/r['destination'])==r['sha256']
