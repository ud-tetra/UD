#!/usr/bin/env python3
"""Exact and symbolic consistency checks for UD March 2026 historical source audit.
No astrophysical data, fitted constants, empirical unit map, or GitHub mutation.
"""
import json
import sympy as s
from fractions import Fraction
from pathlib import Path

A, rho, r, n, x = s.symbols('A rho r n x', positive=True)
ns = 1 - A*rho**n
lambda_k = s.log(1/r)
running = s.simplify(s.diff(ns,n) / lambda_k)
# If 0<rho,r<1, ln rho <0 and ln(1/r)>0, so running>0.

# Cyclic link-coherence with fixed links: independent local phases do not preserve it.
before = [s.Integer(1),s.Integer(1),s.Integer(1)]
after = [s.Integer(1),-s.Integer(1),s.Integer(1)]
coherence=lambda a: a[0]*a[1]+a[1]*a[2]+a[2]*a[0]

# Linear event-count action is not asymptotic to a quadratic pointwise function.
eps=s.symbols('epsilon',positive=True)
ratio = s.simplify(eps/(eps**2/s.Integer(2)))

# Uniform smallness does not control derivatives.
r0=s.symbols('r0',positive=True)
f=r0**n*s.sin(x/r0**(2*n))
first=s.simplify(s.diff(f,x))
second=s.simplify(s.diff(f,x,2))

difference=Fraction('1.422')-Fraction('1.267')

assert coherence(before)==3
assert coherence(after)==-1
assert difference == Fraction(31,200)
assert s.simplify(running + A*rho**n*s.log(rho)/lambda_k)==0
assert s.simplify(first-r0**(-n)*s.cos(x/r0**(2*n)))==0
assert s.simplify(second + r0**(-3*n)*s.sin(x/r0**(2*n)))==0
assert ratio==2/eps

receipt={
  'artifact':'UD_MARCH_MATH_INDEPENDENT_CHECK_v0.1',
  'status':'EXACT_SYMBOLIC_CHECKS_PASS',
  'physical_promotion':0,
  'checks':[
   {'id':'GAP2_RUNNING_SIGN','expression':str(running),'assumptions':'A>0, 0<rho<1, 0<r<1, dn/dlnk=+1/ln(1/r)','conclusion':'running strictly positive'},
   {'id':'GAP4_LOCAL_PHASE_COHERENCE','baseline':str(coherence(before)),'transformed':str(coherence(after)),'assumptions':'three real unit amplitudes, fixed edge links, phase at middle vertex changed by pi','conclusion':'independent local phases not invariant'},
   {'id':'GAP3_ACTION_COST','linear_to_quadratic_ratio':str(ratio),'assumptions':'v=epsilon>0','conclusion':'ratio diverges as epsilon->0; no pointwise asymptotic equivalence'},
   {'id':'GAP1_DERIVATIVE_OBSTRUCTION','f':str(f),'df_dx':str(first),'d2f_dx2':str(second),'assumptions':'0<r0<1, n positive integer','conclusion':'sup-norm decays but derivative amplitudes grow'},
   {'id':'GAP5_DIFFERENCE','difference_exact':str(difference),'decimal':str(float(difference)),'conclusion':'IFS exceeds Poisson, inconsistent with historical negative/lower wording'}
  ]
}
Path('/mnt/data/UD_MARCH_MATH_CHECK_RECEIPT_v0.1.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
