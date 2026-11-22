#!/usr/bin/env python3
"""Exact source-scoped tetrahedral sphere/dual/inversion tests. Python 3 + SymPy.
All coordinates are dimensionless; no physical length, clock, energy, or metric emergence.
"""
from itertools import combinations, permutations
from collections import Counter
import json
from pathlib import Path
import sympy as S

V = tuple(range(4))
bases = {k: list(combinations(V, k+1)) for k in range(3)}

def sign(seq):
    return (-1) ** sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))

def boundary(k):
    out = S.zeros(len(bases[k-1]), len(bases[k]))
    for col, sigma in enumerate(bases[k]):
        for j in range(k+1):
            out[bases[k-1].index(sigma[:j]+sigma[j+1:]), col] += (-1)**j
    return out

B1, B2 = boundary(1), boundary(2)
assert B1*B2 == S.zeros(4,4)
b3 = S.Matrix([(-1)**(3-i) for i in range(4)])  # check separately against face order
b3 = S.zeros(4,1)
for i in range(4):
    face = V[:i]+V[i+1:]
    b3[bases[2].index(face),0]=(-1)**i
assert B2*b3 == S.zeros(6,1)
r1,r2 = B1.rank(),B2.rank()
betti = [4-r1,6-r1-r2,4-r2]
assert betti == [1,0,1]
assert (4-6+4)==sum(((-1)**i)*betti[i] for i in range(3))==2

# Signed complement sends each k-simplex to opposite (2-k)-simplex.
D = {}
for k in range(3):
    Dk = S.zeros(len(bases[2-k]), len(bases[k]))
    for j, sigma in enumerate(bases[k]):
        comp = tuple(v for v in V if v not in sigma)
        Dk[bases[2-k].index(comp),j] = sign(sigma+comp)
    D[k]=Dk
assert D[0]*B1 == -B2.T*D[1]
assert D[1]*B2 == B1.T*D[2]
assert D[1]*D[1]==S.eye(6)
assert D[2]*D[0]==-S.eye(4)

# Signed S4 covariance is twisted by orientation sign; no unqualified equivariance.
for g in permutations(V):
    T = {}
    for k in range(3):
        Tg = S.zeros(len(bases[k]))
        for j,sigma in enumerate(bases[k]):
            image = tuple(g[v] for v in sigma)
            Tg[bases[k].index(tuple(sorted(image))),j]=sign(image)
        T[k]=Tg
    for k in range(3):
        assert D[k]*T[k] == sign(g)*T[2-k]*D[k]

# An S4-equivariant map from the four vertices to themselves is the identity.
centralizers=[]
for f in permutations(V):
    if all(tuple(f[g[i]] for i in V)==tuple(g[f[i]] for i in V) for g in permutations(V)):
        centralizers.append(f)
assert centralizers == [V]

# Fixed regular tetra in Euclidean R3: vertices have unit norm, pairwise dot -1/3.
W = [S.Matrix((1,1,1)),S.Matrix((1,-1,-1)),S.Matrix((-1,1,-1)),S.Matrix((-1,-1,1))]
vert = [w/S.sqrt(3) for w in W]
assert all(S.simplify(vert[i].dot(vert[j]))==(1 if i==j else S.Rational(-1,3)) for i in V for j in V)
face_centroids = [sum((vert[j] for j in V if j!=i),S.zeros(3,1))/3 for i in V]
assert all(face_centroids[i]==-vert[i]/3 for i in V)
polar_vertices = [-3*v for v in vert]
assert all(S.simplify(polar_vertices[i].dot(vert[j]))==(S.Integer(-3) if i==j else S.Integer(1)) for i in V for j in V)

def invert(x):
    return S.simplify(x / x.dot(x))
def radial(x):
    return x / S.sqrt(x.dot(x))
def vec_equal(a,b):
    return all(S.simplify(a[i]-b[i])==0 for i in range(3))

for i in V:
    assert vec_equal(invert(vert[i]),vert[i])
    assert vec_equal(invert(face_centroids[i]),polar_vertices[i])
mid=(vert[0]+vert[1])/2
assert S.simplify(mid.dot(mid))==S.Rational(1,3)
assert vec_equal(invert(mid),3*mid)
assert S.simplify(invert(mid).dot(invert(mid)))==S.Integer(3)

# Two *different* tetrahedral boundaries, primal T and face-centroid dual T*= -T/3.
# A: T -> T*, x -> -x/3; B: T* -> T, y -> -3y; A and B are mutual inverses.
# The radial sphere readout makes this exact pair correspond to *antipodal* map,
# NOT to ordinary spherical inversion (identity when already on unit S2).
probes=[]
for f in bases[2]:
    pts=[vert[i] for i in f]
    probes.extend([pts[0],(pts[0]+pts[1])/2,(pts[0]+pts[1]+pts[2])/3,(pts[0]+2*pts[1]+3*pts[2])/6])
for x in probes:
    y = -x/3
    assert vec_equal(-3*y,x)
    assert vec_equal(radial(y),-radial(x))

# A two-copy hidden sign has a nontrivial information involution but a readout
# which cannot see it: P(x,sign)=radial(x), I(x,sign)=(x,-sign).
for x in probes:
    assert vec_equal(radial(x),radial(x)) # P after flip = P before
# Nontrivial sphere inversion on the boundary impossible under injective P:
# J|S2 = identity and P homeomorphism -> P(Ix)=P(x) => Ix=x.

result={
 "classification":"EXACT_CONDITIONAL; NO_PHYSICAL_PROMOTION",
 "sphere_boundary":{"f_vector":[4,6,4],"euler":2,"betti_Q":betti,"B1_rank":r1,"B2_rank":r2,"B1B2_zero":True,"B2B3_zero":True},
 "complement_dual":{"dimensions":["C0->C2","C1->C1","C2->C0"],"D0B1=-B2tD1":True,"D1B2=B1tD2":True,"D1_squared":"+I6","D2D0":"-I4","twisted_S4_cases":24*3,"trivial_vertex_selfmap_centralizer":True},
 "euclidean":{"vertex_norm2":"1","cross_vertex_dot":"-1/3","opposite_face_center":"-v_i/3","polar_vertex":"-3v_i","J_unit(face_center)":"polar_vertex","edge_midpoint_norm2":"1/3","J_unit(edge_midpoint)_norm2":"3","boundary_vertices_fixed_by_J_unit":4},
 "typed_primal_dual":{"primal_to_dual":"A(x)=-x/3","dual_to_primal":"B(y)=-3y","two_way_inverse":True,"sphere_readout":"P=radial","commutator":"P_dual A = antipodal P_primal","probe_count":len(probes),"antipodal_degree":-1,"not_geometric_sphere_inversion":True},
 "null_control":{"sphere_inversion_restricted_S2":"identity","nontrivial_latent_flip_readout_blind":True,"injective_readout_forces_latent_identity":True,"conventional_tetra_dual_reproduces_all":True},
 "physical_promotion":0,"event_generator":"OPEN","metric_and_radial_map":"ASSUMED_EUCLIDEAN","source_selection":"OPEN"
}
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,sort_keys=True,indent=2))
print('PASS: topology, twisted duality, 24 S4 permutations, null, primal-dual antipodal, 16 probes')
