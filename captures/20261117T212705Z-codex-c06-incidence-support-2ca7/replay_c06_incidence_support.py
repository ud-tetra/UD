"""Exact controls for the fixed-support incidence obstruction."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def apply(matrix, vector):
    return tuple(dot(row, vector) for row in matrix)


def rank(matrix):
    rows = [list(map(Fraction, row)) for row in matrix]
    count = 0
    for col in range(len(rows[0])):
        pivot = next((i for i in range(count, len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[count], rows[pivot] = rows[pivot], rows[count]
        for i in range(count + 1, len(rows)):
            scale = rows[i][col] / rows[count][col]
            rows[i] = [a - scale * b for a, b in zip(rows[i], rows[count])]
        count += 1
    return count


vertices = tuple(range(4))
edges = tuple(combinations(vertices, 2))
faces = tuple(combinations(vertices, 3))
pairs = tuple((i, 5-i) for i in range(3))
b1 = tuple(tuple(int(v == j) - int(v == i) for i, j in edges)
           for v in vertices)
curl = tuple(tuple(int(e == (i, j)) + int(e == (j, k)) - int(e == (i, k))
                   for e in edges) for i, j, k in faces)
witness = apply(tuple(zip(*b1)), (0, 1, 1, 0))
assert witness == (1, 1, 0, 0, -1, -1)
assert apply(b1, witness) == (-2, 2, 2, -2)
assert apply(curl, witness) == (0, 0, 0, 0)
assert rank(tuple(tuple(row[i]-row[j] for i, j in pairs) for row in b1)) == 2

local_supports = [tuple(v in edge for edge in edges) for v in vertices]
local_supports += [tuple(set(edge) <= set(face) for edge in edges) for face in faces]
dimensions = Counter()
for support in product((False, True), repeat=6):
    # One free common coefficient per complete opposite pair in the support.
    dimensions[sum(support[i] and support[j] for i, j in pairs)] += 1
assert dimensions == {0: 27, 1: 27, 2: 9, 3: 1}
assert all(not any(mask[i] and mask[j] for i, j in pairs)
           for mask in local_supports)

p_plus = tuple(tuple(Fraction(int(j in (i, 5-i)), 2) for j in range(6))
               for i in range(6))
for row in p_plus:
    assert all(row[i] == row[j] for i, j in pairs)
    assert [sum(value + shift != 0 for value in row)
            for shift in (0, Fraction(-1, 2), 1)] == [2, 4, 6]
for left, right in combinations(pairs, 2):
    even = tuple(int(i in left) - int(i in right) for i in range(6))
    assert apply(p_plus, even) == even
assert rank(tuple(tuple(int(i == j) - p_plus[i][j] for j in range(6))
                  for i in range(6))) == 3

print('Signed gradient witness, divergence and rank-two boundary restriction passed.')
print('64 masks: 27 admit no nonzero odd-annihilating row; all eight local supports are in this class.')
print('Six exact pair-average rows, support sizes 2/4/6 and rank-three cut passed.')
