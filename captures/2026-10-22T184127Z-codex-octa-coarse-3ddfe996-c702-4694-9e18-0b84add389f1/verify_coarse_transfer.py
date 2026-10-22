"""Exact subdivision/retraction and unit-incidence dynamical leakage audit.

Uses only the Python standard library; no material parameters are inferred.
"""
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from pathlib import Path
import json


def mm(a, b):
    return [[sum(a[i][t] * b[t][j] for t in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def sub(a, b):
    return [[x - y for x, y in zip(row, other)] for row, other in zip(a, b)]


def zmat(n, m):
    return [[0] * m for _ in range(n)]


def trans(a):
    return [list(x) for x in zip(*a)]


def boundary(lower, upper):
    look = {s: i for i, s in enumerate(lower)}
    b = zmat(len(lower), len(upper))
    for j, simplex in enumerate(upper):
        for k in range(len(simplex)):
            b[look[simplex[:k] + simplex[k + 1:]]][j] = (-1) ** k
    return b


def orientation(seq):
    assert len(seq) == len(set(seq))
    return (-1) ** sum(seq[i] > seq[j] for i in range(len(seq))
                       for j in range(i + 1, len(seq)))


def determinant3(a, b, c):
    return (a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


def oriented_volume6(simplex, coords):
    u, v, w, z = [coords[i] for i in simplex]
    return determinant3(tuple(v[i] - u[i] for i in range(3)),
                        tuple(w[i] - u[i] for i in range(3)),
                        tuple(z[i] - u[i] for i in range(3)))


def signed_action(simplices, vertex_map):
    look = {s: i for i, s in enumerate(simplices)}
    a = zmat(len(simplices), len(simplices))
    for j, sigma in enumerate(simplices):
        image = [vertex_map[v] for v in sigma]
        a[look[tuple(sorted(image))]][j] = orientation(image)
    return a


def signed_simplicial_map(source, target, vertex_map):
    look = {s: i for i, s in enumerate(target)}
    d = zmat(len(target), len(source))
    for j, sigma in enumerate(source):
        image = [vertex_map[v] for v in sigma]
        if len(set(image)) == len(image):
            d[look[tuple(sorted(image))]][j] = orientation(image)
    return d


def equal_identity(a):
    return all(x == int(i == j) for i, row in enumerate(a)
               for j, x in enumerate(row))


def factor_result(x):
    if isinstance(x, Q):
        return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else x.numerator
    return x


def exact_charpoly(a):
    n = len(a)
    b = [[Q(int(i == j)) for j in range(n)] for i in range(n)]
    out = [Q(1)]
    for k in range(1, n + 1):
        t = mm(a, b)
        ck = -sum(t[i][i] for i in range(n)) / k
        out.append(ck)
        for i in range(n):
            t[i][i] += ck
        b = t
    assert not any(any(row) for row in b)
    return out


def poly_mul(a, b):
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def main():
    old_points = [(1, 1, 1), (1, -1, -1),
                  (-1, 1, -1), (-1, -1, 1)]
    old = [list(combinations(range(4), k + 1)) for k in range(4)]
    old_b = [boundary(old[k - 1], old[k]) for k in (1, 2, 3)]
    midpoint = {pair: tuple((old_points[pair[0]][k] + old_points[pair[1]][k]) // 2
                            for k in range(3))
                for pair in combinations(range(4), 2)}
    shell_xyz = [tuple(sign if axis == k else 0 for k in range(3))
                 for axis in range(3) for sign in (-1, 1)]
    shell_ids = {q: i for i, q in enumerate(shell_xyz)}
    mid_ids = {pair: shell_ids[q] for pair, q in midpoint.items()}
    assert set(mid_ids.values()) == set(range(6))
    # Fine IDs 0..5: edge midpoints, 6: centroid, 7..10: old vertices.
    xyz = shell_xyz + [(0, 0, 0)] + old_points
    inner = [tuple(sorted((6,) + tuple(shell_ids[tuple(s[axis] if axis == k
                         else 0 for k in range(3))] for axis in range(3))))
             for s in product((-1, 1), repeat=3)]
    corners = [tuple(sorted((7 + i,) + tuple(mid_ids[p]
                           for p in mid_ids if i in p))) for i in range(4)]
    cells = sorted(inner + corners)
    fine = [list(combinations(range(11), 1)),
            sorted(set(e for c in cells for e in combinations(c, 2))),
            sorted(set(f for c in cells for f in combinations(c, 3))), cells]
    assert [len(q) for q in fine] == [11, 30, 32, 12]
    fine_b = [boundary(fine[k - 1], fine[k]) for k in (1, 2, 3)]
    assert not any(any(row) for row in mm(fine_b[0], fine_b[1]))
    assert not any(any(row) for row in mm(fine_b[1], fine_b[2]))

    # Geometric subdivision S: old vertices, halved edges, quartered faces,
    # and all twelve correctly oriented 3-cells, respectively.
    subdivision = []
    for k in range(4):
        m = zmat(len(fine[k]), len(old[k]))
        lookup = {sigma: i for i, sigma in enumerate(fine[k])}
        for col, simplex in enumerate(old[k]):
            if k == 0:
                m[lookup[(7 + simplex[0],)]][col] = 1
            elif k == 1:
                i, j = simplex
                mid = mid_ids[(i, j)]
                for segment in ((7 + i, mid), (mid, 7 + j)):
                    m[lookup[tuple(sorted(segment))]][col] += orientation(segment)
            elif k == 2:
                i, j, h = simplex
                u, v, w = mid_ids[(i, j)], mid_ids[(i, h)], mid_ids[(j, h)]
                pieces = ((7 + i, u, v), (7 + j, u, w),
                          (7 + h, v, w), (u, v, w))
                def bary(t, index):
                    if t >= 7:
                        return 2 * int(t - 7 == index)
                    return int(index in next(pair for pair, n in mid_ids.items()
                                             if n == t))
                for piece in pieces:
                    t = tuple(sorted(piece))
                    a, b, c = [(bary(x, j), bary(x, h)) for x in t]
                    area2 = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
                    assert abs(area2) == 1
                    m[lookup[t]][col] = 1 if area2 > 0 else -1
            else:
                old_sigma = tuple(7 + x for x in simplex)
                old_sign = 1 if oriented_volume6(old_sigma, xyz) > 0 else -1
                for t in cells:
                    m[lookup[t]][col] = old_sign * (1 if oriented_volume6(t, xyz) > 0 else -1)
        subdivision.append(m)
    for k in (1, 2, 3):
        assert mm(fine_b[k - 1], subdivision[k]) == mm(subdivision[k - 1], old_b[k - 1])
    g = [1, 2, 4, 12]
    for k in range(4):
        gram = mm(trans(subdivision[k]), subdivision[k])
        assert gram == [[g[k] * int(i == j) for j in range(len(old[k]))]
                        for i in range(len(old[k]))]

    # A deterministic simplicial retraction exists, but assigning a fixed
    # old vertex to an edge midpoint breaks inherited S4 symmetry.
    old_of_fine = [min(pair for pair, index in mid_ids.items() if index == v)[0]
                   for v in range(6)] + [0] + list(range(4))
    d = [signed_simplicial_map(fine[k], old[k], old_of_fine)
         for k in range(4)]
    for k in range(4):
        assert equal_identity(mm(d[k], subdivision[k]))
    for k in (1, 2, 3):
        assert mm(old_b[k - 1], d[k]) == mm(d[k - 1], fine_b[k - 1])
    edge_stabilizer = [p for p in permutations(range(4))
                       if {p[0], p[1]} == {0, 1}]
    assert len(edge_stabilizer) == 4
    assert not any(all(p[v] == v for p in edge_stabilizer) for v in range(4))

    # Average conjugates of D to obtain an S4-equivariant rational chain
    # retraction. This remains a left inverse of the equivariant S.
    d_sym = [zmat(len(old[k]), len(fine[k])) for k in range(4)]
    actions = []
    for perm in permutations(range(4)):
        inv = tuple(perm.index(i) for i in range(4))
        def induced(p):
            f_map = [mid_ids[tuple(sorted(p[i] for i in pair))]
                     for pair in (next(pair for pair, n in mid_ids.items() if n == v)
                                  for v in range(6))]
            f_map += [6] + [7 + p[i] for i in range(4)]
            return ([signed_action(old[k], list(p)) for k in range(4)],
                    [signed_action(fine[k], f_map) for k in range(4)])
        ct, ft = induced(perm)
        _, ft_inv = induced(inv)
        actions.append((ct, ft))
        for k in range(4):
            assert mm(ft[k], subdivision[k]) == mm(subdivision[k], ct[k])
            piece = mm(mm(ct[k], d[k]), ft_inv[k])
            for i, row in enumerate(piece):
                for j, val in enumerate(row):
                    d_sym[k][i][j] += Q(val, 24)
    for k in range(4):
        assert equal_identity(mm(d_sym[k], subdivision[k]))
        for ct, ft in actions:
            assert mm(d_sym[k], ft[k]) == mm(ct[k], d_sym[k])
    for k in (1, 2, 3):
        assert mm(old_b[k - 1], d_sym[k]) == mm(d_sym[k - 1], fine_b[k - 1])

    # Orthogonal Euclidean least-squares projection is equivariant but fails
    # to be a chain map. The Gram-weighted projected skew generator is not
    # the original unit-weight tetrahedral generator.
    d_orth = [[[Q(x, g[k]) for x in row] for row in trans(subdivision[k])]
              for k in range(4)]
    orth_chain_fail = [sub(mm(old_b[k - 1], d_orth[k]),
                           mm(d_orth[k - 1], fine_b[k - 1])) for k in (1, 2, 3)]
    assert any(any(any(x for x in row) for row in mat) for mat in orth_chain_fail)

    no = sum(map(len, old))
    nf = sum(map(len, fine))
    assert (no, nf) == (15, 85)
    o_offsets, f_offsets = [0, 4, 10, 14], [0, 11, 41, 73]
    s = zmat(nf, no)
    for k in range(4):
        for i, row in enumerate(subdivision[k]):
            for j, x in enumerate(row):
                s[f_offsets[k] + i][o_offsets[k] + j] = x
    old_a, fine_a = zmat(no, no), zmat(nf, nf)
    for a, bs, offsets in ((old_a, old_b, o_offsets),
                           (fine_a, fine_b, f_offsets)):
        for k, b in enumerate(bs):
            for i, row in enumerate(b):
                for j, x in enumerate(row):
                    a[offsets[k] + i][offsets[k + 1] + j] = x
                    a[offsets[k + 1] + j][offsets[k] + i] = -x
    gs = [g[k] for k, grade in enumerate(old) for _ in grade]
    projected = [[Q(x, gs[i]) for x in row]
                 for i, row in enumerate(mm(mm(trans(s), fine_a), s))]
    for k, b in enumerate(old_b):
        lo, hi = o_offsets[k], o_offsets[k + 1]
        for i, row in enumerate(b):
            for j, x in enumerate(row):
                assert projected[lo + i][hi + j] == x
                assert projected[hi + j][lo + i] == -Q(g[k], g[k + 1]) * x
    assert projected != old_a
    projected_charpoly = exact_charpoly(projected)
    old_charpoly = exact_charpoly(old_a)
    expected_old = [Q(1), Q(0)]
    for _ in range(7):
        expected_old = poly_mul(expected_old, [Q(1), Q(0), Q(4)])
    assert old_charpoly == expected_old
    predicted = [Q(1), Q(0)]
    predicted = poly_mul(predicted, [Q(1), Q(0), Q(4, 3)])
    for _ in range(6):
        predicted = poly_mul(predicted, [Q(1), Q(0), Q(2)])
    assert projected_charpoly == predicted
    residual = sub(mm(fine_a, s), mm(s, projected))
    assert any(any(x for x in row) for row in residual)
    # Columns of S/sqrt(G) are orthonormal. These exact fractions are the
    # squared norms of the high-mode leakage per original chain basis.
    leak_col = [Q(sum(row[j] * row[j] for row in residual), gs[j])
                for j in range(no)]
    leak_by_grade = [sum(leak_col[o_offsets[k]:o_offsets[k] + len(old[k])])
                     for k in range(4)]
    assert leak_by_grade[3] == 0 and all(x >= 0 for x in leak_by_grade)
    leak_total = sum(leak_by_grade)
    assert leak_total > 0
    projected_action_sq = Q(2) * (Q(4, 3) + 6 * Q(2))
    assert projected_action_sq == Q(80, 3)
    total_action_sq = projected_action_sq + leak_total
    assert total_action_sq == Q(124, 3)
    leakage_action_fraction = leak_total / total_action_sq
    assert leakage_action_fraction == Q(11, 31)

    result = {
        "lane": "Development; exact finite chain/refinement; physical promotion 0",
        "base_capture": "2026-10-22T183342Z-codex-centered-octahedron-03df6bff-dcf6-4dee-b364-9b170b4885c5",
        "coarse_f": [4, 6, 4, 1], "fine_f": [11, 30, 32, 12],
        "subdivision_gram_by_grade": g,
        "subdivision_is_chain_map": True,
        "deterministic_retraction_is_chain_map_and_left_inverse": True,
        "S4_equivariant_retraction_exists_over_rationals": True,
        "S4_equivariant_deterministic_vertex_retraction_exists": False,
        "orthogonal_projection_chain_map": False,
        "orthogonal_projection_chain_residual_entries":
            [sum(bool(x) for row in m for x in row) for m in orth_chain_fail],
        "projected_orthonormal_incidence_couplings_squared":
            ["1/2", "1/2", "1/3"],
        "unit_incidence_dynamic_intertwiner": False,
        "projected_coarse_characteristic_polynomial_descending":
            [factor_result(x) for x in projected_charpoly],
        "projected_coarse_characteristic_polynomial_factored":
            "lambda*(lambda^2+4/3)*(lambda^2+2)^6",
        "seed_unit_incidence_characteristic_polynomial_factored":
            "lambda*(lambda^2+4)^7",
        "leakage_frobenius_squared_by_coarse_grade":
            [factor_result(x) for x in leak_by_grade],
        "leakage_frobenius_squared_total": factor_result(leak_total),
        "projected_action_frobenius_squared": factor_result(projected_action_sq),
        "total_action_frobenius_squared": factor_result(total_action_sq),
        "leakage_fraction_of_squared_action": factor_result(leakage_action_fraction),
        "leakage_squares_per_coarse_basis": [factor_result(x) for x in leak_col],
        "scope": "Unit simplex inner products only; no material-metric or graphite-port claim."
    }
    (Path(__file__).parent / "RESULTS.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "gram": g,
                      "leak_by_grade": result["leakage_frobenius_squared_by_coarse_grade"],
                      "leak_total": result["leakage_frobenius_squared_total"]}))


if __name__ == "__main__":
    main()
