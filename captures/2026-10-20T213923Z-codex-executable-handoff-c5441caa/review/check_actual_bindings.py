#!/usr/bin/env python3
"""Independent finite handoff binding/state review; does not redo matrix products."""
import hashlib,json,math
from fractions import Fraction
from pathlib import Path
P=Path(__file__).resolve().parent;B=P.parent;R=B/'c22_runner';REPO=B/'ud-repo'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb')as f:
  for z in iter(lambda:f.read(1048576),b''):h.update(z)
 return h.hexdigest()
load=lambda p:json.loads(p.read_text())
config=load(R/'DEPENDENCIES.json');seal=load(R/'SEAL.json');checks=0
for name,h in seal['files'].items():assert sha(R/name)==h;checks+=1
depcount=0
for role in config['roles'].values():
 for rel,h in role['files'].items():assert sha(REPO/rel)==h;checks+=1;depcount+=1
paths={k:REPO/v['entry']for k,v in config['roles'].items()};catalog=load(paths['identity'].parent/'KNOWN_RECORDS.json')
rows=[]
for case,man in [('boundary_pair_block',B/'c20_block_manifest.json'),('boundary_pair_rotating',B/'c20_rotating_manifest.json')]:
 d=B/'c22_primary'/case;manifest=load(man);roll=load(d/'ROLLUP.json');s=load(d/'identity/SCREEN.json');c=load(d/'numerical/CERTIFICATE.json');a=load(d/'audit/CERTIFICATE.json')
 assert roll['workflow_status']=='NUMERICAL_PASS_PROVENANCE_HOLD';checks+=1
 assert [x['role']for x in roll['stages_invoked']]==['identity','numerical','audit'];checks+=1
 assert all(x['returncode']==0 and x['timed_out']is False for x in roll['stages_invoked']);checks+=1
 for key,val in {'provenance_status':'HOLD_PROVENANCE_NOT_ESTABLISHED','independent_acquisition':'NOT_ESTABLISHED','fresh_preparation':'NOT_ESTABLISHED','external_promotion_review':'PENDING','physical_promotion':0,'all_input_backend_conformance':'OPEN','new_estimator_calls':0}.items():assert roll[key]==val;checks+=1
 assert roll['runner_seal_sha256']==sha(R/'SEAL.json') and roll['dependencies_sha256']==sha(R/'DEPENDENCIES.json');checks+=2
 for rel,h in roll['artifacts_sha256'].items():assert sha(d/rel)==h;checks+=1
 assert set(roll['artifacts_sha256'])=={'identity/SCREEN.json','numerical/CERTIFICATE.json','numerical/WITNESS.json.gz','audit/CERTIFICATE.json'};checks+=1
 mh=sha(man);payload=manifest['record']['payload_sha256'];rh=manifest['record']['sha256']
 assert all(x['manifest_sha256']==mh and x['record_payload_sha256']==payload for x in [roll,c,a]);checks+=6
 assert s['record_npy_sha256']==rh and s['canonical']['input_C_order_int64_payload_sha256']==payload;checks+=2
 ids=[x['record_id']for x in catalog['records']if x['fingerprint_sha256']==s['canonical']['fingerprint_sha256']]
 assert s['matching_record_ids']==ids and len(ids)==1 and s['identity_relation']=='LISTED_FINGERPRINT';checks+=3
 assert s['catalog_sha256']==sha(paths['identity'].parent/'KNOWN_RECORDS.json') and s['catalog_coverage']==catalog['coverage'];checks+=2
 for key,file in [('protocol_sha256','PROTOCOL.json'),('seal_sha256','SEAL.json')]:assert s[key]==sha(paths['identity'].parent/file);checks+=1
 assert c['status']=='CERTIFIED_FINITE_SUPPLIED_RECORD' and all(type(x)is bool and x for x in c['gates'].values());checks+=2
 assert c['witness_sha256']==sha(d/'numerical/WITNESS.json.gz');checks+=1
 for key,file in [('protocol_sha256','PROTOCOL.json'),('seal_sha256','SEAL.json')]:assert c[key]==sha(paths['numerical'].parent/file);checks+=1
 eps=Fraction(*map(int,c['bounds']['full_abs_error_upper']));assert 0<=eps<Fraction(1,2**41);checks+=1
 assert a['status']=='PASS_ALL_SIX_EXACT_CRT_AND_FRESH_SCALAR_CERTIFICATE';checks+=1
 assert a['witness_sha256']==c['witness_sha256'] and a['producer_certificate_sha256']==sha(d/'numerical/CERTIFICATE.json') and a['audit_freeze_sha256']==sha(paths['audit'].parent/'FREEZE.json');checks+=3
 assert a['dimensions']==c['dimensions']==roll['dimensions'];checks+=2
 n,q=c['dimensions']['n'],c['dimensions']['q'];sizes={'M':n*n,'K':n*q,'A':q*q,'B':q*q,'E':(n-q)**2,'H':(n-q)**2};entries=0;residues=0
 assert set(a['matrix_checks'])==set(sizes);checks+=1
 for name,z in a['matrix_checks'].items():
  assert z['status']=='PASS_EXACT_ALL_ENTRY_CRT';checks+=1
  primes=z['primes'];assert len(primes)==len(set(primes))and all(type(p)is int and 2<=p<2**24 and all(p%v for v in range(2,math.isqrt(p)+1))for p in primes);checks+=1
  assert math.prod(primes)==int(z['CRT_product'])>2*int(z['difference_bound'])>=0;checks+=1
  assert len(z['checks'])==len(primes);checks+=1
  for prime,check in zip(primes,z['checks']):
   assert check['prime']==prime and check['trial_division_prime_proved']is True and check['all_entries_match']is True and check['entries']==check['matching_entries']==sizes[name];checks+=1
   assert all(0<=int(v)<2**63 for v in check['maximum_int64_dot_sums']);checks+=1
   residues+=check['entries']
  entries+=sizes[name]
 sc=a['scalar_checks'];assert sc['independently_derived_status']==c['status'];checks+=1
 for field in ['gates','metrics','bounds']:assert sc[field]==c[field];checks+=1
 for stage in ['identity','numerical','audit']:
  proc=load(d/(stage+'_PROCESS.json'));assert proc['role']==stage and proc['returncode']==0 and proc['timed_out']is False;checks+=1
 rows.append({'case':case,'rollup_sha256':sha(d/'ROLLUP.json'),'identity_sha256':sha(d/'identity/SCREEN.json'),'numerical_certificate_sha256':sha(d/'numerical/CERTIFICATE.json'),'audit_certificate_sha256':sha(d/'audit/CERTIFICATE.json'),'identity_relation':'LISTED_FINGERPRINT','matrix_audit_distinct_entries':entries,'matrix_audit_residue_comparisons':residues,'full_abs_error_upper':c['bounds']['full_abs_error_upper'],'pass':True})
result={'status':'PASS_TWO_EXISTING_SUPPLIED_RECORD_HANDOFF_BINDINGS','case_count':2,'dependency_files':depcount,'check_count':checks,'results':rows,'scope':'Independent content/hash/typed-state/prime/CRT-bound review of parent-run outputs; no independent re-execution of matrix products or fresh acquisition claim. Pinned distinct auditor is the finite product/scalar dependency.','physical_promotion':0,'external_promotion_review':'PENDING','independent_acquisition':'NOT_ESTABLISHED','fresh_preparation':'NOT_ESTABLISHED','all_input_backend_conformance':'OPEN'}
(P/'ACTUAL_BINDING_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({k:result[k]for k in ['status','case_count','dependency_files','check_count']}))
