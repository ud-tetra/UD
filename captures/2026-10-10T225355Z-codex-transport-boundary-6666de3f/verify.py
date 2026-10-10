#!/usr/bin/env python3
"""Exact rational audit of a conditional contractive edge-map transition class."""
import itertools
import json
from collections import Counter
from fractions import Fraction as F

I = ((F(1), F(0)), (F(0), F(1)))
Z = ((F(0), F(0)), (F(0), F(0)))


def tr(A):
    return ((A[0][0], A[1][0]), (A[0][1], A[1][1]))


def mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def sub(A, B):
    return tuple(tuple(A[i][j] - B[i][j] for j in range(2)) for i in range(2))


def gram(A):
    return mul(tr(A), A)


def psd(A):
    return A[0][0] >= 0 and A[1][1] >= 0 and A[0][1] == A[1][0] and (
        A[0][0] * A[1][1] - A[0][1] * A[1][0] >= 0)


def diagonal(a, b):
    return ((a, F(0)), (F(0), b))


def main():
    signed_perms = []
    for pi in itertools.permutations(range(2)):
        for signs in itertools.product((-1, 1), repeat=2):
            V = tuple(tuple(F(signs[i] if pi[i] == j else 0)
                            for j in range(2)) for i in range(2))
            assert gram(V) == I
            signed_perms.append(V)
    assert len(signed_perms) == 8
    contractions = tuple(diagonal(a, b) for a, b in itertools.product(
        (F(0), F(1, 2), F(1)), repeat=2))
    counts = Counter()
    for V1, C1, V2, C2 in itertools.product(signed_perms, contractions,
                                            signed_perms, contractions):
        U0 = I
        U1 = mul(mul(V1, C1), U0)
        U2 = mul(mul(V2, C2), U1)
        Q0, Q1, Q2 = (sub(I, gram(U)) for U in (U0, U1, U2))
        d1 = mul(mul(tr(U0), sub(I, gram(C1))), U0)
        d2 = mul(mul(tr(U1), sub(I, gram(C2))), U1)
        assert Q0 == Z and sub(Q1, Q0) == d1 and sub(Q2, Q1) == d2
        assert psd(Q1) and psd(Q2) and psd(d1) and psd(d2)
        T0, T1, T2 = (int(Q == Z) for Q in (Q0, Q1, Q2))
        assert T0 == 1 and T2 <= T1
        assert T1 == int(gram(C1) == I)
        if T1:
            assert T2 == int(gram(C2) == I)
        counts["two_step_sequences"] += 1
        counts["first_step_integrity_fails"] += int(T1 == 0)
        counts["second_step_integrity_fails_newly"] += int(T1 == 1 and T2 == 0)
        counts["reopenings"] += int(T1 == 0 and T2 == 1)
        counts["rank_loss_sequences"] += int(C1[0][0] == 0 or C1[1][1] == 0)
    assert counts["two_step_sequences"] == 8 * 9 * 8 * 9 == 5184
    assert counts["reopenings"] == 0
    # An isometric signed permutation can change U without failing integrity.
    assert sub(I, gram(mul(signed_perms[-1], I))) == Z
    # A deliberately source-free G-sign -> contraction proposal would fail the
    # prior fixed-structure K4 null: G<0, yet its local U was declared fixed I.
    proposed_from_loss = diagonal(F(1, 2), F(1))
    assert sub(I, gram(proposed_from_loss)) != Z
    print(json.dumps({
        "status": "EXACT conditional contraction recurrence; no source-derived step map",
        "counts": dict(counts),
        "hard_transport_reopening_in_pure_contraction_class": False,
        "self_loss_zero_state_is_invariant_if_step_is_isometric_at_Q_zero": True,
        "negative_signed_support_alone_would_false_trigger_static_K4_null": True,
        "primitive_contraction_from_pre_event_UD_state_derived": False,
        "independent_event_history_scored": False,
        "physical_promotion": 0,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
