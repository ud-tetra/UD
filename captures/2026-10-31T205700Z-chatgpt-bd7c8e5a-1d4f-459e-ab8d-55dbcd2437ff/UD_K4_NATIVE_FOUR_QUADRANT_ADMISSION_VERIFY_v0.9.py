#!/usr/bin/env python3
"""Exact K4 four-quadrant admission and source-blocker audit, v0.9.

Purely mathematical model. Does not derive UD Omega_0 physics, energy or time.
Reproducibility: python3 with sympy; no randomness or external network.
"""
from __future__ import annotations
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
import sympy as S

ROOT = Path(__file__).resolve().parent
checks = []

def check(name: str, truth: bool, detail=None):
    if not truth:
        raise AssertionError(f"{name}: {detail}")
    checks.append(name)

n = 4
one = S.ones(n, 1)
J = one*one.T
I = S.eye(n)
P = I - J/4
L = 4*I - J
E = [S.eye(4)[:, i] for i in range(4)]
V = [S.simplify(L*e/2) for e in E]  # 4 vectors in the intrinsic zero-sum subspace

check('K4 graph adjacency and rank', L.rank() == 3 and L*one == S.zeros(4,1))
check('K4 Laplacian exact spectrum', L.eigenvals() == {S.Integer(0):1,S.Integer(4):3})
check('Centered vertex vectors',sum(V,S.zeros(4,1)) == S.zeros(4,1))
check('Canonical centered Gram', S.Matrix.hstack(*V).T * S.Matrix.hstack(*V) == 4*I-J)
check('Vertex Gram positive rank 3', (S.Matrix.hstack(*V).T*S.Matrix.hstack(*V)).rank()==3)
check('Normalized tetrahedral tight frame 4/3',S.Matrix.hstack(*V)*S.Matrix.hstack(*V).T/3 == S.Rational(4,3)*P)
for i in range(4):
    for j in range(4):
        check(f'Gram pair {i},{j}', S.expand((V[i].dot(V[j]))-(4*int(i==j)-1))==0)
for i,j in itertools.combinations(range(4),2):
    check(f'Equal edge {i}-{j}', (V[i]-V[j]).dot(V[i]-V[j]) == 8)
for leave in range(4):
    M = S.Matrix.hstack(*[V[j] for j in range(4) if j != leave])
    check(f'Positive cone Gram {leave}',(M.T*M)==4*S.eye(3)-S.ones(3,3) and (M.T*M).det()==16)

# Each centered regular tetrahedral vertex triple gives a 3D pointed cone.
# Readout x= sum_i lambda_i v_i and lambda_i=(1+v_i dot x)/4.
pts = [S.Matrix([S.Rational(a,2),S.Rational(b,2),S.Rational(c,2)])
       for a,b,c in itertools.product(range(-3,4),repeat=3)]
# Use {v_0,v_1,v_2} as a rational basis of H.
active_fan_hist = [0,0,0,0]
for index,t in enumerate(pts):
    x = t[0]*V[0]+t[1]*V[1]+t[2]*V[2]
    lam = [S.cancel((1+V[i].dot(x))/4) for i in range(4)]
    check(f'Partition-of-unity {index}', sum(lam)==1)
    check(f'Barycentric reconstruction {index}', sum((lam[i]*V[i] for i in range(4)),S.zeros(4,1)) == x)
    mi = min(lam)
    winners=[i for i in range(4) if lam[i]==mi]
    for leave in winners:
        ts=[S.simplify(lam[j]-lam[leave]) for j in range(4) if j!=leave]
        check(f'Conical inversion point {index} chart {leave}',all(v>=0 for v in ts) and sum((ts[k]*V[j] for k,j in enumerate([j for j in range(4) if j!=leave])),S.zeros(4,1))==x)
        active_fan_hist[leave] += 1
check('All four cones occur in rational test lattice',all(x>0 for x in active_fan_hist))

