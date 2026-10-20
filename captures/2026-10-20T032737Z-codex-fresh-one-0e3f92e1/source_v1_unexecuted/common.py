"""Frozen custody for one computational out-of-fit negated recipe, no physical lineage."""
import sys,os,json,hashlib
from pathlib import Path
from flint import arb,fmpq,ctx
sys.dont_write_bytecode=True;ctx.prec=512
P=Path(__file__).resolve().parent
CASE='null_top1_alternating_negated'
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def need(x,s):
 if not x:raise ValueError(s)
def a(p):return arb(fmpq(int(p[0]),int(p[1])))
def up(x):
 n=(arb(x.upper())*(1<<180)).ceil().unique_fmpz();need(n is not None,'HOLD outward upper');return [int(n),1<<180]
def down(x):
 n=(arb(x.lower())*(1<<180)).floor().unique_fmpz();need(n is not None,'HOLD outward lower');return [int(n),1<<180]
def repo():return Path(os.environ['UD_REPO']).resolve()
def freeze():
 need(__debug__,'assertions required');f=json.loads((P/'FREEZE.json').read_text())
 for n,h in f['files'].items():need(sha(P/n)==h,'local source changed '+n)
 for n,h in f['repository_sources'].items():need(sha(repo()/n)==h,'source changed '+n)
 return f

def write_new(path,obj):
 with Path(path).open('x')as f:json.dump(obj,f,indent=2);f.write('\n')
def guard(arg):
 lex=Path(os.path.abspath(arg));out=lex.resolve();protected={P.absolute(),P.resolve()}
 for q in(P,*P.parents):
  if(q/'MANIFEST.json').is_file():protected.update((q.absolute(),q.resolve()))
 for q in(lex,out):need(all(q!=z and z not in q.parents and q not in z.parents for z in protected),'protected output or ancestor')
 need(not out.exists(),'new output required');return out

def shared_raw(raw):
 p=Path(raw).resolve();d=json.loads((P/'DATA_FREEZE.json').read_text());need(d['status']=='EXACT_ONE_INPUT_FROZEN_BEFORE_FIT','data status');need(d['protocol_sha256']==sha(P/'FREEZE.json'),'data protocol binding');need(p.stat().st_size==150321232 and sha(p)==d['record']['record_sha256'],'shared raw identity');need(p.stat().st_mode&0o222==0,'shared raw must be read-only');return d

def reserve(path,anticipated=0):
 v=os.statvfs(Path(path));free=v.f_bfree*v.f_frsize;need(free-anticipated>=180000000,'HOLD physical root reserve below180MB');return free
