import json,tempfile,shutil,subprocess,os,sys
from bindings import P,freeze,sha
if __name__=='__main__':
 for e in json.loads((P/'PACKAGE_MANIFEST.json').read_text())['files']+json.loads((P/'WITNESS_INDEX.json').read_text())['arrays']:
  p=P/e['path'];assert p.stat().st_size==e['size_bytes'] and sha(p)==e['sha256']
 freeze()
 with tempfile.TemporaryDirectory(prefix='ud-uniform-lag2-') as temp:
  dest=__import__('pathlib').Path(temp)/'work';shutil.copytree(P,dest,ignore=shutil.ignore_patterns('records','__pycache__','UNIFORM_REPLAY.json','ORDER_REPLAY.json','REPLAY_CERTIFICATE.json','DIRECT_ERROR.json','VALIDATION.json'))
  for args in [['uniform.py','--replay'],['source_order.py','cyclic_unit','--replay'],['certify.py','cyclic_unit','--replay'],['direct_error_v2.py','cyclic_unit'],['validate.py']]:
   r=subprocess.run([sys.executable,*args],cwd=dest,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'});assert r.returncode==0
 print('PASS: package/witness hashes; exact baseline residual and uniform phase grid; actual phase replay; zero-factor HOLD control. Raw cross-Grams and raw noise are not regenerated in this portable replay.')
