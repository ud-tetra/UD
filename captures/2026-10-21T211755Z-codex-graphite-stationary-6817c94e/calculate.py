from pathlib import Path
import numpy as np,json,hashlib,ctypes,sys,time
from scipy.optimize import minimize
from lammps import lammps
p=Path(__file__).resolve().parent;root=p.parent;freeze=json.loads((p/'FREEZE.json').read_text());row=freeze['inputs'][int(sys.argv[1])];src=root/row['folder']/'MATRICES.npz';assert hashlib.sha256(src.read_bytes()).hexdigest()==row['sha256'];old=np.load(src);case=row['case'];pat,name=case.split('_',1);out=p/case;out.mkdir(exist_ok=True);start=time.time()
plugin=root/'graphite-width/plugin/kcz_width2.so';params=root/'lammps-runtime/lammps/share/lammps/potentials';data=root/'graphite-target-replay/selected'/pat/name/'struct.inp.data';l=lammps(cmdargs=['-screen','none','-log',str(out/'lammps.log')])
def helmert(d):
 Q=np.zeros((d,d-1))
 for j in range(d-1):Q[:j+1,j]=1/np.sqrt((j+1)*(j+2));Q[j+1,j]=-(j+1)/np.sqrt((j+1)*(j+2))
 return Q
