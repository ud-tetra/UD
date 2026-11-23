#!/usr/bin/env python3
"""Independent standard-library exact replay: explicit 3D fan, barycentric point-glued control, topological and transfer checks.
No SymPy, NumPy, external data, clocks, physical interpretation or fitted parameters.
"""
import itertools, json
from collections import defaultdict
from pathlib import Path
A=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
V=A+[tuple(-x for x in v) for v in A]
X=V+[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1),(0,0,0)]
IDX={p:i for i,p in enumerate(X)};CENTER=14
add=lambda u,v:tuple(a+b for a,b in zip(u,v))
sub=lambda u,v:tuple(a-b for a,b in zip(u,v))
dot=lambda u,v:sum(a*b for a,b in zip(u,v))
cross=lambda u,v:(u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
det3=lambda a,b,c:dot(a,cross(b,c))
vol=lambda t:det3(sub(X[t[1]],X[t[0]]),sub(X[t[2]],X[t[0]]),sub(X[t[3]],X[t[0]]))
sgn=lambda a:(1 if a>0 else -1 if a<0 else 0)

def octface(signs):
    x,y,z=signs
    return (IDX[(x,0,0)],IDX[(0,y,0)],IDX[(0,0,z)])

def canonical(seq):
    inv=sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
    assert len(set(seq))==len(seq)
    return tuple(sorted(seq)),(-1 if inv%2 else 1)

def boundary_single(simplex):
    out=defaultdict(int)
    for k in range(len(simplex)):
        f=simplex[:k]+simplex[k+1:]
        key,eps=canonical(f)
        out[key]+=((-1)**k)*eps
    return {k:v for k,v in out.items() if v}

def boundary_chain(chain):
    out=defaultdict(int)
    for simplex,coef in chain.items():
        for f,c in boundary_single(simplex).items():out[f]+=coef*c
    return {k:v for k,v in out.items() if v}

def flags(top):
    return {k:sorted({tuple(sorted(f)) for tet in top for f in itertools.combinations(tet,k+1)}) for k in range(4)}

def fan():
    ts=[]
    for s in itertools.product([-1,1],repeat=3):
        f=octface(s)
        ts.extend((tuple(sorted((CENTER,*f))),tuple(sorted((IDX[s],*f)))))
    return flags(ts)

def point_glue():
    names=[]; ids={}
    for packet in (0,1):
        for level in range(1,5):
            for face in itertools.combinations(range(4),level):
                if level==2:
                    f=face if packet==0 else tuple(i for i in range(4) if i not in face)
                    label=('junction',f)
                else:label=(packet,face)
                names.append(label);ids[packet,face]=label
    keys=sorted(set(names),key=str);lookup={x:i for i,x in enumerate(keys)}
    ts=[]
    for packet in (0,1):
        for perm in itertools.permutations(range(4)):
            chain=[tuple(sorted(perm[:i])) for i in range(1,5)]
            ts.append(tuple(sorted(lookup[ids[packet,c]] for c in chain)))
    return flags(ts),keys

def rank_mod(mat,prime):
    a=[[x%prime for x in row] for row in mat]
    nr,nc=len(a),len(a[0]);rank=0
    for col in range(nc):
        pivot=next((row for row in range(rank,nr) if a[row][col]),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        inv=pow(a[rank][col],-1,prime)
        for j in range(col,nc):a[rank][j]=(a[rank][j]*inv)%prime
        for row in range(rank+1,nr):
            c=a[row][col]
            if c:
                for j in range(col,nc):a[row][j]=(a[row][j]-c*a[rank][j])%prime
        rank+=1
        if rank==nr:break
    return rank

def incidence(low,high):
    idx={f:i for i,f in enumerate(low)}
    mat=[[0]*len(high) for _ in low]
    for j,face in enumerate(high):
        for k in range(len(face)):
            f=face[:k]+face[k+1:]
            mat[idx[f]][j]=(-1)**k
    return mat

def homology(b):
    bs=[incidence(b[k-1],b[k]) for k in range(1,4)]
    for p in (101,103,107):
        ranks=[rank_mod(z,p) for z in bs]
        if p==101:base=ranks
        else:assert ranks==base
    f=[len(b[k]) for k in range(4)]
    betti=[f[0]-base[0],f[1]-base[0]-base[1],f[2]-base[1]-base[2],f[3]-base[2]]
    for k in range(2):
        assert all(sum(bs[k][i][l]*bs[k+1][l][j] for l in range(len(bs[k][0])))==0 for i in range(len(bs[k])) for j in range(len(bs[k+1][0])))
    return f,base,betti

new=fan();old=point_glue();f,r,betti_fan=homology(new);fp,rp,bp=homology(old[0])
assert (f,r,betti_fan)==([15,42,44,16],[14,28,16],[1,0,0,0])
assert (fp,rp,bp)==([24,100,120,48],[23,72,48],[1,5,0,0])
# Source-to-target transfer via explicit midpoint edge and triangle subdivisions.

def oriented(t,old):
    k=len(t)-1
    if k==0:return 1
    if k==1:return sgn(dot(sub(X[t[1]],X[t[0]]),sub(X[old[1]],X[old[0]])))
    if k==2:
        un=cross(sub(X[t[1]],X[t[0]]),sub(X[t[2]],X[t[0]]))
        vn=cross(sub(X[old[1]],X[old[0]]),sub(X[old[2]],X[old[0]]))
        return sgn(dot(un,vn))
    return sgn(vol(t)*vol(old))

def lift(simplex):
    k=len(simplex)-1
    if k==0:return {simplex:1}
    if k==1:
        u,v=simplex
        midpoint=IDX[tuple((a+b)//2 for a,b in zip(X[u],X[v]))]
        terms=((u,midpoint),(midpoint,v))
    elif k==2:
        a,b,c=simplex
        mids={(a,b):IDX[tuple((i+j)//2 for i,j in zip(X[a],X[b]))],(a,c):IDX[tuple((i+j)//2 for i,j in zip(X[a],X[c]))],(b,c):IDX[tuple((i+j)//2 for i,j in zip(X[b],X[c]))]}
        ab,ac,bc=mids[a,b],mids[a,c],mids[b,c]
        terms=((a,ab,ac),(b,ab,bc),(c,ac,bc),(ab,ac,bc))
    else:
        packet=0 if simplex[0]<4 else 1
        # 8 octa tetra plus the 4 original packet's corner caps
        tets=[f for f in new[3] if CENTER in f or any(v in (range(0,4) if packet==0 else range(4,8)) for v in f)]
        assert len(tets)==12
        terms=tets
    vals=defaultdict(int)
    for f0 in terms:
        f,order=canonical(f0)
        coeff=oriented(f,simplex)
        assert coeff
        vals[f]+=coeff
    assert len(vals)==[1,2,4,12][k]
    return dict(vals)

OLD={k:[tuple(i for i in face) for packet in (0,1) for face in itertools.combinations(range(packet*4,packet*4+4),k+1)] for k in range(4)}
for k in range(1,4):
    for face in OLD[k]:
        left=boundary_chain(lift(face))
        right=defaultdict(int)
        for oface,coef in boundary_single(face).items():
            for newface,a in lift(oface).items():right[newface]+=coef*a
        right={z:y for z,y in right.items() if y}
        assert left==right,(k,face,left,right)

# The only shared top subsimplices are the 8 central octahedron tetrahedra.
A3=lift(tuple(range(0,4)));B3=lift(tuple(range(4,8)))
shared=set(A3)&set(B3)
assert len(shared)==8
normAA=sum(v*v for v in A3.values());normBB=sum(v*v for v in B3.values());crossBB=sum(A3[t]*B3[t] for t in shared)
assert (normAA,normBB,abs(crossBB))==(12,12,8)
# The sign-corrected top Gram eigenvalues are 12±8.
assert (12-abs(crossBB),12+abs(crossBB))==(4,20)
# Topological link of each shared midpoint in point-glued model has two components.
name_to_id={x:i for i,x in enumerate(old[1])}
components=[]
for v,vertex in enumerate(old[1]):
    if vertex[0]!='junction':continue
    facets=[tuple(x for x in t if x!=v) for t in old[0][3] if v in t]
    vset={a for t in facets for a in t}
    parent={x:x for x in vset}
    def root(i):
        while parent[i]!=i:i=parent[i]
        return i
    for tri in facets:
        for a,b in itertools.combinations(tri,2): parent[root(a)]=root(b)
    components.append(len({root(i) for i in vset}))
assert components==[2]*6
# Exact volume receipts: O=8 octants * 1/6; 8 caps * 1/3; union 4.
central=[t for t in new[3] if CENTER in t]
caps=[t for t in new[3] if CENTER not in t]
assert len(central)==8 and len(caps)==8
assert {abs(vol(t)) for t in central}=={1} and {abs(vol(t)) for t in caps}=={2}
assert sum(abs(vol(t)) for t in new[3])==24
out={'status':'EXACT_CONDITIONAL / SOURCE_OPEN','fan':{'f':f,'ranks_over_101_103_107':r,'betti':betti_fan,'top_transfer_independent_mass':normAA,'top_transfer_shared_volume_cells':len(shared),'top_cross_sign':crossBB,'top_gram_eigenvalues':[4,20],'total_union_volume':'4'},'pointglued':{'f':fp,'ranks_over_101_103_107':rp,'betti':bp,'six_link_component_counts':components},'chain_equivariance':'PASS all old simplices 1,2,3','physical_promotion':0}
Path(__file__).with_name('replay_results.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
