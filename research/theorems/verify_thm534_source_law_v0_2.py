#!/usr/bin/env python3
"""THM-534 source-law gate v0.2: exact symmetry and forward control verifier."""
from fractions import Fraction as F
from itertools import combinations, permutations
from math import exp, log

E = list(combinations(range(4), 2))
opp = {e: next(f for f in E if not(set(e) & set(f))) for e in E}

def kernel(a, b, c):
    return [[a if e == f else b if f == opp[e] else c for f in E] for e in E]

def matvec(A, v):
    return [sum(A[i][j] * v[j] for j in range(6)) for i in range(6)]

def check_spectrum(A, a, b, c):
    pairs = []
    for e in E:
        if not any(e in p for p in pairs):
            pairs.append((e, opp[e]))
    eigenvectors = [([1]*6, a+b+4*c)]
    for p in pairs[1:]:
        eigenvectors.append(([1 if e in pairs[0] else -1 if e in p else 0 for e in E], a+b-2*c))
    for p in pairs:
        eigenvectors.append(([1 if e == p[0] else -1 if e == p[1] else 0 for e in E], a-b))
    assert len(eigenvectors) == 6
    for v, lam in eigenvectors:
        assert matvec(A, v) == [lam*x for x in v]

target = kernel(F(1,2), F(1,6), F(1,12))
alternate = kernel(F(3,5), F(1,10), F(3,40))
for A, (a,b,c) in ((target,(F(1,2),F(1,6),F(1,12))),
                    (alternate,(F(3,5),F(1,10),F(3,40)))):
    check_spectrum(A,a,b,c)
    assert all(sum(row) == 1 for row in A)
    assert all(A[i][j] == A[j][i] for i in range(6) for j in range(6))
    for p in permutations(range(4)):
        index = [E.index(tuple(sorted((p[e[0]],p[e[1]])))) for e in E]
        assert all(A[index[i]][index[j]] == A[i][j] for i in range(6) for j in range(6))
assert target != alternate and all(x>0 for row in alternate for x in row)

# Independently declared forward event law: choose a uniform vertex transposition.
C = [[F(0) for _ in E] for _ in E]
for p,q in E:
    perm = list(range(4))
    perm[p],perm[q] = perm[q],perm[p]
    for i,e in enumerate(E):
        j = E.index(tuple(sorted((perm[e[0]],perm[e[1]]))))
        C[i][j] += F(1,6)
assert C == kernel(F(1,3),F(0),F(1,6))
check_spectrum(C,F(1,3),F(0),F(1,6))

# Inverse spectral calibration: this is NOT a forward micro-event derivation.
u = log(3)/2 - log(2)/3
v = log(2)/6
assert u > 0 and v > 0
assert abs(exp(-6*v) - .5) < 1e-14
assert abs(exp(-2*u-4*v) - 1/3) < 1e-14
print("PASS: 24 S4 relabelings, exact eigenchecks, strict-positive alternative, forward transposition control")
print("target: (1/2,1/6,1/12), eigenvalues (1,1/2×2,1/3×3)")
print("alternative: (3/5,1/10,3/40), eigenvalues (1,11/20×2,1/2×3)")
print("forward transpositions: (1/3,0,1/6), eigenvalues (1,0×2,1/3×3)")
print("Original THM-534 event measure: SOURCE-BLOCKED; physical promotion: 0")
