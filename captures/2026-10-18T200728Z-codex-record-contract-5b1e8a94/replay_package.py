import tempfile,shutil,subprocess,json,os,sys
from pathlib import Path
from bindings import P,freeze,sha
if __name__=='__main__':
 for e in json.loads((P/'PACKAGE_MANIFEST.json').read_text())['files']+json.loads((P/'WITNESS_INDEX.json').read_text())['arrays']:
  p=P/e['path'];assert p.stat().st_size==e['size_bytes'] and sha(p)==e['sha256']
 freeze()
 with tempfile.TemporaryDirectory(prefix='ud-record-contract-') as temp:
  out=Path(temp)/'work';shutil.copytree(P,out,ignore=shutil.ignore_patterns('__pycache__','REPLAY_CERTIFICATE.json','VALIDATION.json'))
  for args in [['verify.py','--replay'],['validate.py']]:
   r=subprocess.run([sys.executable,*args],cwd=out,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'});assert r.returncode==0
 print('PASS: all package/witness hashes, actual basis/cross-Grams, exact sketch residual arithmetic, archived floating phase and raw eligibility HOLD replays, four negative controls. Omitted raw records not reprojected and no proposer rerun.')
