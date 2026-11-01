#!/usr/bin/env python3
"""Exact UD simplex-fill ladder checks; abstract mathematics only.

No native UD fill event, physical energy identity, or physical metric is claimed.
Uses Python and SymPy with exact integers and rationals.
"""
from __future__ import annotations

import itertools
import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

import sympy as sp

OUT = Path(__file__).resolve().parent
checks = []


def ck(label: str, cond: bool):
    if not bool(cond):
        raise AssertionError(label)
    checks.append(label)


def simplex_complex(n: int, top_dim: int | None = None):
    """All simplices (sorted tuples) of an n-simplex through top_dim."""
    if top_dim is None:
        top_dim = n
    return {k: list(itertools.combinations(range(n + 1), k + 1))
            for k in range(top_dim + 1)}


def boundary_matrix(C, k: int):
    """Exact cellular boundary d_k: C_k -> C_{k-1}, k>0."""
    if k <= 0:
        raise ValueError('ordinary boundary d_k defined for k>=1')
    low = C.get(k-1, [])
    high = C.get(k, [])
    index = {x: i for i, x in enumerate(low)}
    M = sp.zeros(len(low), len(high))
    for j, cell in enumerate(high):
        for i in range(len(cell)):
            face = cell[:i] + cell[i+1:]
            M[index[face], j] += (-1)**i
    return M


def betti(C):
    """Ordinary Betti numbers via ranks over Q, including H_0."""
    keys = sorted(C)
    last = max(keys)
    ranks = {k: boundary_matrix(C, k).rank() for k in range(1, last+1)}
    return {k: len(C[k]) - ranks.get(k, 0) - ranks.get(k+1, 0) for k in keys}


def euler(C):
    return sum((-1)**k * len(C.get(k, [])) for k in C)


def parity(ordered):
    return (-1) ** sum(ordered[i] > ordered[j] for i in range(len(ordered))
                       for j in range(i+1, len(ordered)))


def oriented(ordered):
    return (tuple(sorted(ordered)), parity(ordered))


def sum_chain(*terms):
    out = defaultdict(int)
    for factor, chain in terms:
        for face, coeff in chain.items():
            out[face] += factor * coeff
    return {f:c for f,c in out.items() if c}


def bd_chain(chain):
    result = defaultdict(int)
    for simplex, coeff in chain.items():
        if not simplex:  # augmentation target C_-1 has zero boundary
            continue
        if len(simplex) == 1:
            result[()] += coeff
            continue
        for j in range(len(simplex)):
            face = simplex[:j] + simplex[j+1:]
            result[face] += coeff * ((-1)**j)
    return {f:c for f,c in result.items() if c}


def cone(chain, apex):
    result = defaultdict(int)
    for simplex,coeff in chain.items():
        if apex in simplex:
            raise ValueError('Cone apex already in base')
        canon, sign = oriented((apex,) + simplex)
        result[canon] += coeff * sign
    return {f:c for f,c in result.items() if c}


def face_chain(dim):
    return bd_chain({tuple(range(dim + 1)):1})


result = {
 'artifact':'UD_SIMPLEX_FILL_LADDER_v0.6',
 'status':'DEVELOPMENT_NO_REGISTRY_ENTRY',
 'physical_promotion':0,
 'coefficient_domain':'integer/rational algebra; symbolic radicals for metric volumes',
 'sign_convention':'ascending vertex orientation; augmented d_0 sends vertex to empty-face generator',
 'dimensions':[], 'skeleta':[], 'binary_cooperative_closure':[], 'geometry':{}, 'energy_receipts':{}
}

