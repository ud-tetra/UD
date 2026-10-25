#!/usr/bin/env python3
"""Exact native Lie certificate, invariant split and checkpoint audit."""
from fractions import Fraction as Q
from itertools import combinations,product
from pathlib import Path
import json,hashlib

CELLS=[(0,1,2,3),(0,1,2,4)];ORIENT=[1,-1]
SIMP=[sorted({s for c in CELLS for s in combinations(c,k)}) for k in range(1,5)]
OFF=[0,5,14,21];N=23
def zero(n=N,m=N):return [[Q(0)]*m for _ in range(n)]
def eye(n=N):return [[Q(i==j) for j in range(n)] for i in range(n)]
def add(A,B,a=Q(1),b=Q(1)):return [[a*x+b*y for x,y in zip(r,s)] for r,s in zip(A,B)]
def scale(A,a):return [[a*x for x in r] for r in A]
def trans(A):return list(map(list,zip(*A)))
def mul(A,B):
    C=zero(len(A),len(B[0]))
    for i,row in enumerate(A):
        for k,a in enumerate(row):
            if a:
                for j,b in enumerate(B[k]):
                    if b:C[i][j]+=a*b
    return C
def mv(A,x):return [sum(a*b for a,b in zip(r,x)) for r in A]
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def norm(x):return dot(x,x)
def wedge(x,y):return [[a*d-b*c for c,d in zip(x,y)] for a,b in zip(x,y)]
def unit(i):return [Q(j==i) for j in range(N)]
def solve(A,b):
    rows=[list(r)+[v] for r,v in zip(A,b)]
    for k in range(len(b)):
        p=next(i for i in range(k,len(b)) if rows[i][k]);rows[k],rows[p]=rows[p],rows[k]
        d=rows[k][k];rows[k]=[v/d for v in rows[k]]
        for i in range(len(b)):
            if i!=k and rows[i][k]:
                d=rows[i][k];rows[i]=[a-d*v for a,v in zip(rows[i],rows[k])]
    return [r[-1] for r in rows]
def inverse(A):return trans([solve(A,[Q(i==j) for i in range(len(A))]) for j in range(len(A))])
def rank_vectors(vectors):
    piv={}
    for v in vectors:
        v=list(v)
        for p,row in sorted(piv.items()):
            if v[p]:
                d=v[p];v=[a-d*b for a,b in zip(v,row)]
        p=next((i for i,a in enumerate(v) if a),None)
        if p is not None:
            d=v[p];piv[p]=[a/d for a in v]
    return len(piv)
def boundary(k):
    B=zero(len(SIMP[k-1]),len(SIMP[k]))
    for j,s in enumerate(SIMP[k]):
        for i in range(k+1):B[SIMP[k-1].index(s[:i]+s[i+1:])][j]=Q((-1)**i*(ORIENT[j] if k==3 else 1))
    return B
B1=boundary(1);B2=boundary(2);B3=boundary(3)
def native(h):
    A=zero()
    for k,B in enumerate((B1,B2,B3)):
        for i,r in enumerate(B):
            for j,d in enumerate(r):
                z=d*(h[i] if k==2 else 1);A[OFF[k]+i][OFF[k+1]+j]=-z;A[OFF[k+1]+j][OFF[k]+i]=z
    return A
A0=native([0]*7);G=[add(native([int(i==f) for i in range(7)]),A0,b=-1) for f in range(7)]
OPS=[];MATS=[]
def node(op,M,**args):
    OPS.append({'op':op,**args});MATS.append(M);return len(MATS)-1
