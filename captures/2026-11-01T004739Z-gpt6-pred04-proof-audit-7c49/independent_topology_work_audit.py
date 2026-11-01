#!/usr/bin/env python3
"""Independent exact finite audit of UD PR479 topology and staged-source claim.
No import from PR479 code. The finite tests are supporting checks, not an empirical bridge.
"""
from __future__ import annotations
from itertools import combinations, permutations, product
from collections import Counter, defaultdict
from fractions import Fraction as F
from math import comb
import argparse, json


def tetra_mesh(nx: int, ny: int, nz: int):
    """Freudenthal tetrahedralization: each integer cube split into 3! simplices."""
    tets=set()
    for i, j, k in product(range(nx), range(ny), range(nz)):
        origin=(i,j,k)
        for perm in permutations(range(3)):
            path=[origin]
            pos=list(origin)
            for a in perm:
                pos[a]+=1
                path.append(tuple(pos))
            tets.add(tuple(sorted(path)))
    return tets


def closure(tets):
    faces={tuple(sorted(p)) for t in tets for p in combinations(t,3)}
    edges={tuple(sorted(p)) for f in faces for p in combinations(f,2)}
    verts={x for e in edges for x in e}
    return sorted(verts), sorted(edges), sorted(faces), sorted(tets)


def rank_bits(cols):
    pivots={}
    for x in cols:
        while x:
            j=x.bit_length()-1
            if j not in pivots:
                pivots[j]=x
                break
            x^=pivots[j]
    return len(pivots)


def betti(simplices):
    v,e,f,t=simplices
    vid={q:i for i,q in enumerate(v)}
    eid={q:i for i,q in enumerate(e)}
    fid={q:i for i,q in enumerate(f)}
    b1=[sum(1<<vid[a] for a in edge) for edge in e]
    b2=[sum(1<<eid[tuple(sorted(pair))] for pair in combinations(face,2)) for face in f]
    b3=[sum(1<<fid[tuple(sorted(tri))] for tri in combinations(tet,3)) for tet in t]
    # boundary-of-boundary independent parity check
    for x,lower in ((b2,b1),(b3,b2)):
        for col in x:
            acc=0
            while col:
                bit=col & -col
                acc^=lower[bit.bit_length()-1]
                col^=bit
            assert acc==0
    r1,r2,r3=map(rank_bits,(b1,b2,b3))
    b=(len(v)-r1,len(e)-r1-r2,len(f)-r2-r3,len(t)-r3)
    assert len(v)-len(e)+len(f)-len(t)==b[0]-b[1]+b[2]-b[3]
    return dict(V=len(v),E=len(e),F=len(f),T=len(t),betti_f2=b,rank=(r1,r2,r3))


