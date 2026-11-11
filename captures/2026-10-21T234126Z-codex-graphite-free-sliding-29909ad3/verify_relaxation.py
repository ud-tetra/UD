from pathlib import Path
import json,hashlib,numpy as np
from common import load,input_guard
p=Path(__file__).resolve().parent;root=p.parent;f=json.loads((p/'FREEZE.json').read_text());rows=[]
for fn,sha in f['inputs'].items():assert hashlib.sha256((root/fn).read_bytes()).hexdigest()==sha
for reg in ['RELAX_CODE_FREEZE.json','CODE_FREEZE.json','PRECHECK_SEAL.json','ELIGIBILITY_AMENDMENT.json']:
 for fn,sha in json.loads((p/reg).read_text())['files'].items():assert hashlib.sha256((p/fn).read_bytes()).hexdigest()==sha
for c in f['cases']:
 a,B,nei,b=load(c);flat=B.reshape(-1,B.shape[-1]);g=flat.T@a['forces'].ravel();assert np.max(abs(g-a['projected_force']))<1e-12;assert np.max(abs(g))<=1e-7;assert np.max(abs(flat.T@flat-np.eye(B.shape[-1])))<1e-12;assert np.max(abs(a['positions_A']-a['reference_positions_A']-np.einsum('nam,m->na',B,a['q'])))<1e-12;assert np.max(abs(np.mean(a['positions_A']-a['reference_positions_A'],axis=0)))<1e-12
 rec=json.loads((p/c/'RELAXATION.json').read_text());assert rec['energy_change_eV']<0;assert abs(rec['max_force_eV_per_A']-np.max(abs(g)))<1e-12
 if c.startswith('21_'):
  assert not (p/c/'RAW.npz').exists();plan=np.load(p/c/'PLAN.npz');assert np.any(plan['steps_A']<1e-6);assert not np.all(np.isfinite(plan['input_metrics']))
 rows.append(dict(case=c,stationarity='PASS',affine_constraints='PASS',energy_change_eV=rec['energy_change_eV'],raw_force_projection_reproduced=True))
(p/'RELAX_VERIFICATION.json').write_text(json.dumps(dict(status='PASS_CONSTRUCTOR',cases=rows,scope='Input/code hashes, stored raw force projections, coordinate reconstruction, global translation, lower-energy record and held-case no-force check. Not a fresh independent force run.'),indent=2)+'\n');print('PASS4')
