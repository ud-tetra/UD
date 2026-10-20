#!/usr/bin/env python3
"""Finite result-content rejection checks on copied dictionaries only."""
import copy,hashlib,importlib.util,json,sys
from pathlib import Path
P=Path(__file__).resolve().parent;BASE=P.parent;R=BASE/'c22_runner';D=P/'executions/exact_q1';F=P/'fixtures/exact_q1'
sys.dont_write_bytecode=True
spec=importlib.util.spec_from_file_location('c22_reviewed_runner',R/'run_submission.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_text())
sourcepins={n:sha(R/n)for n in ['run_submission.py','PROTOCOL.json','DEPENDENCIES.json','SEAL.json']}
config=load(R/'DEPENDENCIES.json');paths={k:BASE/'ud-repo'/v['entry']for k,v in config['roles'].items()};catalog=load(paths['identity'].parent/'KNOWN_RECORDS.json');ids={}
for row in catalog['records']:ids.setdefault(row['fingerprint_sha256'],[]).append(row['record_id'])
manifest=load(F/'manifest.json');exp={'manifest_sha256':sha(F/'manifest.json'),'payload_sha256':manifest['record']['payload_sha256'],'dimensions':{'m':2,'n':2,'q':1},'denominator_bits':0,'record_npy_sha256':sha(F/'N.npy'),'identity_seal_sha256':sha(paths['identity'].parent/'SEAL.json'),'identity_protocol_sha256':sha(paths['identity'].parent/'PROTOCOL.json'),'catalog_sha256':sha(paths['identity'].parent/'KNOWN_RECORDS.json'),'catalog_coverage':catalog['coverage'],'catalog_fingerprint_ids':ids,'numerical_seal_sha256':sha(paths['numerical'].parent/'SEAL.json'),'numerical_protocol_sha256':sha(paths['numerical'].parent/'PROTOCOL.json'),'audit_freeze_sha256':sha(paths['audit'].parent/'FREEZE.json')}
s=load(D/'identity/SCREEN.json');c=load(D/'numerical/CERTIFICATE.json');a=load(D/'audit/CERTIFICATE.json');wh=sha(D/'numerical/WITNESS.json.gz');ch=sha(D/'numerical/CERTIFICATE.json')
def identity(x):m.validate_identity(x,exp)
def numerical(x):
 m.validate_numerical(x,exp)
 # This is the explicit witness binding condition in run(), outside its helper.
 m.need(x['witness_sha256']==wh,'numerical witness hash')
def audit(x):m.validate_audit(x,exp,c,wh,ch)
rows=[]
def check(name,fn,expect_reject):
 try:fn();rejected=False;reason=None
 except Exception as e:rejected=True;reason=type(e).__name__+': '+str(e)
 assert rejected==expect_reject,(name,rejected,reason)
 rows.append({'case':name,'expected_reject':expect_reject,'rejected':rejected,'reason':reason,'pass':True})
def mutate(base,changes,fn,name):
 x=copy.deepcopy(base);changes(x);check(name,lambda:fn(x),True)
check('unmodified_actual_small_child_reports',lambda:(identity(s),numerical(c),audit(a)),False)
for name in ['identity_missing_file','numerical_missing_certificate','audit_missing_certificate']:check(name,lambda:m.load(P/'deliberately_absent_report.json'),True)
mutate(s,lambda x:x.update(identity_relation='FORGED'),identity,'identity_bad_status')
mutate(s,lambda x:x.update(record_npy_sha256='0'*64),identity,'identity_record_hash_mismatch')
mutate(s,lambda x:x.update(catalog_sha256='0'*64),identity,'identity_catalog_hash_mismatch')
mutate(s,lambda x:x.update(protocol_sha256='0'*64),identity,'identity_protocol_or_seal_mismatch')
mutate(s,lambda x:x.update(identity_relation='LISTED_FINGERPRINT',matching_record_ids=['FORGED']),identity,'identity_matching_ID_class_inconsistency')
mutate(s,lambda x:x.update(independent_acquisition='ESTABLISHED'),identity,'identity_acquisition_promotion')
mutate(s,lambda x:x.update(physical_promotion=1),identity,'identity_physical_promotion')
mutate(c,lambda x:x.update(status='HOLD_NUMERICAL'),numerical,'numerical_status_HOLD')
mutate(c,lambda x:x['gates'].update(full_abs_error_below_gate=False),numerical,'numerical_false_gate')
mutate(c,lambda x:x['gates'].update(full_abs_error_below_gate=1),numerical,'numerical_nonboolean_gate')
for key,name in [('manifest_sha256','numerical_manifest_hash_mismatch'),('record_payload_sha256','numerical_payload_hash_mismatch'),('witness_sha256','numerical_witness_hash_mismatch'),('protocol_sha256','numerical_protocol_hash_mismatch')]:mutate(c,lambda x,k=key:x.update({k:'0'*64}),numerical,name)
mutate(c,lambda x:x['dimensions'].update(q=2),numerical,'numerical_dimensions_mismatch')
mutate(c,lambda x:x.update(new_estimator_calls=1),numerical,'numerical_estimator_or_prior_call_claim')
mutate(c,lambda x:x.update(all_input_backend_conformance='CLOSED'),numerical,'numerical_physical_or_universal_claim')
mutate(a,lambda x:x.update(status='HOLD_MATRIX_OR_SCALAR_AUDIT'),audit,'audit_exit_zero_but_HOLD_status')
for key,name in [('manifest_sha256','audit_manifest_hash_mismatch'),('witness_sha256','audit_witness_hash_mismatch'),('producer_certificate_sha256','audit_producer_certificate_hash_mismatch')]:mutate(a,lambda x,k=key:x.update({k:'0'*64}),audit,name)
mutate(a,lambda x:x['matrix_checks']['M'].update(status='HOLD_MATRIX_CRT'),audit,'audit_one_matrix_nonPASS')
mutate(a,lambda x:x['scalar_checks'].update(independently_derived_status='HOLD_NUMERICAL'),audit,'audit_scalar_status_HOLD')
mutate(a,lambda x:x['scalar_checks']['gates'].update(full_abs_error_below_gate=False),audit,'audit_scalar_false_gate')
planned=load(P/'RESULT_VALIDATION_PLAN.json');assert {r['case']for r in rows if r['expected_reject']}==set(planned['expected_reject'])
assert sourcepins=={n:sha(R/n)for n in sourcepins}
result={'status':'PASS_FROZEN28_RESULT_CONTENT_CONTROLS','case_count':len(rows),'negative_cases':sum(r['expected_reject']for r in rows),'positive_cases':1,'source_pins':sourcepins,'results':rows,'scope':'Copied dictionary/file-validator controls; no forged child source, no subprocess false-acceptance injection, no adversarially complete forged-report security claim. Witness control exercises run() condition in addition to numerical helper.','physical_promotion':0,'external_promotion_review':'PENDING'}
(P/'RESULT_VALIDATION_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({k:result[k]for k in ['status','case_count','negative_cases','positive_cases']}))
