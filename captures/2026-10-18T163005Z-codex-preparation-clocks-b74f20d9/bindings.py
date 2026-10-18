from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def check():
 f=json.loads((P/'PREPARATION_CLOCK_FREEZE.json').read_text())
 for n,h in f['code_sha256'].items():assert sha(P/n)==h,(n,'frozen code changed')
 for n,h in f['inputs_sha256'].items():assert sha(P/'inputs'/n)==h
 assert sha(P/'inputs/REFERENCE_PROPOSAL.npz')==json.loads((P/'inputs/PHASE_STABILITY_CERTIFICATE.json').read_text())['reference_proposal_sha256']
 return f
