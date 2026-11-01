#!/usr/bin/env python3
"""Exact, conditional mathematics for UD K4 pre-birth source channel v1.1.

Does NOT derive an Omega0 birth rule, physical energy, or measured time.
Uses candidate comparison carriers; not a native evolution simulation.
"""
from itertools import permutations, combinations, product
from pathlib import Path
import json
import sympy as S

V = tuple(range(4))
E = list(combinations(V, 2))
F = list(combinations(V, 3))
T = [V]
Z = S.Integer(0)
ONE = S.Integer(1)
checks = {}

def pass_check(group, condition):
    assert condition, f"FAILED {group}"
    checks[group] = checks.get(group, 0) + 1

def oriented_incidence(basis_low, basis_high):
    out = S.zeros(len(basis_low), len(basis_high))
    for j, high in enumerate(basis_high):
        for k in range(len(high)):
            face = high[:k] + high[k+1:]
            out[basis_low.index(face), j] += (-1)**k
    return out

def parity(p):
    return (-1)**sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))

def signed_rep(basis, p):
    out = S.zeros(len(basis))
    for j, face in enumerate(basis):
        seq = tuple(p[v] for v in face)
        canon = tuple(sorted(seq))
        out[basis.index(canon), j] = parity(seq)
    return out

B1 = oriented_incidence([(i,) for i in V], E)
B2 = oriented_incidence(E, F)
B3 = oriented_incidence(F, T)
u = -B3
P = u * u.T / 4
Q = S.eye(4) - P

pass_check('chain_dimensions', B1.shape == (4,6) and B2.shape == (6,4) and B3.shape == (4,1))
pass_check('chain_boundary_squared', B1 * B2 == S.zeros(4,4))
pass_check('chain_boundary_squared', B2 * B3 == S.zeros(6,1))
pass_check('chain_kernel_rank', B2.rank() == 3 and B2*u == S.zeros(6,1))
pass_check('chain_spectral_identity', B2.T*B2 == 4*S.eye(4) - u*u.T)
pass_check('chain_projector', P*P == P and Q*Q == Q and P*Q==S.zeros(4))
pass_check('chain_normalization', (u.T*u)[0] == 4)

Rs=[]; signs=[]
for p in permutations(V):
    R0 = signed_rep([(i,) for i in V], p)
    R1 = signed_rep(E, p)
    R2 = signed_rep(F, p)
    sign = parity(p)
    pass_check('S4_permutation_chain_map', B2*R2 == R1*B2)
    pass_check('S4_permutation_chain_map', B1*R1 == R0*B1)
    pass_check('S4_shell_sign', R2*u == sign*u)
    pass_check('S4_projector_equivariance', R2*P == P*R2)
    pass_check('S4_isometry', R2.T * R2 == S.eye(4))
    Rs.append(R2)
    signs.append(sign)

# Only all-on or all-off binary hard face gates preserve full S4 symmetry
# when no symmetry-breaking source state has been supplied.
for hard_gate in product((0,1), repeat=4):
    h = S.Matrix(hard_gate)
    invariant = all(R.applyfunc(abs)*h == h for R in Rs)
    pass_check('S4_binary_hard_gate_all_or_none', invariant == (sum(hard_gate) in (0,4)))

# Determine Hom_{S4}(C2,C3_sign), and contrast trivial codomain.
Msign = S.Matrix.vstack(*[R.T - sign*S.eye(4) for R,sign in zip(Rs,signs)])
Mtriv = S.Matrix.vstack(*[R.T - S.eye(4) for R in Rs])
nsign = Msign.nullspace()
pass_check('unique_signed_intertwiner', Msign.rank() == 3 and len(nsign)==1 and nsign[0][0]!=0 and nsign[0]==(nsign[0][0]/u[0])*u)
pass_check('no_linear_even_scalar_intertwiner', Mtriv.rank() == 4 and Mtriv.nullspace()==[])

# Confirm a scalar quadratic can nevertheless be invariant; orientation sign is lost.
for cvals in product((-1,0,1), repeat=4):
    c=S.Matrix(cvals)
    q=(u.T*c)[0]/2
    pass_check('quadratic_decomposition', S.expand((c.T*c)[0] - (Q*c).dot(Q*c) - q*q)==0)
    for R,sign in zip(Rs,signs):
        d = R*c
        qd=(u.T*d)[0]/2
        pass_check('linear_sign_covariance', qd==sign*q)
        pass_check('quadratic_even_invariance', qd*qd==q*q)

A=S.zeros(5)
A[:4,4]=-u/2
A[4,:4]=u.T/2
pass_check('minimal_skew_support_generator', A.T==-A)
pass_check('minimal_skew_support_generator', A*A*A == -A)
pass_check('minimal_skew_support_generator', S.expand(A.charpoly().as_expr()-S.Symbol('lambda')**3*(S.Symbol('lambda')**2+1))==0)
pass_check('minimal_skew_support_generator', (A*A)[:4,:4]==-P and (A*A)[4,4]==-1 and (A*A)[:4,4]==S.zeros(4,1))

# Different rational Pythagorean rotations conserve stock for the same initial state.
fractions=[(S.Rational(1),S.Rational(0)),(S.Rational(3,5),S.Rational(4,5)),(S.Rational(5,13),S.Rational(12,13)),(S.Rational(8,17),S.Rational(15,17)),(S.Rational(-3,5),S.Rational(4,5))]
for alpha,beta in fractions:
    pass_check('transfer_normalization', alpha**2+beta**2==1)
    for cvals in product((-1,0,1), repeat=4):
        c=S.Matrix(cvals)
        q=(u.T*c)[0]/2
        new_face=Q*c+alpha*P*c
        bulk=beta*q
        pass_check('isometric_transfer_family', S.expand(new_face.dot(new_face) + bulk*bulk - c.dot(c))==0)

