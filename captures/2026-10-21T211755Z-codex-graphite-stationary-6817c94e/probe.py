from pathlib import Path
import numpy as np,json,ctypes,sys,hashlib
from lammps import lammps
p=Path(__file__).resolve().parent;root=p.parent;f=json.loads((p/'FREEZE.json').read_text());cfg=f['inputs'][int(sys.argv[1])];case=cfg['case'];out=p/case;diag=json.loads((p/'DIAGNOSTIC_FREEZE.json').read_text());a=np.load(out/'RELAXED.npz');h=np.load(out/'HESSIAN.npz');diff=h['H_fine']-h['H_coarse'];columns=np.argsort(np.max(np.abs(diff),axis=0))[-2:][::-1];P=h['primitive_P'];S=h['basis_S'];Q=h['basis_Q'];d=P.shape[1];nx=d-2;m=3*d-5;N=len(a['positions_A']);B=np.zeros((N,3,m));B[:,0,:nx]=P@S;B[:,1,nx:2*nx]=P@S;B[:,2,2*nx:]=P@Q;flat=B.reshape(3*N,m);x=a['positions_A'];pat,name=case.split('_',1);params=root/'lammps-runtime/lammps/share/lammps/potentials';plugin=root/'graphite-width/plugin/kcz_width2.so';data=root/'graphite-target-replay/selected'/pat/name/'struct.inp.data';l=lammps(cmdargs=['-screen','none','-log',str(out/'probe.log')])
try:
 for cmd in [f'plugin load {plugin}','units metal','boundary p p p','atom_style full','box tilt large',f'read_data {data}','pair_style hybrid/overlay rebo rebo kolmogorov/crespi/z/smooth 24',f'pair_coeff * * rebo 1 {params}/CH.rebo C NULL',f'pair_coeff * * rebo 2 {params}/CH.rebo NULL C',f'pair_coeff 1 2 kolmogorov/crespi/z/smooth {params}/CC.KC C C','neighbor 3.0 nsq','neigh_modify one 4096']:l.command(cmd)
 def force(xx):
  xx=np.ascontiguousarray(xx);l.scatter_atoms('x',1,3,xx.ctypes.data_as(ctypes.POINTER(ctypes.c_double)));l.command('run 0 pre yes post no');F=np.ctypeslib.as_array(l.gather_atoms('f',1,3),shape=(3*N,)).copy();return flat.T@F
 rows=[];arrays=[]
 for j in columns:
  j=int(j);i=int(np.argmax(abs(diff[:,j])));derivs=[];data_rows=[]
  for step in diag['steps_A']:
   deriv=-(force(x+step*B[:,:,j])-force(x-step*B[:,:,j]))/(2*step);derivs.append(deriv);data_rows.append({'step_A':step,'worst_entry_value':float(deriv[i]),'successive_max_change':None if len(derivs)==1 else float(np.max(np.abs(derivs[-1]-derivs[-2])))})
  arrays.append(derivs);rows.append({'selected_column':j,'selected_row':i,'original_max_column_discrepancy':float(np.max(abs(diff[:,j]))),'ladder':data_rows})
 np.savez_compressed(out/'PROBE_COLUMNS.npz',columns=np.array(columns),steps=np.array(diag['steps_A']),derivatives=np.array(arrays));result={'case':case,'purpose':'post-primary selected-column diagnostic only','records':rows,'full_hessian_qualified_by_probe':False,'physical_promotion':0};(out/'PROBE.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
finally:l.close()
