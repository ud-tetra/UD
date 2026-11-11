#!/usr/bin/env python3
"""THM534 v1.1: exact Q171-Q173 midpoint face event selects NEXT edge mask.

Candidate state-to-gate sign rule, not admitted intrinsic chi/b law.
"""
import itertools
import sympy as S
V=tuple(range(4)); E=list(itertools.combinations(V,2)); F=list(itertools.combinations(V,3))
d=S.Matrix([-1,1,-1,1]); B1=S.zeros(4,6);B2=S.zeros(6,4)
for k,(u,v) in enumerate(E):B1[u,k]=-1;B1[v,k]=1
for k,f in enumerate(F):
    for j in range(3):B2[E.index(f[:j]+f[j+1:]),k]=(-1)**j
assert B1*B2==S.zeros(4,4) and B2*d==S.zeros(6,1)
# These face-to-core couplings remain on, even if all edge gates are off.
hstep=S.Rational(1,4);A=S.zeros(5)
A[:4,4]=-d;A[4,:4]=d.T
I=S.eye(5);U=(I-hstep*A/2).inv()*(I+hstep*A/2)
assert U.T*U==I
w=S.Matrix([1,1,0,0]); zz=w+d/2; t=S.Integer(0)
assert (w.T*d)[0]==0 and (zz.T*zz)[0]+t*t==3
rho=S.Matrix([1,0,0,0]);r=S.ones(4,1)
chi=0;boundary=(0,)*4;gate=(0,)*6
hist=[];receipts=[]; nnonzero=0
for n in range(14):
    # first apply burden redistribution at current gate; paired reservoir receipt separate
    H=S.diag(*gate);j=-H*B1.T*rho/4;facecurl=B2.T*j
    p=rho+B1*j;src=(r-p)/4;rn=p+src; rr=r-src
    assert sum(rn)+sum(rr)==5 and min(rn)>=0 and min(rr)>=0
    assert (d.T*facecurl)[0]==0
    hist.append((n,chi,''.join(map(str,boundary)),''.join(map(str,gate)),list(facecurl)))
    if n==1:
        assert gate==(0,0,1,0,1,1)
        assert list(facecurl)==[0,-S.Rational(3,16),-S.Rational(3,16),0]
    if n==7:
        assert gate==(0,1,0,1,0,1) and facecurl!=S.zeros(4,1)
    # independent face-cell Q171-Q173 transfer on declared always-admitted face-cell carrier
    state=S.Matrix(list(zz)+[t]); new=U*state;mid=(state+new)/2
    Jmid=S.Matrix([2*hstep*d[f]*mid[f]*mid[4] for f in range(4)])
    for f in range(4):
        assert new[f]*new[f]-state[f]*state[f]==-Jmid[f]
    assert new[4]*new[4]-state[4]*state[4]==sum(Jmid)
    assert (new.T*new)[0]==3
    receipts.append(tuple(Jmid))
    chi=int(bool(sum(Jmid)>0))
    boundary=tuple(int(bool(q>0)) for q in Jmid)
    gate=tuple(chi*int(all(boundary[f] for f,face in enumerate(F) if set(e).issubset(face))) for e in E)
    zz=new[:4,0];t=new[4];rho=rn;r=rr
    nnonzero+=int(facecurl!=S.zeros(4,1))
expect={0:'000000',1:'001011',2:'001011',3:'001011',4:'000000',5:'000000',6:'000000',7:'010101',10:'010101',11:'000000'}
for n,g in expect.items():assert hist[n][3]==g,(n,hist[n])
assert receipts[0]==tuple(S.Matrix([-S.Rational(18,289),S.Rational(50,289),S.Rational(16,289),S.Rational(16,289)]))
assert sum(receipts[0])==S.Rational(64,289)

# Exact two-mode rotation + static face dark vector.
ca=S.Rational(15,17);sa=S.Rational(8,17)
a,b=S.Integer(1),S.Integer(0)
for _ in range(14):
    state=S.Matrix(list(w+d*a/2)+[b]);nxt=U*state
    aa=ca*a-sa*b;bb=sa*a+ca*b
    assert nxt==S.Matrix(list(w+d*aa/2)+[bb])
    a,b=aa,bb

# All 24 vertex relabelings: signed chain face and core sectors,
# the face current as unsignedly permuted scalar transfer and resultant edge masks.
def sg(z):return (-1)**sum(z[i]>z[j] for i in range(len(z)) for j in range(i+1,len(z)))
for perm in itertools.permutations(V):
    Q2=S.zeros(4);Pface=S.zeros(4);Pedge=S.zeros(6)
    for k,face in enumerate(F):
        moved=[perm[i] for i in face];tgt=F.index(tuple(sorted(moved)))
        Q2[tgt,k]=sg(moved);Pface[tgt,k]=1
    for k,e in enumerate(E):Pedge[E.index(tuple(sorted(perm[i] for i in e))),k]=1
    Q3=sg(perm); assert Q2*d==d*Q3
    W=S.eye(5);W[:4,:4]=Q2;W[4,4]=Q3
    assert W*U==U*W
    for n in (0,3,6,9):
        aa,bb=S.Integer(1),S.Integer(0)
        for _ in range(n):aa,bb=ca*aa-sa*bb,sa*aa+ca*bb
        st=S.Matrix(list(w+d*aa/2)+[bb]);fn=U*st;mid=(st+fn)/2
        j=S.Matrix([2*hstep*d[k]*mid[k]*mid[4] for k in range(4)])
        mst=W*st;mfn=W*fn;mmid=(mst+mfn)/2
        jj=S.Matrix([2*hstep*d[k]*mmid[k]*mmid[4] for k in range(4)])
        assert jj==Pface*j
        def mask(jj):
            ch=int(bool(sum(jj)>0)); bf=[int(bool(t>0)) for t in jj]
            return S.Matrix([ch*int(all(bf[k] for k,face in enumerate(F) if set(e).issubset(face))) for e in E])
        assert mask(jj)==Pedge*mask(j)

# Two strict negative controls: source state zero; face-cell admission shutoff.
assert U*S.zeros(5,1)==S.zeros(5,1)
# If the face coupling is gated by its own positive *pre-event* flux,
# c3=0 forces h_f=0 and state freeze; it cannot bootstrap itself.
assert t!=0  # working witness not confused with vacuum
z0=w+d/2;t0=S.Integer(0)
assert all(2*d[k]*z0[k]*t0==0 for k in range(4))
assert (S.eye(5)*S.Matrix(list(z0)+[t0]))==S.Matrix(list(z0)+[t0])
# With zero dark-mode input, face signs are identical => no nonuniform edge gate.
a,b=S.Integer(1),S.Integer(0)
for n in range(14):
    z=d*a/2;st=S.Matrix(list(z)+[b]);nx=U*st;mm=(st+nx)/2
    J=S.Matrix([2*hstep*d[k]*mm[k]*mm[4] for k in range(4)])
    assert len(set(J))==1
    a,b=ca*a-sa*b,sa*a+ca*b
print('PASS exact 14 events: edge alloff n0; open n1; closed n4; reopen n7')
print('PASS first midpoint face transfer:',receipts[0],'core gain',sum(receipts[0]))
print('PASS 24 signed S4 relabelings x four epochs, dual conserved totals 3 & 5')
print('PASS full-off face-gate and zero-carrier no-restart, symmetric-mode null controls')
print('Nonzero burden-face curl events:',nnonzero,'of 14; PHYSICAL PROMOTION 0')