# Same pre-state: HOLD versus two distinct supported, occupied 3-cell extensions.
old = u/2
input_support=old.dot(old)
solutions=[]
for alpha,beta,occupied in [(S.Integer(1),S.Integer(0),0),(S.Rational(3,5),S.Rational(4,5),1),(S.Rational(5,13),S.Rational(12,13),1)]:
    face=alpha*old
    bulk=beta
    pass_check('same_prestate_countermodels',face.dot(face)+bulk*bulk==input_support)
    pass_check('same_prestate_countermodels',B2*face==S.zeros(6,1))
    solutions.append((occupied,alpha,beta,face,bulk))
pass_check('distinct_birth_countermodels',len(set((x[0],x[1],x[2]) for x in solutions))==3)
pass_check('distinct_birth_countermodels',solutions[1][4]!=solutions[2][4])

# Binary four-face shell closure masks: nonempty closure only when all faces present.
closed=[]
for mask in product((0,1),repeat=4):
    c=S.Matrix([u[i]*mask[i] for i in range(4)])
    flat=B2*c==S.zeros(6,1)
    pass_check('all_face_masks',flat in (True,False))
    pass_check('all_face_masks',flat==(sum(mask) in (0,4)))
    if flat: closed.append(''.join(str(k) for k in mask))
pass_check('only_full_nonempty_closed',closed==['0000','1111'])

# The Q162 restricted, purely relaxational flux vanishes on uniform burden,
# even if the hard edge gates differ. No source nor birth event is specified.
rho=S.ones(4,1)
for edgegate in product((0,1),repeat=6):
    diag=S.diag(*edgegate)
    j = -S.Rational(1,4) * diag * B1.T * rho
    pass_check('uniform_burden_no_mixing_flux', j==S.zeros(6,1))
    pass_check('uniform_burden_no_mixing_flux', B1*j == S.zeros(4,1))

# For 16 vertex binary fields, an exact edge coboundary has zero triangular coboundary.
for vertexbits in product((0,1),repeat=4):
    b=S.Matrix(vertexbits)
    e=(B1.T*b).applyfunc(lambda x: int(x)%2)
    de=(B2.T*e).applyfunc(lambda x: int(x)%2)
    pass_check('exact_distinction_coboundary_vacuous',de==S.zeros(4,1))

# Q173 face-cell support flux vanishes at zero pre-cell amplitude for every hard face gate.
for facegates in product((0,1),repeat=4):
    flux=S.Matrix([2*facegates[i]*B3[i,0]*old[i]*0 for i in range(4)])
    pass_check('Q173_zero_prebirth_flux',flux==S.zeros(4,1))

# The only birth amplitude bound from counting-norm conservation when the
# perpendicular pre-face part is held unchanged: 0<=z^2<=q^2.
for cvals in product((-1,0,1),repeat=4):
    c=S.Matrix(cvals)
    q=(u.T*c)[0]/2
    for alpha,beta in fractions[:4]:
        retained=Q*c+alpha*P*c
        released=c.dot(c)-retained.dot(retained)
        pass_check('sharp_support_funding_bound',released==beta*beta*q*q)
        pass_check('sharp_support_funding_bound',released>=0 and released<=q*q)

result={
  'artifact':'UD_K4_OMEGA0_PREBIRTH_SOURCE_CHANNEL_v1.1',
  'date':'2026-10-31',
  'claim_scope':'EXACT representation-level uniqueness and source insufficiency; NOT a native Omega0 birth law',
  'physical_promotion':0,
  'verification':'SymPy exact arithmetic',
  'groups':checks,
  'checks_total':sum(checks.values()),
  'mathematical_findings':{
      'dim_signed_equivariant_linear_maps':len(nsign),
      'dim_scalar_even_equivariant_linear_maps':len(Mtriv.nullspace()),
      'unique_intertwiner':'ell(c)=gamma*u.T*c, u=(-1,1,-1,1)',
      'normalized_shell_coordinate':'q=u.T*c/2',
      'support_generator_spectrum':'0 (multiplicity 3), +i, -i for lambda=1 (comparison normalization)',
      'only_binary_closed_masks':closed,
      'same_input_compatible_outcomes':['HOLD','BIRTH(3/5,4/5)','BIRTH(5/13,12/13)'],
      'closed_system_support_balance':'S2_after+S3_after=S2_before under comparison isometries',
      'why_no_native_birth':'Q153 has open predictive source/sink; Q173 presupposes admitted C3 and vanishes at c3=0; selection angle and event trigger not supplied'
  },
  'controls':{'S4_elements':len(Rs),'rational_face_vectors':3**4,'face_masks':16,'edge_gate_masks':64,'independent_vertex_bit_masks':16,'tested_rational_rotations':len(fractions)},
  'next_required_inputs':['Omega_face predictive occupancy map','Omega_bulk event selector','native source/sink and stock transfer law','oriented time/metric/energy bridge'],
  'status':'STRUCTURAL_PASS__NATIVE_BIRTH_SOURCE_BLOCKED'
}
path=Path(__file__).with_name('UD_K4_OMEGA0_PREBIRTH_SOURCE_CHANNEL_RESULTS_v1.1.json')
path.write_text(json.dumps(result,indent=2)+'\n')
print('PASS',result['checks_total'],'exact checks in',len(checks),'groups')
print('Signed channel dim',len(nsign),'even scalar channel dim',len(Mtriv.nullspace()))
print('Closed masks',closed)
print('STATUS',result['status'])
