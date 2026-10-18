import tempfile,shutil,json,subprocess,sys,os
from pathlib import Path
from bindings import P,sha,freeze
if __name__=='__main__':
 for e in json.loads((P/'PACKAGE_MANIFEST.json').read_text())['files']:
  p=P/e['path'];assert p.stat().st_size==e['size_bytes'] and sha(p)==e['sha256']
 for e in json.loads((P/'WITNESS_INDEX.json').read_text())['arrays']:
  p=P/e['path'];assert p.stat().st_size==e['size_bytes'] and sha(p)==e['sha256']
 with tempfile.TemporaryDirectory(prefix='ud-two-step-replay-') as tmp:
  out=Path(tmp)/'work';shutil.copytree(P,out,ignore=shutil.ignore_patterns('__pycache__','REPLAY_CERTIFICATE.json','ORDER_REPLAY.json','VALIDATION.json','TEST_RESULTS.txt'))
  for e in freeze()['cases']:
   n=e['case']
   for args in [['source_order.py',n,'--replay'],*([['certify.py',n,'--replay']] if not (out/f'results/{n}/ADAPTER_HOLD.json').exists() else [])]:
    r=subprocess.run([sys.executable,*args],cwd=out,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'});assert r.returncode==0
  r=subprocess.run([sys.executable,'validate.py'],cwd=out,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'});assert r.returncode==0
 print('PASS: all package/array hashes, exact source-order and actual two-step phase replays, retained HOLDs and six tests. Raw projection/proposer not rerun.')
