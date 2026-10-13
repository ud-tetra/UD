"""Exact local-symbol calculation and finite periodic-chain replay.

Development calculation. The periodic Freudenthal family is supplied, not
selected by the native UD event/admission law.
"""
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.sparse import dok_matrix


S = tuple(v for v in itertools.product((0, 1), repeat=3) if any(v))
C = [[sum(v[i] * v[j] for v in S) for j in range(3)] for i in range(3)]
assert C == [[4, 2, 2], [2, 4, 2], [2, 2, 4]]
assert np.linalg.eigvalsh(np.array(C)).round(12).tolist() == [2.0, 2.0, 8.0]


def periodic_complex(n):
    """Triangulate each cube into six tetrahedra on the n^3 periodic torus."""
    vertices = list(itertools.product(range(n), repeat=3))
    index = {p: i for i, p in enumerate(vertices)}
    cells = set()
    for p in vertices:
        for perm in itertools.permutations(range(3)):
            q = list(p)
            tet = [index[tuple(q)]]
            for d in perm:
                q[d] = (q[d] + 1) % n
                tet.append(index[tuple(q)])
            cells.add(tuple(sorted(tet)))
    faces = sorted({tuple(sorted(t)) for cell in cells for t in itertools.combinations(cell, 3)})
    edges = sorted({tuple(sorted(t)) for cell in cells for t in itertools.combinations(cell, 2)})
    return vertices, edges, faces, sorted(cells)


def boundary(higher, lower):
    lookup = {c: i for i, c in enumerate(lower)}
    m = dok_matrix((len(lower), len(higher)), dtype=np.int64)
    for j, c in enumerate(higher):
        for i in range(len(c)):
            face = c[:i] + c[i + 1 :]
            m[lookup[face], j] = (-1) ** i
    return m.tocsr()


n = 4
vertices, edges, faces, cells = periodic_complex(n)
assert len(vertices) == n**3 and len(cells) == 6 * n**3
B1 = boundary(edges, [(i,) for i in range(len(vertices))])
B2 = boundary(faces, edges)
B3 = boundary(cells, faces)
assert (B1 @ B2).nnz == 0 and (B2 @ B3).nnz == 0
L0 = (B1 @ B1.T).toarray()
assert np.array_equal(L0, L0.T)
for p in vertices:
    i = vertices.index(p)
    offsets = {vertices[j] for j in np.flatnonzero(L0[i] == -1)}
    expected = {
        tuple((p[d] + sign * v[d]) % n for d in range(3))
        for v in S for sign in (-1, 1)
    }
    assert len(offsets) == 14 and offsets == expected
assert set(np.diag(L0)) == {14}

# Independent finite-matrix check of the offset-derived dispersion relation.
mode = np.array([np.exp(2j * math.pi * (p[0] + 2 * p[1]) / n) for p in vertices])
lambda_mode = 2 * sum(
    1 - math.cos(2 * math.pi * (v[0] + 2 * v[1]) / n) for v in S
)
assert np.max(np.abs(L0 @ mode - lambda_mode * mode)) < 1e-12


def symbol(a, k):
    return 2 * sum(1 - math.cos(a * sum(v[i] * k[i] for i in range(3))) for v in S) / a**2


k = (Fraction(1), Fraction(2), Fraction(3))
limit = sum(k[i] * C[i][j] * k[j] for i in range(3) for j in range(3))
assert limit == 100
values = [symbol(1 / n, tuple(map(float, k))) for n in (16, 32, 64, 128)]
errors = [abs(z - float(limit)) for z in values]
assert all(errors[i + 1] < errors[i] for i in range(len(errors) - 1))
assert 3.8 < errors[-2] / errors[-1] < 4.2

out = {
    "status": "PASS",
    "scope": "supplied periodic Freudenthal tetrahedral family with UD unit-incidence skew generator",
    "cells_at_n4": {"vertices": len(vertices), "edges": len(edges), "faces": len(faces), "tetrahedra": len(cells)},
    "boundary_squared_zero": True,
    "vertex_graph_degree": 14,
    "finite_fourier_mode_check": True,
    "positive_offsets": [list(v) for v in S],
    "C_exact": C,
    "C_eigenvalues_exact": [2, 2, 8],
    "symbol_exact": "2/a^2 sum_{v in S} [1-cos(a k.v)]",
    "continuum_principal_symbol": "-omega^2 + k^T C k (in supplied t=a*s and x=a*m charts)",
    "sample_wavevector": [1, 2, 3],
    "sample_limit_exact": str(limit),
    "sample_errors_n16_32_64_128": errors,
    "icosahedron_surface_intrinsic_dimension": 2,
    "UD_native_family_selector": "OPEN",
    "physical_clock_and_GR_metric": "OPEN",
    "physical_promotion": 0,
}
Path(__file__).with_name("results.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