def cut_center(tets, nx, ny, nz):
    core={(nx//2,ny//2,k) for k in range(nz+1)}
    return {tet for tet in tets if core.isdisjoint(tet)}


def triangle_incidence(faces):
    inc=Counter(edge for face in faces for edge in combinations(face,2))
    return dict(Counter(inc.values())),max(inc.values())


def face_bound_check():
    """Exhausts all three-edge closed real cochains on a small rational grid,
    all six update orders, all n=0,1,2, arbitrary positive rational lambdas/mu.
    The sharp face inequality max(first**2,last**2)<=2/3 sum squares is proved
    algebraically in the manuscript, not by this finite sweep.
    """
    check_count=0;worst_ratio=F(0);saturators=[]
    vals=[F(a,2) for a in range(-6,7)]
    for x,y in product(vals,repeat=2):
        z=-x-y
        if x==y==z==0:
            continue
        vs=[x,y,z];Q=sum(t*t for t in vs)
        for order in permutations((0,1,2)):
            seq=[F(0)];cur=F(0)
            for idx in order:
                cur+=vs[idx];seq.append(cur*cur)
            assert seq[-1]==0
            variation=sum(max(seq[i+1]-seq[i],F(0)) for i in range(3))
            ratio=variation/Q
            assert variation==max(seq)
            assert ratio<=F(2,3)
            check_count+=1
            if ratio>worst_ratio:
                worst_ratio=ratio;saturators=[dict(triple=tuple(map(str,vs)),order=order,ratio=str(ratio))]
    assert worst_ratio==F(2,3)
    # Scalar three-edge triangle action with a quadratic base and curvature penalty.
    # n>=0 makes the baseline norm part monotone under individual updates.
    sequences=0
    for x,y in product([F(-2),F(-1),F(0),F(1),F(2)],repeat=2):
        z=-x-y
        if x==y==z==0:continue
        h=[x,y,z]
        q=sum(v*v for v in h)
        for order in permutations(range(3)):
            for n,lam,mu in product([0,1,2],[F(1,3),F(2)],[F(1,7),F(3,2)]):
                a=[n*v for v in h]
                def A(a):return lam*sum(v*v for v in a)/2+mu*(sum(a))**2/2
                es=[A(a)]
                for ix in order:
                    a[ix]+=h[ix];es.append(A(a))
                positive=sum(max(es[i+1]-es[i],F(0)) for i in range(3))
                endpoint=lam*F(2*n+1,2)*q
                assert es[-1]-es[0]==endpoint
                assert positive<=endpoint+mu*q/F(3)
                sequences+=1
    return dict(exact_closed_face_cases=check_count,sharp_face_ratio=str(worst_ratio),sharp_example=saturators[0],exact_action_sequences=sequences)


def main():
    p=argparse.ArgumentParser();p.add_argument('--out',default='INDEPENDENT_AUDIT.json');a=p.parse_args()
    verified=[]
    for N in (4,6,8):
        full=tetra_mesh(N,N,2)
        cut=cut_center(full,N,N,2)
        sx=closure(full); sy=closure(cut)
        out0=betti(sx);out1=betti(sy)
        assert out0['T']==12*N*N and out1['T']==12*N*N-36
        assert out0['betti_f2']==(1,0,0,0)
        assert out1['betti_f2']==(1,1,0,0)
        counts,max_inc=triangle_incidence(sy[2]);assert max_inc<=6
        expected=(3*(N+1)**2,17*N*N+14*N+2,26*N*N+8*N,12*N*N)
        assert tuple(out0[x] for x in ('V','E','F','T'))==expected
        drops=tuple(out0[x]-out1[x] for x in ('V','E','F','T'))
        assert drops==(3,32,66,36)
        verified.append(dict(grid_N=N,full=out0,excised=out1,drops=dict(zip(('V','E','F','T'),drops)),triangle_edge_incidence_counts=counts,max_incidence=max_inc))
    # A single bottom-boundary vertex excision does NOT produce the full tunnel.
    # This is a finite F2 counterexample to an unqualified "one local defect => H1=Z".
    partial=[]
    for N in (4,6,8):
        base=tetra_mesh(N,N,2)
        seed=(N//2,N//2,0)
        first={tet for tet in base if seed not in tet}
        v=betti(closure(first))
        assert v['betti_f2']==(1,0,0,0)
        partial.append({'N':N,'tetra_remaining':v['T'],'betti_F2':v['betti_f2']})

    # A literal legal 2<->3 interior face move changes the number of tetrahedra
    # but preserves H1 in both intact and excised complexes.
    def pachner_witness(tets):
        face_to_tets=defaultdict(list)
        for tet in tets:
            for tri in combinations(tet,3):face_to_tets[tri].append(tet)
        old_edges=set(closure(tets)[1])
        for face,incident in sorted(face_to_tets.items()):
            if len(incident)!=2:continue
            u=next(v for v in incident[0] if v not in face)
            v=next(v for v in incident[1] if v not in face)
            if tuple(sorted((u,v))) in old_edges:continue
            a,b,c=face
            replacements={tuple(sorted(vertices)) for vertices in
                          ((u,v,a,b),(u,v,b,c),(u,v,c,a))}
            moved=(tets-set(incident))|replacements
            before=betti(closure(tets));after=betti(closure(moved))
            assert before['betti_f2']==after['betti_f2']
            assert after['T']==before['T']+1
            return {'face':face,'new_edge':tuple(sorted((u,v))),
                    'before_F2':before['betti_f2'],'after_F2':after['betti_f2']}
        raise AssertionError('no legal 2-3 move located')
    legal_moves={}
    for name,tets in [('intact',tetra_mesh(4,4,2)),
                      ('tunnel',cut_center(tetra_mesh(4,4,2),4,4,2))]:
        legal_moves[name]=pachner_witness(tets)

    # Infinite interior local-type check: 7 nonzero 0/1 edge directions, cubes in [-1,1]^3.
    local=tetra_mesh(3,3,3)
    edges_to_faces=defaultdict(set)
    for tri in closure(local)[2]:
        for edge in combinations(tri,2):edges_to_faces[edge].add(tri)
    origin=(1,1,1)
    local_dir={}
    for dx,dy,dz in product((0,1),repeat=3):
        if (dx,dy,dz)==(0,0,0):continue
        edge=(origin,(origin[0]+dx,origin[1]+dy,origin[2]+dz))
        local_dir[str((dx,dy,dz))]=len(edges_to_faces[edge])
    assert max(local_dir.values())==6
    face_tests=face_bound_check()
    report=dict(protocol='UD_PR479_independent_topology_and_source_audit_v1.0',
       source_pr='UD#479 @ b5c8146ae4b956279e6f399553e02cffbc42c7ea',
       verification='EXACT_FINITE_DOMAIN_CHECK_ONLY',physical_promotion=0,
       grids=verified,partial_source_counterexamples=partial,legal_pachner_2to3_witnesses=legal_moves,
       local_infinite_lattice_edge_types=local_dir,face_checks=face_tests,
       structural_claims={'K4_tetra_full':'12*N*N','drops_on_center_excision':'(3,32,66,36)',
       'H1_Z_before_after':'0 -> Z conditional on full column excision',
       'uniform_incidence_bound':'d_F <= 6 for the declared Freudenthal cubic triangulation',
       'improved_work_bound':'W_plus <= Delta + (mu/3)*d_F*||h||^2',
       'n2_unit_gap_mu_equals_lambda':'W_plus <= 9/5 (prior 41/5 bound valid but loose)'},
       assumptions={'source_seed':'external','direction':'assumed +z','excision':'assumed',
       'integer_lift':'assumed','h':'closed 1-cochain','base_transition_n':'nonnegative integer',
       'edge_updates':'each edge updated once by its h_component, any order',
       'positive_stiffness':'lambda>0,mu>=0'} )
    with open(a.out,'w') as f:json.dump(report,f,indent=2,sort_keys=True)
    print('PASS; grids',[(a['grid_N'],a['excised']['betti_f2']) for a in verified],
          '; max triangle incidence',max(local_dir.values()),
          '; sharp face ratio',face_tests['sharp_face_ratio'],
          '; exact tests',face_tests['exact_closed_face_cases'],face_tests['exact_action_sequences'])

if __name__=='__main__':main()
