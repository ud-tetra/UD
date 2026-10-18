from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def checked(path,expected):
 assert sha(path)==expected,'HOLD: frozen file hash mismatch'
def load_case(case):
 f=json.loads((P/'CAMPAIGN_FREEZE.json').read_text())
 for n,h in f['code_sha256'].items():checked(P/n,h)
 for n,h in f['inputs_sha256'].items():checked(P/'inputs'/n,h)
 assert json.loads((P/'inputs/PHASE_STABILITY_CERTIFICATE.json').read_text())['reference_proposal_sha256']==sha(P/'inputs/REFERENCE_PROPOSAL.npz')
 e=next(e for e in f['cases'] if e['case']==case);o=P/f'results/{case}'
 checked(o/'FLOAT_WITNESS.npz',e['witness_sha256']);checked(o/'PROPOSAL.npz',e['proposal_sha256'])
 parent=json.loads((P/'inputs'/f'PARENT_{case}.json').read_text())
 assert parent['witness_sha256']==e['witness_sha256'] and parent['proposal_sha256']==e['proposal_sha256'] and parent['record_sha256']==e['record_sha256']
 return f,e,o,parent
