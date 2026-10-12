#!/usr/bin/env python3
"""Exact rational checks of a proposed K4 cochain sign-crossing event rule.

This is a candidate constitutive rule, not a sourced UD event mechanism.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
import json
import random
from pathlib import Path

VERTICES = tuple(range(4))
SIMPLICES = [list(combinations(VERTICES, k)) for k in range(1, 5)]
SIMP = sum(SIMPLICES, [])
INDEX = {s: i for i, s in enumerate(SIMP)}
N = len(SIMP)
EDGES = SIMPLICES[1]
PAIRS = ((0, 5), (1, 4), (2, 3))  # 01/23, 02/13, 03/12
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}


def ident(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def matmul(a, b):
    return [[sum((x * b[k][j] for k, x in enumerate(row)), F(0))
             for j in range(len(b[0]))] for row in a]


def matvec(a, v):
    return [sum((x * y for x, y in zip(row, v)), F(0)) for row in a]


def inverse(a):
    n = len(a)
    m = [row[:] + eye for row, eye in zip(a, ident(n))]
    for j in range(n):
        pivot = next(i for i in range(j, n) if m[i][j])
        m[j], m[pivot] = m[pivot], m[j]
        q = m[j][j]
        m[j] = [x / q for x in m[j]]
        for i in range(n):
            if i != j and m[i][j]:
                q = m[i][j]
                m[i] = [x - q * y for x, y in zip(m[i], m[j])]
    return [row[n:] for row in m]


def transpose(a):
    return list(map(list, zip(*a)))


def generator():
    # Boundary B maps an oriented k-simplex to its signed (k-1)-faces.
    # A_{k-1,k}=-B_k, A_{k,k-1}=B_k^T.
    a = [[F(0) for _ in range(N)] for _ in range(N)]
    for higher in SIMP:
        if len(higher) == 1:
            continue
        j = INDEX[higher]
        for t in range(len(higher)):
            lower = higher[:t] + higher[t+1:]
            i = INDEX[lower]
            a[i][j] = -F((-1)**t)
            a[j][i] = F((-1)**t)
    return a


def cayley(a, h):
    left = [[F(i == j) - h * a[i][j] / 2 for j in range(N)] for i in range(N)]
    right = [[F(i == j) + h * a[i][j] / 2 for j in range(N)] for i in range(N)]
    return matmul(inverse(left), right)


def sign_of_reordering(seq):
    return -1 if sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i+1, len(seq))) % 2 else 1


def action(g):
    r = [[F(0) for _ in range(N)] for _ in range(N)]
    for j, simplex in enumerate(SIMP):
        mapped = tuple(g[v] for v in simplex)
        r[INDEX[tuple(sorted(mapped))]][j] = F(sign_of_reordering(mapped))
    return r


def pair_action(g):
    out = []
    for pair in PAIRS:
        mapped = {EDGE_INDEX[tuple(sorted((g[v] for v in EDGES[e])))] for e in pair}
        out.append(next(i for i, q in enumerate(PAIRS) if set(q) == mapped))
    return out


def contrasts(c):
    energies = [sum((c[INDEX[EDGES[e]]]**2 for e in pair), F(0)) for pair in PAIRS]
    total = sum(energies, F(0))
    return tuple(3*x - total for x in energies)


def receipt(c, q):
    before, after = contrasts(c), contrasts(matvec(q, c))
    return tuple(int(x*y < 0) for x, y in zip(before, after)), before, after


def sample_states():
    yield [F(0)]*N
    for j in range(N):
        v = [F(0)]*N
        v[j] = F(1)
        yield v
    rng = random.Random(1729)
    for _ in range(600):
        yield [F(rng.randrange(-2, 3)) for _ in range(N)]


def main():
    a = generator()
    assert [[-x for x in row] for row in a] == transpose(a)
    q1, qhalf = cayley(a, F(1)), cayley(a, F(1, 2))
    eye = ident(N)
    assert matmul(transpose(q1), q1) == eye
    assert matmul(transpose(qhalf), qhalf) == eye
    actions = [(g, action(g), pair_action(g)) for g in permutations(VERTICES)]
    assert len({tuple(perm) for _, _, perm in actions}) == 6
    for _, r, _ in actions:
        assert matmul(a, r) == matmul(r, a)
        assert matmul(q1, r) == matmul(r, q1)

    cases = list(sample_states())
    classes = set()
    nonzero = null = degenerate = 0
    step_sensitive = None
    one_nonzero = None
    two_nonzero = None
    for c in cases:
        xi, d0, d1 = receipt(c, q1)
        assert sum(d0) == sum(d1) == 0
        assert receipt([2*x for x in c], q1)[0] == xi
        assert receipt([-x for x in c], q1)[0] == xi
        classes.add(sum(xi))
        nonzero += bool(sum(xi))
        null += not any(xi)
        degenerate += any(not x for x in d0+d1)
        if sum(xi) == 1 and one_nonzero is None:
            one_nonzero = c
        if sum(xi) >= 2 and two_nonzero is None:
            two_nonzero = c
        if step_sensitive is None and xi != receipt(c, qhalf)[0]:
            step_sensitive = c
        for _, r, pairperm in actions:
            rc = matvec(r, c)
            xig = receipt(rc, q1)[0]
            expected = [0]*3
            for p, pnew in enumerate(pairperm):
                expected[pnew] = xi[p]
            assert xig == tuple(expected)
    assert one_nonzero is not None and two_nonzero is not None
    assert step_sensitive is not None
    assert receipt([F(0)]*N, q1)[0] == (0, 0, 0)
    assert matvec(q1, [F(0)]*N) == [F(0)]*N
    trajectory = one_nonzero
    repeated_flip_counts = []
    initial_norm = sum((x*x for x in trajectory), F(0))
    for _ in range(32):
        repeated_flip_counts.append(sum(receipt(trajectory, q1)[0]))
        trajectory = matvec(q1, trajectory)
        assert sum((x*x for x in trajectory), F(0)) == initial_norm
    # Theta uses the matching pair permutation; T is a separate edge object.
    for c in [one_nonzero, two_nonzero]:
        xi = receipt(c, q1)[0]
        for theta in product(range(2), repeat=3):
            post = tuple(x^y for x, y in zip(theta, xi))
            for g, _, perm in actions:
                def act(v):
                    out = [0]*3
                    for i, j in enumerate(perm):
                        out[j] = v[i]
                    return tuple(out)
                assert act(post) == tuple(x^y for x, y in zip(act(theta), act(xi)))
                edge_perm = [EDGE_INDEX[tuple(sorted((g[v] for v in edge)))] for edge in EDGES]
                for transport in product(range(2), repeat=6):
                    by_edge = [0]*6
                    for p, pair in enumerate(PAIRS):
                        for e in pair:
                            by_edge[e] = (1-post[p])*transport[e]
                    gt = [0]*6
                    gh = [0]*6
                    for e, j in enumerate(edge_perm):
                        gt[j] = transport[e]
                        gh[j] = by_edge[e]
                    pushed = [0]*6
                    for p, pair in enumerate(PAIRS):
                        for e in pair:
                            pushed[e] = (1-act(post)[p])*gt[e]
                    assert gh == pushed
    output = {
        'status': 'PASS', 'source_status': 'CANDIDATE constitutive sign-crossing rule',
        'states_checked': len(cases), 'pair_covariance_checks': len(cases)*24,
        'native_generator_and_cayley_covariance_checks': 24,
        'conditional_hard_mask_covariance_checks': 2*8*24*64,
        'observed_flip_counts': sorted(classes), 'null_windows_in_sample': null,
        'nonzero_windows_in_sample': nonzero, 'degenerate_windows_in_sample': degenerate,
        'step_size_sensitive_witness': [int(x) for x in step_sensitive],
        'step_size_sensitive_xi_h1': receipt(step_sensitive, q1)[0],
        'step_size_sensitive_xi_hhalf': receipt(step_sensitive, qhalf)[0],
        'one_flip_witness': [int(x) for x in one_nonzero],
        'simultaneous_witness': [int(x) for x in two_nonzero],
        'repeated_witness_32_window_flip_count': sum(repeated_flip_counts),
        'repeated_witness_32_window_null_count': repeated_flip_counts.count(0),
        'held_out_target': 'NOT_RUN', 'physical_promotion': 0,
    }
    Path(__file__).with_name('results.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
