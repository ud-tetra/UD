from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def freeze():
 f=json.loads((P/'PROTOCOL_FREEZE.json').read_text())
 for n,h in f['code_sha256'].items():assert sha(P/n)==h,'HOLD: frozen code changed'
 for n,h in f['inputs_sha256'].items():assert sha(P/'inputs'/n)==h,'HOLD: frozen input changed'
 return f
def case(n):return next(e for e in freeze()['cases'] if e['case']==n)
def witness(n):
 e=case(n);o=P/'results'/n;r=json.loads((o/'REPORT.json').read_text());d=json.loads((P/'DATA_FREEZE.json').read_text());entry=next(x for x in d['records'] if x['case']==n)
 assert r['record_sha256']==entry['record_sha256'] and r['proposal_sha256']==sha(o/'PHASE_PROPOSAL.npz')
 assert sha(o/'PHASE_PROPOSAL.npz')==sha(P/f'results/original-{n}/PHASE_PROPOSAL.npz')
 return {**e,'record_sha256':entry['record_sha256']},o
