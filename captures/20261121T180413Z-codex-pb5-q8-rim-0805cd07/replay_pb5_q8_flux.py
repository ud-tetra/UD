#!/usr/bin/env python3
"""Exact quaternion rim and relative holonomy checks on PB5."""

from fractions import Fraction
from itertools import combinations, product

Q8 = (-4, -3, -2, -1, 1, 2, 3, 4)  # ±(1, i, j, k)
TABLE = ((1, 2, 3, 4), (2, -1, 4, -3),
         (3, -4, -1, 2), (4, 3, -2, -1))
CELLS = [tuple(sorted((i, (i + 1) % 5, 5, 6))) for i in range(5)]
EDGES = sorted({e for cell in CELLS for e in combinations(cell, 2)})
ROTATION = (1, 2, 3, 4, 0, 5, 6)
MIRROR = (0, 4, 3, 2, 1, 5, 6)
POLE_SWAP = (0, 1, 2, 3, 4, 6, 5)


def mul(a, b):
    sign = -1 if (a < 0) != (b < 0) else 1
    return sign * TABLE[abs(a)-1][abs(b)-1]


def inv(a):
    return a if abs(a) == 1 else -a


def chi(a):
    return a if abs(a) == 1 else 0


def link(links, a, b):
    return links[a, b] if a < b else inv(links[b, a])


def holonomy(links, loop):
    result = 1
    for a, b in zip(loop, loop[1:]):
        result = mul(result, link(links, a, b))
    return result


def permute(links, permutation):
    return {(a, b): link(links, permutation[a], permutation[b]) for a, b in EDGES}


def switch(links, vertex, h):
    gauge = [h if i == vertex else 1 for i in range(7)]
    return {(a, b): mul(mul(gauge[a], u), inv(gauge[b])) for (a, b), u in links.items()}


def signal(links):
    values = []
    for base in range(5):
        rim = tuple((base + k) % 5 for k in range(6))
        w = holonomy(links, rim)
        references = [holonomy(links, (base, (base+d) % 5, pole, base))
                      for d, pole in product((-1, 1), (5, 6))]
        weight = Fraction(sum(map(chi, references)), 4)
        contrast = Fraction(sum(chi(mul(w, v)) - chi(mul(inv(w), v))
                                for v in references), 4)
        values.append(weight * contrast)
    return sum(values)


def main():
    for w in Q8:
        assert any(mul(mul(g, w), inv(g)) == inv(w) for g in Q8)
        assert chi(w) == chi(inv(w))
    for w, v, g in product(Q8, repeat=3):
        w_g = mul(mul(g, w), inv(g))
        v_g = mul(mul(g, v), inv(g))
        assert chi(mul(w_g, v_g)) == chi(mul(w, v))

    links = dict.fromkeys(EDGES, 1)
    links[0, 1] = 2
    links[2, 5] = links[2, 6] = 3
    assert mul(2, 3) != mul(3, 2)
    assert holonomy(links, (0, 1, 2, 3, 4, 0)) == 2
    assert holonomy(links, (1, 2, 5, 1)) == 3
    assert signal(links) == -Fraction(1, 2)
    assert signal(permute(links, ROTATION)) == signal(links)
    assert signal(permute(links, MIRROR)) == -signal(links)
    assert permute(links, POLE_SWAP) == links
    for vertex, g in product(range(7), Q8):
        assert signal(switch(links, vertex, g)) == signal(links)

    # A mirror-symmetric connection has an order-four holonomy as well.
    symmetric = dict.fromkeys(EDGES, 1)
    for a in range(5):
        b = (a + 1) % 5
        symmetric[tuple(sorted((a, b)))] = 2 if a < b else -2
    assert holonomy(symmetric, (0, 1, 2, 3, 4, 0)) == 2
    mirrored = permute(symmetric, MIRROR)
    for vertex in range(7):
        mirrored = switch(mirrored, vertex, 3)
    assert mirrored == symmetric and signal(symmetric) == 0

    print("All 8 rim holonomies are conjugate to their inverses.")
    print("A rotation-even, vertical-mirror-odd, pole-even comparison is -1/2 on the supplied example.")
    print("Order-four flux also occurs in a connection mirror-symmetric up to gauge.")


if __name__ == "__main__":
    main()
