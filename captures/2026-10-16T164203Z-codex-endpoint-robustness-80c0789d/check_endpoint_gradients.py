"""NUMERICAL full-matrix gradient/readout diagnostics at the critical orbit.
Does not simulate trajectories or impose Gauss; bounds hold on fixed norms.
"""
import json
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from geometry import nodes,edges,diamonds,rho,D0
from parity_budget import constants
bn=np.array([(-1)**nodes[j].index(next(t for t in nodes[j] if t not in nodes[i])) for i,j in edges])
ds=[[edges.index((h,k)),edges.index((i,h)),edges.index((i,j)),edges.index((j,k))] for i,j,h,k in diamonds]

def potential_gradient(U,E,q,w,da,dk,xi,site,N):
 r=U.shape[1];Gl=np.zeros_like(U);Ge=da[:,None,None]*E
 V=.5*sum(da[e]*np.trace(E[e]@E[e]).real for e in range(28));h=np.zeros((15*r,15*r),complex)
 for e,(i,j) in enumerate(edges):
  h[i*r:(i+1)*r,j*r:(j+1)*r]=-1j*bn[e]*xi[e]*U[e]
  h[j*r:(j+1)*r,i*r:(i+1)*r]=h[i*r:(i+1)*r,j*r:(j+1)*r].conj().T
  for f in [q,w]:
   M=np.outer(U[e]@f[j],f[i].conjugate());Gl[e]+=N*bn[e]*xi[e]*(M+M.conj().T)
 for i in range(15):h[i*r:(i+1)*r,i*r:(i+1)*r]=site[i]*np.eye(r)
 for d,es in enumerate(ds):
  fac=[U[es[0]].conj().T,U[es[1]].conj().T,U[es[2]],U[es[3]]];W=fac[0]@fac[1]@fac[2]@fac[3];V+=N*dk[d]*(r-np.trace(W).real)
  for k,e in enumerate(es):
   pre=np.eye(r,dtype=complex);post=pre.copy()
   for j in range(k):pre=pre@fac[j]
   for j in range(k+1,4):post=post@fac[j]
   M=post@pre@fac[k] if k<2 else fac[k]@post@pre
   Gl[e]+=N*dk[d]*(-1 if k<2 else 1)*(M-M.conj().T)/(2j)
 matter=[]
 for f in [q,w]:
  ff=f.ravel();hf=h@ff;ev=np.vdot(ff,hf).real;V+=N*ev;matter.append((2*N*(hf-ev*ff)).reshape(15,r))
 return V,(Gl,Ge,*matter)

def direction(r,q,w,rng):
 def herm():
  a=rng.normal(size=(28,r,r))+1j*rng.normal(size=(28,r,r));return (a+a.conj().transpose(0,2,1))/2
 A,F=herm(),herm();p=rng.normal(size=q.shape)+1j*rng.normal(size=q.shape);z=rng.normal(size=w.shape)+1j*rng.normal(size=w.shape)
 p-=q*np.vdot(q,p).real;z-=w*np.vdot(w,z).real
 n=np.sqrt(sum(np.vdot(x,x).real for x in [A,F,p,z]));return tuple(x/n for x in [A,F,p,z])
def displaced(state,v,t):
 U,E,q,w=state;A,F,p,z=v
 def sphere(f,p):
  c=np.linalg.norm(p);return np.cos(c*t)*f+(np.sin(c*t)/c if c else t)*p
 return np.array([expm(1j*t*A[e])@U[e] for e in range(28)]),E+t*F,sphere(q,p),sphere(w,z)
def norm(g):return float(np.sqrt(sum(np.vdot(x,x).real for x in g)))
def loops(U,q):
 out=[]
 for es,(_,_,_,k) in zip(ds,diamonds):
  W=U[es[0]].conj().T@U[es[1]].conj().T@U[es[2]]@U[es[3]];out.append(-np.vdot(q[k],W@q[k])/np.vdot(q[k],q[k]))
 return np.array(out)

rng=np.random.default_rng(1632616);rows=[]
for r,a,N in [(1,1.,1.),(2,.4,2.),(3,50.,.3),(5,1.,1.)]:
 eta=float(constants(str(a),str(N))[5]);dist=.7*eta
 U0=np.array([np.diag([-1j*b]+[1]*(r-1)) for b in bn]);E0=np.zeros_like(U0);q0=np.zeros((15,r),complex)
 rr=float(rho);d=float(D0);lv=[1,rr/3,(1+d)/3,4*(1+d)/(3*rr)];ell=16*(10+d)/9;q0[:,0]=[lv[len(t)-1]/ell**.5 for t in nodes]
 star=(U0,E0,q0,q0);v=direction(r,q0,q0,rng);state=displaced(star,v,dist)
 A,K,H,G,D=.03,.002,.004,.005,.006
 da=rng.uniform(-A,A,28);dk=rng.uniform(-K,K,18);xir=rng.uniform(-G,G,28);site=rng.uniform(-D,D,15)
 zero=np.zeros(15);zr=np.zeros(28);zd=np.zeros(18)
 _,gc0=potential_gradient(*star,da,dk,np.full(28,H),zero,N);bg=norm(gc0);assert bg<5e-13
 _,gc=potential_gradient(*state,da,dk,np.full(28,H),zero,N);beta=A+12*N*K+24*N*H;assert norm(gc)<beta*dist
 _,gg=potential_gradient(*state,zr,zd,xir,site,N);nu=N*(14*G+3*D);assert norm(gg)<nu
 V,gt=potential_gradient(*state,da,dk,H+xir,site,N);assert norm(gt)<=nu+beta*dist
 test=direction(r,state[2],state[3],rng);pred=sum(np.vdot(x,y).real for x,y in zip(gt,test));step=1e-5
 plus=potential_gradient(*displaced(state,test,step),da,dk,H+xir,site,N)[0];minus=potential_gradient(*displaced(state,test,-step),da,dk,H+xir,site,N)[0];err=abs((plus-minus)/(2*step)-pred);assert err<2e-9
 _,shifted=potential_gradient(*state,da,dk,H+xir,site+100,N);free=max(np.max(abs(x-y)) for x,y in zip(gt,shifted));assert free<1e-10
 read=float(np.max(abs(loops(state[0],state[2])-1)));assert read<21*dist
 rows.append({'r':r,'a':a,'N':N,'path_distance_upper_bound':dist,'centered_background_gradient_residual':bg,'centered_gradient_norm':norm(gc),'centered_gradient_bound':beta*dist,'generic_gradient_norm':norm(gg),'generic_gradient_bound':nu,'mixed_gradient_norm':norm(gt),'mixed_gradient_bound':nu+beta*dist,'directional_derivative_error':float(err),'uniform_detuning_gradient_residual':float(free),'complex_loop_error_over_path_distance':read/dist,'scale_to_canonical_gradient_budget':N*eta**3/(12800*(nu+beta*eta)),'note':'Unscaled coefficient shapes; multiply all coefficient arrays by this scale to meet the canonical tube gradient budget. Gauss not imposed.'})
out={'status':'PASS','claim_bin':'NUMERICAL','fixtures':rows,'scope':'Four synthetic full-matrix critical-background gradient, coefficient-split and loop diagnostics; no trajectory, interval proof or empirical data','physical_promotion':0,'independent_review':'PENDING'}
Path('ENDPOINT_GRADIENT_DIAGNOSTIC_v0.1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
