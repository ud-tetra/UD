"""Hash-gated exact replay of neighbor state/flux and joined floating certificates."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[1]
for dep in json.loads((HERE/'CONTRACT.json').read_text())['source_dependencies']:
 p=REPO/dep['path'];b=p.read_bytes()
 assert len(b)==dep['size_bytes'] and hashlib.sha256(b).hexdigest()==dep['sha256'],'source dependency changed: '+dep['path']
print('frozen dependency hashes PASS',flush=True)
import neighbor_state
neighbor_state.main(HERE,False)
import neighbor_flux
neighbor_flux.main(HERE,False)
import neighbor_audit
neighbor_audit.main()
import join_audit
join_audit.main()
