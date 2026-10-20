#!/usr/bin/env python3
"""Independent gcd canonicalization of existing supplied arrays; no fits/copies."""
import array, hashlib, json, math, struct, sys
from pathlib import Path
import numpy as np
BASE=Path('/workspace/scratch/f3d1c2f040c9')
OUT=BASE/'c21_identity_review'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for z in iter(lambda:f.read(1048576),b''):h.update(z)
 return h.hexdigest()
def canonical(p,b):
 before=sha(p); a=np.load(p,mmap_mode='r',allow_pickle=False)
 assert a.dtype==np.dtype('<i8') and a.ndim==2
 g=0
 for start in range(0,len(a),256):
  for v in np.asarray(a[start:start+256]).flat:
   g=math.gcd(g,int(v))
   if g==1:break
  if g==1:break
 c=math.gcd(g,1<<b); bb=b-(c.bit_length()-1)
 h=hashlib.sha256(b'UD_DYADIC_MATRIX_V1\0'+struct.pack('<IIH',*a.shape,bb)); payload=hashlib.sha256()
 for start in range(0,len(a),256):
  z=np.asarray(a[start:start+256]);payload.update(z.astype('<i8',copy=False).tobytes(order='C'))
  if c==1:raw=z.astype('<i8',copy=False).tobytes(order='C')
  else:
   arr=array.array('q',(int(v)//c for v in z.flat))
   if sys.byteorder!='little':arr.byteswap()
   raw=arr.tobytes()
  h.update(raw)
 assert sha(p)==before
 return {'fingerprint_sha256':h.hexdigest(),'canonical_denominator_bits':bb,'removed_power_of_two':b-bb,'all_zero':g==0,'input_C_order_int64_payload_sha256':payload.hexdigest()},before,a,c
catalog=BASE/'c21_identity/KNOWN_RECORDS.json';known=json.loads(catalog.read_text());rows=[];checks=0
pins={str(p.relative_to(BASE)):sha(p) for p in [catalog,BASE/'c21_identity/PROTOCOL.json',BASE/'c21_identity/SEAL.json',BASE/'c21_identity/screen_record.py']}
for case in ['boundary_pair_block','boundary_pair_rotating']:
 orig=None;origc=None
 for variant in ['original','fortran','scaled','one_entry_changed']:
  p=BASE/(f'c18_work/{case}/N.npy' if variant=='original' else f'c21_work/{case}/{variant}.npy');b=56 if variant=='scaled' else 55
  report=BASE/f'c21_primary/{case}/{variant}/SCREEN.json';s=json.loads(report.read_text());can,rawhash,a,c=canonical(p,b)
  assert can==s['canonical'];checks+=5
  assert list(a.shape)==s['shape'] and b==s['input_denominator_bits'];checks+=2
  assert rawhash==s['record_npy_sha256'] and sha(catalog)==s['catalog_sha256'];checks+=2
  assert pins['c21_identity/PROTOCOL.json']==s['protocol_sha256'] and pins['c21_identity/SEAL.json']==s['seal_sha256'];checks+=2
  ids=[r['record_id'] for r in known['records'] if r['fingerprint_sha256']==can['fingerprint_sha256']]
  assert s['matching_record_ids']==ids;checks+=1
  expected='UNLISTED_FINGERPRINT' if variant=='one_entry_changed' else 'LISTED_FINGERPRINT'
  assert s['identity_relation']==expected and bool(ids)==(expected=='LISTED_FINGERPRINT');checks+=2
  for k,v in {'independent_acquisition':'NOT_ESTABLISHED','fresh_preparation':'NOT_ESTABLISHED','provenance_status':'HOLD_PROVENANCE_NOT_ESTABLISHED','numerical_spectral_certificate':'NOT_EVALUATED','all_input_backend_conformance':'OPEN','external_promotion_review':'PENDING','new_estimator_calls':0,'physical_promotion':0,'hash_injectivity_claimed':False}.items():assert s[k]==v;checks+=1
  if variant=='original':orig=a;origc=c
  else:
   same=True;diffcount=0
   for st in range(0,len(a),256):
    # Actual divisors are 1 or 2; no overflow and divisibility established by gcd.
    aa=np.asarray(a[st:st+256])//c;oo=np.asarray(orig[st:st+256])//origc
    diffcount+=int(np.count_nonzero(aa!=oo))
   assert (diffcount==0)==(variant!='one_entry_changed');checks+=1
   if variant=='one_entry_changed':assert diffcount==1;checks+=1
  rows.append({'case':case,'variant':variant,'input':str(p.relative_to(BASE)),'input_sha256':rawhash,'screen_sha256':sha(report),'identity_relation':expected,'canonical':can,'exact_canonical_difference_count_vs_original':0 if variant=='original' else diffcount,'pass':True})
  print(json.dumps({'case':case,'variant':variant,'pass':True}),flush=True)
 replay=BASE/f'c21_replay/{case}/SCREEN.json';primary=BASE/f'c21_primary/{case}/original/SCREEN.json'
 assert replay.read_bytes()==primary.read_bytes();checks+=1
result={'status':'PASS_INDEPENDENT_GCD_ACTUAL8_IDENTITY_REVIEW','case_count':8,'listed':6,'unlisted_synthetic':2,'check_count':checks,'oracle':'Python-int gcd and integer division, typed little-endian canonical bytes; no signed OR/right shift','exact_alias_entry_comparisons':True,'source_pins':pins,'results':rows,'scope':{'no_new_acquisition':True,'no_estimator_calls':True,'no_large_matrix_copy_written':True,'physical_promotion':0,'external_promotion_review':'PENDING','stable_input_assumption':True,'all_input_backend_conformance':'OPEN','identity_not_acquisition_or_physical_semantics':True}}
(OUT/'ACTUAL_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:result[k] for k in ['status','case_count','listed','unlisted_synthetic','check_count']}))
