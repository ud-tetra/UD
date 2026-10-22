import contextlib,io,runpy,sys,json
import numpy as np
from pathlib import Path
repo=Path(__file__).resolve().parents[2]
old=next((repo/'captures').glob('*graphite-material-projection-fcd6e90e*'))/'derive_graphite_source_projection.py'
archive_path=sys.argv[1]
sys.argv=[str(old),archive_path]
with contextlib.redirect_stdout(io.StringIO()): d=runpy.run_path(str(old))
for n in ['top','bottom','rotation_xy','cart0','labels','basis','R','inv_supercell','A','z0','C0','C2','C4','delta','lam','Kcart','constraint','vertex_permutation','physical_rot']:
 globals()[n]=d[n]
B=Kcart.reshape(7,-1).T
# Replicate top enumerator, retaining integer address and sublattice.
addr=[]
for p in range(-18,19):
 for q in range(-18,19):
  local=inv_supercell@R@np.array([p,q])
  for site in range(2):
   if np.all(local>=-1e-9) and np.all(local<1-1e-9): addr.append((site,p,q))
assert len(addr)==14
assert [site*7+(q-2*p)%7 for site,p,q in addr]==labels
lookup={(site,(q-2*p)%7):j for j,(site,p,q) in enumerate(addr)}
neighbors=[]
for i,(site,p,q) in enumerate(addr):
 if site==0: paths=[(1,p,q),(1,p-1,q),(1,p,q-1)]
 else: paths=[(0,p,q),(0,p+1,q),(0,p,q+1)]
 dn=[]
 for other,pp,qq in paths:
  vec=np.array([pp-p,qq-q]) + (np.array([1/3,1/3]) if other==1 else np.array([0,0])) -(np.array([1/3,1/3]) if site==1 else np.array([0,0]))
  dn.append((lookup[(other,(qq-2*pp)%7)],basis@R@vec))
 neighbors.append(dn)
assert all(abs(np.linalg.norm(v)-1.42)<1e-9 for row in neighbors for j,v in row)
# Check three-neighbor normal by averaging cyclic cross products of atom-to-neighbor vectors.
def n_from_heights(vecs,z):
 r=np.column_stack([vecs,z])
 cross=np.array([np.cross(r[j],r[(j+1)%3]) for j in range(3)])
 cross/=np.linalg.norm(cross,axis=1)[:,None]
 n=cross.sum(axis=0)
 return n/np.linalg.norm(n)
step=1e-5
n_test=[]
for row in neighbors:
 dvec=np.array([v for j,v in row])
 assert abs(n_from_heights(dvec,np.zeros(3))[2]-1)<1e-12
 for m in range(3):
  t=np.zeros(3);t[m]=step
  finite=(n_from_heights(dvec,t)-n_from_heights(dvec,-t))/(2*step)
  prediction=np.r_[-(2/(3*1.42**2))*dvec[m],[0.]]
  n_test.append(float(np.linalg.norm(finite-prediction)))
assert max(n_test)<1e-10

def height_forces(cart,rc,full):
 z=3.46
 dif=top[:,None,:]+cart-bottom[None,:,:]
 rr=np.sum(dif*dif,axis=-1)
 r2=rr+z*z
 valid=r2<rc**2
 r=np.sqrt(r2)
 u=rr/delta**2
 D=A*(z0/r)**6
 H=(d['C']+2*np.exp(-u)*(C0+C2*u+C4*u*u))*np.exp(-lam*(r-z0))
 ez=6*D*z/r2-lam*H*z/r
 forces=np.sum(np.where(valid,ez,0),axis=1)/14
 if not full: return forces
 fp=np.exp(-u)*(C2+2*C4*u-(C0+C2*u+C4*u*u))/delta**2
 multiplier=np.where(valid,np.exp(-lam*(r-z0))*fp,0)
 for i,row in enumerate(neighbors):
  for j,vec in row:
   forces[j]+=np.sum(multiplier[i]*(4*z/(3*1.42**2))*(dif[i]@vec))/14
 return forces

def cross_hessian(rc,step,full):
 m=np.empty((2,14))
 for axis in range(2):
  dx=np.eye(2)[axis]*step
  m[axis]=(height_forces(cart0+dx,rc,full)-height_forces(cart0-dx,rc,full))/(2*step)
 o=np.empty_like(m)
 for j,k in enumerate(labels): o[:,k]=m[:,j]
 a=np.empty_like(o)
 for site in range(2):
  for k in range(7): a[:,site*7+(k+2)%7]=o[:,site*7+k]
 return a

