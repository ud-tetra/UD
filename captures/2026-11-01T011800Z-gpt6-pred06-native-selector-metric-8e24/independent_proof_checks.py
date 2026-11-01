#!/usr/bin/env python3
"""Independent exact finite checks for UD PRED06 conditional theorems.
This script does not establish source-native physics or non-constructor review.
Requires SymPy>=1.12. It uses exact rationals only.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from math import factorial
from pathlib import Path
import json
import sympy as sp

V = tuple(range(4))
E = tuple(combinations(V, 2))
PERMS = list(permutations(V))


def s4_checks():
    assert len(PERMS) == factorial(4) == 24
    common_fixed_vertices = [v for v in V if all(p[v] == v for p in PERMS)]
    common_fixed_edges = [e for e in E if all(tuple(sorted((p[e[0]],p[e[1]]))) == e for p in PERMS)]
    fixed_first = [p for p in PERMS if p[0] == 0]
    neighbor_orbit = {p[1] for p in fixed_first}
    assert len(fixed_first) == 6
    assert not common_fixed_vertices and not common_fixed_edges
    assert neighbor_orbit == {1, 2, 3}
    return {
        "s4_order": len(PERMS),
        "common_fixed_vertices": common_fixed_vertices,
        "common_fixed_unoriented_edges": common_fixed_edges,
        "vertex_stabilizer_order": len(fixed_first),
        "neighbor_orbit_after_vertex_seed": sorted(neighbor_orbit),
    }


def flux_selector(b, gates=None, threshold=0):
    """Conditional strict-local-peak burden selector on *one* K4 packet.
    Returns a vertex and flux-maximizing outgoing edge, or None on degeneracy.
    The decision predicate is newly assumed; Q162 supplies flux formula only.
    """
    if gates is None:
        gates = {e: 1 for e in E}
    peaks = [v for v in V if b[v] > threshold and all(b[v] > b[w] for w in V if w != v)]
    if len(peaks) != 1:
        return None
    v = peaks[0]
    current = []
    for w in V:
        if w != v:
            h = gates[tuple(sorted((v, w)))]
            j = sp.Rational(1, 4) * h * (b[v] - b[w])
            if j > 0:
                current.append((w, j))
    if not current:
        return None
    maxj = max(j for _, j in current)
    winning = [w for w, j in current if j == maxj]
    if len(winning) != 1:
        return None
    return (v, winning[0], maxj)


def selector_checks():
    b = (sp.Rational(4), sp.Rational(3), sp.Rational(2), sp.Rational(0))
    result = flux_selector(b)
    assert result == (0, 3, sp.Rational(1))
    equivariant = True
    for p in PERMS:
        moved_b = [None] * 4
        for v in V:
            moved_b[p[v]] = b[v]
        res = flux_selector(tuple(moved_b))
        if res != (p[0], p[3], sp.Rational(1)):
            equivariant = False
    assert equivariant
    assert flux_selector((1, 1, 1, 1)) is None
    assert flux_selector((4, 1, 1, 1)) is None  # outgoing flux ties, no port
    assert flux_selector((1, 2, 3, 4), gates={e: 0 for e in E}) is None
    return {"example_burden": [str(x) for x in b],
            "selected_source_vertex": result[0], "selected_outgoing_vertex": result[1],
            "selected_native_flux": str(result[2]), "s4_equivariant_24_actions": equivariant,
            "uniform_input": "NO_SELECTOR", "port_tie": "NO_SELECTOR", "all_gates_closed": "NO_SELECTOR"}


def parity_checks():
    # A homomorphism from Z2^3 to Z must vanish because f(x)+f(x)=f(0)=0.
    states=list(product([0,1], repeat=3))
    add=lambda x,y: tuple((a+b) % 2 for a,b in zip(x,y))
    cases=0; valid=[]
    for coeff in product(range(-2,3), repeat=3):
        f=lambda x:sum(a*b for a,b in zip(coeff,x))
        ok=all(f(add(x,y))==f(x)+f(y) for x in states for y in states)
        cases+=1
        if ok:valid.append(coeff)
    assert valid==[(0,0,0)]
    return {"Theta": "Z2^3", "states": len(states), "candidate_generator_images_tested": cases,
            "additive_integer_homomorphisms_in_range": [list(x) for x in valid],
            "full_proof": "2*f(x)=f(2*x)=f(0)=0 in Z, hence f(x)=0 for all x"}


def diffusion_checks():
    B=sp.zeros(4,6)
    for col,(u,v) in enumerate(E):
        B[u,col]=-1;B[v,col]=1
    L=B*B.T
    uniform=sp.Matrix([1]*4)
    contrast=sp.Matrix([4,3,2,0])
    assert L*uniform==sp.zeros(4,1)
    derivative=-(sp.Rational(1,4))*L*contrast
    assert (sp.ones(1,4)*derivative)[0]==0
    quadratic=-(sp.Rational(1,4))*(contrast.T*L*contrast)[0]
    assert quadratic < 0
    assert all(x==0 for x in (-(sp.Rational(1,4))*L*uniform))
    return {"Laplacian_eigenvalues":{str(k):int(v) for k,v in L.eigenvals().items()},
            "homogeneous_stationary":True,"mean_burden_conserved":True,
            "contrast_energy_derivative":str(quadratic),"divergence_only_cannot_generate_cell_excision":True}


def face_boundary(edges, faces):
    idx={e:k for k,e in enumerate(edges)}
    B2=sp.zeros(len(edges),len(faces))
    for j,(a,b,c) in enumerate(faces):
        for u,v in ((a,b),(b,c),(c,a)):
            e=tuple(sorted((u,v)))
            B2[idx[e],j]+=1 if (u,v)==e else -1
    return B2


def annulus_exact():
    # Simple triangulated annulus, independent of earlier Freudenthal code.
    faces=[]
    for i in range(4):
        j=(i+1)%4
        faces.append((i,j,4+j))
        faces.append((i,4+j,4+i))
    edges=sorted({tuple(sorted(e)) for face in faces for e in combinations(face,2)})
    B1=sp.zeros(8,len(edges))
    for j,(u,v) in enumerate(edges):B1[u,j]=-1;B1[v,j]=1
    B2=face_boundary(edges,faces)
    assert B1*B2==sp.zeros(8,len(faces))
    assert B1.rank()==7 and B2.rank()==8
    # Inner cycle I0->I1->I2->I3->I0, with orientation relative to sorted edges.
    row=sp.zeros(1,len(edges)); emap={e:j for j,e in enumerate(edges)}
    for i in range(4):
        u=4+i;v=4+(i+1)%4;e=tuple(sorted((u,v)))
        row[0,emap[e]]+=1 if (u,v)==e else -1
    M=B2.T.col_join(B1).col_join(row)
    rhs=sp.zeros(M.rows,1);rhs[M.rows-1]=1
    assert M.rank()==len(edges)
    h=next(iter(sp.linsolve((M,rhs))))
    h=sp.Matrix(h)
    assert B1*h==sp.zeros(8,1) and B2.T*h==sp.zeros(8,1) and (row*h)[0]==1
    P=(h.T*h)[0]
    assert P>0
    # Incidence-count metric is a positive *candidate* local metric, not a source-derived unique one.
    deg=[sum(abs(B2[j,k]) for k in range(B2.cols)) for j in range(B2.rows)]
    G=sp.diag(*deg)
    assert min(deg)==1 and max(deg)==2
    Mg=B2.T.col_join(B1*G).col_join(row)
    assert Mg.rank()==len(edges)
    hw=sp.Matrix(next(iter(sp.linsolve((Mg,rhs)))))
    assert B2.T*hw==sp.zeros(B2.cols,1) and B1*G*hw==sp.zeros(8,1)
    Pg=(hw.T*G*hw)[0]
    assert P<=Pg<=2*P
    # Flatness/harmonic blindness for each nonzero period sector, all n.
    for n in (-3,-2,-1,0,1,2,3):
        assert B2.T*(n*h)==sp.zeros(B2.cols,1)
        assert B1*(n*h)==sp.zeros(B1.rows,1)
    # Even perfect knowledge of a quadratic form identifies only lambda*G.
    lam=sp.Rational(3,7);c=sp.Rational(5,2)
    sample=sp.Matrix(range(1,len(edges)+1))
    assert lam*(sample.T*G*sample)[0]==(lam/c)*(sample.T*(c*G)*sample)[0]
    return {"toy":"eight-triangle planar annulus", "vertices":8,"edges":len(edges),"faces":8,
            "ranks_B1_B2":[B1.rank(),B2.rank()],"betti_1":len(edges)-B1.rank()-B2.rank(),
            "inner_period":str((row*h)[0]),"unweighted_harmonic_norm_sq":str(P),
            "incidence_metric_diagonal_multiplicities":{str(k):v for k,v in Counter(deg).items()},
            "weighted_harmonic_norm_sq":str(Pg),
            "unit_metric_hodge_zero":True, "weighted_coflatness":True,
            "sector_curvature_action_gap":"0", "quadratic_scale_pair_invariant":True}


def harmonic_bounds_checks():
    # Source theorem PRED05-SCALE-002 is assumed; this checks exact propagation of inequalities.
    rows=[]
    for N in (4,6,8,16,32,64,128):
        m=N//2
        H=sum((sp.Rational(1,r) for r in range(1,m+1)),sp.Rational(0))
        c=sp.Rational(1,2);C=sp.Rational(3)
        lo=(3*c*H)/8;hi=336*C*H
        # kappa=1/H gives a finite nonzero *conditional* gap from inherited bounds.
        k=1/H
        gap_lower=sp.Rational(5,2)*k*lo
        gap_upper=sp.Rational(5,2)*k*hi
        assert gap_lower == sp.Rational(15,16)*c
        assert gap_upper == 840*C
        rows.append({"N":N,"H_halfN":str(H),"P_metric_lower":str(lo),
                     "P_metric_upper":str(hi), "kappa_example_inverse_H":"1/H", "gap_lower":str(gap_lower),
                     "gap_upper":str(gap_upper)})
    return {"ellipticity":"c=1/2,C=3 independent of N", "inherited_source_bounds": "3/8 H_m <= P_I <= 336 H_m",
            "generalized":"(3c/8)H_m <= P_G <= 336C H_m",
            "gap":"(5/2)kappa_N P_G", "kappa_necessary_if_gap_bounded":"Theta(1/H_m)",
            "corollary":"fixed positive kappa diverges for uniformly elliptic metric", "rows":rows}


def main():
    v={"status":"EXACT_CONDITIONAL_FINITE_CHECKS_ONLY", "review":"DEFERRED", "physical_promotion":0,
       "symmetry":s4_checks(),"conditional_selector":selector_checks(),"parity":parity_checks(),
       "diffusion":diffusion_checks(),"cochain":annulus_exact(),"elliptic_metric":harmonic_bounds_checks()}
    path=Path(__file__).with_name("EXACT_AUDIT.json")
    path.write_text(json.dumps(v,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v[k] for k in ("symmetry","conditional_selector","parity","diffusion","cochain")},indent=2))
    return v

if __name__=="__main__":main()
