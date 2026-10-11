#!/usr/bin/env python3
"""Exact finite audit: memory-to-frame bridge and coordinate seat certificate."""
import itertools
import json
from fractions import Fraction as F

V = range(4)
EDGES = list(itertools.combinations(V, 2))
PAIR_EDGES = ((0, 5), (1, 4), (2, 3))

def zeros(n, m): return [[F(0) for _ in range(m)] for _ in range(n)]
def ident(n):
    a = zeros(n, n)
    for i in range(n): a[i][i] = F(1)
    return a
def transpose(a): return [list(x) for x in zip(*a)]
def matmul(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]
def block2(a, b, c, d):
    n = len(a)
    return [a[i] + b[i] for i in range(n)] + [c[i] + d[i] for i in range(n)]
def perm0(r):
    a = zeros(4, 4)
    for i in V: a[r[i]][i] = F(1)
    return a
def perm1(r):
    a = zeros(6, 6)
    for j, (u, v) in enumerate(EDGES):
        x, y = r[u], r[v]
        a[EDGES.index(tuple(sorted((x, y))))][j] = F(1 if x < y else -1)
    return a
def boundary1():
    a = zeros(4, 6)
    for j, (u, v) in enumerate(EDGES):
        a[u][j], a[v][j] = F(-1), F(1)
    return a

def rref(rows):
    a = [[F(x) for x in row] for row in rows if any(row)]
    p = 0
    for j in range(3):
        k = next((k for k in range(p, len(a)) if a[k][j]), None)
        if k is None: continue
        a[p], a[k] = a[k], a[p]
        v = a[p][j]
        a[p] = [x / v for x in a[p]]
        for k in range(len(a)):
            if k != p:
                v = a[k][j]
                a[k] = [x - v*y for x,y in zip(a[k], a[p])]
        p += 1
        if p == len(a): break
    return tuple(tuple(row) for row in a[:p])

def main():
    b = boundary1()
    j4 = [[F(1) for _ in V] for _ in V]
    reps = {r: perm1(r) for r in itertools.permutations(V)}
    assert len({tuple(map(tuple, q)) for q in reps.values()}) == 24
    mq = block2(zeros(6,6), [[F(1,2)*x for x in row] for row in ident(6)],
                [[F(-2)*x for x in row] for row in ident(6)], zeros(6,6))
    minv = [[-x for x in row] for row in mq]
    assert matmul(mq, minv) == ident(12)

    def decode(obs):
        residual = matmul(obs, minv)
        q = [row[:6] for row in residual[:6]]
        assert [row[6:] for row in residual[:6]] == zeros(6,6)
        assert [row[:6] for row in residual[6:]] == zeros(6,6)
        assert [row[6:] for row in residual[6:]] == q
        x = matmul(matmul(b, q), transpose(b))
        p0 = [[(x[i][k] + j4[i][k])/4 for k in V] for i in V]
        matches = [r for r in reps if perm0(r) == p0 and matmul(b, q) == matmul(p0, b)]
        assert len(matches) == 1 and reps[matches[0]] == q
        return matches[0]

    for r, q in reps.items():
        obs = matmul(block2(q, zeros(6,6), zeros(6,6), q), mq)
        assert decode(obs) == r
    # Independent input/output re-expression, including the singular q-only step.
    for h0, h1 in itertools.product(reps, repeat=2):
        q0, q1 = reps[h0], reps[h1]
        obs = matmul(block2(q1,zeros(6,6),zeros(6,6),q1),
                     matmul(mq,block2(transpose(q0),zeros(6,6),zeros(6,6),transpose(q0))))
        recovered = decode(obs)
        p = matmul(q1,transpose(q0))
        assert reps[recovered] == p
    # A one-block decoder is unsound unless the p block and mixed blocks pass.
    swap = next(r for r in reps if r != tuple(V))
    bad = matmul(block2(ident(6),zeros(6,6),zeros(6,6),reps[swap]), mq)
    residual = matmul(bad, minv)
    assert [row[:6] for row in residual[:6]] == ident(6)
    assert [row[6:] for row in residual[6:]] != ident(6)

    vectors = [v for v in itertools.product((-1,0,1),repeat=3) if any(v)]
    spaces = {rref(())}
    for k in (1,2,3):
        spaces.update(rref(rows) for rows in itertools.combinations(vectors,k))
    seat_count = 0
    covariance = 0
    for w in spaces:
        support = tuple(i for i in range(3) if any(row[i] for row in w))
        coordinate = len(w) == len(support)
        if coordinate:
            assert w == rref(tuple(tuple(int(j==i) for j in range(3)) for i in support))
            seat_count += 1
        for g in itertools.permutations(range(3)):
            wp = rref(tuple(tuple(row[g.index(i)] for i in range(3)) for row in w))
            support_p = tuple(i for i in range(3) if any(row[i] for row in wp))
            assert (len(wp) == len(support_p)) == coordinate
            assert set(support_p) == {g[i] for i in support}
            covariance += 1
    assert seat_count == 8
    assert len(rref(((1,1,0),))) == 1
    assert len([i for i in range(3) if (1,1,0)[i]]) == 2
    print(json.dumps({
      "status":"EXACT conditional bridge and seat certificate; no sourced exposure event",
      "frame_conditional_cases":24,"two_sided_frame_relabels":576,
      "frame_block_mismatch_counterexample":1,
      "finite_rational_subspaces":len(spaces),"coordinate_subspaces":seat_count,
      "seat_relabel_checks":covariance,
      "independent_endpoint_records":0,"physical_promotion":0
    },indent=2))

if __name__ == '__main__': main()