def bracket(i,j):return node('bracket',add(mul(MATS[i],MATS[j]),mul(MATS[j],MATS[i]),b=-1),left=i,right=j)
def difference(i,j):return node('subtract',add(MATS[i],MATS[j],b=-1),left=i,right=j)
def times(i,a):return node('scale',scale(MATS[i],a),input=i,value=str(a))
def upper(A):return [A[i][j] for i in range(N) for j in range(i+1,N)]
def hash_matrix(A):return hashlib.sha256(json.dumps([[str(v) for v in r] for r in A],separators=(',',':')).encode()).hexdigest()
def main():
    assert mul(B1,B2)==zero(5,7) and mul(B2,B3)==zero(9,2)
    assert rank_vectors(B1)==4 and rank_vectors(B2)==5 and rank_vectors(B3)==2
    drift=node('native_mask',A0,mask=[0]*7);gids=[]
    for f in range(7):
        a=node('native_mask',native([int(i==f) for i in range(7)]),mask=[int(i==f) for i in range(7)])
        gids.append(difference(a,drift))
    shared=next(f for f,r in enumerate(B3) if all(r));private=next(f for f,r in enumerate(B3) if r[0] and not r[1])
    isolated=bracket(bracket(gids[private],gids[shared]),gids[private])
    other=difference(gids[shared],isolated)
    planes={}
    for idx in [gids[f] for f in range(7) if f!=shared]+[isolated,other]:
        M=MATS[idx];pairs=[(i,j) for i in range(14,23) for j in range(i+1,23) if M[i][j]]
        assert len(pairs)==1;i,j=pairs[0];idx=times(idx,1/M[i][j]);planes[i,j]=idx
    while len(planes)<36:
        changed=False
        for i,j in combinations(range(14,23),2):
            if (i,j) in planes:continue
            for k in range(14,23):
                p=tuple(sorted((i,k)));q=tuple(sorted((k,j)))
                if i!=k!=j and p in planes and q in planes:
                    idx=bracket(planes[p],planes[q]);idx=times(idx,1/MATS[idx][i][j])
                    assert MATS[idx]==wedge(unit(i),unit(j));planes[i,j]=idx;changed=True;break
        assert changed
    columns=[[B2[i][f] for i in range(9)] for f in range(7)];chosen=[]
    for f,v in enumerate(columns):
        if rank_vectors([columns[j] for j in chosen]+[v])>len(chosen):chosen.append(f)
    assert len(chosen)==5
    U=[]
    for f in chosen:U.append([Q(0)]*5+columns[f]+[Q(0)]*9)
    V=U+[unit(i) for i in range(14,23)];basis={}
    for i,j in combinations(range(5,14),2):basis[i,j]=planes[14+i-5,14+j-5]
    cross={}
    for i,f in enumerate(chosen):
        idx=times(bracket(drift,planes[14+f,21]),Q(-1))
        assert MATS[idx]==wedge(U[i],unit(21));cross[i,21]=idx
        for a in range(14,23):
            if a==21:continue
            p=tuple(sorted((21,a)));idx2=bracket(idx,planes[p]);target=wedge(U[i],unit(a))
            pos=next((r,s) for r in range(N) for s in range(N) if target[r][s])
            idx2=times(idx2,target[pos[0]][pos[1]]/MATS[idx2][pos[0]][pos[1]])
            assert MATS[idx2]==target;cross[i,a]=idx2
        for a in range(14,23):basis[i,5+a-14]=cross[i,a]
    for i,j in combinations(range(5),2):
        idx=bracket(cross[i,21],cross[j,21]);target=wedge(U[i],U[j])
        pos=next((r,s) for r in range(N) for s in range(N) if target[r][s])
        idx=times(idx,target[pos[0]][pos[1]]/MATS[idx][pos[0]][pos[1]])
        assert MATS[idx]==target;basis[i,j]=idx
    assert len(basis)==91 and rank_vectors([upper(MATS[i]) for i in basis.values()])==91
    Vm=trans(V);Gram=mul(trans(Vm),Vm);L=mul(inverse(Gram),trans(Vm));P=mul(Vm,L);Pg=add(eye(),P,b=-1)
    assert mul(P,P)==P and P==trans(P) and sum(P[i][i] for i in range(N))==14
    cycle=zero()
    for i,r in enumerate(B2):
        for j,d in enumerate(r):cycle[5+i][14+j]=-d;cycle[14+j][5+i]=d
    grad=add(A0,cycle,b=-1)
    assert mul(grad,P)==zero() and mul(P,grad)==zero()
    for idx in basis.values():assert mul(MATS[idx],Pg)==zero()
    assert rank_vectors([upper(MATS[i]) for i in basis.values()]+[upper(grad)])==92
    # Every native mask belongs to so(active) plus the one common gradient drift.
    for h in product((0,1),repeat=7):
        A=native(h);active=add(A,grad,b=-1)
        assert mul(active,Pg)==zero() and mul(Pg,active)==zero()
    def decompose(S):
        C=mul(mul(L,S),trans(L));rebuild=zero();terms=[]
        for pair,idx in sorted(basis.items()):
            a=C[pair[0]][pair[1]]
            if a:rebuild=add(rebuild,MATS[idx],b=a);terms.append({'basis_node':idx,'coefficient':str(a)})
        assert rebuild==S
        return terms
    cycle_terms=decompose(cycle)
    # Native embedding of all four v2.18 checkpoints, including retained output.
    x=[Q(0)]*23
    for edge,val in [((0,1),-1),((0,2),1),((1,2),-1)]:x[5+SIMP[1].index(edge)]=Q(val)
    c=Q(24,37);feed=14+SIMP[2].index((0,1,4));out=14+SIMP[2].index((0,2,4))
    y=scale([x],Q(3,37))[0]
    for face,val in [((0,1,2),-48),((0,1,3),-20),((0,2,3),20),((1,2,3),-20)]:y[14+SIMP[2].index(face)]=Q(val,37)
    y[21]=c;z=y.copy();z[21]=Q(0)
    p0=x.copy();p0[feed]=c;p1=y.copy();p1[feed]=c
    p2=z.copy();p2[feed]=c;p2[out]=c;p3=x.copy();p3[out]=c
    states=[p0,p1,p2,p3];assert all(norm(v)==norm(p0) and mv(P,v)==v for v in states)
    checkpoint=[]
    for a,b in zip(states,states[1:]):
        q=norm(a);d=dot(a,b);S=scale(wedge(b,a),2/(q+d))
        assert mul(P,S)==S and mul(S,P)==S
        # Exact Cayley action without solving the entire generator word.
        lhs=[b[i]-sum(S[i][j]*b[j] for j in range(N))/2 for i in range(N)]
        rhs=[a[i]+sum(S[i][j]*a[j] for j in range(N))/2 for i in range(N)]
        assert lhs==rhs
        checkpoint.append({'generator_terms':decompose(S),'generator_sha256':hash_matrix(S)})
    owned=[]
    for v in states:
        owned.append([sum(v[OFF[k]+i]**2/sum(set(s)<=set(cell) for cell in CELLS)
             for k,ss in enumerate(SIMP) for i,s in enumerate(ss) if set(s)<=set(tau)) for tau in CELLS])
    assert owned[0]==owned[-1]==[Q(3,2),Q(3,2)+c*c]
    # Exact graph Laplacian spectral projectors: eigenvalues 0,3,5 (multiplicity 1,1,3).
    Lap=mul(B1,trans(B1));ones=[Q(1)]*5;diff=[Q(0),Q(0),Q(0),Q(1),Q(-1)]
    P0=[[a*b/5 for b in ones] for a in ones];P3=[[a*b/2 for b in diff] for a in diff]
    P5=add(add(eye(5),P0,b=-1),P3,b=-1)
    assert Lap==add(scale(P3,Q(3)),scale(P5,Q(5)))
    replay=[]
    for n,op in enumerate(OPS):
        if op['op']=='native_mask':M=native(op['mask'])
        elif op['op']=='subtract':M=add(replay[op['left']],replay[op['right']],b=-1)
        elif op['op']=='scale':M=scale(replay[op['input']],Q(op['value']))
        elif op['op']=='bracket':
            a=replay[op['left']];b=replay[op['right']];M=add(mul(a,b),mul(b,a),b=-1)
        else:raise AssertionError('unknown certificate operation')
        assert M==MATS[n];replay.append(M)
    certificate={'inputs':'Native full masks on Kminus; subtraction/brackets/scalars are Lie algebra operations, not finite pulse sequences',
      'nodes':OPS,'basis':[{'active_pair':list(pair),'node':idx,'sha256':hash_matrix(MATS[idx])} for pair,idx in sorted(basis.items())],
      'edge_cycle_face_columns':chosen,'cycle_drift_terms':cycle_terms,'checkpoint_generators':checkpoint,
      'checkpoint_vectors':[[str(v) for v in a] for a in states]}
    root=Path(__file__).parent;root.joinpath('LIE_CERTIFICATE.json').write_text(json.dumps(certificate,indent=2)+'\n')
    report={'status':'PASS','arithmetic':'exact fractions.Fraction','physical_promotion':0,
      'review':'CONSTRUCTOR_ONLY; INDEPENDENT_REVIEW_PENDING','carrier_dimensions':[5,9,7,2],
      'active_dimension':14,'gradient_vertex_dimension':9,'active_skew_basis_rank':91,'formal_generated_lie_rank':92,
      'face_core_plane_generators':36,'edge_cycle_cross_generators':45,'edge_cycle_plane_generators':10,
      'mask_invariant_controls':128,'native_checkpoint_generators_decomposed':3,
      'constructor_certificate_nodes_replayed':len(replay),
      'feed_simplex':[0,1,4],'output_simplex':[0,2,4],'abstract_ports_added':0,
      'endpoint_owned_stocks':list(map(str,owned[0])),'gradient_frequencies_squared':{'3':1,'5':3},
      'scope':'FORMAL_LIE_AND_CHECKPOINT_COMPATIBILITY; NO_EXACT_FINITE_NATIVE_WORD',
      'open':['Admissible mask/time sequence and approximation certificate','Predictive local control, clock and records',
        'Native output-retaining renewal and physical action/particle bridge']}
    root.joinpath('RESULTS.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
