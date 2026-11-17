"""Exact tetrahedral face coverage and balance controls."""

from itertools import combinations, product


def replay():
    vertices = set(range(4))
    faces = tuple(combinations(range(4), 3))
    edges = tuple(combinations(range(4), 2))

    def opposite(edge):
        return tuple(sorted(vertices - set(edge)))

    def read(values):
        return tuple(sum(values[e] for e in combinations(face, 2)) for face in faces)

    for left, right in product(faces, repeat=2):
        assert len(set(combinations(left, 2)) & set(combinations(right, 2))) == (3 if left == right else 1)

    tested = 0
    for free in product(range(-1, 2), repeat=5):
        z = dict(zip(edges, (*free, -sum(free))))
        odd_twice = {e: z[e] - z[opposite(e)] for e in edges}
        sums = read(z)
        assert sum(sums) == 0 and read(odd_twice) == tuple(2*s for s in sums)
        assert 2 * sum(s*s for s in sums) == sum(v*v for v in odd_twice.values())
        for three in combinations(range(4), 3):
            assert any(sums) == any(sums[i] for i in three)
            assert 12*max(sums[i]**2 for i in three) >= sum(s*s for s in sums)
        for u, v in ((7, 1), (5, 5), (1, 7)):
            balances = tuple((v*s)**2-(u*s)**2 for s in sums)
            assert sum(balances) == (v*v-u*u)*sum(s*s for s in sums)
            assert any(s != 0 and b == 0 for s, b in zip(sums, balances)) == (any(sums) and u == v)
            tested += 1

    for observed in combinations(range(4), 2):
        hidden = sorted(set(range(4)) - set(observed))
        witness = tuple(int(i == hidden[0])-int(i == hidden[1]) for i in range(4))
        lifted = {e: sum(v for f, v in zip(faces, witness) if set(e) <= set(f)) for e in edges}
        assert read(lifted) == tuple(2*v for v in witness)
    assert 12*max(s*s for s in (1, 1, 1)) == 1+1+1+9
    assert tested == 729
    print("729 exact balance controls passed, plus six blind-pair witnesses and the sharp coverage bound.")


if __name__ == "__main__":
    replay()
