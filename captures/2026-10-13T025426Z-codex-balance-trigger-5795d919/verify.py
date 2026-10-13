"""Exact support-balance trigger and reservoir-lift audit for one K4.

The equality-to-renewal decision and the prepared donor bank are proposed
inputs, not sourced native UD laws.
"""
from fractions import Fraction
from itertools import combinations
import json
import math
from pathlib import Path


V = tuple(range(4))
cells = {k: list(combinations(V, k + 1)) for k in range(4)}
f_old = [len(cells[k]) for k in range(4)]
assert f_old == [4, 6, 4, 1]


def boundary(simplex):
    return {simplex[:i] + simplex[i + 1:]: (-1) ** i for i in range(len(simplex))}


b3 = [boundary((0, 1, 2, 3)).get(face, 0) for face in cells[2]]
f = [Fraction(v, 2) for v in b3]
assert sum(x * x for x in f) == 1
assert all(sum(boundary(face).get(edge, 0) * b3[j]
               for j, face in enumerate(cells[2])) == 0 for edge in cells[1])
assert sum(b3[j] * f[j] for j in range(4)) == 2

# t is the unit top simplex. A t=-2 f, A f=2 t. The prepared trajectory
# c(s)=cos(2s)t - sin(2s)f has E3=cos^2(2s), E2=sin^2(2s).
first_downcrossing = "pi/8"
E3 = Fraction(1, 2)
E2 = Fraction(1, 2)
assert E3 + E2 == 1
assert math.isclose(math.cos(4 * math.pi / 8), 0, abs_tol=1e-15)
assert -4 * math.sin(4 * math.pi / 8) < 0

# Barycentric topological face counts: chains of nested nonempty faces.
all_faces = sum((cells[k] for k in range(4)), [])
f_new = []
for length in range(1, 5):
    n = sum(all(set(flags[i]) < set(flags[i + 1])
                for i in range(length - 1))
            for flags in combinations(all_faces, length))
    f_new.append(n)
assert f_new == [15, 50, 60, 24]

m = [math.factorial(k + 1) for k in range(4)]
assert m == [1, 2, 6, 24]
gram_S = sum(([m[k]] * f_old[k] for k in range(4)), [])
gram_R = sum(([m[k] - 1] * f_old[k] for k in range(4)), [])
assert [1 + x for x in gram_R] == gram_S
rank_R = sum(x > 0 for x in gram_R)
assert rank_R == 11
assert sum(gram_S) == 64  # number of nonzero descendant coordinates across basis vectors
target_dim = sum(f_new)
assert target_dim == 149
assert target_dim - sum(f_old) - rank_R == 123
local_blank_count = sum(f_old[k] * (m[k] - 2) for k in range(1, 4))
assert local_blank_count == 38
assert target_dim - sum(gram_S) == 85
assert local_blank_count + 85 == 123


def householder_block(size):
    """Orthogonal map from (1,sqrt(m-1),0...) to (1,...,1)."""
    if size == 1:
        return [[1.0]]
    x = [1.0] + [math.sqrt(size - 1.0)] + [0.0] * (size - 2)
    y = [1.0] * size
    delta = [x[i] - y[i] for i in range(size)]
    length = math.sqrt(sum(z * z for z in delta))
    if length < 1e-14:
        return [[float(i == j) for j in range(size)] for i in range(size)]
    v = [z / length for z in delta]
    return [[float(i == j) - 2 * v[i] * v[j] for j in range(size)] for i in range(size)]


for size in m:
    H = householder_block(size)
    x = [1.0] if size == 1 else [1.0, math.sqrt(size - 1.0)] + [0.0] * (size - 2)
    assert max(abs(sum(H[i][j] * x[j] for j in range(size)) - 1.0)
               for i in range(size)) < 1e-12
    assert max(abs(sum(H[r][i] * H[r][j] for r in range(size)) - float(i == j))
               for i in range(size) for j in range(size)) < 1e-12

donor_event_norm_sq = 23 * E3 + 5 * E2
assert donor_event_norm_sq == 14

out = {
    "status": "PASS",
    "source_observables": "Q171 top-core and Q172 face-interface stocks, summed on one K4",
    "candidate_decision": "first transverse downward zero of q=E3-E2 while armed; not source-authored admission",
    "prepared_two_mode_generator": "A t=-2 f, A f=2 t; q(s)=cos(4s)",
    "first_downcrossing_internal_s_exact": first_downcrossing,
    "stocks_at_crossing_exact": {"E3": "1/2", "E2": "1/2"},
    "barycentric_face_counts_old": f_old,
    "barycentric_face_counts_new": f_new,
    "subdivision_gram_by_grade_exact": m,
    "donor_gram_by_grade_exact": [x - 1 for x in m],
    "minimum_linear_donor_rank_for_universal_gram_completion": rank_R,
    "total_target_chain_dimension": target_dim,
    "prepared_input_blank_coordinate_count": 123,
    "local_blank_count": local_blank_count,
    "unused_target_coordinate_count": 85,
    "householder_block_unitarity_and_transfer_check": True,
    "donor_support_debit_at_crossing_exact": str(donor_event_norm_sq),
    "post_native_support_at_crossing_exact": str(1 + donor_event_norm_sq),
    "physical_clock_or_bank_preparation": "OPEN",
    "physical_promotion": 0,
}
Path(__file__).with_name("results.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
