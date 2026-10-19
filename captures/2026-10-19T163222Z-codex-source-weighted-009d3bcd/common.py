"""Pinned archive data intake and directed rational enclosures."""
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
 f=json.loads((P/'FREEZE.json').read_text())
 for n,h in f['files'].items():assert sha(P/n)==h,('frozen',n)
 return f
def intake(repo,out):
 freeze();out=Path(out);out.mkdir(parents=True,exist_ok=False)
 rows=json.loads((P/'INPUT_INDEX.json').read_text())['members']
 for row in rows:
  cap=Path(repo)/'captures'/row['capture'];assert sha(cap/'MANIFEST.json')==row['manifest_sha256']
  zf=Path(repo)/row['archive'];assert sha(zf)==row['archive_sha256']
  manifest=json.loads((cap/'MANIFEST.json').read_text());assert any(v['path']==row['archive'] and v['sha256']==row['archive_sha256'] for v in manifest['files'])
  with zipfile.ZipFile(zf) as z:
   members=[v for v in z.infolist() if v.filename==row['member']];assert len(members)==1
   data=z.read(members[0]);assert len(data)==row['size_bytes'] and hashlib.sha256(data).hexdigest()==row['sha256']
  dest=out/row['destination'];assert dest.parent==out and not dest.exists();dest.write_bytes(data)
 return {'members':len(rows),'bytes':sum(v['size_bytes'] for v in rows)}
def check_evidence(path):
 for row in json.loads((P/'INPUT_INDEX.json').read_text())['members']:assert sha(Path(path)/row['destination'])==row['sha256']
