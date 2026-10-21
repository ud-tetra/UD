from pathlib import Path
import numpy as np,json,ctypes
from lammps import lammps
root=Path(__file__).parent;params=root.parent/'lammps-runtime/lammps/share/lammps/potentials';rows=[]
for cut in [16,20,24]:
 l=lammps(cmdargs=['-screen','none','-log',str(root/f'pair_runtime_{cut}.log')])
 for cmd in ['units metal','atom_style full','boundary p p p','region box block 0 100 0 100 0 100','create_box 2 box','create_atoms 1 single 30 30 30','create_atoms 2 single 35 30 33.4','mass * 12.011',f'pair_style hybrid/overlay rebo rebo kolmogorov/crespi/z {cut}',f'pair_coeff * * rebo 1 {params}/CH.rebo C NULL',f'pair_coeff * * rebo 2 {params}/CH.rebo NULL C',f'pair_coeff 1 2 kolmogorov/crespi/z {params}/CC.KC C C'] : l.command(cmd)
 for rad in [3.5,cut-1e-4,cut+1e-4]:
  z=3.4;r=np.array([np.sqrt(rad**2-z*z),0,z]);x=np.array([[30.,30,30],[30+r[0],30,30+z]])
  l.scatter_atoms('x',1,3,x.ctypes.data_as(ctypes.POINTER(ctypes.c_double)));l.command('run 0 pre yes post no');E=float(l.get_thermo('pe'));f=np.ctypeslib.as_array(l.gather_atoms('f',1,3),shape=(6,)).copy().reshape(2,3)[1,2]
  rs=r@r;rho=(r[:2]@r[:2])/.578**2;ex=np.exp(-3.629*(rad-3.34));C=.003030+2*np.exp(-rho)*(.01571+.01229*rho+.004933*rho*rho)
  ep=(-.010238*(3.34/rad)**6+ex*C+.010238*(3.34/cut)**6)*(rs<cut*cut);fp=z*(-6*.010238*3.34**6/rad**8+3.629*ex/rad*C)*(rs<cut*cut)
  rows.append({'cutoff_A':cut,'r_A':rad,'runtime_energy_eV':E,'pair_energy_eV':ep,'runtime_Fz_eV_per_A':f,'pair_Fz_eV_per_A':fp,'passes':bool(abs(E-ep)<1e-12 and abs(f-fp)<1e-12)})
 l.close()
res={'runtime_version':20250722,'checks':rows,'all_pass':all(r['passes'] for r in rows),'scope':'Nine isolated unlike-type pairs, near-contact and both cutoff sides; numerical runtime/source-formula bridge, not historical source byte identity'}
(root/'RUNTIME_CHECK.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
