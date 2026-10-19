"""Hash-gated exact replay of the P2 state and paired audits."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import json,hashlib
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[1]
for dep in json.loads((HERE/'CONTRACT.json').read_text())['source_dependencies']:
 b=(REPO/dep['path']).read_bytes()
 assert len(b)==dep['size_bytes'] and hashlib.sha256(b).hexdigest()==dep['sha256'],'source dependency changed: '+dep['path']
print('immutable source dependency hashes PASS',flush=True)
import p2_state
p2_state.main(HERE,False)
