"""Independent finite CLI screen tests against a Fraction oracle."""
from pathlib import Path
import hashlib,json,os,resource,subprocess,sys
import numpy as np
from oracle import canonical_fraction
P=Path(__file__).resolve().parent;W=P.parent;ROOT=W/'c21_identity';EX=P/'executions'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def limits():resource.setrlimit(resource.RLIMIT_AS,(2*2**30,2*2**30));resource.setrlimit(resource.RLIMIT_CPU,(10,10))
def main():
 EX.mkdir(exist_ok=False);seal=read(ROOT/'SEAL.json');pins={n:sha(ROOT/n)for n in ['screen_record.py','PROTOCOL.json','KNOWN_RECORDS.json','SEAL.json']}
 for n,h in seal['files'].items():assert sha(ROOT/n)==h
 index=read(P/'FIXTURES.json');freeze=read(P/'FIXTURE_FREEZE.json');rows=[];env=os.environ.copy();env.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
 for case in index['cases']:
  name=case['case'];record=P/case['record'];known=P/case['known'];out=EX/name/'result';out.parent.mkdir();sentinel=None
  if name=='existing_output_sentinel':out.mkdir();sentinel=out/'KEEP.bin';sentinel.write_bytes(b'UNCHANGED_IDENTITY_REVIEW')
  elif name=='output_is_record_file':out=record
  elif name=='output_is_input_directory':out=record.parent
  before={str(p.relative_to(P/'fixtures')):sha(p)for p in(P/'fixtures').rglob('*')if p.is_file()and not p.is_symlink()}
  cp=subprocess.run([sys.executable,str(ROOT/'screen_record.py'),'--record',str(record),'--denominator-bits',case['bits'],'--known',str(known),'--out',str(out)],capture_output=True,text=True,timeout=15,env=env,preexec_fn=limits)
  check=[]
  def ck(label,b):
   assert b,(name,label)
   check.append({'id':label,'pass':True})
  status=None;screen=None
  if case['expected']=='VALID':
   ck('valid_exit0',cp.returncode==0 and(out/'SCREEN.json').is_file());screen=read(out/'SCREEN.json');status=screen['identity_relation'];can=screen['canonical']
   ck('independent_fraction_fingerprint',can['fingerprint_sha256']==case['expected_fingerprint'])
   ck('independent_fraction_canonical_exponent',can['canonical_denominator_bits']==case['expected_bbar'])
   ck('exact_cancelled_power',can['removed_power_of_two']==case['expected_removed'])
   ck('allzero_rule',can['all_zero']==case['expected_all_zero'])
   ck('typed_shape_and_input_exponent',screen['shape']==case['expected_shape'] and screen['input_denominator_bits']==int(case['bits']))
   ck('catalog_relative_class',status==case['expected_relation'] and screen['matching_record_ids']==case['expected_matches'])
   ck('no_acquisition_or_preparation_promotion',screen['independent_acquisition']==screen['fresh_preparation']=='NOT_ESTABLISHED'and screen['provenance_status']=='HOLD_PROVENANCE_NOT_ESTABLISHED')
   ck('no_numerical_or_hash_injectivity_claim',screen['numerical_spectral_certificate']=='NOT_EVALUATED'and screen['hash_injectivity_claimed']is False)
   ck('unchanged_project_and_physical_scope',screen['new_estimator_calls']==screen['physical_promotion']==0 and screen['all_input_backend_conformance']=='OPEN'and screen['external_promotion_review']=='PENDING')
   ck('file_catalog_and_package_hash_binding',screen['record_npy_sha256']==sha(record)and screen['catalog_sha256']==sha(known)and screen['protocol_sha256']==pins['PROTOCOL.json']and screen['seal_sha256']==pins['SEAL.json'])
   N=np.load(record,allow_pickle=False);ck('C_order_payload_binding',can['input_C_order_int64_payload_sha256']==hashlib.sha256(np.asarray(N,dtype='<i8').tobytes(order='C')).hexdigest())
  else:
   ck('invalid_exit2',cp.returncode==2)
   if case['expected']=='ARGUMENT_ERROR':status='ARGUMENT_ERROR';ck('CLI_argument_rejection',not cp.stdout.strip() and bool(cp.stderr.strip()))
   else:
    messages=[json.loads(x)for x in cp.stdout.splitlines()if x.startswith('{')];status=messages[-1]['status']if messages else None;ck('structured_intake_hold',status=='HOLD_INTAKE_OR_IO')
   if case['expected']!='OUTPUT_REJECTION':ck('no_invalid_output_created',not out.exists())
  after={str(p.relative_to(P/'fixtures')):sha(p)for p in(P/'fixtures').rglob('*')if p.is_file()and not p.is_symlink()}
  ck('all_input_and_sentinel_bytes_unchanged',before==after and(sentinel is None or sentinel.read_bytes()==b'UNCHANGED_IDENTITY_REVIEW'))
  row={'case':name,'expected':case['expected'],'returncode':cp.returncode,'status':status,'checks':check,'pass':all(x['pass']for x in check),'stdout':cp.stdout,'stderr':cp.stderr,'output_exists':out.exists()};rows.append(row);print(json.dumps({k:row[k]for k in ['case','returncode','status','pass']}),flush=True)
 for n,h in pins.items():assert sha(ROOT/n)==h
 for row in freeze['rows']:
  p=P/row['path']
  if'sha256'in row:assert sha(p)==row['sha256']
  else:assert p.is_symlink()and os.readlink(p)==row['symlink_target']
 ckcount=sum(len(x['checks'])for x in rows)
 result={'status':'PASS_FROZEN47_CANONICAL_IDENTITY_CLI_FIXTURES','case_count':len(rows),'valid_screens':sum(x['expected']=='VALID'for x in rows),'negative_cases':sum(x['expected']!='VALID'for x in rows),'check_count':ckcount,'cases':rows,'package_sha256':pins,'fixture_freeze_sha256':sha(P/'FIXTURE_FREEZE.json'),'all_inputs_and_sources_unchanged':True,'all_valid_classes_keep_provenance_HOLD':True,'same_projection_proves_replay':False,'unlisted_proves_independent_acquisition':False,'new_acquisitions':0,'physical_promotion':0}
 with(P/'SUITE_RESULTS.json').open('x')as f:json.dump(result,f,indent=2);f.write('\n')
 print(json.dumps({k:result[k]for k in ['status','case_count','valid_screens','negative_cases','check_count']}))
if __name__=='__main__':main()
