from pathlib import Path
import numpy as np,json,hashlib,itertools
p=Path(__file__).resolve().parent;root=p.parent;f=json.loads((p/'FREEZE.json').read_text());result=json.loads((p/'RESULTS.json').read_text());count=0;windowsets=[]
for cfg in f['inputs']:
 case=cfg['case'];source=root/'graphite-stationary'/case
 for fn,sha in cfg['files'].items():assert hashlib.sha256((source/fn).read_bytes()).hexdigest()==sha
 a=np.load(p/case/'RAW.npz');r=json.loads((p/case/'RESULTS.json').read_text());old=np.load(source/'REFINED_HESSIAN.npz');H=(old['H_fine']+old['H_fine'].T)/2;steps=a['steps'];Ds=-(a['positive_forces']-a['negative_forces'])/(2*steps[None,:,None])
 for oi,obs in enumerate(r['observables']):
  changes=[None]+[float(np.max(abs(Ds[oi,j]-Ds[oi,j-1]))) for j in range(1,len(steps))];windows=[]
  for j in range(len(steps)-2):
   if changes[j+1]<1e-6 and changes[j+2]<1e-6:windows.append(list(steps[j:j+3]))
  assert windows==obs['stable_three_step_windows'];windowsets.append({tuple(w) for w in windows})
  for j,lr in enumerate(obs['ladder']):
   nominal=float(np.max(abs(Ds[oi,j]-H@a['vectors'][oi])));effective=float(np.max(abs(Ds[oi,j]-H@a['effective_tangent_directions'][oi,j])));assert abs(nominal-lr['nominal_error_max'])<1e-12 and abs(effective-lr['effective_tangent_error_max'])<1e-12
   if j:assert abs(changes[j]-lr['successive_max_change'])<1e-12
  count+=1
 assert np.max(abs(a['baseline_forces']-a['baseline_forces'][0]))==0
assert not set.intersection(*windowsets) and count==20
# Independent nearest periodic-image enumeration for every corrected bond map.
graph=np.load(p/'GRAPH_CORE.npz');maps=np.load(p/'CORRECTED_GEOMETRIC_MAPS.npz');geo=json.loads((p/'GEOMETRY_REPLAY.json').read_text());worst=0.
reg=json.loads((p/'SOURCE_REGISTER.json').read_text())
for entry in reg['files']:assert hashlib.sha256((p/entry['path']).read_bytes()).hexdigest()==entry['sha256']
assert hashlib.sha256((root/'graphite-map/MAPS.npz').read_bytes()).hexdigest()==json.loads((p/'IMAGE_GAUGE_CORRECTION_FREEZE.json').read_text())['old_map_archive_sha256']
records=json.loads((root/'graphite-width/SUMMARY.json').read_text())['rows'];lookup={(r['case'],r['cutoff_A'],r['width_A']):r for r in records}
for row in geo['rows']:
 case=row['case'];rec=lookup[(case,row['cutoff_A'],row['width_A'])];assert hashlib.sha256((root/rec['folder']/'MATRICES.npz').read_bytes()).hexdigest()==row['input_matrix_sha256'];a=np.load(root/rec['folder']/'MATRICES.npz');x=a['equilibrium_positions_A'];edges=graph[case+'_edges_0based'];pat,name=case.split('_',1);lines=(root/'graphite-target-replay/selected'/pat/name/'struct.inp.data').read_text().splitlines();lx=float(next(z for z in lines if 'xlo xhi' in z).split()[1]);ly=float(next(z for z in lines if 'ylo yhi' in z).split()[1]);xy=float(next(z for z in lines if 'xy xz yz' in z).split()[0]);L=np.array([[lx,xy],[0,ly]]);shifts=np.array([L@np.array(v) for v in itertools.product(range(-2,3),repeat=2)]);vec=x[edges[:,1]]-x[edges[:,0]];cand=vec[None,:,:2]+shifts[:,None,:];chosen=np.argmin(np.sum(cand*cand,axis=2),axis=0);vec[:,:2]+=shifts[chosen];norm=np.linalg.norm(vec,axis=1);assert norm.max()<1.7;normals=vec/norm[:,None];key=f"{case}_c{row['cutoff_A']}_w{row['width_A']}";err=np.max(abs(normals-maps[key+'_corrected_normals']));worst=max(worst,float(err));assert err<1e-10
 for c in row['closure']:assert c['rank']==c['dimension']-1 and c['status']=='RESOLVED_NONCLOSURE' and c['breathing_kernel_relative']<1e-10
assert geo['status']=='CORRECTED_REPLAY_PASS'
r={'status':'PASS_CONSTRUCTOR_INTEGRITY','force_observables_recomputed':count,'common_step_window':'NONE on frozen ladder','independent_nearest_image_configurations':36,'max_normal_difference':worst,'corrected_closure_tests':72,'prior_stiffness_qualification':'unchanged2/4','review':'non-constructor pending','physical_promotion':0};(p/'VERIFICATION.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
