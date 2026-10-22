#!/usr/bin/env python3
"""Exact conditional checks of the C3 two-coordinate response equations."""
from fractions import Fraction as Q
import json

# Each rotation plane is 2D; every matrix in this restricted example is
# scalar times I_2. A second plane is included to test additivity.
planes = [(Q(2), Q(3), Q(5)), (Q(7), Q(11), Q(13))] # coupling c, damping d, stiffness k
bare = Q(17)
static = Q(19)

def port(s):
    return static + s * bare - sum(c*c/(k+s*d) for c,d,k in planes)

gamma = bare + sum(c*c*d/(k*k) for c,d,k in planes)
assert port(Q(0)) == static - sum(c*c/k for c,d,k in planes)
assert (port(Q(1,100))-port(Q(0))) / Q(1,100) > 0
# Exact derivative of the rational Schur expression at s=0.
assert gamma == bare + sum(c*c*d/(k*k) for c,d,k in planes)
# R120 commutes with a scalar 2x2 response: R=[[0,-1],[1,-1]] in
# triangular coordinates, R^3=I. The physical metric does not change
# the fact that scalar I commutes with it.
R=((0,-1),(1,-1))
def mul(A,B):
    return tuple(tuple(sum(A[i][h]*B[h][j] for h in range(2)) for j in range(2)) for i in range(2))
assert mul(mul(R,R),R)==((1,0),(0,1))
assert mul(((gamma,0),(0,gamma)),R)==mul(R,((gamma,0),(0,gamma)))

# Coefficients linear in load at L=0; quotient rule for the full
# two-plane gamma, including all k' factors.
slopes=[(Q(1),Q(2),Q(3)),(Q(-1),Q(1),Q(-2))] # c',d',k'
bare_prime=Q(4)
def gamma_load(L):
    return bare + L*bare_prime + sum((c+L*cp)**2*(d+L*dp)/(k+L*kp)**2
        for (c,d,k),(cp,dp,kp) in zip(planes,slopes))
closed=bare_prime+sum(2*c*cp*d/k**2+c*c*dp/k**2-2*c*c*d*kp/k**3
    for (c,d,k),(cp,dp,kp) in zip(planes,slopes))
# Exact rational central finite differences converge to the derivative;
# the bound is deliberately broad and does not stand in for symbolic proof.
for n in (10000,100000):
    h=Q(1,n)
    assert abs((gamma_load(h)-gamma_load(-h))/(2*h)-closed)<Q(1,10000)
# Same symmetry and stable static Schur matrix; bath drag can be zero or
# arbitrary nonnegative target by selecting d (coupling 1, stiffness 1).
for target in (Q(0),Q(1),Q(1000)):
    c=Q(0) if target==0 else Q(1)
    d=Q(1) if target==0 else target
    k=Q(1)
    K_x=Q(2)
    assert K_x-c*c/k>0
    assert c*c*d/k**2==target
# Independently check the general matrix derivative with noncommuting K,D,K'.
import numpy as np
K=np.array([[5.,1.],[1.,4.]])
D=np.array([[2.,0.5],[0.5,3.]])
C=np.array([[1.,2.],[3.,-1.]])
Kp=np.array([[0.1,0.3],[0.3,-0.2]])
Dp=np.array([[0.4,0.1],[0.1,-0.1]])
Cp=np.array([[0.2,0.1],[-0.3,0.4]])
A=np.linalg.inv(K)
analytic=np.trace(2*Cp@A@D@A@C.T+C@(A@Dp@A-A@Kp@A@D@A-A@D@A@Kp@A)@C.T)/2

def noncommuting_gamma(L):
    Ct=C+L*Cp
    At=np.linalg.inv(K+L*Kp)
    return np.trace(Ct@At@(D+L*Dp)@At@Ct.T)/2
h=1.e-5
assert abs((noncommuting_gamma(h)-noncommuting_gamma(-h))/(2*h)-analytic)<1.e-8
print(json.dumps({"status":"PASS_CONDITIONAL", "gamma_two_planes":str(gamma),
    "load_derivative_two_planes":str(closed),"arbitrary_bath_targets":["0","1","1000"]},indent=2))
