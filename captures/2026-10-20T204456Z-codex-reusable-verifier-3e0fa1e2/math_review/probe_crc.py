"""Post-freeze malformed payload CRC classification probe; controlled small input."""
from pathlib import Path
import hashlib,io,json,os,resource,struct,subprocess,sys,zipfile
import numpy as np
P=Path(__file__).resolve().parent;W=P.parent;D=P/'supplemental_crc_fixture';O=P/'supplemental_crc_result'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def limited():resource.setrlimit(resource.RLIMIT_AS,(2*2**30,2*2**30));resource.setrlimit(resource.RLIMIT_CPU,(15,15))
def main():
 D.mkdir(exist_ok=False);N=np.zeros((600,2),dtype='<i8');N[0,0]=2;np.save(D/'N.npy',N,allow_pickle=False)
 np.savez_compressed(D/'SVD_META.npz',singular=np.array([2.,0.]),right_transpose=np.eye(2));U=np.zeros((600,1));U[0,0]=1
 buffer=io.BytesIO();np.save(buffer,U,allow_pickle=False)
 with zipfile.ZipFile(D/'U.npz','w',compression=zipfile.ZIP_STORED)as z:z.writestr('basis.npy',buffer.getvalue())
 with zipfile.ZipFile(D/'U.npz')as z:info=z.infolist()[0];offset=info.header_offset
 data=bytearray((D/'U.npz').read_bytes());name_length,extra_length=struct.unpack_from('<HH',data,offset+26);data_start=offset+30+name_length+extra_length;changed_offset=data_start+info.file_size-1;data[changed_offset]^=1;(D/'U.npz').write_bytes(data)
 manifest={'schema_version':'1.0','record':{'path':'N.npy','sha256':sha(D/'N.npy'),'payload_sha256':hashlib.sha256(N.tobytes()).hexdigest(),'dyadic_exponent':0},'svd':{'path':'SVD_META.npz','sha256':sha(D/'SVD_META.npz')},'left_chunks':[{'path':'U.npz','sha256':sha(D/'U.npz'),'start':0,'stop':600}]}
 (D/'manifest.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n');before={p.name:sha(p)for p in D.iterdir()if p.is_file()};pkg=W/'c20_verifier';package_hashes={n:sha(pkg/n)for n in ['verifier.py','PROTOCOL.json','SEAL.json']}
 env=os.environ.copy();env.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
 cp=subprocess.run([sys.executable,str(pkg/'verifier.py'),'--manifest',str(D/'manifest.json'),'--out',str(O)],capture_output=True,text=True,timeout=20,env=env,preexec_fn=limited)
 messages=[json.loads(x)for x in cp.stdout.splitlines()if x.startswith('{')];status=messages[-1]['status']if messages else None;unchanged=before=={p.name:sha(p)for p in D.iterdir()if p.is_file()}
 assert unchanged and all(sha(pkg/n)==h for n,h in package_hashes.items())
 assert cp.returncode in (2,3) and status in ('HOLD_INTAKE_OR_INPUT_IO','HOLD_EXECUTION')and not O.exists()
 result={'status':'FAIL_CLOSED_MALFORMED_PAYLOAD_CRC_CLASSIFICATION_OBSERVED','timing':'Additional probe after frozen38-fixture suite; initial freeze and results unchanged','package_sha256':package_hashes,'fixture_manifest_sha256':sha(D/'manifest.json'),'source_files_before_after_unchanged':unchanged,'fixture':'600x2 int64 record, valid600x1 float64 left-factor NPY inside stored ZIP; final payload byte flipped without CRC update, archive SHA updated in manifest','changed_archive_offset':changed_offset,'uncompressed_member_bytes':info.file_size,'expected_structured_intake_exit':2,'observed_exit':cp.returncode,'observed_status':status,'stdout':cp.stdout,'stderr':cp.stderr,'output_directory_created':O.exists(),'false_acceptance':False,'classification_gap_observed':cp.returncode==3,'scientific_result_affected':False,'interpretation':'Malformed payload is rejected before output mutation. If exit3, decoder exception is classified as execution HOLD rather than structured intake HOLD; document this bounded diagnostic limitation without claiming universal malformed-input classification.','new_fits':0,'physical_promotion':0}
 with(P/'CRC_PROBE.json').open('x')as f:json.dump(result,f,indent=2);f.write('\n')
 print(json.dumps({k:result[k]for k in ['status','observed_exit','observed_status','output_directory_created','classification_gap_observed']}))
if __name__=='__main__':main()