# Symmetry: standard representation of S4 on H, including parity of handedness.
D=S.Matrix.hstack(E[0]-E[3],E[1]-E[3],E[2]-E[3])
check('Zero-sum basis Gram nonsingular',(D.T*D).det()==4)
counts={'+':0,'-':0}
for k,perm in enumerate(itertools.permutations(range(4))):
    Z=S.zeros(4,4)
    for i in range(4): Z[perm[i],i]=1
    check(f'Permutation covariant Laplacian {k}',Z*L*Z.T==L)
    for i in range(4):
        check(f'Vertex equivariance {k} face {i}',Z*V[i]==V[perm[i]])
    rep=(D.T*D).inv()*D.T*Z*D
    sign=S.Integer((-1)**sum(perm[a]>perm[b] for a,b in itertools.combinations(range(4),2)))
    check(f'Orientation parity {k}',rep.det()==sign)
    counts['+' if sign==1 else '-']+=1
check('S4 has 12 proper, 12 improper standard frame actions',counts=={'+':12,'-':12})

# Filled-face versus shell distinction: oriented tetrahedron boundary incidence B2.
edges=list(itertools.combinations(range(4),2))
faces=list(itertools.combinations(range(4),3))
B2=S.zeros(len(edges),len(faces))
for k,(i,j,l) in enumerate(faces):
    B2[edges.index((j,l)),k] += 1
    B2[edges.index((i,l)),k] -= 1
    B2[edges.index((i,j)),k] += 1
B3=S.Matrix([(-1)**i for i in range(4)])
# faces order: 012 013 023 123. Alternating boundary coordinates in ascending face order:
B3 = S.Matrix([-1,1,-1,1])
check('Boundary-of-boundary K4',B2*B3==S.zeros(6,1))
check('Full-face cycle kernel rank',B2.rank()==3 and B2.nullspace()==[B3])
mask_stats=[]
for mask in range(16):
    f=S.Matrix([int(bool(mask & (1<<i)))*B3[i] for i in range(4)])
    is_closed=(B2*f)==S.zeros(6,1)
    check(f'Four-face cooperative closure mask {mask:04b}',is_closed==(mask in (0,15)))
    mask_stats.append({'mask':format(mask,'04b'),'closed':bool(is_closed),'exposed_edge_count':sum(int(b!=0) for b in B2*f)})
check('No single-face path of closed shell states',sum(z['closed'] for z in mask_stats)==2)

# Group action transitive: only empty/full invariant face subsets.
for mask in range(16):
    invariant=True
    for perm in itertools.permutations(range(4)):
        pmask=sum((1<<perm[i]) for i in range(4) if mask & (1<<i))
        if pmask!=mask:
            invariant=False
            break
    check(f'Invariant subset iff empty or full {mask:04b}',invariant == (mask in (0,15)))

# F_2 vertex distinction -> edge coboundary -> face parity has no discriminatory power.
# This is a strict no-go for deriving a nontrivial admission trigger from delta(delta(b)).
def triangle_parities(edge_bits):
    return tuple((edge_bits[edges.index((i,j))] ^ edge_bits[edges.index((i,k))] ^ edge_bits[edges.index((j,k))])
                 for i,j,k in faces)
vertex_edge_patterns=set()
for mask in range(16):
    b=[int(bool(mask & (1<<i))) for i in range(4)]
    edge_bits=tuple(b[i]^b[j] for i,j in edges)
    check(f'Vertex distinction double coboundary zero {mask:04b}',triangle_parities(edge_bits)==(0,0,0,0))
    vertex_edge_patterns.add(edge_bits)
check('Vertex gradients have 8 distinct edge patterns',len(vertex_edge_patterns)==8)
parity_occurrences={}
flat_edge_count=0
for mask in range(64):
    bits=tuple(int(bool(mask & (1<<i))) for i in range(6))
    ph=triangle_parities(bits)
    check(f'Independent edge cochain has even face parity {mask:06b}',sum(ph)%2==0)
    parity_occurrences[ph]=parity_occurrences.get(ph,0)+1
    flat_edge_count+=ph==(0,0,0,0)
