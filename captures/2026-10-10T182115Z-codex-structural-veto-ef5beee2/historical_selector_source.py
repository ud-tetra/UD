#!/usr/bin/env python3
"""Exact finite audit of the historical JOP §7 v0.4 conditional pair selector."""
import itertools
import json
from collections import Counter
from fractions import Fraction

PAIRS = range(3)


def unique_max(scored):
    if not scored:
        return None
    best = max(score for _, score in scored)
    winners = [key for key, score in scored if score == best]
    return winners[0] if len(winners) == 1 else None


def select(theta, integrity, signed_source, burden_weight):
    """Return (new_theta, branch, chosen addresses), holding on ties or no candidate."""
    total = sum(signed_source)
    if total < 0:
        pool = [(p, (-signed_source[p], -burden_weight[p])) for p in PAIRS
                if theta[p] == 0 and integrity[p] == 1 and signed_source[p] < 0]
        p = unique_max(pool)
        if p is None:
            return theta, "closure_hold", None
        result = list(theta); result[p] = 1
        return tuple(result), "closure", (p,)
    if total > 0:
        pool = [(p, (signed_source[p], burden_weight[p])) for p in PAIRS
                if theta[p] == 1 and integrity[p] == 1 and signed_source[p] > 0]
        p = unique_max(pool)
        if p is None:
            return theta, "reopen_hold", None
        result = list(theta); result[p] = 0
        return tuple(result), "reopen", (p,)
    pool = [((p, q), (burden_weight[q] - burden_weight[p], signed_source[q] - signed_source[p]))
            for p in PAIRS for q in PAIRS
            if theta[p] == 0 and theta[q] == 1 and integrity[p] == integrity[q] == 1
            and burden_weight[q] > burden_weight[p]]
    pq = unique_max(pool)
    if pq is None:
        return theta, "swap_hold", None
    p, q = pq
    result = list(theta); result[p] = 1; result[q] = 0
    return tuple(result), "swap", pq


def permute(x, perm):
    y = [None] * 3
    for p in PAIRS:
        y[perm[p]] = x[p]
    return tuple(y)


def main():
    binary = tuple(itertools.product((0, 1), repeat=3))
    signed = tuple(itertools.product((-1, 0, 1), repeat=3))
    weights = tuple(itertools.product((0, 1, 2), repeat=3))
    perms = tuple(itertools.permutations(PAIRS))
    branches = Counter()
    cases = 0
    for theta, integrity, G, W in itertools.product(binary, binary, signed, weights):
        new, branch, addresses = select(theta, integrity, G, W)
        branches[branch] += 1
        cases += 1
        delta = sum(new) - sum(theta)
        assert delta == (1 if branch == "closure" else -1 if branch == "reopen" else 0)
        if branch == "swap":
            assert sum(G) == 0 and sum(new) == sum(theta)
            assert addresses is not None and W[addresses[1]] > W[addresses[0]]
            old_score = sum((1 - theta[p]) * W[p] for p in PAIRS) * Fraction(1, 4)
            new_score = sum((1 - new[p]) * W[p] for p in PAIRS) * Fraction(1, 4)
            assert new_score - old_score == Fraction(W[addresses[1]] - W[addresses[0]], 4) > 0
        for perm in perms:
            moved, moved_branch, _ = select(*(permute(x, perm) for x in (theta, integrity, G, W)))
            assert moved == permute(new, perm) and moved_branch == branch
    assert cases == 8 * 8 * 27 * 27 == 46656
    assert sum(branches.values()) == cases
    # Direct witnesses, including both sourced restrictions and synthetic controls.
    assert select((0, 1, 1), (1, 1, 1), (-1, 0, 0), (0, 0, 0))[1] == "closure"
    assert select((0, 0, 0), (1, 1, 1), (1, 1, 1), (0, 0, 0))[1] == "reopen_hold"
    assert select((0, 1, 1), (1, 1, 1), (0, 0, 0), (0, 2, 0))[1] == "swap"
    assert select((0, 1, 1), (1, 1, 1), (0, 0, 0), (0, 1, 1))[1] == "swap_hold"
    assert select((0, 1, 1), (0, 1, 1), (-1, 0, 0), (0, 0, 0))[1] == "closure_hold"
    print(json.dumps({"status":"EXACT finite conditional selector / primitive event and edge transport maps OPEN",
                      "synthetic_receipt_cases": cases, "S3_equivariance_checks": cases * len(perms),
                      "branch_counts": dict(sorted(branches.items())),
                      "source_candidate": "JOP Section 7 Directed Parity Source-Law Amendment v0.4",
                      "held_out_target_scored": False, "physical_promotion": 0},indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
