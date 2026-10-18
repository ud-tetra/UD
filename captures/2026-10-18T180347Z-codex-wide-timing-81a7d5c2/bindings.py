from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def freeze():
 f=json.loads((P/'WIDE_FREEZE.json').read_text())
 for n,h in f['code_sha256'].items():assert sha(P/n)==h,'HOLD: frozen code changed'
 for n,h in f['inputs_sha256'].items():assert sha(P/'inputs'/n)==h,'HOLD: frozen input changed'
 return f
