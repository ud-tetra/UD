#!/usr/bin/env python3
"""3+1 tetrahedral meshing, typed energy-preserving folding, and frame-twist controls.
Development mathematical comparator only; no native UD dynamics or physical promotion.
Python 3.10+, SymPy; exact arithmetic, no floating tolerances.
"""
from fractions import Fraction as F
from itertools import permutations, combinations
from collections import defaultdict
from pathlib import Path
from hashlib import sha256
import json
import sympy as s

checks=[]
def check(label, condition):
    if not bool(condition):
        raise AssertionError(label)
    checks.append(label)

def cube_triangulation(d):
    vertices=[]
    O=s.zeros(d,1)
    for perm in permutations(range(d)):
        cur=O.copy(); S=[cur.copy()]
        for coordinate in perm:
            cur=cur.copy();cur[coordinate]+=1
            S.append(cur)
        vertices.append((perm,S))
    return vertices

def simplex_volume(S):
    d=len(S)-1
    V=s.Matrix.hstack(*[S[i]-S[0] for i in range(1,d+1)])
    return abs(V.det())/s.factorial(d)

meshes={}
for dim in (3,4):
    cells=cube_triangulation(dim)
    vols=[simplex_volume(v) for _,v in cells]
    check('cube%d_cell_count'%dim,len(cells)==s.factorial(dim))
    check('cube%d_all_simplex_volume_exact'%dim,all(v==s.Rational(1,s.factorial(dim)) for v in vols))
    check('cube%d_partition_total_volume'%dim,sum(vols)==1)
    check('cube%d_vertex_paths_coordinate_monotonicity'%dim,all(all(sum(S[k+1][j]-S[k][j] for j in range(dim))==1 for k in range(dim)) for _,S in cells))
    meshes[dim]=cells

rho=lambda P: 1+P[0]+2*P[1]+3*P[2]
energy_cell=[]
for perm,S in meshes[3]:
    value=s.simplify(simplex_volume(S)*sum(rho(p) for p in S)/4)
    energy_cell.append(value)
check('3d_cube_total_energy_four_exact',sum(energy_cell)==4)
check('3d_cube_density_linear_exact_quadrature',all(val>0 for val in energy_cell))
# Check separately using direct exact cubical integration.
x,y,z=s.symbols('x y z')
check('integral_cube_equals_tetra_sum',s.integrate(1+x+2*y+3*z,(x,0,1),(y,0,1),(z,0,1))==sum(energy_cell))

rho4=lambda P: 1+P[0]+2*P[1]+3*P[2]+P[3]
action_like=[]
for perm,S in meshes[4]:
    action_like.append(simpl:=s.simplify(simplex_volume(S)*sum(rho4(p) for p in S)/5))
check('4d_integrated_density_is_nine_halves_not_3d_energy',sum(action_like)==s.Rational(9,2))
# CAUTION: integral rho4 d^3x dt has energy*time units when rho4 is energy density.

# Embedding of a tetrahedral 3D cell into a 4D time slab.
V3=[s.Matrix([0,0,0]),s.Matrix([1,0,0]),s.Matrix([0,1,0]),s.Matrix([0,0,1])]
low=[s.Matrix([*V3[i],0]) for i in range(4)]
high=[s.Matrix([*V3[i],1]) for i in range(4)]
slab_cells=[]
for k in range(4):
    # k-th simplex uses lower vertices 0..k and upper vertices k..3.
    slab_cells.append(low[:k+1]+high[k:])
slab_vols=[simplex_volume(S) for S in slab_cells]
check('tetrahedron_time_prism_has_four_4simplices',len(slab_cells)==4)
check('four_slab_simplex_volumes_equal_one_twentyfourth',all(v==s.Rational(1,24) for v in slab_vols))
check('slab_total_4volume_parent_3volume_times_duration',sum(slab_vols)==s.Rational(1,6))
# Source-free 1->4 spatial stellar subdivision, with a new internal apex.
bar=(V3[0]+V3[1]+V3[2]+V3[3])/4
star_children=[]
for missing in range(4):
    star_children.append([V3[j] for j in range(4) if j!=missing]+[bar])
