"""Exact rational checks for the graphite harmonic-port curvature formulas."""
from fractions import Fraction as F
import json


def inner(v, w, metric):
    return sum(v[i] * metric[i][j] * w[j] for i in range(2) for j in range(2))


def outer_sum(vectors):
    return [[sum(v[i] * v[j] for v in vectors) for j in range(2)] for i in range(2)]

G = [[F(1), F(1, 2)], [F(1, 2), F(1)]]
Ginv = [[F(4, 3), F(-2, 3)], [F(-2, 3), F(4, 3)]]
assert [[sum(G[i][k] * Ginv[k][j] for k in range(2)) for j in range(2)]
        for i in range(2)] == [[1, 0], [0, 1]]

bonds = [(F(1, 3), F(1, 3)), (F(-2, 3), F(1, 3)), (F(1, 3), F(-2, 3))]
assert sum(inner(d, d, G) for d in bonds) == 1
covectors = [tuple(sum(d[i] * G[i][j] for i in range(2)) for j in range(2))
             for d in bonds * 7]
MtM = outer_sum(covectors)
assert MtM == [[F(7, 2) * x for x in row] for row in G]
ItI = [[x / 2 for x in row] for row in MtM]
assert ItI == [[F(7, 4) * x for x in row] for row in G]

# The reciprocal phase covectors are a 120-degree star under G inverse.
star = [(F(1), F(0)), (F(0), F(1)), (F(1), F(1))]
g2 = inner(star[0], star[0], Ginv)
assert g2 == F(4, 3)
assert all(inner(h, h, Ginv) == g2 for h in star)
assert inner(star[0], star[1], Ginv) == -g2 / 2
Sstar = outer_sum(star)
assert Sstar == [[F(3, 2) * g2 * x for x in row] for row in G]

# U=2 V S: at the two possible stable registries cos_j=-1/2 or +1.
beta = {"positive": F(3, 2), "negative": F(3)}
assert Sstar == [[beta["positive"] * g2 * x for x in row] for row in G]
assert [[2 * x for x in row] for row in Sstar] == [
    [beta["negative"] * g2 * x for x in row] for row in G]
assert F(4, 7) * beta["positive"] == F(6, 7)
assert F(4, 7) * beta["negative"] == F(12, 7)
barrier = {"positive": F(1), "negative": F(8)}
ratio = {key: beta[key] / barrier[key] for key in beta}
assert ratio == {"positive": F(3, 2), "negative": F(3, 8)}

# Check signs of implicit-load chain rule using admissible polynomial jets.
for Sm, V, Vprime, Vsecond, E0second in [
    (F(-3, 2), F(2), F(-3), F(1), F(10)),
    (F(3), F(-2), F(3), F(-1), F(10)),
]:
    Kz = E0second + 2 * Sm * Vsecond
    assert Kz > 0
    sign = 1 if V > 0 else -1
    dz_dL = -F(1) / Kz
    dabsV_dL = sign * Vprime * dz_dL
    assert dabsV_dL == -sign * Vprime / Kz
    assert dabsV_dL / abs(V) == -Vprime / (V * Kz)

print(json.dumps({
    "exact_checks": ["Gram inverse", "bond Gram", "relative lift",
                     "reciprocal star", "branch Hessians", "barrier ratios",
                     "two load derivative signs"],
    "relative_gram": "7/4 G",
    "kx_over_absV_gstar_squared": {"positive": "3/2", "negative": "3"},
    "kx_over_barrier_gstar_squared": {k: str(v) for k, v in ratio.items()},
    "status": "EXACT_CONDITIONAL_CONSTRUCTOR_CHECK"
}, indent=2))
