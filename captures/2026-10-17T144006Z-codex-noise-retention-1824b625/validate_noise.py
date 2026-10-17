"""Verify inherited hashes; replay in a fresh directory; compare exact generated data."""
from pathlib import Path
import json,hashlib,tempfile,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parent
for s in json.loads((ROOT/'PROVENANCE.json').read_text())['sources']:
 b=(ROOT/s['path']).read_bytes()
 assert len(b)==s['size_bytes'] and hashlib.sha256(b).hexdigest()==s['sha256']
with tempfile.TemporaryDirectory(prefix='ud-noise-replay-') as tmp:
 p=Path(tmp);shutil.copytree(ROOT/'sources',p/'sources')
 for n in ['certify_noise.py','test_noise.py']:shutil.copy2(ROOT/n,p/n)
 for args in [['certify_noise.py'],['-m','unittest','-v','test_noise.py']]:
  r=subprocess.run([sys.executable]+args,cwd=p,text=True,capture_output=True)
  assert r.returncode==0,r.stderr
  if args[0]=='-m':assert 'Ran 6 tests' in r.stderr and r.stderr.rstrip().endswith('OK')
 for n in ['NOISE_RETENTION_CERTIFICATE.json','NOISE_RETENTION_CURVE.csv','ACQUISITION_CHOICES.json']:
  assert (ROOT/n).read_bytes()==(p/n).read_bytes(),n
out={'status':'PASS','physical_promotion':0,'independent_review':'pending',
 'scope':'Fresh-directory replay of supplied block bounds, budget transfer and all207 sampled curve rows; six contract checks',
 'interval_bits':512,'outward_dyadic_bits':160,'sampled_curve_rows':207,'contract_checks':6,
 'parent_modal_diagonalization_reexecuted':False,
 'apparatus_execution':False,'large_Hankel_allocated':False}
(ROOT/'VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
