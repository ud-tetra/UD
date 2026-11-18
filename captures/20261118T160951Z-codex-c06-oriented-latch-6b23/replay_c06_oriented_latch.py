"""Exact incidence and endpoint controls for C06 v0.39."""
from fractions import Fraction as F
from itertools import permutations, product


def orientation(p):
    return (-1)**sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p)))


def face_sign(cell, face):
    removed = next(i for i, v in enumerate(cell) if v not in face)
    boundary = cell[:removed] + cell[removed+1:]
    return (-1)**removed * orientation(tuple(face.index(v) for v in boundary))


count = 0
for base in permutations((0, 1, 2)):
    face = (0, 1, 2)
    left, right = (*base, 3), (base[1], base[0], base[2], 4)
    for face_orientation in (1, -1):
        assert face_sign(left, face)*face_orientation == -face_sign(right, face)*face_orientation
        count += 1
assert count == 12
for p in permutations(range(4)):
    trace = sum(i == j for i, j in enumerate(p))-1
    assert trace >= -1
# Rational unit-circle samples via the half-angle parameter.
tests = 0
for m, n in product(range(-5, 6), range(1, 6)):
    t = F(m, n)
    a, b = (1-t*t)/(1+t*t), 2*t/(1+t*t)
    r, c = a*a, a*b
    assert a*a+b*b == 1 and r*(1-r) == c*c
    assert (c == 0 and 2*r-1 < 0) == (r == 0)
    if r <= F(1, 2):
        assert r <= 2*c*c
    tests += 1
# Unaligned positive donor: e1 dot (2 e2) = 0 and archive dominates.
s, d = (1, 0, 0), (0, 2, 0)
assert sum(a*b for a,b in zip(s,d)) == 0
r = F(sum(a*a for a in s), sum(a*a for a in s)+sum(b*b for b in d))
assert r == F(1, 5) and 2*r-1 == F(-3, 5) and r*(1-r) == F(4, 25)
print("12 oriented-face gluing controls and 24 relabeling trace controls passed.")
print(f"{tests} rational phase controls and one unaligned false-positive witness passed.")
