import tempfile,shutil,subprocess,sys,json,os
from pathlib import Path
from bindings import P,sha
if __name__=='__main__':
 for e in json.loads((P/'PACKAGE_MANIFEST.json').read_text())['files']:
  p=P/e['path'];assert p.stat().st_size==e['size_bytes'] and sha(p)==e['sha256']
 with tempfile.TemporaryDirectory(prefix='ud-prep-clocks-') as d:
  out=Path(d)/'package';shutil.copytree(P,out,ignore=shutil.ignore_patterns('__pycache__','REPLAY_CERTIFICATE.json','VALIDATION.json','TEST_RESULTS.txt'))
  for args in [['certify.py','--replay'],['validate.py']]:
   r=subprocess.run([sys.executable,*args],cwd=out,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'});assert r.returncode==0
 print('All hashes, exact offset/excitation witnesses, preparation clock budgets and controls PASS')
