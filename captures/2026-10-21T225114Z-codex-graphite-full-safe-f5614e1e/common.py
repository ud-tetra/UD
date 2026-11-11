from pathlib import Path
import numpy as np,sys
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'graphite-branch-aware'))
from geometry import setup,clearance

def load(case):
 a=np.load(ROOT/'graphite-stationary'/case/'RELAXED.npz');q=np.load(ROOT/'graphite-stationary'/case/'HESSIAN.npz');P=q['primitive_P'];d=P.shape[1];m=3*d-5;nx=d-2;B=np.zeros((len(P),3,m));B[:,0,:nx]=P@q['basis_S'];B[:,1,nx:2*nx]=P@q['basis_S'];B[:,2,2*nx:]=P@q['basis_Q'];nei,b=setup(ROOT,case,a);return a,B,nei,b

def vector(m,kind,index):
 if kind=='column':w=np.eye(m)[index]
 else:w=np.cos(np.sqrt(3)*np.arange(1,m+1));w/=np.linalg.norm(w)
 return w

def positions(x,disp,h):
 # Compute affine coordinates in extended precision, then round once to native double.
 return np.asarray(np.asarray(x,dtype=np.longdouble)+np.longdouble(h)*np.asarray(disp,dtype=np.longdouble),dtype=np.float64)

def directions(m):
 v=[];names=[]
 for i in range(3):
  w=np.sin((i+1)*np.arange(1,m+1));v.append(w/np.linalg.norm(w));names.append('regression_sine_'+str(i))
 for k in [2,3,5,7,11,13]:
  w=np.cos(np.sqrt(k)*np.arange(1,m+1));v.append(w/np.linalg.norm(w));names.append(('regression_' if k in [2,3,5] else 'fresh_')+'cos_sqrt_'+str(k))
 return np.array(v),names

def input_guard(x,B,nei,b,disp,steps,knots):
 flat=B.reshape(-1,B.shape[2]);norm=np.linalg.norm(b,axis=2);u=b/norm[:,:,None];theta=np.stack([np.sum(u[:,i]*u[:,j],axis=1) for i,j in [(0,1),(0,2),(1,2)]],axis=1);branch0=np.searchsorted(knots,theta);errors=[];tangent=[];perp=[];margins=[];safe=[];w=flat.T@disp.ravel()
 for h in steps:
  xp=positions(x,disp,h);xm=positions(x,disp,-h);eff=np.asarray((xp.astype(np.longdouble)-xm.astype(np.longdouble))/(2*np.longdouble(h)),dtype=np.float64).ravel();qe=flat.T@eff;errors.append(float(np.linalg.norm(eff-disp.ravel())));tangent.append(float(np.linalg.norm(qe-w)));perp.append(float(np.linalg.norm(eff-flat@qe)));ok=True;margin=np.inf
  for t in np.linspace(-1,1,9):
   xx=positions(x,disp,t*h);bb=b+(xx-x)[nei]-(xx-x)[:,None,:];lens=np.linalg.norm(bb,axis=2);assert np.max(lens)<1.7;uu=bb/lens[:,:,None];theta=np.stack([np.sum(uu[:,i]*uu[:,j],axis=1) for i,j in [(0,1),(0,2),(1,2)]],axis=1);ok=bool(ok and np.array_equal(np.searchsorted(knots,theta),branch0));margin=min(margin,float(np.min(abs(theta[:,:,None]-knots))))
  safe.append(ok);margins.append(margin)
 return np.array([errors,tangent,perp,margins]),np.array(safe)
