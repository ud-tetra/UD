#!/usr/bin/env python3
"""Reconstruct flat-layer KC height derivatives for the index-seven graphite interface.

Usage: python3 derive_kc_load_proxy.py /path/to/svnpzbjc3t-v1.zip
Parameters/equation: Minkin et al. arXiv:2308.06302 source SI Table S1 and Eq S1.
Numeric raw-grid validation: Mendeley Data DOI 10.17632/svnpzbjc3t.1.
This is a new finite rigid-pair sum with a spherical cutoff, not the source's
exact simulation implementation or an experimental friction calculation.
"""
import hashlib,io,json,math,sys,zipfile
import numpy as np
SHA='b1ccf62a3e75928e1382cbdd6c669b99675fef9ad5f077e79057a142a0a07875'
with open(sys.argv[1],'rb') as h:assert hashlib.file_digest(h,'sha256').hexdigest()==SHA
bond=1.42;a=math.sqrt(3)*bond
basis=np.array([[a,a/2],[0,a*math.sqrt(3)/2]])
R=np.array([[8,3],[-3,5]])/7
L=np.array([[2,-1],[1,3]]);invL=np.linalg.inv(L)
shift=np.array([1/3,1/3]);bottom=[];top=[]
for p in range(-18,19):
 for q in range(-18,19):
  n=np.array([p,q]);local=invL@R@n
  for s in (np.zeros(2),shift):
   bottom.append(basis@(n+s))
   if np.all(local>=-1e-9) and np.all(local<1-1e-9):top.append(basis@R@(n+s))
bottom=np.array(bottom);top=np.array(top)
assert len(top)==14
with zipfile.ZipFile(sys.argv[1]) as archive:
 def read(q):
  name=next(n for n in archive.namelist() if '/data/pes21_' in n and n.endswith('/'+q+'.txt'))
  return np.loadtxt(io.BytesIO(archive.read(name)))
 grids={q:read(q) for q in 'XYZ'}
X,Y,Z=(grids[q][::8,::8].ravel() for q in 'XYZ')
phi=math.atan(math.sqrt(3)/5)
physical=np.column_stack([math.cos(phi)*X-math.sin(phi)*Y,math.sin(phi)*X+math.cos(phi)*Y])
# Table S1: all energies meV, lengths Angstrom.
A0,z0,C,C0,C2,C4,delta,lam=10.238,3.34,3.030,15.71,12.29,4.933,0.578,3.629
rho2=[]
for x in physical:
 d=top[:,None,:]+x-bottom[None,:,:]
 rho2.append(np.sum(d*d,axis=-1))

def energy_derivatives(height,cutoff):
 out=[]
 for rr in rho2:
  rr3=rr+height**2;mask=rr3<cutoff**2;r=np.sqrt(rr3[mask]);q=rr[mask]/delta**2
  dispersion=A0*(z0/r)**6
  rep=(C+2*np.exp(-q)*(C0+C2*q+C4*q*q))*np.exp(-lam*(r-z0))
  E=(-dispersion+rep).sum()/len(top)
  Ez=(6*dispersion*height/r**2-lam*rep*height/r).sum()/len(top)
  Ezz=(6*dispersion*(1/r**2-8*height*height/r**4)+
       rep*(lam**2*height*height/r**2-lam*rr[mask]/r**3)).sum()/len(top)
  out.append((E,Ez,Ezz))
 return np.array(out)
# Analytic pairwise z derivatives versus fixed-neighbor finite differences.
rhotest=rho2[0];height=3.46;rc=16;mask=(rhotest+height**2)<rc**2
r=np.sqrt(rhotest[mask]+height**2);q=rhotest[mask]/delta**2
D=A0*(z0/r)**6;H=(C+2*np.exp(-q)*(C0+C2*q+C4*q*q))*np.exp(-lam*(r-z0))
analytic1=(6*D*height/r**2-lam*H*height/r).sum()/len(top)
analytic2=(6*D*(1/r**2-8*height**2/r**4)+H*(lam**2*height**2/r**2-lam*rhotest[mask]/r**3)).sum()/len(top)
def fixed_energy(z):
 r=np.sqrt(rhotest[mask]+z*z)
 return np.sum(-A0*(z0/r)**6+(C+2*np.exp(-q)*(C0+C2*q+C4*q*q))*np.exp(-lam*(r-z0)))/len(top)
