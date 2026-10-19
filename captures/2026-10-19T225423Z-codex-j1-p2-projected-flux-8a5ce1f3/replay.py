"""Hash-gated exact replay of the frozen projected-source P2 flux proposal."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import json,hashlib
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[1]
for dep in json.loads((HERE/'CONTRACT.json').read_text())['source_dependencies']:
 p=REPO/dep['path'];b=p.read_bytes()
 assert len(b)==dep['size_bytes'] and hashlib.sha256(b).hexdigest()==dep['sha256'],'source dependency changed: '+dep['path']
print('immutable source dependency hashes PASS',flush=True)
import projected_flux
projected_flux.main(HERE,False)

import local_band
local_band.main(HERE)
