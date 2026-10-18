import tempfile,json,shutil,subprocess,sys,os
from pathlib import Path
from bindings import P,sha,freeze
if __name__=='__main__':
 for e in json.loads((P/'PACKAGE_MANIFEST.json').read_text())['files']:
  f=P/e['path'];assert f.stat().st_size==e['size_bytes'] and sha(f)==e['sha256']
 with tempfile.TemporaryDirectory(prefix='ud-wide-timing-') as tmp:
  out=Path(tmp)/'work';shutil.copytree(P,out,ignore=shutil.ignore_patterns('__pycache__','REPLAY_CERTIFICATE.json','VALIDATION.json','TEST_RESULTS.txt'))
  for e in freeze()['cases']:
   r=subprocess.run([sys.executable,'certify.py',e['case'],'--replay'],cwd=out,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'});assert r.returncode==0
  r=subprocess.run([sys.executable,'validate.py'],cwd=out,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'});assert r.returncode==0
 print('PASS: package hashes, exact small-Gram certificates, all count/HOLD outcomes and five tests. Raw projection/estimator not rerun.')