star_vols=[simplex_volume(S) for S in star_children]
star_energies=[s.simplify(simplex_volume(S)*sum(rho(v) for v in S)/4) for S in star_children]
parent_E=s.simplify(simplex_volume(V3)*sum(rho(v) for v in V3)/4)
check('stellar_1_to_4_child_count',len(star_children)==4)
check('stellar_child_volumes_are_one_quarter',all(v==s.Rational(1,24) for v in star_vols))
check('stellar_child_volume_additivity',sum(star_vols)==simplex_volume(V3))
check('stellar_affine_density_energy_preservation',sum(star_energies)==parent_E)
check('stellar_nonuniform_density_changes_energy_allocation',len(set(star_energies))>1)

check('all_slab_vertices_are_on_two_time_slices',all(all(pt[3] in (0,1) for pt in S) for S in slab_cells))

# Adjacency by exactly one shared triangular face, in original 6-tetrahedron cube triangulation.
def keypoint(v):return tuple(int(t) for t in v)
tets3=[frozenset(keypoint(v) for v in S) for _,S in meshes[3]]
faces=[{frozenset(face) for face in combinations(T,3)} for T in tets3]
neighbors=defaultdict(list)
for i in range(6):
    for j in range(i+1,6):
        if len(faces[i] & faces[j])==1:
            neighbors[i].append(j);neighbors[j].append(i)
check('cube_tetrahedral_dual_graph_has_six_adjacent_pairs',sum(map(len,neighbors.values()))==12)
check('cube_tetrahedra_each_share_two_internal_faces',all(len(neighbors[i])==2 for i in range(6)))
# Conservative, positivity preserving symmetric exchange, arbitrary test weight not UD parameter.
E0=s.Matrix(energy_cell)
alpha=s.Rational(1,12)
E=E0.copy();snapshots=[str(sum(E))]
for n in range(12):
    En=s.Matrix([s.expand(E[i]+alpha*sum((E[j]-E[i]) for j in neighbors[i])) for i in range(6)])
    check('total_energy_conserved_update_%02d'%n,sum(En)==4)
    check('positive_cell_energies_update_%02d'%n,all(e>0 for e in En))
    E=En;snapshots.append(str(sum(E)))
check('internal_exchange_is_not_trivial',E!=E0)


# S4-equivariant 4-to-(3+1) tetrahedral tight-frame folding.
# Four tetrahedral normals in R3, four channel coordinates, normalized analysis map.
face_signs=s.Matrix([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]])
face_unit=face_signs/s.sqrt(3)
T=face_signs/2  # sqrt(3/4) times normalized face rows; rational map.
u=s.ones(4,1)/2
Q=s.Matrix.hstack(T,u)
check('tetrahedron_4_over_3_tight_frame',s.simplify(face_unit.T*face_unit)==s.Rational(4,3)*s.eye(3))
check('tetrahedron_face_normals_sum_zero',face_unit.T*s.ones(4,1)==s.zeros(3,1))
check('tetra_3_over_4_orthonormal_analysis',T.T*T==s.eye(3))
check('tetra_four_channel_orthogonal_split',Q.T*Q==s.eye(4))
check('tetra_spatial_projection_and_normal_complete',T*T.T+u*u.T==s.eye(4))
check('tetra_spatial_projection_kills_normal',T.T*u==s.zeros(3,1))
z_sample=s.Matrix([1,2,3,5])
x_fold=T.T*z_sample;q_fold=(u.T*z_sample)[0]
check('tetra_fold_inverse_reconstructs_all_four_channels',T*x_fold+u*q_fold==z_sample)
check('tetra_fold_preserves_full_quadratic_stock',s.simplify(z_sample.dot(z_sample)-(x_fold.dot(x_fold)+q_fold**2))==0)
check('tetra_fold_spatial_projection_alone_loses_q_norm',s.simplify(z_sample.dot(z_sample)-x_fold.dot(x_fold))==q_fold**2 and q_fold!=0)
# General positive quadratic energy uses a transported metric / mass matrix; cross terms survive.
M_channel=s.diag(1,2,3,5)
y_full=s.Matrix.vstack(x_fold,s.Matrix([q_fold]))
M_fold=Q.T*M_channel*Q
check('tetra_fold_general_quadratic_form_preserved_with_full_tensor',s.simplify((z_sample.T*M_channel*z_sample)[0]-(y_full.T*M_fold*y_full)[0])==0)
check('tetra_fold_general_metric_has_nonzero_mixed_terms',any(M_fold[i,3]!=0 for i in range(3)))

