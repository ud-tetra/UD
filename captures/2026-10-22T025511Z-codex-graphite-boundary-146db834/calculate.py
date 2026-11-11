from pathlib import Path
import numpy as np,json,ctypes,sys,hashlib,time
from lammps import lammps
from common import ROOT,load,positions
p=Path(__file__).resolve().parent;f=json.loads((p/'FREEZE.json').read_text());case=sys.argv[1];out=p/case;plan=np.load(out/'PLAN.npz');a,B,nei,b=load(case);x=a['positions_A'];N=len(x);m=B.shape[2];flat=B.reshape(3*N,m);vectors=plan['vectors'];n=len(vectors)
assert next(r for r in json.loads((p/'FEASIBILITY.json').read_text())['cases'] if r['case']==case)['preflight_pass']
for fn,sha in f['inputs'].items():assert hashlib.sha256((ROOT/fn).read_bytes()).hexdigest()==sha
for register in ['CODE_FREEZE.json','PRECHECK_SEAL.json']:
 for fn,sha in json.loads((p/register).read_text())['files'].items():assert hashlib.sha256((p/fn).read_bytes()).hexdigest()==sha
pat,name=case.split('_',1);params=ROOT/'lammps-runtime/lammps/share/lammps/potentials';plugin=ROOT/'graphite-width/plugin/kcz_width2.so';data=ROOT/'graphite-target-replay/selected'/pat/name/'struct.inp.data';l=lammps(cmdargs=['-screen','none','-log',str(out/('lammps_'+sys.argv[2]+'.log'))]);start=time.time()
try:
 for cmd in [f'plugin load {plugin}','units metal','boundary p p p','atom_style full','box tilt large',f'read_data {data}','pair_style hybrid/overlay rebo rebo kolmogorov/crespi/z/smooth 24',f'pair_coeff * * rebo 1 {params}/CH.rebo C NULL',f'pair_coeff * * rebo 2 {params}/CH.rebo NULL C',f'pair_coeff 1 2 kolmogorov/crespi/z/smooth {params}/CC.KC C C','neighbor 3.0 nsq','neigh_modify one 4096']:l.command(cmd)
 def force(xx):
  xx=np.ascontiguousarray(xx);l.scatter_atoms('x',1,3,xx.ctypes.data_as(ctypes.POINTER(ctypes.c_double)));l.command('run 0 pre yes post no');F=np.ctypeslib.as_array(l.gather_atoms('f',1,3),shape=(3*N,)).copy();return flat.T@F
 base=[force(x)];indices=np.array_split(np.arange(n),2)[int(sys.argv[2])];raw=np.empty((len(indices),4,2,m));repeat=np.empty((len(indices),2,2,m))
 for jj,j in enumerate(indices):
  disp=np.einsum('nam,m->na',B,vectors[j])
  for k,h in enumerate(plan['radii_A']):
   raw[jj,k,0]=force(positions(x,disp,h));raw[jj,k,1]=force(positions(x,disp,-h))
  for kk,k in enumerate([2,1]):
   h=plan['radii_A'][k];repeat[jj,kk,1]=force(positions(x,disp,-h));repeat[jj,kk,0]=force(positions(x,disp,h))
  if (jj+1)%10==0:
   base.append(force(x));print(str(jj+1)+'/'+str(len(indices)),flush=True)
 base.append(force(x));np.savez_compressed(out/('RAW_'+sys.argv[2]+'.npz'),indices=indices,positive_negative_forces=raw,repeat_middle_samples=repeat,baseline_forces=base);print('COMPLETE '+case+' shard'+sys.argv[2],flush=True)

finally:l.close()
