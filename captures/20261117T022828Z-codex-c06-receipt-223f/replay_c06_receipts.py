from fractions import Fraction as F
from itertools import permutations, product

bits = list(product((0, 1), repeat=3))
masks = list(product((0, 1), repeat=6))
witnesses = [(F(1,2), F(1), F(2)), (F(1,4),F(1),F(4)),
             (F(1,2),F(1,2),F(3,2)), (F(1,3),F(1,2),F(2))]

def gains(f, eta):
    even_record = f + (1-f)*eta
    even_retained = (1-f)*(1-eta)
    assert even_record+even_retained == f+(1-f) == 1
    return even_record, f

for f, eta, gain_ratio in witnesses:
    even, odd = gains(f, eta)
    assert even/odd == gain_ratio
    assert (even/2 == odd) == (eta == f/(1-f))

count = 0
for theta, permutation, flip, t in product(bits, permutations(range(3)), bits, masks):
    pre = tuple(theta[i] for i in permutation)
    post = tuple(a^b for a,b in zip(pre,flip))
    gates_before = tuple((1-pre[e//2])*t[e] for e in range(6))
    gates_after = tuple((1-post[e//2])*t[e] for e in range(6))
    assert all((a^b) == flip[e//2]*t[e]
               for e,(a,b) in enumerate(zip(gates_before,gates_after)))
    count += 1
assert count == 24576
print(f"PASS_EXACT · {count} binary/transport records; four rational gain witnesses; conserved stocks")
