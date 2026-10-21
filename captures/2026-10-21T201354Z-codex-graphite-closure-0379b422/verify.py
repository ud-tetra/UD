from pathlib import Path
import json,hashlib,numpy as np
from scipy import sparse
from scipy.sparse.linalg import lsmr
p=Path(__file__).resolve().parent;base=p.parent;r=json.loads((p/'RESULTS.json').read_text());a=np.load(p/'CLOSURE.npz');maps=np.load(base/'graphite-map/MAPS.npz');h=lambda f:hashlib.sha256(f.read_bytes()).hexdigest();assert h(p/'CLOSURE.npz')==r['closure_sha256']
for fn,sha in r['input_sha256'].items():assert h(base/fn)==sha
checks=[];corollary=[]
for row in r['rows']:
 name=row['case'];c=row['cutoff_A'];w=row['width_A'];kind=row['observable'];key=f'{name}_c{c}_w{w}';prefix=key+'_'+kind;H=a[key+'_H'];Hc=a[key+'_H_coarse'];b=a[key+'_b'];n=len(H);V=a[prefix+'_Vrow'];Null=a[prefix+'_Vnull'];cross=V.T@H@Null;leak=np.linalg.norm(cross)/np.linalg.norm(H);assert abs(leak-row['closure_relative_F'])<1e-14
 # Geometry-fixed Householder row coordinates, independent of the constructor's SVD.
 z=b.copy();z[0]-=1;z/=np.linalg.norm(z);Z=(np.eye(n)-2*np.outer(z,z))[:,1:];leak_alt=np.linalg.norm(Z.T@H@b)/np.linalg.norm(H);assert abs(leak_alt-leak)<1e-10;angle=np.linalg.norm(Null@Null.T-np.outer(b,b));assert angle<1e-10
 assert row['rank']==n-1 and row['rank_stable'];assert np.linalg.norm(V.T@V-np.eye(n-1))<1e-10;assert row['status']=='RESOLVED_NONCLOSURE';assert leak>1e-8 and leak>10*row['operator_relative_step_uncertainty'];assert row['breathing_kernel_relative']<1e-10 and row['hidden_map_relative']<1e-10
 edges=maps[name+'_edges_0based'];N=len(maps[name+'_types']);E=len(edges);ii,jj=edges.T;B=sparse.csc_matrix((np.r_[-np.ones(E),np.ones(E)],(np.r_[ii,jj],np.r_[np.arange(E),np.arange(E)])),shape=(N,E));dr=base/'graphite-smooth'/name/f'cutoff_{c}' if w==2 else base/'graphite-width'/f'width_{w}'/name/f'cutoff_{c}';src=np.load(dr/'MATRICES.npz');d=len(src['K_fine']);group=src['group_index'];rep=np.zeros((N,d));rep[np.arange(N),group]=1/np.sqrt(np.bincount(group)[group]);Q=np.zeros((d,n))
 for j in range(n):sc=np.sqrt((j+1)*(j+2));Q[:j+1,j]=1/sc;Q[j+1,j]=-(j+1)/sc
 bond=src['equilibrium_positions_A'][jj]-src['equilibrium_positions_A'][ii];bond[:,:2]+=maps[name+'_edge_shifts_xy_A'];nv=bond/np.linalg.norm(bond,axis=1)[:,None]
 for label,v in [('breathing',b),('witness',a[prefix+'_witness'])]:
  u=rep@Q@H@v;diff=u[jj]-u[ii];raw=nv[:,:,None]*nv[:,2,None,None]*diff[:,None,:] if diff.ndim==2 else nv*nv[:,2,None]*diff[:,None]
  # u is1D: raw isE-by3. Project using least squares instead of anchored Laplacian.
  if kind=='cycle_axial':
   raw=np.stack([raw[:,j]-B.T@lsmr(B.T,raw[:,j],atol=1e-13,btol=1e-13,maxiter=10000)[0] for j in range(3)],1)
  saved=a[prefix+('_breathing_visible_acceleration' if label=='breathing' else '_witness_visible_acceleration')];assert np.linalg.norm(raw.reshape(-1)-saved)/np.linalg.norm(saved)<1e-9
 # Codimension1 + noninvariance forces any invariant rowspace containing this one to be the full quotient.
 S=np.vstack([V.T,b]);augerr=np.linalg.norm(S@S.T-np.eye(n));assert augerr<1e-10;trans=S@H@S.T;assert np.linalg.norm(trans[:-1,-1])>0
 corollary.append({'case':name,'cutoff_A':c,'width_A':w,'observable':kind,'hidden_span_breathing_projector_error':float(angle),'augmented_position_dimension':n,'augmented_phase_space_dimension':2*n,'orthogonal_augmentation_error':float(augerr),'minimal_invariant_linear_superspace':'full constrained quotient','observed_to_hidden_coupling_norm':float(np.linalg.norm(trans[:-1,-1]))})
 checks.append(prefix)
assert len(checks)==72
out={'status':'CONSTRUCTOR_VERIFICATION_PASS','inputs_hash_checked':len(r['input_sha256']),'observable_tests':len(checks),'method':'Geometry-fixed Householder breathing split versus SVD rowspace; independent least-squares cycle projection of witness accelerations; input hashes and augmentation','scope':'Same-constructor retained undamped linear dynamics, not independent review or physical damping identification','physical_promotion':0};(p/'VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n');(p/'AUGMENTATION_COROLLARY.json').write_text(json.dumps({'status':'DERIVED_CONDITIONAL_COROLLARY_WITH_NUMERICAL_HYPOTHESES','timing':'Corollary inferred after primary rank/nonclosure outcomes; not a new preregistered test','proof':'An(n-1)-dimensional rowspace has only itself or the full n-space as linear superspaces. Noninvariance excludes itself; adding its1D breathing complement yields the full quotient.','rows':corollary,'physical_promotion':0},indent=2)+'\n');print(json.dumps(out,indent=2))
