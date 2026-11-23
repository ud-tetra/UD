#!/usr/bin/env python3
"""Exact two-tetra 3D gluing and source-interface audit (SymPy, rationals only).
Does not infer a UD event or physical metric, time, or energy.
"""
import itertools, json, sys
from pathlib import Path
import sympy as S
C=tuple
V_A=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
V_B=[tuple(-x for x in a) for a in V_A]
O=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
CENTER=(0,0,0)
coords=V_A+V_B+O+[CENTER]; center=14
coord2id={c:i for i,c in enumerate(coords)}
assert len(coord2id)==15

def oct_face(s):
    return [coord2id[(s[0],0,0)],coord2id[(0,s[1],0)],coord2id[(0,0,s[2])]]

def build_fan():
    top=[]
    for s in itertools.product((-1,1), repeat=3):
        face=oct_face(s)
        top.append(tuple(sorted((center,*face))))
        cap=coord2id[s]
        top.append(tuple(sorted((cap,*face))))
    assert len(set(top))==16
    return {k:sorted({face for t in top for face in itertools.combinations(t,k+1)}) for k in range(4)}

def build_sd_pointglued():
    # Barycentric subdivision of each full tetra: simplex=chain of nested nonempty faces.
    oldbases=[list(itertools.combinations(range(4),k)) for k in range(1,5)]
    nodes=[]; vnames={}
    for p in (0,1):
        for oldsize in range(1,5):
            for face in oldbases[oldsize-1]:
                if oldsize==2:
                    # six geometrically matched canonical dual-edge midpoint vertices
                    if p==0: label=('J',face)
                    else: label=('J',tuple(x for x in range(4) if x not in face))
                else: label=(p,face)
                vnames[p,face]=label
                nodes.append(label)
    names=sorted(set(nodes),key=str)
    idx={v:i for i,v in enumerate(names)}
    facets=set()
    for p in (0,1):
        for perm in itertools.permutations(range(4)):
            chain=[tuple(sorted(perm[:i])) for i in range(1,5)]
            facets.add(tuple(sorted(idx[vnames[p,face]] for face in chain)))
    assert len(facets)==48
    return {k:sorted({face for t in facets for face in itertools.combinations(t,k+1)}) for k in range(4)},names

def boundary(low,high):
    R={x:i for i,x in enumerate(low)}
    B=S.zeros(len(low),len(high))
    for j,face in enumerate(high):
        for k in range(len(face)):
            f=face[:k]+face[k+1:]
            B[R[f],j] += (-1)**k
    return B

def mats(b):
    return [boundary(b[k-1],b[k]) for k in range(1,4)]

def topgeom(t):
    p=[S.Matrix(coords[i]) for i in t]
    return S.det(S.Matrix.hstack(p[1]-p[0],p[2]-p[0],p[3]-p[0]))

def inside(pt,orig):
    ps=[S.Matrix(coords[i]) for i in orig]
    pt=S.Matrix(pt)
    if len(orig)==1:return pt==ps[0]
    mat=S.Matrix.hstack(*[ps[i]-ps[0] for i in range(1,len(ps))])
    try:
        sol,params=mat.gauss_jordan_solve(pt-ps[0])
        if params.rows:return False
        return all(x>=0 for x in [1-sum(sol),*sol])
    except ValueError:return False

def orient_sign(new,orig):
    p=[S.Matrix(coords[i]) for i in orig]
    q=[S.Matrix(coords[i]) for i in new]
    k=len(orig)-1
    if k==0: return 1
    if k==1:
        dp=p[1]-p[0];dq=q[1]-q[0];v=dp.dot(dq)
    elif k==2:
        dp=(p[1]-p[0]).cross(p[2]-p[0]);dq=(q[1]-q[0]).cross(q[2]-q[0]);v=dp.dot(dq)
    else:
        dp=S.det(S.Matrix.hstack(*[p[i]-p[0] for i in range(1,4)]))
        dq=S.det(S.Matrix.hstack(*[q[i]-q[0] for i in range(1,4)]))
        v=dp*dq
    assert v!=0,(new,orig)
    return S.sign(v)

def old_source():
    return {k: [tuple(4*p+i for i in f) for p in (0,1) for f in itertools.combinations(range(4),k+1)] for k in range(4)}

def transfer(old,new):
    Ts=[]
    for k in range(4):
        Tk=S.zeros(len(new[k]),len(old[k]))
        for j,oface in enumerate(old[k]):
            included=[]
            for i,nface in enumerate(new[k]):
                if all(inside(coords[v],oface) for v in nface):
                    Tk[i,j]=orient_sign(nface,oface)
                    included.append(nface)
            assert len(included)==[1,2,4,12][k],(k,j,len(included),included)
        Ts.append(Tk)
    return Ts

