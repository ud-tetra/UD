from pathlib import Path
import numpy as np,json,hashlib
from numpy.linalg import norm,eigh,eigvalsh
from numpy.polynomial.legendre import leggauss
p=Path(__file__).resolve().parent; freeze=json.loads((p/'FREEZE.json').read_text());src=p.parent/freeze['input']
assert hashlib.sha256(src.read_bytes()).hexdigest()==freeze['input_sha256']
d=np.load(src);keys=sorted(k[:-2] for k in d.files if k.endswith('_H')); out={};rows=[]
quad={m:leggauss(m) for m in freeze['quadrature_orders']}
def rel(r,*terms):return float(norm(r)/max([1.]+[norm(t) for t in terms]))
for key in keys:
 H=d[key+'_H'];b=d[key+'_b'];n=len(b);h=b.copy();h[0]-=1;h/=norm(h);Z=(np.eye(n)-2*np.outer(h,h))[:,1:];T=np.column_stack([Z,b]);B=T.T@H@T;A=B[:-1,:-1];a=B[:-1,-1];k=B[-1,-1];om=np.sqrt(k);S=A-np.outer(a,a)/k
 lam,V=eigh(H);freq=np.sqrt(lam);lb,W=eigh(B);fb=np.sqrt(lb);period=2*np.pi/om
 metrics={s:0. for s in ['orthogonality','block_reconstruction','full_block_evolution','displacement_memory','velocity_memory','hidden_reconstruction','quadrature_difference','energy','time_reversal']}
 metrics['orthogonality']=rel(T.T@T-np.eye(n));metrics['block_reconstruction']=rel(H-T@B@T.T,H)
 e=np.zeros(n-1);e[0]=1;xx=np.sin(np.arange(1,n));xx/=norm(xx);vv=np.cos(np.arange(1,n));vv/=norm(vv)
 states=[(e,0.,np.zeros(n-1),0.),(np.zeros(n-1),1.,np.zeros(n-1),0.),(xx,.3,.2*vv,-.4),(e,-a@e/k,np.zeros(n-1),0.)]
 records=[]
 for si,(x0,z0,v0,w0) in enumerate(states):
  q0=Z@x0+b*z0;vfull=Z@v0+b*w0;c=V.T@q0;dv=V.T@vfull;bc=W.T@(T.T@q0);bd=W.T@(T.T@vfull)
  def traj(t):
   t=np.atleast_1d(t);co=np.cos(freq[:,None]*t);sn=np.sin(freq[:,None]*t)
   q=V@(c[:,None]*co+dv[:,None]*sn/freq[:,None]);v=V@(-c[:,None]*freq[:,None]*sn+dv[:,None]*co);return q,v
  E0=.5*(vfull@vfull+q0@H@q0)
  for tt in freeze['sample_times_hidden_periods']:
   t=tt*period;q,v=traj(t);q=q[:,0];v=v[:,0];x=Z.T@q;vel=Z.T@v;acc=-Z.T@H@q;z=b@q
   qb=T@W@(bc*np.cos(fb*t)+bd*np.sin(fb*t)/fb);vb=T@W@(-bc*fb*np.sin(fb*t)+bd*np.cos(fb*t))
   metrics['full_block_evolution']=max(metrics['full_block_evolution'],rel(q-qb,q),rel(v-vb,v))
   qm,vm=traj(-t);qrev=V@(c*np.cos(freq*t)-dv*np.sin(freq*t)/freq);vrev=V@(c*freq*np.sin(freq*t)+dv*np.cos(freq*t))
   metrics['time_reversal']=max(metrics['time_reversal'],rel(qm[:,0]-qrev,qrev),rel(vm[:,0]-vrev,vrev))
   E=.5*(v@v+q@H@q);metrics['energy']=max(metrics['energy'],abs(E-E0)/max(1,abs(E0)))
   integ=[]
   for order,(nodes,weights) in quad.items():
    s=(nodes+1)*t/2;qs,vs=traj(s);ax=a@(Z.T@qs);av=a@(Z.T@vs)
    Id=float(t/2*(weights@(np.sin(om*(t-s))/om*ax)));Iv=float(t/2*(weights@(np.cos(om*(t-s))*av)))
    zh=z0*np.cos(om*t)+w0*np.sin(om*t)/om
    rd=acc+A@x-a*Id+a*zh
    rhs=-a*((z0+a@x0/k)*np.cos(om*t)+w0*np.sin(om*t)/om)
    rv=acc+S@x+a/k*Iv-rhs
    metrics['displacement_memory']=max(metrics['displacement_memory'],rel(rd,acc,A@x,a*Id,a*zh))
    metrics['velocity_memory']=max(metrics['velocity_memory'],rel(rv,acc,S@x,a/k*Iv,rhs))
    metrics['hidden_reconstruction']=max(metrics['hidden_reconstruction'],abs(z-(zh-Id))/max(1,abs(z),abs(zh),abs(Id)))
    integ.append(np.array([Id,Iv]));records.append([si,tt,order,Id,Iv,float(norm(rd)),float(norm(rv)),float(z)])
   metrics['quadrature_difference']=max(metrics['quadrature_difference'],rel(integ[0]-integ[1],integ[1]))
 out[key+'_Z']=Z;out[key+'_A']=A;out[key+'_a']=a;out[key+'_k']=np.array(k);out[key+'_Schur']=S;out[key+'_checks']=np.array(records)
 row={'configuration':key,'dimension':n,'k':float(k),'omega_model_time_inverse':float(om),'coupling_norm':float(norm(a)),'kernel_amplitude_spectral_norm':float(a@a/k),'schur_min_eigenvalue':float(eigvalsh(S)[0]),'metrics':metrics}
 row['pass']=bool(k>0 and row['schur_min_eigenvalue']>0 and all(v<freeze['relative_residual_tolerance'] for v in metrics.values()) and metrics['orthogonality']<freeze['algebra_tolerance'] and metrics['block_reconstruction']<freeze['algebra_tolerance'] and metrics['energy']<freeze['energy_tolerance']);rows.append(row)
np.savez_compressed(p/'MEMORY.npz',**out)
r={'status':'PASS' if all(r['pass'] for r in rows) else 'FAIL','configurations':len(rows),'initial_states_per_configuration':4,'sample_times_per_state':6,'quadrature_orders':[256,512],'max_metrics':{s:max(r['metrics'][s] for r in rows) for s in rows[0]['metrics']},'rows':rows,'physical_promotion':0,'review':'constructor verification only'}
(p/'RESULTS.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k!='rows'},indent=2))
