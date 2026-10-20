from pathlib import Path
import hashlib,json,subprocess,sys,numpy as np
P=Path('/workspace/scratch/f3d1c2f040c9');D=P/'c21_identity';W=P/'c21_work';W.mkdir(exist_ok=False)
records=[]
for case in ['boundary_pair_block','boundary_pair_rotating']:
 p=P/'c18_work'/case/'N.npy';N=np.load(p,mmap_mode='r',allow_pickle=False)
 variants=[('original',p,55,'Existing PR291 projected record')]
 folder=W/case;folder.mkdir()
 f=folder/'fortran.npy';np.save(f,np.asfortranarray(N),allow_pickle=False);variants.append(('fortran',f,55,'Synthetic NPY layout alias of existing record'))
 assert int(N.max())<=np.iinfo(np.int64).max//2 and int(N.min())>=np.iinfo(np.int64).min//2
 f=folder/'scaled.npy';np.save(f,N*2,allow_pickle=False);variants.append(('scaled',f,56,'Synthetic equivalent dyadic encoding (2N,b+1)'))
 f=folder/'one_entry_changed.npy';C=N.copy();C[0,0]=int(C[0,0])+1;np.save(f,C,allow_pickle=False);variants.append(('one_entry_changed',f,55,'Synthetic one-entry change, not acquisition evidence'))
 original_fingerprint=None
 for variant,path,bits,origin in variants:
  output=P/'c21_primary'/case/variant
  cmd=[sys.executable,str(D/'screen_record.py'),'--record',str(path),'--denominator-bits',str(bits),'--known',str(D/'KNOWN_RECORDS.json'),'--out',str(output)]
  r=subprocess.run(cmd,check=True,capture_output=True,text=True,env={**__import__('os').environ,'PYTHONDONTWRITEBYTECODE':'1'})
  x=json.loads((output/'SCREEN.json').read_text());expected='UNLISTED_FINGERPRINT' if variant=='one_entry_changed' else 'LISTED_FINGERPRINT'
  assert x['identity_relation']==expected
  assert x['provenance_status']=='HOLD_PROVENANCE_NOT_ESTABLISHED' and x['independent_acquisition']=='NOT_ESTABLISHED' and x['fresh_preparation']=='NOT_ESTABLISHED' and x['numerical_spectral_certificate']=='NOT_EVALUATED' and x['physical_promotion']==0
  if variant=='original':original_fingerprint=x['canonical']['fingerprint_sha256']
  elif variant!='one_entry_changed':assert x['canonical']['fingerprint_sha256']==original_fingerprint
  else:assert x['canonical']['fingerprint_sha256']!=original_fingerprint
  records.append({'case':case,'variant':variant,'origin':origin,'input_file':str(path),'input_size_bytes':path.stat().st_size,'npy_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'denominator_bits':bits,'identity_relation':x['identity_relation'],'fingerprint':x['canonical']['fingerprint_sha256'],'SCREEN_sha256':hashlib.sha256((output/'SCREEN.json').read_bytes()).hexdigest(),'stdout':r.stdout,'screen_exit':r.returncode})
 # Only the two original receipts need deterministic replay; alias identity is independently tested.
 replay=P/'c21_replay'/case
 subprocess.run([sys.executable,str(D/'screen_record.py'),'--record',str(p),'--denominator-bits','55','--known',str(D/'KNOWN_RECORDS.json'),'--out',str(replay)],check=True,capture_output=True,env={**__import__('os').environ,'PYTHONDONTWRITEBYTECODE':'1'})
 assert (replay/'SCREEN.json').read_bytes()==(P/'c21_primary'/case/'original/SCREEN.json').read_bytes()
receipt={'status':'PASS_TWO_ORIGINALS_FOUR_EQUIVALENT_ENCODINGS_TWO_SYNTHETIC_CHANGES','cases':records,'byte_identical_original_replays':2,'listed_screens':6,'unlisted_synthetic_screens':2,'new_independently_supplied_records':0,'new_estimator_calls':0,'new_physical_acquisitions':0,'all_provenance_results':'HOLD_PROVENANCE_NOT_ESTABLISHED','scope':'Original projections and controlled byte/layout/arithmetic variants; no raw/preparation independence established','physical_promotion':0}
(P/'c21_root/CASE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'status':receipt['status'],'screens':len(records),'replays':2}))
