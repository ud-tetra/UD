import contextlib,io,runpy,sys,json,numpy as np
from pathlib import Path
from scipy.optimize import minimize
repo=Path(__file__).resolve().parents[2]
p=next((repo/'captures').glob('*graphite-flexural-schur-8b2d4c61*'))/'derive_graphite_flexural_schur.py'
archive_path=sys.argv[1];cutoff=float(sys.argv[2]) if len(sys.argv)>2 else 16.
sys.argv=[str(p),archive_path]
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path(str(p))
o=d['obj'];cart=o['cart0'];top=o['top'];bottom=o['bottom'];n=14;rc=cutoff;D=1.44;z=3.46
s0=top[:,None,:]+cart-bottom[None,:,:]
mask=np.sum(s0*s0,axis=-1)+z*z<rc*rc
ii,jj=np.where(mask);sv=s0[ii,jj];delta=o['delta'];A=o['A'];z0=o['z0'];lam=o['lam'];C0_coeff=o['C0'];C2=o['C2'];C4=o['C4'];Cbase=o['d']['C']
neighbor_ids=np.array([[j for j,v in row] for row in o['neighbors']]);neighbor_vectors=np.array([[v for j,v in row] for row in o['neighbors']])
Kb=D*d['K_plate_per_ev'];perm=d['perm'];Kbphysical=Kb[np.ix_(np.argsort(perm),np.argsort(perm))]
def energy(x,h,withplate=True,withload=False):
    t=np.concatenate([neighbor_vectors,(h[neighbor_ids]-h[:,None])[:,:,None]],axis=2)
    cr=np.cross(t,np.roll(t,-1,axis=1))
    cr/=np.linalg.norm(cr,axis=2)[:,:,None]
    norm=cr.sum(axis=1);norm/=np.linalg.norm(norm,axis=1)[:,None]
    s=sv+(x-cart)[None,:];zi=z+h[ii];r2=np.sum(s*s,axis=1)+zi*zi;r=np.sqrt(r2)
    rhot=r2-(np.einsum('ij,ij->i',s,norm[ii,:2])+zi*norm[ii,2])**2
    rhob=np.sum(s*s,axis=1)
    def f(rho):
        u=rho/delta**2
        return np.exp(-u)*(C0_coeff+C2*u+C4*u*u)
    v=np.sum(-A*(z0/r)**6+np.exp(-lam*(r-z0))*(Cbase+f(rhot)+f(rhob)))/n
    if withplate:v+=h@Kbphysical@h/2
    if withload:v+=load*h.mean()
    return v
assert abs(energy(cart,np.zeros(n),False)-o['direct_energy'](cart,np.zeros(n),rc))<1e-9
hstep=1e-5;un=np.eye(n)*hstep
forces=np.array([(energy(cart,un[i])-energy(cart,-un[i]))/(2*hstep) for i in range(n)])
load=-forces.sum()
print('pair roster',len(ii),'closest margin',np.min(np.abs(np.sqrt(np.sum(s0*s0,axis=-1)+z*z)-rc)),'load',load,'force nonuniform norm',np.linalg.norm(forces-forces.mean()))

def fn(q):return energy(q[:2],q[2:],withload=True)
def grad(q):
  step=1e-5
  out=np.empty(len(q))
  for i in range(len(q)):
   t=q.copy();t[i]+=step;plus=fn(t);t[i]-=2*step;minus=fn(t)
   out[i]=(plus-minus)/(2*step)
  return out
q0=np.r_[cart,np.zeros(n)]
res=minimize(fn,q0,jac=grad,method='L-BFGS-B',bounds=[(cart[0]-.03,cart[0]+.03),(cart[1]-.03,cart[1]+.03)]+[(-.015,.015)]*n,options={'ftol':1e-15,'gtol':1e-8,'maxiter':300})
print('result',res.success,res.message,res.nit,res.nfev,'energy difference',res.fun-fn(q0),'grad max',np.max(np.abs(grad(res.x))))
print('xshift',res.x[:2]-cart,'hmin max mean',np.min(res.x[2:]),np.max(res.x[2:]),np.mean(res.x[2:]))
changed=np.sum((np.sum((top[:,None,:]+res.x[:2]-bottom[None,:,:])**2,axis=-1)+(z+res.x[2:,None])**2<rc*rc)!=mask)
print('roster changed',changed)
result=dict(cutoff_angstrom=rc,source_archive_sha256='b1ccf62a3e75928e1382cbdd6c669b99675fef9ad5f077e79057a142a0a07875',fixed_roster_pairs=len(ii),roster_changed_at_optimum=int(changed),reference_load_mev_per_a_per_atom=float(load),reference_minimum_pair_cutoff_margin_angstrom=float(np.min(np.abs(np.sqrt(np.sum(s0*s0,axis=-1)+z*z)-rc))),converged=bool(res.success),maximum_stationary_gradient_mev_per_a_per_atom=float(np.max(np.abs(grad(res.x)))),lateral_shift_angstrom=(res.x[:2]-cart).tolist(),height_min_max_mean_angstrom=[float(np.min(res.x[2:])),float(np.max(res.x[2:])),float(np.mean(res.x[2:]))],hessian_step_checks=[])

def numerical_hess(q,dx,dh):
 H=np.zeros((len(q),len(q)));f0=fn(q)
 steps=np.r_[np.ones(2)*dx,np.ones(n)*dh]
 for i in range(len(q)):
  vi=np.eye(len(q))[i]*steps[i]
  H[i,i]=(fn(q+vi)-2*f0+fn(q-vi))/steps[i]**2
  for j in range(i):
   vj=np.eye(len(q))[j]*steps[j]
   H[i,j]=(fn(q+vi+vj)-fn(q+vi-vj)-fn(q-vi+vj)+fn(q-vi-vj))/(4*steps[i]*steps[j]);H[j,i]=H[i,j]
 return H
