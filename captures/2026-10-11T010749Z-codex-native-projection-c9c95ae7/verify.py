#!/usr/bin/env python3
"""Exact filled-tetrahedron native-flow compression audit."""
import itertools
import json
from fractions import Fraction as F

verts = tuple(range(4))
simplices = [tuple(itertools.combinations(verts, k)) for k in (1, 2, 3, 4)]
offset = [0, 4, 10, 14]
N = 15


def zeros(n=N, m=N):
    return [[F(0) for _ in range(m)] for _ in range(n)]


def eye():
    out = zeros()
    for i in range(N):
        out[i][i] = F(1)
    return out


def tr(A):
    return list(map(list, zip(*A)))


def mul(A, B):
    assert len(A[0]) == len(B)
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), F(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def add(A, B, a=F(1), b=F(1)):
    return [[a * x + b * y for x, y in zip(rx, ry)]
            for rx, ry in zip(A, B)]


def boundary(lower, upper):
    out = zeros(len(lower), len(upper))
    lowindex = {s: i for i, s in enumerate(lower)}
    for j, high in enumerate(upper):
        for p in range(len(high)):
            face = high[:p] + high[p+1:]
            out[lowindex[face]][j] = F((-1) ** p)
    return out


def main():
    B1, B2, B3 = (boundary(simplices[k-1], simplices[k])
                  for k in (1, 2, 3))
    assert mul(B1, B2) == zeros(4, 4)
    assert mul(B2, B3) == zeros(6, 1)
    L1 = add(mul(tr(B1), B1), mul(B2, tr(B2)))
    assert L1 == [[F(4 if i == j else 0) for j in range(6)]
                  for i in range(6)]

    # Native skew Hodge-Dirac: c0'=-B1 c1;
    # c1'=B1^T c0-B2 c2; c2'=B2^T c1-B3 c3; c3'=B3^T c2.
    A = zeros()
    for k, B in enumerate((B1, B2, B3)):
        low, high = offset[k], offset[k+1]
        for i in range(len(B)):
            for j in range(len(B[0])):
                A[low+i][high+j] = -B[i][j]
                A[high+j][low+i] = B[i][j]
    assert tr(A) == add(zeros(), A, b=-F(1))
    A2 = mul(A, A)
    A3 = mul(A2, A)
    assert A3 == add(zeros(), A, b=-F(4))
    I = eye()
    # Exact native intervals s=pi/4 and s=pi/2, using the minimal polynomial.
    Oq = add(add(I, A, b=F(1, 2)), A2, b=F(1, 4))
    Oh = add(I, A2, b=F(1, 2))
    assert mul(tr(Oq), Oq) == I
    assert mul(Oq, Oq) == Oh
    assert mul(tr(Oh), Oh) == I

    # P_e denotes compression to a fixed one-dimensional edge-chain basis.
    for edge in range(6):
        e = offset[1] + edge
        assert A[e][e] == 0
        assert Oq[e][e] == 0
        assert Oh[e][e] == -1
        assert Oq[e][e] * Oq[e][e] == 0 != Oh[e][e]
        assert 1 - Oq[e][e]**2 == 1
        assert 1 - Oh[e][e]**2 == 0
        column = [Oq[i][e] for i in range(N)]
        assert sum((x*x for x in column), F(0)) == 1
        assert column[e] == 0
        # The earlier fixed-structure null explicitly declares the distinct
        # internal edge transport to be I throughout this same native flow.
        declared_transport_in_static_null = F(1)
        assert declared_transport_in_static_null != Oq[e][e]

    # Independently generated boundaries match the literal incidence arrays
    # frozen in the previous K4 static-null capture (10 Oct 2026).
    frozen_B1 = [
        [-1, -1, -1, 0, 0, 0],
        [1, 0, 0, -1, -1, 0],
        [0, 1, 0, 1, 0, -1],
        [0, 0, 1, 0, 1, 1],
    ]
    frozen_B2 = [
        [1, 1, 0, 0], [-1, 0, 1, 0], [0, -1, -1, 0],
        [1, 0, 0, 1], [0, 1, 0, -1], [0, 0, 1, 1],
    ]
    assert B1 == frozen_B1 and B2 == frozen_B2
    print(json.dumps({
        "status": "EXACT candidate-compression counterexample, bridge NO-GO as universal identification",
        "carrier": "filled oriented tetrahedron, Euclidean C0+C1+C2+C3, 15 dimensions",
        "six_edge_compressed_U_at_native_s": {"0": "1", "pi/4": "0", "pi/2": "-1"},
        "integrity_T_at_native_s": {"0": 1, "pi/4": 0, "pi/2": 1},
        "composition_at_pi_over_4": {"compressed_two_steps": "0", "compressed_full_step": "-1"},
        "exact_checks": ["B1B2=0", "B2B3=0", "L1=4I6", "A^3=-4A",
                         "Oq^T Oq=I", "Oq^2=Oh", "all six edge projections"],
        "independent_event_history_scored": False,
        "candidate_agrees_with_prior_fixed_map_completion": False,
        "native_local_transport_bridge_derived": False,
        "physical_promotion": 0,
    }, indent=2))


if __name__ == "__main__":
    main()
