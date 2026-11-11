from pathlib import Path
import numpy as np,json,hashlib,collections
p=Path(__file__).resolve().parent;freeze=json.loads((p/'FREEZE.json').read_text());rf=json.loads((p/'REFINEMENT_FREEZE.json').read_text());rows=[]
for cfg in freeze['inputs']:
 case=cfg['case'];out=p/case;assert hashlib.sha256((out/'RELAXED.npz').read_bytes()).hexdigest()==rf['inputs'][str((out/'RELAXED.npz').relative_to(p))];r=json.loads((out/'REFINED_RESULTS.json').read_text());a=np.load(out/'REFINED_HESSIAN.npz');H=(a['H_fine']+a['H_fine'].T)/2;delta=a['H_fine']-a['H_coarse'];ev=np.linalg.eigvalsh(H);assert np.max(abs(ev-a['eigenvalues']))<1e-10;m=len(H);d=(m+5)//3;nx=d-2;dirs=[]
 for i,z in enumerate(a['directional_force_columns']):
  w=np.sin((i+1)*np.arange(1,m+1));w/=np.linalg.norm(w);err=z-H@w;dirs.append({'relative_error':float(np.linalg.norm(err)/np.linalg.norm(H@w)),'max_abs_error':float(np.max(abs(err)))})
 checks={'stationarity':np.max(abs(a['fresh_projected_force']))<=1e-7,'step_relative':np.linalg.norm(delta)/np.linalg.norm(H)<1e-5,'step_absolute':np.max(abs(delta))<1e-6,'symmetry':np.linalg.norm(a['H_fine']-a['H_fine'].T)/np.linalg.norm(H)<1e-6,'directional':all(x['relative_error']<1e-5 and x['max_abs_error']<1e-6 for x in dirs)}
 assert {k:bool(v) for k,v in checks.items()}==r['checks'];assert bool(all(checks.values()))==r['all_checks_pass']
 assert np.linalg.norm(a['fresh_projected_force']-np.load(out/'RELAXED.npz')['projected_force'])<1e-8
 for x,y in zip(dirs,r['directional_checks']):assert max(abs(x[k]-y[k]) for k in x)<1e-12
 rows.append(r)
r={'status':'PASS_REFINED' if all(x['all_checks_pass'] for x in rows) else 'HOLD_REFINED_DERIVATIVE_QUALIFICATION','fully_qualified':sum(x['all_checks_pass'] for x in rows),'stability':dict(collections.Counter(x['stability'] for x in rows)),'coupling':dict(collections.Counter(x['coupling'] for x in rows)),'max_step_absolute':max(x['step_absolute'] for x in rows),'max_step_relative':max(x['step_relative'] for x in rows),'max_asymmetry_relative':max(x['symmetry_relative'] for x in rows),'max_directional_absolute':max(y['max_abs_error'] for x in rows for y in x['directional_checks']),'rows':rows,'constructor_integrity':'PASS','review':'non-constructor pending','original_primary_status':'HOLD_DERIVATIVE_QUALIFICATION','physical_promotion':0};(p/'REFINEMENT_RESULTS.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k!='rows'},indent=2))
