"""Exact controls for the common-state capture-and-cut candidate."""
from fractions import Fraction as F
from itertools import product


def dot(x, y):
    return sum(a*b for a,b in zip(x,y))


def norm(x):
    return dot(x,x)


def readback(p, q):
    return F(dot(p,q)+sum(p)*sum(q), 2)


points = tuple(product((-1,0,1), repeat=3))
for p,q in product(points, repeat=2):
    s,d = (*p,-sum(p)), (*q,-sum(q))
    assert readback(p,q) == F(dot(s,d),2)
    stock_s, stock_d, corr = readback(p,p), readback(q,q), readback(p,q)
    assert stock_s*stock_d >= corr*corr
    if corr == 0 and stock_s < stock_d and stock_s*stock_d == 0:
        assert stock_s == 0 < stock_d


rotations = ((1,0),(F(3,5),F(4,5)),(F(5,13),F(12,13)),(0,1),(-1,0))
roots = (((0,0,0),(1,0,0)), ((1,0,0),(0,2,0)), ((0,1,0),(2,0,2)))
for (s0,d0),(a,b) in product(roots, rotations):
    stock = norm(s0)+norm(d0)
    r0 = F(norm(s0),stock)
    s = tuple(a*x-b*y for x,y in zip(s0,d0))
    d = tuple(b*x+a*y for x,y in zip(s0,d0))
    r = F(norm(s),stock)
    assert norm(s)+norm(d)==stock
    assert r==r0+(1-2*r0)*b*b
    assert F(norm(d),2)==stock*(1-r)/2


def can_cut(capture, current, armed):
    """Tokens below identify immutable model states; epoch is deliberately absent."""
    return armed and capture == current


before, after = "resolved-root", "advanced-amplitudes"
old_mode = "armed"
assert can_cut(before,before,old_mode=="armed")
assert not can_cut(before,after,old_mode=="armed")
assert not can_cut(before,before,False)
# Positive odd cosine and negative even cosine do not imply reciprocal phases.
ho, he = (F(3,5),F(4,5)), (F(-5,13),F(12,13))
assert ho[0]*he[0]<0 and any(a+b for a,b in zip(ho,he))
print("729 common-state Gram controls and 15 exact delayed-cut cases passed.")
print("Fresh, stale and disarmed receipt controls; opposite-cosine nonsingularity passed.")
