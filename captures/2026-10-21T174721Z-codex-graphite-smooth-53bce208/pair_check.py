from pathlib import Path
import json,ctypes,numpy as np,hashlib
from lammps import lammps
p=Path(__file__).parent;params=p.parent/'lammps-runtime/lammps/share/lammps/potentials';rows=[]
def exact(r,c):
 rad=np.linalg.norm(r);t=(rad-(c-2))/2
 if t<=0:s,ds=1.,0.
 elif t>=1:s,ds=0.,0.
 else:s,ds=1-10*t**3+15*t**4-6*t**5,-15*t*t*(1-t)**2
 rho=(r[0]**2+r[1]**2)/.578**2;e=np.exp(-3.629*(rad-3.34));er=np.exp(-rho);pol=.01571+.01229*rho+.004933*rho*rho;C=.003030+2*er*pol;U=-.010238*(3.34/rad)**6+e*C
 fr=-6*.010238*3.34**6/rad**8+3.629*e/rad*C;fa=e*er*(4*pol-2*(2*.01229+4*.004933*rho))/.578**2
 F=r*fr;F[:2]+=r[:2]*fa
 return s*U,s*F-U*ds*r/rad
for cut in [16,20,24]:
 l=lammps(cmdargs=['-screen','none','-log',str(p/f'pair_check_{cut}.log')])
 for cmd in [f'plugin load {p.resolve()}/plugin/kcz_smooth.so','units metal','atom_style full','boundary p p p','region box block 0 100 0 100 0 100','create_box 2 box','create_atoms 1 single 30 30 30','create_atoms 2 single 35 30 33.4','mass * 12.011',f'pair_style hybrid/overlay rebo rebo kolmogorov/crespi/z/smooth {cut}',f'pair_coeff * * rebo 1 {params}/CH.rebo C NULL',f'pair_coeff * * rebo 2 {params}/CH.rebo NULL C',f'pair_coeff 1 2 kolmogorov/crespi/z/smooth {params}/CC.KC C C']:l.command(cmd)
 for rad in [3.5,cut-2-1e-4,cut-2,cut-2+1e-4,cut-1,cut-1e-4,cut,cut+1e-4]:
  z=3.4;lat=np.sqrt(rad*rad-z*z);r=np.array([.8*lat,.6*lat,z]);x=np.stack([np.ones(3)*30,np.ones(3)*30+r]);x=np.ascontiguousarray(x)
  l.scatter_atoms('x',1,3,x.ctypes.data_as(ctypes.POINTER(ctypes.c_double)));l.command('run 0 pre yes post no');E=l.get_thermo('pe');F=np.ctypeslib.as_array(l.gather_atoms('f',1,3),shape=(6,)).copy().reshape(2,3)[1];ep,fp=exact(r,cut)
  h=1e-5;fd=np.array([-(exact(r+np.eye(3)[j]*h,cut)[0]-exact(r-np.eye(3)[j]*h,cut)[0])/(2*h) for j in range(3)])
  row={'cutoff_A':cut,'r_A':rad,'energy_abs_error':abs(E-ep),'force_max_abs_error':float(abs(F-fp).max()),'energy_force_FD_max_abs_error':float(abs(fd-fp).max())};row['passes']=row['energy_abs_error']<=1e-12 and row['force_max_abs_error']<=1e-12 and row['energy_force_FD_max_abs_error']<=1e-8;rows.append(row)
 l.close()
res={'status':'PASS' if all(r['passes'] for r in rows) else 'FAIL','checks':rows,'source_sha256':hashlib.sha256((p/'plugin/pair_kcz_smooth.cpp').read_bytes()).hexdigest(),'binary_sha256':hashlib.sha256((p/'plugin/kcz_smooth.so').read_bytes()).hexdigest(),'runtime_version':20250722,'physical_promotion':0,'scope':'Isolated-pair energies and all force components against analytic expressions and finite energy derivatives, including switch boundaries'}
(p/'PAIR_CHECK.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2));assert res['status']=='PASS'