def fit(m):
 t=m.reshape(-1)
 coef=np.linalg.lstsq(B,t,rcond=None)[0]
 residual=np.linalg.norm(B@coef-t)/np.linalg.norm(t)
 return dict(norm=float(np.linalg.norm(m)),relative_residual=float(residual),explained_squared=float(1-residual**2),coefficients=coef.tolist(),uniform=m.sum(axis=1).tolist(),symmetry_defect=float(np.linalg.norm(constraint@t)/np.linalg.norm(t)))
def direct_energy(cart, heights, rc):
    total=0.
    for i,row in enumerate(neighbors):
        v=np.array([p for j,p in row])
        dz=np.array([heights[j]-heights[i] for j,p in row])
        n=n_from_heights(v,dz)
        s=top[i]+cart-bottom
        z=3.46+heights[i]
        r2=np.sum(s*s,axis=1)+z*z
        valid=r2<rc*rc
        r=np.sqrt(r2[valid]); sv=s[valid]
        rho_top=r2[valid]-(sv@n[:2]+z*n[2])**2
        rho_bottom=np.sum(sv*sv,axis=1)
        def ff(rho):
            u=rho/delta**2
            return np.exp(-u)*(C0+C2*u+C4*u*u)
        total+=np.sum(-A*(z0/r)**6+np.exp(-lam*(r-z0))*(d['C']+ff(rho_top)+ff(rho_bottom)))
    return total/14

fd_force_errors=[]
for cart in (cart0,cart0+np.array([0.013,-0.021])):
    ana=height_forces(cart,16,True)
    zstep=1e-5
    fd=[]
    for k in range(14):
        q=np.zeros(14);q[k]=zstep
        fd.append((direct_energy(cart,q,16)-direct_energy(cart,-q,16))/(2*zstep))
    fd_force_errors.append(float(np.max(np.abs(ana-np.array(fd)))))
assert max(fd_force_errors)<3e-7
result={'neighbor_normal_linear_fd_errors':n_test,'full_energy_height_force_fd_max_errors':fd_force_errors,'checks':[]}
base_full=cross_hessian(16,1e-4,True)
scan=[]
for offset in range(7):
   m=np.empty_like(base_full)
   for site in range(2):
      for k in range(7):m[:,site*7+(k+offset)%7]=base_full[:,site*7+k]
   scan.append({'offset_relative_to_selected_2':offset,'C3_defect':fit(m)['symmetry_defect']})
result['registration_offset_scan']=scan
# Independent mixed four-point differences of the nonlinear local-normal energy.
xy_step=1e-3
z_step=1e-4
mixed=np.zeros((2,14))
for axis in range(2):
  for atom in range(14):
    dx=np.eye(2)[axis]*xy_step
    dz=np.eye(14)[atom]*z_step
    mixed[axis,atom]=(direct_energy(cart0+dx,dz,16)-direct_energy(cart0+dx,-dz,16)
                      -direct_energy(cart0-dx,dz,16)+direct_energy(cart0-dx,-dz,16))/(4*xy_step*z_step)
ordered=np.empty_like(mixed)
for j,k in enumerate(labels):ordered[:,k]=mixed[:,j]
aligned=np.empty_like(ordered)
for site in range(2):
 for k in range(7):aligned[:,site*7+(k+2)%7]=ordered[:,site*7+k]
result['full_mixed_energy_four_point_max_error_mev_per_a2_per_atom']=float(np.max(np.abs(aligned-cross_hessian(16,xy_step,True))))
assert result['full_mixed_energy_four_point_max_error_mev_per_a2_per_atom']<2e-4
for rc,h in ((14,1e-4),(16,1e-3),(16,1e-4),(16,1e-5),(18,1e-4)):
 frozen=cross_hessian(rc,h,False); full=cross_hessian(rc,h,True); extra=full-frozen
 result['checks'].append(dict(cutoff=rc,h=h,frozen=fit(frozen),full_local_normal=fit(full),normal_rotation_term=fit(extra),relative_norm_change=float(np.linalg.norm(extra)/np.linalg.norm(frozen))))
print(json.dumps(result,indent=2))
