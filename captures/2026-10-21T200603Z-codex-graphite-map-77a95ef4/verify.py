from pathlib import Path
import json,hashlib,numpy as np
from scipy import sparse
from scipy.sparse.csgraph import connected_components
from scipy.sparse.linalg import lsmr
p=Path(__file__).resolve().parent;base=p.parent;r=json.loads((p/'RESULTS.json').read_text());a=np.load(p/'MAPS.npz');h=lambda f:hashlib.sha256(f.read_bytes()).hexdigest();assert h(p/'MAPS.npz')==r['maps_sha256']
for fn,sha in r['input_sha256'].items():assert h(base/fn)==sha
checks=[]
for gd in r['graphs']:
 name=gd['case'];edges=a[name+'_edges_0based'];N=gd['atoms'];E=len(edges);ii,jj=edges.T;B=sparse.csc_matrix((np.r_[-np.ones(E),np.ones(E)],(np.r_[ii,jj],np.r_[np.arange(E),np.arange(E)])),shape=(N,E));assert connected_components(abs(B)@abs(B).T,directed=False,return_labels=False)==2;assert np.all(np.asarray(abs(B).sum(1)).ravel()==3)
 for row in [z for z in r['rows'] if z['case']==name]:
  key=f"{name}_c{row['cutoff_A']}_w{row['width_A']}";u=a[key+'_u'];v=a[key+'_diff'];vc=a[key+'_diff_cycle'];ax=a[key+'_axial_vector'];ac=a[key+'_axial_cycle'];assert np.max(abs(v-B.T@u))<1e-14;assert np.linalg.norm(B@vc)/np.linalg.norm(v)<1e-11;assert np.linalg.norm(B@ac)/np.linalg.norm(ax)<1e-10
  # Independent iterative least-squares: project onto im(B^T), rather than constructor's anchored Laplacian solve.
  for j in [0,1]:
   sol=lsmr(B.T,ax[:,j],atol=1e-13,btol=1e-13,maxiter=10000);res=ax[:,j]-B.T@sol[0];assert np.linalg.norm(res-ac[:,j])/np.linalg.norm(ax[:,j])<1e-9
  gfrac=np.linalg.norm(vc)**2/np.linalg.norm(v)**2;afrac=np.linalg.norm(ac)**2/np.linalg.norm(ax)**2;assert abs(gfrac-row['gradient_cycle_energy_fraction'])<1e-20;assert abs(afrac-row['axial_vector_cycle_energy_fraction'])<1e-12;assert row['all_pass'] and all(row['checks'].values());assert 0<afrac<1
  checks.append(key)
assert len(checks)==36
old=np.load(p/'export_failure/MAPS.npz');assert set(old.files)==set(a.files);assert all(np.array_equal(old[k],a[k]) for k in a.files)
out={'status':'CONSTRUCTOR_VERIFICATION_PASS','input_hashes':len(r['input_sha256']),'graphs':4,'responses':36,'method':'Sparse independent least-squares versus anchored Laplacian projection; graph degree/connectivity, divergence, map reconstruction and hashes','export_repair_arrays_identical':len(a.files),'scope':'Material graph analogue; same-constructor checks, not independent review or a600-cell identification','physical_promotion':0};(p/'VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
