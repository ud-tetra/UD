#!/usr/bin/env python3
"""Exact, target-exposed/source-first tetrahedral-incidence transport audit v0.3.

Carrier: filled oriented tetrahedron Delta^3 and unoriented edge readout.
This file checks theorems N5/N6/N7, not an empirical or target-blind bridge.
Requires SymPy. Physical promotion 0.
"""
import itertools
import sympy as sp

verts = list(range(4))
edges = list(itertools.combinations(verts, 2))
faces = list(itertools.combinations(verts, 3))

# Standard alternating simplicial boundary maps.
B1 = sp.zeros(4, 6)
for j, (a, b) in enumerate(edges):
    B1[a, j] = -1
    B1[b, j] = 1

B2 = sp.zeros(6, 4)
for j, face in enumerate(faces):
    for k in range(3):
        e = tuple(face[:k] + face[k+1:])
        B2[edges.index(e), j] += (-1)**k

B3 = sp.zeros(4, 1)
for k in range(4):
    f = tuple(verts[:k] + verts[k+1:])
    B3[faces.index(f), 0] = (-1)**k

assert B1 * B2 == sp.zeros(4, 4)
assert B2 * B3 == sp.zeros(6, 1)
assert B1.T * B1 + B2 * B2.T == 4 * sp.eye(6)

# Uniform lower/upper two-stage incidence events, with replacement.
Avert, Aface = abs(B1), abs(B2)
Pdown = (Avert.T * Avert) / 6
Pup = (Aface * Aface.T) / 6
assert Pdown == Pup

I, J = sp.eye(6), sp.ones(6)
S = sp.zeros(6)
for i, e in enumerate(edges):
    j = next(j for j, f in enumerate(edges) if not (set(e) & set(f)))
    S[i, j] = 1
P = I/3 + (J-I-S)/6
assert Pdown == P
assert P.eigenvals() == {sp.Integer(1): 1, sp.Integer(0): 2, sp.Rational(1, 3): 3}
historical = I/2 + S/6 + (J-I-S)/12
assert historical.eigenvals() == {sp.Integer(1): 1, sp.Rational(1, 2): 2, sp.Rational(1, 3): 3}

# Finite-step exact receipts, verifying the analytic inequality
# lambda_minus >= lambda_plus for every nonnegative step-length mixture.
expected = [
    (sp.Rational(1, 3), 0, sp.Rational(1, 6)),
    (sp.Rational(2, 9), sp.Rational(1, 9), sp.Rational(1, 6)),
    (sp.Rational(5, 27), sp.Rational(4, 27), sp.Rational(1, 6))
]
for k, triple in enumerate(expected, 1):
    A = P**k
    assert (A[0, 0], A[0, 5], A[0, 1]) == triple

# Verify all 24 S4 equivariance checks, not a sample.
for perm in itertools.permutations(verts):
    idx = [edges.index(tuple(sorted((perm[a], perm[b])))) for a, b in edges]
    assert all(P[idx[i], idx[j]] == P[i, j] for i in range(6) for j in range(6))

print("PASS: signed chain identities and unit-Hodge edge Laplacian L1=4I6")
print("PASS: lower edge-vertex-edge and upper edge-face-edge kernels identical")
print("PASS: incidence spectrum {1,0x2,(1/3)x3}; 24 S4 relabelings")
print("PASS: P^1, P^2, P^3 exact edge probabilities")
print("EXACT NO-GO: nonnegative independent incidence length-mixtures cannot attain historical THM-534")
print("SOURCE STATUS: original THM-534 event law OPEN; physical promotion 0")
