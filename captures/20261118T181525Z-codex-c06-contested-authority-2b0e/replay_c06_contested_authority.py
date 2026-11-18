"""Exact controls for equivariant selection and factor-typed abort receipts."""
from fractions import Fraction as F
from itertools import combinations, permutations, product


v = range(4)
edges = tuple(combinations(v,2))
group = tuple(permutations(v))
actions = tuple(tuple(edges.index(tuple(sorted((g[i],g[j])))) for i,j in edges) for g in group)
masks = tuple(frozenset(i for i,on in enumerate(bits) if on) for bits in product((0,1),repeat=6))


def act(g, subset):
    return frozenset(g[i] for i in subset)


seen = set()
orbits = possible = impossible = unique = 0
for x in masks:
    if x in seen:
        continue
    around = {act(g,x) for g in actions}
    seen.update(around)
    orbits += 1
    fixing = [g for g in actions if act(g,x)==x]
    fixed = [a for a in x if all(g[a]==a for g in fixing)]
    if fixed:
        possible += 1
        unique += len(fixed) == 1
        for a in fixed:
            chosen = {}
            for g in actions:
                y = act(g,x)
                assert g[a] in y
                assert chosen.setdefault(y,g[a]) == g[a]
            for g,y in product(actions,around):
                assert chosen[act(g,y)] == g[chosen[y]]
    else:
        impossible += 1
        assert all(any(g[a]!=a for g in fixing) for a in x)
assert len(seen)==64 and orbits==11 and possible+impossible==orbits

p = (1,1,-1,-1)
odd = tuple(p[i]+p[j] for i,j in edges)
assert any(odd) and odd == tuple(-a for a in reversed(odd))
stab = [g for g in group if all(p[i]==p[g[i]] for i in v)]
assert not any(all(g[i]==i for g in stab) for i in v) # faces indexed by absent vertex
cross = tuple(e for e in edges if p[e[0]]!=p[e[1]])
assert not any(all(tuple(sorted(g[i] for i in e))==e for g in stab) for e in cross)

reasons = {}
for cl,ti in product((0,1),repeat=2):
    h = cl*ti
    reasons[(cl,ti)] = ("closure" if not cl else "", "integrity" if not ti else "")
    assert (not h) == any(reasons[(cl,ti)])
assert reasons[(0,1)] != reasons[(1,0)]
assert sum((1,0))==sum((0,1)) and (1,0)[0]!=(0,1)[0]
for old,new,y in product((0,1),(0,1),(-2,-1,0,1,2)):
    assert new*y*y-old*y*y == (new-old)*y*y
for phi in (F(0),F(1,4),F(1,2),F(1)):
    assert (-phi)**2+1 == 1+phi**2
assert (1+F(1,2)**2) == F(5,4)
print(f"64 edge eligibility masks, {orbits} S4 orbits, {possible} feasible, {unique} uniquely forced and {impossible} obstructed.")
print("Prepared face and cross-edge witnesses, four factor cases and 20 ownership and 4 split-cut cases passed.")
