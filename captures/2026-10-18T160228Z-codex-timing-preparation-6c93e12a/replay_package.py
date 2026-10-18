from pathlib import Path
import tempfile,shutil,json,subprocess,sys,os
from bindings import P,sha
if __name__=='__main__':
 for e in json.loads((P/'PACKAGE_MANIFEST.json').read_text())['files']:
  p=P/e['path'];assert p.stat().st_size==e['size_bytes'] and sha(p)==e['sha256']
 with tempfile.TemporaryDirectory(prefix='ud-clock-budget-') as d:
  out=Path(d)/'package';shutil.copytree(P,out,ignore=shutil.ignore_patterns('__pycache__','REPLAY_CERTIFICATE.json','VALIDATION.json','TEST_RESULTS.txt'))
  for args in [['certify_budgets.py','--replay'],['validate.py']]:
   r=subprocess.run([sys.executable,*args],cwd=out,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'});assert r.returncode==0
 print('All package hashes, exact excitation/clock budgets, finite controls and tests PASS')