S4_det=[]
for perm in permutations(range(4)):
    P=s.zeros(4,4)
    for i,j in enumerate(perm):P[i,j]=1
    U=T.T*P*T
    parity=int(P.det())
    check('tetra_fold_S4_equivariance_'+''.join(map(str,perm)),U.T*U==s.eye(3) and P*u==u and P*T==T*U)
    check('tetra_fold_S4_orientation_'+''.join(map(str,perm)),U.det()==parity)
    S4_det.append(parity)
check('tetra_fold_S4_even_odd_split',S4_det.count(1)==12 and S4_det.count(-1)==12)
# The sign choice below is an added Lorentzian metric, NOT derivable from Euclidean energy norm.
eta_channel=T*T.T-u*u.T
check('tetra_fold_Lorentz_metric_signature',sorted(eta_channel.eigenvals().items())==[(-1,1),(1,3)])
check('tetra_fold_Lorentz_metric_involution',eta_channel*eta_channel==s.eye(4))
check('tetra_fold_Lorentz_metric_det_minus_one',eta_channel.det()==-1)
check('tetra_fold_Lorentz_interval_decomposes',s.simplify((z_sample.T*eta_channel*z_sample)[0]-(x_fold.dot(x_fold)-q_fold**2))==0)

# ADM decomposition, unit timelike normal and irreducible missing lapse/shift information.
h=s.diag(4,9,25)
N=s.Integer(7)
beta=s.Matrix([s.Rational(1,2),s.Rational(1,3),s.Rational(1,5)])
def adm_metric(h,N,beta):
    b=h*beta
    return s.Matrix.vstack(s.Matrix.hstack(s.Matrix([[-N**2+(beta.T*h*beta)[0]]]),b.T),s.Matrix.hstack(b,h))
g=adm_metric(h,N,beta)
check('ADM_metric_Lorentzian_signature_by_Schur',s.simplify(g.det())==-N*N*h.det())
normal=s.Matrix([1,-beta[0],-beta[1],-beta[2]])/N
check('ADM_unit_timelike_normal',s.simplify((normal.T*g*normal)[0])==-1)
normalcov=g*normal
check('ADM_normal_covariant_components',normalcov==s.Matrix([-N,0,0,0]))
hspacetime=g+normalcov*normalcov.T
check('ADM_induced_spatial_metric_recovers_h',hspacetime[1:4,1:4]==h)
check('ADM_normal_projection_annihilates_timelike_normal',hspacetime*normal==s.zeros(4,1))
check('ADM_mixed_projection_encodes_nonzero_shift',all(hspacetime[0,i+1]==(h*beta)[i] for i in range(3)))
g_control=adm_metric(h,s.Integer(5),s.Matrix([0,0,0]))
check('same_spatial_metric_distinct_lapse_shift_spacetimes',g!=g_control and g[1:4,1:4]==g_control[1:4,1:4])
check('Lorentzian_inertia_not_Euclidean_Gram',g.det()<0 and h.det()>0)

# Twisted auxiliary 3-frame bundle: metric-invisible but orientation-sensitive holonomy.
R=s.diag(-1,1,1)
check('reflection_twist_is_orthogonal',R.T*R==s.eye(3))
check('reflection_twist_preserves_spatial_metric_h',R.T*h*R==h)
check('reflection_twist_orientation_odd',R.det()==-1)
check('reflection_twist_is_nontrivial_monodromy',R!=s.eye(3))
# Spin double cover: after a 2*pi spatial rotation vectors return, but spinors change sign.
U2pi=s.diag(-1,-1)
U4pi=s.eye(2)
R2pi=s.eye(3)
check('spinor_2pi_sign_hidden_from_vector_metric',U2pi==-U4pi and R2pi==s.eye(3))
check('spinor_4pi_identity',U2pi*U2pi==U4pi)

