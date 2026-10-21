from pathlib import Path
import numpy as np,json,hashlib
from geometry import setup
p=Path(__file__).resolve().parent;root=p.parent;f=json.loads((p/'FREEZE.json').read_text());code=json.loads((p/'CODE_FREEZE.json').read_text());results=json.loads((p/'RESULTS.json').read_text());checks=[]
prior=json.loads((root/'graphite-step-audit/ZIP_MANIFEST.json').read_text())['files']; identities=[]
for entry in prior:
 path=entry['path']
 if path.startswith('graphite-target-replay/selected/') or path in ['lammps-runtime/lammps/share/lammps/potentials/CH.rebo','lammps-runtime/lammps/share/lammps/potentials/CC.KC','graphite-map/MAPS.npz','graphite-width/plugin/kcz_width2.so']:
  assert hashlib.sha256((root/path).read_bytes()).hexdigest()==entry['sha256'];identities.append(entry)
assert len(identities)==8
assert (root/'graphite-step-audit/sources/CH.rebo').read_bytes()==(root/'lammps-runtime/lammps/share/lammps/potentials/CH.rebo').read_bytes()
(p/'INPUT_IDENTITY_CHECK.json').write_text(json.dumps({'prior_capture':'2026-10-21T213321Z-codex-graphite-step-correction-03ffa1ca','status':'UNCHANGED_FROM_PRIOR_CAPTURE','files':identities},indent=2)+'\n')
for fn,sha in code['files'].items():assert hashlib.sha256((p/fn).read_bytes()).hexdigest()==sha
for fn,sha in f['source_hashes'].items():assert hashlib.sha256((root/fn).read_bytes()).hexdigest()==sha
for case,inputs in f['inputs'].items():
 for fn,sha in inputs.items():assert hashlib.sha256((root/'graphite-stationary'/case/fn).read_bytes()).hexdigest()==sha
 a=np.load(root/'graphite-stationary'/case/'RELAXED.npz');bas=np.load(root/'graphite-stationary'/case/'HESSIAN.npz');P=bas['primitive_P'];S=bas['basis_S'];Q=bas['basis_Q'];N,d=P.shape;m=3*d-5;nx=d-2;B=np.zeros((N,3,m));B[:,0,:nx]=P@S;B[:,1,nx:2*nx]=P@S;B[:,2,2*nx:]=P@Q;assert np.max(abs(B.reshape(-1,m).T@B.reshape(-1,m)-np.eye(m)))<1e-12
 nei,b=setup(root,case,a);out=p/case;sel=json.loads((out/'GEOMETRY_SELECTION.json').read_text())['columns'];raw=np.load(out/'MATRIX_RAW.npz');h=raw['fine_steps_A'];assert len(sel)==m
 u=b/np.linalg.norm(b,axis=2)[:,:,None];c0=np.stack([np.sum(u[:,i]*u[:,j],axis=1) for i,j in [(0,1),(0,2),(1,2)]],axis=1);branch0=np.searchsorted(f['branch_knots'],c0);min_margin=np.inf
 for j,row in enumerate(sel):
  crossing=row['nearest_crossing_A'];valid=[v for v in f['fine_ladder_A'] if crossing is None or v<=.9*crossing];assert h[j]==row['fine_step_A']==valid[0]
  db=B[nei,:,j]-B[:,None,:,j]
  for t in np.linspace(-1,1,9):
   bb=b+t*h[j]*db;uu=bb/np.linalg.norm(bb,axis=2)[:,:,None];cc=np.stack([np.sum(uu[:,i]*uu[:,j],axis=1) for i,j in [(0,1),(0,2),(1,2)]],axis=1);assert np.array_equal(np.searchsorted(f['branch_knots'],cc),branch0);min_margin=min(min_margin,float(np.min(abs(cc[:,:,None]-np.array(f['branch_knots'])))))
  for k,step in enumerate([2*h[j],h[j],h[j]/2]):assert np.array_equal(raw['matrices'][k,:,j],-(raw['raw_forces'][j,k,0]-raw['raw_forces'][j,k,1])/(2*step))
 Hc,Hf,Ha=raw['matrices'];H=(Hf+Hf.T)/2;rr=next(v for v in results['cases'] if v['case']==case);assert abs(rr['eigenvalue_min']-np.linalg.eigvalsh(H)[0])<1e-12
 z=np.load(out/'DIRECTION_RAW.npz');assert np.array_equal(z['derivatives'],-(z['raw_forces'][:,:,0]-z['raw_forces'][:,:,1])/(2*z['steps_A'][None,:,None]));assert np.max(abs(np.linalg.norm(z['vectors'],axis=1)-1))<1e-12
 for i,w in enumerate(z['vectors']):
  err=z['derivatives'][i,1]-H@w;assert abs(rr['directions'][i]['max_abs_error']-np.max(abs(err)))<1e-12
 checks.append({'case':case,'basis_isometry':True,'raw_derivative_reconstruction':'byte-identical','geometry_selection_reproduced':True,'retained_stencil_9_point_branch_check':True,'minimum_sampled_knot_distance':min_margin,'directional_checks_recomputed':6,'physical_promotion':0})
result={'status':'PASS_CONSTRUCTOR_INTEGRITY','checks':checks,'review':'Constructor recomputation only; no non-constructor review','scope':'Input/code hashes, independent sampled angular guard, basis, raw differences, spectra and directional residuals; no interval-proof or physical validation','physical_promotion':0};(p/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
