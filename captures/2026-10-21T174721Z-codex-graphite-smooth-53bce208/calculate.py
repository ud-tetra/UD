import os,json,pathlib,hashlib,ctypes,time,sys
import numpy as np
from lammps import lammps
root=pathlib.Path(__file__).resolve().parent
source=root.parent/'graphite-target-replay'/'selected'
params=root.parent/'lammps-runtime'/'lammps'/'share'/'lammps'/'potentials'
cases=[('21','dir_0'),('21','dir_10024'),('31','dir_10084'),('31','dir_10134')]
steps=[1e-4,5e-5]
cutoff=float(sys.argv[2])
contract={'cases':cases,'steps_A':steps,'scope':'primitive-periodic vertical sector only; omitted Bloch sectors untested','K':'negative central derivative of vertical Cartesian force with respect to each vertical coordinate','g':'negative central derivative of vertical force under rigid lateral translation of layer2; separate laboratory x,y columns','constraints':'fixed lateral coordinates except imposed sliding; all z free; one global z translation removed','K_units':'eV/Angstrom^2','g_units':'eV/Angstrom^2','step_relative_Fro_tolerance':1e-5,'step_absolute_max_tolerance':1e-6,'g_absolute_max_tolerance':1e-7,'symmetry_relative_Fro_tolerance':1e-6,'null_relative_2_tolerance':1e-6,'positive_test':'minimum projected eigenvalue positive; no interval or physical stability certificate','runtime_version':20250722,'physical_promotion':0,'review':'constructor only','lane':'Development — no registry entry'}
(root/('REDUCED_FREEZE_'+sys.argv[1]+'_'+sys.argv[2]+'.json')).write_text(json.dumps(contract,indent=2)+'\n')
results=[]
case_index=int(sys.argv[1]); cases=[cases[case_index]]
for pat,name in cases:
 start=time.time();p=source/pat/name;out=root/(pat+'_'+name)/('cutoff_'+sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
 l=lammps(cmdargs=['-screen','none','-log',str(out/'lammps.log')])
 try:
  commands=[f'plugin load {root}/plugin/kcz_smooth.so','units metal','boundary p p p','atom_style full','box tilt large',f'read_data {p}/struct.inp.data',f'pair_style hybrid/overlay rebo rebo kolmogorov/crespi/z/smooth {cutoff}',f'pair_coeff * * rebo 1 {params}/CH.rebo C NULL',f'pair_coeff * * rebo 2 {params}/CH.rebo NULL C',f'pair_coeff 1 2 kolmogorov/crespi/z/smooth {params}/CC.KC C C','neighbor 3.0 nsq','neigh_modify one 4096','thermo_modify format float %18.18g','fix 2 all lineforce 0.0 0.0 1.0','min_style cg','min_modify dmax 0.005','minimize 1.0e-15 1.0e-15 30000 30000']
  for cmd in commands:l.command(cmd)
  n=l.get_natoms();x0=np.ctypeslib.as_array(l.gather_atoms('x',1,3),shape=(n*3,)).copy().reshape(n,3)
  typ=np.ctypeslib.as_array(l.gather_atoms('type',0,1),shape=(n,)).copy();top=typ==2
  f0=np.ctypeslib.as_array(l.gather_atoms('f',1,3),shape=(n*3,)).copy().reshape(n,3)[:,2]
  def force(x):
   a=np.ascontiguousarray(x,dtype=np.float64);l.scatter_atoms('x',1,3,a.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
   l.command('run 0 pre yes post no')
   return np.ctypeslib.as_array(l.gather_atoms('f',1,3),shape=(n*3,)).copy().reshape(n,3)[:,2]
  mult=6 if pat=='21' else 5
  lines=(p/'struct.inp.data').read_text().splitlines()
  lx=float(next(x for x in lines if 'xlo xhi' in x).split()[1]);ly=float(next(x for x in lines if 'ylo yhi' in x).split()[1]);xy=float(next(x for x in lines if 'xy xz yz' in x).split()[0])
  ay=x0[:,1]/ly;ax=(x0[:,0]-xy*ay)/lx
  frac=np.stack([np.mod(ax*mult,1),np.mod(ay*mult,1)],axis=1)
  frac[np.isclose(frac,1,atol=1e-8)]=0
  keys=[(int(typ[i]),round(float(frac[i,0]),7),round(float(frac[i,1]),7)) for i in range(n)]
  unique=sorted(set(keys));d=len(unique); assert d==(28 if pat=='21' else 52),(d,unique)
  index={k:i for i,k in enumerate(unique)};group=np.array([index[k] for k in keys]);counts=np.bincount(group);assert np.all(counts==mult**2)
  P=np.zeros((n,d));P[np.arange(n),group]=1/np.sqrt(counts[group])
  assert np.max(np.abs(P.T@P-np.eye(d)))<1e-12
  zmean=P@(P.T@x0[:,2]);zdev=np.max(np.abs(x0[:,2]-zmean))
  Ks=[];gs=[];leaks=[];g_leaks=[];rawcolumns=[];rawgs=[]
  for h in steps:
   C=np.empty((n,d))
   for j in range(d):
    xp=x0.copy();xm=x0.copy();xp[:,2]+=h*P[:,j];xm[:,2]-=h*P[:,j]
    C[:,j]=-(force(xp)-force(xm))/(2*h)
    if j%200==0:print(json.dumps({'case':pat+'_'+name,'h':h,'column':j,'n':n}),flush=True)
   g=np.empty((n,2))
   for axis in range(2):
    xp=x0.copy();xm=x0.copy();xp[top,axis]+=h;xm[top,axis]-=h
    g[:,axis]=-(force(xp)-force(xm))/(2*h)
   K=P.T@C; gp=P.T@g
   leaks.append(float(np.linalg.norm(C-P@K)/np.linalg.norm(C)));g_leaks.append(float(np.linalg.norm(g-P@gp)/max(np.linalg.norm(g),1e-30)));rawcolumns.append(C);rawgs.append(g)
   Ks.append(K);gs.append(gp)
  # Full matrix space; Householder maps the normalized constant vector to e0.
  u=np.ones(d)/np.sqrt(d);v=u.copy();v[0]-=1;v/=np.linalg.norm(v)
  H=np.eye(d)-2*np.outer(v,v);Q=H[:,1:]
  K=Ks[-1];S=(K+K.T)/2;reduced=Q.T@S@Q;eigs=np.linalg.eigvalsh(reduced)
  dK=Ks[1]-Ks[0];dg=gs[1]-gs[0]
  norm=np.linalg.norm(K);sym=np.linalg.norm(K-K.T)/norm;null=np.linalg.norm(K@u)/norm
  flags={'K_step_relative':np.linalg.norm(dK)/norm<=1e-5,'K_step_max':np.max(np.abs(dK))<=1e-6,'g_step_max':np.max(np.abs(dg))<=1e-7,'symmetry':sym<=1e-6,'translation_null':null<=1e-6,'projected_positive':eigs[0]>0,'K_sector_invariance':max(leaks)<=1e-5,'g_sector_invariance':max(g_leaks)<=1e-5}
  result={'pattern':pat,'case':name,'cutoff_A':cutoff,'model_id':'KCz-C2-unshifted-tail-v0.1','atoms':n,'sector_dimension':d,'projected_dimension':d-1,'K_sector_leakage_relative':leaks,'g_sector_leakage_relative':g_leaks,'equilibrium_periodicity_max_A':float(zdev),'initial_vertical_force_max_eV_per_A':float(np.max(np.abs(f0))),'K_norm_F_eV_per_A2':float(norm),'K_step_relative_F':float(np.linalg.norm(dK)/norm),'K_step_max_eV_per_A2':float(np.max(np.abs(dK))),'g_step_max_eV_per_A2':float(np.max(np.abs(dg))),'symmetry_relative_F':float(sym),'translation_null_relative':float(null),'minimum_projected_eigenvalue_eV_per_A2':float(eigs[0]),'maximum_projected_eigenvalue_eV_per_A2':float(eigs[-1]),'g_column_norms_eV_per_A2':np.linalg.norm(gs[-1],axis=0).tolist(),'g_translation_components':(u@gs[-1]).tolist(),'checks':flags,'all_checks_pass':all(flags.values()),'seconds':time.time()-start}
  if all(flags.values()):
   response=Q@np.linalg.solve(reduced,Q.T@gs[-1]);result['equilibrium_vertical_response_norms_per_A_slide']=np.linalg.norm(response,axis=0).tolist();result['stationary_response_only_no_bath']=True
  np.savez_compressed(out/'MATRICES.npz',K_coarse=Ks[0],K_fine=Ks[1],g_coarse=gs[0],g_fine=gs[1],equilibrium_positions_A=x0,vertical_forces=f0,eigenvalues_projected=eigs,atom_types=typ,group_index=group,raw_K_columns_coarse=rawcolumns[0],raw_K_columns_fine=rawcolumns[-1],raw_g_coarse=rawgs[0],raw_g_fine=rawgs[-1])
  result['matrix_sha256']=hashlib.sha256((out/'MATRICES.npz').read_bytes()).hexdigest()
 except Exception as e:
  result={'pattern':pat,'case':name,'cutoff_A':cutoff,'model_id':'KCz-C2-unshifted-tail-v0.1','error':str(e),'all_checks_pass':False};raise
 finally:l.close()
 result['final_log_sha256']=hashlib.sha256((out/'lammps.log').read_bytes()).hexdigest()
 results.append(result);(out/'RESULTS.json').write_text(json.dumps({'cases':results,'physical_promotion':0,'independent_review':'pending'},indent=2,default=lambda x:x.item())+'\n');print(json.dumps(result,default=lambda x:x.item()),flush=True)