try:
 for cmd in [f'plugin load {plugin}','units metal','boundary p p p','atom_style full','box tilt large',f'read_data {data}','pair_style hybrid/overlay rebo rebo kolmogorov/crespi/z/smooth 24',f'pair_coeff * * rebo 1 {params}/CH.rebo C NULL',f'pair_coeff * * rebo 2 {params}/CH.rebo NULL C',f'pair_coeff 1 2 kolmogorov/crespi/z/smooth {params}/CC.KC C C','neighbor 3.0 nsq','neigh_modify one 4096']:
  l.command(cmd)
 x0=old['equilibrium_positions_A'];N=len(x0);group=old['group_index'];d=int(max(group))+1;half=d//2;count=np.bincount(group);P=np.zeros((N,d));P[np.arange(N),group]=1/np.sqrt(count[group]);S=np.zeros((d,d-2));S[:half,:half-1]=helmert(half);S[half:,half-1:]=helmert(half);Q=helmert(d);nx=d-2;nz=d-1;m=2*nx+nz;B=np.zeros((N,3,m));B[:,0,:nx]=P@S;B[:,1,nx:2*nx]=P@S;B[:,2,2*nx:]=P@Q;flat=B.reshape(3*N,m)
 def evaluate(q):
  x=np.ascontiguousarray(x0+np.einsum('nam,m->na',B,q));l.scatter_atoms('x',1,3,x.ctypes.data_as(ctypes.POINTER(ctypes.c_double)));l.command('run 0 pre yes post no');F=np.ctypeslib.as_array(l.gather_atoms('f',1,3),shape=(3*N,)).copy().reshape(N,3);E=float(l.get_thermo('pe'));return E,F,flat.T@F.ravel(),x
 E0,F0,g0,_=evaluate(np.zeros(m));history=[];evaluations=0
 def objective(q):
  global evaluations
  E,F,g,x=evaluate(q);evaluations+=1
  if evaluations%20==0:print(json.dumps({'case':case,'evaluations':evaluations,'max_force':float(np.max(np.abs(g))),'delta_energy':E-E0}),flush=True)
  history.append([evaluations,E-E0,float(np.max(np.abs(g))),float(np.linalg.norm(g))]);return E-E0,-g
 opt=minimize(objective,np.zeros(m),jac=True,method='L-BFGS-B',options={'gtol':1e-9,'ftol':0.,'maxiter':2000,'maxls':50});q=opt.x.copy();stages=[{'stage':'L-BFGS-B','success':bool(opt.success),'message':str(opt.message),'iterations':int(opt.nit),'evaluations':evaluations}]
 def hessian(q,h):
  H=np.empty((m,m))
  for j in range(m):
   qp=q.copy();qm=q.copy();qp[j]+=h;qm[j]-=h;gp=evaluate(qp)[2];gm=evaluate(qm)[2];H[:,j]=-(gp-gm)/(2*h)
  return H
 for pol in range(3):
  E,F,g,x=evaluate(q);norm=float(np.max(np.abs(g)))
  np.savez_compressed(out/f'PRE_POLISH_{pol}.npz',q=q,positions_A=x,forces=F,projected_force=g)
  if norm<=1e-7:break
  H=hessian(q,1e-4);H=(H+H.T)/2
  try:step=np.linalg.solve(H,g)
  except np.linalg.LinAlgError:stages.append({'stage':'Newton','index':pol,'status':'SINGULAR_HESSIAN'});break
  atomstep=np.max(np.abs(flat@step));step*=min(1,.05/max(atomstep,1e-30));accepted=False
  for back in range(9):
   trial=q+step/(2**back);Et,Ft,gt,xt=evaluate(trial)
   if np.linalg.norm(gt)<np.linalg.norm(g):q=trial;accepted=True;break
  stages.append({'stage':'Newton','index':pol,'force_before':norm,'accepted':accepted,'halvings':back,'hessian_min_eigenvalue':float(np.linalg.eigvalsh(H)[0])})
  if not accepted:break
 E,F,g,x=evaluate(q);np.savez_compressed(out/'RELAXED.npz',q=q,positions_A=x,forces=F,projected_force=g,initial_positions_A=x0,group_index=group,atom_types=old['atom_types'],initial_projected_force=g0)
 (out/'OPTIMIZER.json').write_text(json.dumps({'stages':stages,'history':history,'energy_initial_eV':E0,'energy_final_eV':E},indent=2)+'\n');print(json.dumps({'case':case,'phase':'relaxed','max_force':float(np.max(np.abs(g))),'delta_energy_eV':E-E0}),flush=True)
 Hc=hessian(q,1e-4);Hf=hessian(q,5e-5);sym=(Hf+Hf.T)/2;delta=Hf-Hc;evals=np.linalg.eigvalsh(sym);unc=float(np.linalg.norm(delta,2));threshold=max(1e-7,10*unc);stab='POSITIVE_RESOLVED' if evals[0]>threshold else 'NEGATIVE_RESOLVED' if evals[0]<-threshold else 'UNRESOLVED';cross=sym[:2*nx,2*nx:];den=np.linalg.norm(sym[:,2*nx:]);ratio=float(np.linalg.norm(cross)/den);cross_unc=float(np.linalg.norm(delta[:,2*nx:])/den);coupling='RESOLVED_NONZERO' if ratio>1e-6 and ratio>10*cross_unc else 'BELOW_THRESHOLD' if ratio<=1e-6 else 'UNRESOLVED'
 directional=[]
 for i in range(3):
  w=np.sin((i+1)*np.arange(1,m+1));w/=np.linalg.norm(w);h=2.5e-5;diff=-(evaluate(q+h*w)[2]-evaluate(q-h*w)[2])/(2*h);pred=sym@w;err=diff-pred;directional.append({'relative_error':float(np.linalg.norm(err)/max(np.linalg.norm(pred),1e-30)),'max_abs_error':float(np.max(np.abs(err)))})
 typ=old['atom_types'];means=[float(np.mean((x-x0)[typ==t,axis])) for t in [1,2] for axis in [0,1]]+[float(np.mean((x-x0)[:,2]))];constraint=max(abs(s) for s in means)
 flags={'stationarity':float(np.max(np.abs(g)))<=1e-7,'constraints':constraint<1e-10,'orthogonality':np.linalg.norm(flat.T@flat-np.eye(m))<1e-10,'step_relative':np.linalg.norm(delta)/np.linalg.norm(sym)<1e-5,'step_absolute':np.max(np.abs(delta))<1e-6,'symmetry':np.linalg.norm(Hf-Hf.T)/np.linalg.norm(sym)<1e-6,'directional':all(v['relative_error']<1e-5 and v['max_abs_error']<1e-6 for v in directional)}
 np.savez_compressed(out/'HESSIAN.npz',H_coarse=Hc,H_fine=Hf,eigenvalues=evals,basis_S=S,basis_Q=Q,primitive_P=P,coordinates=q)
 result={**row,'dimension':m,'vertical_dimension':nz,'lateral_dimension':2*nx,'initial_projected_force_max_eV_per_A':float(np.max(np.abs(g0))),'final_projected_force_max_eV_per_A':float(np.max(np.abs(g))),'max_individual_lateral_force_eV_per_A':float(np.max(np.abs(F[:,:2]))),'energy_change_eV':E-E0,'max_atom_displacement_A':float(np.max(np.linalg.norm(x-x0,axis=1))),'max_constraint_error_A':constraint,'hessian_step_relative':float(np.linalg.norm(delta)/np.linalg.norm(sym)),'hessian_step_max_abs':float(np.max(np.abs(delta))),'hessian_asymmetry_relative':float(np.linalg.norm(Hf-Hf.T)/np.linalg.norm(sym)),'eigenvalue_min':float(evals[0]),'eigenvalue_max':float(evals[-1]),'spectral_step_diagnostic':unc,'stability_threshold':threshold,'stability':stab,'coupling_relative':ratio,'coupling_step_relative':cross_unc,'coupling':coupling,'directional_checks':directional,'checks':{k:bool(v) for k,v in flags.items()},'all_numerical_checks_pass':bool(all(flags.values())),'physical_promotion':0,'bath':'HOLD','seconds':time.time()-start}
 (out/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
finally:l.close()
