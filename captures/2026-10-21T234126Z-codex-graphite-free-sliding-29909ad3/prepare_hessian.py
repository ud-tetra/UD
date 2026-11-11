from pathlib import Path
import json,hashlib,numpy as np
from common import ROOT,load,directions,clearance,input_guard
p=Path(__file__).resolve().parent;f=json.loads((p/'FREEZE.json').read_text());rows=[];seal={}
for case in f['cases']:
 out=p/case;a,B,nei,b=load(case);x=a['positions_A'];m=B.shape[2];V,names=directions(m);vectors=np.concatenate([np.eye(m),V]);names=['column_'+str(j) for j in range(m)]+names;records=[];steps=[];metrics=[];safes=[]
 for j,(w,name) in enumerate(zip(vectors,names)):
  disp=np.einsum('nam,m->na',B,w);cap=1.25e-5 if j<m else 2.5e-5;c,n,res=clearance(nei,b,disp,f['branch_knots'],hmax=cap);top=min(cap,.8*c);hh=np.array([top,.8*top,.6*top]);me,sa=input_guard(x,B,nei,b,disp,hh,np.array(f['branch_knots']));steps.append(hh);metrics.append(me);safes.append(sa);records.append({'name':name,'nearest_crossing_A':None if not np.isfinite(c) else c,'steps_A':hh.tolist(),'root_residual_max':res})
 steps=np.array(steps);metrics=np.array(metrics);safes=np.array(safes);ok=bool(np.all(safes) and np.min(steps)>=1e-6 and np.max(metrics[:,0,:])<=1e-6 and np.max(abs(a['projected_force']))<=1e-7)
 np.savez_compressed(out/'PLAN.npz',vectors=vectors,steps_A=steps,input_metrics=metrics,branch_safe=safes);(out/'PLAN.json').write_text(json.dumps({'case':case,'columns':m,'directions':9,'probes':records},indent=2)+'\n');row={'case':case,'all_feasibility_checks_pass':ok,'columns':m,'min_step':float(steps.min()),'input_error':float(metrics[:,0,:].max())};rows.append(row);print(row,flush=True)
 for fn in ['PLAN.npz','PLAN.json','RELAXED.npz']:seal[case+'/'+fn]=hashlib.sha256((out/fn).read_bytes()).hexdigest()
(p/'FEASIBILITY.json').write_text(json.dumps({'all_pass':all(z['all_feasibility_checks_pass'] for z in rows),'cases':rows},indent=2)+'\n');seal['FEASIBILITY.json']=hashlib.sha256((p/'FEASIBILITY.json').read_bytes()).hexdigest();(p/'PRECHECK_SEAL.json').write_text(json.dumps({'files':seal},indent=2)+'\n')