check('Eight flat edge patterns are exactly vertex gradients',flat_edge_count==8 and
      vertex_edge_patterns=={tuple(int(bool(mask & (1<<i))) for i in range(6)) for mask in range(64) if triangle_parities(tuple(int(bool(mask & (1<<i))) for i in range(6)))==(0,0,0,0)})
check('Eight even-parity face syndromes with eight preimages each',len(parity_occurrences)==8 and set(parity_occurrences.values())=={8})

# Combinatorial admission candidate: requires complete closed 2-shell and 3-cell occupancy.
def fan_admission(mask:int,cell_filled:bool):
    return bool(mask==15 and cell_filled)
for mask in range(16):
    for filled in [False,True]:
        check(f'Atlas occupancy gated for mask={mask}, cell={filled}',fan_admission(mask,filled)==(mask==15 and filled))

# Source non-identifiability: two distinct permutation-invariant maps with different birth.
def hold(a:int): return a
def complete(a:int): return 15
check('K4 admissible maps disagree starting without faces',hold(0)!=complete(0))
for mask in range(16):
    check(f'Hold idempotent and complete idempotent {mask}', hold(hold(mask))==hold(mask) and complete(complete(mask))==complete(mask))

# Weighted effective-resistance readout: a metric candidate, NOT a UD physical metric.
def weighted_laplacian(weight_by_pair):
    ret=S.zeros(4,4)
    for (i,j),wt in weight_by_pair.items():
        q=E[i]-E[j]
        ret+=wt*q*q.T
    return ret
w={ij:S.Integer(1) for ij in edges}
w[(0,1)]=S.Integer(2)
w[(1,2)]=S.Integer(3)
Lw=weighted_laplacian(w)
Lwp=(Lw+J/4).inv()-J/4  # exact Moore-Penrose pseudoinverse on connected graph
check('Positive weighted graph rank 3',Lw.rank()==3 and Lwp*one==S.zeros(4,1))
check('Weighted Green inverse on H',Lw*Lwp==P and Lwp*Lw==P)
R=S.Matrix(4,4,lambda i,j: ((E[i]-E[j]).T*Lwp*(E[i]-E[j]))[0])
check('Nonregular weighted resistance geometry',len({R[i,j] for i,j in edges})>1)
D3=S.Matrix.hstack(E[0]-E[3],E[1]-E[3],E[2]-E[3])
M3=D3.T*Lwp*D3
check('Weighted resistance affine lift rank 3',M3.det()>0 and M3.rank()==3)
for k,perm in enumerate(itertools.permutations(range(4))):
    Z=S.zeros(4,4)
    for i in range(4):Z[perm[i],i]=1
    pw={(perm[i],perm[j]) if perm[i]<perm[j] else (perm[j],perm[i]):val for (i,j),val in w.items()}
    check(f'Weighted graph equivariance {k}',weighted_laplacian(pw)==Z*Lw*Z.T)
    check(f'Weighted resistance equivariance {k}',(weighted_laplacian(pw)+J/4).inv()-J/4 == Z*Lwp*Z.T)

# Finite non-Abelian curvature check: a curved connection can coexist with a closed tetrahedral shell.
perms=list(itertools.permutations(range(3)))
ident=(0,1,2)
def mul(a,b):return tuple(a[b[i]] for i in range(3))
def inv(a):return tuple(a.index(i) for i in range(3))
U={ij:ident for ij in edges}
U[(0,1)]=(1,0,2)
U[(0,2)]=(0,2,1)
def getU(i,j,assigned):
    return assigned[(i,j)] if i<j else inv(assigned[(j,i)])
def hol(tri,assigned):
    i,j,k=tri
    return mul(mul(getU(i,j,assigned),getU(j,k,assigned)),getU(k,i,assigned))
