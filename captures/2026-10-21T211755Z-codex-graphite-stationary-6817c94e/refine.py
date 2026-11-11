from pathlib import Path
import numpy as np,json,ctypes,sys,hashlib,time
from lammps import lammps
p=Path(__file__).resolve().parent;root=p.parent;freeze=json.loads((p/'FREEZE.json').read_text());rf=json.loads((p/'REFINEMENT_FREEZE.json').read_text());cfg=freeze['inputs'][int(sys.argv[1])];case=cfg['case'];out=p/case;path=out/'RELAXED.npz';assert hashlib.sha256(path.read_bytes()).hexdigest()==rf['inputs'][str(path.relative_to(p))];a=np.load(path);basis=np.load(out/'HESSIAN.npz');P=basis['primitive_P'];S=basis['basis_S'];Q=basis['basis_Q'];d=P.shape[1];nx=d-2;m=3*d-5;N=len(a['positions_A']);B=np.zeros((N,3,m));B[:,0,:nx]=P@S;B[:,1,nx:2*nx]=P@S;B[:,2,2*nx:]=P@Q;flat=B.reshape(3*N,m);x=a['positions_A'];pat,name=case.split('_',1);params=root/'lammps-runtime/lammps/share/lammps/potentials';plugin=root/'graphite-width/plugin/kcz_width2.so';data=root/'graphite-target-replay/selected'/pat/name/'struct.inp.data';l=lammps(cmdargs=['-screen','none','-log',str(out/'refinement.log')]);start=time.time()
try:
 for cmd in [f'plugin load {plugin}','units metal','boundary p p p','atom_style full','box tilt large',f'read_data {data}','pair_style hybrid/overlay rebo rebo kolmogorov/crespi/z/smooth 24',f'pair_coeff * * rebo 1 {params}/CH.rebo C NULL',f'pair_coeff * * rebo 2 {params}/CH.rebo NULL C',f'pair_coeff 1 2 kolmogorov/crespi/z/smooth {params}/CC.KC C C','neighbor 3.0 nsq','neigh_modify one 4096']:l.command(cmd)
 def force(xx):
  xx=np.ascontiguousarray(xx);l.scatter_atoms('x',1,3,xx.ctypes.data_as(ctypes.POINTER(ctypes.c_double)));l.command('run 0 pre yes post no');F=np.ctypeslib.as_array(l.gather_atoms('f',1,3),shape=(3*N,)).copy();return flat.T@F
 g=force(x);Hs=[]
 for step in rf['hessian_steps_A']:
  H=np.empty((m,m))
  for j in range(m):H[:,j]=-(force(x+step*B[:,:,j])-force(x-step*B[:,:,j]))/(2*step)
  Hs.append(H)
 Hc,Hf=Hs;H=(Hf+Hf.T)/2;delta=Hf-Hc;ev=np.linalg.eigvalsh(H);unc=np.linalg.norm(delta,2);th=max(1e-7,10*unc);stability='POSITIVE_RESOLVED' if ev[0]>th else 'NEGATIVE_RESOLVED' if ev[0]<-th else 'UNRESOLVED';den=np.linalg.norm(H[:,2*nx:]);ratio=np.linalg.norm(H[:2*nx,2*nx:])/den;cu=np.linalg.norm(delta[:,2*nx:])/den;coupling='RESOLVED_NONZERO' if ratio>1e-6 and ratio>10*cu else 'BELOW_THRESHOLD' if ratio<=1e-6 else 'UNRESOLVED';directions=[];raw=[]
 for i in range(3):
  w=np.sin((i+1)*np.arange(1,m+1));w/=np.linalg.norm(w);h=rf['directional_step_A'];z=-(force(x+h*np.einsum('nam,m->na',B,w))-force(x-h*np.einsum('nam,m->na',B,w)))/(2*h);err=z-H@w;raw.append(z);directions.append({'relative_error':float(np.linalg.norm(err)/np.linalg.norm(H@w)),'max_abs_error':float(np.max(np.abs(err)))})
 flags={'stationarity':np.max(np.abs(g))<=1e-7,'step_relative':np.linalg.norm(delta)/np.linalg.norm(H)<1e-5,'step_absolute':np.max(np.abs(delta))<1e-6,'symmetry':np.linalg.norm(Hf-Hf.T)/np.linalg.norm(H)<1e-6,'directional':all(x['relative_error']<1e-5 and x['max_abs_error']<1e-6 for x in directions)}
 np.savez_compressed(out/'REFINED_HESSIAN.npz',H_coarse=Hc,H_fine=Hf,eigenvalues=ev,directional_force_columns=np.array(raw),fresh_projected_force=g)
 r={'case':case,'checks':{k:bool(v) for k,v in flags.items()},'all_checks_pass':bool(all(flags.values())),'stability':stability,'eigenvalue_min':float(ev[0]),'eigenvalue_max':float(ev[-1]),'spectral_step_diagnostic':float(unc),'stability_threshold':float(th),'coupling':coupling,'coupling_relative':float(ratio),'step_relative':float(np.linalg.norm(delta)/np.linalg.norm(H)),'step_absolute':float(np.max(np.abs(delta))),'symmetry_relative':float(np.linalg.norm(Hf-Hf.T)/np.linalg.norm(H)),'directional_checks':directions,'seconds':time.time()-start,'physical_promotion':0};(out/'REFINED_RESULTS.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r),flush=True)
finally:l.close()
