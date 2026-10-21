import os,json,pathlib,hashlib,ctypes,time
import numpy as np
from lammps import lammps
root=pathlib.Path(__file__).resolve().parent
source=root.parent/'graphite-target-replay'/'selected'
params=root.parent/'lammps-runtime'/'lammps'/'share'/'lammps'/'potentials'
cases=[('21','dir_0'),('21','dir_10024'),('31','dir_10084'),('31','dir_10134')]
steps=[1e-4,5e-5]
contract={'cases':cases,'steps_A':steps,'K':'negative central derivative of vertical Cartesian force with respect to each vertical coordinate','g':'negative central derivative of vertical force under rigid lateral translation of layer2; separate laboratory x,y columns','constraints':'fixed lateral coordinates except imposed sliding; all z free; one global z translation removed','K_units':'eV/Angstrom^2','g_units':'eV/Angstrom^2','step_relative_Fro_tolerance':1e-5,'step_absolute_max_tolerance':1e-6,'g_absolute_max_tolerance':1e-7,'symmetry_relative_Fro_tolerance':1e-6,'null_relative_2_tolerance':1e-6,'positive_test':'minimum projected eigenvalue positive; no interval or physical stability certificate','runtime_version':20250722,'physical_promotion':0,'review':'constructor only','lane':'Development — no registry entry'}
(root/'FREEZE.json').write_text(json.dumps(contract,indent=2)+'\n')
results=[]
for pat,name in cases:
 start=time.time();p=source/pat/name;out=root/(pat+'_'+name);out.mkdir(exist_ok=True)
 l=lammps(cmdargs=['-screen','none','-log',str(out/'lammps.log')])
 try:
  commands=['units metal','boundary p p p','atom_style full','box tilt large',f'read_data {p}/struct.inp.data','pair_style hybrid/overlay rebo rebo kolmogorov/crespi/z 16.0',f'pair_coeff * * rebo 1 {params}/CH.rebo C NULL',f'pair_coeff * * rebo 2 {params}/CH.rebo NULL C',f'pair_coeff 1 2 kolmogorov/crespi/z {params}/CC.KC C C','neighbor 3.0 nsq','neigh_modify one 4096','thermo_modify format float %18.18g','fix 2 all lineforce 0.0 0.0 1.0','min_style cg','min_modify dmax 0.005','minimize 1.0e-15 1.0e-15 30000 30000']
  for cmd in commands:l.command(cmd)
  n=l.get_natoms();x0=np.ctypeslib.as_array(l.gather_atoms('x',1,3),shape=(n*3,)).copy().reshape(n,3)
  typ=np.ctypeslib.as_array(l.gather_atoms('type',0,1),shape=(n,)).copy();top=typ==2
  f0=np.ctypeslib.as_array(l.gather_atoms('f',1,3),shape=(n*3,)).copy().reshape(n,3)[:,2]
  def force(x):
   a=np.ascontiguousarray(x,dtype=np.float64);l.scatter_atoms('x',1,3,a.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
   l.command('run 0 pre yes post no')
   return np.ctypeslib.as_array(l.gather_atoms('f',1,3),shape=(n*3,)).copy().reshape(n,3)[:,2]
  Ks=[];gs=[]
  for h in steps:
   K=np.empty((n,n))
   for j in range(n):
    xp=x0.copy();xm=x0.copy();xp[j,2]+=h;xm[j,2]-=h
    K[:,j]=-(force(xp)-force(xm))/(2*h)
    if j%200==0:print(json.dumps({'case':pat+'_'+name,'h':h,'column':j,'n':n}),flush=True)
   g=np.empty((n,2))
   for axis in range(2):
    xp=x0.copy();xm=x0.copy();xp[top,axis]+=h;xm[top,axis]-=h
    g[:,axis]=-(force(xp)-force(xm))/(2*h)
   Ks.append(K);gs.append(g)
  # Full matrix space; Householder maps the normalized constant vector to e0.
  u=np.ones(n)/np.sqrt(n);v=u.copy();v[0]-=1;v/=np.linalg.norm(v)
  H=np.eye(n)-2*np.outer(v,v);Q=H[:,1:]
  K=Ks[-1];S=(K+K.T)/2;reduced=Q.T@S@Q;eigs=np.linalg.eigvalsh(reduced)
  dK=Ks[1]-Ks[0];dg=gs[1]-gs[0]
  norm=np.linalg.norm(K);sym=np.linalg.norm(K-K.T)/norm;null=np.linalg.norm(K@u)/norm
  flags={'K_step_relative':np.linalg.norm(dK)/norm<=1e-5,'K_step_max':np.max(np.abs(dK))<=1e-6,'g_step_max':np.max(np.abs(dg))<=1e-7,'symmetry':sym<=1e-6,'translation_null':null<=1e-6,'projected_positive':eigs[0]>0}
  result={'pattern':pat,'case':name,'atoms':n,'projected_dimension':n-1,'initial_vertical_force_max_eV_per_A':float(np.max(np.abs(f0))),'K_norm_F_eV_per_A2':float(norm),'K_step_relative_F':float(np.linalg.norm(dK)/norm),'K_step_max_eV_per_A2':float(np.max(np.abs(dK))),'g_step_max_eV_per_A2':float(np.max(np.abs(dg))),'symmetry_relative_F':float(sym),'translation_null_relative':float(null),'minimum_projected_eigenvalue_eV_per_A2':float(eigs[0]),'maximum_projected_eigenvalue_eV_per_A2':float(eigs[-1]),'g_column_norms_eV_per_A2':np.linalg.norm(gs[-1],axis=0).tolist(),'g_translation_components':(u@gs[-1]).tolist(),'checks':flags,'all_checks_pass':all(flags.values()),'seconds':time.time()-start}
  if all(flags.values()):
   response=Q@np.linalg.solve(reduced,Q.T@gs[-1]);result['equilibrium_vertical_response_norms_per_A_slide']=np.linalg.norm(response,axis=0).tolist();result['stationary_response_only_no_bath']=True
  np.savez_compressed(out/'MATRICES.npz',K_coarse=Ks[0],K_fine=Ks[1],g_coarse=gs[0],g_fine=gs[1],equilibrium_positions_A=x0,vertical_forces=f0,eigenvalues_projected=eigs,atom_types=typ)
  result['matrix_sha256']=hashlib.sha256((out/'MATRICES.npz').read_bytes()).hexdigest()
 except Exception as e:
  result={'pattern':pat,'case':name,'error':str(e),'all_checks_pass':False};raise
 finally:l.close()
 result['final_log_sha256']=hashlib.sha256((out/'lammps.log').read_bytes()).hexdigest()
 results.append(result);(root/'RESULTS.json').write_text(json.dumps({'cases':results,'physical_promotion':0,'independent_review':'pending'},indent=2)+'\n');print(json.dumps(result),flush=True)
