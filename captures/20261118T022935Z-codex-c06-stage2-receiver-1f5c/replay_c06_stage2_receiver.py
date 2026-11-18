"""Exact matching-action and Stage 2 stock controls."""
from fractions import Fraction as F
from itertools import combinations, product

edges = tuple(combinations(range(4), 2))
pairs = tuple((i, 5-i) for i in range(3))
group = ((0, 1, 2, 3), (1, 0, 3, 2), (2, 3, 0, 1), (3, 2, 1, 0))
signs = []
for perm in group:
    action = tuple(edges.index(tuple(sorted((perm[i], perm[j])))) for i, j in edges)
    assert all({action[i], action[j]} == {i, j} for i, j in pairs)
    signs.append(tuple(1 if action[i] == i else -1 for i, _ in pairs))
assert set(signs) == {(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)}
assert tuple(map(sum, zip(*signs))) == (0, 0, 0)


def norm(v):
    return sum(x*x for x in v)


rows = tuple(product((-1, 0, 1), repeat=3))
for w in rows:
    orbit = {tuple(a*b for a, b in zip(sign, w)) for sign in signs}
    population = sum(x != 0 for x in w)
    assert len(orbit) == (1 if population == 0 else 2 if population == 1 else 4)

count = 0
for a, b, w in product((-1, 0, 1), (-1, 0, 1), rows):
    p = (a, b, -a-b)
    e = tuple(p[i] for i in (0,1,2,2,1,0))
    odd = (*w, *(-x for x in reversed(w)))
    x0 = tuple(x+y for x, y in zip(e, odd))
    # squared endpoint norms, accounting for both normalizing sqrt(2) factors.
    retained = F(norm(odd), 2)
    direct = F(norm(x0), 2)
    z_stock = sum(F((x0[i]+x0[j])**2, 4) for i,j in pairs)
    assert z_stock == F(norm(e), 2)
    assert retained + direct + z_stock == norm(x0)
    assert direct + z_stock == norm(e) + F(norm(odd), 2)
    count += 1
assert count == 243
print("Four V4 action controls and 27 exact odd-orbit controls passed.")
print("243 exact Stage 2 endpoint stock and record checks passed.")
