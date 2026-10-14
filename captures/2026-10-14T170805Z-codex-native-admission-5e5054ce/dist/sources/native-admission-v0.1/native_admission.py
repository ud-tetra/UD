"""Exact spectrum-admission relaxation. Optimized scale is a comparison variable, not native prediction."""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
import math

@dataclass(frozen=True)
class Radical:
    a:F=F(0)
    b:F=F(0)
    D:int=15
    def __post_init__(self):
        object.__setattr__(self,'a',F(self.a));object.__setattr__(self,'b',F(self.b))
        if self.D not in [10,15]:raise ValueError('Declared positive nonsquare field required.')
    def cast(self,x):
        if isinstance(x,Radical):
            if self.D!=x.D:raise ValueError('Mixed radical fields.')
            return x
        return Radical(x,0,self.D)
    def __add__(self,x):
        x=self.cast(x);return Radical(self.a+x.a,self.b+x.b,self.D)
    __radd__=__add__
    def __neg__(self):return Radical(-self.a,-self.b,self.D)
    def __sub__(self,x):return self+-self.cast(x)
    def __rsub__(self,x):return self.cast(x)+-self
    def __mul__(self,x):
        x=self.cast(x);return Radical(self.a*x.a+self.D*self.b*x.b,self.a*x.b+self.b*x.a,self.D)
    __rmul__=__mul__
    def __truediv__(self,x):
        x=self.cast(x);den=x.a*x.a-self.D*x.b*x.b
        if not den:raise ZeroDivisionError()
        return self*Radical(x.a/den,-x.b/den,self.D)
    def __rtruediv__(self,x):return self.cast(x)/self
    def sign(self):
        if not self.b:return (self.a>0)-(self.a<0)
        if not self.a:return (self.b>0)-(self.b<0)
        if self.a>0 and self.b>0:return 1
        if self.a<0 and self.b<0:return -1
        cmp=(self.a*self.a>self.D*self.b*self.b)-(self.a*self.a<self.D*self.b*self.b)
        return cmp if self.a>0 else -cmp
    def __lt__(self,x):return (self-self.cast(x)).sign()<0
    def __le__(self,x):return (self-self.cast(x)).sign()<=0
    def __abs__(self):return -self if self.sign()<0 else self
    def __float__(self):return float(self.a)+float(self.b)*math.sqrt(self.D)
    def exact(self):
        if not self.b:return str(self.a)
        return f'{self.a} + ({self.b}) sqrt({self.D})'
    def json(self):return {'rational':str(self.a),'sqrt_coefficient':str(self.b),'radicand':self.D,'exact':self.exact(),'decimal_display':float(self)}

CLASSES={
 'tetra':{'name':'Filled tetrahedron','dimension':15,'squared_positive_frequencies':[4],'positive_multiplicities':[7],'scale_rule':'high centre y=2 gamma/kappa'},
 'minus':{'name':'K-minus','dimension':23,'squared_positive_frequencies':[3,5],'positive_multiplicities':[4,7],'scale_rule':'high centre y=sqrt(5) gamma/kappa'},
 'plus':{'name':'K-plus','dimension':27,'squared_positive_frequencies':[2,5],'positive_multiplicities':[2,11],'scale_rule':'high centre y=sqrt(5) gamma/kappa'}}

