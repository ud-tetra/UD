"""Prospective raw recipes ONLY. No function generating raw/noise is called now."""
import hashlib
from fractions import Fraction as F

PROTOCOL_ID='UD_PHASE_PROSPECTIVE_V1_20261019'
SHAPE=(37,8191,62)
QUANTUM=F(1,1<<48)
T_EXPONENT=22
DEN=(1<<44)+1
COS_NUM=(1<<44)-1
SIN_NUM=1<<23

def round_ratio(n,d):
    """Exact nearest-even integer rounding, including negative numerators."""
    assert isinstance(n,int) and isinstance(d,int) and d>0
    q,r=divmod(n,d)
    return q+int(2*r>d or (2*r==d and q%2!=0))

def identity():return [[int(i==j) for j in range(37)] for i in range(37)]
def matmul(A,B):
    # STATIC 37x37 contract arithmetic only; Python arbitrary-precision integers.
    return [[sum(int(A[i][k])*int(B[k][j]) for k in range(37)) for j in range(37)] for i in range(37)]
def cayley_numerator(offset):
    R=[[DEN*int(i==j) for j in range(37)] for i in range(37)]
    for parity in [0,1]:
        g=list(range(parity,37,2));g=g[offset:]+g[:offset]
        for k in range(0,len(g)-1,2):
            i,j=g[k:k+2];R[i][i]=R[j][j]=COS_NUM;R[i][j]=-SIN_NUM;R[j][i]=SIN_NUM
    return R
def seeded_spatial():
    rows=[]
    for a in range(37):
        material=f'{PROTOCOL_ID}|B|spatial|{a}'.encode('ascii');digest=hashlib.sha256(material).digest()
        rows.append({'preparation':a,'channel':int.from_bytes(digest[:8],'little')%62,'sign':1 if digest[8]&1 else -1})
    return rows

class UnresolvedCarrierSign(ArithmeticError):pass
def carrier_sign(kind,argument):
    """FUTURE ONLY: exact rational input; fixed512-bit certified sign or HOLD."""
    from flint import arb,fmpq,ctx
    assert ctx.prec==512,'HOLD_CARRIER_PRECISION_CONTRACT'
    argument=F(argument)
    if argument==0:return 1  # sin(0)=0 gets declared +1; cos(0)>0 also +1.
    value=arb(fmpq(argument.numerator,argument.denominator))
    value=value.sin() if kind=='sin' else value.cos()
    if value>0:return 1
    if value<0:return -1
    raise UnresolvedCarrierSign('HOLD: fixed512-bit carrier sign unresolved; no float sign, epsilon, precision retry or replacement')

def noise_value(case,a,k):
    """FUTURE ONLY: returns(channel,integer noise); no raw record written here."""
    assert 0<=a<37 and 0<=k<8191
    row=case['spatial'][a];assert row['preparation']==a
    kind=case['noise_kind']
    if kind=='zero':return row['channel'],0
    omega=F(*case['carrier_omega'])
    if kind=='ramped_low_sine':
        amplitude=round_ratio(1127*(k-4095),4095)
        if amplitude==0:return row['channel'],0
        sign=carrier_sign('sin',omega*k)
    elif kind=='chirped_high_cosine':
        amplitude=1127;sign=carrier_sign('cos',omega*k+F(k,8191)+F(k*k,8191**2))
    else:raise ValueError('unknown frozen noise kind')
    value=int(row['sign'])*amplitude*sign
    assert abs(value)<=1127
    return row['channel'],value

def nominal_block(baseline,matrix,den,a,start,stop):
    """FUTURE ONLY: ONE rounding of Y0*Tnew^T, never overflow-prone int64 products."""
    import numpy as np
    assert baseline.shape==SHAPE and 0<=a<37 and 0<=start<stop<=8191
    active=[j for j in range(37) if matrix[a][j]];assert len(active)<=2
    result=np.empty((stop-start,62),np.int64)
    for k in range(start,stop):
        for c in range(62):
            numerator=sum(int(matrix[a][j])*int(baseline[j,k,c]) for j in active)
            value=round_ratio(numerator,int(den));assert -(1<<63)<value<(1<<63)
            result[k-start,c]=value
    return result
