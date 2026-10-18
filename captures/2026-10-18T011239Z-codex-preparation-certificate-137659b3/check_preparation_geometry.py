"""Floating diagnostics only. The analytic metric inequalities are in the paper.
Uses direct residuals to avoid trace-subtraction cancellation near the orbit.
"""
import numpy as np,json
from scipy.linalg import expm
from preparation_certificate import carrier
from pathlib import Path
nodes,edges,parent,phase,paths,cycles=carrier();rng=np.random.default_rng(20261018)
adj=np.zeros((15,15))
for i,j,b in edges:adj[i,j]=adj[j,i]=1
_,vs=np.linalg.eigh(adj);v=vs[:,-1];v*=np.sign(v.sum());v/=np.linalg.norm(v)
def norm(x):return float(np.linalg.norm(x))
def herm(r):
 A=rng.normal(size=(r,r))+1j*rng.normal(size=(r,r));return (A+A.conj().T)/2

def point(r):
 U=[np.diag([-1j*b]+[1]*(r-1)).astype(complex) for i,j,b in edges]
 q=np.zeros((15,r),complex);q[:,0]=v
 return U,[np.zeros((r,r),complex) for _ in edges],q,q.copy()

def evaluate(U,E,q,w):
 r=q.shape[1];T={14:np.eye(r,dtype=complex)}
 for i in range(13,-1,-1):
  j=parent[i];e=next(k for k,(a,b,c) in enumerate(edges) if (a,b)==(i,j));T[i]=U[e]@T[j]
 tq=np.array([T[i].conj().T@q[i] for i in range(15)]);tw=np.array([T[i].conj().T@w[i] for i in range(15)])
 S=sum(v[i]*phase[i]*tq[i] for i in range(15));W=sum(v[i]*phase[i]*tw[i] for i in range(15));n=S/norm(S);P=np.outer(n,n.conj());h=[];linkgeo=[]
 for c in cycles:
  H=T[c['i']].conj().T@U[c['edge']]@T[c['j']];D=np.eye(r)+(c['sign']-1)*P
  h.append(norm(H-D)**2);linkgeo.append(sum(np.angle(np.linalg.eigvals(D.conj().T@H))**2))
 target=np.array([v[i]*phase[i].conjugate()*n for i in range(15)])
 cross=np.vdot(n,W);wt=target*(cross/abs(cross) if abs(cross)>0 else 1)
 chord=norm(tq-target)**2+norm(tw-wt)**2;electric=sum(norm(x)**2 for x in E)
 def angle(x,y):
  inner=float(np.vdot(x,y).real);return np.arctan2(norm(y-inner*x),inner)
 witness=electric+sum(linkgeo)+angle(target,tq)**2+angle(wt,tw)**2
 score=electric+121/49*(sum(h)+chord)
 return score,witness

def dressed(U,q):
 vals=[]
 for k,s in enumerate(nodes):
  for i,t in enumerate(nodes):
   if len(s)==len(t)+2 and set(t)<set(s):
    mid=[j for j,u in enumerate(nodes) if len(u)==len(t)+1 and set(t)<set(u)<set(s)];j,h=mid
    def mat(a,b):return U[next(e for e,(x,y,z) in enumerate(edges) if (x,y)==(a,b))]
    W=(mat(i,h)@mat(h,k)).conj().T@mat(i,j)@mat(j,k)
    vals.append(-np.vdot(q[k],W@q[k])/np.vdot(q[k],q[k]))
 return np.array(vals)
rows=[]
for r in [1,2,3,5]:
 U,E,q,w=point(r);base,dist=evaluate(U,E,q,w)
 for scale in [1e-3,1e-9]:
  A=[herm(r) for _ in edges];F=[herm(r) for _ in edges];p=rng.normal(size=q.shape)+1j*rng.normal(size=q.shape);z=rng.normal(size=w.shape)+1j*rng.normal(size=w.shape)
  p-=q*np.vdot(q,p).real;z-=w*np.vdot(w,z).real
  total=np.sqrt(sum(norm(x)**2 for x in A+F)+norm(p)**2+norm(z)**2);A=[x*scale/total for x in A];F=[x*scale/total for x in F];p*=scale/total;z*=scale/total
  def sphere(q,p):
   h=norm(p);return np.cos(h)*q+np.sin(h)/h*p
  X=[expm(1j*x)@u for x,u in zip(A,U)];Q=sphere(q,p);W=sphere(w,z)
  score,witness=evaluate(X,F,Q,W)
  G=[expm(1j*herm(r)) for _ in nodes];a,b=.37,-.29
  Xg=[G[i]@x@G[j].conj().T for x,(i,j,c) in zip(X,edges)];Fg=[G[i]@f@G[i].conj().T for f,(i,j,c) in zip(F,edges)]
  Qg=np.array([np.exp(1j*a)*g@x for g,x in zip(G,Q)]);Wg=np.array([np.exp(1j*b)*g@x for g,x in zip(G,W)])
  sg,_=evaluate(Xg,Fg,Qg,Wg)
  assert witness<=score*(1+1e-5)+1e-28
  assert score<=10000*scale**2
  assert abs(score-sg)<=1e-5*max(score,sg)+1e-27
  rows.append({'rank':r,'input_product_geodesic_length':scale,'score_direct':score,'constructed_orbit_distance_squared':witness,'score_over_path_squared':score/scale**2,'gauge_phase_relative_error':abs(score-sg)/max(score,sg),'nominal_score_roundoff':base})
# Explicit zero-divergence hidden electric witness on the first diamond.
import verify_preparation
cert=json.loads((Path(__file__).parent/'PREPARATION_CERTIFICATE_v0.1.json').read_text());cycle=cert['topology']['diamond_cycle_witness'];hidden=[]
for r in [1,2,3,5]:
 U,E,q,w=point(r);s=3.0
 F=[s*z*np.eye(r) for z in cycle]
 divergence=[np.zeros((r,r),complex) for _ in nodes]
 for f,u,(i,j,b) in zip(F,U,edges):divergence[i]+=f;divergence[j]-=u.conj().T@f@u
 err=max(abs(dressed(U,q)-1));sc,wd=evaluate(U,F,q,w)
 assert err<1e-12 and max(map(norm,divergence))<1e-12 and abs(sc-4*r*s*s)<1e-10
 x={'rank':r,'electric_orbit_distance_squared':4*r*s*s,'score':sc,'gauss_residual':max(map(norm,divergence)),'active_loop_error':float(err)}
 if r>=2:
  X=[u.copy() for u in U];e=cycles[0]['edge'];X[e][1,1]=np.exp(.2j);sc,_=evaluate(X,E,q,w)
  assert sc>0 and max(abs(dressed(X,q)-1))<1e-12
  x.update(unused_configuration_score=sc,unused_active_loop_error=float(max(abs(dressed(X,q)-1))))
 hidden.append(x)
out={'status':'PASS_NUMERICAL_DIAGNOSTICS','perturbation_fixtures':rows,'hidden_sector_controls':hidden,'scope':'Floating direct-residual checks, random off-constraint perturbations for full-manifold upper bounds, explicit zero-Gauss hidden electric controls; no independent review or empirical input','physical_promotion':0}
(Path(__file__).parent/'PREPARATION_GEOMETRY_DIAGNOSTIC_v0.1.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS: 8 full-matrix perturbations, 4 hidden-electric controls, 3 unused-color controls')
