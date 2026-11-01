#!/usr/bin/env python3
"""UD tetrahedral quadrant atlas v0.8 — exact mathematical model checks.
No physical claims, no native dynamics. Requires sympy only.
"""
import json, itertools, math, hashlib
from fractions import Fraction
from pathlib import Path
import sympy as s

R=s.Rational
V=[s.Matrix(x) for x in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
O=s.zeros(3,1)
I=s.eye(3)
x,y,z=s.symbols('x y z',real=True)
X=s.Matrix([x,y,z])
checks=[]
def check(name, cond):
    if not bool(cond): raise AssertionError(name)
    checks.append(name)
def det3(a,b,c):return s.det(s.Matrix.hstack(a,b,c))
def simplex_volume(a,b,c,d):return abs(det3(b-a,c-a,d-a))/6

def energy(p, density):
    # Affine density integral over a tetrahedron
    vol=simplex_volume(*p)
    return s.factor(vol*sum(density(v) for v in p)/4)

def face_boundary(simplex):
    """oriented boundary of a simplex as signed formal chains"""
    out={}
    for k in range(len(simplex)):
        face=tuple(simplex[:k]+simplex[k+1:])
        coefficient=(-1)**k
        sorted_face=tuple(sorted(face))
        inv=sum(1 for a in range(len(face)) for b in range(a+1,len(face)) if face[a]>face[b])
        out[sorted_face]=out.get(sorted_face,0)+coefficient*(-1)**inv
    return {k:v for k,v in out.items() if v}

def accumulate(boundary, coeff, accum):
    for face,value in boundary.items():
        accum[face]=accum.get(face,0)+coeff*value
    return accum

check('four_vertex_center_exact',sum(V,O)==O)
check('regular_equal_norms', all(v.dot(v)==3 for v in V))
check('regular_opposite_inner_products', all(V[i].dot(V[j])==-1 for i in range(4) for j in range(i+1,4)))
check('tetrahedral_frame_4I',sum((v*v.T for v in V),s.zeros(3))==4*I)

lam=[s.factor((1+v.dot(X))/4) for v in V]
check('barycentric_sum_one',s.simplify(sum(lam)-1)==0)
check('global_barycentric_reconstruction',all(s.simplify((sum((lam[i]*V[i] for i in range(4)),s.zeros(3,1)) -X)[r])==0 for r in range(3)))

quadrants={}
for i in range(4):
    indices=[j for j in range(4) if j!=i]
    M=s.Matrix.hstack(*[V[j] for j in indices])
    ti=s.Matrix([s.factor(lam[j]-lam[i]) for j in indices])
    G=s.simplify(M.T*M)
    check(f'quadrant_{i}_basis_nonzero',abs(M.det())==4)
    check(f'quadrant_{i}_gram_exact',G==4*I-s.ones(3))
    check(f'quadrant_{i}_gram_inverse',G.inv()==(I+s.ones(3))/4)
    check(f'quadrant_{i}_jacobian',abs(M.det())==4)
    check(f'quadrant_{i}_dual_basis',all(s.simplify((M*ti-X)[r])==0 for r in range(3)))
    check(f'quadrant_{i}_positive_metric',all(v>0 for v in [G.det(),G[:1,:1].det(),G[:2,:2].det()]))
    check(f'quadrant_{i}_one_fourth_parent_volume',simplex_volume(O,*[V[j] for j in indices])==R(2,3))
    check(f'quadrant_{i}_facet_barycentric_bounds',s.simplify(sum(ti)-(1-4*lam[i]))==0)
    quadrants[i]={
      'basis_vertices':indices,
      'determinant':str(M.det()),
      'gram':[[str(G[a,b]) for b in range(3)] for a in range(3)],
      'parameter_rules':[str(v) for v in ti],
      'volume_finite':str(R(2,3)),
    }

parent=simplex_volume(*V)
check('parent_volume_8_over_3',parent==R(8,3))
check('four_child_tetrahedra_fill_parent_volume',sum((simplex_volume(O,*[V[j] for j in range(4) if j!=i]) for i in range(4)))==parent)

# Pair intersections are conical spans of exactly two complementary vertex rays.
for i,j in itertools.combinations(range(4),2):
    other=[k for k in range(4) if k not in (i,j)]
    for k in other:
        check(f'pair_{i}{j}_intersection_ray_{k}',s.simplify(lam[i].subs({x:V[k][0],y:V[k][1],z:V[k][2]})-lam[j].subs({x:V[k][0],y:V[k][1],z:V[k][2]}))==0)
    check(f'pair_{i}{j}_shared_face_independent',s.Matrix.hstack(*[V[k] for k in other]).rank()==2)

# A set of exact points verifies that the minimum-coordinate cone cover has no holes.
for abc in itertools.product([-2,-1,0,1,2],repeat=3):
    P=s.Matrix(abc)
    ls=[s.factor((1+v.dot(P))/4) for v in V]
    m=min(ls)
    covering=[i for i in range(4) if ls[i]==m]
    assert covering
    for i in covering:
        t=[ls[j]-ls[i] for j in range(4) if j!=i]
        assert all(q>=0 for q in t)
        recon=sum((t[k]*V[j] for k,j in enumerate([j for j in range(4) if j!=i])),s.zeros(3,1))
        assert recon==P
check('exact_125_point_quadrant_coverage', True)
check('all_four_charts_meet_at_origin',all(l.subs({x:0,y:0,z:0})==R(1,4) for l in lam))

# Each cone has exactly pi sr solid angle via exact symmetric trihedral formula.
# denom = 1 + a.b + b.c + c.a = 0; determinant strictly nonzero.
solid_angles=[]
for i in range(4):
    idx=[j for j in range(4) if j!=i]
    U=[V[j]/s.sqrt(3) for j in idx]
    denom=s.simplify(1+U[0].dot(U[1])+U[1].dot(U[2])+U[2].dot(U[0]))
    numerator=s.simplify(abs(s.det(s.Matrix.hstack(*U))))
    check(f'cone_{i}_solid_angle_denominator_zero',denom==0)
    check(f'cone_{i}_solid_angle_positive_numerator',numerator==4*s.sqrt(3)/9)
    omega=2*s.atan2(numerator,denom)
    check(f'cone_{i}_solid_angle_exact_pi',omega==s.pi)
    solid_angles.append(omega)
check('solid_angles_total_four_pi',sum(solid_angles)==4*s.pi)

# Chain boundary conservation for the four 3-simplex children and outer face.
outer=face_boundary([0,1,2,3])
child_chains=[((-1)**i,[4]+[j for j in range(4) if j!=i]) for i in range(4)]
acc={}
for coeff,tet in child_chains:
    accumulate(face_boundary(tet),coeff,acc)
acc={k:v for k,v in acc.items() if v}
check('oriented_child_boundaries_equal_original',acc==outer)
check('internal_triangles_cancel',all(4 not in f for f in acc))

# Exact positive test energy density, not a native UD energy law.
def rho(P):return 8+P[0]+2*P[1]+3*P[2]
check('test_energy_positive_all_parent_vertices',all(rho(v)>0 for v in V))
Etot=energy(V,rho)
Ei=[energy([O]+[V[j] for j in range(4) if j!=i],rho) for i in range(4)]
check('parent_energy_64_over_3',Etot==R(64,3))
check('child_energy_vector_exact',Ei==[R(13,3),6,R(17,3),R(16,3)])
check('energy_partition_conserved',sum(Ei)==Etot)
check('equal_volume_not_equal_energy',len(set(Ei))==4)

# Independent unit-circumradius frame factor and local coordinate pullback.
n=[v/s.sqrt(3) for v in V]
check('unit_frame_is_four_thirds',sum((w*w.T for w in n),s.zeros(3))==R(4,3)*I)
normalized_lam=[(1+3*w.dot(X))/4 for w in n]
J=s.Matrix(4,3,lambda a,b:s.diff(normalized_lam[a],X[b]))
check('unit_frame_barycentric_full_metric_pullback',s.simplify(J.T*J)==R(3,4)*I)
check('unit_frame_inverse_metric_full',s.simplify(R(4,3)*J.T*J)==I)

# General tetrahedra: centered vertex face cones still cover, volume shares are quarters.
W=[s.Matrix(c) for c in [(0,0,0),(2,0,0),(1,3,0),(0,1,4)]]
C=sum(W,s.zeros(3,1))/4
wc=[w-C for w in W]
AW=s.Matrix.hstack(*[W[j]-W[0] for j in range(1,4)])
muW=AW.inv()*(X-W[0])
lamW=[s.simplify(1-sum(muW))]+[s.simplify(u) for u in muW]
check('nonregular_barycentric_sum_one',s.simplify(sum(lamW)-1)==0)
for i in range(4):
    ix=[j for j in range(4) if j!=i]
    tw=[lamW[j]-lamW[i] for j in ix]
    rec=sum((tw[k]*wc[j] for k,j in enumerate(ix)),s.zeros(3,1))
    check(f'nonregular_cone_{i}_exact_inverse',all(s.simplify((rec-(X-C))[q])==0 for q in range(3)))
parent_w=simplex_volume(*W)
check('nonregular_parent_volume_4',parent_w==4)
for i in range(4):
  check(f'nonregular_{i}_one_quarter_volume',simplex_volume(C,*[W[j] for j in range(4) if j!=i])==parent_w/4)

# Critical no-go: four-way barycentric splitting is volume-contracting, but
# a nested branch retaining the same parent face is NOT diameter-contracting.
face_vertices=V[1:4]
face_center=sum(face_vertices,s.zeros(3,1))/3
parent_diameter_squared=max((V[i]-V[j]).dot(V[i]-V[j]) for i in range(4) for j in range(i+1,4))
check('regular_parent_diameter_squared_8',parent_diameter_squared==8)
for level in range(7):
    apex=face_center+R(1,4)**level*(V[0]-face_center)
    nested=[apex]+face_vertices
    check(f'nested_{level}_volume_quarter_power',simplex_volume(*nested)==parent/R(4**level))
    d2=max((nested[i]-nested[j]).dot(nested[i]-nested[j]) for i in range(4) for j in range(i+1,4))
    check(f'nested_{level}_diameter_noncontracting',d2==8)
# Inner interface counts of a 4-cell fan: 6 faces, 4 rays, 1 origin.
check('interface_combinatorial_count', (math.comb(4,2),math.comb(4,3),math.comb(4,4))==(6,4,1))

results={
 'artifact':'UD_TETRAHEDRAL_QUADRANTS_3D_COVERING_v0.8',
 'date':'2026-10-31', 'classification':'DEVELOPMENT_ONLY', 'physical_promotion':0,
 'exact_assertion_groups':len(checks),
 'scope':'Four regular-tetrahedral face cones, conical coordinates, positive-definite metrics, exact bounded 1-to-4 volumes, oriented boundaries, test energy and nonregular generalization.',
 'vertices':[[int(q) for q in v] for v in V],
 'parent_volume':str(parent), 'quadrants':quadrants,
 'quad_solid_angle_sr':'pi', 'four_quad_solid_angle_sr':'4*pi',
 'child_volumes':[str(R(2,3))]*4,
 'test_energy_density':'8+x+2*y+3*z',
 'parent_energy':str(Etot), 'child_energies':[str(e) for e in Ei],
 'internal_interfaces':{'two_sector_shared_faces':6,'three_sector_shared_rays':4,'four_sector_shared_origin':1},
 'fractal_counterexample':'Nested fixed-face barycentric children have volume V/4^n but constant diameter 2*sqrt(2)',
 'no_physical_claims':['Native Omega0 selected the fan','Metric energy is physical energy','Global 3D universe is one tetrahedron','Fractal growth follows from cone partition','4/3 geometry equals another typed 4/3 coefficient']
}
root=Path('/mnt/data')
(root/'UD_TETRAHEDRAL_QUADRANTS_RESULTS_v0.8.json').write_text(json.dumps(results,indent=2,sort_keys=True)+'\n',encoding='utf8')
print('PASS',len(checks),'exact assertion groups')
print('Quadrants:',len(quadrants),'solid angle each=pi, total=4*pi')
print('Volume:',parent,'children volumes',R(2,3),'times 4')
print('Energy:',Etot,'children:',Ei)
print('Gram (per quadrant):', quadrants[0]['gram'])
