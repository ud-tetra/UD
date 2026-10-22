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
