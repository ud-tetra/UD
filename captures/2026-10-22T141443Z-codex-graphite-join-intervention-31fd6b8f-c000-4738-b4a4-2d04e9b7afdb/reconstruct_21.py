"""Independent exploratory reconstruction of the two held 21 geometries.
The original released arrays are not available; compare force fingerprints before use.
"""
from pathlib import Path
import ctypes,hashlib,json,sys,time
import numpy as np
from scipy.optimize import minimize,root
from lammps import lammps
R=Path(__file__).resolve().parent
CASE=sys.argv[1]
expected={'21_dir_0':'ccc1728bea36a89dedc98f7012847336ccae385df1d4f7be50935be55fc0300a','21_dir_10024':'d02f1cb7cc8325d35efb2ecdddcfac1ca2e84d90d3b27e47f209abad42029603'}
assert CASE in expected
name=CASE.split('_',1)[1]
data=R/'graphite-target-replay/selected/21'/name/'struct.inp.data'
assert hashlib.sha256(data.read_bytes()).hexdigest()==expected[CASE]
params=R/'lammps-runtime/lammps/share/lammps/potentials';plugin=R/'graphite-width/plugin/kcz_width2.so'
l=lammps(cmdargs=['-screen','none','-log',str(R/f'{CASE}_reconstruct.log')]);t0=time.time()
try:
 cmds=[f'plugin load {plugin}','units metal','boundary p p p','atom_style full','box tilt large',f'read_data {data}','pair_style hybrid/overlay rebo rebo kolmogorov/crespi/z/smooth 24',f'pair_coeff * * rebo 1 {params}/CH.rebo C NULL',f'pair_coeff * * rebo 2 {params}/CH.rebo NULL C',f'pair_coeff 1 2 kolmogorov/crespi/z/smooth {params}/CC.KC C C','neighbor 3.0 nsq','neigh_modify one 4096','fix z all lineforce 0.0 0.0 1.0','min_style cg','min_modify dmax 0.005','minimize 1.0e-15 1.0e-15 30000 30000']
 for c in cmds:l.command(c)
 l.command('unfix z')
 n=int(l.get_natoms());typ=np.ctypeslib.as_array(l.gather_atoms('type',0,1),shape=(n,)).copy()
 x0=np.ctypeslib.as_array(l.gather_atoms('x',1,3),shape=(3*n,)).copy().reshape(n,3)
 lines=data.read_text().splitlines();lx=float(next(x for x in lines if 'xlo xhi' in x).split()[1]);ly=float(next(x for x in lines if 'ylo yhi' in x).split()[1]);xy=float(next(x for x in lines if 'xy xz yz' in x).split()[0])
 ay=x0[:,1]/ly;ax=(x0[:,0]-xy*ay)/lx;frac=np.stack([np.mod(ax*6,1),np.mod(ay*6,1)],axis=1);frac[np.isclose(frac,1,atol=1e-8)]=0
 keys=[(int(typ[i]),round(float(frac[i,0]),7),round(float(frac[i,1]),7)) for i in range(n)];unique=sorted(set(keys));assert len(unique)==28,len(unique)
 idx={k:i for i,k in enumerate(unique)};group=np.array([idx[k] for k in keys]);count=np.bincount(group);assert np.all(count==36)
 P=np.zeros((n,28));P[np.arange(n),group]=1/6
 def helmert(d):
  Q=np.zeros((d,d-1))
  for j in range(d-1):Q[:j+1,j]=1/np.sqrt((j+1)*(j+2));Q[j+1,j]=-(j+1)/np.sqrt((j+1)*(j+2))
  return Q
 S=np.zeros((28,26));S[:14,:13]=helmert(14);S[14:,13:]=helmert(14);Q=helmert(28)
 B=np.zeros((n,3,81));B[:,0,:26]=P@S;B[:,1,26:52]=P@S;B[:,2,52:79]=P@Q
 sign=np.where(typ==2,1.,-1.);B[:,0,79]=sign/np.sqrt(n);B[:,1,80]=sign/np.sqrt(n)
 flat=B.reshape(3*n,81);assert np.max(abs(flat.T@flat-np.eye(81)))<1e-12
 def eval(q):
  x=np.ascontiguousarray(x0+np.einsum('nam,m->na',B,q))
  l.scatter_atoms('x',1,3,x.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
  l.command('run 0 pre yes post no')
  F=np.ctypeslib.as_array(l.gather_atoms('f',1,3),shape=(3*n,)).copy()
  return float(l.get_thermo('pe')),flat.T@F,x,F
 E0,g0,_,_=eval(np.zeros(81));k=0
 def fun(q):
  global k
  k+=1;E,g,_,_=eval(q)
  if k%30==0:print(json.dumps({'case':CASE,'eval':k,'delta_E':E-E0,'max_g':float(np.max(abs(g))),'slide':(2*q[-2:]/np.sqrt(n)).tolist(),'s':time.time()-t0}),flush=True)
  return E-E0,-g
 seed=np.zeros(81);seed[-2]=.05*np.sqrt(n)/2
 opt=minimize(fun,seed,jac=True,method='L-BFGS-B',options={'gtol':1e-10,'ftol':0.,'maxiter':2000,'maxls':50})
 q=opt.x;E,g,x,F=eval(q)
 if np.max(abs(g))>1e-7:
  rr=root(lambda qq:-eval(qq)[1],q,method='hybr',options={'xtol':1e-9,'eps':1e-10,'maxfev':2000})
  E2,g2,x2,F2=eval(rr.x)
  if np.max(abs(g2))<np.max(abs(g)):q=rr.x;E,g,x,F=E2,g2,x2,F2
 np.savez_compressed(R/f'{CASE}_candidate.npz',positions_A=x,initial_positions_A=x0,B_extended=B,q=q,projected_force=g,forces=F.reshape(n,3),group_index=group,atom_types=typ)
 out={'case':CASE,'initial_energy_eV':E0,'energy_eV':E,'max_projected_force_eV_per_A':float(np.max(abs(g))),'relative_slide_A':(2*q[-2:]/np.sqrt(n)).tolist(),'optimizer':str(opt.message),'evaluations':k,'seconds':time.time()-t0}
 (R/f'{CASE}_candidate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
finally:l.close()
