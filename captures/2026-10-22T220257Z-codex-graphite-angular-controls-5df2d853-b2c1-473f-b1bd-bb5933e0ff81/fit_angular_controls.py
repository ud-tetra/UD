#!/usr/bin/env python3
"""Fit fixed-height conventional (2,1),(3,1),(3,2),(5,1) PES controls.

Usage: python3 fit_angular_controls.py /path/to/svnpzbjc3t-v1.zip
Reads only numeric X/Y/Z text files from the public archive; no embedded code.
"""
import hashlib,io,json,math,sys,zipfile
import numpy as np
SHA='b1ccf62a3e75928e1382cbdd6c669b99675fef9ad5f077e79057a142a0a07875'
with open(sys.argv[1],'rb') as h:assert hashlib.file_digest(h,'sha256').hexdigest()==SHA
source={
 'pes21':{'pair':[2,1],'N':7,'angle_deg':21.787,'reported_U1_microeV_per_atom':-20.2,'reported_shear_Pa':1.67e7,'paper_cell':'18x18'},
 'pes31':{'pair':[3,1],'N':13,'angle_deg':32.204,'reported_U1_microeV_per_atom':4.66,'reported_shear_Pa':1.12e6,'paper_cell':'18x18'},
 'pes32':{'pair':[3,2],'N':19,'angle_deg':13.174,'reported_U1_microeV_per_atom':0.434,'reported_shear_Pa':1.26e5,'paper_cell':'10x10'},
 'pes51':{'pair':[5,1],'N':31,'angle_deg':42.103,'reported_U1_microeV_per_atom':0.00115,'reported_shear_Pa':425,'paper_cell':'11x11'},
}
a=math.sqrt(3)*1.42 # Angstrom
unit=160217.6634 # MPa per eV/Angstrom^3
out={'status':'NUMERICAL_CONVENTIONAL_FIXED_HEIGHT_CONTROL','doi':'10.17632/svnpzbjc3t.1','archive_sha256':SHA,'height_A':3.46,'results':[],'physical_promotion':0}
with zipfile.ZipFile(sys.argv[1]) as z:
 for tag,entry in source.items():
  folder=next(p.rsplit('/',1)[0] for p in z.namelist() if '/data/'+tag+'_' in p and p.endswith('/Z.txt'))
  def read(q):return np.loadtxt(io.BytesIO(z.read(folder+'/'+q+'.txt')))
  grids={q:read(q) for q in 'XYZ'}
  assert grids['Z'].shape==(128,129)
  X,Y,Z=(grids[q].ravel() for q in 'XYZ')
  g=math.sqrt(entry['N'])*4*math.pi/(math.sqrt(3)*a)
  waves=[g*np.array([math.cos(math.pi/6+j*2*math.pi/3),math.sin(math.pi/6+j*2*math.pi/3)]) for j in range(3)]
  A=np.column_stack([np.ones(Z.size)]+[f(v[0]*X+v[1]*Y) for v in waves for f in (np.cos,np.sin)])
  idx=np.indices(grids['Z'].shape);hold=((idx[0]+3*idx[1])%4==0).ravel()
  coef=np.linalg.lstsq(A[~hold],Z[~hold],rcond=None)[0]
  residual=Z-A@coef
  amps=np.array([math.hypot(coef[2*j+1],coef[2*j+2]) for j in range(3)])*1000 # stored Z meV to microeV
  phases=np.array([math.atan2(-coef[2*j+2],coef[2*j+1]) for j in range(3)])
  closure0=math.remainder(float(sum(phases)),2*math.pi)
  closurePi=math.remainder(float(sum(phases)-math.pi),2*math.pi)
  sign=1 if abs(closure0)<abs(closurePi) else -1
  U=sign*float(np.mean(amps))
  coeff=(16*math.pi/math.sqrt(3) if sign<0 else 6.183)
  tau=coeff*math.sqrt(entry['N'])*abs(U)*1e-6/a**3*unit
  rec={**entry,'archive_folder':folder.split('/')[-1], 'grid_shape':list(grids['Z'].shape),
       'raw_range_microeV_per_atom':float(1000*np.ptp(Z)),
       'fit_U1_microeV_per_atom':U,
       'fit_three_amplitudes_microeV_per_atom':[float(v) for v in amps],
       'phase_closure_error_rad':float(closure0 if sign>0 else closurePi),
       'holdout_rms_microeV_per_atom':float(1000*np.sqrt(np.mean(residual[hold]**2))),
       'model_first_shell_ideal_static_shear_MPa':tau,
       'reported_shear_MPa':entry['reported_shear_Pa']/1e6}
  assert abs(U-entry['reported_U1_microeV_per_atom'])/abs(entry['reported_U1_microeV_per_atom'])<.004
  assert abs(tau-rec['reported_shear_MPa'])/rec['reported_shear_MPa']<.005
  assert abs(rec['phase_closure_error_rad'])<.002
  out['results'].append(rec)
ref=out['results'][0]['model_first_shell_ideal_static_shear_MPa']
for r in out['results']:r['ideal_shear_ratio_to_index7']=r['model_first_shell_ideal_static_shear_MPa']/ref
print(json.dumps(out,indent=2))
