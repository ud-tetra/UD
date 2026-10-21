from pathlib import Path
import sys,json,ctypes,time,numpy as np
from scipy.optimize import minimize,root as solve_root
from lammps import lammps
p=Path(__file__).resolve().parent;ROOT=p.parent;case=sys.argv[1];out=p/case;out.mkdir(exist_ok=True)
a=np.load(ROOT/'graphite-stationary'/case/'RELAXED.npz');B=np.load(ROOT/'graphite-sliding-port'/case/'PLAN.npz')['B_extended'];x0=a['positions_A'];N=len(x0);m=B.shape[-1];flat=B.reshape(3*N,m);old=np.load(ROOT/'graphite-sliding-port'/case/'MODEL.npz');ev,U=np.linalg.eigh(old['H']);R=np.zeros((m,m));R[:-2,:-2]=(U/np.sqrt(ev))@U.T;R[-2:,-2:]=np.eye(2)/np.sqrt(.002)
pat,name=case.split('_',1);params=ROOT/'lammps-runtime/lammps/share/lammps/potentials';plugin=ROOT/'graphite-width/plugin/kcz_width2.so';data=ROOT/'graphite-target-replay/selected'/pat/name/'struct.inp.data';l=lammps(cmdargs=['-screen','none','-log',str(out/'lammps.log')]);history=[];start=time.time()
try:
 for cmd in [f'plugin load {plugin}','units metal','boundary p p p','atom_style full','box tilt large',f'read_data {data}','pair_style hybrid/overlay rebo rebo kolmogorov/crespi/z/smooth 24',f'pair_coeff * * rebo 1 {params}/CH.rebo C NULL',f'pair_coeff * * rebo 2 {params}/CH.rebo NULL C',f'pair_coeff 1 2 kolmogorov/crespi/z/smooth {params}/CC.KC C C','neighbor 3.0 nsq','neigh_modify one 4096']:l.command(cmd)
 def evaluate(y):
  q=R@y;x=np.asarray(x0.astype(np.longdouble)+np.einsum('nam,m->na',B.astype(np.longdouble),q.astype(np.longdouble)),dtype=np.float64);x=np.ascontiguousarray(x);l.scatter_atoms('x',1,3,x.ctypes.data_as(ctypes.POINTER(ctypes.c_double)));l.command('run 0 pre yes post no');F=np.ctypeslib.as_array(l.gather_atoms('f',1,3),shape=(3*N,)).copy();E=float(l.get_thermo('pe'));g=flat.T@F;history.append([E,float(np.max(abs(g)))]);return E,g,x,F
 E0,g0,_,_=evaluate(np.zeros(m));qseed=np.zeros(m);qseed[-2]=.05*np.sqrt(N)/2;yseed=np.linalg.solve(R,qseed)
 def objective(y):
  E,g,_,_=evaluate(y);return E-E0,-R.T@g
 opt=minimize(objective,yseed,jac=True,method='L-BFGS-B',options={'gtol':1e-10,'ftol':0.,'maxiter':2000,'maxls':50});y=opt.x.copy();E,g,x,F=evaluate(y);np.savez_compressed(out/'PRE_POLISH.npz',q=R@y,positions_A=x,projected_force=g)
 stages=[dict(method='preconditioned L-BFGS-B',success=bool(opt.success),message=str(opt.message),iterations=int(opt.nit),max_force=float(np.max(abs(g))))]
 if np.max(abs(g))>1e-7:
  rr=solve_root(lambda yy:-R.T@evaluate(yy)[1],y,method='hybr',options={'xtol':1e-9,'eps':1e-10,'maxfev':2000});E2,g2,x2,F2=evaluate(rr.x);accepted=bool(np.max(abs(g2))<np.max(abs(g)));stages.append(dict(method='force-root polish',success=bool(rr.success),message=str(rr.message),accepted=accepted,max_force=float(np.max(abs(g2)))))
  if accepted:y=rr.x;E,g,x,F=E2,g2,x2,F2
 q=R@y;np.savez_compressed(out/'RELAXED.npz',q=q,positions_A=x,forces=F.reshape(N,3),projected_force=g,initial_positions_A=a['initial_positions_A'],atom_types=a['atom_types'],B_extended=B,reference_positions_A=x0)
 r=dict(case=case,stationarity_pass=bool(np.max(abs(g))<=1e-7),max_force_eV_per_A=float(np.max(abs(g))),energy_change_eV=E-E0,relative_slide_A=(2*q[-2:]/np.sqrt(N)).tolist(),global_translation_error_A=float(np.max(abs(np.mean(x-x0,axis=0)))),stages=stages,evaluations=len(history),seconds=time.time()-start)
 (out/'RELAXATION.json').write_text(json.dumps(r,indent=2)+'\n');np.savez_compressed(out/'HISTORY.npz',energy_force=history);print(json.dumps(r),flush=True)
finally:l.close()
