from pathlib import Path
import numpy as np,json,ctypes,sys,hashlib,time
from lammps import lammps
p=Path(__file__).resolve().parent;root=p.parent;f=json.loads((p/'FREEZE.json').read_text());cfg=f['inputs'][int(sys.argv[1])];case=cfg['case'];source=root/'graphite-stationary'/case
for fn,sha in cfg['files'].items():assert hashlib.sha256((source/fn).read_bytes()).hexdigest()==sha
out=p/(case+'_REBO_ONLY');out.mkdir(exist_ok=True);a=np.load(source/'RELAXED.npz');bas=np.load(source/'HESSIAN.npz');old=np.load(source/'REFINED_HESSIAN.npz');H=(old['H_fine']+old['H_fine'].T)/2;P=bas['primitive_P'];S=bas['basis_S'];Q=bas['basis_Q'];d=P.shape[1];nx=d-2;m=3*d-5;x=a['positions_A'];N=len(x);B=np.zeros((N,3,m));B[:,0,:nx]=P@S;B[:,1,nx:2*nx]=P@S;B[:,2,2*nx:]=P@Q;flat=B.reshape(3*N,m);pat,name=case.split('_',1);params=root/'lammps-runtime/lammps/share/lammps/potentials';plugin=root/'graphite-width/plugin/kcz_width2.so';data=root/'graphite-target-replay/selected'/pat/name/'struct.inp.data';l=lammps(cmdargs=['-screen','none','-log',str(out/'lammps.log')]);start=time.time()
try:
 for cmd in [f'plugin load {plugin}','units metal','boundary p p p','atom_style full','box tilt large',f'read_data {data}','pair_style hybrid/overlay rebo rebo',f'pair_coeff * * rebo 1 {params}/CH.rebo C NULL',f'pair_coeff * * rebo 2 {params}/CH.rebo NULL C','pair_coeff 1 2 none','neighbor 3.0 nsq','neigh_modify one 4096']:l.command(cmd)
 def force(xx):
  xx=np.ascontiguousarray(xx);l.scatter_atoms('x',1,3,xx.ctypes.data_as(ctypes.POINTER(ctypes.c_double)));l.command('run 0 pre yes post no');v=np.ctypeslib.as_array(l.gather_atoms('f',1,3),shape=(3*N,)).copy();return flat.T@v
 g0=force(x);gb=force(x);vectors=[];names=[]
 for i in range(3):w=np.sin((i+1)*np.arange(1,m+1));w/=np.linalg.norm(w);vectors.append(w);names.append('direction_'+str(i))
 for j in cfg['columns']:w=np.zeros(m);w[j]=1;vectors.append(w);names.append('column_'+str(j))
 allplus=[];allminus=[];allqe=[];allperp=[];rows=[]
 for name,w in zip(names,vectors):
  disp=np.einsum('nam,m->na',B,w);plus=[];minus=[];qes=[];perps=[];ladder=[];derivs=[]
  for h in f['steps_A']:
   xp=x+h*disp;xm=x-h*disp;gp=force(xp);gm=force(xm);D=-(gp-gm)/(2*h);plus.append(gp);minus.append(gm);derivs.append(D);eff=(xp-xm).ravel()/(2*h);qe=flat.T@eff;perp=eff-flat@qe;qes.append(qe);perps.append(float(np.linalg.norm(perp)));nominal=D-H@w;corrected=D-H@qe
   ladder.append({'step_A':h,'nominal_error_max':float(np.max(abs(nominal))),'nominal_error_relative':float(np.linalg.norm(nominal)/np.linalg.norm(H@w)),'effective_tangent_error_max':float(np.max(abs(corrected))),'input_direction_error_norm':float(np.linalg.norm(eff-flat@w)),'input_tangent_error_norm':float(np.linalg.norm(qe-w)),'input_orthogonal_error_norm':float(np.linalg.norm(perp)),'max_actual_atom_displacement_A':float(np.max(abs(xp-x))),'step_rounding_max_A':float(max(np.max(abs((xp-x)-h*disp)),np.max(abs((xm-x)+h*disp)))),'successive_max_change':None if len(derivs)==1 else float(np.max(abs(derivs[-1]-derivs[-2]))),'one_sided_difference_max':float(np.max(abs(-(gp-g0)/h-(gm-g0)/h)))})
  changes=[z['successive_max_change'] for z in ladder];windows=[[f['steps_A'][i],f['steps_A'][i+1],f['steps_A'][i+2]] for i in range(len(changes)-2) if changes[i+1]<1e-6 and changes[i+2]<1e-6];rows.append({'observable':name,'stable_three_step_windows':windows,'ladder':ladder});allplus.append(plus);allminus.append(minus);allqe.append(qes);allperp.append(perps)
 end0=force(x);end1=force(x);np.savez_compressed(out/'RAW.npz',positive_forces=np.array(allplus),negative_forces=np.array(allminus),baseline_forces=np.array([g0,gb,end0,end1]),effective_tangent_directions=np.array(allqe),orthogonal_direction_norms=np.array(allperp),vectors=np.array(vectors),steps=np.array(f['steps_A']))
 result={'case':case,'baseline_reproduction_max':float(max(np.max(abs(z-a['projected_force'])) for z in [g0,gb,end0,end1])),'baseline_repeat_difference_max':float(max(np.max(abs(z-g0)) for z in [gb,end0,end1])),'observables':rows,'physical_promotion':0,'purpose':'diagnostic only; original qualification unchanged','seconds':time.time()-start};(out/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'case':case,'seconds':result['seconds'],'baseline_error':result['baseline_reproduction_max']}),flush=True)
finally:l.close()