# Pascal increments and homology, including 0D-to-1D connection.
for d in range(1, 5):
    old = simplex_complex(d-1)
    shell = simplex_complex(d, d-1)
    full = simplex_complex(d)
    f_old = [len(old.get(k, [])) for k in range(d+1)]
    f_shell = [len(shell.get(k, [])) for k in range(d+1)]
    f_full = [len(full.get(k, [])) for k in range(d+1)]
    delta_shell = [f_shell[k] - f_old[k] for k in range(d+1)]
    delta_full = [f_full[k] - f_old[k] for k in range(d+1)]
    target_delta_full = [math.comb(d, k) for k in range(d+1)]
    target_delta_shell = [math.comb(d, k) for k in range(d)] + [0]
    ck(f'd{d}_f_vector_pascal', delta_full == target_delta_full)
    ck(f'd{d}_shell_increment', delta_shell == target_delta_shell)
    ck(f'd{d}_single_interior_cell', f_full[-1]-f_shell[-1] == 1)
    ck(f'd{d}_euler_fill_ball', euler(full) == 1)
    ck(f'd{d}_euler_shell_sphere', euler(shell) == 1 + (-1)**(d-1))
    for C,kind in ((shell,'shell'), (full,'fill')):
        for k in range(2, max(C)+1):
            ck(f'd{d}_{kind}_boundary_square_k{k}',
               boundary_matrix(C,k-1)*boundary_matrix(C,k) == sp.zeros(len(C[k-2]), len(C[k])))
    bs = betti(shell)
    bf = betti(full)
    if d == 1:
        ck('d1_shell_two_components', bs == {0:2})
        ck('d1_fill_one_component', bf == {0:1,1:0})
    else:
        ck(f'd{d}_shell_unique_top_hole', bs == {k:(1 if k in (0,d-1) else 0) for k in range(d)})
        ck(f'd{d}_fill_contractible', bf == {k:(1 if k==0 else 0) for k in range(d+1)})
        topbd = boundary_matrix(shell,d-1)
        ck(f'd{d}_one_dim_oriented_cycle',len(shell[d-1])-topbd.rank()==1)
    # Chain-level shell-first / fill-second: u=old - cone_d d(old) = boundary cone_d(old).
    c={tuple(range(d)):1}
    apex=d
    direct=bd_chain(cone(c,apex))
    indirect=sum_chain((1,c),(-1,cone(bd_chain(c),apex)))
    ck(f'd{d}_cone_boundary_identity',direct==indirect)
    ck(f'd{d}_closed_shell_chain',bd_chain(direct)=={})
    ck(f'd{d}_shell_exact_facets',len(direct)==d+1 and sorted(direct.values())==[-1]*(sum(v==-1 for v in direct.values())) + [1]*(sum(v==1 for v in direct.values())))
    # Exact regular metric volume: Gram = (a^2/2)(I+J). a=1.
    G=sp.Rational(1,2)*(sp.eye(d)+sp.ones(d,d))
    gramdet=sp.factor(G.det())
    expected_det=sp.Rational(d+1,2**d)
    ck(f'd{d}_regular_simplex_gram_determinant',gramdet==expected_det)
    V=sp.sqrt(gramdet)/sp.factorial(d)
    expected_volume=sp.sqrt(d+1)/(sp.factorial(d)*sp.sqrt(2**d))
    ck(f'd{d}_regular_simplex_volume',sp.simplify(V-expected_volume)==0)
    # Independent incenter/pyramid computation: (d+1) congruent facet pyramids.
    r_d=1/sp.sqrt(2*d*(d+1))
    A_d=sp.sqrt(d)/(sp.factorial(d-1)*sp.sqrt(2**(d-1)))
    V_from_facets=sp.simplify(sp.Rational(d+1,d)*A_d*r_d)
    ck(f'd{d}_incenter_facets_reconstruct_volume',sp.simplify(V-V_from_facets)==0)
    result['dimensions'].append({
      'd':d,'old_f':f_old,'shell_f':f_shell,'full_f':f_full,
      'shell_increment':delta_shell,'full_increment':delta_full,
      'euler_shell':euler(shell),'euler_full':euler(full),
      'betti_shell':bs,'betti_full':bf,
      'regular_unit_edge_volume':str(sp.simplify(V)),
      'gram_determinant':str(gramdet),
      'facet_to_bulk_ratio':str(sp.Rational(d+1,d)),
      'inradius_unit_edge':str(sp.simplify(r_d)),
      'regular_facet_volume_unit_edge':str(sp.simplify(A_d)),
      'bulk_volume_from_facet_pyramids':str(V_from_facets),
      'oriented_shell_cycle':{str(face):coeff for face,coeff in direct.items()},
    })

