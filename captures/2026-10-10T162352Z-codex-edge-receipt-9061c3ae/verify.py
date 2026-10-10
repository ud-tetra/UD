#!/usr/bin/env python3
"""Finite, exact checks for the tetrahedral edge-mask receipt carrier."""
import itertools
import json
from collections import Counter

V = range(4)
EDGES = tuple(itertools.combinations(V, 2))
PAIRS = (( (0, 1), (2, 3) ), ( (0, 2), (1, 3) ), ( (0, 3), (1, 2) ))
PERMS = tuple(itertools.permutations(V))


def acted_mask(mask, perm):
    transformed = {}
    for edge, bit in zip(EDGES, mask):
        transformed[tuple(sorted((perm[edge[0]], perm[edge[1]])))] = bit
    return tuple(transformed[e] for e in EDGES)


def acted_pair(pair, perm):
    return frozenset(tuple(sorted((perm[a], perm[b]))) for a, b in pair)


def encode(mask):
    d = dict(zip(EDGES, mask))
    return tuple((d[e0] + d[e1], None if d[e0] == d[e1] else int(d[e0]))
                 for e0, e1 in PAIRS)


def decode(record):
    d = {}
    for (e0, e1), (count, selector) in zip(PAIRS, record):
        if count == 0:
            assert selector is None
            d[e0] = d[e1] = 0
        elif count == 2:
            assert selector is None
            d[e0] = d[e1] = 1
        else:
            assert count == 1 and selector in (0, 1)
            d[e0], d[e1] = selector, 1 - selector
    return tuple(d[e] for e in EDGES)


def acted_record(record, perm):
    """Act directly on pair counts and within-pair selectors."""
    output = [None] * len(PAIRS)
    for (e0, e1), (count, selector) in zip(PAIRS, record):
        mapped_first = tuple(sorted((perm[e0[0]], perm[e0[1]])))
        target = next(i for i, pair in enumerate(PAIRS) if mapped_first in pair)
        target_selector = (selector if mapped_first == PAIRS[target][0] else 1 - selector) if count == 1 else None
        output[target] = (count, target_selector)
    return tuple(output)


def main():
    masks = tuple(itertools.product((0, 1), repeat=6))
    assert len(set(map(encode, masks))) == 64
    assert all(decode(encode(m)) == m for m in masks)
    checks = 2

    # Compare the independent record action with the six-edge action.
    for perm in PERMS:
        assert {acted_pair(p, perm) for p in PAIRS} == {frozenset(p) for p in PAIRS}
        for m in masks:
            assert encode(acted_mask(m, perm)) == acted_record(encode(m), perm)
    checks += 24 * 64

    kernel = tuple(p for p in PERMS if all(acted_pair(pair, p) == frozenset(pair) for pair in PAIRS))
    assert len(kernel) == 4
    fixed = [sum(acted_mask(m, p) == m for m in masks) for p in kernel]
    assert sorted(fixed) == [16, 16, 16, 64]
    orbit_count_burnside = sum(fixed) // len(kernel)
    assert sum(fixed) % len(kernel) == 0 and orbit_count_burnside == 28
    checks += 3

    # Direct orbit enumeration is independent of the fixed-point formula.
    unseen = set(masks)
    orbits = []
    while unseen:
        seed = next(iter(unseen))
        orbit = {acted_mask(seed, p) for p in kernel}
        assert orbit <= unseen
        orbits.append(orbit)
        unseen -= orbit
    assert len(orbits) == orbit_count_burnside
    checks += 1

    counts = Counter(tuple(n for n, _ in encode(m)) for m in masks)
    assert len(counts) == 27
    assert Counter(counts.values()) == Counter({1: 8, 2: 12, 4: 6, 8: 1})
    distribution = Counter()
    for orbit in orbits:
        signatures = {tuple(n for n, _ in encode(m)) for m in orbit}
        assert len(signatures) == 1
        distribution[next(iter(signatures))] += 1
    assert Counter(distribution.values()) == Counter({1: 26, 2: 1})
    assert distribution[(1, 1, 1)] == 2
    checks += 5

    # Pair-level source constraints, separate from six-edge mask typing.
    admissible = tuple((T, L, q) for T, L, q in itertools.product((0, 1), repeat=3)
                       if T * L <= q <= T)
    assert len(admissible) == 5
    source_transitions = tuple(itertools.product(itertools.product((0, 1), repeat=2), repeat=2))
    diffs = []
    for (Tm, Lm), (Tp, Lp) in source_transitions:
        qm = Tm * Lm  # previous saturation assumption
        close = Tp * Lp
        hold = Tp * int(bool(qm or Tp * Lp))
        if close != hold:
            diffs.append(((Tm, Lm), (Tp, Lp)))
        assert Tp * Lp <= close <= Tp and Tp * Lp <= hold <= Tp
    assert len(source_transitions) == 16
    assert diffs == [((1, 1), (1, 0))]
    checks += 4

    result = {
        "status": "EXACT finite carrier and conditional pair-rule no-go; physical promotion 0",
        "checks": checks,
        "S4_order": len(PERMS),
        "V4_order": len(kernel),
        "binary_edge_masks": len(masks),
        "edge_records": len(set(map(encode, masks))),
        "fixed_mask_counts_V4": sorted(fixed),
        "V4_orbits_burnside": orbit_count_burnside,
        "V4_orbits_direct": len(orbits),
        "pair_count_signatures": len(counts),
        "signature_multiplicities": {str(k): v for k, v in sorted(Counter(counts.values()).items())},
        "all_mixed_signature_orbits": distribution[(1, 1, 1)],
        "admissible_pair_triples": len(admissible),
        "saturated_source_transitions": len(source_transitions),
        "close_hold_disagreements": diffs,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return result


if __name__ == "__main__":
    main()
