from pathlib import Path
import numpy as np,json,hashlib
p=Path(__file__).resolve().parent;root=p.parent;freeze=json.loads((p/'FREEZE.json').read_text());rows=[];hashes=[]
for source in freeze['inputs']:
 src=root/source['folder']/'MATRICES.npz';assert hashlib.sha256(src.read_bytes()).hexdigest()==source['sha256'];old=np.load(src);key=f"{source['case']}_c{source['cutoff_A']}_w{source['width_A']}";folder=p/key;r=json.loads((folder/'RESULTS.json').read_text());assert r['all_checks_pass'];f=folder/'COLUMNS.npz';assert hashlib.sha256(f.read_bytes()).hexdigest()==r['column_archive_sha256'];d=np.load(f);group=d['group_index'];counts=np.bincount(group);N=len(group);m=len(counts);Q=np.zeros((m,m-1))
 for j in range(m-1):Q[:j+1,j]=1/np.sqrt((j+1)*(j+2));Q[j+1,j]=-(j+1)/np.sqrt((j+1)*(j+2))
 # Independent group averaging, without forming P or using stored primitive blocks.
 def project(v):
  reduced=np.zeros((m,v.shape[1]));np.add.at(reduced,group,v);reduced/=np.sqrt(counts)[:,None];return reduced, reduced[group]/np.sqrt(counts[group])[:,None]
 C=d['full_columns_fine'];CQ=C@Q;prim=[];leak=[]
 for axis in [0,1,2]:
  a,rep=project(CQ[:,axis,:]);prim.append(a);leak.append(CQ[:,axis,:]-rep)
 norm=np.linalg.norm(CQ);values={'vertical_nonprimitive':np.linalg.norm(leak[2])/norm,'inplane_primitive':np.linalg.norm(np.stack(prim[:2]))/norm,'inplane_nonprimitive':np.linalg.norm(np.stack(leak[:2]))/norm}
 for s,v in values.items():assert abs(v-r['relative_output_components'][s])<1e-12
 # Verify prior raw z columns are reproduced by full-force observation.
 prior_raw=old['raw_K_columns_fine'];match=np.linalg.norm(C[:,2,:]-prior_raw)/np.linalg.norm(prior_raw);assert match<1e-8
 assert np.array_equal(d['equilibrium_positions_A'],old['equilibrium_positions_A']) and np.array_equal(d['group_index'],old['group_index'])
 rows.append({'configuration':key,'full_z_column_match_relative':float(match),'independent_projection_pass':True});hashes.append({'path':str(f.relative_to(root)),'sha256':r['column_archive_sha256']})
model=json.loads((p/'MODEL_SOURCE_REGISTER.json').read_text())
for entry in model['files']:
 assert hashlib.sha256((root/entry['path']).read_bytes()).hexdigest()==entry['sha256']
result={'status':'PASS','configurations':len(rows),'constructor_only':True,'independent_review':'PENDING','checks':rows,'output_hashes':hashes,'maximum_full_z_column_match':max(r['full_z_column_match_relative'] for r in rows),'physical_promotion':0};(p/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['checks','output_hashes']},indent=2))
