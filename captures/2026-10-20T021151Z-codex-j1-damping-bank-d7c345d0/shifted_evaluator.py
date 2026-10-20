"""Two-input corrected J1 estimators, exact selector, explicit binary64 operations."""
import sys
sys.dont_write_bytecode=True
import math
from fractions import Fraction as F
CONSTANTS={'original':{'J_R':float.fromhex('-0x1.31ad11be700c8p+2'),'J_I':float.fromhex('-0x1.1da368829f9ddp+0'),'M_R':float.fromhex('0x1.19c2e94324a17p+0'),'M_I':float.fromhex('0x1.1639bbd367c1cp-1'),'OMEGA0':float.fromhex('0x1.2000000000000p+2'),'GAMMA0':float.fromhex('0x1.9db22d0e56042p-4'),'TWO':float.fromhex('0x1.0000000000000p+1')},'neighbor':{'J_R':float.fromhex('-0x1.27f25920ff61cp+2'),'J_I':float.fromhex('-0x1.0bd3ac99df99bp+0'),'M_R':float.fromhex('0x1.091227715674ep+0'),'M_I':float.fromhex('0x1.f9285830389f2p-2'),'OMEGA0':float.fromhex('0x1.2100000000000p+2'),'GAMMA0':float.fromhex('0x1.9db22d0e56042p-4'),'TWO':float.fromhex('0x1.0000000000000p+1')}}
CENTERS={'original':F(9,2),'neighbor':F(289,64)}
RHO=F(17,2000)
CENTER_GAMMA=F(101,1000)
GAMMA_LOWER=F(401,4000)
GAMMA_UPPER=F(203,2000)
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
