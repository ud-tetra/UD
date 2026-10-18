"""Portable saved-array proof replay; raw generation is separate and explicit."""
import json,tempfile,shutil,subprocess,sys,os
from pathlib import Path
from bindings import P,sha
if __name__=='__main__':
 for e in json.loads((P/'PACKAGE_MANIFEST.json').read_text())['files']:
  p=P/e['path'];assert p.stat().st_size==e['size_bytes'] and sha(p)==e['sha256']
 for e in json.loads((P/'WITNESS_INDEX.json').read_text())['arrays']:
  p=P/e['path'];assert p.stat().st_size==e['size_bytes'] and sha(p)==e['sha256']
 with tempfile.TemporaryDirectory(prefix='ud-new-seeds-replay-') as tmp:
  root=Path(tmp)/'package';shutil.copytree(P,root,ignore=shutil.ignore_patterns('__pycache__','records','codec','REPLAY_CERTIFICATE.json','REPLAY_EXECUTIONS.json','VALIDATION.json','TEST_RESULTS.txt','replay-*.log','replay_all.log'))
  r=subprocess.run([sys.executable,'replay_all.py'],cwd=root,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'});assert r.returncode==0
 print('Package hashes, all available actual-array phase residual replays and HOLD receipts: PASS. Raw records/proposer not rerun.')
