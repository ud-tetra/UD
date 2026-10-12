#!/usr/bin/env python3
"""Independent exact filled-K4 check of the frozen contrast and clock claims.

Uses only Python's standard library. No prior verifier code or result is imported.
"""
from fractions import Fraction as F
from itertools import combinations, product, permutations

S = [tuple(c) for k in range(4) for c in combinations(range(4), k + 1)]
index = {simplex: i for i, simplex in enumerate(S)}
N = len(S)
edges = [index[e] for e in combinations(range(4), 2)]
pairs = ((index[(0, 1)], index[(2, 3)]),
         (index[(0, 2)], index[(1, 3)]),
         (index[(0, 3)], index[(1, 2)]))


def matvec(M, v):
    return tuple(sum((a * b for a, b in zip(row, v)), F(0)) for row in M)


def mm(X, Y):
    return tuple(tuple(sum((X[i][k] * Y[k][j] for k in range(N)), F(0))
                       for j in range(N)) for i in range(N))


I = tuple(tuple(F(i == j) for j in range(N)) for i in range(N))
A = [[F(0) for _ in range(N)] for _ in range(N)]
for high in S:
    if len(high) == 1:
        continue
    hi = index[high]
    for k in range(len(high)):
        low = high[:k] + high[k + 1:]
        lo = index[low]
        sign = F((-1) ** k)
        A[lo][hi] -= sign
        A[hi][lo] += sign
A = tuple(tuple(row) for row in A)
P = tuple(tuple(F(1, 4) if i < 4 and j < 4 else F(0)
                for j in range(N)) for i in range(N))


def q(h, v):
    """Closed polynomial in A; separately check Cayley equation below."""
    av = matvec(A, v)
    pv = matvec(P, v)
    return tuple(pv[i] + (1 - h * h) / (1 + h * h) * (v[i] - pv[i])
                 + h / (1 + h * h) * av[i] for i in range(N))


def contrast(v):
    E = [sum(v[i] * v[i] for i in pair) for pair in pairs]
    return tuple(3 * x - sum(E) for x in E)


def receipt(v, h):
    before, after = contrast(v), contrast(q(h, v))
    return tuple(int(x * y < 0) for x, y in zip(before, after))


