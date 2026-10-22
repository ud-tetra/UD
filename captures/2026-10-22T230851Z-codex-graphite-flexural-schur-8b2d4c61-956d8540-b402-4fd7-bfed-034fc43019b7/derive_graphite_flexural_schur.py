#!/usr/bin/env python3
"""Conditional static flexural Schur response of the index-7 KC reconstruction."""
import contextlib, hashlib, io, json, runpy, sys
from pathlib import Path
import numpy as np
from scipy.linalg import eigh

repo=Path(__file__).resolve().parents[2]
source=repo/'captures/2026-10-22T225658Z-codex-graphite-three-neighbor-kc-46d38a7f-1ef8f60e-1510-42e1-81d1-332643cb9319/derive_three_neighbor_kc_projection.py'
archive=Path(sys.argv[1]);expected='b1ccf62a3e75928e1382cbdd6c669b99675fef9ad5f077e79057a142a0a07875'
with archive.open('rb') as f: assert hashlib.file_digest(f,'sha256').hexdigest()==expected
sys.argv=[str(source),str(archive)]
with contextlib.redirect_stdout(io.StringIO()): obj=runpy.run_path(str(source))
n=14; b=1.42; cutoff=16.;cart=obj['cart0']; top=obj['top'];bottom=obj['bottom'];z0=obj['z0'];A=obj['A'];delta=obj['delta'];lam=obj['lam'];C=obj['C0'];C2=obj['C2'];C4=obj['C4']
L=np.zeros((n,n))
for i,row in enumerate(obj['neighbors']):
 L[i,i]=3
 for j,v in row:L[i,j]-=1
