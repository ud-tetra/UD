"""Exact constructor audit of synchronous barycentric refinement of a tetrahedron.

This proposed renewal rule is not sourced by native UD admission dynamics.
"""
import itertools
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


def avg(points):
    n = len(points)
    return tuple(sum(p[d] for p in points) / n for d in range(3))


def subdivide(tetrahedra):
    next_tets = set()
    for tet in tetrahedra:
        for perm in itertools.permutations(tet):
            flag = tuple(avg(perm[:j]) for j in range(1, 5))
            assert len(set(flag)) == 4
            next_tets.add(tuple(sorted(flag)))
    return next_tets


origin = (Fraction(0), Fraction(0), Fraction(0))
standard = tuple(sorted((origin, (Fraction(1), Fraction(0), Fraction(0)),
                         (Fraction(0), Fraction(1), Fraction(0)),
                         (Fraction(0), Fraction(0), Fraction(1)))))
tetrahedra = {standard}
counts = []
for depth in range(4):
    verts = {v for tet in tetrahedra for v in tet}
    neighbors = {v for tet in tetrahedra if origin in tet for v in tet if v != origin}
    original_incident = sum(origin in tet for tet in tetrahedra)
    counts.append(dict(depth=depth,tetrahedra=len(tetrahedra),vertices=len(verts),
                       degree_original_vertex=len(neighbors),
                       incident_tetrahedra=original_incident))
    assert len(tetrahedra) == 24**depth
    assert original_incident == 6**depth
    assert len(neighbors) >= (6**(depth - 1) if depth else 3)
    if depth < 3:
        tetrahedra = subdivide(tetrahedra)


# Barycentric chain subdivision of an oriented edge [a,b] is [a,m]+[m,b].
# Using oriented-edge incidence dictionaries, its boundary is [b]-[a].
def boundary_edge(edge):
    return {edge[0]: -1, edge[1]: 1}


a, m, b = 0, 1, 2
bd = {a: 0, m: 0, b: 0}
for edge in ((a, m), (m, b)):
    for v, c in boundary_edge(edge).items():
        bd[v] += c
assert bd == {a: -1, m: 0, b: 1}
# On a single old edge, A_old(a)=-[a,b]. After subdivision,
# A_new(S_0 a)=-[a,m], while S_1(A_old a)=-[a,m]-[m,b].
A_new_on_a = {edge: boundary_edge(edge).get(a, 0) for edge in ((a, m), (m, b))}
S_A_old_on_a = {edge: boundary_edge((a, b))[a] for edge in ((a, m), (m, b))}
assert A_new_on_a == {(a, m): -1, (m, b): 0}
assert S_A_old_on_a == {(a, m): -1, (m, b): -1}

# Sum-of-squared coefficients of the unnormalized subdivisions by grade;
# supports of distinct original same-grade simplices do not overlap.
child_counts = [1, 2, 6, 24]
assert child_counts == [__import__('math').factorial(k + 1) for k in range(4)]


def sign_of_permutation(items, parent):
    positions = [parent.index(x) for x in items]
    return (-1) ** sum(positions[i] > positions[j]
                       for i in range(len(items)) for j in range(i + 1, len(items)))


def subdivided_chain(parent):
    chain = defaultdict(int)
    for perm in itertools.permutations(parent):
        flags = tuple(frozenset(perm[:j]) for j in range(1, len(parent) + 1))
        chain[flags] += sign_of_permutation(perm, parent)
    return dict(chain)


def chain_boundary(chain):
    out = defaultdict(int)
    for simplex, coeff in chain.items():
        for i in range(len(simplex)):
            out[simplex[:i] + simplex[i + 1:]] += (-1) ** i * coeff
    return {x: c for x, c in out.items() if c}


for k in range(1, 4):
    parent = tuple(range(k + 1))
    left = chain_boundary(subdivided_chain(parent))
    right = defaultdict(int)
    for i in range(k + 1):
        for x, c in subdivided_chain(parent[:i] + parent[i + 1:]).items():
            right[x] += (-1) ** i * c
    assert left == {x: c for x, c in right.items() if c}
# T_k=S_k/sqrt((k+1)!) makes a grade isometry; boundary intertwining
# coefficient is sqrt(k!/(k+1)!)=1/sqrt(k+1), unequal to one for k>=1.
out = dict(
    status="PASS",
    candidate="simultaneous supplied-tick barycentric subdivision with either standard chain transfer S or grade-isometric T",
    recursion=counts,
    full_mesh_tetra_factor=24,
    corner_incident_tetra_factor=6,
    unnormalized_subdivision_norm_squared_by_grade=child_counts,
    degree_original_vertex_unbounded=True,
    edge_boundary_intertwining_unnormalized=True,
    all_grades_boundary_intertwining_unnormalized=True,
    edge_boundary_intertwining_grade_isometric=False,
    edge_generator_intertwining_unnormalized=False,
    max_diameter_contracts_at_most="(3/4)^n times initial diameter",
    native_event_trigger="NOT_DERIVED",
    physical_clock_and_common_cone="OPEN",
    physical_promotion=0,
)
Path(__file__).with_name("results.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
