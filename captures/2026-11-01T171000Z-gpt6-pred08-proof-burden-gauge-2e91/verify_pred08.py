#!/usr/bin/env python3
"""Exact symbolic corroboration of assumption-scoped PRED08 theorems.
Not an independent reviewer or a physical test. Uses SymPy 1.14.0.
"""
import json
from itertools import permutations
from fractions import Fraction
from pathlib import Path
import sympy as sp

B=sp.Matrix([[1,1,1,0,0,0],[-1,0,0,1,1,0],[0,-1,0,-1,0,1],[0,0,-1,0,-1,-1]])
# B may have all edges oriented consistently or arbitrarily; signs do not change L.
L=B*B.T
I=sp.eye(4); ONE=sp.ones(4,1)
assert L==4*I-ONE*ONE.T
x=sp.symbols('b0:4', nonnegative=True)
M=sp.symbols('M',positive=True); gamma=sp.symbols('gamma',positive=True)
b=sp.Matrix(x)
Q=sum(y*y for y in b)
s=sp.Matrix([gamma*y*(y-Q/M) for y in b])
# Restrict to the mass shell before simplifying.
subsM={M:sum(b)}
assert sp.factor(sum(s).subs(subsM))==0
assert all(sp.factor((s[i]-s[j]).subs(subsM)-gamma*(b[i]-b[j])*(b[i]+b[j]-Q/sum(b)))==0 for i in range(4) for j in range(4))
A=sum(v**3 for v in b)-Q**2/M
assert sp.factor((b.T*s)[0]-gamma*A)==0
# Reservoir contribution and diffusion are distinct in exact ring.
u=sp.symbols('u',nonnegative=True)
V=sp.Rational(1,2)*sum((y-M/4)**2 for y in b)
flow=-L*b/sp.Integer(4)+u*s
Vdot=sp.expand(sum(sp.diff(V,b[i])*flow[i] for i in range(4))).subs(subsM)
Ddot=(b.T*L*b)[0]/4
assert sp.factor(Vdot+Ddot-u*gamma*A.subs(subsM))==0
assert sp.factor(sum(flow).subs(subsM))==0
# Differential linearization on the mass constraint.
center=sp.Matrix([M/4]*4)
J=flow.jacobian(b)
J0=J.subs({b[i]:M/4 for i in range(4)})
for v in [sp.Matrix([1,-1,0,0]),sp.Matrix([0,1,-1,0]),sp.Matrix([0,0,1,-1])]:
    assert sp.simplify(J0*v-(-1+u*gamma*M/4)*v)==sp.zeros(4,1)
# S4 covariance of burden current and conservative source, symbolic on mass shell.
for p in permutations(range(4)):
    pb=sp.Matrix([b[i] for i in p])
    ps=sp.Matrix([s[i] for i in p])
    spb=sp.Matrix([gamma*y*(y-Q/M) for y in pb])
    assert sp.simplify(ps-spb)==sp.zeros(4,1)
# Uniform stochastic seed with exact rational mass and reserve.
eps=sp.Rational(1,10); M0=sp.Integer(4); mean=M0/4
post=sp.Matrix([mean+eps, mean-eps,mean,mean])
assert sum(post)==M0
assert sp.Rational(1,2)*sum((v-mean)**2 for v in post)==eps**2
assert post[0]>post[2]>post[1]
assert (post[0]-post[1])/4==sp.Rational(1,20)
assert (post[0]-post[2])/4==sp.Rational(1,40)
# Exact closed triangle flat integer cochain lifts (1,0,0) and zero have same compact U.
z=sp.Matrix([1,0,0]); a=sp.Matrix([0,0,0]); cycle=sp.ones(3,1)
assert (z.T*cycle)[0]==1
assert [sp.exp(2*sp.pi*sp.I*v).simplify() for v in z]==[1,1,1]
tau=sp.symbols('tau',positive=True)
S=lambda n: tau*n*n/2
assert sp.simplify(S(3)-S(2)-sp.Rational(5,2)*tau)==0
# Exact updates are annihilated by cycle boundary.
Bcycle=sp.Matrix([[-1,0,1],[1,-1,0],[0,1,-1]])
assert (Bcycle*cycle)==sp.zeros(3,1)
ks=sp.Matrix(sp.symbols('k0:3'))
assert (cycle.T*Bcycle.T*ks)[0]==0
# Simultaneous large-lift shifts preserve relative period, but separate lifts do not.
n,r,k=sp.symbols('n r k',integer=True)
assert sp.simplify(((n+k)-(r+k))-(n-r))==0
assert sp.simplify(S(n+1)-S(n))!=0
out={
  'scope':'EXACT_CONDITIONAL, no physical promotion',
  'sympy':sp.__version__,
  'K4_laplacian':[[int(v) for v in L.row(i)] for i in range(4)],
  'variance_identity':'Vdot=-1/4 sum_edges (delta b)^2 + u*gamma*(sum b_i^3-Q^2/M)',
  'reservoir_ledger':'V+R+D conserved; Rdot=-u gamma A; Ddot=1/4 sum_edges (delta b)^2',
  'linear_contrast_eigenvalue':'-1+u(R0)*gamma*M/4',
  'stochastic_seed':{'M':4,'epsilon':'1/10','delta_V':'1/100','selected_outgoing_current':'1/20'},
  'compact_link_counterexample':'a=(0,0,0) and a+z=(1,0,0) give identical U=(1,1,1) but periods 0 and 1',
  'large_lift_relative_period':'(n+k)-(r+k)=n-r',
  'review':'CONSTRUCTOR_ONLY_AND_INDEPENDENT_METHOD',
  'physical_promotion':0
}
p=Path(__file__).with_name('EXACT_AUDIT.json');p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
