"""Exact icosahedron chain/spectrum and a T=7 patch-selection counterexample.

No archived research script is executed. Python standard library only.
"""
import json
import math
from collections import Counter
from itertools import combinations, product
from pathlib import Path


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def neg(x):
    return -x[0], -x[1]


def mul(x, y):
    # x and y represent a + b*phi, phi**2=phi+1.
    return (x[0] * y[0] + x[1] * y[1],
            x[0] * y[1] + x[1] * y[0] + x[1] * y[1])


def squared_distance(x, y):
    out = (0, 0)
    for a, b in zip(x, y):
        d = add(a, neg(b))
        out = add(out, mul(d, d))
    return out


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def gram(b, left=True):
    n = len(b) if left else len(b[0])
    m = len(b[0]) if left else len(b)
    return [[sum((b[i][k] * b[j][k] if left else b[k][i] * b[k][j])
                 for k in range(m)) for j in range(n)] for i in range(n)]


def integer_charpoly(a):
    # Faddeev-LeVerrier with arbitrary-precision integers; last matrix must vanish.
    n = len(a)
    b = [[int(i == j) for j in range(n)] for i in range(n)]
    coefficients = [1]
    for k in range(1, n + 1):
        t = matmul(a, b)
        trace = sum(t[i][i] for i in range(n))
        assert trace % k == 0
        ck = -trace // k
        coefficients.append(ck)
        for i in range(n):
            t[i][i] += ck
        b = t
    assert not any(any(row) for row in b)
    return coefficients


