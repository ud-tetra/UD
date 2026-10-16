"""NUMERICAL diagnostics of the analytic isometric involution.
No trajectory, interval-domain proof, physical data or Gauss projection.
"""
import json
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from geometry import nodes,edges,diamonds,kc,rho,D0
rng=np.random.default_rng(17616)
def herm(r):
 x=rng.normal(size=(r,r))+1j*rng.normal(size=(r,r));return (x+x.conj().T)/2

def energy(U,E,q,w,a,N):
 r=U.shape[-1];D=np.zeros((15*r,15*r),complex)
 for e,(i,j) in enumerate(edges):
  b=(-1)**next(k for k,t in enumerate(nodes[j]) if t not in nodes[i]);D[i*r:(i+1)*r,j*r:(j+1)*r]=b*U[e]
 h=1j*(D.conj().T-D);out=a/2*sum(np.trace(x@x).real for x in E)
 for i,j,l,k in diamonds:
  X=U[edges.index((i,l))]@U[edges.index((l,k))];Y=U[edges.index((i,j))]@U[edges.index((j,k))]
  out+=N*float(kc)*(r-np.trace(X.conj().T@Y).real)
 for f in [q,w]:
  v=f.reshape(-1);out+=N*np.vdot(v,h@v).real
 return out

def flip(U,E,q,w):
 r=U.shape[-1];Js=[np.diag([1]+[(-1)**len(t)]*(r-1)) for t in nodes]
 return (np.array([-Js[i]@U[e].conj()@Js[j] for e,(i,j) in enumerate(edges)]),
         np.array([Js[i]@E[e].conj()@Js[i] for e,(i,j) in enumerate(edges)]),
         np.array([Js[i]@q[i].conj() for i in range(15)]),np.array([Js[i]@w[i].conj() for i in range(15)]))

rows=[]
for r,a,N in [(1,1.,1.),(2,.03,2.),(3,2.,.4),(5,1.,1.)]:
 U=np.array([expm(1j*herm(r)) for _ in edges]);E=np.array([herm(r) for _ in edges]);fields=[]
 for _ in range(2):
  f=rng.normal(size=(15,r))+1j*rng.normal(size=(15,r));fields.append(f/np.linalg.norm(f))
 state=(U,E,*fields);flipped=flip(*state);twice=flip(*flipped)
 diff=abs(energy(*state,a,N)-energy(*flipped,a,N));invol=max(float(np.max(abs(x-y))) for x,y in zip(state,twice))
 metric=abs(sum(np.vdot(x,x).real for x in state)-sum(np.vdot(x,x).real for x in flipped))
 # Test the fixed representative with all active-link orientation signs.
 stU=[]
 for i,j in edges:
  b=(-1)**next(k for k,t in enumerate(nodes[j]) if t not in nodes[i]);stU.append(np.diag([-1j*b]+[1]*(r-1)))
 d=float(D0);rr=float(rho);lev=[1,rr/3,(1+d)/3,4*(1+d)/(3*rr)];ell=16*(10+d)/9
 f=np.zeros((15,r),complex);f[:,0]=[lev[len(t)-1]/ell**.5 for t in nodes]
 star=(np.array(stU),np.zeros_like(E),f,f);fixed=max(float(np.max(abs(x-y))) for x,y in zip(star,flip(*star)))
 assert diff<2e-10 and invol==0 and metric<2e-10 and fixed==0
 rows.append({'r':r,'a':a,'N':N,'energy_invariance_abs_error':diff,'involution_abs_error':invol,'ambient_norm_invariance_abs_error':metric,'background_fixed_abs_error':fixed})
out={'status':'PASS','claim_bin':'NUMERICAL','scope':'Four deterministic full-matrix synthetic states; diagnostic of analytic energy isometry, square identity and fixed background. No empirical samples, constrained trajectory or domain proof.','fixtures':rows,'physical_promotion':0}
Path('PARITY_MATRIX_DIAGNOSTIC_v0.1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
