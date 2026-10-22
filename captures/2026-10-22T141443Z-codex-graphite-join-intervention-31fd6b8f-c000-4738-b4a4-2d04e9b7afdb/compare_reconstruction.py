"""Exploratory comparison against the published PR #381 projected force samples."""
from pathlib import Path
import ctypes, json, sys
import numpy as np
from lammps import lammps

R=Path(__file__).resolve().parent
case=sys.argv[1]
a=np.load(R/f'{case}_candidate.npz')
x=a['positions_A']; B=a['B_extended']; flat=B.reshape(-1,81)
arch=np.load(R/'ud-sync/graphite-analysis'/f'{case}_projected.npz')
assert list(arch['modes'])==['total','rebo','rebo1','rebo2','kc']
assert arch['point_keys'][0]=='0'
probe=34 if case=='21_dir_0' else 30
disp=B[:,:,probe]
mode=sys.argv[2] if len(sys.argv)>2 else 'rebo1'
pattern,name=case.split('_',1)
params=R/'lammps-runtime/lammps/share/lammps/potentials'
data=R/'graphite-target-replay/selected'/pattern/name/'struct.inp.data'
plugin=R/'graphite-width/plugin/kcz_width2.so'
cmds=['units metal','boundary p p p','atom_style full','box tilt large',f'read_data {data}']
if mode in ('total','kc'):cmds.insert(0,f'plugin load {plugin}')
if mode=='total':cmds += ['pair_style hybrid/overlay rebo rebo kolmogorov/crespi/z/smooth 24',f'pair_coeff * * rebo 1 {params}/CH.rebo C NULL',f'pair_coeff * * rebo 2 {params}/CH.rebo NULL C',f'pair_coeff 1 2 kolmogorov/crespi/z/smooth {params}/CC.KC C C']
elif mode=='rebo1':cmds += ['pair_style hybrid/overlay rebo',f'pair_coeff * * rebo {params}/CH.rebo C NULL','pair_coeff 1 2 none','pair_coeff 2 2 none']
elif mode=='kc':cmds += ['pair_style hybrid/overlay kolmogorov/crespi/z/smooth 24','pair_coeff 1 1 none','pair_coeff 2 2 none',f'pair_coeff 1 2 kolmogorov/crespi/z/smooth {params}/CC.KC C C']
else:raise ValueError(mode)
cmds += ['neighbor 3.0 nsq','neigh_modify one 4096']
l=lammps(cmdargs=['-screen','none','-log',str(R/f'{case}_{mode}_comparison.log')])
try:
 for c in cmds:l.command(c)
 i=list(arch['modes']).index(mode);rows=[]
 for key,ref in zip(arch['point_keys'],arch['projected_forces'][i]):
  hh=float(key) if key!='0' else 0.
  xx=np.asarray(x.astype(np.longdouble)+np.longdouble(hh)*disp.astype(np.longdouble),dtype=np.float64)
  xx=np.ascontiguousarray(xx)
  l.scatter_atoms('x',1,3,xx.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
  l.command('run 0 pre yes post no')
  f=flat.T@np.ctypeslib.as_array(l.gather_atoms('f',1,3),shape=(3*len(x),)).copy()
  d=f-ref
  rows.append(dict(key=str(key),candidate_norm=float(np.linalg.norm(f)),archive_norm=float(np.linalg.norm(ref)),max_abs=float(np.max(abs(d))),rms=float(np.sqrt(np.mean(d*d))),fixed_component_delta=float(d[8 if probe==34 else 4])))
 result={'case':case,'mode':mode,'rows':rows}
 print(json.dumps(result,indent=2),flush=True)
 (R/f'{case}_{mode}_comparison.json').write_text(json.dumps(result,indent=2)+'\n')
finally:l.close()
