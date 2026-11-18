"""Exact rational controls for the declared first-crossing dispatch model."""
from fractions import Fraction as F
from itertools import product


def guard(a, b):
    """Aligned normalized state (s,d)=(a,b) on an incoming positive-rate orbit."""
    return a*b == 0 and a*a < b*b


def dispatch(urgent, armed, resolved):
    if armed and resolved:
        return "cut"
    return "stall" if urgent else "advance"


phases = ((1,0),(F(3,5),F(4,5)),(0,1),(F(-3,5),F(4,5)),
          (0,-1),(1,0),(0,1))
assert all(a*a+b*b==1 for a,b in phases)
assert [guard(a,b) for a,b in phases] == [False,False,True,False,True,False,True]
assert phases[0][0]**2-phases[0][1]**2 == 1
assert phases[2][0]**2-phases[2][1]**2 == -1
assert phases[3][0]*phases[3][1] < 0
assert phases[2][1] == -phases[4][1]
assert phases[2] == phases[6]

# Logical table tests only the declared dispatch fixture, not a native scheduler.
table = ("advance","advance","advance","cut","stall","stall","stall","cut")
cases = 0
for flags, expected in zip(product((False,True), repeat=3),table):
    assert dispatch(*flags) == expected
    cases += 1

# Rescale phase so one unit equals pi/2. Constant rates attain every endpoint.
margins = 0
for p,g,d in product((F(0),F(1,4),F(1,2),F(3,4)),
                     (F(0),F(1,4),F(1,2),F(1)), (F(0),F(1,2),F(1),F(2))):
    end = p+g*d
    assert (g*d < 1-p) == (end < 1)
    assert (g*d == 1-p) == (end == 1)
    margins += 1

print(f"7 exact phase points, {cases} dispatch branches and {margins} preparation-margin controls passed.")
