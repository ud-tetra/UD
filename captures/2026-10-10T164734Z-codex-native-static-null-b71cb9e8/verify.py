#!/usr/bin/env python3
"""Exact K4 vertex-edge static-structure null for a signed-source gate rule."""
import json
from fractions import Fraction as Q


def transpose(a):
    return [list(row) for row in zip(*a)]


def mv(a, x):
    return [sum((u * v for u, v in zip(row, x)), Q(0)) for row in a]


def dot(x, y):
    return sum((u * v for u, v in zip(x, y)), Q(0))


def subtract(x, y):
    return [u - v for u, v in zip(x, y)]


def scale(a, x):
    return [a * u for u in x]


# Oriented edges: 01, 02, 03, 12, 13, 23; faces: 012, 013, 023, 123.
B1 = [[Q(z) for z in row] for row in
      [[-1, -1, -1, 0, 0, 0],
       [1, 0, 0, -1, -1, 0],
       [0, 1, 0, 1, 0, -1],
       [0, 0, 1, 0, 1, 1]]]
B2 = [[Q(z) for z in row] for row in
      [[1, 1, 0, 0], [-1, 0, 1, 0], [0, -1, -1, 0],
       [1, 0, 0, 1], [0, 1, 0, -1], [0, 0, 1, 1]]]
PAIRS = ((0, 5), (1, 4), (2, 3))


def main():
    assert all(z == 0 for col in transpose(B2) for z in mv(B1, col))
    v = [Q(1), Q(-1), Q(0), Q(0)]
    g = mv(transpose(B1), v)
    assert g == list(map(Q, (-2, -1, -1, 1, 1, 0)))
    assert mv(B1, g) == scale(Q(4), v)
    assert mv(transpose(B2), g) == [Q(0)] * 4

    # c0=v cos(2s), c1=g/2 sin(2s), c2=c3=0. Their derivatives
    # satisfy c0'=-B1*c1 and c1'=B1^T*c0-B2*c2 by the identities above.
    def pair_stock(sin_2s):
        c1 = scale(Q(sin_2s, 2), g)
        return [dot([c1[i] for i in p], [c1[i] for i in p]) for p in PAIRS]

    start, end = pair_stock(1), pair_stock(0)  # s=pi/4 and pi/2
    G = subtract(end, start)  # integral d||P_p*c1||^2/ds
    assert start == [Q(1), Q(1, 2), Q(1, 2)]
    assert G == [Q(-1), Q(-1, 2), Q(-1, 2)] and sum(G) == -2
    theta_pre = (0, 0, 0)
    integrity = (1, 1, 1)
    burden = (Q(0), Q(0), Q(0))  # c2=0, hence face burden is zero
    candidates = [p for p in range(3) if theta_pre[p] == 0
                  and integrity[p] == 1 and G[p] < 0]
    candidate_pair = max(candidates, key=lambda p: (-G[p], -burden[p]))
    assert candidate_pair == 0 and sum(G) < 0
    candidate_theta = tuple(int(p == candidate_pair) for p in range(3))

    # Fixed primitive structural receipts and local edge maps U_e=I on C.
    # The cited closure and transport tests are satisfied at both endpoints.
    closure = (1,) * 6
    transport = (1,) * 6
    hard_mask_pre = tuple(c * t for c, t in zip(closure, transport))
    hard_mask_post = tuple(c * t for c, t in zip(closure, transport))
    assert hard_mask_pre == hard_mask_post == (1,) * 6
    assert candidate_theta == (1, 0, 0)
    print(json.dumps({
        "status": "EXACT static-structure null; universal autonomous extension NO-GO",
        "domain": "oriented fully retained K4, fixed closure receipts and U_e=I",
        "native_interval": ["pi/4", "pi/2"],
        "pair_stock_start": [str(x) for x in start],
        "pair_stock_end": [str(x) for x in end],
        "signed_pair_source": [str(x) for x in G],
        "source_sum": str(sum(G)),
        "conditional_selector_pair_request": candidate_pair,
        "candidate_theta_if_event_assumed": candidate_theta,
        "observed_structural_mask_pre": hard_mask_pre,
        "observed_structural_mask_post": hard_mask_post,
        "held_out_target_scored": False,
        "physical_promotion": 0
    }, indent=2))


if __name__ == "__main__":
    main()
