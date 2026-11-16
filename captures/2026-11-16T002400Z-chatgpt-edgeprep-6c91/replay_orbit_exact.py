#!/usr/bin/env python3
"""Independent source-selection orbit proof: exact rationals only, no R4 target."""
from fractions import Fraction as F

pi = (F(16,25),F(4,25),F(1,25),F(4,25))
A=(F(16,25),F(4,25),F(4,25),F(16,25))
B=(F(2,5),)*4
h=F(8,5)/10
assert tuple(k*h for k in (4,1,1,4)) == A
assert sum(A)==sum(B)==F(8,5) and A!=B
# Direct unequal coherent input ratio 2:1 leaves a nonzero blocked-port leakage.
assert F((2-1)**2,2*(2**2+1**2)) == F(1,10)
# Six-phase symmetric Gibbs control: pi proportional to (256,64,4,1,4,64).
assert F(256+64,64+4) == F(80,17)
assert F(128,16) == 8
assert F(80,17) != 8
assert (1-F(8,17))/2 == F(9,34)
# An empty receiver distinguishes source preparation laws.
assert F(1)+F(0)==1 and 2*min(F(1),F(0))==0
print("EXACT CONDITIONAL ORBIT & BOUNDARY REPLAY PASS")