initial_nonflat=[t for t in faces if hol(t,U)!=ident]
check('Admitted geometric fan permits nonflat edge connection',len(initial_nonflat)>0 and fan_admission(15,True))
for k,gs in enumerate(itertools.product(perms,repeat=4)):
    ug={(i,j):mul(mul(gs[i],v),inv(gs[j])) for (i,j),v in U.items()}
    check(f'Curvature gauge covariance {k}',all(hol(tri,ug)==mul(mul(gs[tri[0]],hol(tri,U)),inv(gs[tri[0]])) for tri in faces))
    check(f'Curvature nonflat face count invariant {k}',sum(hol(t,ug)!=ident for t in faces)==len(initial_nonflat))

# Graph masks/cell/readout vs physical reality must remain different status types.
results={
  'artifact':'UD_K4_NATIVE_FOUR_QUADRANT_ADMISSION_AUDIT_v0.9',
  'date':'2026-10-31',
  'status':'DEVELOPMENT_NO_REGISTRY_ENTRY','physical_promotion':0,
  'exact_assertion_groups':len(checks),
  'k4_laplacian_spectrum':{'0':1,'4':3},
  'vertex_gram':'4I4-J4',
  'coordinate_carrier':'H={x in R^4 | sum(x)=0}',
  'graph_symmetry':{'order':24,'proper':counts['+'],'improper':counts['-']},
  'face_masks':mask_stats,
  'all_or_none_closure':True,
  'binary_double_coboundary_gate':{'vertex_masks_tested':16,'edge_masks_tested':64,'exact_flat_edge_patterns':flat_edge_count,'distinct_face_parity_syndromes':len(parity_occurrences),'verdict':'NO_GO as selective trigger if edge labels are only delta b'},
  'S4_invariant_nonempty_face_subsets':['1111'],
  'coordinate_quadrants':4,
  'cone_solid_angle_steradians':'pi each, under unweighted counting metric',
  'weighted_metric_control':{'weights':{str(e):str(w[e]) for e in edges},'resistance_squared_lengths':{str(e):str(R[e[0],e[1]]) for e in edges},'affine_gram_det':str(M3.det()),'rank':3},
  'curved_nonabelian_control':{'group':'S3','nonflat_faces':[list(f) for f in initial_nonflat],'gauge_transforms_checked':len(perms)**4},
  'rational_coordinate_grid_points':len(pts),
  'candidate_admission_gate':'all four oriented triangles closed AND separately admitted filled C3 cell',
  'source_blockers':['Omega0 face activation law','native causal/energy source trigger','physical metric and frame scale','choice of global chart transition/gauge','chirality and absolute orientation'],
  'no_go':['S4 cannot select a single face/direction from symmetric K4','fixed carrier cannot create a new simplex','closed 2-shell does not force a filled 3-cell','delta(delta(b))=0 cannot be an informative face admission selector if edge cochain is solely vertex coboundary'],
  'check_names':checks
}
(ROOT/'UD_K4_NATIVE_FOUR_QUADRANT_ADMISSION_RESULTS_v0.9.json').write_text(json.dumps(results,indent=2)+'\n')
print('EXACT_ASSERTION_GROUPS',len(checks))
print('GRID_POINT_CHECKS',len(pts),'GAUGE_TRANSFORMS',len(perms)**4)
print('MASKS_CLOSED',[a['mask'] for a in mask_stats if a['closed']])
print('BINARY_COBDRY_CONTROL',flat_edge_count,'of 64 independent edge patterns flat; every vertex gradient flat')
print('NONFLAT_FACES',initial_nonflat)
print('WEIGHTED_RESISTANCE_PAIRS',[(str(e),str(R[e[0],e[1]])) for e in edges])
print('CLASSIFICATION','STRUCTURAL_PASS__OMEGA0_BIRTH_SOURCE_BLOCKED')
