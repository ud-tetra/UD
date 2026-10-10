#!/usr/bin/env python3
"""Exact finite audit of sourced exogenous Theta flips and typed edge gates."""
import itertools
import json
from collections import Counter

PAIRS = ((0, 5), (1, 4), (2, 3))  # 01/23, 02/13, 03/12


def permute(x, p):
    return tuple(x[p[i]] for i in range(3))  # Phase 23 direct-event convention


def lift(x):
    e = [None] * 6
    for p, pair in enumerate(PAIRS):
        for a in pair:
            e[a] = x[p]
    return tuple(e)


def audit(theta, p, xi, T):
    y = permute(theta, p)
    after = tuple(y[i] ^ xi[i] for i in range(3))
    cl_before, cl_after = lift(tuple(1 - z for z in y)), lift(tuple(1 - z for z in after))
    hard_before = tuple(cl_before[e] * T[e] for e in range(6))
    hard_after = tuple(cl_after[e] * T[e] for e in range(6))
    C_theta = sum((1 - y[i]) * xi[i] for i in range(3))
    O_theta = sum(y[i] * xi[i] for i in range(3))
    C_cl = sum(a == 1 and b == 0 for a, b in zip(cl_before, cl_after))
    O_cl = sum(a == 0 and b == 1 for a, b in zip(cl_before, cl_after))
    C_h = sum(a == 1 and b == 0 for a, b in zip(hard_before, hard_after))
    O_h = sum(a == 0 and b == 1 for a, b in zip(hard_before, hard_after))
    weighted_C = sum((1 - y[i]) * xi[i] * sum(T[e] for e in PAIRS[i]) for i in range(3))
    weighted_O = sum(y[i] * xi[i] * sum(T[e] for e in PAIRS[i]) for i in range(3))
    assert C_cl == 2 * C_theta and O_cl == 2 * O_theta
    assert C_h == weighted_C and O_h == weighted_O
    assert sum(after) - sum(y) == C_theta - O_theta
    assert tuple(cl_before[e] ^ cl_after[e] for e in range(6)) == lift(xi)
    return after, C_h, O_h, C_cl, O_cl


def main():
    vectors = tuple(itertools.product((0, 1), repeat=3))
    perms = tuple(itertools.permutations(range(3)))
    six_bits = tuple(itertools.product((0, 1), repeat=6))
    cases = 0
    tally = Counter()
    for theta, p, xi, T in itertools.product(vectors, perms, vectors, six_bits):
        after, C_h, O_h, C_cl, O_cl = audit(theta, p, xi, T)
        cases += 1
        tally[(C_cl, O_cl, C_h, O_h)] += 1
        # Pair-relabeling covariance for the complete typed hard-mask readout.
        y = permute(theta, p)
        for q in perms:
            yq, xiq = permute(y, q), permute(xi, q)
            # T has two independent edge values per pair; move the whole pair.
            moved_T = [None] * 6
            for i in range(3):
                for j in range(2):
                    moved_T[PAIRS[i][j]] = T[PAIRS[q[i]][j]]
            moved = audit(yq, (0, 1, 2), xiq, tuple(moved_T))
            assert moved[0] == permute(after, q)
            assert moved[1:5] == (C_h, O_h, C_cl, O_cl)
    assert cases == 8 * 6 * 8 * 64 == 24576
    # Same prestate, permutation and transport factors; two admitted exogenous
    # receipts yield incompatible poststates. No endogenous choice is supplied.
    theta = (0, 1, 0)
    T = (1,) * 6
    close = audit(theta, (0, 1, 2), (1, 0, 0), T)
    reopen = audit(theta, (0, 1, 2), (0, 1, 0), T)
    assert close[0] == (1, 1, 0) and close[3:5] == (2, 0)
    assert reopen[0] == (0, 0, 0) and reopen[3:5] == (0, 2)
    # A failed transport edge cannot appear in a hard-mask change even when
    # its closure factor flips. This keeps closure and hard-mask counts typed.
    partial = audit(theta, (0, 1, 2), (1, 0, 0), (1, 1, 1, 1, 1, 0))
    assert partial[1:5] == (1, 0, 2, 0)
    print(json.dumps({"status":"EXACT conditional exogenous Theta-to-closure and fixed-T hard-mask pushforward",
                      "finite_cases":cases,"pair_covariance_checks":cases * 6,
                      "distinct_count_signatures":len(tally),
                      "same_prestate_closure_poststate":close[0],
                      "same_prestate_reopening_poststate":reopen[0],
                      "transport_partial_closure_edges":partial[3],
                      "transport_partial_hard_edges":partial[1],
                      "endogenous_xi_source_derived":False,
                      "independent_signed_G_event_histories_scored":0,
                      "physical_promotion":0},indent=2))


if __name__ == "__main__":
    main()
