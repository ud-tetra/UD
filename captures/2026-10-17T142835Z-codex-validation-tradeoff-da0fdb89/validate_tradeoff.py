"""Isolated replay of geometry, optimization, finite controls and decoder tests."""
from pathlib import Path
import hashlib,json,subprocess,sys,tempfile,shutil
root=Path(__file__).resolve().parent
prov=json.loads((root/'PROVENANCE.json').read_text())
for x in prov['sources']:
 b=(root/x['path']).read_bytes();assert len(b)==x['size_bytes'] and hashlib.sha256(b).hexdigest()==x['sha256']
with tempfile.TemporaryDirectory(prefix='ud-tradeoff-replay-') as tmp:
 p=Path(tmp);shutil.copytree(root/'sources',p/'sources')
 for name in ['certify_tradeoff.py','optimized_gate.py','check_controls.py','test_optimized.py']:shutil.copy2(root/name,p/name)
 for args in [['certify_tradeoff.py'],['check_controls.py'],['-m','unittest','-v','test_optimized.py']]:
  r=subprocess.run([sys.executable]+args,cwd=p,text=True,capture_output=True)
  assert r.returncode==0,r.stderr
  if args[0]=='-m':assert 'Ran 6 tests' in r.stderr and r.stderr.rstrip().endswith('OK')
 for name in ['TRADEOFF_CERTIFICATE.json','MATCHED_FILTER_DESIGN.json','FINITE_CONTROLS.json']:
  assert json.loads((root/name).read_text())==json.loads((p/name).read_text()),name
out={'status':'PASS','physical_promotion':0,'independent_review':'pending',
 'isolated_replay':'geometry, frontier, continuous precision ceiling and finite controls identical',
 'decoder_tests':6,'actual_carrier_finite_controls':3,'optimization_interval_bits':512,
 'recommended_readings':493290,'recommended_error_ceiling':[1,2**58],
 'retained_strict_variant_readings':394632,'retained_strict_variant_error_ceiling':[1,2**64],
 'binary_precision_floor_scope':'This fixed-code central-stencil deterministic error-envelope family; not a physical lower bound',
 'apparatus_execution':False,'independent_review_pending':True}
(root/'VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