h=1e-4
assert abs((fixed_energy(height+h)-fixed_energy(height-h))/(2*h)-analytic1)<2e-6
assert abs((fixed_energy(height+h)-2*fixed_energy(height)+fixed_energy(height-h))/h**2-analytic2)<5e-5
# Regress each of E, dE/dz and d2E/dz2 on the same index-seven Fourier basis.
g=math.sqrt(7)*4*math.pi/(math.sqrt(3)*a)
G=np.array([[g*math.cos(math.pi/6+j*2*math.pi/3),g*math.sin(math.pi/6+j*2*math.pi/3)] for j in range(3)])
points=np.column_stack([X,Y]);phase=points@G.T
F=np.column_stack([np.ones(len(X))]+[f(phase[:,j]) for j in range(3) for f in (np.cos,np.sin)])
reference=np.linalg.lstsq(F,Z,rcond=None)[0]
refamp=np.array([math.hypot(reference[1+2*j],reference[2+2*j]) for j in range(3)])
area_atom=math.sqrt(3)*a*a/4
pressure_unit=160217.6634 # MPa per eV / Angstrom^3
results=[]
for rc in (14,16,18):
 vals=energy_derivatives(3.46,rc)
 u,up,upp=(np.linalg.lstsq(F,vals[:,k],rcond=None)[0] for k in (0,1,2))
 amp=np.array([math.hypot(u[1+2*j],u[2+2*j]) for j in range(3)])
 alpha=np.array([(u[1+2*j]*up[1+2*j]+u[2+2*j]*up[2+2*j])/amp[j]**2 for j in range(3)])
 Asecond=np.array([(u[1+2*j]*upp[1+2*j]+u[2+2*j]*upp[2+2*j])/amp[j] for j in range(3)])
 # Negative-U1 minimum has S=3; project the amplitude second derivative.
 kz=upp[0]-sum(Asecond) # meV / Angstrom^2 / atom
 load_slope=-area_atom/(pressure_unit*(kz/1000))*np.mean(alpha)
 compare=vals[:,0]-Z;shape_rms=1000*np.std(compare)
 results.append({'cutoff_A':rc,'U1_amplitude_microeV_per_atom':[float(v*1000) for v in amp],
  'log_amplitude_height_derivative_inv_A':[float(v) for v in alpha],
  'normal_curvature_at_first_shell_min_meV_per_A2_per_atom':float(kz),
  'mean_normal_energy_curvature_meV_per_A2_per_atom':float(upp[0]),
  'mean_normal_energy_first_derivative_meV_per_A_per_atom':float(up[0]),
  'predicted_log_stiffness_pressure_slope_per_MPa':float(load_slope),
  'first_shell_leading_sliding_barrier_pressure_slope_microeV_per_atom_per_MPa':float(4*np.mean(amp)*1000*load_slope),
  'first_shell_leading_saddle_min_height_gap_A':float(4*np.mean(amp)*abs(float(np.mean(alpha)))/kz),
  'raw_grid_centered_shape_rms_difference_microeV_per_atom':float(shape_rms),
  'raw_grid_mean_energy_offset_meV_per_atom':float(np.mean(compare)),
  'raw_grid_spatial_correlation':float(np.corrcoef(vals[:,0],Z)[0,1])})
assert min(r['normal_curvature_at_first_shell_min_meV_per_A2_per_atom'] for r in results)>0
assert all(0.00043<r['predicted_log_stiffness_pressure_slope_per_MPa']<0.00047 for r in results)
assert results[1]['raw_grid_spatial_correlation']>.999
print(json.dumps({'status':'NUMERICAL_KC_RECONSTRUCTION_CONDITIONAL_LOAD_PROXY',
 'source':'Minkin et al. arXiv:2308.06302 source SI Eq. S1 and Table S1; public PES DOI 10.17632/svnpzbjc3t.1',
 'source_tar_sha256':'adea7468f311c648a0d25abf4f5eecacd8eebe1b6fc7761ffcea7d073b2f460b',
 'PES_archive_sha256':SHA,'sample_grid':list(grids['Z'][::8,::8].shape),
 'reference_first_shell_amplitude_microeV_per_atom':[float(v*1000) for v in refamp],
 'geometry':'Rigid planar layers, 14 top atoms in index-seven coincidence cell, periodic bottom patch, spherical distance cutoff, no lateral/bath relaxation',
 'pressure_conversion':'1 eV/Angstrom^3 = 160217.6634 MPa, pressure force per carbon atom = P*sqrt(3)*a^2/4',
 'cutoff_sensitivity':results,
 'scope':'Local first-shell equilibrium stiffness and leading weak-corrugation barrier pressure proxy; not a kinetic-friction/load prediction. Full source implementation not exactly reproduced.',
 'physical_promotion':0},indent=2))
