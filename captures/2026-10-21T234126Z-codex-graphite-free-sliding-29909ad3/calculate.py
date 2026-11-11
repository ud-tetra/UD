from pathlib import Path
import numpy as np,json,ctypes,sys,hashlib,time
from lammps import lammps
from common import ROOT,load,positions
p=Path(__file__).resolve().parent;f=json.loads((p/'FREEZE.json').read_text());case=sys.argv[1];out=p/case;plan=np.load(out/'PLAN.npz');a,B,nei,b=load(case);x=a['positions_A'];N=len(x);m=B.shape[2];flat=B.reshape(3*N,m);vectors=plan['vectors'];steps=plan['steps_A'];n=len(vectors)
assert json.loads((p/'FEASIBILITY.json').read_text())['all_pass']
for fn,sha in f['inputs'].items():assert hashlib.sha256((ROOT/fn).read_bytes()).hexdigest()==sha
for register in ['CODE_FREEZE.json','PRECHECK_SEAL.json']:
 for fn,sha in json.loads((p/register).read_text())['files'].items():assert hashlib.sha256((p/fn).read_bytes()).hexdigest()==sha
pat,name=case.split('_',1);params=ROOT/'lammps-runtime/lammps/share/lammps/potentials';plugin=ROOT/'graphite-width/plugin/kcz_width2.so';data=ROOT/'graphite-target-replay/selected'/pat/name/'struct.inp.data';l=lammps(cmdargs=['-screen','none','-log',str(out/'lammps.log')]);start=time.time()
try:
 for cmd in [f'plugin load {plugin}','units metal','boundary p p p','atom_style full','box tilt large',f'read_data {data}','pair_style hybrid/overlay rebo rebo kolmogorov/crespi/z/smooth 24',f'pair_coeff * * rebo 1 {params}/CH.rebo C NULL',f'pair_coeff * * rebo 2 {params}/CH.rebo NULL C',f'pair_coeff 1 2 kolmogorov/crespi/z/smooth {params}/CC.KC C C','neighbor 3.0 nsq','neigh_modify one 4096']:l.command(cmd)
 def force(xx):
  xx=np.ascontiguousarray(xx);l.scatter_atoms('x',1,3,xx.ctypes.data_as(ctypes.POINTER(ctypes.c_double)));l.command('run 0 pre yes post no');F=np.ctypeslib.as_array(l.gather_atoms('f',1,3),shape=(3*N,)).copy();return flat.T@F
 base=[force(x)];raw=np.empty((n,3,2,m));derivs=np.empty((n,3,m));repeat=np.empty((n,2,m))
 for j,w in enumerate(vectors):
  disp=np.einsum('nam,m->na',B,w)
  for k,h in enumerate(steps[j]):
   gp=force(positions(x,disp,h));gm=force(positions(x,disp,-h));raw[j,k,0]=gp;raw[j,k,1]=gm;derivs[j,k]=-(gp-gm)/(2*h)
  h=steps[j,1];repeat[j,1]=force(positions(x,disp,-h));repeat[j,0]=force(positions(x,disp,h))
  if (j+1)%20==0:
   base.append(force(x));(out/'PROGRESS.json').write_text(json.dumps({'completed_probes':j+1,'total_probes':n,'seconds':time.time()-start})+'\n');print(str(j+1)+'/'+str(n),flush=True)
 base.append(force(x));np.savez_compressed(out/'RAW.npz',positive_negative_forces=raw,derivatives=derivs,repeat_middle_positive_negative_forces=repeat,baseline_forces=base);(out/'TIMING.json').write_text(json.dumps({'seconds':time.time()-start,'probes':n})+'\n');print('COMPLETE '+case,flush=True)
finally:l.close()
