"""Own isolated frozen workspace; unchanged estimator numerical source."""
import sys
sys.dont_write_bytecode=True
import json,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def freeze():
    f=json.loads((P/'PROTOCOL_FREEZE.json').read_text())
    for n,h in f['files'].items():assert sha(P/n)==h,('code',n)
    for n,h in f['source_files'].items():assert sha(P.parent/n)==h,('source',n)
    return f