assert np.allclose(L,L.T) and np.max(np.abs(L@np.ones(n)))<1e-12
# As in the v18 source projection, reorder atom heights into C3-aligned carrier labels.
target=[site*7+(k+2)%7 for site,k in ((v//7,v%7) for v in obj['labels'])]
perm=np.argsort(target)
P=np.zeros((n,n))
for v,pv in enumerate(obj['vertex_permutation']):P[pv,v]=1
Aatom=3*np.sqrt(3)*b*b/4
K_plate_per_ev=(1000*Aatom/n)*(4/(3*b*b))**2*(L@L)
K_plate_per_ev=K_plate_per_ev[np.ix_(perm,perm)]
assert np.linalg.norm(P@K_plate_per_ev@P.T-K_plate_per_ev)<1e-9

# This finite-difference energy uses the same hard cutoff and no source code from the archive.
def energy(x,h,normal_rule):
 if normal_rule=='three_neighbor':return obj['direct_energy'](x,h,cutoff)
 total=0.
 for i in range(n):
  s=top[i]+x-bottom
  zz=3.46+h[i]
  r2=np.sum(s*s,axis=1)+zz*zz
  valid=r2<cutoff*cutoff
  r=np.sqrt(r2[valid]);u=np.sum(s[valid]*s[valid],axis=1)/delta**2
  total+=np.sum(-A*(z0/r)**6+np.exp(-lam*(r-z0))*(obj['d']['C']+2*np.exp(-u)*(C+C2*u+C4*u*u)))
 return total/n

def height_derivatives(rule,step):
 unit=np.eye(n)*step;flat=np.zeros(n);e0=energy(cart,flat,rule)
 grad=np.zeros(n);H=np.zeros((n,n))
 for i in range(n):
  eplus=energy(cart,unit[i],rule);eminus=energy(cart,-unit[i],rule)
  grad[i]=(eplus-eminus)/(2*step)
  H[i,i]=(eplus-2*e0+eminus)/step**2
  for j in range(i):
   H[i,j]=(energy(cart,unit[i]+unit[j],rule)-energy(cart,unit[i]-unit[j],rule)-energy(cart,-unit[i]+unit[j],rule)+energy(cart,-unit[i]-unit[j],rule))/(4*step**2)
   H[j,i]=H[i,j]
 return grad[perm],H[np.ix_(perm,perm)]

def lateral_derivatives(step):
 unit=np.eye(2)*step;flat=np.zeros(n);e0=energy(cart,flat,'three_neighbor');H=np.zeros((2,2))
 for i in range(2):
  H[i,i]=(energy(cart+unit[i],flat,'three_neighbor')-2*e0+energy(cart-unit[i],flat,'three_neighbor'))/step**2
  for j in range(i):
   H[i,j]=(energy(cart+unit[i]+unit[j],flat,'three_neighbor')-energy(cart+unit[i]-unit[j],flat,'three_neighbor')-energy(cart-unit[i]+unit[j],flat,'three_neighbor')+energy(cart-unit[i]-unit[j],flat,'three_neighbor'))/(4*step**2)
   H[j,i]=H[i,j]
 return H

Hxx=lateral_derivatives(1e-4)
assert np.linalg.eigvalsh(Hxx).min()>0
assert np.max(np.abs(lateral_derivatives(3e-4)-Hxx))<5e-5
# Control deliberately shows how the hard cutoff corrupts a larger lateral difference.
Hxx_crossing=lateral_derivatives(1e-3)
results={'archive_sha256':expected,'units':'Hessians meV/Angstrom^2 per upper atom; D in eV; lateral x and heights in Angstrom','normalization':'energy averaged over 14 upper atoms','graph_eigenvalues':np.linalg.eigvalsh(L).tolist(),'plate_per_ev_eigenvalues':np.linalg.eigvalsh(K_plate_per_ev).tolist(),'lateral_hessian_fixed_height':Hxx.tolist(),'hard_cutoff_crossing_hessian_at_0p001_a':Hxx_crossing.tolist(),'rules':{}}
for rule,full in (('frozen',False),('three_neighbor',True)):
 grad,Hzz=height_derivatives(rule,1e-3)
 grad2,Hzz2=height_derivatives(rule,3e-3)
 Cmap=obj['cross_hessian'](16,1e-4,full)
 # Orthogonal Frobenius projection of the mixed Hessian onto the rank-six source span.
 B_source=obj['B'];weights=np.linalg.lstsq(B_source,Cmap.reshape(-1),rcond=None)[0]
 C_source=(B_source@weights).reshape(2,n);C_complement=Cmap-C_source
 assert np.max(np.abs(Hzz-Hzz2))<.001
 u=np.ones(n)/np.sqrt(n);other=eigh(K_plate_per_ev)[1][:,1:]
 K00=u@Hzz@u
 S=other.T@Hzz@other-np.outer(other.T@Hzz@u,other.T@Hzz@u)/K00
 B=other.T@K_plate_per_ev@other
 crit=max(0.,float(eigh(-S,B,eigvals_only=True).max()))
 out={'height_force_at_reference':grad.tolist(),'uniform_reference_load_mev_per_a_per_atom':-float(np.sum(grad)),
      'height_hessian_eigenvalues':np.linalg.eigvalsh(Hzz).tolist(),'minimum_stable_D_eV':crit,
      'max_hessian_step_discrepancy':float(np.max(np.abs(Hzz-Hzz2))),
      'C3_height_hessian_defect':float(np.linalg.norm(P@Hzz@P.T-Hzz)/np.linalg.norm(Hzz)),
      'C3_height_force_defect':float(np.linalg.norm(P@grad-grad)/np.linalg.norm(grad)),
      'cases':[]}
 for DeV in (.1,.3,.69,1.2,1.44,1.7,3.0):
  K=Hzz+DeV*K_plate_per_ev
  eig=np.linalg.eigvalsh(K)
  if eig.min()<=0: out['cases'].append({'D_eV':DeV,'status':'UNSTABLE'});continue
  invC=np.linalg.solve(K,Cmap.T)
  soften=Cmap@invC
  source_soften=C_source@np.linalg.solve(K,C_source.T)
  complement_soften=C_complement@np.linalg.solve(K,C_complement.T)
  cross_soften=soften-source_soften-complement_soften
  damp_factor=invC.T@invC  # gamma_add/d if Rayleigh D_b=d I in mean-energy normalization.
  effective=Hxx-soften
  nonuniform_force=grad-grad.mean()
  hstar=-np.linalg.solve(K,nonuniform_force)
  out['cases'].append({'D_eV':DeV,'smallest_height_stiffness':float(eig.min()),
                      'softening_tensor':soften.tolist(),'source_only_softening_tensor':source_soften.tolist(),
                      'complement_only_softening_tensor':complement_soften.tolist(),
                      'source_complement_cross_softening_tensor':cross_soften.tolist(),
                      'source_only_to_full_softening_trace_ratio':float(np.trace(source_soften)/np.trace(soften)),
                      'softening_isotropic_scalar':float(np.trace(soften)/2),
                      'softening_fraction_of_fixed_curvature':float(np.trace(soften)/np.trace(Hxx)),
                      'relaxed_lateral_hessian':effective.tolist(),'damping_tensor_per_unit_height_Rayleigh_d':damp_factor.tolist(),
                      'damping_isotropic_factor':float(np.trace(damp_factor)/2),
                      'maximum_linear_nonuniform_height_shift_a':float(np.abs(hstar).max())})
 results['rules'][rule]=out
print(json.dumps(results,indent=2))
