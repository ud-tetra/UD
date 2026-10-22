#!/usr/bin/env python3
"""UD THM-534 v0.7: exact burden redistribution / sourced face-circulation.

Sources: coefficient provenance v0.39, Q153/Q155/Q156/Q162.
Fixed carrier: filled oriented Delta^3, unit simplex metric.
Uses SymPy and standard Python; no physical time/energy or Born map.
"""
from itertools import combinations, product
import sympy as sp

v = tuple(range(4))
edges = list(combinations(v, 2))
faces = list(combinations(v, 3))
B1, B2, B3 = sp.zeros(4, 6), sp.zeros(6, 4), sp.zeros(4, 1)
for c, (a, b) in enumerate(edges):
    B1[a, c], B1[b, c] = -1, 1
for c, face in enumerate(faces):
    for k in range(3):
        B2[edges.index(face[:k] + face[k + 1:]), c] = (-1) ** k
for k in range(4):
    B3[faces.index(v[:k] + v[k + 1:]), 0] = (-1) ** k

assert B1 * B2 == sp.zeros(4, 4)
assert B2 * B3 == sp.zeros(6, 1)
assert B1.T * B1 + B2 * B2.T == 4 * sp.eye(6)
ones = sp.ones(4, 1)
unit_burden = [sp.eye(4)[:, i] for i in range(4)]

flat = []
ranks = {}
for bits in product((0, 1), repeat=6):
    H = sp.diag(*bits)
    Lap = B1 * H * B1.T
    P = sp.eye(4) - Lap / 4
    C = B2.T * H * B1.T
    r = C.rank()
    ranks[r] = ranks.get(r, 0) + 1
    if C == sp.zeros(4, 4):
        flat.append(bits)
    assert P.T == P and P * ones == ones and ones.T * P == ones.T
    assert all(P[i, j] >= 0 for i in range(4) for j in range(4))
    for rho in unit_burden:
        j = -H * B1.T * rho / 4
        delta = B1 * j
        prime = rho + delta
        circ = B2.T * j
        assert prime == P * rho
        assert all(prime[i] >= 0 for i in range(4))
        assert (ones.T * prime)[0] == 1
        assert B3.T * circ == sp.zeros(1, 1)
        assert 4*(j.T*j)[0] == (delta.T*delta)[0] + (circ.T*circ)[0]
    assert all(0 <= lam <= 1 for lam in P.eigenvals())

assert len(flat) == 2
assert flat == [(0,)*6, (1,)*6]
assert ranks == {0:2, 1:12, 2:38, 3:12}

H=sp.diag(0,1,1,1,1,1)
rho=sp.Matrix([1,0,0,0])
j= -H * B1.T*rho/4
prime=rho+B1*j
circ=B2.T*j
assert list(j) == [0, sp.Rational(1,4),sp.Rational(1,4),0,0,0]
assert list(prime) == [sp.Rational(1,2),0,sp.Rational(1,4),sp.Rational(1,4)]
assert list(circ) == [-sp.Rational(1,4),-sp.Rational(1,4),0,0]
assert 4*(j.T*j)[0] == sp.Rational(1,2)
assert ((B1*j).T*(B1*j))[0] == sp.Rational(3,8)
assert (circ.T*circ)[0] == sp.Rational(1,8)
assert B3.T*circ==sp.zeros(1,1)

for i in range(6):
    G=sp.eye(6);G[i,i]=-1
    changed_B1=B1*G;changed_B2=G*B2
    jj=-H*changed_B1.T*rho/4
    assert changed_B1*jj==B1*j
    assert changed_B2.T*jj==circ

for Hnull in (sp.zeros(6),sp.eye(6)):
    assert B2.T*Hnull*B1.T == sp.zeros(4,4)
    for rho in unit_burden:
        assert B2.T*(-Hnull*B1.T*rho/4) == sp.zeros(4,1)
for bits in product((0,1), repeat=6):
    H=sp.diag(*bits)
    assert -H*B1.T*ones/4==sp.zeros(6,1)

print('PASS exact signed chain identities and Hodge current norm split')
print('PASS all 64 gate masks x 4 vertex unit-burden inputs: nonnegative and total-burden-preserving')
print('PASS curvature closed on tetrahedron, 6 edge-orientation sign flips')
print('flat-for-all-burden masks:', flat)
print('rank B2.T H B1.T distribution:', dict(sorted(ranks.items())))
print('positive witness j:',list(j),'burden prime:',list(prime),'face circulation:',list(circ))
print('source-normalization and physical holonomy map remain OPEN; physical promotion 0')
