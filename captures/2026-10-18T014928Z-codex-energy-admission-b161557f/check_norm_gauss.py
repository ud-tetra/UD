"""Floating constructor diagnostics, distinct from exact enclosure arithmetic."""
from preparation_certificate import carrier
from scipy.linalg import expm
import numpy as np,json
from pathlib import Path
nodes,edges,*_=carrier();rng=np.random.default_rng(20261018)
adj=np.zeros((15,15))
for i,j,b in edges:adj[i,j]=adj[j,i]=1
_,V=np.linalg.eigh(adj);v=V[:,-1];v*=np.sign(v.sum());v/=np.linalg.norm(v)
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
rows=[]
for r in [1,2,3,5]:
 U=[np.diag([-1j*b]+[1]*(r-1)).astype(complex) for i,j,b in edges];q=np.zeros((15,r),complex);q[:,0]=v
 A=[herm(r) for e in edges];p=rng.normal(size=q.shape)+1j*rng.normal(size=q.shape);p-=q*np.vdot(q,p).real
 speed=np.sqrt(sum(norm(a)**2 for a in A)+norm(p)**2);A=[a/speed for a in A];p/=speed
 H=h(U,r);H1=h([1j*a@u for a,u in zip(A,U)],r)
 fprime=2*np.vdot(p.ravel(),H@q.ravel()).real+np.vdot(q.ravel(),H1@q.ravel()).real
 assert abs(fprime)<1e-12
 ratios=[]
 for trial in range(8):
  X=[expm(1j*herm(r))@u for u in U];z=rng.normal(size=q.shape)+1j*rng.normal(size=q.shape);z/=norm(z);p=rng.normal(size=q.shape)+1j*rng.normal(size=q.shape);p-=z*np.vdot(z,p).real;A=[herm(r) for e in edges]
  speed=np.sqrt(sum(norm(a)**2 for a in A)+norm(p)**2);A=[a/speed for a in A];p/=speed;c2=norm(p)**2
  H=h(X,r);H1=h([1j*a@u for a,u in zip(A,X)],r);H2=h([-a@a@u for a,u in zip(A,X)],r);z=z.ravel();p=p.ravel()
  f2=2*np.vdot(p,H@p).real-2*c2*np.vdot(z,H@z).real+4*np.vdot(p,H1@z).real+np.vdot(z,H2@z).real
  assert abs(f2)<=20+1e-12;ratios.append(abs(f2)/20)
 # Near-nominal nonzero Gauss level; use a known comparison path length.
 nq,nw=1.03,.98;scale=.01;A=[herm(r) for e in edges];E=[herm(r) for e in edges]
 p=rng.normal(size=q.shape)+1j*rng.normal(size=q.shape);p-=q*np.vdot(q,p).real
 z=rng.normal(size=q.shape)+1j*rng.normal(size=q.shape);z-=q*np.vdot(q,z).real
 speed=np.sqrt(sum(norm(a)**2 for a in A+E)+norm(p)**2+norm(z)**2);A=[a*scale/speed for a in A];E=[e*scale/speed for e in E];p*=scale/speed;z*=scale/speed
 def sphere(p):
  t=norm(p);return np.cos(t)*q+np.sin(t)/t*p
 Q,W=sphere(p),sphere(z);X=[expm(1j*a)@u for a,u in zip(A,U)];G=gauss(X,E,Q,W,nq,nw);G0=gauss(U,[np.zeros((r,r),complex) for e in edges],q,q,nq,nw)
 L=np.sqrt(8+4*nq*nq+4*nw*nw);difference=norm(G-G0)
 assert difference<=L*scale;assert abs(sum(np.trace(g).real for g in G)-(nw-nq))<1e-12
 assert norm(G)>=abs(nw-nq)/np.sqrt(15*r)
 gs=[expm(1j*herm(r)) for i in nodes];Xg=[gs[i]@x@gs[j].conj().T for x,(i,j,b) in zip(X,edges)];Eg=[gs[i]@e@gs[i].conj().T for e,(i,j,b) in zip(E,edges)];Qg=np.array([g@x for g,x in zip(gs,Q)]);Wg=np.array([g@x for g,x in zip(gs,W)])
 Gg=gauss(Xg,Eg,Qg,Wg,nq,nw);cov=norm(Gg-np.array([g@x@g.conj().T for g,x in zip(gs,G)]));assert cov<1e-12
 rows.append({'rank':r,'nominal_single_species_first_derivative_abs':abs(fprime),'random_hessian_fixtures':8,'max_hessian_over_bound':max(ratios),'comparison_path_length':scale,'gauss_difference':difference,'gauss_difference_bound':L*scale,'global_trace':sum(np.trace(g).real for g in G),'trace_target':nw-nq,'gauss_covariance_residual':cov})
result={'status':'PASS_NUMERICAL_DIAGNOSTICS','rows':rows,'scope':'32 random geodesic Hessian fixtures, four centering and four Gauss/covariance controls. Nonzero Gauss states are ambient controls, not zero-source constrained-action solutions. No trajectory or empirical data.','physical_promotion':0}
(Path(__file__).parent/'NORM_GAUSS_DIAGNOSTIC_v0.1.json').write_text(json.dumps(result,indent=2)+'\n');print('PASS: 32 Hessian fixtures, 4 centering and 4 Gauss/covariance controls')
