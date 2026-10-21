from pathlib import Path
import json,hashlib
import numpy as np
root=Path(__file__).parent;summary=[]
for name in ['21_dir_0','21_dir_10024','31_dir_10084','31_dir_10134']:
 p=root/name;record=json.loads((p/'RESULTS.json').read_text())['cases'][0];assert record['all_checks_pass']
 a=np.load(p/'MATRICES.npz');group=a['group_index'];n=len(group);d=a['K_fine'].shape[0];counts=np.bincount(group)
 P=np.zeros((n,d));P[np.arange(n),group]=1/np.sqrt(counts[group]);u=np.ones(d)/np.sqrt(d)
 assert np.max(np.abs(P.T@P-np.eye(d)))<1e-12
 for label in ['coarse','fine']:
  K=a['K_'+label];g=a['g_'+label];C=a['raw_K_columns_'+label];f=a['raw_g_'+label]
  assert np.max(np.abs(P.T@C-K))<1e-12 and np.max(np.abs(P.T@f-g))<1e-12
  assert np.linalg.norm(C-P@K)/np.linalg.norm(C)<1e-5
  assert np.linalg.norm(f-P@g)/np.linalg.norm(f)<1e-5
 # A different null-removal basis: Helmert columns, not the calculation's Householder.
 Q=np.zeros((d,d-1))
 for j in range(d-1):
  scale=np.sqrt((j+1)*(j+2));Q[:j+1,j]=1/scale;Q[j+1,j]=-(j+1)/scale
 assert np.max(np.abs(Q.T@Q-np.eye(d-1)))<1e-12
 S=(a['K_fine']+a['K_fine'].T)/2;ev=np.linalg.eigvalsh(Q.T@S@Q)
 assert ev[0]>0 and np.max(np.abs(ev-a['eigenvalues_projected']))<1e-10
 old=np.load(root/'serialization_failure'/name/'MATRICES.npz')
 common=['K_coarse','K_fine','g_coarse','g_fine','equilibrium_positions_A']
 drift={k:float(np.max(np.abs(a[k]-old[k]))) for k in common}
 assert max(drift.values())<1e-12
 assert hashlib.sha256((p/'lammps.log').read_bytes()).hexdigest()==record['final_log_sha256']
 summary.append({'case':name,'sector_dimension':d,'null_removed_dimension':d-1,'minimum_eigenvalue_eV_per_A2':float(ev[0]),'g_norms_eV_per_A2':record['g_column_norms_eV_per_A2'],'repeat_max_difference':max(drift.values()),'all_frozen_checks_pass':True})
result={'status':'PASS_SCOPED_NUMERICAL','cases':summary,'independent_constructor_check':'Helmert null basis, raw-column projection, repeated-array equality; not non-constructor review','physical_promotion':0}
(root/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
