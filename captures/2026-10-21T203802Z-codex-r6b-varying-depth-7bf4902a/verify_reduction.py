#!/usr/bin/env python3
"""Fresh exact-arithmetic verifier; does not import or execute recovered code."""
from fractions import Fraction as F
from decimal import Decimal, localcontext
import json
from pathlib import Path


def run():
    eta=F(185,192); delta=1-eta
    a,b=eta**4,eta**6
    v={h:delta*(1-eta**h) for h in (2,3,4)}
    c={h:eta**2*delta*(1-eta**h)*(eta**h-eta**(2*h)) for h in v}
    r={h:4*eta**2+v[h] for h in v}
    depth=[]; parity=[]
    for i in range(64):
        digits=[0,i//16,(i//4)%4,i%4]
        depth.append(next((k+1 for k,d in enumerate(digits) if d),4))
        parity.append((-1)**sum(digits))
    hs=[depth[4*g] for g in range(16)]
    assert all(depth[i]==hs[i//4] for i in range(64))
    assert [hs.count(h) for h in (2,3,4)]==[12,3,1]
    H=[[F(0) for _ in range(128)] for _ in range(128)]
    for i in range(64):
        H[i][i]+=v[depth[i]]
        H[i][64+i]=H[64+i][i]=parity[i]*c[depth[i]]
        for j in range(i+1,64):
            if i//4==j//4:
                w=eta**2; offset=0
            else:
                w=a if i//16==j//16 else b; offset=64
            H[offset+i][offset+i]+=w; H[offset+j][offset+j]+=w
            H[offset+i][offset+j]-=w; H[offset+j][offset+i]-=w
    L=[[F(0) for _ in range(16)] for _ in range(16)]
    for g in range(16):
        for j in range(16):
            L[g][j]=12*a+48*b if g==j else -4*(a if g//4==j//4 else b)
        assert sum(L[g])==0
    K=[[F(0) for _ in range(32)] for _ in range(32)]
    for g,h in enumerate(hs):
        K[g][g]=r[h]; K[g][16+g]=K[16+g][g]=c[h]
        for j in range(16): K[16+g][16+j]=L[g][j]
    # Each row of B=2Q has one nonzero; columns have squared norm 4.
    cols=[i//4 for i in range(64)]+[16+i//4 for i in range(64)]
    signs=parity+[1]*64
    gram=[sum(signs[i]**2 for i in range(128) if cols[i]==j) for j in range(32)]
    assert gram==[4]*32
    checked=0
    for i in range(128):
        hb=[F(0)]*32
        for j in range(128): hb[cols[j]]+=H[i][j]*signs[j]
        assert hb==[signs[i]*x for x in K[cols[i]]]
        checked+=32
    # Exact spectral decomposition of the 16-coordinate Theta quotient.
    E=lambda n:[[F(int(i//n==j//n),n) for j in range(16)] for i in range(16)]
    E1,E4,E16=E(1),E(4),E(16)
    for i in range(16):
        for j in range(16):
            assert L[i][j]==64*b*(E4[i][j]-E16[i][j])+(16*a+48*b)*(E1[i][j]-E4[i][j])
    gamma=64*b
    g0=12*a+48*b
    M=max(c[h]**2/r[h] for h in hs)
    m=min(c[h]**2/(r[h]+M) for h in hs)
    eps=(M-m)/(2*(gamma-M))
    excess=4*eps**2*(1+2*eps)**2
    margin=g0-2*max(c.values())**2/min(v.values())
    assert gamma>M>m>0 and eps<1 and margin>min(v.values())/2
    # Uniformity is impossible throughout the entire certified root interval.
    ordering=[c[4]**2/(r[4]+M)-c[3]**2/r[3],c[3]**2/(r[3]+M)-c[2]**2/r[2]]
    assert min(ordering)>0
    assert excess<F(1,10**17)
    values={'eta':eta,'a':a,'b':b,'gamma':gamma,'complement_theta_stiffness':g0,
            'complement_theta_margin':margin,'v_min_half':min(v.values())/2,
            'M':M,'m':m,'epsilon':eps,'F_within_excess_upper':excess,
            'strict_order_margin_43':ordering[0],'strict_order_margin_32':ordering[1]}
    with localcontext() as ctx:
        ctx.prec=65
        decimal={k:str(Decimal(x.numerator)/Decimal(x.denominator)) for k,x in values.items()}
    return {'status':'PASS','arithmetic':'fractions.Fraction; decimal displays only',
            'scope':'EXACT CONDITIONAL on rational clean L=4 R6b source model and identity metric',
            'physical_promotion':0,'depth_group_counts':{'2':12,'3':3,'4':1},
            'embedding_shape':[128,32],'HB_equals_BK_entries_checked':checked,
            'B_transpose_B':'4 I_32; disjoint supports',
            'theta_quotient_eigenvalues':{'0':1,'64b':3,'16a+48b':12},
            'rational':{k:str(x) for k,x in values.items()},'decimal':decimal,
            'bounds':{'lambda':'-M <= lambda <= -m < 0',
                      'theta_profile':'0 < F_within - 1 <= F_within_excess_upper < 1e-17'},
            'negative_eigenvalue_count_in_module':1,
            'proof_dependency':'THEOREM.md; inequalities checked here, analytical implications require review'}

if __name__=='__main__':
    result=run()
    Path(__file__).with_name('CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'decimal':result['decimal']},indent=2))
