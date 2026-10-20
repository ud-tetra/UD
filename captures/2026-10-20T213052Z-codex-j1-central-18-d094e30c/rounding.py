"""Integer-only rational oracle for binary64 round-to-nearest, ties-to-even."""
import struct
from fractions import Fraction as F

def bits(x):return struct.unpack('>Q',struct.pack('>d',x))[0]
def frombits(n):return struct.unpack('>d',struct.pack('>Q',n))[0]
def pow2(e):return F(2**e) if e>=0 else F(1,2**(-e))
def round64(x):
 x=F(x);sgn=int(x<0);x=abs(x)
 if x==0:return 0.0
 e=x.numerator.bit_length()-x.denominator.bit_length()
 if x<pow2(e):e-=1
 assert pow2(e)<=x<pow2(e+1)
 unit=pow2(max(e-52,-1074));y=x/unit;n,r=divmod(y.numerator,y.denominator)
 if 2*r>y.denominator or (2*r==y.denominator and n%2):n+=1
 if e<-1022:
  assert n<=2**52
  word=(sgn<<63)|n
 else:
  if n==2**53:n//=2;e+=1
  if e>1023:raise OverflowError('binary64 oracle overflow')
  assert 2**52<=n<2**53
  word=(sgn<<63)|((e+1023)<<52)|(n-2**52)
 return frombits(word)
