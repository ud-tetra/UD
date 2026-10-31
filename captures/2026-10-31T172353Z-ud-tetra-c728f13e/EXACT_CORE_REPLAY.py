#!/usr/bin/env python3
# Source-bound exact checks only; not an empirical or 28-row validation.
from fractions import Fraction as F
x=F(1,2)*F(7,16)*F(1,6)
ns=F(185,192)
r=F(7,192)
inv_alpha=1/F(7,960)
s0=F(43,7); H=F(101,6); S=2*s0
assert x==r==F(7,192)
assert ns==F(185,192) and ns+r==1
assert inv_alpha==F(960,7)
assert S*H==F(4343,21)
assert S*H**2==F(438643,126)
assert float(r)>0.036
assert float(inv_alpha)>137.035999177
print("PASS: scoped exact internal arithmetic; original 22 rows missing, physical promotion 0")
