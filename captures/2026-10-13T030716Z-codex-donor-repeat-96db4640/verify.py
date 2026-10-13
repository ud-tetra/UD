"""Prepared joint rotor proof and exploratory first repeat on sd(K4)."""
import itertools
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import brentq


# Five orthonormal abstract axes: top t, face f, donor top,
# donor face, and a residual bank sink. This joint model is engineered.
v0 = np.array([1, 0, math.sqrt(23), 0, 0], dtype=float)
v1 = np.array([0, -1, 0, -math.sqrt(5), math.sqrt(18)], dtype=float)
assert math.isclose(v0 @ v0, 24) and math.isclose(v1 @ v1, 24)
assert v0 @ v1 == 0
Aj = (np.outer(v1, v0) - np.outer(v0, v1)) / 12
assert np.max(np.abs(Aj.T + Aj)) < 1e-14
assert np.max(np.abs(Aj @ v0 - 2 * v1)) < 1e-14
assert np.max(np.abs(Aj @ v1 + 2 * v0)) < 1e-14
first = (v0 + v1) / math.sqrt(2)
assert math.isclose(first[:2] @ first[:2], 1)
assert math.isclose(first[2:4] @ first[2:4], 14)
assert math.isclose(first[4] ** 2, 9)
assert math.isclose(first @ first, 24)


# Build the barycentric subdivision of one oriented filled tetrahedron.
faces = sorted(range(1, 16), key=lambda mask: (mask.bit_count(), mask))
cells = []
for length in range(1, 5):
    cells.append([
        flag for flag in itertools.combinations(faces, length)
        if all(flag[i] & flag[i + 1] == flag[i] for i in range(length - 1))
    ])
assert [len(c) for c in cells] == [15, 50, 60, 24]
lookup = [{flag: i for i, flag in enumerate(cells[k])} for k in range(4)]
offsets = np.cumsum([0] + [len(c) for c in cells])
A = np.zeros((149, 149))
for k in range(1, 4):
    for j, simplex in enumerate(cells[k]):
        for i in range(k + 1):
            face = simplex[:i] + simplex[i + 1:]
            row = offsets[k - 1] + lookup[k - 1][face]
            col = offsets[k] + j
            b = (-1) ** i
            A[col, row] += b
            A[row, col] -= b
assert np.max(np.abs(A.T + A)) == 0


def sign_perm(p, basis):
    x = [basis.index(z) for z in p]
    return (-1) ** sum(x[i] > x[j] for i in range(len(x)) for j in range(i + 1, len(x)))


def subdivided_old_simplex(basis, amp, out):
    k = len(basis) - 1
    for p in itertools.permutations(basis):
        prefix = 0
        flag = []
        for vertex in p:
            prefix |= 1 << vertex
            flag.append(prefix)
        out[offsets[k] + lookup[k][tuple(flag)]] += amp * sign_perm(p, basis)


u = np.zeros(149)
w = np.zeros(149)
old_top = (0, 1, 2, 3)
subdivided_old_simplex(old_top, 1, u)
for omit in range(4):
    face = tuple(v for v in old_top if v != omit)
    subdivided_old_simplex(face, (-1) ** omit / 2, w)
# Exact integer incidence identities: A u=-2w, A w=u/2.
assert np.array_equal(A @ u, -2 * w)
assert np.array_equal(2 * (A @ w), u)
assert u @ u == 24 and w @ w == 6 and u @ w == 0
post = (u - w) / math.sqrt(2)
assert math.isclose(post @ post, 15)


def stocks(c):
    squared = np.abs(c) ** 2
    return [float(sum(squared[offsets[k]:offsets[k + 1]])) for k in range(4)]


start = stocks(post)
assert np.allclose(start, [0, 0, 3, 12], atol=1e-12)
# Spectral propagation under the *new* native skew generator.
evals, eigvec = np.linalg.eigh(1j * A)
coeff = eigvec.conj().T @ post


def evolved(t):
    c = eigvec @ (np.exp(-1j * evals * t) * coeff)
    assert max(abs(z.imag) for z in c) < 1e-10
    return c.real


def q(t):
    e = stocks(evolved(t))
    return e[3] - e[2]


grid = np.linspace(0, 3, 1201)
brackets = [(float(grid[i]), float(grid[i + 1])) for i in range(len(grid) - 1)
            if q(float(grid[i])) > 0 and q(float(grid[i + 1])) < 0]
assert brackets, 'no second downward crossing found in scan'
t2 = brentq(q, *brackets[0], xtol=1e-14)
e2 = stocks(evolved(t2))
assert abs(t2 - math.atan(1 / 3)) < 1e-12
assert np.allclose(e2, [0, 0, 7.5, 7.5], atol=1e-10)
assert abs(sum(e2) - 15) < 1e-9
assert abs(e2[3] - e2[2]) < 1e-9
debit2 = e2[1] + 5 * e2[2] + 23 * e2[3]

# Exact conditional resource inequality: D>=5(E2+E3), so if the high-grade
# fraction is >=epsilon at each event, each event multiplies native stock by
# at least 1+5 epsilon. Finite total stock then bounds the number of events.
assert debit2 + 1e-10 >= 5 * (e2[2] + e2[3])

out = {
    "status": "PASS",
    "joint_rotor": "Aj=(v1 v0^T-v0 v1^T)/12; v0^2=v1^2=24; Aj v0=2v1",
    "joint_pre_event_support_at_first_crossing": {"native": 1, "prepared_donor": 14, "residual_bank": 9, "total": 24},
    "post_first_native_support": 15,
    "post_first_residual_bank": 9,
    "post_initial_grade_stocks": start,
    "second_crossing_scan": {"range": [0, 3], "spacing": 3 / 1200, "bracket": brackets[0]},
    "second_crossing_internal_delay_numerical": t2,
    "second_crossing_internal_delay_exact": "atan(1/3)",
    "post_closed_sector_incidence_exact": "A u=-2w, A w=u/2; ||u||^2=24, ||w||^2=6",
    "second_crossing_grade_stocks_exact": ["0", "0", "15/2", "15/2"],
    "second_crossing_grade_stocks_numerical": e2,
    "second_crossing_debit_exact": 210,
    "second_crossing_debit_numerical": debit2,
    "second_crossing_shortfall_vs_residual_exact": 201,
    "second_hypothetical_native_output_support_exact": 225,
    "residual_bank_suffices_at_second_crossing": debit2 <= 9 + 1e-9,
    "fixed_total_stock": 24,
    "native_event_law_and_repeatable_donor_source": "OPEN",
    "physical_promotion": 0,
}
Path(__file__).with_name("results.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
