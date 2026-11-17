from fractions import Fraction as F
from itertools import product

HALF = F(1,2)

def stocks_after_wait(order, initial):
    source = list(initial)
    record = [F(0),F(0)]
    held = {i for i in range(2) if initial[i] == 0}
    for event in order:
        if event in held:
            continue
        before = [(source[k],record[k]) for k in held]
        source[event] = initial[event]*HALF
        record[event] = initial[event]*HALF
        assert before == [(source[k],record[k]) for k in held]
        held.add(event)
    assert held == {0,1}
    assert all(a+b==c for a,b,c in zip(source,record,initial))
    return source, record

for order, initial in product(((0,1),(1,0)),
                              ((F(3),F(5)),(F(0),F(5)),(F(3),F(0)),(F(0),F(0)))):
    source,record=stocks_after_wait(order,initial)
    final=(source[0]+record[0],record[1])
    assert final==(initial[0],initial[1]*HALF)
assert stocks_after_wait((0,1),(F(3),F(5))) == stocks_after_wait((1,0),(F(3),F(5)))
assert F(4,3) < F(106,9)
assert F(4,3)/F(106,9)==F(6,53)

epsilon_e,epsilon_t=F(1,10),F(1,5)
for e,t,eta in product((-epsilon_e,0,epsilon_e),(-epsilon_t,0,epsilon_t),(F(0),F(3,4),F(1))):
    f_e,f_t=(1+e)/2,(1+t)/2
    w_e=(1-(1-f_e)*(1-eta))/2
    assert abs(w_e-f_t)<=epsilon_t/2+(1+epsilon_e)*(1-eta)/4
    if eta==1:
        assert w_e==HALF
print('PASS_EXACT · both latch orders, zero-stock controls, conservation and 27 error-envelope controls')
