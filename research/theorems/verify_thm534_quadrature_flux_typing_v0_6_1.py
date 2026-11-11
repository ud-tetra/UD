#!/usr/bin/env python3
"""THM-534 v0.6.1 exact quadrature vs norm-current audit (SymPy)."""
import sympy as s
r=s.Integer(-1)
x=s.sqrt(2)/2
y=s.I*r*s.sqrt(2)/2
q=s.simplify(2*s.im(s.conjugate(x)*r*y))
flow=s.simplify(2*s.re(s.conjugate(x)*r*y))
assert q==1 and flow==0
yc=s.conjugate(y)
assert s.simplify(s.conjugate(y)*y-s.conjugate(yc)*yc)==0
assert s.simplify(2*s.im(s.conjugate(x)*r*yc))==-1
xr=s.sqrt(2)/2; yr=r*s.sqrt(2)/2
assert s.simplify(2*s.im(s.conjugate(xr)*r*yr))==0
assert s.simplify(2*s.re(s.conjugate(xr)*r*yr))==1
print("PASS: exact q_phase=1, equal-time J_norm=0")
print("PASS: conjugate input preserves magnitudes and reverses q_phase")
print("PASS: real input q_phase=0 but J_norm=1")
print("AMENDMENT: do not identify phase quadrature with conservation current or physical packet burden")
