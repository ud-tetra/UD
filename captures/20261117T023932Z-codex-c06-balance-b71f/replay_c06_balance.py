from fractions import Fraction as F

def check_stock(source, direct, flux_over_rate_squared):
    assert 0 <= source <= 1 and source + direct == 1
    b = direct - source
    assert b*b + flux_over_rate_squared == 1
    return b

assert check_stock(F(1), F(0), F(0)) == -1
assert check_stock(F(1,2), F(1,2), F(1)) == 0
assert check_stock(F(0), F(1), F(0)) == 1
even = F(1,4)
odd = F(3,4)
assert (even + odd)/2 == F(1,2)
assert check_stock(1-even, even, F(3,4)) == -F(1,2)
assert check_stock(1-odd, odd, F(3,4)) == F(1,2)
assert (F(1,2), odd) == (F(1,2), F(3,4))

# Use an exact bracket with sin(2δ)=3/5 and cos(2δ)=4/5.
epsilon, kappa, omega_min = F(1,5), F(1,2), F(1)
assert F(3,5) > epsilon and 2*omega_min*F(4,5)-kappa == F(11,10)
fractions = [(1+b)/2 for b in (-epsilon, epsilon)]
assert fractions == [F(2,5), F(3,5)]
assert 1/F(1,4) == 4 and 1/F(1,5) == 5
print('PASS_EXACT · stock-flux controls; bracket margins; 1/4 versus 3/4 sector counterexample; v0.7 audit witnesses')
