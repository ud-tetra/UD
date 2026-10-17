"""Fresh-directory source-hash audit, exact tests and full-dimension controls."""
from pathlib import Path
import hashlib,json,tempfile,shutil,subprocess,sys,os
ROOT=Path(__file__).resolve().parent
for s in json.loads((ROOT/'PROVENANCE.json').read_text())['sources']:
 b=(ROOT/s['path']).read_bytes();assert len(b)==s['size_bytes'] and hashlib.sha256(b).hexdigest()==s['sha256']
env={**os.environ,'OPENBLAS_NUM_THREADS':'1'}
with tempfile.TemporaryDirectory(prefix='ud-spectral-replay-') as tmp:
 p=Path(tmp);shutil.copytree(ROOT/'sources',p/'sources')
 for n in ['hankel_exact.py','spectral_certificate.py','propose_basis.py','run_certificate.py','full_size_controls.py','review_parallel.py','test_spectral.py','native_precision_contract.py']:shutil.copy2(ROOT/n,p/n)
 for args in [['review_parallel.py'],['native_precision_contract.py'],['-m','unittest','-v','test_spectral.py'],['full_size_controls.py']]:
  r=subprocess.run([sys.executable]+args,cwd=p,text=True,capture_output=True,env=env)
  assert r.returncode==0,r.stderr
  if args[0]=='-m':assert 'Ran 13 tests' in r.stderr and r.stderr.rstrip().endswith('OK')
 for n in ['PARALLEL_APPENDIX_REVIEW.json','FULL_SIZE_CONTROLS.json','NATIVE_PRECISION_CONTRACT.json']:
  assert (ROOT/n).read_bytes()==(p/n).read_bytes(),n
out={'status':'PASS','physical_promotion':0,'independent_review':'pending',
 'exact_and_adversarial_tests':13,'full_size_spectral_controls':3,
 'full_size_dense_action_and_adjoint':True,'full_size_control_rank':1893,
 'fresh_directory_math_artifacts_identical':True,'dense_Hankel_stored':False,
 'floating_proposal_not_trusted_as_proof':True,'core_eigen_residual_verified_exactly':True,
 'conditional_native_precision_contract_checked':True,
 'nominal600cell_full_history_execution':False,'apparatus_data_execution':False,
 'full_dense_candidate_runtime_benchmarked':False,
 'scope':'Method and supplied constructed numeric controls. No independent review or metrological/physical certification.'}
(ROOT/'VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
