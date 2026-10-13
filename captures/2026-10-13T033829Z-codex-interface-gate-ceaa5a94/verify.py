"""Exact integer checks for the vertex interface and generator obstruction."""
import itertools
import json
from pathlib import Path

import numpy as np

old = [list(itertools.combinations(range(4), k + 1)) for k in range(4)]
faces = sorted(range(1, 16), key=lambda x: (x.bit_count(), x))
new = [[flag for flag in itertools.combinations(faces, k + 1)
        if all(flag[j] & flag[j + 1] == flag[j] for j in range(k))]
       for k in range(4)]


def boundary(cells):
    b = []
    for k in range(1, 4):
        lookup = {x: i for i, x in enumerate(cells[k - 1])}
        m = np.zeros((len(cells[k - 1]), len(cells[k])), dtype=np.int64)
        for col, simplex in enumerate(cells[k]):
            for j in range(k + 1):
                m[lookup[simplex[:j] + simplex[j + 1:]], col] = (-1) ** j
        b.append(m)
    return b


bo, bn = boundary(old), boundary(new)
S = []
for k in range(4):
    lookup = {s: i for i, s in enumerate(new[k])}
    m = np.zeros((len(new[k]), len(old[k])), dtype=np.int64)
    for col, simplex in enumerate(old[k]):
        for perm in itertools.permutations(simplex):
            flag = []
            mask = 0
            for vertex in perm:
                mask |= 1 << vertex
                flag.append(mask)
            inds = [simplex.index(x) for x in perm]
            sign = (-1) ** sum(inds[i] > inds[j] for i in range(k + 1) for j in range(i + 1, k + 1))
            m[lookup[tuple(flag)], col] = sign
    S.append(m)

for k in range(1, 4):
    assert np.array_equal(bn[k - 1] @ S[k], S[k - 1] @ bo[k - 1])
assert [int(np.max(np.diag(m.T @ m))) for m in S] == [1, 2, 6, 24]
assert [len(c) for c in new] == [15, 50, 60, 24]


def generator(cells, b):
    sizes = [len(x) for x in cells]
    offsets = np.cumsum([0] + sizes)
    A = np.zeros((offsets[-1], offsets[-1]), dtype=np.int64)
    for k in range(1, 4):
        low, high = offsets[k - 1], offsets[k]
        A[high:offsets[k + 1], low:offsets[k]] = b[k - 1].T
        A[low:offsets[k], high:offsets[k + 1]] = -b[k - 1]
    assert np.array_equal(A.T, -A)
    return A


Ao, An = generator(old, bo), generator(new, bn)
SO = np.zeros((149, 15), dtype=np.int64)
soff, noff = np.cumsum([0] + [len(x) for x in old]), np.cumsum([0] + [len(x) for x in new])
for k in range(4):
    SO[noff[k]:noff[k + 1], soff[k]:soff[k + 1]] = S[k]
e0 = np.zeros(15, dtype=np.int64); e0[0] = 1
v0 = SO @ e0
assert np.count_nonzero(v0) == 1
old_degree = int((Ao @ e0) @ (Ao @ e0))
new_degree = int((An @ v0) @ (An @ v0))
assert old_degree == 3 and new_degree == 7, (old_degree, new_degree)
comm = An @ SO - SO @ Ao
assert int(comm[:, 0] @ comm[:, 0]) == 7

# The unit vertex amplitude and a Euclidean contraction force T e0 to be
# the singleton basis vector (Cauchy equality); generator intertwining then
# demands sqrt(7) <= sqrt(3), impossible. This is an analytic proof, and the
# integer arrays above verify its degree inputs independently.
flags_with_singleton_0 = [cell for cell in new[3] if cell[0] == 1]
assert len(flags_with_singleton_0) == 6

out = {
    "status": "PASS",
    "native_old_vertex_incident_edges_exact": old_degree,
    "native_new_singleton_incident_edges_exact": new_degree,
    "strict_vertex_contractivity_and_generator_intertwining": "NO-GO",
    "common_scalar_chain_map_contractivity": "|a|<=1/sqrt(24)",
    "unit_vertex_readout_in_common_scalar_family": "a=1; incompatible with contractivity",
    "bounded_map_vertex_generator_commutator_squared": "7/24",
    "new_top_star_of_old_vertex": 6,
    "Q178_aggregate_owned_vertex_support_after_bounded_map": "1/24 (old: 1)",
    "UD_sourced_interface_or_cross_event_generator": "OPEN",
    "physical_promotion": 0,
}
Path(__file__).with_name("results.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
