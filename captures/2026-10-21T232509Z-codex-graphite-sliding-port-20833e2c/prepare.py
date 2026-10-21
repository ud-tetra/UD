from pathlib import Path
import sys,json,hashlib,datetime,numpy as np
p=Path(__file__).resolve().parent;root=p.parent
sys.path.insert(0,str(root/'graphite-safe-full'))
from common import load,clearance,input_guard,directions
f=json.loads((root/'graphite-safe-full/FREEZE.json').read_text());f.update(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),purpose='Two normalized relative-layer sliding ports. Nine directional reciprocity tests, not all internal columns. Development — no registry entry.',status='FROZEN_BEFORE_PORT_FORCES',numerical_rule='Adjacent full derivative max change <=1e-6; port-column relative change <=1e-5; repeat <=1e-7; reciprocity <=1e-6 absolute. Baseline stationarity applies only to internal coordinates. No positivity requirement on port Schur block.',dynamics_rule='Prescribed r=(sin(.2t),.7*(1-cos(.13t))), tau 0..80; zero and nonzero internal preparations; full internal ODE versus memory ODE force max error <=1e-8 normalized. DOP853 rtol1e-11 atol1e-13.',scope='Port Hessian/coupling extension, four stationary references; conventional finite conservative harmonic elimination.')
for c in f['cases']:
 fn=f'graphite-safe-full/{c}/HESSIANS.npz';f['inputs'][fn]=hashlib.sha256((root/fn).read_bytes()).hexdigest()
(p/'FREEZE.json').write_text(json.dumps(f,indent=2)+'\n')
rows=[]
for c in f['cases']:
 o=p/c;o.mkdir();a,B,nei,b=load(c);N=len(B);m=B.shape[2];sign=np.where(a['atom_types']==2,1.,-1.);assert sign.sum()==0
 T=np.zeros((N,3,2));T[:,0,0]=sign/np.sqrt(N);T[:,1,1]=sign/np.sqrt(N);E=np.concatenate([B,T],axis=2);flat=E.reshape(3*N,m+2);assert np.max(abs(flat.T@flat-np.eye(m+2)))<1e-12
 vv,_=directions(m);vectors=np.zeros((11,m+2));vectors[:2,m:]=np.eye(2);vectors[2:,:m]=vv
 steps=[];metrics=[];safe=[]
 for j,w in enumerate(vectors):
  disp=np.einsum('nam,m->na',E,w);cap=1.25e-5 if j<2 else 2.5e-5;cl,_,_=clearance(nei,b,disp,f['branch_knots'],hmax=cap);top=min(cap,.8*cl);hh=top*np.array([1,.8,.6]);me,sa=input_guard(a['positions_A'],E,nei,b,disp,hh,np.array(f['branch_knots']));steps.append(hh);metrics.append(me);safe.append(sa)
 steps=np.array(steps);metrics=np.array(metrics);safe=np.array(safe);ok=bool(safe.all() and steps.min()>=1e-6 and metrics[:,0,:].max()<=1e-6)
 np.savez_compressed(o/'PLAN.npz',vectors=vectors,steps_A=steps,input_metrics=metrics,branch_safe=safe,B_extended=E)
 rows.append(dict(case=c,pass_preflight=ok,min_step=float(steps.min()),orthogonality_error=float(np.max(abs(flat.T@flat-np.eye(m+2))))))
(p/'FEASIBILITY.json').write_text(json.dumps(dict(all_pass=all(r['pass_preflight'] for r in rows),cases=rows),indent=2)+'\n')
seal={str(z.relative_to(p)):hashlib.sha256(z.read_bytes()).hexdigest() for z in p.glob('*/PLAN.npz')};seal['FEASIBILITY.json']=hashlib.sha256((p/'FEASIBILITY.json').read_bytes()).hexdigest();(p/'PRECHECK_SEAL.json').write_text(json.dumps(dict(files=seal),indent=2)+'\n')
print(rows)
