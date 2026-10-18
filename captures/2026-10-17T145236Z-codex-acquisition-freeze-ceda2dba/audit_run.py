"""Fail-closed record audit. References/metadata never establish empirical certification.

Usage: python audit_run.py RUN_RECEIPT.json --data-dir PATH
The result separates structural checks from unresolved evidence/proof review.
"""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime
import argparse,csv,hashlib,json,re,uuid
import numpy as np
ROOT=Path(__file__).resolve().parent
HEX=re.compile(r'^[0-9a-f]{64}$')
ID=re.compile(r'^[A-Za-z0-9._:-]{1,128}$')
def exact(x):
 if not isinstance(x,list) or len(x)!=2 or any(type(v) is not int for v in x) or x[1]<=0:
  raise ValueError('Requires exact [integer,positive denominator]')
 return F(*x)
def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as stream:
  for b in iter(lambda:stream.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def hash_ok(x):return isinstance(x,str) and HEX.fullmatch(x) is not None

def audit_history(data_dir,fmt,declared_data_hash,declared_index_hash):
 """Check length, integer range, hashes and one-to-one indexed vector coverage.
 Small custom fmt is only for tests; production uses the frozen format unchanged.
 """
 directory=Path(data_dir);problems=[];missing=[]
 data=directory/fmt['filename'];ledger=directory/fmt['index_ledger']['filename']
 for p in [data,ledger]:
  if not p.is_file():missing.append(p.name)
 if missing:return {'problems':problems,'missing':missing}
 if data.stat().st_size!=fmt['bytes']:problems.append('normalized dataset byte count mismatch')
 if declared_data_hash is None:missing.append('normalized_data_sha256')
 elif not hash_ok(declared_data_hash) or sha(data)!=declared_data_hash:problems.append('normalized dataset hash mismatch')
 if declared_index_hash is None:missing.append('sample_index_sha256')
 elif not hash_ok(declared_index_hash) or sha(ledger)!=declared_index_hash:problems.append('sample index hash mismatch')
 if not problems:
  with data.open('rb') as stream:
   for b in iter(lambda:stream.read(1024*1024),b''):
    z=np.frombuffer(b,dtype='<i8')
    # Do not useabs(int64_min), which can overflow.
    if np.any(z<-(2**49)) or np.any(z>2**49):
     problems.append('normalized amplitude exceeds conservative absolute bound2');break
 n_p,n_t,_=fmt['shape'];seen=set();n=0
 with ledger.open(newline='') as stream:
  reader=csv.reader(stream)
  if next(reader,None)!=fmt['index_ledger']['columns']:problems.append('sample index header mismatch')
  for row in reader:
   if len(row)!=3:problems.append('sample index row malformed');break
   aa,kk,rid=row
   if aa!=str(n//n_t) or kk!=str(n%n_t):problems.append('sample index missing, duplicate or out of order');break
   if not ID.fullmatch(rid) or rid in seen:problems.append('raw_record_id empty, invalid or reused');break
   seen.add(rid);n+=1
   if n>n_p*n_t:problems.append('excess indexed records');break
 if n!=n_p*n_t:problems.append('indexed record count mismatch')
 return {'problems':problems,'missing':missing,'indexed_records_checked':n,
  'scope':'Integrity and coverage only. Contents, physical provenance and time accuracy are not authenticated.'}

def evaluate_declared_intervals(spectral,rule):
 """Algebra on externally certified enclosures. This function does not certify their provenance or truth."""
 vals={}
 for k in ['sigma1','sigma1893','sigma1894']:
  lo,hi=map(exact,spectral[k])
  if lo<0 or hi<lo:raise ValueError('Invalid nonnegative singular-value interval')
  vals[k]=(lo,hi)
 if vals['sigma1'][1]<vals['sigma1893'][0] or vals['sigma1893'][1]<vals['sigma1894'][0]:
  raise ValueError('Intervals incompatible with sorted singular values')
 if exact(spectral['numerical_operator_error_upper'])>exact(rule['numerical_operator_error_ceiling']):
  return 'INCONCLUSIVE_NUMERICAL_ERROR_TOO_LARGE'
 if exact(spectral['numerical_operator_error_upper'])<0:raise ValueError('Negative error bound')
 if (vals['sigma1893'][1]<exact(rule['computed_sigma_1893_lower']) or
     vals['sigma1894'][0]>exact(rule['computed_sigma_1894_upper']) or
     vals['sigma1'][0]>exact(rule['computed_sigma_1_upper'])):
  return 'CONTRACT_CONTRADICTION_IF_ENCLOSURES_VALID'
 T=exact(rule['selection_threshold'])
 if vals['sigma1893'][0]>T and vals['sigma1894'][1]<T:
  if vals['sigma1'][1]<2029*vals['sigma1893'][0]:return 'CONDITIONAL_SIGNATURE_CONSISTENT'
 return 'INCONCLUSIVE'

def audit_run(receipt,contract_path,data_dir):
 config=json.loads(Path(contract_path).read_text());bad=[];missing=[]
 if type(receipt.get('schema_version')) is not int or receipt['schema_version']!=1:bad.append('unsupported receipt schema version')
 if receipt.get('protocol_sha256')!=sha(contract_path):bad.append('frozen contract hash mismatch')
 if type(receipt.get('acquisition_executed')) is not bool:bad.append('acquisition_executed must be boolean')
 if receipt.get('selected_target_count')!=1893:bad.append('rank target changed after freeze')
 for k,s in config['budgets'].items():
  x=receipt.get('error_evidence',{}).get(k)
  if not isinstance(x,dict):missing.append('error_evidence.'+k);continue
  if x.get('unit')!=s['unit']:bad.append('wrong error unit: '+k)
  if x.get('reported_upper') is None:missing.append('error bound: '+k)
  else:
   try:
    val=exact(x['reported_upper'])
    cap=exact(s['upper_ceiling'])
    if val<0 or val>cap or (s.get('comparison')=='<' and val==cap):bad.append('error ceiling exceeded: '+k)
   except (ValueError,TypeError):bad.append('malformed rational: '+k)
  if not hash_ok(x.get('evidence_sha256')):missing.append('evidence hash: '+k)
  if not isinstance(x.get('method'),str) or not x['method'].strip():missing.append('evidence method: '+k)
 required=['raw_source_sha256','processing_implementation_sha256','normalized_data_sha256','sample_index_sha256',
  'review_receipt','family_and_stability_receipt','diagnostic_pass_receipt','shape_gate_pass_receipt','six_ratio_gate_receipt','spectral_proof_receipt']
 for k in required:
  if not hash_ok(receipt.get(k)):missing.append(k)
 for k in ['run_id','started_utc','completed_utc']:
  if not receipt.get(k):missing.append(k)
 if receipt.get('run_id'):
  try:uuid.UUID(receipt['run_id'])
  except (ValueError,TypeError,AttributeError):bad.append('run_id is not a UUID')
 times=[]
 for k in ['started_utc','completed_utc']:
  if receipt.get(k):
   try:
    t=datetime.fromisoformat(receipt[k].replace('Z','+00:00'))
    if t.tzinfo is None:raise ValueError('timezone absent')
    times.append(t)
   except (ValueError,TypeError,AttributeError):bad.append('invalid timestamp '+k)
 if len(times)==2 and times[1]<times[0]:bad.append('completion precedes start')
 data_result=None;signature='NOT_EVALUATED'
 if receipt.get('acquisition_executed') is True:
  data_result=audit_history(data_dir,config['data_format'],receipt.get('normalized_data_sha256'),receipt.get('sample_index_sha256'))
  bad.extend(data_result['problems']);missing.extend(data_result['missing'])
  if receipt.get('signature_evaluation') is not None:
   try:signature=evaluate_declared_intervals(receipt['signature_evaluation'],config['spectral_rule'])
   except (KeyError,TypeError,ValueError):bad.append('invalid spectral interval metadata')
  else:missing.append('signature_evaluation')
 structural='REJECTED' if bad else 'INCOMPLETE' if missing else 'COMPLETE'
 research='REJECTED_METADATA_OR_INTEGRITY' if bad else 'NOT_EXECUTED' if receipt.get('acquisition_executed') is False else 'HOLD_PENDING_EVIDENCE_AND_PROOF_REVIEW'
 return {'structural_status':structural,'research_status':research,'physical_promotion':0,
  'empirical_certification':False,'independent_review':'not authenticated by this checker',
  'problems':bad,'missing':missing,'declared_interval_result':signature,'data_integrity':data_result,
  'scope':'Checks arithmetic, format, coverage and hash consistency. Evidence references, family membership, independent review and spectral proof are not validated by their hashes alone.'}

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('receipt');p.add_argument('--data-dir',default='.')
 p.add_argument('--contract',default=str(ROOT/'FROZEN_CONTRACT.json'));args=p.parse_args()
 print(json.dumps(audit_run(json.loads(Path(args.receipt).read_text()),args.contract,args.data_dir),indent=2))
