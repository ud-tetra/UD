"""Hash-gated replay of the frozen floating evaluator and uniform certificate."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import json,hashlib
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[1]
for dep in json.loads((HERE/'CONTRACT.json').read_text())['source_dependencies']:
 p=REPO/dep['path'];b=p.read_bytes()
 assert len(b)==dep['size_bytes'] and hashlib.sha256(b).hexdigest()==dep['sha256'],'source dependency changed: '+dep['path']
print('frozen source dependency hashes PASS',flush=True)
# Verify the authoritative parent manifest binds the pointwise source and its completed replay.
parent=REPO/'captures/2026-10-19T225423Z-codex-j1-p2-projected-flux-8a5ce1f3'
m=json.loads((parent/'MANIFEST.json').read_text())
for name in ['UPPER_RESULTS.json','LOCAL_BAND_RESULTS.json','REPLAY.log']:
 p=parent/name;b=p.read_bytes();r=next(x for x in m['files'] if x['path']==p.relative_to(REPO).as_posix())
 assert len(b)==r['size_bytes'] and hashlib.sha256(b).hexdigest()==r['sha256']
assert 'read-only replay matches UPPER_RESULTS.json' in (parent/'REPLAY.log').read_text()
import audit
audit.main()
