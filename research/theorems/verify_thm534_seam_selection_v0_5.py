#!/usr/bin/env python3
"""Exact finite tetrahedral seam-selection/rigidity tests, v0.5 (constructor)."""
from itertools import combinations, product
from collections import Counter
import sympy as sp
V=tuple(range(4))
E=list(combinations(V,2)); F=list(combinations(V,3))
B1=sp.zeros(4,6); B2=sp.zeros(6,4); B3=sp.zeros(4,1)
for j,(a,b) in enumerate(E): B1[a,j]=-1; B1[b,j]=1
for j,f in enumerate(F):
    for i in range(3):
        e=f[:i]+f[i+1:]; B2[E.index(e),j]=(-1)**i
for i in range(4): B3[i,0]=(-1)**i
assert B1*B2 == sp.zeros(4,4) and B2*B3 == sp.zeros(6,1)
assert B1.T*B1+B2*B2.T == 4*sp.eye(6)
slots=[(e,f) for e in range(6) for f in range(4) if B2[e,f]!=0]
assert len(slots)==12
states=Counter(); flat_masks=[]; full_masks=[]; best_pos=10**9
for bits in product((1,-1), repeat=len(slots)):
    N=B2.copy()
    for (e,f),phase in zip(slots,bits): N[e,f]=B2[e,f]*phase
    f12=B1*N; f23=N*B3
    energy=sum(int(a)**2 for a in f12)+sum(int(a)**2 for a in f23)
    b12=f12==sp.zeros(4,4); b23=f23==sp.zeros(6,1)
    states[(b12,b23)]+=1
    if b12: flat_masks.append(bits)
    if b12 and b23: full_masks.append(bits)
    if energy>0 and energy<best_pos: best_pos=energy
print('slot count',len(slots),'binary assignments',2**len(slots))
print('chain class count',dict(states),'min positive curvature/closure energy',best_pos)
assert states[(True,True)]==2 and states[(True,False)]==14
assert len(flat_masks)==16 and len(full_masks)==2
# Existing allowed signed face phases produce source-free B1N but not necessarily NB3.
for signs in product((1,-1),repeat=4):
    D=sp.diag(*signs)
    N=B2*D
    assert B1*N == sp.zeros(4,4)
    assert B1.T*B1 + N*N.T == 4*sp.eye(6)
    if N*B3 == sp.zeros(6,1): assert len(set(signs))==1

# Weighted lower/upper (no physical rate selection), edge-block amplitude conditional readout.
X=B1.T*B1; Y=B2*B2.T
px=X/4; py=Y/4
ca,cb=sp.symbols('ca cb', real=True)
R=ca*px+cb*py
assert all(sp.simplify(R[i,i]-(ca+cb)/2)==0 for i in range(6))
for i,e in enumerate(E):
    for j,f in enumerate(E):
        if not(set(e)&set(f)): assert R[i,j]==0
    norm=sp.expand(sum(R[j,i]**2 for j in range(6)))
    assert sp.simplify(norm-(ca**2+cb**2)/2)==0

# Single-entry phase defect, curvature cost and opposite edge all-time invariant.
z=sp.symbols('z')
ei=E.index((0,1)); fi=F.index((0,1,2))
N=B2.copy(); N[ei,fi]=z*B2[ei,fi]
F12=B1*N; F23=N*B3
assert sp.simplify(sum(x**2 for x in F12) - 2*(z-1)**2)==0
assert sp.simplify(sum(x**2 for x in F23) - (z-1)**2)==0
# even-power generator on (C0+C2) versus (C1+C3); only C1+C3 block matters
K=B1.T*B1+N*N.T
v=N*B3
H=sp.zeros(7); H[:6,:6]=K; H[:6,6]=-v; H[6,:6]=-v.T; H[6,6]=3
j_opp=next(i for i,f in enumerate(E) if not(set(E[ei])&set(f)))
assert j_opp!=ei
u=sp.zeros(7,1);u[ei,0]=1
for n in range(16):
    assert u[j_opp,0]==0
    u=H*u
# Benchmark spinor basis proof that twists at one incidence cannot mix opposite edge for any s.
print('SINGLE_DEFECT formal real-z costs=',sp.factor(sum(x**2 for x in F12)),'upper obstruction=',sp.factor(sum(x**2 for x in F23)))
print('PASS: exact Z2 exhaustive 4096, 16 lower-closed, 2 fully closed (global phases); min positive energy',best_pos)
print('PASS: face gauge phases maintain K=4I; weighted flat edge block has opposite amplitude 0')
print('PASS: single-entry covariant phase has no opposite-edge amplitudes in entire finite 15D power series')

# Separate complex U(1) check; squared norms conjugate correctly.
for zz in (sp.Integer(1),-sp.Integer(1),sp.I,-sp.I):
    Nz=B2.copy(); Nz[ei,fi]=zz*B2[ei,fi]
    f12z=B1*Nz; f23z=Nz*B3
    norm12=sp.simplify(sum(x*sp.conjugate(x) for x in f12z))
    norm23=sp.simplify(sum(x*sp.conjugate(x) for x in f23z))
    d=sp.simplify((zz-1)*sp.conjugate(zz-1))
    assert norm12==2*d and norm23==d
print("PASS: U(1) sample complex conjugate norms z={1,-1,i,-i}")

# Upper-chain breach: nonuniform face phases retain lower closure, K=4I, but 4th-order
# edge amplitudes are sourced by v = N B3, which is not a lawful simplicial boundary.
D=sp.diag(-1,1,1,1)
N=B2*D
assert B1*N==sp.zeros(4,4)
assert N*B3 != sp.zeros(6,1)
v=N*B3
assert sum(x*x for x in v)==12
# Define whole 15D skew-adjoint generator and compute even powers exactly.
A=sp.zeros(15)
for row,col,B in ((0,4,B1),(4,10,N),(10,14,B3)):
    A[row:row+B.rows,col:col+B.cols]=B
    A[col:col+B.cols,row:row+B.rows]=-B.T
assert A.T == -A
A2=A*A; A4=A2*A2
assert A2[4:10,4:10]==-4*sp.eye(6)
assert A4[4:10,4:10]==16*sp.eye(6)+v*v.T
assert any((v*v.T)[i,j]!=0 for i in range(6) for j in range(6) if i!=j)
print('PASS: flat-lower, broken-upper face phases produce first offdiagonal edge term at order s^4; ||NB3||^2=12')