def product_poly(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result


def factored_poly(factors):
    result = [1]
    for factor, power in factors:
        for _ in range(power):
            result = product_poly(result, factor)
    return result


def main():
    zero = (0, 0)
    vertices = set()
    for a, b in product((-1, 1), repeat=2):
        vertices.update(((zero, (a, 0), (0, b)),
                         ((a, 0), (0, b), zero),
                         ((0, a), zero, (b, 0))))
    vertices = sorted(vertices)  # icosahedron coordinates in Z[phi]^3
    edges = [(i, j) for i, j in combinations(range(12), 2)
             if squared_distance(vertices[i], vertices[j]) == (4, 0)]
    edge_set = set(edges)
    faces = [(a, b, c) for a, b, c in combinations(range(12), 3)
             if (a, b) in edge_set and (a, c) in edge_set and (b, c) in edge_set]
    assert (len(vertices), len(edges), len(faces)) == (12, 30, 20)
    assert Counter(sum(i in e for e in edges) for i in range(12)) == {5: 12}
    b1 = [[0] * 30 for _ in range(12)]
    b2 = [[0] * 20 for _ in range(30)]
    lookup = {edge: j for j, edge in enumerate(edges)}
    for j, (a, b) in enumerate(edges):
        b1[a][j], b1[b][j] = -1, 1
    for j, (a, b, c) in enumerate(faces):
        for edge, sign in (((b, c), 1), ((a, c), -1), ((a, b), 1)):
            b2[lookup[edge]][j] = sign
    assert all(sum(b1[i][e] * b2[e][f] for e in range(30)) == 0
               for i in range(12) for f in range(20))
    assert all(sum(abs(x) for x in row) == 2 for row in b2)

    l0 = integer_charpoly(gram(b1))
    l2 = integer_charpoly(gram(b2, left=False))
    f0 = [([1, 0], 1), ([1, -6], 5), ([1, -10, 20], 3)]
    f2 = [([1, 0], 1), ([1, -2], 5), ([1, -3], 4),
          ([1, -5], 4), ([1, -6, 4], 3)]
    assert l0 == factored_poly(f0)
    assert l2 == factored_poly(f2)
    # Symmetric Gram matrices: simple zero factors give ranks 11 and 19.
    assert (l0[-2] != 0 and l0[-1] == 0 and
            l2[-2] != 0 and l2[-1] == 0)
    assert 11 + 19 == 30  # A has 30 oscillator pairs and 2 harmonic zeros.

    # A straight-boundary patch of area seven is NOT the standard Goldberg patch.
    # u=(2,1), v=R60 u=(-1,3), det(u,v)=7. These six points include
    # only the three corners on the macro boundary. The seven little faces
    # have lattice determinant one but need not be equilateral/unit edges.
    points = [(-1, 3), (0, 0), (0, 1), (0, 2), (1, 1), (2, 1)]
    triangles = [(0, 1, 2), (0, 2, 3), (0, 3, 5), (1, 2, 4),
                 (1, 4, 5), (2, 3, 4), (3, 4, 5)]
    def inside(p):
        alpha7 = 3 * p[0] + p[1]
        beta7 = -p[0] + 2 * p[1]
        return alpha7 >= 0 and beta7 >= 0 and alpha7 + beta7 <= 7
    assert all(inside(p) for p in points)
    dets = [abs((points[b][0] - points[a][0]) * (points[c][1] - points[a][1])
                - (points[c][0] - points[a][0]) * (points[b][1] - points[a][1]))
            for a, b, c in triangles]
    assert dets == [1] * 7
    patch_edges = Counter(tuple(sorted(pair)) for t in triangles for pair in
                          ((t[0], t[1]), (t[0], t[2]), (t[1], t[2])))
    assert len(patch_edges) == 12
    assert {e for e, count in patch_edges.items() if count == 1} == {(0, 1), (0, 5), (1, 5)}
    assert all(count in (1, 2) for count in patch_edges.values())
    patch_degrees = Counter(v for e in patch_edges for v in e)
    assert patch_degrees == {i: 4 for i in range(6)}
    assert 6 - 12 + 7 == 1  # patch disk
    T = 2 * 2 + 2 * 1 + 1 * 1
    V, E, F = 10 * T + 2, 30 * T, 20 * T
    assert (V, E, F) == (72, 210, 140) and V - E + F == 2
    # Gluing this particular patch along original macro edges has the SAME
    # f-vector but different valences. At an old corner, five patches each
    # bring two non-boundary incident edges plus five shared macro edges.
    old_degree = 5 * (patch_degrees[0] - 2) + 5
    new_degree = patch_degrees[2]
    assert (old_degree, new_degree) == (15, 4)
    assert 12 * old_degree + (V - 12) * new_degree == 2 * E
    assert 12 * (6 - old_degree) + (V - 12) * (6 - new_degree) == 12
    # A standard Goldberg/Caspar-Klug T7 construction has degree 5/6,
    # consistent with these counts, but is not constructed by this script.
    assert 12 * 5 + (V - 12) * 6 == 2 * E
    assert (V - 1, E - (V - 1)) == (71, 139)  # sphere homology and rank-nullity

    # Macro-edge orientation alpha is distinct from the graphene twist theta.
    alpha = math.degrees(math.atan(math.sqrt(3) / 5))
    theta = math.degrees(math.acos(13 / 14))
    assert abs((60 - 2 * alpha) - theta) < 1e-12
    assert abs(2 * alpha - (60 - theta)) < 1e-12
    result = {
        "lane": "Development — no registry entry", "physical_promotion": 0,
        "regular_icosahedron": {"f_vector": [12, 30, 20], "chain_dimension": 62,
            "betti": [1, 0, 1], "boundary_ranks": [11, 19],
            "face_count_per_vertex": 5, "angle_defect_per_vertex_degrees": 60,
            "total_angle_defect_degrees": 720,
            "l0_charpoly_descending": l0, "l2_charpoly_descending": l2,
            "hodge_dirac_zero_modes": 2, "hodge_dirac_oscillator_pairs": 30},
        "T7_straight_patch_counterexample": {"indices": [2, 1], "T": T,
            "patch_points": points, "patch_triangles": triangles,
            "patch_degrees": [patch_degrees[i] for i in range(6)],
            "glued_degree15_old_vertices": 12,
            "glued_degree4_new_vertices": V - 12,
            "f_vector": [V, E, F],
            "chain_dimension": V + E + F,
            "boundary_ranks_from_sphere_homology": [V - 1, E - (V - 1)],
            "hodge_dirac_zero_modes": 2, "hodge_dirac_oscillator_pairs": E},
        "standard_Goldberg_T7_literature_pattern_not_constructed_here": {
            "f_vector": [V, E, F], "degree5_vertices": 12,
            "degree6_vertices": V - 12,
            "dual_fullerene_pentagons": 12,
            "dual_fullerene_hexagons": V - 12,
            "dual_fullerene_vertex_count": F},
        "angles_degrees": {"icosadelta_macro_edge_alpha": alpha,
            "mirror_macro_edge_60_minus_alpha": 60 - alpha,
            "graphite_twist_theta": theta,
            "graphite_twist_complement": 60 - theta,
            "identity": "theta=60-2 alpha; 60-theta=2 alpha"},
    }
    (Path(__file__).parent / "RESULTS.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "PASS_EXACT_INTEGER_CHECKS", "f": [12, 30, 20],
                      "T7_f": [V, E, F], "theta": theta, "alpha": alpha}))


if __name__ == "__main__":
    main()
