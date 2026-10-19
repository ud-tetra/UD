"""Frozen scalar binary64 corrected J1 P2 estimator; explicit operation sequence."""
import sys,math
from fractions import Fraction as F
sys.dont_write_bytecode=True
J_R=float.fromhex('-0x1.31fce20219ef9p+2')
J_I=float.fromhex('-0x1.1b19329c9fc6cp+0')
M_R=float.fromhex('0x1.1aa812196d0f3p+0')
M_I=float.fromhex('0x1.140858603cc06p-1')
TWO_GAMMA=float.fromhex('0x1.999999999999ap-3')
OMEGA0=float.fromhex('0x1.2000000000000p+2')
LOWER=F(8983,2000)
UPPER=F(9017,2000)

def trace(omega):
 if type(omega) is not float or not math.isfinite(omega):raise ValueError('frequency must be a finite native binary64 float')
 q=F.from_float(omega)
 if not LOWER<=q<=UPPER:raise ValueError('frequency outside certified interval [4.4915,4.5085]')
 # Every statement below performs one native binary64 operation, with no fused complex expression.
 dw=omega-OMEGA0
 sw=omega+OMEGA0
 s=dw*sw
 t=TWO_GAMMA*dw
 pr=s*M_R
 qr=t*M_I
 cr=pr+qr
 real=J_R+cr
 pi=s*M_I
 qi=t*M_R
 ci=pi-qi
 imag=J_I+ci
 return [dw,sw,s,t,pr,qr,cr,real,pi,qi,ci,imag]

def evaluate(omega):
 nodes=trace(omega)
 return complex(nodes[7],nodes[11])
