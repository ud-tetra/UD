#!/usr/bin/env python3
"""Matrix-free Chebyshev reference recurrence with checked whole-step rounding.

The caller must independently certify g~F^T y and every A-action~F^T F v.
This module checks arithmetic enclosures, NOT the truth of an opaque oracle.
All vectors returned by or supplied to this module are integers times2^-96.
"""
from fractions import Fraction as F
from flint import arb,ctx

S=F(61,27648)
STATE_BITS=96
STATE_SCALE=2**STATE_BITS
LOCAL_U=F(1,2**67)
COORD_ERROR=F(1,2**80)
MAX_DIM=2640

def ball(q):
 q=F(q);return arb(q.numerator)/q.denominator

def checked_quantize(value):
 """Round an enclosing ball; certify true whole-expression coordinate defect."""
 k=(value*STATE_SCALE).mid().floor().unique_fmpz()
 if k is None:raise ArithmeticError('nonfinite or undecidable arithmetic enclosure')
 k=int(k)
 if not abs(value-ball(F(k,STATE_SCALE)))<ball(COORD_ERROR):
  raise ArithmeticError('whole-step coordinate error exceeds certified allowance')
 return k

def decode_from_adjoint(g_ints,normal_action,steps=8192):
 """Return dyadic output and arithmetic receipt; g/A truth is a caller obligation.

Required: ||y||<=2, ||g-F^Ty||<=2^-67, and each action has absolute
error<=2^-67 on ||v||<=2048. No unit-vector-only claim suffices.
The actual fixed map must have nonzero singular values in[S,1].
"""
 ctx.prec=192
 if steps<1 or not 1<=len(g_ints)<=MAX_DIM:raise ValueError('unsupported shape/step count')
 if any(type(v) is not int for v in g_ints):raise TypeError('g must use exact integer dyadics')
 n=len(g_ints)
 if sum(v*v for v in g_ints)>(3*STATE_SCALE)**2:raise ValueError('g outside declared bounded domain')
 assert n*COORD_ERROR**2<LOCAL_U**2
 a=S*S;c=(1+a)/2;d=(1-a)/2;sigma=ball(c/d);rho=ball(d/c)
 x0=[0]*n;x1=[checked_quantize(ball(F(v,STATE_SCALE))/ball(c))for v in g_ints]
 checked=n;calls=0
 def domain(v):
  if sum(t*t for t in v)>(2048*STATE_SCALE)**2:raise ValueError('iterate exceeds certified action domain')
 domain(x1)
 for k in range(1,steps):
  av=normal_action(tuple(x1));calls+=1
  if len(av)!=n or any(type(v) is not int for v in av):raise TypeError('normal action must return integer dyadics of matching dimension')
  nxt=1/(2*sigma-rho)
  if not (nxt>0 and nxt<1 and 2*nxt/ball(d)<5):raise ArithmeticError('coefficient enclosure lost')
  momentum=nxt*rho;stepfactor=2*nxt/ball(d)
  x2=[checked_quantize(ball(F(u,STATE_SCALE))+momentum*ball(F(u-v,STATE_SCALE))+stepfactor*ball(F(g-w,STATE_SCALE)))for u,v,g,w in zip(x1,x0,g_ints,av)]
  checked+=n;domain(x2);x0,x1=x1,x2;rho=nxt
 return x1,{'status':'PASS_WHOLE_STEP_ARITHMETIC_ENCLOSURES','steps':steps,'state_dimension':n,'normal_action_calls':calls,'whole_step_coordinates_checked':checked,'coefficient_precision_bits':192,'state_dyadic_bits':96,'whole_update_arithmetic_defect':'<2^-67','oracle_truth':'CALLER_OBLIGATION_NOT_VERIFIED_BY_THIS_MODULE','actual_600cell_admission':'NOT_ESTABLISHED_BY_THIS_MODULE'}

def decode(data_ints,adjoint_action,normal_action,steps=8192):
 """Decode a dyadic normalized data vector using caller-certified action oracles.

Data have norm<=2; the callbacks' exact mathematical identities and absolute
error contracts remain caller obligations. Arithmetic checks are internal.
"""
 if not 1<=len(data_ints)<=253952 or any(type(v)is not int for v in data_ints):
  raise ValueError('data must be a supported exact integer dyadic vector')
 if sum(v*v for v in data_ints)>(2*STATE_SCALE)**2:
  raise ValueError('normalized data exceed certified norm2 domain')
 g=adjoint_action(tuple(data_ints))
 answer,receipt=decode_from_adjoint(g,normal_action,steps)
 receipt.update(adjoint_action_calls=1,data_dimension=len(data_ints),data_norm_bound=2)
 return answer,receipt
