#!/usr/bin/env python3
"""THM-534 v1.1 independent-method Fraction exact event-receipt replay.
Same constructor, independent implementation; no outside review.
"""
from fractions import Fraction as R
from itertools import combinations
E=list(combinations(range(4),2));F=list(combinations(range(4),3));d=(-1,1,-1,1);w=(1,1,0,0)
a,t=R(1),R(0)
rho=(R(1),R(0),R(0),R(0));reserve=(R(1),)*4
mask=(0,)*6;hist=[];first=None
for n in range(14):
    hist.append(''.join(map(str,mask)))
    cur=[-R(mask[k],4)*(rho[v]-rho[u]) for k,(u,v) in enumerate(E)]
    edgeflow=[cur[E.index((b,c))]-cur[E.index((a,c))]+cur[E.index((a,b))] for a,b,c in F]
    assert -edgeflow[0]+edgeflow[1]-edgeflow[2]+edgeflow[3]==0
    p=list(rho)
    for k,(u,v) in enumerate(E):p[u]-=cur[k];p[v]+=cur[k]
    src=[(reserve[k]-p[k])/4 for k in range(4)]
    rnew=tuple(p[k]+src[k] for k in range(4))
    reserve_new=tuple(reserve[k]-src[k] for k in range(4))
    assert sum(rnew)+sum(reserve_new)==5 and min(rnew+reserve_new)>=0
    if n==1:assert edgeflow==[R(0),R(-3,16),R(-3,16),R(0)]
    if n==7:assert edgeflow!=[R(0)]*4
    # Exact face/core Cayley step in 2D active mode plus static dark face w.
    za=tuple(w[f]+R(d[f],2)*a for f in range(4))
    aa=R(15,17)*a-R(8,17)*t
    tt=R(8,17)*a+R(15,17)*t
    zz=tuple(w[f]+R(d[f],2)*aa for f in range(4))
    midz=tuple((za[f]+zz[f])/2 for f in range(4));midt=(t+tt)/2
    receipt=tuple(R(1,2)*d[f]*midz[f]*midt for f in range(4))
    assert tuple(zz[f]**2-za[f]**2 for f in range(4))==tuple(-i for i in receipt)
    assert tt*tt-t*t==sum(receipt)
    assert sum(q*q for q in zz)+tt*tt==3
    if n==0:
        first=receipt
        assert first==(R(-18,289),R(50,289),R(16,289),R(16,289))
    chi=int(sum(receipt)>0)
    bf=[int(q>0) for q in receipt]
    mask=tuple(chi*int(all(bf[f] for f,face in enumerate(F) if set(e).issubset(face))) for e in E)
    a,t=aa,tt;rho, reserve=rnew,reserve_new
expect={0:'000000',1:'001011',2:'001011',3:'001011',4:'000000',5:'000000',6:'000000',7:'010101',10:'010101',11:'000000'}
for n,g in expect.items():assert hist[n]==g,(n,hist[n])
print('PASS pure Fraction 14-step actual midpoint face receipts, delayed edge permissions')
print('PASS n0 all-off, n1 open, n4 closed, n7 reopen; 3 and 5 typed totals conserved')
print('PASS first face receipt',first,'core stock gain',sum(first))
print('Governance: candidate sign rule, h_face=1 supplied; no global all-off reset')
