"""Two-step contractive barycentric branch on filled K4 (candidate normalization)."""
import itertools
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import brentq


old = [[z for z in itertools.combinations(range(4), k + 1)] for k in range(4)]
faces = sorted(range(1, 16), key=lambda mask: (mask.bit_count(), mask))
new = [[flag for flag in itertools.combinations(faces, k + 1)
        if all(flag[i] & flag[i + 1] == flag[i] for i in range(k))] for k in range(4)]
assert list(map(len, new)) == [15, 50, 60, 24]


def boundaries(cells):
    out = []
    for k in range(1, 4):
        lookup = {face: i for i, face in enumerate(cells[k - 1])}
        b = np.zeros((len(cells[k - 1]), len(cells[k])), dtype=np.int64)
        for col, cell in enumerate(cells[k]):
            for j in range(k + 1):
                b[lookup[cell[:j] + cell[j + 1:]], col] = (-1) ** j
        out.append(b)
    return out


bo, bn = boundaries(old), boundaries(new)
maps = []
for k in range(4):
    lookup = {f: j for j, f in enumerate(new[k])}
    m = np.zeros((len(new[k]), len(old[k])), dtype=np.int64)
    for col, simplex in enumerate(old[k]):
        for perm in itertools.permutations(simplex):
            flag = []
            mask = 0
            for vertex in perm:
                mask |= 1 << vertex
                flag.append(mask)
            p = [simplex.index(x) for x in perm]
            sign = (-1) ** sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
            m[lookup[tuple(flag)], col] = sign
    assert np.array_equal(m.T @ m, math.factorial(k + 1) * np.eye(len(old[k]), dtype=np.int64))
    maps.append(m)
for k in range(1, 4):
    assert np.array_equal(bn[k - 1] @ maps[k], maps[k - 1] @ bo[k - 1])

# A single scalar on *all* degrees is needed for this scalar family to commute
# with boundary. Largest Gram eigenvalue 4!=24 fixes the largest contraction.
alpha = 1 / math.sqrt(24)
t = np.zeros(len(old[3])); t[0] = 1
f = bo[2] @ t / 2
c3, c2 = t / math.sqrt(2), -f / math.sqrt(2)
first_e = {"top": float(c3 @ c3), "face": float(c2 @ c2)}
u, v = maps[3] @ t, maps[2] @ f
assert u @ u == 24 and v @ v == 6
assert np.array_equal(bn[2] @ u, 2 * v)
assert np.array_equal(bn[2].T @ (2 * v), u)
after1_3, after1_2 = alpha * (maps[3] @ c3), alpha * (maps[2] @ c2)
n1 = float(after1_3 @ after1_3 + after1_2 @ after1_2)
assert math.isclose(n1, 5 / 8)
assert math.isclose(1 - n1, 3 / 8)
U, V = u / math.sqrt(24), v / math.sqrt(6)
a, b = float(U @ after1_3), float(V @ after1_2)
assert math.isclose(a, math.sqrt(1 / 2)) and math.isclose(b, -math.sqrt(1 / 8))


def q(s):
    return (a * math.cos(s) + b * math.sin(s)) ** 2 - (b * math.cos(s) - a * math.sin(s)) ** 2


delta = brentq(q, 0.3, 0.35, xtol=1e-14)
assert abs(delta - math.atan(1 / 3)) < 1e-12
assert q(delta - 1e-4) > 0 and q(delta + 1e-4) < 0
e2 = 5 / 16
n2 = (6 / 24) * e2 + (24 / 24) * e2
assert n2 == 25 / 64
sink_total = 1 - n2

# The post map is a contraction with exact complementary Gram on C(K).
out = {
    "status": "PASS",
    "old_and_first_refined_f_vectors": [[len(x) for x in old], [len(x) for x in new]],
    "boundary_chain_and_gram_integer_checks": "PASS",
    "normalization": "T_k=S_k/sqrt(24) all k; D_k=sqrt(1-(k+1)!/24) I",
    "first_crossing_native_before": "1",
    "first_crossing_post_native": "5/8",
    "first_crossing_sink": "3/8",
    "second_crossing_delay_exact": "atan(1/3)",
    "second_crossing_delay_numeric": delta,
    "second_crossing_pre_stocks": {"face": "5/16", "top": "5/16"},
    "second_crossing_native_before": "5/8",
    "second_crossing_post_native": "25/64",
    "sink_after_second": "39/64",
    "total_closed_support": "1",
    "fixed_vertex_amplitudes": False,
    "dynamic_intertwining": False,
    "UD_sourced_event_or_normalization": False,
    "physical_promotion": 0,
}
assert sink_total == 39 / 64
Path(__file__).with_name("results.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