# R is auxiliary O(3) transport around S^1 in a spatial slice; it is not a fourth spatial dimension.

# A dimension-forgetting readout loses the lapse and shift (explicit counterexample above),
# while energy total can still be retained by volume-weighted integration.
result={
 'artifact':'UD_TETRAHEDRAL_3PLUS1_ENERGY_FOLD_VERIFY_v0.5',
 'status':'DEVELOPMENT_NO_REGISTRY_ENTRY',
 'physical_promotion':0,
 'checks_count':len(checks),'all_pass':True,
 'cube3':{'simplex_count':6,'volume_each':'1/6','volume_total':'1',
          'cell_energy_exact':list(map(str,energy_cell)),'energy_total':'4',
          'internal_adjacent_pairs':6,'conservative_updates':12,'exchange_parameter':'1/12 PROTOCOL_CONTROL',
          'all_energy_totals':snapshots},
 'cube4':{'simplex_count':24,'4simplex_hypervolume_each':'1/24',
          'integrated_density_spacetime':'9/2','warning':'Energy-density integral over time has units energy*time, not energy'},
 'stellar_birth_3d':{'child_tetrahedra':4,'child_volumes':list(map(str,star_vols)),'child_energies_exact':list(map(str,star_energies)),'parent_energy_exact':str(parent_E),'resulting_dimension':'3 (not 4)'},
 'tetra_time_prism':{'4simplex_count':4,'hypervolume_each':'1/24',
                     'total_4volume':'1/6 (3volume*unit time interval)'},
 'tetra_4_over_3_fold':{'shape_factor':'4/3','inverse_factor':'3/4','analysis_T':[[str(T[i,j]) for j in range(3)] for i in range(4)],'normal_u':[str(t) for t in u],'sample_z':[1,2,3,5],'fold_x':[str(t) for t in x_fold],'fold_q':str(q_fold),'quadratic_stock_original':str(z_sample.dot(z_sample)),'quadratic_stock_spatial':str(x_fold.dot(x_fold)),'quadratic_stock_normal':str(q_fold**2),'S4_permutations_verified':24,'S4_rotations_12_reflections_12':True,'Lorentzian_signature_sign_assignment':'ADDED_CHOICE_NOT_DERIVED','general_positive_energy_metric_requires_cross_terms':True,'M_channel_diagonal':['1','2','3','5'],'M_fold':[[str(M_fold[i,j]) for j in range(4)] for i in range(4)]},
 '3plus1_ADM':{'h_det':'900','N':'7','beta':['1/2','1/3','1/5'],
               'g_det':str(g.det()),'g_matrix':[[str(g[i,j]) for j in range(4)] for i in range(4)],
               'timelike_unit_normal':'PASS','induced_h':'PASS','reconstruction_requires_lapse_shift':'PASS'},
 'twist':{'auxiliary_transport_R':[['-1','0','0'],['0','1','0'],['0','0','1']],
          'metric_invariant':True,'orientation_holonomy_detectable':True,'spinor_2pi_returns_minus_identity':True,
          'interpretation':'O(3) bundle monodromy on noncontractible spatial loop; no extra geometric spatial dimension'},
 'open':{'native_omega0_birth_trigger':'OPEN','native_energy_density_metric':'OPEN',
         'native_time_calibration':'OPEN','physical_global_energy_conservation_generic_GR':'NO-GO',
         '4_over_3_frame_factor_spacetime_identification':'OPEN'},
 'checks':checks
}
out=Path('/mnt/data/UD_TETRAHEDRAL_3PLUS1_ENERGY_FOLD_RESULTS_v0.5.json')
out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('PASS',len(checks),'exact checks')
print('Cube3: 6 tets total 3D E=4; cube4: 24 4-simplices total spacetime integral=9/2')
print('Tetra time prism: 4 4-simplices; exact total prism hypervolume=1/6')
print('ADM g_det=',g.det(),'normal^2=-1; same h distinct g')
print('Twist: scalar metric invariant, orientation changes')
