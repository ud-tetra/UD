"""Frozen data-only source binding and outward exact dyadic endpoints."""
import sys
sys.dont_write_bytecode=True
import json,hashlib
from pathlib import Path
from flint import arb,fmpq,ctx
ctx.prec=512
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
a=lambda x:arb(fmpq(int(x[0]),int(x[1])))
def up(x):
    n=(x*(1<<180)).ceil().unique_fmpz();assert n is not None;return [int(n),1<<180]
def down(x):
    n=(x*(1<<180)).floor().unique_fmpz();assert n is not None;return [int(n),1<<180]
def freeze():
    f=json.loads((P/'PROTOCOL_FREEZE.json').read_text())
    for n,h in f['files'].items():assert sha(P/n)==h,('code/input',n)
    for n,h in f['source_files'].items():assert sha(P.parent/n)==h,('saved-output source',n)
    return f
