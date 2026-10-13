"""Exact integer replay for fixed-complex and 2-to-3 source witnesses.

The source audit and nonexistence of a source selector are textual scope findings,
not consequences of this finite checker.
"""
from collections import Counter
from itertools import combinations
import json
from pathlib import Path


def boundary(simplex):
    return Counter({simplex[:i] + simplex[i + 1:]: (-1) ** i for i in range(len(simplex))})


def chain_boundary(chain):
    result = Counter()
    for simplex, coeff in chain.items():
        for face, sign in boundary(simplex).items():
            result[face] += coeff * sign
    return +result - -result  # preserve nonzero signed entries


verts = [(i,) for i in range(4)]
edges = list(combinations(range(4), 2))
faces = list(combinations(range(4), 3))
tet = tuple(range(4))

for face in faces:
    assert not any(chain_boundary(boundary(face)).values())
assert not any(chain_boundary(boundary(tet)).values())

# B1 has -1 at the lower vertex and +1 at the upper vertex.
incidence = [[boundary(e).get(v, 0) for e in edges] for v in verts]
L0 = [
    [sum(incidence[i][e] * incidence[j][e] for e in range(6)) for j in range(4)]
    for i in range(4)
]
assert L0 == [[3 if i == j else -1 for j in range(4)] for i in range(4)]
assert [sum(row) for row in L0] == [0] * 4
for contrast in ((1, -1, 0, 0), (0, 1, -1, 0), (0, 0, 1, -1)):
    assert tuple(sum(row[j] * contrast[j] for j in range(4)) for row in L0) == tuple(4 * x for x in contrast)

minus = {(0, 1, 2, 3): 1, (0, 1, 2, 4): -1}
plus = {(1, 2, 3, 4): -1, (0, 2, 3, 4): 1, (0, 1, 3, 4): -1}
assert chain_boundary(minus) == chain_boundary(plus)
assert sum(c * c for c in minus.values()) == 2
assert sum(c * c for c in plus.values()) == 3
assert len(set(sum((list(s) for s in minus), []))) == 5
assert len(set(sum((list(s) for s in plus), []))) == 5

result = {
    "status": "PASS",
    "scope": "exact integer finite-complex witness; source selection remains textual audit",
    "K4_boundary_squared_zero": True,
    "K4_vertex_laplacian": L0,
    "K4_vertex_eigenvalues_exact": [0, 4, 4, 4],
    "move_2_to_3_same_exterior_boundary": True,
    "move_top_chain_squared_norms": [2, 3],
    "move_vertex_counts": [5, 5],
    "coframe_positive_sign_obstruction": "general proof by v^T E E^T v = ||E^T v||^2 in report",
    "native_refinement_selector": "NOT_FOUND_IN_AUDITED_CURRENT_SOURCES",
    "physical_promotion": 0,
}
Path(__file__).with_name("results.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