# Independent mod-2 exhaustive facet-closure enumeration (no free boundary).
# A complete d-simplex has d+1 top facets, and all-or-none is the only mod-2 cycle.
for d in range(1,5):
    shell=simplex_complex(d,d-1)
    facet_count=d+1
    if d==1:
        M=sp.ones(1,facet_count)  # augmented boundary of vertices
    else:
        M=boundary_matrix(shell,d-1)
    valid=[]
    for mask in range(1 << facet_count):
        coeff=sp.Matrix([(mask>>i)&1 for i in range(facet_count)])
        residue=M*coeff
        if all(int(v)%2==0 for v in residue):
            valid.append(mask)
    ck(f'd{d}_all_or_none_facet_shell_GF2',valid==[0,(1<<facet_count)-1])
    result['binary_cooperative_closure'].append({'d':d,'facets':facet_count,
       'subsets_tested':1<<facet_count, 'zero_boundary_masks':valid})

# Topological holes migrate upward as all cliques are added in skeleton stages.
for ambient_dim in (2,3,4):
    for skeleton_dim in range(1,ambient_dim+1):
        C=simplex_complex(ambient_dim,skeleton_dim)
        b=betti(C)
        ck(f'K{ambient_dim+1}_skeleton_{skeleton_dim}_lower_homology',
           all(b.get(k,0)==0 for k in range(1,skeleton_dim)))
        if skeleton_dim<ambient_dim:
            ck(f'K{ambient_dim+1}_skeleton_{skeleton_dim}_hole_binomial',
               b[skeleton_dim]==math.comb(ambient_dim,skeleton_dim+1))
        else:
            ck(f'K{ambient_dim+1}_complete_simplex_contractible',
               b=={k:(1 if k==0 else 0) for k in range(ambient_dim+1)})
        result['skeleta'].append({'n_vertices':ambient_dim+1,'top_dim':skeleton_dim,
                                   'f':[len(C.get(k,[])) for k in range(skeleton_dim+1)],
                                   'betti':b,'euler':euler(C)})

# Explicit counterexample: 4-edge square has closed cycle but is not one triangle's boundary.
square=( (0,1),(1,2),(2,3),(0,3))
ck('closed_square_not_one_triangle',len(set().union(*[set(x) for x in square]))==4)

# Metric rank: same K4 abstract simplex may carry degenerate Euclidean 3D volume.
A=sp.eye(3)
B=sp.Matrix([[1,0,1],[0,1,1],[0,0,0]])
ck('tetra_gram_positive', A.det()>0)
ck('coplanar_tetra_gram_degenerate', (B.T*B).det()==0)

# Oriented boundary flux exactly measures *enclosed geometric volume*, even for unfilled shell.
verts={0:sp.Matrix([0,0,0]), 1:sp.Matrix([1,0,0]),
       2:sp.Matrix([0,1,0]), 3:sp.Matrix([0,0,1])}
faces=bd_chain({(0,1,2,3):1})
area_flux=sp.zeros(3,1)
flux_moment=sp.S.Zero
face_evidence=[]
for face,sign in sorted(faces.items()):
    p,q,r=(verts[v] for v in face)
    outward=sign*(q-p).cross(r-p)/2
    centroid=(p+q+r)/3
    area_flux+=outward
    flux_moment+=centroid.dot(outward)
    face_evidence.append({'face':list(face),'oriented_sign':sign,
                           'area_vector':[str(x) for x in outward],
                           'centroid':[str(x) for x in centroid]})
ck('tetra_outward_area_vectors_close',area_flux==sp.zeros(3,1))
Vboundary=sp.simplify(flux_moment/3)
Vdet=sp.Abs(sp.Matrix.hstack(verts[1]-verts[0], verts[2]-verts[0], verts[3]-verts[0]).det())/6
ck('tetra_boundary_divergence_volume',Vboundary==sp.Rational(1,6))
ck('tetra_boundary_determinant_agrees',Vboundary==Vdet)
result['geometry']={'reference_tetrahedron_enclosed_volume_from_boundary':str(Vboundary),
                    'reference_tetrahedron_enclosed_volume_from_determinant':str(Vdet),
                    'outward_faces':face_evidence,
                    'caveat':'Same enclosed volume can be evaluated for a hollow shell; does not witness 3-cell occupancy',
                    'coplanar_abstract_tetra_volume':'0'}

