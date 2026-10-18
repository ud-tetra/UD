"""Fresh-directory deterministic replay and adversarial contract checks."""
from pathlib import Path
import hashlib,json,subprocess,sys,tempfile,shutil
ROOT=Path(__file__).resolve().parent
for s in json.loads((ROOT/'PROVENANCE.json').read_text())['sources']:
 b=(ROOT/s['path']).read_bytes()
 assert len(b)==s['size_bytes'] and hashlib.sha256(b).hexdigest()==s['sha256']
with tempfile.TemporaryDirectory(prefix='ud-acquisition-replay-') as tmp:
 p=Path(tmp);shutil.copytree(ROOT/'sources',p/'sources')
 for n in ['freeze_protocol.py','audit_run.py','exact_encoding.py','test_protocol.py']:shutil.copy2(ROOT/n,p/n)
 for args in [['freeze_protocol.py'],['-W','error::ResourceWarning','-m','unittest','-v','test_protocol.py']]:
  r=subprocess.run([sys.executable]+args,cwd=p,text=True,capture_output=True)
  assert r.returncode==0,r.stderr
  if '-m' in args:assert 'Ran 13 tests' in r.stderr and r.stderr.rstrip().endswith('OK')
 for n in ['FROZEN_CONTRACT.json','FREEZE_CERTIFICATE.json','RUN_RECEIPT_TEMPLATE.json','CHANNEL_ORDER.csv','PREPARATION_ORDER.csv']:
  assert (ROOT/n).read_bytes()==(p/n).read_bytes(),n
 audit=subprocess.run([sys.executable,'audit_run.py','RUN_RECEIPT_TEMPLATE.json'],cwd=p,text=True,capture_output=True,check=True)
 result=json.loads(audit.stdout)
 assert result['research_status']=='NOT_EXECUTED' and result['empirical_certification'] is False
out={'status':'PASS','physical_promotion':0,'independent_review':'pending',
 'isolated_replay':'Five generated contract, certificate, template and ordering artifacts identical',
 'adversarial_contract_checks':13,'original_preparation_SHAKE_design_checked':True,
 'A_sparse_skew_entries_checked':14880,'precision_bits':512,
 'empty_run_template_status':'NOT_EXECUTED','empirical_certification':False,
 'inherited_modal_and_diagnostic_proofs_reexecuted':False,
 'validated_full_size_spectral_solver_implemented':False,'apparatus_data_generated_or_tested':False}
(ROOT/'VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
