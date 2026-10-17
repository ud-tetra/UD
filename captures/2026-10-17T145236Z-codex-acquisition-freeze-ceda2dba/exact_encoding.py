"""Exact fixed-point encoders. Input is a rational pair, never binary floating point."""
import struct
from fractions import Fraction as F
from audit_run import exact
def quantize(value,bits):
 x=exact(value);q,r=divmod(x.numerator*2**bits,x.denominator)
 if 2*r>x.denominator or (2*r==x.denominator and q%2):q+=1
 assert abs(F(q,2**bits)-x)<=F(1,2**(bits+1))
 return q
def history_bytes(value):
 q=quantize(value,48)
 if not -(2**63)<=q<2**63:raise ValueError('No clipping: signedint64 overflow')
 return struct.pack('<q',q)
def diagnostic_record(value):
 return {'numerator_decimal':str(quantize(value,64)),'denominator_pow2':64}
