"""Frozen scalar binary64 corrected J1 P2 estimator; explicit operation sequence."""
import sys,math
from fractions import Fraction as F
sys.dont_write_bytecode=True
J_R=float.fromhex('-0x1.283b0d3d406b1p+2')
J_I=float.fromhex('-0x1.096dea6466e81p+0')
M_R=float.fromhex('0x1.09dc7c12e071ap+0')
M_I=float.fromhex('0x1.f51d9c0270eafp-2')
TWO_GAMMA=float.fromhex('0x1.999999999999ap-3')
OMEGA0=float.fromhex('0x1.2100000000000p+2')
LOWER=F(36057,8000)
UPPER=F(36193,8000)

def trace(omega):
 if type(omega) is not float or not math.isfinite(omega):raise ValueError('frequency must be a finite native binary64 float')
 q=F.from_float(omega)
 if not LOWER<=q<=UPPER:raise ValueError('frequency outside certified interval [4.507125,4.524125]')
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
