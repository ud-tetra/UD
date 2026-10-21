#!/usr/bin/env python3
"""Exact rational embedding, inertia, root bisection and interval channel receipt."""
from fractions import Fraction as F
from decimal import Decimal, localcontext
from pathlib import Path
import json

class I:
    def __init__(self,lo,hi=None):
        self.lo=F(lo); self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,o):
        o=o if isinstance(o,I) else I(o)
        return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+-as_i(o)
    def __rsub__(self,o): return as_i(o)+-self
    def __mul__(self,o):
        o=as_i(o); p=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)]
        return I(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=as_i(o); assert not o.lo<=0<=o.hi
        return self*I(1/o.hi,1/o.lo)
    def square(self):
        return I(0 if self.lo<=0<=self.hi else min(self.lo**2,self.hi**2),max(self.lo**2,self.hi**2))

def as_i(o):return o if isinstance(o,I) else I(o)
def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
            -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))

def run():
    eta=F(185,192); delta=1-eta; a,b=eta**4,eta**6
    hs=[4,3,2]; n=[1,3,12]
    v=[delta*(1-eta**h) for h in hs]
    c=[eta**2*delta*(1-eta**h)*(eta**h-eta**(2*h)) for h in hs]
    r=[4*eta**2+z for z in v]
    A=[[12*a+48*b,-12*a,-48*b],[-4*a,4*a+48*b,-48*b],[-4*b,-12*b,16*b]]
    K=[[F(0) for _ in range(6)] for _ in range(6)]
    for j in range(3):
        K[j][j]=r[j]; K[j][3+j]=K[3+j][j]=c[j]
        for k in range(3): K[3+j][3+k]=A[j][k]
    metric=n+n
    assert all(metric[i]*K[i][j]==metric[j]*K[j][i] for i in range(6) for j in range(6))
    H=[[F(0) for _ in range(128)] for _ in range(128)]
    depth=[]; parity=[]
    for i in range(64):
        digits=[0,i//16,(i//4)%4,i%4]
        depth.append(next((j+1 for j,d in enumerate(digits) if d),4))
        parity.append((-1)**sum(digits))
    for i in range(64):
        k=hs.index(depth[i]); H[i][i]+=v[k]
        H[i][64+i]=H[64+i][i]=parity[i]*c[k]
        for j in range(i+1,64):
            offset,w=(0,eta**2) if i//4==j//4 else (64,a if i//16==j//16 else b)
            H[offset+i][offset+i]+=w; H[offset+j][offset+j]+=w
            H[offset+i][offset+j]-=w; H[offset+j][offset+i]-=w
    cols=[hs.index(h) for h in depth]+[3+hs.index(h) for h in depth]
    signs=parity+[1]*64
    assert [cols.count(j) for j in range(6)]==[4*z for z in metric]
    for i in range(128):
        hb=[F(0)]*6
        for j in range(128):hb[cols[j]]+=H[i][j]*signs[j]
        assert hb==[signs[i]*z for z in K[cols[i]]]
    # Conditions used in the full-module uniqueness proof in THEOREM.md.
    gamma=64*b; g0=12*a+48*b
    M=max(c[j]**2/r[j] for j in range(3))
    assert a>b>0 and gamma>M>0
    assert g0-2*max(c)**2/min(v)>min(v)/2>0
    def schur(lam):
        return [[A[i][j]-(lam+c[i]**2/(r[i]-lam) if i==j else 0)
                 for j in range(3)] for i in range(3)]
    lo=-M; hi=F(0)
    assert det3(schur(lo))>0 and det3(schur(hi))<0
    for _ in range(160):
        mid=(lo+hi)/2; d=det3(schur(mid))
        assert d!=0,'exact midpoint root needs separate receipt'
        if d>0:lo=mid
        else:hi=mid
    assert hi-lo<F(1,10**55)
    # Ground Theta amplitudes in order h=4,3,2; fix y4=1.
    lam=I(lo,hi)
    S=[[as_i(A[i][j])-(lam+as_i(c[i]**2)/(as_i(r[i])-lam) if i==j else 0)
        for j in range(3)] for i in range(3)]
    den=S[1][1]*S[2][2]-S[1][2]*S[2][1]
    assert den.lo>0
    y=[I(1),(-S[1][0]*S[2][2]+S[1][2]*S[2][0])/den,
       (-S[1][1]*S[2][0]+S[2][1]*S[1][0])/den]
    assert all(z.lo>0 for z in y)
    x=[-as_i(c[j])*y[j]/(as_i(r[j])-lam) for j in range(3)]
    T=sum(n[j]*y[j].square() for j in range(3))
    R=sum(n[j]*x[j].square() for j in range(3))
    Wr=R/(R+T); Wt=T/(R+T)
    # Stable pairwise-variance identity avoids subtraction of 1.
    excess=sum(n[i]*n[j]*(y[i].square()-y[j].square()).square()
               for i in range(3) for j in range(i+1,3))/T.square()
    assert excess.lo>0 and excess.hi<F(1,10**17)
    assert 0<Wr.lo<Wr.hi<1 and 0<Wt.lo<Wt.hi<1
    assert Wr.hi-Wr.lo<F(1,10**50)
    quantities={'lambda':lam,'W_rho':Wr,'W_Theta':Wt,'F_Theta_within_minus_1':excess,
                'Theta_amplitude_h4':y[0],'Theta_amplitude_h3':y[1],'Theta_amplitude_h2':y[2]}
    # Outward rational quantization keeps certificates compact without losing enclosure.
    scale=10**65
    quantities={k:I(F((z.lo*scale).__floor__(),scale),F((z.hi*scale).__ceil__(),scale)) for k,z in quantities.items()}
    def inside(key,lo,hi):
        z=quantities[key]; assert F(lo)<z.lo<=z.hi<F(hi)
    inside('lambda','-0.000000016145247540177632','-0.000000016145247540177631')
    inside('W_rho','0.0000000043430663967222016','0.0000000043430663967222018')
    inside('W_Theta','0.99999999565693360','0.99999999565693361')
    inside('F_Theta_within_minus_1','5.7515757103508979e-19','5.7515757103508980e-19')
    assert quantities['lambda'].hi-quantities['lambda'].lo<F(1,10**55)
    with localcontext() as ctx:
        ctx.prec=65
        display={k:[str(Decimal(z.numerator)/Decimal(z.denominator)) for z in (v.lo,v.hi)] for k,v in quantities.items()}
    return {'status':'PASS','claim_status':'EXACT CONDITIONAL','lane':'development — no registry entry',
            'physical_promotion':0,'constructor':'Codex','reviewers':[],
            'arithmetic':'stdlib Fraction for all checks, interval operations and 160 bisections; Decimal display only',
            'checks':{'HB_equals_BK_entries':768,'B_transpose_B':'4 diag(1,3,12,1,3,12)',
                      'weighted_self_adjointness':True,'full_module_uniqueness_inequalities':True,
                      'root_endpoint_determinant_signs':['positive','negative'],'root_width_lt':'1e-55',
                      'channel_weight_interval_width_lt':'1e-50','positive_Theta_amplitude_intervals':True},
            'depth_order':hs,'multiplicities':n,'coordinate_matrix':[[str(z) for z in row] for row in K],
            'intervals_exact':{k:{'lower':str(z.lo),'upper':str(z.hi)} for k,z in quantities.items()},
            'decimal_displays_not_outward_rounded':display,
            'dependencies':['rational clean L4 R6b equations','identity site metric','analytical proof in THEOREM.md']}

if __name__=='__main__':
    result=run()
    Path(__file__).with_name('CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'displays':result['decimal_displays_not_outward_rounded']},indent=2))