for dx,dh in ((1e-4,1e-3),(3e-4,3e-3)):
 H=numerical_hess(res.x,dx,dh)
 K=H[2:,2:];C=H[:2,2:];eff=H[:2,:2]-C@np.linalg.solve(K,C.T)
 print('step',dx,dh,'clamped',H[:2,:2],'soften',C@np.linalg.solve(K,C.T),'relaxed',eff,'Kmin',np.min(np.linalg.eigvalsh(K)))
 result['hessian_step_checks'].append(dict(lateral_step_angstrom=dx,height_step_angstrom=dh,clamped_curvature_mev_per_a2_per_atom=float(np.trace(H[:2,:2])/2),softening_mev_per_a2_per_atom=float(np.trace(C@np.linalg.solve(K,C.T))/2),relaxed_curvature_mev_per_a2_per_atom=float(np.trace(eff)/2),smallest_height_stiffness_mev_per_a2_per_atom=float(np.min(np.linalg.eigvalsh(K)))))
 if dx==1e-4:
  aligned_C=C[:,perm];aligned_K=K[np.ix_(perm,perm)]
  source_B=o['B'];source_coef=np.linalg.lstsq(source_B,aligned_C.reshape(-1),rcond=None)[0]
  source_C=(source_B@source_coef).reshape(2,n);rest_C=aligned_C-source_C
  full_S=aligned_C@np.linalg.solve(aligned_K,aligned_C.T)
  source_S=source_C@np.linalg.solve(aligned_K,source_C.T)
  rest_S=rest_C@np.linalg.solve(aligned_K,rest_C.T)
  result['source_projection_at_optimum']=dict(euclidean_squared_norm_fit=float(1-np.linalg.norm(rest_C)**2/np.linalg.norm(aligned_C)**2),full_softening_scalar=float(np.trace(full_S)/2),source_only_softening_scalar=float(np.trace(source_S)/2),complement_only_softening_scalar=float(np.trace(rest_S)/2),cross_softening_scalar=float(np.trace(full_S-source_S-rest_S)/2),source_only_to_full_ratio=float(np.trace(source_S)/np.trace(full_S)))
if rc==16.0:
 pressure_unit=d['Aatom']*1000/160217.6634 # meV/Angstrom/atom per MPa
 base_load=load
 pressure_rows=[]
 for dp in (-5.,-2.5,0.,2.5,5.):
  load=base_load+dp*pressure_unit
  rr=minimize(fn,res.x,jac=grad,method='L-BFGS-B',bounds=[(cart[0]-.03,cart[0]+.03),(cart[1]-.03,cart[1]+.03)]+[(-.015,.015)]*n,options={'ftol':1e-15,'gtol':1e-8,'maxiter':300})
  HH=numerical_hess(rr.x,1e-4,1e-3)
  KK=HH[2:,2:];CC=HH[:2,2:];soft=CC@np.linalg.solve(KK,CC.T);rel=HH[:2,:2]-soft
  newmask=np.sum((top[:,None,:]+rr.x[:2]-bottom[None,:,:])**2,axis=-1)+(z+rr.x[2:,None])**2<rc*rc
  row=dict(dp=dp,stationary_gradient=float(np.max(np.abs(grad(rr.x)))),xshift=(rr.x[:2]-cart).tolist(),mean_height=float(np.mean(rr.x[2:])),hmin=float(min(rr.x[2:])),hmax=float(max(rr.x[2:])),roster_changed=int(np.sum(newmask!=mask)),clamped=float(np.trace(HH[:2,:2])/2),soften=float(np.trace(soft)/2),relaxed=float(np.trace(rel)/2),anisotropy=float(np.ptp(np.linalg.eigvalsh(rel))))
  pressure_rows.append(row)
  print('PRESSURE',row)
 load=base_load
 result['pressure_rows']=pressure_rows
 result['pressure_slopes']=[]
 for a,b in ((pressure_rows[0],pressure_rows[4]),(pressure_rows[1],pressure_rows[3])):
  slope=(b['relaxed']-a['relaxed'])/(b['dp']-a['dp'])
  result['pressure_slopes'].append(dict(interval_MPa=[a['dp'],b['dp']],slope_mev_per_a2_per_atom_per_MPa=slope))
  print('SLOPE interval',a['dp'],b['dp'],'dK/dP',slope)
 # Independent curvature of the height-minimized energy at fixed lateral offsets.
 load=base_load
 baseq=res.x.copy()
 def emin_at(x):
  def inner(h):return energy(x,h,withload=True)
  def ginner(h):
   step=1e-5;out=np.zeros(n)
   for i in range(n):
    v=np.zeros(n);v[i]=step;out[i]=(inner(h+v)-inner(h-v))/(2*step)
   return out
  opt=minimize(inner,baseq[2:],jac=ginner,method='L-BFGS-B',bounds=[(-.015,.015)]*n,options={'ftol':1e-15,'gtol':1e-8,'maxiter':300})
  return opt.fun,float(np.max(np.abs(ginner(opt.x))))
 result['eliminated_energy_curvature_checks']=[]
 for h in (.002,.005):
  f0,_=emin_at(baseq[:2]);values=[]
  for i in range(2):
   ei=np.eye(2)[i]*h
   fp,gp=emin_at(baseq[:2]+ei);fm,gm=emin_at(baseq[:2]-ei)
   values.append((fp-2*f0+fm)/h**2)
  print('ELIMINATED_ENERGY_CURVATURE',h,values)
  result['eliminated_energy_curvature_checks'].append(dict(lateral_step_angstrom=h,curvatures_mev_per_a2_per_atom=values))

print("RESULT_JSON "+json.dumps(result))
