"""Exact tests for flag readout and shared one-time commit."""

from fractions import Fraction as Q
from itertools import combinations, product


def replay():
    faces = tuple(combinations(range(4), 3))
    edges = tuple(combinations(range(4), 2))
    pairs = [(edge, tuple(i for i in range(4) if i not in edge)) for edge in edges[:3]]
    flags = [(face, edge) for face in faces for edge in combinations(face, 2)]
    diagonal, off_diagonal = Q(53, 9), Q(47, 9)
    rate_squared = Q(106, 9)

    for first, second in pairs:
        row = {}
        for face, edge in flags:
            relevant = first if all(i in face for i in first) else second
            sign = 1 if relevant == first else -1
            row[face, edge] = sign * (diagonal if edge == relevant else off_diagonal)
        assert len(row) == 12 and all(row.values())
        for values in product((-1, 0, 1), repeat=5):
            record = dict(zip(edges, (*values, -sum(values))))
            exact = sum(value * record[edge] for (_, edge), value in row.items())
            for flag_first, flag_second in product(
                (flag for flag in flags if flag[1] == first),
                (flag for flag in flags if flag[1] == second),
            ):
                assert exact == rate_squared * (record[flag_first[1]] - record[flag_second[1]])
        off_pair = next(flag for flag in flags if flag[1] not in (first, second))
        assert abs(row[off_pair]) == off_diagonal

    batches = 0
    for length in range(4):
        for submissions in product(range(3), repeat=length):
            ready = True
            commits = 0
            for _ in submissions:
                if ready:
                    ready = False
                    commits += 1
            assert commits == int(bool(set(submissions)))
            batches += 1
    assert batches == 40
    print("729 exact copied records, 2916 two-flag choices, three off-range witnesses, 40 ordered receipt controls passed.")


if __name__ == "__main__":
    replay()
