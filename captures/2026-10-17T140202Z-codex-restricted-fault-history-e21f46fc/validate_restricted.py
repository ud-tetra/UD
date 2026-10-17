"""Isolated constructor replay, source hashes and inherited contract checks."""
from pathlib import Path
import hashlib,json,subprocess,sys,tempfile,shutil
root=Path(__file__).resolve().parent
prov=json.loads((root/'PROVENANCE.json').read_text())
for x in prov['sources']:
 b=(root/x['path']).read_bytes();assert len(b)==x['size_bytes'] and hashlib.sha256(b).hexdigest()==x['sha256']
with tempfile.TemporaryDirectory(prefix='ud-restricted-replay-') as tmp:
 p=Path(tmp);shutil.copytree(root/'sources',p/'sources')
 for name in ['certify_restricted.py','restricted_gate.py','test_restricted.py']:shutil.copy2(root/name,p/name)
 r=subprocess.run([sys.executable,'certify_restricted.py'],cwd=p,text=True,capture_output=True)
 assert r.returncode==0,r.stderr
 assert json.loads((root/'RESTRICTED_FAULT_CERTIFICATE.json').read_text())==json.loads((p/'RESTRICTED_FAULT_CERTIFICATE.json').read_text())
 t=subprocess.run([sys.executable,'-m','unittest','-v','test_restricted.py'],cwd=p,text=True,capture_output=True)
 assert t.returncode==0,t.stderr
 assert 'Ran 5 tests' in t.stderr and t.stderr.rstrip().endswith('OK')
d=json.loads((root/'RESTRICTED_FAULT_CERTIFICATE.json').read_text())
assert d['static_gate']['declared_passing_readout_error_ceiling']==[1,2**57]
assert d['dynamic_gate']['declared_passing_metric_defect_ceiling']==[1,2**47]
assert d['robust_six_ratio_extension']['declared_six_ratio_vector_ceiling']==[1,2**40]
out={'status':'PASS','physical_promotion':0,'independent_review':'pending','constructor_only':True,
 'isolated_certificate_replay':'all fields identical','decoder_tests':5,
 'restricted_readout_coefficients':16175,'metric_pairs':2574,'metric_finite_controls':3,
 'new_calibration_bound_below':[1,2**40],'history_operator_budget_hypotheses_satisfied_conditionally':True,
 'apparatus_data_used':False,'remaining':['Family membership','Actual precision receipts','Measured shape gate','History acquisition receipts','Independent review']}
(root/'VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
