from pathlib import Path
import numpy as np,json,ctypes,sys,hashlib,time
from lammps import lammps
from geometry import setup,clearance
p=Path(__file__).resolve().parent;root=p.parent;f=json.loads((p/'FREEZE.json').read_text());case=list(f['inputs'])[int(sys.argv[1])];source=root/'graphite-stationary'/case
for fn,sha in f['inputs'][case].items():assert hashlib.sha256((source/fn).read_bytes()).hexdigest()==sha
for fn,sha in f['source_hashes'].items():assert hashlib.sha256((root/fn).read_bytes()).hexdigest()==sha
out=p/case;out.mkdir(exist_ok=True);a=np.load(source/'RELAXED.npz');bas=np.load(source/'HESSIAN.npz');P=bas['primitive_P'];S=bas['basis_S'];Q=bas['basis_Q'];d=P.shape[1];nx=d-2;m=3*d-5;x=a['positions_A'];N=len(x);B=np.zeros((N,3,m));B[:,0,:nx]=P@S;B[:,1,nx:2*nx]=P@S;B[:,2,2*nx:]=P@Q;flat=B.reshape(3*N,m);assert np.max(abs(flat.T@flat-np.eye(m)))<1e-12;nei,bonds=setup(root,case,a);steps=[];guards=[]
for j in range(m):
 c,n,res=clearance(nei,bonds,B[:,:,j],f['branch_knots']);valid=[h for h in f['fine_ladder_A'] if h<=.9*c];assert valid,'No safe declared step';h=valid[0];steps.append(h);guards.append({'column':j,'fine_step_A':h,'nearest_crossing_A':None if not np.isfinite(c) else c,'polynomials_checked':n,'max_root_cosine_residual':res})
(out/'GEOMETRY_SELECTION.json').write_text(json.dumps({'case':case,'columns':guards},indent=2)+'\n');print('geometry frozen '+case+' '+str(dict(zip(*np.unique(steps,return_counts=True)))),flush=True)
pat,name=case.split('_',1);params=root/'lammps-runtime/lammps/share/lammps/potentials';plugin=root/'graphite-width/plugin/kcz_width2.so';data=root/'graphite-target-replay/selected'/pat/name/'struct.inp.data';l=lammps(cmdargs=['-screen','none','-log',str(out/'lammps.log')]);start=time.time()
try:
 for cmd in [f'plugin load {plugin}','units metal','boundary p p p','atom_style full','box tilt large',f'read_data {data}','pair_style hybrid/overlay rebo rebo kolmogorov/crespi/z/smooth 24',f'pair_coeff * * rebo 1 {params}/CH.rebo C NULL',f'pair_coeff * * rebo 2 {params}/CH.rebo NULL C',f'pair_coeff 1 2 kolmogorov/crespi/z/smooth {params}/CC.KC C C','neighbor 3.0 nsq','neigh_modify one 4096']:l.command(cmd)
 def force(xx):
  xx=np.ascontiguousarray(xx);l.scatter_atoms('x',1,3,xx.ctypes.data_as(ctypes.POINTER(ctypes.c_double)));l.command('run 0 pre yes post no');v=np.ctypeslib.as_array(l.gather_atoms('f',1,3),shape=(3*N,)).copy();return flat.T@v
 g0=force(x);raw=np.empty((m,3,2,m));Hs=np.empty((3,m,m))
 for j,h in enumerate(steps):
  for k,hk in enumerate([2*h,h,h/2]):
   raw[j,k,0]=force(x+hk*B[:,:,j]);raw[j,k,1]=force(x-hk*B[:,:,j]);Hs[k,:,j]=-(raw[j,k,0]-raw[j,k,1])/(2*hk)
  if j%20==0:print('column '+str(j)+'/'+str(m),flush=True)
 np.savez_compressed(out/'MATRIX_RAW.npz',raw_forces=raw,matrices=Hs,fine_steps_A=steps,baseline_force=g0)
 Hc,Hf,Ha=Hs;H=(Hf+Hf.T)/2;V=[]
 for i in range(3):w=np.sin((i+1)*np.arange(1,m+1));V.append(w/np.linalg.norm(w))
 for freq in np.sqrt([2,3,5]):w=np.cos(freq*np.arange(1,m+1));V.append(w/np.linalg.norm(w))
 dr=np.empty((6,3,2,m));Ds=np.empty((6,3,m))
 for i,w in enumerate(V):
  disp=np.einsum('nam,m->na',B,w)
  for k,h in enumerate([2.5e-5,1.25e-5,6.25e-6]):dr[i,k,0]=force(x+h*disp);dr[i,k,1]=force(x-h*disp);Ds[i,k]=-(dr[i,k,0]-dr[i,k,1])/(2*h)
 np.savez_compressed(out/'DIRECTION_RAW.npz',raw_forces=dr,derivatives=Ds,vectors=V,steps_A=[2.5e-5,1.25e-5,6.25e-6],final_baseline_force=force(x))
 (out/'TIMING.json').write_text(json.dumps({'seconds':time.time()-start})+'\n');print('COMPLETE '+case,flush=True)
finally:l.close()
