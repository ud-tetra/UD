"""Exact fixed-port mask and face-projector tests."""

from fractions import Fraction as Q
from itertools import combinations, product


def replay():
    vertices = set(range(4))
    faces = tuple(combinations(range(4), 3))
    edges = tuple(combinations(range(4), 2))
    flags = tuple(e for f in faces for e in combinations(f, 2))
    odd = [{a: int(a == e)-int(set(a) == vertices-set(e)) for a in edges}
           for e in edges if 0 in e]
    copied = [tuple(mode[e] for e in flags) for mode in odd]
    for mask in product((0, 1), repeat=12):
        survives = any(weight * amplitude for mode in copied
                       for weight, amplitude in zip(mask, mode))
        assert survives == any(mask)

    face_rows = [tuple(sum(mode[e] for e in combinations(f, 2)) for mode in odd)
                 for f in faces]
    for three in combinations(face_rows, 3):
        assert all(Q(sum(row[i]*row[j] for row in three), 2)
                   + Q(sum(row[i] for row in three)*sum(row[j] for row in three), 2)
                   == 2*int(i == j) for i, j in product(range(3), repeat=2))
    for left, right in combinations(range(4), 2):
        hidden = [i for i in range(4) if i not in (left, right)]
        mode = tuple(a-b for a, b in zip(*(face_rows[i] for i in hidden)))
        assert any(mode)
        assert all(sum(a*b for a, b in zip(face_rows[i], mode)) == 0
                   for i in (left, right))
    witness = tuple(a-b for a, b in zip(face_rows[0], face_rows[3]))
    assert [sum(a*b for a, b in zip(row, witness)) for row in face_rows] == [4, 0, 0, -4]
    print("4096 exact flag masks, four projector checks, six blind pairs, and one-visible-face witness passed.")


if __name__ == "__main__":
    replay()
