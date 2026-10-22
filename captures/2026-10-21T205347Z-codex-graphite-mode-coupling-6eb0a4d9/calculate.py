from pathlib import Path
import numpy as np,json,hashlib,ctypes,sys,time
from lammps import lammps
p=Path(__file__).resolve().parent;root=p.parent;freeze=json.loads((p/'FREEZE.json').read_text());row=freeze['inputs'][int(sys.argv[1])];src=root/row['folder']/'MATRICES.npz';assert hashlib.sha256(src.read_bytes()).hexdigest()==row['sha256'];old=np.load(src);case=row['case'];pat,name=case.split('_',1);cut=row['cutoff_A'];width=row['width_A'];out=p/f'{case}_c{cut}_w{width}';out.mkdir(exist_ok=True);start=time.time()
plugin=root/'graphite-width/plugin'/f'kcz_width{width}.so';params=root/'lammps-runtime/lammps/share/lammps/potentials';data=root/'graphite-target-replay/selected'/pat/name/'struct.inp.data'
l=lammps(cmdargs=['-screen','none','-log',str(out/'lammps.log')])
try:
 for cmd in [f'plugin load {plugin}','units metal','boundary p p p','atom_style full','box tilt large',f'read_data {data}',f'pair_style hybrid/overlay rebo rebo kolmogorov/crespi/z/smooth {cut}',f'pair_coeff * * rebo 1 {params}/CH.rebo C NULL',f'pair_coeff * * rebo 2 {params}/CH.rebo NULL C',f'pair_coeff 1 2 kolmogorov/crespi/z/smooth {params}/CC.KC C C','neighbor 3.0 nsq','neigh_modify one 4096']:
  l.command(cmd)
 x0=old['equilibrium_positions_A'];N=len(x0);group=old['group_index'];d=int(max(group))+1;count=np.bincount(group);P=np.zeros((N,d));P[np.arange(N),group]=1/np.sqrt(count[group]);Q=np.zeros((d,d-1))
 for j in range(d-1):Q[:j+1,j]=1/np.sqrt((j+1)*(j+2));Q[j+1,j]=-(j+1)/np.sqrt((j+1)*(j+2))
 def force(x):
  xx=np.ascontiguousarray(x);l.scatter_atoms('x',1,3,xx.ctypes.data_as(ctypes.POINTER(ctypes.c_double)));l.command('run 0 pre yes post no');return np.ctypeslib.as_array(l.gather_atoms('f',1,3),shape=(3*N,)).copy().reshape(N,3)
 f0=force(x0);Cs=[];recip=[]
 for h in freeze['steps_A']:
  if len(sys.argv)>2 and sys.argv[2]=='reuse':
   saved=np.load(p/'development_failure'/out.name/'COLUMNS.npz');C=saved['full_columns_coarse' if h==freeze['steps_A'][0] else 'full_columns_fine']
  else:
   C=np.empty((N,3,d))
   for j in range(d):
    xp=x0.copy();xm=x0.copy();xp[:,2]+=h*P[:,j];xm[:,2]-=h*P[:,j];C[:,:,j]=-(force(xp)-force(xm))/(2*h)
  Cs.append(C)
  rec=[]
  for axis in [0,1]:
   for trig in [np.sin,np.cos]:
    v=trig(np.arange(1,d+1));v/=np.linalg.norm(v);xp=x0.copy();xm=x0.copy();xp[:,axis]+=h*(P@v);xm[:,axis]-=h*(P@v);reverse=-P.T@(force(xp)[:,2]-force(xm)[:,2])/(2*h);forward=v@(P.T@C[:,axis,:]);rec.append(float(np.max(np.abs(reverse-forward))))
  recip.append(rec)
 Cc,C=Cs;CQ=np.einsum('nad,dm->nam',C,Q);coarseQ=np.einsum('nad,dm->nam',Cc,Q);norm=np.linalg.norm(CQ);delta=np.linalg.norm(CQ-coarseQ)/norm
 blocks={};decomp=[]
 for axis,aname in [(0,'x'),(1,'y'),(2,'z')]:
  primitive=P.T@CQ[:,axis,:];nonprimitive=CQ[:,axis,:]-P@primitive;blocks[aname+'_primitive']=primitive;blocks[aname+'_nonprimitive']=nonprimitive
  decomp.append(np.linalg.norm(primitive)**2+np.linalg.norm(nonprimitive)**2)
 kval=Q.T@P.T@C[:,2,:]@Q;prior=Q.T@old['K_fine']@Q;match=np.linalg.norm(kval-prior)/np.linalg.norm(prior)
 xyz_primitive=np.stack([P.T@C[:,axis,:] for axis in [0,1,2]])
 stats={'vertical_nonprimitive':float(np.linalg.norm(blocks['z_nonprimitive'])/norm),'inplane_primitive':float(np.linalg.norm(xyz_primitive[:2]@Q)/norm),'inplane_nonprimitive':float(np.linalg.norm(np.stack([blocks['x_nonprimitive'],blocks['y_nonprimitive']]))/norm)}
 classification={k:('RESOLVED_NONZERO' if v>freeze['qualification']['resolved_nonzero_relative'] and v>10*delta else 'BELOW_THRESHOLD' if v<=freeze['qualification']['resolved_nonzero_relative'] else 'UNRESOLVED') for k,v in stats.items()}
 flags={'full_column_step_relative':delta<1e-5,'full_column_step_max':float(np.max(np.abs(C-Cc)))<1e-6,'retained_block_match':match<1e-8,'reciprocity':max(max(x) for x in recip)<1e-6,'decomposition':abs(sum(decomp)-norm*norm)/max(1,norm*norm)<1e-10}
 periodic_z=x0[:,2]-P@(P.T@x0[:,2]);vertical_null=float(np.linalg.norm(np.ones(d)@xyz_primitive[2]@Q)/norm/np.sqrt(d))
 np.savez_compressed(out/'COLUMNS.npz',full_columns_coarse=Cc,full_columns_fine=C,primitive_blocks_fine=xyz_primitive,equilibrium_positions_A=x0,atom_types=old['atom_types'],group_index=group,prior_K_fine=old['K_fine'],prior_g_fine=old['g_fine'],baseline_full_forces=f0)
 result={**row,'configuration':out.name,'atoms':N,'primitive_dimension':d,'quotient_dimension':d-1,'relative_output_components':stats,'classification':classification,'full_column_step_relative':float(delta),'full_column_step_max_eV_per_A2':float(np.max(np.abs(C-Cc))),'retained_block_match_relative':float(match),'reciprocity_max_abs':float(max(max(x) for x in recip)),'vertical_translation_output_relative':vertical_null,'baseline_inplane_force_max_eV_per_A':float(np.max(np.abs(f0[:,:2]))),'baseline_vertical_force_max_eV_per_A':float(np.max(np.abs(f0[:,2]))),'baseline_inplane_force_norm_eV_per_A':float(np.linalg.norm(f0[:,:2])),'equilibrium_z_periodicity_max_A':float(np.max(np.abs(periodic_z))),'column_norm_F_eV_per_A2':float(norm),'checks':flags,'all_checks_pass':all(flags.values()),'seconds':time.time()-start,'column_archive_sha256':hashlib.sha256((out/'COLUMNS.npz').read_bytes()).hexdigest(),'plugin_sha256':hashlib.sha256(plugin.read_bytes()).hexdigest()}
 (out/'RESULTS.json').write_text(json.dumps(result,indent=2,default=lambda x:x.item())+'\n');print(json.dumps(result,default=lambda x:x.item()),flush=True)
finally:l.close()
