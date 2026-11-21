#!/usr/bin/env python3
"""Exhaust the equatorial and filled PB5 Z2 edge connections."""

from itertools import combinations, product
from math import prod


def edge(a, b):
    return tuple(sorted((a, b)))


def main():
    rim = [edge(i, (i + 1) % 5) for i in range(5)]
    signs = (-1, 1)
    ring_representatives = {}
    for links in product(signs, repeat=5):
        flux = prod(links)
        assert flux == prod(reversed(links)) == 1 // flux
        switched = {
            tuple(links[i] * gauge[i] * gauge[(i + 1) % 5] for i in range(5))
            for gauge in product(signs, repeat=5)
        }
        assert len(switched) == 16 and {prod(item) for item in switched} == {flux}
        assert (flux,) * 5 in switched
        ring_representatives.setdefault(flux, switched)
        assert ring_representatives[flux] == switched

    cells = [tuple(sorted((i, (i + 1) % 5, 5, 6))) for i in range(5)]
    edges = sorted({side for cell in cells for side in combinations(cell, 2)})
    triangles = sorted({face for cell in cells for face in combinations(cell, 3)})
    caps = [[tuple(sorted((*side, pole))) for side in rim] for pole in (5, 6)]
    radial = [(i, 5, 6) for i in range(5)]
    # Fix the north spokes and spine, a spanning tree, to +1.
    tree = {(i, 5) for i in range(5)} | {(5, 6)}
    free_edges = [side for side in edges if side not in tree]
    assert (len(edges), len(triangles), len(free_edges)) == (16, 15, 10)

    symmetries = [
        tuple((i + 1) % 5 for i in range(5)) + (5, 6),
        tuple((-i) % 5 for i in range(5)) + (5, 6),
        (0, 1, 2, 3, 4, 6, 5),
    ]
    cap_union = set(caps[0] + caps[1])
    negative_support = []
    invariant_patterns = set()
    for config in product(signs, repeat=len(free_edges)):
        links = {**dict.fromkeys(tree, 1), **dict(zip(free_edges, config))}
        flux = prod(links[side] for side in rim)
        curvature = {face: prod(links[side] for side in combinations(face, 2))
                     for face in triangles}
        assert all(prod(curvature[face] for face in cap) == flux for cap in caps)
        assert all(prod(curvature[face] for face in combinations(cell, 3)) == 1
                   for cell in cells)
        if flux == -1:
            support = frozenset(face for face in triangles if curvature[face] == -1)
            negative_support.append(len(support))
            if all({tuple(sorted(p[i] for i in face)) for face in support} == support
                   for p in symmetries):
                invariant_patterns.add(support)

    assert len(negative_support) == 512 and min(negative_support) == 2
    assert invariant_patterns == {frozenset(cap_union), frozenset(cap_union | set(radial))}
    print("Ring: two gauge classes, both invariant under reversal.")
    print("PB5: 1,024 gauge-fixed connections, 512 with negative rim flux.")
    print("Negative flux: minimum curvature support 2; fully symmetric supports 10 and 15.")
    print("No mirror-odd orientation selector from the rim flux alone.")


if __name__ == "__main__":
    main()
