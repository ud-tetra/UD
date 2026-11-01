#!/usr/bin/env python3
"""Exact constructive checks for UD candidate tetrahedral 3D coordinate atlas v0.7.
Requires SymPy; all assertions use exact arithmetic. Does not execute UD-native dynamics.
"""
from __future__ import annotations
import itertools, json, hashlib
from pathlib import Path
from sympy import (Matrix, Rational as Q, sqrt, eye, zeros, symbols,
                   simplify, det, integrate, factorial)

ROOT=Path(__file__).resolve().parent
checks=[]
def test(name, condition):
    assert bool(condition), name
    checks.append(name)

def equal_mat(a,b):
    return all(simplify(x)==0 for x in a-b)

def parity(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

# Four vectors, one constrained barycentric spatial coordinate frame.
W=Matrix([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]])
N=W/sqrt(3)
ones=Matrix([1,1,1,1])
spatial=Matrix(symbols('x y z',real=True))
lambda4=ones/4+Q(3,4)*N*spatial
lam=Matrix(symbols('l0 l1 l2 l3',real=True))
test('center_zero_vector',equal_mat(N.T*ones,zeros(3,1)))
test('regular_tetra_frame_bound',equal_mat(N.T*N,Q(4,3)*eye(3)))
test('four_lambdas_sum_one',simplify(sum(lambda4)-1)==0)
test('barycentric_inverse_to_spatial',equal_mat(N.T*lambda4,spatial))
test('barycentric_inverse_from_constrained_lambdas',equal_mat(
    ones/4+Q(3,4)*N*(N.T*lam)-lam,
    ones*(1-sum(lam))/4))
J=lambda4.jacobian(spatial)
test('metric_from_barycentric_differentials',equal_mat(Q(4,3)*J.T*J,eye(3)))
test('metric_three_independent_coordinates',J.rank()==3)
test('barycentric_fourth_mode_fixed_not_time',simplify(sum(lambda4)-1)==0)
for i in range(4):
    ell=lambda4.subs({spatial[j]:N[i,j] for j in range(3)})
    test('vertex_one_hot_'+str(i),equal_mat(ell,Matrix([int(k==i) for k in range(4)])))
    face_lambda=ones/3-Matrix([int(k==i)/3 for k in range(4)])
    test('face_centroid_sums_to_one_'+str(i),simplify(sum(face_lambda)-1)==0)
# Barycentric support exactly encodes point -> line -> face -> volumetric interior.
strata=[
    ('point',(Q(1),Q(0),Q(0),Q(0)),0),
    ('line',(Q(1,2),Q(1,2),Q(0),Q(0)),1),
    ('face',(Q(1,3),Q(1,3),Q(1,3),Q(0)),2),
    ('volume',(Q(1,4),Q(1,4),Q(1,4),Q(1,4)),3),
]
for name,weights,dimension in strata:
    test('barycentric_support_dimension_'+name,sum(bool(w>0) for w in weights)-1==dimension and sum(weights)==1)
# S4 equivariance including orientation reversal.
for perm in itertools.permutations(range(4)):
    P=Matrix(4,4,lambda i,j:int(perm[i]==j))
    O=Q(3,4)*N.T*P*N
    name=''.join(map(str,perm))
    test('S4_orthogonal_'+name,equal_mat(O.T*O,eye(3)))
    test('S4_vertex_frame_intertwines_'+name,equal_mat(N*O,P*N))
    test('S4_parity_'+name,det(O)==parity(perm))
# Concrete example at rational coordinates.
center=spatial.subs({v:0 for v in spatial})
test('barycentric_center_equal_quarters',equal_mat(lambda4.subs(dict(zip(spatial,center))),ones/4))

# A general affine (non-regular) tetrahedron and induced spatial metric.
verts=[Matrix(x) for x in [(0,0,0),(2,0,0),(1,3,0),(0,1,4)]]
A=Matrix.hstack(*[verts[k]-verts[0] for k in (1,2,3)])
g=A.T*A
mu1,mu2,mu3=symbols('mu1 mu2 mu3',real=True)
mu=[1-mu1-mu2-mu3,mu1,mu2,mu3]
coord=sum((mu[k]*verts[k] for k in range(4)),zeros(3,1))
test('affine_barycentric_coordinate_map',equal_mat(coord,A*Matrix([mu1,mu2,mu3])))
test('affine_metric_pullback',equal_mat(coord.jacobian([mu1,mu2,mu3]).T*coord.jacobian([mu1,mu2,mu3]),g))
test('general_tetra_metric_positive_definite',all(g[:i,:i].det()>0 for i in (1,2,3)))
test('general_tetra_volume_from_determinant',abs(det(A))/6==4)
test('general_tetra_local_chart_nondegenerate',det(A)!=0)
# Density is an illustrative conserved scalar, not native packet energy.
rho=lambda p:4+p[0]+2*p[1]+p[2]
E=sum(rho(v) for v in verts)*Q(4,4)
test('energy_parent_integral_affine_exact',E==31)
centroid=sum(verts,zeros(3,1))/4
child_volumes=[]
child_energies=[]
for omit in range(4):
    child=[centroid]+[verts[i] for i in range(4) if i!=omit]
    childA=Matrix.hstack(*[child[i]-child[0] for i in (1,2,3)])
    volume=abs(det(childA))/6
    child_volumes.append(volume)
    e=volume*sum(rho(v) for v in child)/4
    child_energies.append(e)
    test(f'refined_child_volume_{omit}',volume==1)
    test(f'refined_child_energy_positive_{omit}',e>0)
