from pathlib import Path
import json,hashlib
import numpy as np
C=Path(__file__).parent;R=C.parents[1]
def sha(b):return hashlib.sha256(b).hexdigest()
pre=json.loads((C/'PRE_RUN_RECEIPT.json').read_text());result=json.loads((C/'RESULTS.json').read_text());s=json.loads((C/'SETTINGS.json').read_text())
assert sha((C/'INPUTS.npz').read_bytes())==pre['input_sha256']
assert sha((C/'SETTINGS.json').read_bytes())==pre['settings_sha256']
assert sha((C/'numerical_replay.py').read_bytes())==pre['runner_sha256']
assert sha((C/'prepare_run.py').read_bytes())==pre['prepare_sha256']
assert sha((C/'NUMERICAL_PAYLOAD.npz').read_bytes())==result['payload_sha256']
for x in pre['source_files']:assert sha((R/x['path']).read_bytes())==x['sha256']
z=np.load(C/'NUMERICAL_PAYLOAD.npz');N=s['N'];assert N==256
for name in ('theta','rho','full'):
 a=z[name];assert sha(np.ascontiguousarray(a,dtype='<f8').tobytes())==pre['matrices'][name]['sha256']
 assert np.array_equal(a,a.T)
assert z['full'].shape==(512,512) and z['coupled_eigenvectors'].shape==(512,512)
assert z['theta_eigenvectors'].shape==(256,256)
checks=[]
for matrix,wname,vname in [('theta','theta_eigenvalues','theta_eigenvectors'),('full','coupled_eigenvalues','coupled_eigenvectors'),('full','blockwise_eigenvalues','blockwise_eigenvectors'),('full','probe0_eigenvalues','probe0_eigenvectors'),('full','probe1_eigenvalues','probe1_eigenvectors')]:
 A=z[matrix];w=z[wname];V=z[vname]
 residual=np.linalg.norm(A@V-V*w,axis=0)/(np.maximum(1,np.linalg.norm(A,np.inf)+np.abs(w)))
 orth=np.linalg.norm(V.T@V-np.eye(len(w)),'fro')
 assert max(residual)<=s['residual_tol'] and orth<=s['orthogonality_tol']
 checks.append({'array':vname,'columns':len(w),'max_scaled_residual':float(max(residual)),'orthogonality_frobenius':float(orth)})
assert result['status']=='PASS_NUMERICAL_SCOPED'
assert all(x['pass'] for x in result['theta']['exact_spectrum_comparison'])
assert result['coupled']['all_cluster_projectors_pass']
out={'status':'PASS','scope':'serialized payload hashes, matrix/source bindings, all retained eigenpair residuals and orthogonality; not independent scientific review','array_checks':checks,'physical_promotion':0}
(C/'VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'PASS','serialized_eigenpair_sets':len(checks),'physical_promotion':0}))
