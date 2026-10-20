from pathlib import Path
import importlib.util,json,hashlib,numpy as np
P=Path('/workspace/scratch/f3d1c2f040c9');D=P/'c21_identity'
spec=importlib.util.spec_from_file_location('builder_screen',D/'screen_record.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
records=[];bindings=[]
for case in ['boundary_pair_block','boundary_pair_rotating']:
 p=P/'c18_work'/case/'N.npy';N=np.load(p,mmap_mode='r',allow_pickle=False)
 c=mod.canonical(N,55)
 records.append({'record_id':'PR291_'+case,'fingerprint_sha256':c['fingerprint_sha256'],'source_reference':'captures/2026-10-20T204456Z-codex-reusable-verifier-3e0fa1e2/primary/'+case+'/CERTIFICATE.json'})
 bindings.append({'record_id':'PR291_'+case,'input_path_at_execution':str(p),'input_file_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'canonical':c,'shape':list(N.shape)})
known={'schema_version':'1.0','identity_format':'UD_DYADIC_MATRIX_V1','coverage':'Only the two projected matrices certified in PR291; not a complete UD record inventory or a catalog of physical acquisitions.','records':records}
(D/'KNOWN_RECORDS.json').write_text(json.dumps(known,indent=2,sort_keys=True)+'\n')
(P/'c21_root/KNOWN_BUILD_RECEIPT.json').write_text(json.dumps({'status':'CONSTRUCTED_TWO_REFERENCE_FINGERPRINTS','bindings':bindings,'builder_uses_screen_algorithm':True,'independent_gcd_scalar_validation':'PENDING_REVIEW','new_acquisition_records':0,'physical_promotion':0},indent=2)+'\n')
seal={'version':'1.0','files':{n:hashlib.sha256((D/n).read_bytes()).hexdigest() for n in ['screen_record.py','PROTOCOL.json','KNOWN_RECORDS.json']},'scope':'Frozen before finite suite/alias screening; two reference projections are already known, not blinded data. SHA is a binding, not injective equality proof or acquisition authenticity.'}
(D/'SEAL.json').write_text(json.dumps(seal,indent=2,sort_keys=True)+'\n')
print(json.dumps(known,indent=2))
