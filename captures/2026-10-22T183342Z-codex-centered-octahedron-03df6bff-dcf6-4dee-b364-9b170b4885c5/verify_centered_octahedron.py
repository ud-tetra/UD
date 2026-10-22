"""Exact, standard-library audit of the tetrahedron-edge-midpoint octahedron.

This script constructs the simplicial ball and its boundary; it does not use
archived research scripts, material coefficients or experimental data.
"""
from collections import Counter
from itertools import combinations, permutations, product
from fractions import Fraction
import json
from pathlib import Path


def mm(a, b):
    n, k, m = len(a), len(b), len(b[0])
    return [[sum(a[i][t] * b[t][j] for t in range(k)) for j in range(m)]
            for i in range(n)]


def gram(b, right=False):
    if right:
        return [[sum(b[k][i] * b[k][j] for k in range(len(b)))
                 for j in range(len(b[0]))] for i in range(len(b[0]))]
    return [[sum(b[i][k] * b[j][k] for k in range(len(b[0])))
             for j in range(len(b))] for i in range(len(b))]


def charpoly(m):
    """Descending coefficients via exact Faddeev–LeVerrier."""
    n = len(m)
    q = [[int(i == j) for j in range(n)] for i in range(n)]
    coeff = [1]
    for k in range(1, n + 1):
        t = mm(m, q)
        trace = sum(t[i][i] for i in range(n))
        assert trace % k == 0
        c = -trace // k
        coeff.append(c)
        for i in range(n):
            t[i][i] += c
        q = t
    assert all(all(x == 0 for x in row) for row in q)
    return coeff


