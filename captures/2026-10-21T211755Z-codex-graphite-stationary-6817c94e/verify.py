from pathlib import Path
import numpy as np,json,hashlib
p=Path(__file__).resolve().parent;root=p.parent;f=json.loads((p/'FREEZE.json').read_text());rows=[]
for entry in f['inputs']:
 src=root/entry['folder']/'MATRICES.npz';assert hashlib.sha256(src.read_bytes()).hexdigest()==entry['sha256'];old=np.load(src);case=entry['case'];a=np.load(p/case/'RELAXED.npz');h=np.load(p/case/'HESSIAN.npz');r=json.loads((p/case/'RESULTS.json').read_text());group=a['group_index'];counts=np.bincount(group);d=len(counts);assert np.all(counts==counts[0]);S=h['basis_S'];Q=h['basis_Q'];P=h['primitive_P'];nx=d-2;nz=d-1
 assert np.array_equal(a['initial_positions_A'],old['equilibrium_positions_A']) and np.array_equal(a['atom_types'],old['atom_types'])
 # Independently gather force by primitive group before applying coordinate complements.
 reduced=np.zeros((d,3));np.add.at(reduced,group,a['forces']);reduced/=np.sqrt(counts)[:,None];g=np.r_[S.T@reduced[:,0],S.T@reduced[:,1],Q.T@reduced[:,2]];assert np.max(np.abs(g-a['projected_force']))<1e-12 and np.max(np.abs(g))<=1e-7
 q=a['q'];delta=np.column_stack([P@S@q[:nx],P@S@q[nx:2*nx],P@Q@q[2*nx:]]);assert np.max(np.abs(a['positions_A']-a['initial_positions_A']-delta))<1e-12
 # Independent constraint projection, including forbidden mean components.
 types=a['atom_types'];constraint=max([abs(np.mean(delta[types==t,k])) for t in [1,2] for k in [0,1]]+[abs(np.mean(delta[:,2]))]);assert constraint<1e-10
 H=(h['H_fine']+h['H_fine'].T)/2;e=np.linalg.eigvalsh(H);assert np.max(np.abs(e-h['eigenvalues']))<1e-10;unc=np.linalg.norm(h['H_fine']-h['H_coarse'],2);th=max(1e-7,10*unc);status='POSITIVE_RESOLVED' if e[0]>th else 'NEGATIVE_RESOLVED' if e[0]<-th else 'UNRESOLVED';assert status==r['stability']
 computed={'stationarity':np.max(np.abs(g))<=1e-7,'constraints':constraint<1e-10,'step_relative':np.linalg.norm(h['H_fine']-h['H_coarse'])/np.linalg.norm(H)<1e-5,'step_absolute':np.max(np.abs(h['H_fine']-h['H_coarse']))<1e-6,'symmetry':np.linalg.norm(h['H_fine']-h['H_fine'].T)/np.linalg.norm(H)<1e-6,'directional':all(x['relative_error']<1e-5 and x['max_abs_error']<1e-6 for x in r['directional_checks'])}
 for name,val in computed.items():assert bool(val)==r['checks'][name]
 ratio=np.linalg.norm(H[:2*nx,2*nx:])/np.linalg.norm(H[:,2*nx:]);assert abs(ratio-r['coupling_relative'])<1e-12
 rows.append({'case':case,'stationarity_reprojected':True,'constraint_error_A':float(constraint),'stability':status,'coupling_relative':float(ratio),'input_hash_match':True,'array_hashes':{name:hashlib.sha256((p/case/name).read_bytes()).hexdigest() for name in ['RELAXED.npz','HESSIAN.npz','OPTIMIZER.json']}})
result={'status':'PASS_INTEGRITY_ONLY','qualification_status':[{'case':entry['case'],'numerical_pass':json.loads((p/entry['case']/'RESULTS.json').read_text())['all_numerical_checks_pass']} for entry in f['inputs']],'cases':rows,'constructor_only':True,'nonconstructor_review':'PENDING','physical_promotion':0};(p/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
