"""Read-only package verification in a fresh temporary copy; original receipts stay intact."""
from pathlib import Path
import tempfile,shutil,subprocess,sys,json,hashlib,os
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def run():
 for f in json.loads((P/'PACKAGE_MANIFEST.json').read_text())['files']:
  p=P/f['path'];assert p.stat().st_size==f['size_bytes'] and sha(p)==f['sha256']
 for f in json.loads((P/'WITNESS_INDEX.json').read_text())['arrays']:
  p=P/f['path'];assert p.stat().st_size==f['size_bytes'] and sha(p)==f['sha256']
 with tempfile.TemporaryDirectory(prefix='ud-floating-replay-') as tmp:
  root=Path(tmp)/'package';shutil.copytree(P,root,ignore=shutil.ignore_patterns('__pycache__','REPLAY_CERTIFICATE.json','REPLAY_EXECUTIONS.json','REPLAY_REFUSAL_RESULTS.json','VALIDATION.json','replay-*.log','replay_all.log','HOSTILE_TEST_RESULTS.txt'))
  r=subprocess.run([sys.executable,'replay_all.py'],cwd=root,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'})
  assert r.returncode==0
 print('All package hashes, actual floating-array residuals, phase bounds and hostile tests: PASS')
if __name__=='__main__':run()
