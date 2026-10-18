"""Floating source-law diagnostics; not interval proofs or trajectories."""
from preparation_certificate import carrier
from scipy.linalg import expm
import numpy as np,json
from pathlib import Path
nodes,edges,*_=carrier();rng=np.random.default_rng(20261018);rho=np.sqrt(8+2*np.sqrt(10))
T=np.zeros((15,15))
for i,j,b in edges:T[i,j]=T[j,i]=1
_,vecs=np.linalg.eigh(T);v=vecs[:,-1];v*=np.sign(v.sum());v/=np.linalg.norm(v)
def norm(a):return float(np.linalg.norm(a))
def herm(r):
 a=rng.normal(size=(r,r))+1j*rng.normal(size=(r,r));return (a+a.conj().T)/2

def h(U,r):
 D=np.zeros((15*r,15*r),complex)
 for u,(i,j,b) in zip(U,edges):D[i*r:(i+1)*r,j*r:(j+1)*r]=b*u
 return 1j*(D.conj().T-D)

def gauss(U,E,q,w,nq,nw):
 G=[-nq*np.outer(x,x.conj())+nw*np.outer(y,y.conj()) for x,y in zip(q,w)]
 for u,e,(i,j,b) in zip(U,E,edges):G[i]+=e;G[j]-=u.conj().T@e@u
 return np.array(G)

def source(U,E,q,w,A,F,p,z,nq,nw,lq,lw):
 S=[-nq*(np.outer(y,x.conj())+np.outer(x,y.conj()))+nw*(np.outer(t,s.conj())+np.outer(s,t.conj()))-lq*np.outer(x,x.conj())+lw*np.outer(s,s.conj()) for x,s,y,t in zip(q,w,p,z)]
 for u,e,a,f,(i,j,b) in zip(U,E,A,F,edges):S[i]+=f;S[j]-=u.conj().T@(f+1j*(e@a-a@e))@u
 return np.array(S)

def sphere(q,p,t=1):
 a=norm(p)
 return np.cos(t*a)*q+(np.sin(t*a)/a*p if a else 0)
rows=[];ground=[]
for r in [1,2,3,5]:
 U=[expm(1j*herm(r)) for e in edges];E=[herm(r) for e in edges];Etot=np.sqrt(sum(norm(e)**2 for e in E));E=[e*.1/Etot for e in E]
 q=rng.normal(size=(15,r))+1j*rng.normal(size=(15,r));q/=norm(q);w=rng.normal(size=(15,r))+1j*rng.normal(size=(15,r));w/=norm(w)
 A=[herm(r) for e in edges];F=[herm(r) for e in edges];p=rng.normal(size=q.shape)+1j*rng.normal(size=q.shape);p-=q*np.vdot(q,p).real;z=rng.normal(size=q.shape)+1j*rng.normal(size=q.shape);z-=w*np.vdot(w,z).real
 Ynorm=np.sqrt(sum(norm(x)**2 for x in A+F)+norm(p)**2+norm(z)**2);A=[x/Ynorm for x in A];F=[x/Ynorm for x in F];p/=Ynorm;z/=Ynorm;nq,nw,lq,lw=1.2,.9,.03,-.02
 S=source(U,E,q,w,A,F,p,z,nq,nw,lq,lw);eps=1e-6
 def moved(t):return gauss([expm(1j*t*a)@u for a,u in zip(A,U)],[e+t*f for e,f in zip(E,F)],sphere(q,p,t),sphere(w,z,t),nq+t*lq,nw+t*lw)
 fd=(moved(eps)-moved(-eps))/(2*eps);error=norm(fd-S);bound=np.sqrt(16*.1**2+8+4*nq**2+4*nw**2)+abs(lq)+abs(lw)
 assert error<2e-8;assert norm(S)<=bound;trace=sum(np.trace(s).real for s in S);assert abs(trace-(lw-lq))<1e-12
 f=rng.normal(size=q.shape)+1j*rng.normal(size=q.shape);inner=np.vdot(q,f).real;raw_l=2*np.sqrt(nq)*inner;raw_p=(f-inner*q)/np.sqrt(nq)
 reconstruction=np.sqrt(nq)*raw_p+raw_l/(2*np.sqrt(nq))*q
 assert norm(reconstruction-f)<1e-12 and abs(np.vdot(q,raw_p).real)<1e-12 and norm(raw_p)<=norm(f)/np.sqrt(nq)+1e-12
 shift=np.vdot(q.ravel(),h(U,r)@q.ravel()).real+rho;assert shift>=-1e-12
 rows.append({'rank':r,'source_directional_derivative_residual':error,'source_norm':norm(S),'source_norm_upper':bound,'source_summed_trace':trace,'trace_rate_target':lw-lq,'raw_force_reconstruction_error':norm(reconstruction-f),'raw_tangent_real_inner_abs':abs(np.vdot(q,raw_p).real),'global_ground_shift':shift})
 U0=[np.diag([-1j*b]+[1]*(r-1)).astype(complex) for i,j,b in edges];q0=np.zeros((15,r),complex);q0[:,0]=v
 for scale in [1e-3,1e-4]:
  A=[herm(r) for e in edges];p=rng.normal(size=q0.shape)+1j*rng.normal(size=q0.shape);p-=q0*np.vdot(q0,p).real;speed=np.sqrt(sum(norm(a)**2 for a in A)+norm(p)**2);A=[a*scale/speed for a in A];p*=scale/speed
  X=[expm(1j*a)@u for a,u in zip(A,U0)];Q=sphere(q0,p);shift=np.vdot(Q.ravel(),h(X,r)@Q.ravel()).real+rho
  assert -1e-12<=shift<=10*scale**2+1e-12
  ground.append({'rank':r,'comparison_path_length':scale,'ground_shift':shift,'centered_upper':10*scale**2})
out={'status':'PASS_NUMERICAL_DIAGNOSTICS','source_and_raw_force_controls':rows,'centered_ground_shift_controls':ground,'scope':'Four full-matrix source derivative/trace and raw-force reconstruction fixtures; eight ground-shift fixtures. Electric bound 0.1 used only for the general derivative inequality; these are not claimed endpoint-tube states, trajectories, interval proofs or empirical data.','physical_promotion':0}
(Path(__file__).parent/'SOURCE_BALANCE_DIAGNOSTIC_v0.1.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS: 4 matrix source/raw-force controls and 8 centered ground-shift controls')
