"""Exact (2,1) triangular coincidence lattice and honeycomb basis count.

No interlayer potential, force or atomistic Hessian is constructed here.
"""
from fractions import Fraction as Q
from math import acos,degrees
from pathlib import Path
from itertools import combinations,product
import json

G=[[Q(1),Q(1,2)],[Q(1,2),Q(1)]]

def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
                     for j in range(len(b[0]))] for i in range(len(a))]
def t(a):return [list(x) for x in zip(*a)]
def det(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def inv(a):
 d=det(a);return [[Q(a[1][1],d),Q(-a[0][1],d)],
                  [Q(-a[1][0],d),Q(a[0][0],d)]]
def dot(a,b):return mm([a],mm(G,t([b])))[0][0]

def rank(a):
    a=[[Q(x) for x in row] for row in a]
    i=0
    for j in range(len(a[0])):
        pivot=next((p for p in range(i,len(a)) if a[p][j]),None)
        if pivot is None:continue
        a[i],a[pivot]=a[pivot],a[i]
        value=a[i][j];a[i]=[x/value for x in a[i]]
        for p in range(i+1,len(a)):
            value=a[p][j]
            if value:a[p]=[x-value*y for x,y in zip(a[p],a[i])]
        i+=1
        if i==len(a):break
    return i

def fine_chain_character():
    old=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
    shell=[tuple(s if axis==k else 0 for k in range(3))
           for axis in range(3) for s in (-1,1)]
    ids={x:i for i,x in enumerate(shell)}
    mid={(i,j):ids[tuple((old[i][k]+old[j][k])//2 for k in range(3))]
         for i,j in combinations(range(4),2)}
    inner=[tuple(sorted((6,)+tuple(ids[tuple(signs[axis] if axis==k
            else 0 for k in range(3))] for axis in range(3))))
           for signs in product((-1,1),repeat=3)]
    corner=[tuple(sorted((7+i,)+tuple(mid[p] for p in mid if i in p)))
            for i in range(4)]
    cells=inner+corner
    fine=[list(combinations(range(11),1)),
          sorted(set(e for c in cells for e in combinations(c,2))),
          sorted(set(f for c in cells for f in combinations(c,3))),
          sorted(cells)]
    assert [len(x) for x in fine]==[11,30,32,12]
    ranks=[]
    for k in (1,2,3):
        lookup={x:i for i,x in enumerate(fine[k-1])}
        b=[[0]*len(fine[k]) for _ in fine[k-1]]
        for j,sigma in enumerate(fine[k]):
            for h in range(k+1):
                b[lookup[sigma[:h]+sigma[h+1:]]][j]=(-1)**h
        ranks.append(rank(b))
    assert ranks==[10,20,12]
    p=(1,2,0,3)
    fmap=[mid[tuple(sorted((p[i],p[j])))] for i,j in
          (next(pair for pair,v in mid.items() if v==x) for x in range(6))]
    fmap += [6]+[7+p[i] for i in range(4)]
    def orientation(seq):
        return (-1)**sum(seq[i]>seq[j] for i in range(len(seq))
                         for j in range(i+1,len(seq)))
    traces=[]
    for grade in fine:
        traces.append(sum(orientation([fmap[v] for v in simplex])
                          for simplex in grade if
                          tuple(sorted(fmap[v] for v in simplex))==simplex))
    assert traces==[2,0,2,3] and sum(traces)==7
    assert sum((-1)**i*x for i,x in enumerate(traces))==1
    # Contractible ball: b0=11-rank(B1)=1, b1=30-r1-r2=0,
    # b2=32-r2-r3=0, b3=12-r3=0. The single harmonic zero mode is
    # the constant vertex function and is C3-trivial.
    betti=[11-ranks[0],30-ranks[0]-ranks[1],
           32-ranks[1]-ranks[2],12-ranks[2]]
    assert betti==[1,0,0,0]
    active_dim=sum(map(len,fine))-sum(betti)
    active_trace=sum(traces)-1
    assert (active_dim,active_trace)==(84,6)
    # Real C3 irreps are one trivial line (trace 1) and one rotation
    # plane (trace -1). Solve n0+2 n2=84 and n0-n2=6.
    n2=(active_dim-active_trace)//3;n0=active_trace+n2
    assert (n0,n2)==(32,26)
    return ranks,betti,traces,(n0,n2)

def main():
    m,n=2,1
    u=[m,n];v=[n,m]
    # J(p,q)=(-q,p+q) is a 60-degree triangular basis rotation.
    J=lambda x:[-x[1],x[0]+x[1]]
    Bu=[[u[0],J(u)[0]],[u[1],J(u)[1]]]
    Bv=[[v[0],J(v)[0]],[v[1],J(v)[1]]]
    assert det(Bu)==det(Bv)==7
    R=mm(Bu,inv(Bv))
    assert R==[[Q(8,7),Q(3,7)],[Q(-3,7),Q(5,7)]]
    assert mm(t(R),mm(G,R))==G and det(R)==1
    assert mm(R,t([v]))==t([u])
    cosine=dot(u,v)/dot(u,u)
    assert dot(u,u)==dot(v,v)==7 and cosine==Q(13,14)
    assert (R[0][0]+R[1][1])/2==cosine
    theta=degrees(acos(float(cosine)))
    assert round(theta,1)==21.8 and round(60-theta,1)==38.2
    # CSL = Bu Z^2: Bu Z^2 is included in both lattices.
    # Its index in the original lattice is 7. Since 7 is prime and R
    # is not integral, no larger common sublattice exists.
    assert all(x.denominator==1 for row in Bu for x in row)
    assert any(x.denominator!=1 for row in R for x in row)
    reps=[(k,0) for k in range(7)]
    q=lambda x:(x[0]-2*x[1])%7
    assert [q(x) for x in reps]==list(range(7))
    assert all(q(col)==0 for col in zip(*Bu))
    # Honeycomb has two basis sites per Bravais cell: A=(0,0),
    # B=(1/3,1/3), with position units a1,a2.
    basis=[(Q(0),Q(0)),(Q(1,3),Q(1,3))]
    layer1=[tuple(Q(x[i])+b[i] for i in range(2)) for x in reps for b in basis]
    layer2=[tuple(mm(R,[[Q(x[0])+b[0]],[Q(x[1])+b[1]]])[i][0]
                  for i in range(2)) for x in reps for b in basis]
    assert len(set(layer1))==len(set(layer2))==14
    J2=[[-1,-1],[1,0]]
    def congruent(a,b):
        coeff=mm(inv(Bu),[[a[i]-b[i]] for i in range(2)])
        return all(x[0].denominator==1 for x in coeff)
    fixed=[]
    for layer in (layer1,layer2):
        perm=[]
        for atom in layer:
            rotated=[x[0] for x in mm(J2,[[v] for v in atom])]
            hits=[j for j,other in enumerate(layer) if congruent(rotated,other)]
            assert len(hits)==1
            perm.append(hits[0])
        assert sorted(perm)==list(range(14))
        assert all(perm[perm[perm[i]]]==i for i in range(14))
        fixed.append(sum(i==v for i,v in enumerate(perm)))
    assert fixed==[2,2]
    ranks,betti,traces,ud_irreps=fine_chain_character()
    # At a fixed atom, the standard 3D displacement action of a 120°
    # spatial rotation has trace 2*cos(120°)+1=0. A permuted atom gives
    # no diagonal trace. Hence the full 84D atomic trace is zero.
    atomic_trace=0
    atomic_irreps=(28,28)
    assert ud_irreps!=atomic_irreps
    max_equivariant_rank=min(ud_irreps[0],atomic_irreps[0])+2*min(ud_irreps[1],atomic_irreps[1])
    assert max_equivariant_rank==80
    # Characters of the seven-cell quotient obey 1+X+...+X^6=0
    # at each nontrivial seventh root; no force cancellation is inferred.
    assert len(reps)*len(basis)*2==28
    result={"lane":"EXACT conventional 2D coincidence geometry; UD physical promotion 0",
            "m_n":[2,1],"supercell_matrices":{"Bu":Bu,"Bv":Bv},
            "rotation_matrix_triangular_basis":[[str(x) for x in row] for row in R],
            "rotation_cosine":"13/14",
            "angle_degrees":[theta,60-theta],
            "coincidence_index":7,"quotient_group":"Z/7Z",
            "coset_representatives":reps,"honeycomb_basis_count":2,
            "atoms_per_layer_supercell":14,"bilayer_atom_count":28,
            "bilayer_3D_coordinate_count":84,"UD_refined_chain_dimension":85,
            "UD_boundary_ranks":ranks,"UD_betti":betti,
            "UD_C3_trace_by_chain_grade":traces,
            "UD_active_C3_real_irreps":{"trivial":ud_irreps[0],"rotation_planes":ud_irreps[1]},
            "atom_fixed_sites_by_layer_under_C3":fixed,
            "atomic_3D_displacement_C3_trace":atomic_trace,
            "atomic_C3_real_irreps":{"trivial":28,"rotation_planes":28},
            "max_C3_equivariant_linear_map_rank":max_equivariant_rank,
            "minimum_kernel_and_cokernel_each":4,
            "standard_C3_equivariant_bijection":"NO_GO for the ideal 28-atom 3D displacement representation versus UD active 84D chain",
            "dimension_match_status":"84-dimensional count matches but C3 characters differ; no standard symmetry-preserving bijection",
            "nontrivial_quotient_character_sum":0,
            "scope":"Planar ideal honeycomb geometry; no relaxed positions, contact mechanics, Hessian, friction, UD embedding, or empirical parameter."}
    (Path(__file__).parent/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\\n')
    print(json.dumps({"status":"PASS","index":7,"atoms":28,
                      "cosine":"13/14","angles":result['angle_degrees']}))

if __name__=='__main__':main()
