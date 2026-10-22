#!/usr/bin/env python3
"""THM-534 oriented seam audit v0.4. Constructor replay; physical promotion 0."""
import itertools
import numpy as np
import sympy as s
from scipy.linalg import expm

vs=tuple(range(4))
E=list(itertools.combinations(vs,2))
F=list(itertools.combinations(vs,3))
B1=s.zeros(4,6)
for j,(a,b) in enumerate(E):
    B1[a,j]=-1; B1[b,j]=1
B2=s.zeros(6,4)
for j,face in enumerate(F):
    for i in range(3):
        B2[E.index(tuple(face[:i]+face[i+1:])),j]=(-1)**i
B3=s.zeros(4,1)
for i in range(4):
    B3[F.index(tuple(vs[:i]+vs[i+1:])),0]=(-1)**i
assert B1*B2 == s.zeros(4,4)
assert B2*B3 == s.zeros(6,1)
assert B1.T*B1+B2*B2.T == 4*s.eye(6)

def A_builder(b1,b2,b3):
    A=s.zeros(15)
    for ii,jj,b in [(0,4,b1),(4,10,b2),(10,14,b3)]:
        A[ii:ii+b.rows,jj:jj+b.cols]=b
        A[jj:jj+b.cols,ii:ii+b.rows]=-b.conjugate().T
    return A

A=A_builder(B1,B2,B3)
assert A.conjugate().T == -A
assert (A*A)[4:10,4:10] == -4*s.eye(6)
X,Y=B1.T*B1,B2*B2.T
assert X*Y == s.zeros(6) and Y*X == s.zeros(6)
assert X*X == 4*X and Y*Y == 4*Y
assert X.rank() == Y.rank() == 3
assert X/4+Y/4 == s.eye(6)
a,b=s.symbols('a b',nonnegative=True)
H=a*X+b*Y
lam=s.Symbol('lambda')
assert s.expand(H.charpoly().as_expr()-(lam-4*a)**3*(lam-4*b)**3)==0
assert H.subs({a:1,b:1}) == 4*s.eye(6)
assert H.subs({a:1,b:4}) != 4*s.eye(6)

# Flat degreewise U(1) unitary phases give exact gauge similarity.
G0=s.diag(1,-1,s.I,-s.I)
G1=s.diag(1,-1,s.I,-s.I,1,-1)
G2=s.diag(-1,1,s.I,-s.I)
G3=s.diag(s.I)
g1=G0*B1*G1.conjugate().T
g2=G1*B2*G2.conjugate().T
g3=G2*B3*G3.conjugate().T
GG=s.diag(*([G0[i,i] for i in range(4)]
           +[G1[i,i] for i in range(6)]
           +[G2[i,i] for i in range(4)]
           +[G3[0,0]]))
Ag=A_builder(g1,g2,g3)
assert g1*g2 == s.zeros(4,4) and g2*g3 == s.zeros(6,1)
assert s.simplify(Ag-GG*A*GG.conjugate().T) == s.zeros(15)
assert (Ag*Ag)[4:10,4:10] == -4*s.eye(6)

# One face-edge U(1) twist is separate covariant transport, not chain boundary.
ei=E.index((1,2)); fi=F.index((0,1,2))
assert B2[ei,fi] != 0
for z in (s.Integer(1),-s.Integer(1),s.I,-s.I):
    N=B2.copy(); N[ei,fi]*=z
    curvature=B1*N
    K=B1.T*B1+N*N.conjugate().T
    norm2=s.simplify(curvature.norm()**2)
    assert s.simplify(norm2-2*(z-1)*s.conjugate(z-1))==0
    assert s.expand(K.charpoly().as_expr()-(lam-4)**4*((lam-4)**2-norm2))==0
    if z!=1:
        assert curvature.rank()==1
        assert N*B3 != s.zeros(6,1)
    else:
        assert curvature == s.zeros(4,4)
# The 12 incidence positions have equal Z2 defect spectrum.
for f,face in enumerate(F):
    for e,edge in enumerate(E):
        if set(edge).issubset(face):
            N=B2.copy(); N[e,f]=-N[e,f]
            K=B1.T*B1+N*N.T
            assert s.expand(K.charpoly().as_expr()-(lam-4)**4*((lam-4)**2-8))==0
N=B2.copy();N[ei,fi]=-N[ei,fi]
Ad=A_builder(B1,N,B3)
assert Ad.T == -Ad
for t in (0.07,0.19):
    U=expm(t*np.array(Ad,dtype=float))
    assert np.max(np.abs(U.T@U-np.eye(15)))<1e-12
    edge=U[4:10,4:10]
    off=np.max(np.abs(edge-np.diag(np.diag(edge))))
    assert off>1e-5
    print(f'Z2 seam t={t:.2f}: max edge off-diagonal amplitude {off:.10f}')
print('PASS signed boundary/gauge-flat no-mixing, two Hodge sectors, U1 curvature spectrum, 12 Z2 locations')
print('OPEN original THM-534 hop source; no empirical probabilities or physical promotion')
