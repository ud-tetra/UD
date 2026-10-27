"""Outward rational interval helpers from the v2.22 constructor certificate."""
from fractions import Fraction as Q
from math import isqrt,factorial
GRID=10**24
def down(x):return Q((x.numerator*GRID)//x.denominator,GRID)
def up(x):return -down(-x)
class I:
    def __init__(self,a,b=None):
        self.lo=Q(a);self.hi=Q(a if b is None else b)
        assert self.lo<=self.hi
    def __add__(self,y):
        y=as_i(y);return I(down(self.lo+y.lo),up(self.hi+y.hi))
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,y):return self+-as_i(y)
    def __rsub__(self,y):return as_i(y)+-self
    def __mul__(self,y):
        y=as_i(y);a=[x*z for x in (self.lo,self.hi) for z in (y.lo,y.hi)]
        return I(down(min(a)),up(max(a)))
    __rmul__=__mul__
    def __truediv__(self,y):
        y=as_i(y);assert y.lo*y.hi>0
        return self*I(down(1/y.hi),up(1/y.lo))
    def __pow__(self,n):
        assert type(n)==int and n>=0
        r=I(1)
        for _ in range(n):r=r*self
        return r
def as_i(x):return x if isinstance(x,I) else I(x)
def sqrt_q(x):
    x=Q(x);assert x>=0
    s=isqrt((x.numerator*GRID*GRID)//x.denominator)
    return I(Q(s,GRID),Q(s+1,GRID))
def sqrt_i(x):return I(sqrt_q(x.lo).lo,sqrt_q(x.hi).hi)
def atan_small(q,n):
    q=Q(q);assert 0<q<1
    a=sum((-1)**j*q**(2*j+1)/Q(2*j+1) for j in range(n))
    b=a+(-1)**n*q**(2*n+1)/Q(2*n+1)
    return I(down(min(a,b)),up(max(a,b)))
def sin_i(x):
    x=as_i(x);r=I(0);n=14
    for j in range(n):r+=(-1)**j*(x**(2*j+1))/factorial(2*j+1)
    err=max(abs(x.lo),abs(x.hi))**(2*n+1)/factorial(2*n+1)
    return r+I(-err,err)
def cos_i(x):
    x=as_i(x);r=I(0);n=14
    for j in range(n):r+=(-1)**j*(x**(2*j))/factorial(2*j)
    err=max(abs(x.lo),abs(x.hi))**(2*n)/factorial(2*n)
    return r+I(-err,err)
def box(x,den=10**15):
    return [str(Q((x.lo.numerator*den)//x.lo.denominator,den)),
            str(Q(-((-x.hi.numerator*den)//x.hi.denominator),den))]
