#!/usr/bin/env python3
"""Exact formal source-interface nonuniqueness checks; not a physical test."""
from fractions import Fraction
from itertools import permutations, product
import json

VERTICES = tuple(range(4))
PAIRS = (
    frozenset(((0, 1), (2, 3))),
    frozenset(((0, 2), (1, 3))),
    frozenset(((0, 3), (1, 2))),
)
PAIR_INDEX = {p: i for i, p in enumerate(PAIRS)}


def action(g):
    return tuple(PAIR_INDEX[frozenset(tuple(sorted((g[u], g[v])))
                                      for u, v in pair)] for pair in PAIRS)


def push(bits, pair_map):
    out = [None] * 3
    for old, new in enumerate(pair_map):
        out[new] = bits[old]
    return tuple(out)


def xor(a, b):
    return tuple(x ^ y for x, y in zip(a, b))


def all_bits():
    return tuple(product((0, 1), repeat=3))


def symmetric_kernel(p):
    """Conditional flip-mask distribution given an applied receipt."""
    zero = (0, 0, 0)
    onehots = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    return {zero: 1 - p, **{v: p / 3 for v in onehots}}


def receipt_kernel(q, p):
    """Formal availability with None distinct from a zero-mask receipt."""
    return {None: 1 - q, **{xi: q * v for xi, v in symmetric_kernel(p).items()}}


def run():
    maps = [action(g) for g in permutations(VERTICES)]
    assert len(maps) == 24 and len(set(maps)) == 6
    bits = all_bits()
    cases = 0
    for theta in bits:
        assert len({xor(theta, xi) for xi in bits}) == 8
        for pi in maps:
            for xi in bits:
                assert push(xor(theta, xi), pi) == xor(push(theta, pi), push(xi, pi))
                cases += 1
    assert cases == 1536

    # Both constant source functions are S4 equivariant and comply with the
    # admitted *conditional* algebra, but yield different endpoints.
    zero, full = (0, 0, 0), (1, 1, 1)
    theta = zero
    assert xor(theta, zero) != xor(theta, full)
    for pi in maps:
        assert push(zero, pi) == zero and push(full, pi) == full

    stochastic_checks = 0
    for p in (Fraction(0), Fraction(1, 2), Fraction(1)):
        k = symmetric_kernel(p)
        assert sum(k.values()) == 1 and all(v >= 0 for v in k.values())
        for pi in maps:
            assert {push(x, pi): v for x, v in k.items()} == k
            stochastic_checks += 1
    assert stochastic_checks == 72
    assert symmetric_kernel(Fraction(0)) != symmetric_kernel(Fraction(1))
    availability_checks = 0
    for q in (Fraction(0), Fraction(1, 2), Fraction(1)):
        for p in (Fraction(0), Fraction(1, 2), Fraction(1)):
            k = receipt_kernel(q, p)
            assert sum(k.values()) == 1 and all(v >= 0 for v in k.values())
            for pi in maps:
                transformed = {None if x is None else push(x, pi): v
                               for x, v in k.items()}
                assert transformed == k
                availability_checks += 1
    assert availability_checks == 216
    assert receipt_kernel(Fraction(0), Fraction(1)) != receipt_kernel(Fraction(1), Fraction(0))

    # Separately typed edge-factor completion: same reduced pre-factors,
    # different sourced post-factors. This is not a joint Theta/edge law.
    before = (1, 1)
    hold = (1, 1)
    closure_loss = (0, 1)
    assert before[0] * before[1] == 1
    assert hold[0] * hold[1] == 1
    assert closure_loss[0] * closure_loss[1] == 0

    return {
        'status': 'PASS',
        'pair_covariance_cases': cases,
        'conditional_theta_outputs_per_fixed_theta': 8,
        'distinct_S4_pair_actions': len(set(maps)),
        'symmetric_kernel_checks': stochastic_checks,
        'availability_kernel_checks': availability_checks,
        'deterministic_covariant_completions': 2,
        'edge_factor_branch_witness': 'PASS',
        'physical_promotion': 0,
        'held_out_event_score': 'NOT_RUN',
    }


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
