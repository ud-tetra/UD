"""Exact vertex-sector leakage under positive diagonal simplicial metrics.

The universal no-go is the two-half-edge support proof in the companion note.
This script reconstructs the full 12-cell refinement and checks the symbolic
formula on rational weights, including symmetry and anisotropic controls.
"""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json


def frac(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def main():
    old_xyz = [(1, 1, 1), (1, -1, -1),
               (-1, 1, -1), (-1, -1, 1)]
    mid_xyz = {pair: tuple((old_xyz[i][k] + old_xyz[j][k]) // 2
                           for k in range(3))
               for i, j in combinations(range(4), 2) for pair in [(i, j)]}
    shell = [tuple(s if axis == k else 0 for k in range(3))
             for axis in range(3) for s in (-1, 1)]
    mid = {p: shell.index(q) for p, q in mid_xyz.items()}
    inner = [tuple(sorted((6,) + tuple(shell.index(tuple(s[a] if a == k
                       else 0 for k in range(3))) for a in range(3))))
             for s in product((-1, 1), repeat=3)]
    corners = [tuple(sorted((7 + i,) + tuple(mid[p] for p in mid if i in p)))
               for i in range(4)]
    cells = inner + corners
    edges = sorted({e for c in cells for e in combinations(c, 2)})
    lookup = {e: j for j, e in enumerate(edges)}
    assert (len(edges), len(cells)) == (30, 12)
    b1 = [[0] * 30 for _ in range(11)]
    for e, (v, w) in enumerate(edges):
        b1[v][e], b1[w][e] = -1, 1
    # Each old edge contributes two disjoint fine edge supports to S1.
    subdiv = [[0] * 6 for _ in range(30)]
    old_edges = list(combinations(range(4), 2))
    for j, (i, k) in enumerate(old_edges):
        m = mid[(i, k)]
        for a, b in ((7 + i, m), (m, 7 + k)):
            subdiv[lookup[tuple(sorted((a, b)))]][j] = 1 if a < b else -1
    assert all(sum(abs(subdiv[e][j]) for e in range(30)) == 2 for j in range(6))
    assert all(sum(abs(subdiv[e][j]) for j in range(6)) <= 1 for e in range(30))

    def audit(vertex_weights, half_weights):
        # All other positive edge weights are irrelevant for an old vertex
        # because its coboundary vanishes there. Give them a fixed value.
        edge_weights = [F(7, 5)] * 30
        for (i, k), (hi, hk) in half_weights.items():
            assert hi > 0 and hk > 0
            edge_weights[lookup[tuple(sorted((7 + i, mid[(i, k)])))]] = hi
            edge_weights[lookup[tuple(sorted((7 + k, mid[(i, k)])))]] = hk
        rows = []
        for i, a in enumerate(vertex_weights):
            assert a > 0
            v = 7 + i
            # -H1^{-1}B1^T H0 e_v; sign does not affect squared norms.
            y = [F(b1[v][e]) * a / edge_weights[e] for e in range(30)]
            coeff = []
            for j in range(6):
                denom = sum(edge_weights[e] * subdiv[e][j] ** 2
                            for e in range(30))
                numer = sum(edge_weights[e] * subdiv[e][j] * y[e]
                            for e in range(30))
                coeff.append(numer / denom)
            residue = [y[e] - sum(subdiv[e][j] * coeff[j]
                                  for j in range(6)) for e in range(30)]
            squared_leak = sum(edge_weights[e] * residue[e] ** 2
                               for e in range(30)) / a
            squared_action = sum(edge_weights[e] * y[e] ** 2
                                 for e in range(30)) / a
            predicted_leak = F(0)
            predicted_action = F(0)
            for j in range(4):
                if j == i:
                    continue
                pair = tuple(sorted((i, j)))
                wn = half_weights[pair][0 if i == pair[0] else 1]
                wf = half_weights[pair][1 if i == pair[0] else 0]
                predicted_leak += a * wf / (wn * (wn + wf))
                predicted_action += a / wn
            assert squared_leak == predicted_leak > 0
            assert squared_action == predicted_action
            ratio = squared_leak / squared_action
            rows.append({'old_vertex': i, 'leakage_squared': frac(squared_leak),
                         'action_squared': frac(squared_action),
                         'leakage_fraction': frac(ratio)})
        contrast = max(max(hi / hk, hk / hi)
                       for hi, hk in half_weights.values())
        assert all(F(row['leakage_fraction']) >= 1 / (1 + contrast)
                   for row in rows)
        return {'contrast_kappa': frac(contrast), 'lower_bound': frac(1 / (1 + contrast)),
                'vertex_rows': rows}

    unit = audit([F(1)] * 4, {p: (F(1), F(1)) for p in old_edges})
    symmetric = audit([F(2)] * 4, {p: (F(3), F(3)) for p in old_edges})
    anisotropic = audit([F(1), F(2), F(3), F(4)],
                        {p: (F(p[0] + 2), F(2 * p[1] + 1)) for p in old_edges})
    assert [r['leakage_fraction'] for r in unit['vertex_rows']] == ['1/2'] * 4
    assert [r['leakage_fraction'] for r in symmetric['vertex_rows']] == ['1/2'] * 4
    assert [r['leakage_squared'] for r in unit['vertex_rows']] == ['3/2'] * 4

    result = {
        'lane': 'Exact conditional positive-diagonal Hodge-metric no-go; physical promotion 0',
        'carrier': 'Full 12-cell subdivision of original regular tetrahedron; standard subdivision S',
        'metric_class': 'H0 and H1 strictly positive diagonal; arbitrary positive H2,H3; B1 down and -H1^-1 B1^T H0 up',
        'universal_vertex_formula':
            'ell_i^2=sum_{j != i} a_i*b_far/[b_near*(b_near+b_far)]',
        'universal_action_formula':
            '||A v_i||_H^2=sum_{j != i} a_i/b_near, v_i=e_i/sqrt(a_i)',
        'universal_exact_invariance': False,
        'S4_symmetric_vertex_leakage_fraction': '1/2',
        'bounded_contrast_lower_fraction': '1/(1+kappa)',
        'unit_control': unit,
        'S4_symmetric_nonunit_control': symmetric,
        'anisotropic_control': anisotropic,
        'scope': 'Only diagonal positive simplex metrics and fixed geometric S. Off-diagonal metrics, new embeddings or zero coupling are not excluded. No damping or graphite coefficient.'
    }
    (Path(__file__).parent / 'RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'unit_leakage_fraction': '1/2',
                      'S4_nonunit_leakage_fraction': '1/2',
                      'anisotropic_fractions': [r['leakage_fraction']
                                                for r in anisotropic['vertex_rows']]}))


if __name__ == '__main__':
    main()