def poly_product(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def factor_product(items):
    p = [1]
    for base, power in items:
        for _ in range(power):
            p = poly_product(p, base)
    return p


def make_boundary(lower, upper):
    index = {simplex: j for j, simplex in enumerate(lower)}
    b = [[0] * len(upper) for _ in lower]
    for j, simplex in enumerate(upper):
        for k in range(len(simplex)):
            face = simplex[:k] + simplex[k + 1:]
            b[index[face]][j] = (-1) ** k
    return b


def rank_q(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    pivot = 0
    for col in range(len(a[0])):
        first = next((r for r in range(pivot, len(a)) if a[r][col]), None)
        if first is None:
            continue
        a[pivot], a[first] = a[first], a[pivot]
        d = a[pivot][col]
        a[pivot] = [x / d for x in a[pivot]]
        for row in range(pivot + 1, len(a)):
            if a[row][col]:
                v = a[row][col]
                a[row] = [x - v * y for x, y in zip(a[row], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def det3(a, b, c):
    return (a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


def volume6(cell, coordinates):
    u, v, w, z = [coordinates[i] for i in cell]
    return abs(oriented_volume6(cell, coordinates))


def oriented_volume6(cell, coordinates):
    u, v, w, z = [coordinates[i] for i in cell]
    return det3(tuple(v[i] - u[i] for i in range(3)),
                tuple(w[i] - u[i] for i in range(3)),
                tuple(z[i] - u[i] for i in range(3)))


def main():
    tetra_vertices = [(1, 1, 1), (1, -1, -1),
                      (-1, 1, -1), (-1, -1, 1)]
    mids = {tuple((tetra_vertices[i][k] + tetra_vertices[j][k]) // 2
                  for k in range(3)): (i, j)
            for i, j in combinations(range(4), 2)}
    shell = [(axis, sign) for axis in range(3) for sign in (-1, 1)]
    xyz = [tuple(sign if axis == k else 0 for k in range(3))
           for axis, sign in shell]
    assert set(xyz) == set(mids) and len(mids) == 6
    # Opposite shell vertices are exactly midpoint pairs of disjoint K4 edges.
    for i, p in enumerate(xyz):
        opposite = xyz.index(tuple(-x for x in p))
        assert set(mids[p]).isdisjoint(mids[xyz[opposite]])

    apex = 6
    sign_words = list(product((-1, 1), repeat=3))
    cells = [tuple(sorted((apex,) + tuple(shell.index((axis, s[axis]))
                                    for axis in range(3))))
             for s in sign_words]
    faces = sorted(set(f for c in cells for f in combinations(c, 3)))
    edges = sorted(set(e for c in cells for e in combinations(c, 2)))
    vertices = [(i,) for i in range(7)]
    assert (len(vertices), len(edges), len(faces), len(cells)) == (7, 18, 20, 8)
    assert len([e for e in edges if apex not in e]) == 12
    assert len([f for f in faces if apex not in f]) == 8
    assert len([f for f in faces if apex in f]) == 12
    assert 7 - 18 + 20 - 8 == 1

    b1 = make_boundary(vertices, edges)
    b2 = make_boundary(edges, faces)
    b3 = make_boundary(faces, cells)
    assert not any(any(row) for row in mm(b1, b2))
    assert not any(any(row) for row in mm(b2, b3))
    bface = [j for j, f in enumerate(faces) if apex not in f]
    assert Counter(sum(abs(b3[j][k]) for k in range(8)) for j in range(20)) == {1: 8, 2: 12}
    assert all(sum(abs(b3[j][k]) for k in range(8)) == 1 for j in bface)
    inner_coordinates = xyz + [(0, 0, 0)]
    inner_volume6 = [volume6(c, inner_coordinates) for c in cells]
    assert inner_volume6 == [1] * 8  # volume 1/6 per inner cell

    # The octahedron occupies only half the original tetrahedron's volume.
    # Four corner cells complete an honest subdivision of the original seed.
    full_coordinates = inner_coordinates + tetra_vertices
    corner_cells = [tuple(sorted((7 + i,) + tuple(xyz.index(q)
                          for q, pair in mids.items() if i in pair)))
                    for i in range(4)]
    full_cells = sorted(cells + corner_cells)
    full_faces = sorted(set(f for c in full_cells for f in combinations(c, 3)))
    full_edges = sorted(set(e for c in full_cells for e in combinations(c, 2)))
    full_vertices = [(i,) for i in range(11)]
    assert (len(full_vertices), len(full_edges), len(full_faces), len(full_cells)) == (11, 30, 32, 12)
    assert 11 - 30 + 32 - 12 == 1
    full_b1 = make_boundary(full_vertices, full_edges)
    full_b2 = make_boundary(full_edges, full_faces)
    full_b3 = make_boundary(full_faces, full_cells)
    assert not any(any(row) for row in mm(full_b1, full_b2))
    assert not any(any(row) for row in mm(full_b2, full_b3))
    assert [rank_q(b) for b in (full_b1, full_b2, full_b3)] == [10, 20, 12]
    face_degrees = [sum(abs(x) for x in row) for row in full_b3]
    assert Counter(face_degrees) == {1: 16, 2: 16}
    assert [volume6(c, full_coordinates) for c in cells] == [1] * 8
    assert [volume6(c, full_coordinates) for c in corner_cells] == [2] * 4
    assert sum(volume6(c, full_coordinates) for c in full_cells) == 16
    assert volume6(tuple(range(7, 11)), full_coordinates) == 16

    # Dual adjacency: share a radial triangular face iff one sign changes.
    adjacent = [[int(i != j and any(abs(b3[f][i] * b3[f][j]) == 1
                       for f in range(20))) for j in range(8)] for i in range(8)]
    hamming = [[sum(a != b for a, b in zip(sign_words[i], sign_words[j]))
                for j in range(8)] for i in range(8)]
    assert all(adjacent[i][j] == int(hamming[i][j] == 1)
               for i in range(8) for j in range(8))
    assert all(sum(row) == 3 for row in adjacent)
    signs = [1 if oriented_volume6(c, inner_coordinates) > 0 else -1
             for c in cells]
    oriented_b3 = [[x * signs[j] for j, x in enumerate(row)] for row in b3]
    assert gram(oriented_b3, right=True) == [
        [4 * int(i == j) - adjacent[i][j] for j in range(8)]
        for i in range(8)]

    # Four even and four odd words are the tetrahedral vertex and face orbits.
    parity = [s[0] * s[1] * s[2] for s in sign_words]
    assert Counter(parity) == {-1: 4, 1: 4}
    assert all(parity[i] == -parity[j] for i in range(8)
               for j in range(8) if adjacent[i][j])
    for s, c in zip(sign_words, cells):
        if s[0] * s[1] * s[2] == 1:
            assert s in tetra_vertices  # octahedral triangle at old vertex
        else:
            assert tuple(-x for x in s) in tetra_vertices  # old face

    # Every S4 permutation of old tetra vertices permutes six midpoints and
    # eight cells and preserves the parity of the sign words.
    for p in permutations(range(4)):
        mapped = []
        for midpoint in xyz:
            i, j = mids[midpoint]
            newpair = tuple(sorted((p[i], p[j])))
            mapped.append(xyz.index(next(q for q, pair in mids.items()
                                         if pair == newpair)))
        assert len(set(mapped)) == 6
        vertex_map = mapped + [apex]
        simplices = [vertices, edges, faces, cells]
        actions = []
        for simplex_list in simplices:
            lookup = {t: j for j, t in enumerate(simplex_list)}
            action = [[0] * len(simplex_list) for _ in simplex_list]
            for j, simplex in enumerate(simplex_list):
                transformed = [vertex_map[v] for v in simplex]
                inversions = sum(transformed[i] > transformed[k]
                                 for i in range(len(transformed))
                                 for k in range(i + 1, len(transformed)))
                action[lookup[tuple(sorted(transformed))]][j] = (-1) ** inversions
            actions.append(action)
        for k, b in enumerate((b1, b2, b3)):
            assert mm(b, actions[k + 1]) == mm(actions[k], b)
        for k, c in enumerate(cells):
            new_shell = {mapped[v] for v in c if v != apex}
            matched = next(i for i, d in enumerate(cells)
                           if {v for v in d if v != apex} == new_shell)
            assert parity[k] == parity[matched]

    # Three matrices carry the nonzero singular spectrum of the full skew
    # incidence generator; the middle matrix has 8 zero eigenvalues.
    p1 = charpoly(gram(b1))
    p2 = charpoly(gram(b2, right=True))
    p3 = charpoly(gram(b3, right=True))
    assert p1[-1] == 0 and p1[-2] != 0  # rank B1=6
    assert p2[-8:] == [0] * 8 and p2[-9] != 0  # rank B2=12
    assert p3[-1] != 0  # rank B3=8
    assert p1 == factor_product([([1, 0], 1), ([1, -5], 3), ([1, -7], 3)])
    assert p3 == factor_product([([1, -1], 1), ([1, -3], 3),
                                ([1, -5], 3), ([1, -7], 1)])
    assert p2 == factor_product([([1, 0], 8), ([1, -3], 3),
                                ([1, -5], 6), ([1, -7], 3)])
    # The shell's vertex and face spectra independently check dual adjacency.
    shell_edges = [e for e in edges if apex not in e]
    shell_faces = [f for f in faces if apex not in f]
    bs1 = make_boundary(vertices[:6], shell_edges)
    bs2 = make_boundary(shell_edges, shell_faces)
    assert not any(any(row) for row in mm(bs1, bs2))
    ps0 = charpoly(gram(bs1))
    ps2 = charpoly(gram(bs2, right=True))
    assert ps0 == factor_product([([1, 0], 1), ([1, -4], 3), ([1, -6], 2)])
    assert ps2 == factor_product([([1, 0], 1), ([1, -2], 3),
                                 ([1, -4], 3), ([1, -6], 1)])
    assert 6 + 12 + 8 == 26  # 26 oscillator pairs, 1 zero on filled ball
    squared_frequencies = {1: 1, 3: 6, 5: 12, 7: 7}
    assert sum(squared_frequencies.values()) == 26
    # A separate full-block assembly checks the sign convention and moments,
    # rather than inferring all checks only from the three Gram matrices.
    offsets = [0, 7, 25, 45]
    a = [[0] * 53 for _ in range(53)]
    for block, b in enumerate((b1, b2, b3)):
        for i, row in enumerate(b):
            for j, x in enumerate(row):
                a[offsets[block] + i][offsets[block + 1] + j] = x
                a[offsets[block + 1] + j][offsets[block] + i] = -x
    assert all(a[i][j] == -a[j][i] for i in range(53) for j in range(53))
    b_matrix = [[-x for x in row] for row in mm(a, a)]
    power = b_matrix
    for k in (1, 2, 3):
        moment = sum(power[i][i] for i in range(53))
        assert moment == 2 * sum(m * freq ** k
                                 for freq, m in squared_frequencies.items())
        power = mm(power, b_matrix)

    result = {
        "lane": "Development; exact finite-chain geometry, physical_promotion 0",
        "tetra_vertices": tetra_vertices,
        "midpoint_to_edge": {str(k): list(v) for k, v in mids.items()},
        "octa_shell_f": [6, 12, 8], "cone_f": [7, 18, 20, 8],
        "chain_dimension": 53, "boundary_ranks": [6, 12, 8],
        "betti": [1, 0, 0, 0], "hodge_zero_modes": 1,
        "hodge_oscillator_pairs": 26,
        "skew_generator_characteristic_polynomial":
            "lambda*(lambda^2+1)^1*(lambda^2+3)^6*(lambda^2+5)^12*(lambda^2+7)^7",
        "squared_frequency_multiplicities": squared_frequencies,
        "shell_charpoly_L0": ps0, "shell_charpoly_L2": ps2,
        "cone_charpoly_B1_B1T": p1,
        "cone_charpoly_B2T_B2": p2,
        "cone_charpoly_B3T_B3": p3,
        "word_order": sign_words, "dual_adjacency": adjacent,
        "parity_order": parity,
        "complete_seed_subdivision": {
            "f_vector": [11, 30, 32, 12], "boundary_ranks": [10, 20, 12],
            "inner_coned_cells": 8, "corner_filler_cells": 4,
            "boundary_triangles": 16, "internal_triangles": 16,
            "sixfold_volumes_inner": [1] * 8,
            "sixfold_volumes_corner": [2] * 4,
            "original_seed_sixfold_volume": 16,
            "chain_dimension": 85, "hodge_zero_modes": 1,
            "hodge_oscillator_pairs": 42},
        "metric": "Euclidean edge-midpoint octahedron: each coned tetra has three radius-1 radial edges and three sqrt(2) base edges; volume 1/6",
        "scope": "No selector, time/energy scale, material port, or damping derived."
    }
    (Path(__file__).parent / "RESULTS.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "shell_f": [6, 12, 8],
                      "cone_f": [7, 18, 20, 8], "ranks": [6, 12, 8],
                      "squared_frequency_multiplicities": squared_frequencies}))


if __name__ == "__main__":
    main()
