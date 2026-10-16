#!/usr/bin/env python3
"""Synthetic matrix gradients and readouts, not empirical or interval evidence."""
from pathlib import Path
import json,numpy as np
from scipy.linalg import expm
from scaled_model import *
O=Path(__file__).resolve().parent;inp=json.loads((O/'CERTIFICATE_INPUTS_v0.1.json').read_text());ep=1e-5
x=refine_scaled([point(v) for v in inp['global_centres'][0]['centre']],arb(str(ep)));uu=Z*col(x[:3])+arb(str(ep))*Y*col(x[3:28]);X=np.sqrt(ep)*np.array(entries(uu),float);f=np.array([float(v0[i]+arb(str(ep))*x[28+i]) for i in range(15)]);u=-1j*np.array([(-1)**nodes[j].index(next(v for v in nodes[j] if v not in nodes[i])) for i,j in edges])*np.exp(1j*X)
bn=np.array([(-1)**nodes[j].index(next(v for v in nodes[j] if v not in nodes[i])) for i,j in edges]);ds=[[edges.index((h,k)),edges.index((i,h)),edges.index((i,j)),edges.index((j,k))] for i,j,h,k in diamonds]
def sphere(q,p,t):
 c=np.linalg.norm(p);return np.cos(c*t)*q+(np.sin(c*t)/c if c else t)*p
def directions(r,q,w,rng):
 A=rng.normal(size=(28,r,r))+1j*rng.normal(size=(28,r,r));A=(A+A.conj().transpose(0,2,1))/2
 F=rng.normal(size=A.shape)+1j*rng.normal(size=A.shape);F=(F+F.conj().transpose(0,2,1))/2
 p=rng.normal(size=q.shape)+1j*rng.normal(size=q.shape);z=rng.normal(size=q.shape)+1j*rng.normal(size=q.shape);p-=q*np.vdot(q,p).real;z-=w*np.vdot(w,z).real
 n=np.sqrt(np.vdot(A,A).real+np.vdot(F,F).real+np.vdot(p,p).real+np.vdot(z,z).real);return A/n,F/n,p/n,z/n
def displaced(U,E,q,w,v,t):
 A,F,p,z=v;return np.array([expm(1j*t*A[e])@U[e] for e in range(28)]),E+t*F,sphere(q,p,t),sphere(w,z,t)
def potential_and_gradient(U,E,q,w,da,dk,dg,dv,N):
 r=U.shape[1];Gl=np.zeros_like(U);Ge=da[:,None,None]*E;V=.5*sum(da[e]*np.trace(E[e]@E[e]).real for e in range(28));h=np.zeros((15*r,15*r),complex)
 for e,(i,j) in enumerate(edges):
  h[i*r:(i+1)*r,j*r:(j+1)*r]=-1j*bn[e]*dg[e]*U[e];h[j*r:(j+1)*r,i*r:(i+1)*r]=h[i*r:(i+1)*r,j*r:(j+1)*r].conj().T
  for a in [q,w]:
   M=np.outer(U[e]@a[j],a[i].conjugate());Gl[e]+=N*bn[e]*dg[e]*(M+M.conj().T)
 for i in range(15):h[i*r:(i+1)*r,i*r:(i+1)*r]=dv[i]*np.eye(r)
 for d,es in enumerate(ds):
  factors=[U[es[0]].conj().T,U[es[1]].conj().T,U[es[2]],U[es[3]]];W=np.eye(r,dtype=complex)
  for a in factors:W=W@a
  V+=N*dk[d]*(r-np.trace(W).real)
  for k,e in enumerate(es):
   pre=np.eye(r,dtype=complex);post=pre.copy()
   for j in range(k):pre=pre@factors[j]
   for j in range(k+1,4):post=post@factors[j]
   if k<2:M=post@pre@factors[k];sg=-1
   else:M=factors[k]@post@pre;sg=1
   Gl[e]+=N*dk[d]*sg*(M-M.conj().T)/(2j)
 matter=[]
 for a in [q,w]:
  v=a.ravel();hv=h@v;ev=np.vdot(v,hv).real;V+=N*ev;matter.append((2*N*(hv-ev*v)).reshape(15,r))
 return float(V),(Gl,Ge,*matter)
def readout(U,q):
 out=[]
 for es,(_,_,_,k) in zip(ds,diamonds):
  W=U[es[0]].conj().T@U[es[1]].conj().T@U[es[2]]@U[es[3]];out.append(-np.vdot(q[k],W@q[k])/np.vdot(q[k],q[k]))
 return np.array(out)
rng=np.random.default_rng(162220);rows=[]
for r,N,a in [(2,1.,1.),(3,2.,.4),(5,.3,50.)]:
 for real in [False,True]:
  m=min(a,N*ep)/2;R=3*m/(62*N);eta=min(R,ep/1680) if real else R;nu=m*eta/16
  U0=np.array([np.diag([v]+[1]*(r-1)) for v in u],complex);E0=np.zeros_like(U0);q0=np.zeros((15,r),complex);q0[:,0]=f;v=directions(r,q0,q0,rng);dist=.7*eta;U,E,q,w=displaced(U0,E0,q0,q0,v,dist)
  A,K,G,D=.03,.002,.004,.005;da=rng.uniform(-A,A,28);dk=rng.uniform(-K,K,18);dg=rng.uniform(-G,G,28);dv=rng.uniform(-1,1,15);dv=D*(2*(dv-dv.min())/(dv.max()-dv.min())-1)
  V,grad=potential_and_gradient(U,E,q,w,da,dk,dg,dv,N);norm=np.sqrt(sum(np.vdot(g,g).real for g in grad));bound=A*eta+N*((1+12*eta)*K+14*G+3*D);assert norm<=bound
  vtest=directions(r,q,w,rng);pred=sum(np.vdot(g,vv).real for g,vv in zip(grad,vtest));h=1e-5
  plus=potential_and_gradient(*displaced(U,E,q,w,vtest,h),da,dk,dg,dv,N)[0];minus=potential_and_gradient(*displaced(U,E,q,w,vtest,-h),da,dk,dg,dv,N)[0];err=abs((plus-minus)/(2*h)-pred);assert err<2e-9
  shifted=potential_and_gradient(U,E,q,w,da,dk,dg,dv+100,N)[1];shift_err=max(np.max(abs(g-gg)) for g,gg in zip(grad,shifted));assert shift_err<1e-10
  zr=readout(U,q);zb=readout(U0,q0);readerr=np.max(abs(zr-zb));assert readerr<21*dist
  rows.append({'rank':r,'a':a,'N':N,'epsilon':ep,'real_readout_cap':real,'target_eta':eta,'gradient_shape_norm':float(norm),'gradient_shape_bound':bound,'scale_to_canonical_gradient_budget':nu/bound,'directional_derivative_absolute_error':float(err),'uniform_detuning_gradient_residual':float(shift_err),'maximum_complex_readout_error_over_path_distance':float(readerr/dist),'Gauss_note':'Not enforced; inequalities are on the larger fixed-norm manifold'})
r={'status':'PASS','type':'NUMERICAL synthetic matrix-gradient/readout diagnostics, not empirical or interval evidence','seed':162220,'fixtures':rows,'physical_promotion':0,'independent_review':'PENDING'}
(O/'ROBUST_GRADIENT_DIAGNOSTIC_v0.1.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
