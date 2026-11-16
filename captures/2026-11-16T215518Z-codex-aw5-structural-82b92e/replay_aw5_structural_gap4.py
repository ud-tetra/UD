"""Exact constructor replay for the AW5 structural and compact-gauge notes."""
from fractions import Fraction
from itertools import combinations, permutations, product


def transpose(matrix):
    return list(zip(*matrix))


def multiply(left, right):
    return [[sum(a * b for a, b in zip(row, col)) for col in transpose(right)]
            for row in left]


def boundary(lower, upper):
    matrix = [[0 for _ in upper] for _ in lower]
    for column, cell in enumerate(upper):
        for index in range(len(cell)):
            face = cell[:index] + cell[index + 1:]
            matrix[lower.index(face)][column] = (-1) ** index
    return matrix


def carrier(*tops):
    return [sorted({face for top in tops for face in combinations(top, size)})
            for size in range(1, 5)]


def incidence(cells):
    return [boundary(lower, upper) for lower, upper in zip(cells, cells[1:])]


def cycle_basis(cells, b1, b2):
    vertices, edges, faces, _ = cells
    root = vertices[0][0]
    chords = [i for i, edge in enumerate(edges) if root not in edge]
    triangles = [faces.index((root, *edges[i])) for i in chords]
    basis = [[row[j] for j in triangles] for row in b2]
    assert [basis[i] for i in chords] == [[int(i == j) for j in range(len(chords))]
                                          for i in range(len(chords))]
    assert not any(map(any, multiply(b1, basis)))
    return basis


def verify_defects():
    pairs = [frozenset(((0, 1), (2, 3))), frozenset(((0, 2), (1, 3))),
             frozenset(((0, 3), (1, 2)))]
    action = set()
    for permutation in permutations(range(4)):
        action.add(tuple(pairs.index(frozenset(tuple(sorted((permutation[i], permutation[j])))
                                              for i, j in pair)) for pair in pairs))
    assert len(action) == 6
    assignments = tuple(product((0, 1), repeat=3))
    orbit = lambda v: {tuple(v[i] for i in p) for p in action}
    assert [len(orbit((1,) * w + (0,) * (3 - w))) for w in range(4)] == [1, 3, 3, 1]
    seeded_closed = []
    for mask in product((0, 1), repeat=7):
        defects = {v for v, enabled in zip(assignments[1:], mask) if enabled}
        if any(orbit(v) - defects for v in defects):
            continue
        if not any(sum(v) == 1 for v in defects):
            continue
        if all(tuple(a ^ b for a, b in zip(x, y)) in defects
               for x, y in combinations(defects, 2)
               if not any(a & b for a, b in zip(x, y))):
            seeded_closed.append(defects)
    assert seeded_closed == [set(assignments[1:])]
    print("PASS orbit sizes 1,3,3,1; unique seeded, equivariant disjoint-union closure yields 7 defects.")


def verify_tetrahedron():
    cells = carrier((0, 1, 2, 3))
    b1, b2, b3 = incidence(cells)
    assert not any(map(any, multiply(b1, b2)))
    assert not any(map(any, multiply(b2, b3)))
    down = multiply(transpose(b1), b1)
    up = multiply(b2, transpose(b2))
    assert all(down[i][j] + up[i][j] == 4 * (i == j) for i in range(6) for j in range(6))
    cycles = cycle_basis(cells, b1, b2)
    faces = [[Fraction(x, 2) for x in row] for row in multiply(transpose(b2), cycles)]
    assert multiply(b2, faces) == [[2 * x for x in row] for row in cycles]
    assert multiply(transpose(b3), faces) == [[0, 0, 0]]
    assert multiply(transpose(faces), faces) == multiply(transpose(cycles), cycles)
    print("PASS tetrahedron cycle basis, signed incidence, paired rotation and isometry.")


def verify_bipyramid():
    cells = carrier((0, 1, 2, 3), (0, 1, 2, 4))
    b1, b2, b3 = incidence(cells)
    assert not any(map(any, multiply(b1, b2)))
    assert not any(map(any, multiply(b2, b3)))
    basis = cycle_basis(cells, b1, b2)
    assert len(basis[0]) == 5
    common = cells[2].index((0, 1, 2))
    x = [row[common] for row in b2]
    a = [[Fraction(entry, 4)] for entry in x]
    turns = multiply(transpose(b2), a)
    assert turns[common] == [Fraction(3, 4)]
    assert multiply(transpose(b3), turns) == [[0], [0]]
    assert not any(map(any, multiply(transpose(b2), transpose(b1))))
    print("PASS bipyramid integer cycle basis and gauge invariance; shared loop = 3/4 turn, both tetrahedral relations zero.")


if __name__ == "__main__":
    verify_defects()
    verify_tetrahedron()
    verify_bipyramid()