def optimize(n,carrier):
    if type(n) is not int or n<2 or n%2:raise ValueError('Even padded clock length≥2 required.')
    if carrier not in CLASSES:raise ValueError('Unknown declared spectral class.')
    m=n//2;D=15 if carrier!='plus' else 10;zero=Radical(0,0,D)
    ratio=Radical(0,F(1,5),D) if carrier!='tetra' else None
    rows=[]
    for k in range(m+1):
        for l in ([0] if carrier=='tetra' else range(m-k+1)):
            low=list(range(2*(k+1),2*(k+l)+1,2));high=list(range(2*(k+l+1),n+1,2))
            bounds=[zero.cast(2*k)];constraints=[]
            if low:bounds.append(zero.cast(F(low[-1]-low[0],2)))
            if high:bounds.append(zero.cast(F(high[-1]-high[0],2)))
            if low and high:bounds.extend([(low[-1]-ratio*high[0])/(1+ratio),(ratio*high[-1]-low[0])/(1+ratio)])
            delta=max(bounds);lower=[zero];upper=[]
            if low:lower.append((low[-1]-delta)/ratio);upper.append((low[0]+delta)/ratio)
            if high:lower.append(high[-1]-delta);upper.append(high[0]+delta)
            lo=max(lower);hi=min(upper) if upper else None
            assert hi is None or lo<=hi
            y=lo;centres=[zero]+([ratio*y] if ratio else [])+[y]
            target=list(range(2,n+1,2));nearest=[min(abs(p-c) for c in centres) for p in target]
            assert max(nearest)<=delta
            rows.append({'zero_count':k,'low_count':l,'bound':delta,'high_centre_min':lo,'high_centre_max':hi})
    best=min(r['bound'] for r in rows);ties=[r for r in rows if r['bound']==best]
    intervals=[]
    for r in sorted(ties,key=lambda r:r['high_centre_min']):
        lo=r['high_centre_min'];hi=r['high_centre_max']
        assert hi is not None # The zero-only partition cannot beat a nonzero centre.
        if intervals and lo<=intervals[-1][1]:intervals[-1]=(intervals[-1][0],max(hi,intervals[-1][1]))
        else:intervals.append((lo,hi))
    return {'carrier':carrier,'clock_word_length':n,'minimum_relative_spectral_floor':best.json(),
      'optimal_high_centre_intervals':[{'min':lo.json(),'max':hi.json()} for lo,hi in intervals],'ratio_low_to_high':ratio.json() if ratio else None,
      'partition_certificates':[{'zero_count':r['zero_count'],'low_count':r['low_count'],'bound':r['bound'].json(),'high_centre_min':r['high_centre_min'].json(),'high_centre_max':r['high_centre_max'].json() if r['high_centre_max'] is not None else None,'high_centre_unbounded':r['high_centre_max'] is None} for r in rows],
      'comparison_scope':'Free common rate and unrestricted isometry with sufficient identical copies; source-selected metric, rate, encoding, locality and state admission are not established.',
      'physical_promotion':0}

def native_generator(carrier):
    tops={'tetra':[(0,1,2,3)],'minus':[(0,1,2,3),(0,1,2,4)],'plus':[(0,1,3,4),(0,2,3,4),(1,2,3,4)]}[carrier]
    sim=sorted({s for t in tops for k in range(1,5) for s in combinations(t,k)},key=lambda s:(len(s),s));idx={s:i for i,s in enumerate(sim)};d=len(sim)
    b=[[0]*d for _ in range(d)]
    for s,j in idx.items():
        if len(s)>1:
            for q in range(len(s)):b[idx[s[:q]+s[q+1:]]][j]=(-1)**q
    a=[[b[j][i]-b[i][j] for j in range(d)] for i in range(d)]
    return sim,b,a

if __name__=='__main__':
    import json
    from pathlib import Path
    p=Path(__file__).parent/'dist/sources/native-admission-v0.1';p.mkdir(parents=True,exist_ok=True)
    out={'version':'0.1','physical_promotion':0,'native_classes':CLASSES,'clock_lengths':[2,4,6,8,10,12],
      'comparisons':[optimize(n,c) for n in [2,4,6,8,10,12] for c in CLASSES],
      'default_clock_word_length':10,'scope':'Exact radical nearest-spectrum lower certificates. These are generator residual bounds, not endpoint error lower bounds or physical parameter fits.'}
    (p/'NATIVE_SPECTRAL_CERTIFICATES_v0.1.json').write_text(json.dumps(out,indent=2)+'\n')
