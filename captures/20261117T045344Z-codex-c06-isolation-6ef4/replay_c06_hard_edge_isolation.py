"""Exact replay of C06 v0.13 on the ordinary tetrahedron edge module."""

from fractions import Fraction as Q
from itertools import combinations, product


def transpose(matrix):
    return tuple(zip(*matrix))


def multiply(left, right):
    columns = transpose(right)
    return tuple(tuple(sum(a * b for a, b in zip(row, col)) for col in columns)
                 for row in left)


def squared_norm(matrix):
    return sum(value ** 2 for row in matrix for value in row)


def replay():
    vertices = range(4)
    edges = tuple(map(frozenset, combinations(vertices, 2)))
    faces = tuple(map(frozenset, combinations(vertices, 3)))
    flags = tuple((face, e) for face in faces for e in edges if e < face)
    copy = tuple(tuple(int(e == flag_edge) for e in edges) for _, flag_edge in flags)
    identity = tuple(tuple(int(e == f) for f in edges) for e in edges)
    pair_even = tuple(tuple(Q(int(e == f or e.isdisjoint(f)), 2) for f in edges)
                      for e in edges)
    even = tuple(tuple(value - Q(1, 6) for value in row) for row in pair_even)
    odd = tuple(tuple(a - b for a, b in zip(row, sums))
                for row, sums in zip(identity, pair_even))

    assert multiply(transpose(copy), copy) == tuple(tuple(2 * x for x in row)
                                                      for row in identity)
    assert multiply(even, even) == even and multiply(odd, odd) == odd
    assert squared_norm(multiply(even, odd)) == 0
    assert sum(even[i][i] for i in range(6)) == 2
    assert sum(odd[i][i] for i in range(6)) == 3

    # Unit-cell action metric on independent flags, with cyclic face convention.
    metric = tuple(tuple(Q(47 + 6 * (i == j), 9) if face == other_face else 0
                         for j, (other_face, _) in enumerate(flags))
                   for i, (face, _) in enumerate(flags))
    copy_even = multiply(copy, even)
    copy_odd = multiply(copy, odd)
    assert squared_norm(multiply(transpose(copy_even), multiply(metric, copy_odd))) == 0
    assert squared_norm(copy_even) > 0

    zero_cases = 0
    for bits in product((0, 1), repeat=6):
        m = sum(bits)
        for projector, weight in ((even, Q(1, 3)), (odd, Q(1, 2))):
            masked = tuple(tuple(bit * value for value in row)
                           for bit, row in zip(bits, projector))
            assert squared_norm(masked) == m * weight
            forward = multiply(copy, masked)
            assert squared_norm(forward) == 2 * m * weight
            reverse = multiply(transpose(forward), metric)
            assert (squared_norm(reverse) == 0) == (m == 0)
        zero_cases += (m == 0)

    # After latching, the even exchange remains and the odd source and record hold.
    post_latch = copy_even
    assert multiply(post_latch, even) == copy_even
    assert squared_norm(multiply(post_latch, odd)) == 0
    assert squared_norm(multiply(transpose(post_latch), multiply(metric, copy_odd))) == 0
    print("64 exact binary masks; both sector couplings vanish only on the all-closed mask")
    print(f"All-closed controls: {zero_cases}; exact mask norms: m/3 and m/2")
    print("Opposite-pair candidate: even coupling retained; odd source and record isolated")


if __name__ == "__main__":
    replay()
