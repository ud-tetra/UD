"""Hash-gated read-only exact rational replay of this certificate."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[1]
for dep in json.loads((HERE/'CONTRACT.json').read_text())['source_dependencies']:
 p=REPO/dep['path']
 assert len(p.read_bytes())==dep['size_bytes'] and hashlib.sha256(p.read_bytes()).hexdigest()==dep['sha256'],'source dependency changed: '+dep['path']
print('immutable source dependency hashes PASS',flush=True)
import upper_flux
upper_flux.main(HERE,False)
