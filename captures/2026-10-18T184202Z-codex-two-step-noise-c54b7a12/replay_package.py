import tempfile,shutil,json,subprocess,sys,os
from pathlib import Path
from bindings import P,sha,freeze
if __name__=='__main__':
 for e in json.loads((P/'PACKAGE_MANIFEST.json').read_text())['files']:
  p=P/e['path'];assert p.stat().st_size==e['size_bytes'] and sha(p)==e['sha256']
 for e in json.loads((P/'WITNESS_INDEX.json').read_text())['arrays']:
  p=P/e['path'];assert p.stat().st_size==e['size_bytes'] and sha(p)==e['sha256']
 with tempfile.TemporaryDirectory(prefix='ud-two-noise-replay-') as tmp:
  out=Path(tmp)/'work';shutil.copytree(P,out,ignore=shutil.ignore_patterns('__pycache__','records','ORDER_REPLAY.json','REPLAY_CERTIFICATE.json','DIRECT_ERROR.json','VALIDATION.json','TEST_RESULTS.txt','UNIFORM_CERTIFICATE.json'))
  commands=[['uniform.py']]
  for e in freeze()['cases']:
   n=e['case'];commands.append(['source_order.py',n,'--replay'])
   if not (out/f'results/{n}/ADAPTER_HOLD.json').exists():commands.extend([['certify.py',n,'--replay'],['direct_error.py',n]])
  commands.append(['validate.py'])
  for args in commands:
   r=subprocess.run([sys.executable,*args],cwd=out,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'});assert r.returncode==0
 print('PASS: hashes, uniform bounds, noisy order and actual phase replays, direct source discrepancies, all HOLDs and six tests. Raw generation/adapter not rerun.')