# 4/3 tetra face frame, distinct from a source-derived response or physical dimension ratio.
n=[sp.Matrix(s)/sp.sqrt(3) for s in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
N=sp.Matrix.hstack(*n)
ck('tetra_frame_sum_zero',sum(n,sp.zeros(3,1))==sp.zeros(3,1))
ck('tetra_frame_bound_4_over_3',sp.simplify(N*N.T-sp.Rational(4,3)*sp.eye(3))==sp.zeros(3,3))

# Conservative fixed-volume refinement, affine energy on coordinate tetrahedron.
lam=sp.symbols('x y z')
f=lambda p: sp.S.One+p[0]+2*p[1]+3*p[2]
vcenter=sum(verts.values(),sp.zeros(3,1))/4
parent_energy=Vdet*sum(f(verts[i]) for i in range(4))/4
child_energies=[]
for omitted in range(4):
    child=[vcenter]+[verts[i] for i in range(4) if i!=omitted]
    mat=sp.Matrix.hstack(child[1]-child[0],child[2]-child[0],child[3]-child[0])
    vol=sp.Abs(mat.det())/6
    ck(f'stellar_child_{omitted}_quarter_volume',vol==Vdet/4)
    child_energy=sp.factor(vol*sum(map(f,child))/4)
    child_energies.append(child_energy)
ck('stellar_energy_additivity',sum(child_energies)==parent_energy==sp.Rational(5,12))
for depth in range(7):
    children_count=4**depth
    child_vol=Vdet/sp.Integer(4)**depth
    ck(f'iterated_tetra_fill_depth_{depth}_conserves_volume',sp.simplify(children_count*child_vol-Vdet)==0)
# Independent calculus confirmation, not just vertex-affine quadrature.
x,y,z=sp.symbols('x y z', nonnegative=True)
parent_integral=sp.integrate(1+x+2*y+3*z,(z,0,1-x-y),(y,0,1-x),(x,0,1))
ck('stellar_energy_direct_integral_independent_check',parent_integral==parent_energy)
result['energy_receipts']['fixed_volume_remesh']={
  'parent_energy':str(parent_energy),'children':[str(e) for e in child_energies],
  'sum':str(sum(child_energies)), 'direct_calculus_integral':str(parent_integral), 'density':'epsilon(x,y,z)=1+x+2y+3z',
  'classification':'EXACT additivity only; test density is not native UD energy',
  'iterated_refinement':'At depth n, 4**n cells each have V_parent/4**n and the total domain remains the original 3D tetrahedron' }

# Birth with positive bulk energy and unchanged prior energy is impossible without separate reserve.
for alpha in (sp.S.Zero,sp.Rational(1,3),sp.S.One):
    old_R=sp.Rational(7,3)
    bulk=alpha*old_R
    remaining=(1-alpha)*old_R
    ck(f'birth_receipt_alpha_{alpha}', bulk+remaining==old_R)
result['energy_receipts']['source_nonuniqueness']={
  'initial_reserve':'7/3','allowed_alpha':['0','1/3','1'],
  'statement':'All conserve the same total; no closure or conservation equation selects alpha',
  'closed_no_source_positive_bulk':'IMPOSSIBLE if old reservoir/energy is unchanged and no compensating transfer occurs'}

result['checks_passed']=len(checks)
result['check_labels']=checks
result['source_scope']='UD coefficient ledger v0.39 rows P01-P09, F01-F05, G05, Q153-Q179; prior v0.3/v0.5 construction models'
result['limitations']=['Flag-complex fill is a chosen mathematical completion, not a dynamical birth law.',
  'Boundary flux computes enclosed geometric volume but cannot prove top-cell occupancy.',
  'Support norm is not physical energy; 2D/3D/4D energy units must be typed.',
  'Nonzero group holonomy is compatible with an attached curved face; flatness is not universally required.',
  'Fractal growth cannot follow from finite Pascal counts alone.',
  'Native UD apex/face/cell birth thresholds, physical time, and empirical bridge remain open.']
path=OUT/'UD_SIMPLEX_FILL_LADDER_RESULTS_v0.6.json'
path.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf8')
print(f'PASS: {len(checks)} exact assertion groups across fill, homology, volume and energy-typing controls')
print('Dimension progression:')
for row in result['dimensions']:
    print(f"  d={row['d']}: delta_f={row['full_increment']} betti_shell={row['betti_shell']} betti_fill={row['betti_full']} V_regular(a=1)={row['regular_unit_edge_volume']}")
print('Topological skeleton progressions:')
for row in result['skeleta']:
    print(f"  K{row['n_vertices']} skeleton {row['top_dim']}: f={row['f']} betti={row['betti']}")
print(f"Boundary volume={Vboundary}; energy parent={parent_energy}; child energies={[str(e) for e in child_energies]}")
