"""Exact mask, star-sum and timestamp alias tests."""
from fractions import Fraction as F
from itertools import combinations, product

edges = tuple(combinations(range(4), 2))
faces = tuple(combinations(range(4), 3))
grid = tuple(product((-1, 0, 1), repeat=3))


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


even = (1, 1, -2, -2, 1, 1)
mask_count = 0
for mask in product((0, 1), repeat=6):
    y = tuple(a*b for a, b in zip(even, mask))
    mean = F(sum(y), 6)
    assert all(y[i]+y[5-i] == 2*mean for i in range(3)) == (not any(mask))
    mask_count += 1

star_count = 0
for w, (a, b) in product(grid, product((-1, 0, 1), repeat=2)):
    odd = (*w, *(-v for v in reversed(w)))
    even = (a,b,-a-b,-a-b,b,a)
    x = tuple(i+j for i, j in zip(odd, even))
    t = tuple(sum(v for edge, v in zip(edges, x) if i in edge) for i in range(4))
    assert sum(t) == 0
    for f in faces:
        p = tuple(t[i] for i in f)
        assert F(dot(p,p)+sum(p)**2, 2) == dot(odd,odd)
        assert tuple(F(t[i]+t[j], 2) for i,j in edges) == odd
        star_count += 1

stale_count = 0
for a,b in product(range(-3, 4), repeat=2):
    e = (0,0,0,-a-b,b,a)
    pe = tuple(F(e[i]-e[5-i], 2) for i in range(6))
    assert dot(pe,pe) == a*a+b*b+a*b <= a*a+b*b+abs(a*b)
    stale_count += 1

o0, o1 = (F(3,5),F(4,5)), (F(5,13),F(12,13))
e0 = (F(-32,65),F(9,65))
assert dot(o0,o0) == dot(o1,o1) == 1
assert o0[0] > o1[0] > 0 and o1[1] > o0[1] > 0
face = tuple(o+e for o,e in zip(o0,e0))
opposite = tuple(-o-e for o,e in zip(o1,e0))
recovered_odd = tuple((a-b)/2 for a,b in zip(face,opposite))
assert recovered_odd == (0,1) and dot(recovered_odd,recovered_odd) == 1
assert (o0[0]**2,o1[0]**2) == (F(9,25),F(25,169))
def multiply(x, y):
    return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])


h = (F(4,5), F(3,5))
histories = (((0,1),(F(1,3),0)), ((F(3,5),F(4,5)), (F(-4,15),F(3,15))))
early_late_residue = []
for o,e in histories:
    a = tuple(x+y for x,y in zip(o,e))
    assert a == (F(1,3),1)
    assert dot(o,o)==1 and dot(e,e)==F(1,9)
    later_o, later_e = multiply(h,o), multiply(tuple(-v for v in h),e)
    assert tuple(y-x for x,y in zip(later_o,later_e)) == tuple(-v for v in multiply(h,a))
    early_late_residue.append((o[0]**2,later_o[0]**2))
assert early_late_residue == [(0,F(9,25)),(F(9,25),0)]
print("Same-rate singular-receipt collision preserved both sector stock totals.")
print(f"{mask_count} exact mask controls; {star_count} star-recovery controls.")
print(f"{stale_count} stale-sample error checks; one stock-matched first-lobe false completion.")
