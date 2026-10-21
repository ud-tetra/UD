from pathlib import Path
import numpy as np,json,hashlib
from numpy.polynomial.legendre import leggauss
p=Path(__file__).resolve().parent;root=p.parent;checks=[]
for reg in ['CODE_FREEZE.json','ANALYSIS_FREEZE.json','PRECHECK_SEAL.json']:
 for fn,sha in json.loads((p/reg).read_text())['files'].items():assert hashlib.sha256((p/fn).read_bytes()).hexdigest()==sha
for fn,sha in json.loads((p/'FREEZE.json').read_text())['inputs'].items():assert hashlib.sha256((root/fn).read_bytes()).hexdigest()==sha
x,w=leggauss(192)
for row in json.loads((p/'RESULTS.json').read_text())['cases']:
 case=row['case'];o=p/case;model=np.load(o/'MODEL.npz');a=model['alpha'];U=model['U'];G=model['G'];V=model['normalized_P'];omega=np.sqrt(a);errs=[]
 for prep in ['zero','hidden']:
  z=np.load(o/(prep+'.npz'));q0=U.T@z['initial_q'];v0=U.T@z['initial_v']
  for i in range(0,801,50):
   t=z['tau'][i];s=(x+1)*t/2;r=np.column_stack([np.sin(.2*s),.7*(1-np.cos(.13*s))]);integral=np.sum((w*t/2)[:,None]*np.sin((t-s[:,None])*omega)/omega*(r@G.T),axis=0);qhat=np.cos(omega*t)*q0+np.sin(omega*t)/omega*v0-integral
   rt=np.array([np.sin(.2*t),.7*(1-np.cos(.13*t))]);acc=np.array([-.04*np.sin(.2*t),.01183*np.cos(.13*t)]);force=acc+V@rt+G.T@qhat;errs.append(float(np.max(abs(force-z['force_memory'][i]))))
 assert max(errs)<1e-10
 checks.append(dict(case=case,max_direct_quadrature_error=max(errs)))
(p/'VERIFICATION.json').write_text(json.dumps(dict(status='PASS',scope='Constructor post-run independent quadrature implementation at17 times per preparation; source/code/plan hashes. Not independent reviewer.',cases=checks),indent=2)+'\n');print(checks)
