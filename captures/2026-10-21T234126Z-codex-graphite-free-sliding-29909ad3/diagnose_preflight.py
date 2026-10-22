from pathlib import Path
import numpy as np,json
from common import load
p=Path(__file__).resolve().parent;rows=[];knots=np.array(json.loads((p/'FREEZE.json').read_text())['branch_knots'])
for case in json.loads((p/'FREEZE.json').read_text())['cases']:
 a,B,nei,b=load(case);u=b/np.linalg.norm(b,axis=2)[:,:,None];theta=np.stack([np.sum(u[:,i]*u[:,j],axis=1) for i,j in [(0,1),(0,2),(1,2)]],axis=1);plan=np.load(p/case/'PLAN.npz');delta=abs(theta[:,:,None]-knots);rows.append(dict(case=case,min_knot_distance=float(delta.min()),triples_within_1e_12_per_knot=np.sum(delta<=1e-12,axis=(0,1)).tolist(),zero_step_probes=np.flatnonzero(np.any(plan['steps_A']==0,axis=1)).tolist(),below_min_step_probes=np.flatnonzero(np.any(plan['steps_A']<1e-6,axis=1)).tolist(),nonfinite_input_metrics=int(np.count_nonzero(~np.isfinite(plan['input_metrics'])))))
(p/'PREFLIGHT_DIAGNOSIS.json').write_text(json.dumps({'cases':rows,'interpretation':'Zero clearance is numerical boundary contact, not proof the physical Hessian fails to exist. Squared quartic construction and floating-point cosines can produce an exact zero root. In either event the frozen same-branch rule fails. Zero steps produced undefined diagnostic direction quotients (NaNs) during preflight, never force evaluations.','physical_promotion':0},indent=2)+'\n');print(rows)