def main():
    assert all(A[i][j] == -A[j][i] for i in range(N) for j in range(N))
    A2 = mm(A, A)
    assert all(A2[i][j] == -4 * (I[i][j] - P[i][j])
               for i in range(N) for j in range(N))
    for h in (F(1), F(1, 2), F(-3, 7)):
        for basis in I:
            qb = q(h, basis)
            aqb = matvec(A, qb)
            ab = matvec(A, basis)
            assert all(qb[i] - h * aqb[i] / 2 == basis[i] + h * ab[i] / 2
                       for i in range(N))

    witness = tuple(map(F, (2, -2, 2, 1, 2, 2, 0, 0, -2, 2, 0, 2, 1, 2, 1)))
    u = witness
    v = tuple(x / 2 for x in matvec(A, u))
    endpoints = (contrast(u), contrast(v))
    # At s=pi/8, edge=(u+v)/sqrt(2), so its quadratic contrast is
    # [d(u+v)]/2, with no floating point trigonometry.
    mid = tuple(x / 2 for x in contrast(tuple(a + b for a, b in zip(u, v))))
    assert endpoints[0] == (F(8), F(8), F(-16))
    assert mid == (F(-5, 4), F(1), F(1, 4))
    assert endpoints[1] == (F(43, 2), F(-10), F(-23, 2))
    print("K4 identity A^2=-4(I-P0): PASS; Cayley equation: PASS")
    print("alias witness d(0), d(pi/8), d(pi/4):", endpoints[0], mid, endpoints[1])
    print("endpoint receipt:", receipt(witness, F(1)))

    # Because the scalar score is alpha+beta cos(4s)+gamma sin(4s),
    # the opposite signs in each half-interval force exactly one
    # sign-changing zero in each open half for A and C.
    for j in (0, 2):
        assert endpoints[0][j] * mid[j] < 0 and mid[j] * endpoints[1][j] < 0
    print("A,C: two distinct sign-changing interior zeros each: PASS")
    # t=tan(2s) maps (0,pi/4) bijectively onto positive reals. The
    # numerator of d(s) is a quadratic in t, so positive roots count
    # crossings without relying on a plot or sampled sign changes.
    coeff = tuple(((endpoints[0][j] + endpoints[1][j]) / 2,
                   (endpoints[0][j] - endpoints[1][j]) / 2,
                   mid[j] - (endpoints[0][j] + endpoints[1][j]) / 2)
                  for j in range(3))
    assert coeff == ((F(59, 4), F(-27, 4), F(-16)),
                     (F(-1), F(9), F(2)),
                     (F(-55, 4), F(-9, 4), F(14)))
    quadratics = tuple((a - b, 2 * g, a + b) for a, b, g in coeff)
    assert quadratics == ((F(43, 2), F(-32), F(8)),
                          (F(-10), F(4), F(8)),
                          (F(-23, 2), F(28), F(-16)))
    for qa, qb, qc in quadratics:
        assert qb * qb - 4 * qa * qc > 0
    assert [int(qa * qc > 0 and -qb / qa > 0) * 2
            + int(qa * qc < 0) for qa, qb, qc in quadratics] == [2, 1, 2]
    print("positive tan(2s) roots in (0,pi/4): (2,1,2): PASS")

    # A full-period theorem: Q1^2=2P0-I and Q1^4=I, while contrast
    # ignores P0 and is quadratic in the edge coordinates.
    for basis in I:
        q2 = q(F(1), q(F(1), basis))
        assert q2 == tuple(2 * matvec(P, basis)[i] - basis[i] for i in range(N))
    assert contrast(q(F(1), q(F(1), witness))) == contrast(witness)
    assert receipt(q(F(1), witness), F(1)) == receipt(witness, F(1))
    print("Q1^2=2P0-I; any nonzero strict receipt repeats forever: PASS")

    # A deliberately small exhaustive search, distinct from either prior
    # verifier's seeded fixtures, finds a tied endpoint with a non-tied next
    # endpoint, and a clock-dependent receipt.
    tied = clock = None
    for support in combinations(range(N), 3):
        for vals in product((-2, -1, 1, 2), repeat=3):
            z = [F(0)] * N
            for i, x in zip(support, vals):
                z[i] = F(x)
            z = tuple(z)
            d0, d1 = contrast(z), contrast(q(F(1), z))
            if tied is None and any(d0[i] == 0 and d1[i] != 0 for i in range(3)):
                tied = z
            if clock is None and receipt(z, F(1)) != receipt(z, F(1, 2)):
                clock = z
            if tied is not None and clock is not None:
                break
        if tied is not None and clock is not None:
            break
    assert tied is not None and clock is not None
    print("tie vector:", tied)
    print("tie before/after:", contrast(tied), contrast(q(F(1), tied)))
    perturbed = list(tied)
    perturbed[index[(0, 1)]] += F(1, 10)
    perturbed = tuple(perturbed)
    assert receipt(tied, F(1)) == (0, 0, 0)
    assert receipt(perturbed, F(1)) == (1, 1, 1)
    print("tie and 01-edge perturbation receipts:", receipt(tied, F(1)), receipt(perturbed, F(1)))
    print("clock vector:", clock)
    print("receipts h=1,1/2:", receipt(clock, F(1)), receipt(clock, F(1, 2)))

    # Conjugation by each signed simplicial relabeling. Check independent
    # coordinates and the induced opposite-edge pair action, including ties.
    for perm in permutations(range(4)):
        G = [None] * N
        for simplex, i in index.items():
            mapped = tuple(perm[k] for k in simplex)
            sign = (-1) ** sum(mapped[a] > mapped[b]
                               for a in range(len(mapped)) for b in range(a + 1, len(mapped)))
            G[i] = (index[tuple(sorted(mapped))], sign)
        def apply(z):
            out = [F(0)] * N
            for i, (j, sign) in enumerate(G):
                out[j] = sign * z[i]
            return tuple(out)
        for z in (witness, tied, clock):
            assert q(F(1), apply(z)) == apply(q(F(1), z))
            orig, transformed = contrast(z), contrast(apply(z))
            for p, pair in enumerate(pairs):
                mapped = frozenset(G[i][0] for i in pair)
                target = next(j for j, pp in enumerate(pairs) if frozenset(pp) == mapped)
                assert transformed[target] == orig[p]
                assert receipt(apply(z), F(1))[target] == receipt(z, F(1))[p]
    print("24 signed relabelings on three independent states: PASS")


if __name__ == "__main__":
    main()
