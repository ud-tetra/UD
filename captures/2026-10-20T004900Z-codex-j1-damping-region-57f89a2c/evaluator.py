"""Two-input corrected J1 estimators, exact selector, explicit binary64 operations."""
import sys
sys.dont_write_bytecode=True
import math
from fractions import Fraction as F
CONSTANTS={'original':{'J_R':float.fromhex('-0x1.31fce20219ef9p+2'),'J_I':float.fromhex('-0x1.1b19329c9fc6cp+0'),'M_R':float.fromhex('0x1.1aa812196d0f3p+0'),'M_I':float.fromhex('0x1.140858603cc06p-1'),'OMEGA0':float.fromhex('0x1.2000000000000p+2'),'GAMMA0':float.fromhex('0x1.999999999999ap-4'),'TWO':float.fromhex('0x1.0000000000000p+1')},'neighbor':{'J_R':float.fromhex('-0x1.283b0d3d406b1p+2'),'J_I':float.fromhex('-0x1.096dea6466e81p+0'),'M_R':float.fromhex('0x1.09dc7c12e071ap+0'),'M_I':float.fromhex('0x1.f51d9c0270eafp-2'),'OMEGA0':float.fromhex('0x1.2100000000000p+2'),'GAMMA0':float.fromhex('0x1.999999999999ap-4'),'TWO':float.fromhex('0x1.0000000000000p+1')}}
CENTERS={'original':F(9,2),'neighbor':F(289,64)}
RHO=F(17,2000)
GAMMA_LOWER=F(1,10)
GAMMA_UPPER=F(201,2000)
LOWER=CENTERS['original']-RHO
UPPER=CENTERS['neighbor']+RHO
SWITCH=F(577,128)

def validated(omega,gamma):
 if type(omega) is not float or type(gamma) is not float or not math.isfinite(omega) or not math.isfinite(gamma):raise ValueError('inputs must be finite native binary64 floats')
 w,g=F.from_float(omega),F.from_float(gamma)
 if not LOWER<=w<=UPPER or not GAMMA_LOWER<=g<=GAMMA_UPPER:raise ValueError('input outside certified frequency/damping rectangle')
 return w,g

def branch(omega,gamma):
 w,g=validated(omega,gamma)
 return 'original' if w<=SWITCH else 'neighbor'

def trace(leaf,omega,gamma):
 w,g=validated(omega,gamma)
 if leaf not in CENTERS or not CENTERS[leaf]-RHO<=w<=CENTERS[leaf]+RHO:raise ValueError('input outside leaf rectangle')
 J_R,J_I,M_R,M_I,OMEGA0,GAMMA0,TWO=[CONSTANTS[leaf][k] for k in ['J_R','J_I','M_R','M_I','OMEGA0','GAMMA0','TWO']]
 # Each assignment is one rounded primitive operation. No FMA/contraction.
 dw=omega-OMEGA0
 sw=omega+OMEGA0
 s=dw*sw
 dg=gamma-GAMMA0
 p=gamma*dw
 q=OMEGA0*dg
 v=p+q
 t=TWO*v
 pr=s*M_R
 qr=t*M_I
 cr=pr+qr
 real=J_R+cr
 pi=s*M_I
 qi=t*M_R
 ci=pi-qi
 imag=J_I+ci
 return [dw,sw,s,dg,p,q,v,t,pr,qr,cr,real,pi,qi,ci,imag]

def evaluate(omega,gamma):
 nodes=trace(branch(omega,gamma),omega,gamma)
 return complex(nodes[11],nodes[15])