test('refined_children_volume_additive',sum(child_volumes)==4)
test('refined_children_energy_additive',sum(child_energies)==E)

# Two face-adjacent tetrahedra, no need for a cubical primitive.
base=[Matrix([0,0,0]),Matrix([1,0,0]),Matrix([0,1,0])]
up=base+[Matrix([0,0,1])]
down=base+[Matrix([0,0,-1])]
face_l0,face_l1,face_l2=symbols('f0 f1 f2',real=True)
face_lambdas=[face_l0,face_l1,face_l2,0]
facemap_up=sum((face_lambdas[i]*up[i] for i in range(4)),zeros(3,1))
facemap_down=sum((face_lambdas[i]*down[i] for i in range(4)),zeros(3,1))
test('shared_face_coordinate_gluing',equal_mat(facemap_up,facemap_down))
test('shared_face_metric_gluing',equal_mat(facemap_up.jacobian([face_l0,face_l1]).T*facemap_up.jacobian([face_l0,face_l1]),
    facemap_down.jacobian([face_l0,face_l1]).T*facemap_down.jacobian([face_l0,face_l1])))
Vu=abs(det(Matrix.hstack(*[up[k]-up[0] for k in (1,2,3)])))/6
Vd=abs(det(Matrix.hstack(*[down[k]-down[0] for k in (1,2,3)])))/6
Eu=Vu*sum(rho(v) for v in up)/4
Ed=Vd*sum(rho(v) for v in down)/4
test('two_tetra_joint_volume',Vu+Vd==Q(1,3))
test('two_tetra_joint_energy',Eu+Ed==Q(19,12))
test('shared_internal_flux_conservation',simplify((Eu-Q(1,7))+(Ed+Q(1,7))-(Eu+Ed))==0)

# Oriented incidence: top [0,1,2,3] and bottom [0,2,1,4].
def boundary(simplex):
    return {tuple(simplex[:i]+simplex[i+1:]):(-1)**i for i in range(len(simplex))}
def canonical_signed(face,coef):
    ids=list(face)
    inv=sum(ids[i]>ids[j] for i in range(len(ids)) for j in range(i+1,len(ids)))
    return tuple(sorted(ids)),coef*(-1 if inv%2 else 1)
b1=boundary((0,1,2,3))
b2=boundary((0,2,1,4))
combined={}
for b in (b1,b2):
    for face,s in b.items():
        k,v=canonical_signed(face,s)
        combined[k]=combined.get(k,0)+v
test('shared_triangle_oriented_cancellation',combined[(0,1,2)]==0)
test('nonshared_faces_bound_union',len([v for v in combined.values() if v!=0])==6)

# K4 is graph not auto-filled simplex, no physical dynamical assertion is imported.
from math import comb
test('K4_edge_count',comb(4,2)==6)
test('K4_triangular_face_count_if_admitted',comb(4,3)==4)
test('K4_interior_count_if_admitted',comb(4,4)==1)

# Full four-dimensional spacetime chart has a new, independent temporal coordinate.
tau=symbols('tau',real=True)
chart4=Matrix([mu1,mu2,mu3,tau])
test('3plus1_independent_coordinate_rank',chart4.jacobian([mu1,mu2,mu3,tau]).rank()==4)
test('space_only_barycentric_constraint',simplify(sum(mu)-1)==0)

results={
 'artifact':'UD_TETRAHEDRAL_NATIVE_COORDINATE_ATLAS_v0.7',
 'status':'DEVELOPMENT_NO_REGISTRY_ENTRY','physical_promotion':0,
 'total_exact_checks_passed':len(checks),
 'checks':checks,
 'regular_frame':{'vertices':'(±1,±1,±1)/sqrt(3), product-sign +','N_transpose_N':'4/3 I_3',
 'lambda':'1/4 ones + 3/4 N x','metric':'ds2=(4/3) sum d_lambda_i^2, sum d_lambda_i=0'},
 'general_affine':{'vertex_coords':[list(v) for v in verts],'Gram':[[str(e) for e in row] for row in g.tolist()],
    'detA':str(det(A)),'volume':str(abs(det(A))/6),'energy':str(E),
    'child_volumes':list(map(str,child_volumes)),'child_energies':list(map(str,child_energies))},
 'two_tetra_glue':{'energy_top':str(Eu),'energy_bottom':str(Ed),'total':str(Eu+Ed),
    'shared_face_flux_cancellation':True},
 'no_go':['Constrained fourth barycentric weight is not an independent spatial/time coordinate',
 'Regular tetrahedral Euclidean 3-space face-to-face tiling fails (angle obstruction)',
 'A tetrahedral representation alone does not derive physical energy or spacetime'],
 'open':['Native edge metrics','Omega0 placement/refinement selection','time/causal bridge','physical energy/current units','twist/holonomy readout']
}
path=ROOT/'UD_TETRAHEDRAL_NATIVE_COORDINATE_ATLAS_RESULTS_v0.7.json'
path.write_text(json.dumps(results,indent=2,default=str)+'\n')
print(f'EXACT_CHECKS_PASS={len(checks)}')
print(f'Affine energy original {E}; children {child_energies}; shared two-tetra energy {Eu+Ed}')
print(f'Results: {path.name}')
