"""Operational custody for two fixed adversarial estimator executions."""
import sys,os,json,hashlib
from pathlib import Path
from flint import arb,fmpq,ctx
sys.dont_write_bytecode=True
ctx.prec=512
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
a=lambda p:arb(fmpq(int(p[0]),int(p[1])))
def up(x):
 n=(arb(x.upper())*(1<<180)).ceil().unique_fmpz()
 if n is None:raise ArithmeticError('HOLD outward upper')
 return [int(n),1<<180]
def down(x):
 n=(arb(x.lower())*(1<<180)).floor().unique_fmpz()
 if n is None:raise ArithmeticError('HOLD outward lower')
 return [int(n),1<<180]
def repo():
 r=Path(os.environ['UD_REPO']).resolve()
 if not (r/'AGENTS.md').is_file():raise RuntimeError('HOLD explicit repository')
 return r
def freeze():
 if not __debug__:raise RuntimeError('HOLD assertions required')
 f=json.loads((P/'PROTOCOL_FREEZE.json').read_text())
 for n,h in f['files'].items():
  if sha(P/n)!=h:raise RuntimeError('HOLD local source changed: '+n)
 for n,h in f['repository_sources'].items():
  if sha(repo()/n)!=h:raise RuntimeError('HOLD repository source changed: '+n)
 return f
def write_new(path,obj):
 with Path(path).open('x') as f:json.dump(obj,f,indent=2);f.write('\n')
def external_output(raw):
 lex=Path(raw).absolute();out=lex.resolve();protected={P.absolute(),P.resolve()}
 for x in [P,*P.parents]:
  if (x/'MANIFEST.json').is_file():protected.update([x.absolute(),x.resolve()])
 for q in [lex,out]:
  if any(q==x or x in q.parents or q in x.parents for x in protected):raise RuntimeError('HOLD protected output')
 if out.exists():raise RuntimeError('HOLD output already exists')
 return out
