"""Counterfactual REBO gC polynomial continuation across cos(theta)=-1/2.

Changes only the gC spline's adjacent interval polynomial in a copied CH.rebo.
Never use this potential as a replacement for the archived original model.
"""
from pathlib import Path
import ctypes,json,sys,hashlib
import numpy as np
from lammps import lammps
R=Path(__file__).resolve().parent;case=sys.argv[1];continuation=sys.argv[2]
assert continuation in ('right','left')
original=R/'lammps-runtime/lammps/share/lammps/potentials/CH.rebo';lines=original.read_text().splitlines(keepends=True)
start=next(i for i,v in enumerate(lines) if '# gC1 and gC2' in v)
indices=[]
for i in range(start+2,len(lines)):
 if '# gH' in lines[i]:break
 if lines[i].strip() and not lines[i].lstrip().startswith('#'):indices.append(i)
assert len(indices)==1+5+4*6*2,len(indices)
coef=indices[6:]
for block in (0,1):
 src=2 if continuation=='right' else 1;dst=1 if continuation=='right' else 2
 for j in range(6):lines[coef[block*24+dst*6+j]]=lines[coef[block*24+src*6+j]]
modified=R/f'CH_join_{continuation}.rebo';modified.write_text(''.join(lines))
a=np.load(R/f'{case}_candidate.npz');x=a['positions_A'];B=a['B_extended'];flat=B.reshape(-1,81);probe,comp=(34,8) if case=='21_dir_0' else (30,4);direction=B[:,:,probe]
pat,name=case.split('_',1);data=R/'graphite-target-replay/selected'/pat/name/'struct.inp.data'
l=lammps(cmdargs=['-screen','none','-log',str(R/f'{case}_{continuation}_counterfactual.log')]);out=[]
try:
 for cmd in ('units metal','boundary p p p','atom_style full','box tilt large',f'read_data {data}','pair_style hybrid/overlay rebo',f'pair_coeff * * rebo {modified} C NULL','pair_coeff 1 2 none','pair_coeff 2 2 none','neighbor 3.0 nsq','neigh_modify one 4096'):l.command(cmd)
 def sample(t):
  xx=np.ascontiguousarray(np.asarray(x.astype(np.longdouble)+np.longdouble(t)*direction.astype(np.longdouble),dtype=np.float64))
  l.scatter_atoms('x',1,3,xx.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
  l.command('run 0 pre yes post no')
  return flat.T@np.ctypeslib.as_array(l.gather_atoms('f',1,3),shape=(3*len(x),)).copy()
 f0=sample(0)
 for h in (8e-5,4e-5,2e-5,1e-5,5e-6,2.5e-6,1.25e-6):
  fp=sample(h);f2p=sample(2*h);fm=sample(-h);f2m=sample(-2*h)
  qp=-(-3*f0+4*fp-f2p)/(2*h);qm=-(3*f0-4*fm+f2m)/(2*h)
  out.append(dict(h_A=h,side_fixed_eV_per_A2=float((qp-qm)[comp]),side_max_eV_per_A2=float(np.max(abs(qp-qm))),avg_fixed_eV_per_A2=float((qp[comp]+qm[comp])/2)))
finally:l.close()
result={'case':case,'continuation':continuation,'original_sha256':hashlib.sha256(original.read_bytes()).hexdigest(),'modified_sha256':hashlib.sha256(modified.read_bytes()).hexdigest(),'baseline_projected_norm_eV_per_A':float(np.linalg.norm(f0)),'rows':out}
print(json.dumps(result,indent=2),flush=True);(R/f'{case}_{continuation}_counterfactual.json').write_text(json.dumps(result,indent=2)+'\n')