if __name__=='__main__':
    new=build_fan(); B1,B2,B3=mats(new)
    assert B1*B2==S.zeros(B1.rows,B2.cols)
    assert B2*B3==S.zeros(B2.rows,B3.cols)
    ranks=[B1.rank(),B2.rank(),B3.rank()]
    f=[len(new[k]) for k in range(4)]
    b=[f[0]-ranks[0],f[1]-ranks[0]-ranks[1],f[2]-ranks[1]-ranks[2],f[3]-ranks[2]]
    assert f==[15,42,44,16],(f,ranks,b)
    assert ranks==[14,28,16],(f,ranks,b)
    assert b==[1,0,0,0]
    # Face incidence: exactly 24 boundary triangle faces
    boundary_faces=[]
    for face in new[2]:
        count=sum(set(face).issubset(t) for t in new[3])
        assert count in (1,2)
        if count==1:boundary_faces.append(face)
    assert len(boundary_faces)==24
    old=old_source(); Bold=mats(old)
    T=transfer(old,new)
    for k in range(1,4):
        assert [B1,B2,B3][k-1]*T[k]==T[k-1]*Bold[k-1],k
    G=[x.T*x for x in T]
    assert G[0]==S.eye(8)
    assert G[1]==2*S.eye(12)
    assert G[2]==4*S.eye(8)
    assert G[3][0,0]==12 and G[3][1,1]==12 and abs(G[3][0,1])==8
    assert G[3].eigenvals()=={S.Integer(20):1,S.Integer(4):1}
    # Compare full 3D point-glued barycentric subdivision (distinct simplex! not the faithful geometric union).
    point,names=build_sd_pointglued()
    K1,K2,K3=mats(point)
    assert K1*K2==S.zeros(K1.rows,K2.cols)
    assert K2*K3==S.zeros(K2.rows,K3.cols)
    point_f=[len(point[k]) for k in range(4)]
    point_r=[K1.rank(),K2.rank(),K3.rank()]
    point_b=[point_f[0]-point_r[0],point_f[1]-point_r[0]-point_r[1],point_f[2]-point_r[1]-point_r[2],point_f[3]-point_r[2]]
    assert point_f==[24,100,120,48],point_f
    assert point_r==[23,72,48],(point_r,point_b)
    assert point_b==[1,5,0,0]
    # Junction node links have disjoint triangles from different packet side
    def link_top(v):
        return [tuple(i for i in t if i!=v) for t in point[3] if v in t]
    jnodes=[i for i,name in enumerate(names) if name[0]=='J'];assert len(jnodes)==6
    # link of a glued midpoint has two connected (vertex-disjoint) disk pieces
    link_counts=[]
    for v in jnodes:
        tris=link_top(v);verts=set(x for tr in tris for x in tr)
        edges={tuple(sorted(e)) for tr in tris for e in itertools.combinations(tr,2)}
        parent={i:i for i in verts}
        def root(u):
            while parent[u]!=u:u=parent[u]
            return u
        for u,w in edges:parent[root(u)]=root(w)
        comps=len({root(u) for u in verts})
        link_counts.append(comps)
    assert link_counts==[2]*6,link_counts
    # Construct skew generator for common 3D fan and second-order B-cap response.
    zero=S.zeros(0,0)
    A=S.zeros(sum(f),sum(f)); offset=[0]
    for size in f: offset.append(offset[-1]+size)
    for k,Bk in enumerate((B1,B2,B3)):
        i,j=offset[k],offset[k+1]
        A[i:j,j:j+Bk.cols]=-Bk
        A[j:j+Bk.cols,i:j]=Bk.T
    assert A+A.T==S.zeros(A.rows,A.cols)
    # Top-volume orientation-correct source A unit fundamental chain
    top_S=T[3][:,0]
    initial=S.zeros(A.rows,1)
    for i,x in enumerate(top_S):initial[offset[3]+i]=x
    second=A*A*initial
    Bcaps=[i for i,t in enumerate(new[3]) if any(x in range(4,8) for x in t)]
    Arest=[i for i,t in enumerate(new[3]) if any(x in range(0,4) for x in t)]
    central=[i for i,t in enumerate(new[3]) if 14 in t]
    assert len(Bcaps)==4 and len(Arest)==4 and len(central)==8
    assert all(initial[offset[3]+i]==0 for i in Bcaps)
    Bsecond=[second[offset[3]+i] for i in Bcaps]
    assert sorted(abs(x) for x in Bsecond)==[1]*4, Bsecond
    # The actual Euclidean union carries a full 3-ball triangulation, not merely correct Betti numbers.
    link_types=[]
    for vid in range(len(coords)):
        lk={k:sorted({tuple(x for x in simplex if x!=vid) for simplex in new[k+1] if vid in simplex}) for k in range(3)}
        d1=boundary(lk[0],lk[1]);d2=boundary(lk[1],lk[2])
        lr1,lr2=d1.rank(),d2.rank()
        lb=(len(lk[0])-lr1,len(lk[1])-lr1-lr2,len(lk[2])-lr2)
        if vid==center: assert lb==(1,0,1)
        else:assert lb==(1,0,0)
        link_types.append(list(lb))
    # Exact Euclidean volumes: eight octant tetrahedra each volume 1/6; eight caps each 1/3.
    center_tets=[t for t in new[3] if center in t]
    cap_tets=[t for t in new[3] if center not in t]
    assert len(center_tets)==len(cap_tets)==8
    absvolume=lambda t:abs(topgeom(t))/6
    assert {absvolume(t) for t in center_tets}=={S.Rational(1,6)}
    assert {absvolume(t) for t in cap_tets}=={S.Rational(1,3)}
    assert sum(absvolume(t) for t in new[3])==4
    # Global old/new skew generators are not intertwining under the exact chain map.
    oldsize=[len(old[k]) for k in range(4)]; oldoff=[0]
    for z in oldsize:oldoff.append(oldoff[-1]+z)
    Aold=S.zeros(sum(oldsize))
    for k,Bk in enumerate(Bold):
        u,v=oldoff[k],oldoff[k+1]
        Aold[u:u+Bk.rows,v:v+Bk.cols]=-Bk
        Aold[v:v+Bk.cols,u:u+Bk.rows]=Bk.T
    Tfull=S.diag(*T)
    defect=A*Tfull-Tfull*Aold
    assert defect!=S.zeros(*defect.shape)
    defect_rank=defect.rank()
    assert defect_rank==28
    assert S.trace(defect.T*defect)==144
    # Fixed positive diagonal target top-cell metric cannot erase correlated central overlap:
    # each of 8 central tetra transfers carries the same sign product for A and B.
    overlap_index=[i for i in range(len(new[3])) if T[3][i,0] and T[3][i,1]]
    assert len(overlap_index)==8
    overlap_products={T[3][i,0]*T[3][i,1] for i in overlap_index}
    assert overlap_products in ({S.Integer(1)},{S.Integer(-1)})
    # Report source scale ambiguity and exact budget
    Gtop=G[3]
    Ktop=Gtop-S.eye(2)
    assert sorted(Ktop.eigenvals().keys())==[3,19]
    assert all(Gtop[0,i]!=0 for i in (0,1))
    outcome={
      'classification':'EXACT_CONDITIONAL / NO_GO_SCOPED / OPEN_CONSTITUTIVE_SOURCE',
      'fan':{'f':f,'ranks':ranks,'betti':b,'boundary_triangles':len(boundary_faces),'euler':sum((-1)**k*f[k] for k in range(4)),'coface_nilpotent':True,'chain_transfer_commutes':True,'transfer_image_counts_by_grade':[1,2,4,12],
             'gram0':str(G[0]),'gram1_diag':2,'gram2_diag':4,'gram3':[[str(y) for y in row] for row in Gtop.tolist()], 'gram3_eigenvalues':[4,20], 'native_stock_gain_top_eigenvalues':[3,19], 'B_cap_second_derivative_signed':[str(x) for x in Bsecond], 'all_vertex_links_betti':link_types, 'union_volume':'4', 'octahedron_overlap_volume':'4/3', 'commutator_rank':defect_rank, 'commutator_frobenius_norm_squared':'144', 'positive_diagonal_top_metric_isometry':'NO_GO_CORRELATED_SHARED_8_CELLS'},
      'point_glued':{'f':point_f,'ranks':point_r,'betti':point_b,'euler':sum((-1)**k*point_f[k] for k in range(4)),'link_components_at_each_identified_vertex':link_counts},
      'status':'GRAPH_ONLY_AND_POINT_GLUED_NO_MANIFOLD ; GEOMETRIC_FAN_3_BALL ; SOURCE_TRIGGER_OPEN','physical_promotion':0}
    out=Path(__file__).with_name('results.json');out.write_text(json.dumps(outcome,indent=2,sort_keys=True)+'\n')
    print(json.dumps(outcome,indent=2,sort_keys=True))
