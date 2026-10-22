#!/usr/bin/env python3
"""Exact conditional checks: seven-coset filtering, shell/basis and load identity."""
from fractions import Fraction as F
import json
from math import sqrt

R=((F(8,7),F(3,7)),(F(-3,7),F(5,7)))
def Rt(h):
    return (R[0][0]*h[0]+R[1][0]*h[1], R[0][1]*h[0]+R[1][1]*h[1])
def norm(h):return h[0]**2-h[0]*h[1]+h[1]**2
def allowed(h):return all(x.denominator==1 for x in Rt(h))
H=[(i,j) for i in range(-5,6) for j in range(-5,6) if (i,j)!=(0,0)]
assert all(allowed(h)==((h[0]-3*h[1])%7==0) for h in H)
first=[h for h in H if norm(h)==1]
assert len(first)==6 and not any(allowed(h) for h in first)
low=min(norm(h) for h in H if allowed(h))
assert low==7
survivors={h for h in H if allowed(h) and norm(h)==7}
triplet=((3,1),(-1,2),(-2,-3))
assert len(survivors)==6 and survivors==set(triplet)|{(-x,-y) for x,y in triplet}
assert tuple(map(sum,zip(*triplet)))==(0,0)
assert abs(sqrt(low)-sqrt(7))<1e-15
# The seven top coset characters have exponent k*(8 h1 - 3 h2)/7.
# Their formal sum is 7 for divisible exponents, zero otherwise.
assert all(((8*h[0]-3*h[1])%7==0)==allowed(h) for h in H)
# Use Z[omega], omega^2+omega+1=0, to check basis phases.
# For each positive triplet, both factors are 1+omega^2=-omega,
# so their product is omega^2 and has modulus one.
for h in triplet:
    hp=Rt(h)
    assert (sum(h)%3,sum(hp)%3)==(1,2)
    t0=(F(1,21),F(4,21))
    assert (h[0]*t0[0]+h[1]*t0[1])%1==F(1,3)
# Critical values of S=cos(a)+cos(b)+cos(a+b): min=-3/2,
# max=3, as follows from S=2u*v+2u^2-1, |u|,|v|<=1.
Smin=F(2)*F(1,2)**2-F(2)*F(1,2)-1
Smax=F(3)
assert (Smin,Smax)==(F(-3,2),F(3))
assert 2*(Smax-Smin)==9
# Exactly solvable vertical model, z_f= zref-(L+f*b)/k.
k=F(20); a=F(10); b=F(1); zref=F(2); L=F(1)
def z(f,L): return zref-(L+f*b)/k
def enthalpy(f,L):return f*(a+b*zref)+L*zref-(L+f*b)**2/(2*k)
barrier=lambda load:enthalpy(F(6),load)-enthalpy(F(-3),load)
assert (barrier(L+F(1,7))-barrier(L))/F(1,7)==z(F(6),L)-z(F(-3),L)==-F(9,20)
assert barrier(L)>0
print(json.dumps({'status':'PASS_CONDITIONAL','first_allowed_squared_reciprocal_ratio':7,
  'surviving_shell':list(map(list,triplet)), 'basis_product':'omega^2; modulus 1',
  'first_shell_barrier_multiplier':9,'exact_example_barrier_load_slope':'-9/20',
  'exact_example_registry_height_difference':'-9/20'},indent=2))
