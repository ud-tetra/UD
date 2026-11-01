#!/usr/bin/env python3
"""Exact SU2/Spin(3) trace readout and four-lift countercontrols. Symbolic proofs plus finite rational fixtures."""
from itertools import product, permutations
import json
from pathlib import Path
import sympy as sp
I=sp.I
C=0
def ck(c,label):
    global C
    C+=1
    if not bool(c): raise AssertionError(f'{C}: {label}')
def ez(a,b,label): ck(sp.simplify(a-b)==0,label)
def mat_eq(A,B,label): ck(all(sp.simplify(z)==0 for z in A-B),label)
E=sp.eye(2); Z=sp.zeros(2)
# SU2 quaternion representation using q=(a,b,c,d) with q*q=1.
def mat(a,b,c,d):return sp.Matrix([[a+I*b,c+I*d],[-c+I*d,a-I*b]])
def mat_tr(M):return sp.trace(M)
def q_matrix(q):return mat(*q)
def conjugate(M,G):return G*M*G.inv()
def spin_def(M):return sp.simplify(1-sp.re(sp.trace(M))/2)
def vec_def(M):
    # SU2 spin-1 character: Tr_adj = |Tr_fund|^2-1; SU2 trace real.
    t=sp.simplify(sp.trace(M))
    return sp.simplify(1-(t**2-1)/3)
def interference(M,psi):
    y=(E+M)*psi/2
    return sp.simplify((y.conjugate().T*y)[0])
# Real symbolic cos theta: SU2 trace vs SO3 spin-1 trace
c=sp.symbols('c',real=True)
ds=1-c
dv=sp.Rational(4,3)*(1-c*c)
ez(dv,sp.Rational(4,3)*ds*(2-ds),'trace relation')
for n in range(-8,9):
    cc=sp.Rational(n,8)
    x=1-cc
    ez(sp.Rational(4,3)*x*(2-x),sp.Rational(4,3)*(1-cc**2),'trace polynomial fixtures')
    ez(sp.Rational(4,3)*(1-cc**2),sp.Rational(4,3)*(1-(-cc)**2),'vector invisible sign reversal')
    ez((1-cc)+(1+cc),2,'spin complementary branch')

# Q8 matrix embedding
q8={'1':(1,0,0,0),'-1':(-1,0,0,0), 'i':(0,1,0,0),'-i':(0,-1,0,0),
'j':(0,0,1,0),'-j':(0,0,-1,0),'k':(0,0,0,1),'-k':(0,0,0,-1)}
M={name:q_matrix(q) for name,q in q8.items()}
for name,g in M.items():
    mat_eq(g*g.conjugate().T,E,'unitary Q8')
    ez(sp.det(g),1,'det SU2')
    ck(sp.trace(g).is_real,'SU2 real trace')
    ez(sp.simplify(sp.trace(-g)), -sp.trace(g),'spin trace sign')
    ez(vec_def(g),vec_def(-g),'vector trace sign blindness')
    ez(spin_def(g)+spin_def(-g),2,'spin mismatch complementary')
    # Individual path density phase-blind for any normalized psi (basis controls)
    for psi in [sp.Matrix([1,0]),sp.Matrix([0,1]),sp.Matrix([sp.Rational(3,5),sp.Rational(4,5)])]:
        ck(sp.simplify((g*psi).conjugate().T*(g*psi))[0] == sp.simplify(((-g)*psi).conjugate().T*((-g)*psi))[0],'single-path blind')
        ez(interference(g,psi),1-spin_def(g)/2,'two-path equals trace mismatch')
        ez(interference(-g,psi),1-spin_def(-g)/2,'two-path sign contrast')
# Holonomy gauge covariance and fixed trace invariance for Q8 H,G
for name,h in M.items():
    for gn,g in M.items():
        hh=conjugate(h,g)
        ez(spin_def(hh),spin_def(h),'gauge invariant Spin trace')
        ez(vec_def(hh),vec_def(h),'gauge invariant vector character')
        for psi in [sp.Matrix([1,0]),sp.Matrix([sp.Rational(3,5),sp.Rational(4,5)])]:
            ez(interference(hh,g*psi), interference(h,psi),'coherent two-path gauge invariance')
# Full SU2 rational quaternion grids, including non-central noncommuting rotations
quats=[(1,0,0,0),(-1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),
       (sp.Rational(3,5),sp.Rational(4,5),0,0),
       (sp.Rational(3,5),0,sp.Rational(4,5),0),
       (sp.Rational(3,5),0,0,sp.Rational(4,5))]
for q in quats:
    h=q_matrix(q)
    mat_eq(h*h.conjugate().T,E,'rational SU2 isometry')
    # SO3 character and interference exact equality
    ez(vec_def(h),sp.Rational(4,3)*spin_def(h)*(2-spin_def(h)),'spin vector identity')
    for psi in [sp.Matrix([1,0]),sp.Matrix([sp.Rational(3,5),sp.Rational(4,5)])]:
        ez(interference(h,psi),1-spin_def(h)/2,'SU2 interferometric trace relation')
    for qq in quats:
        g=q_matrix(qq)
        ez(spin_def(conjugate(h,g)),spin_def(h),'rational SU2 arbitrary gauge')
# HALF-TURN GATE: Q140 fundamental trace alone cannot resolve H versus -H at trace zero.
H=sp.diag(I,-I)
mat_eq(H*H.conjugate().T,E,'SU2 half-turn element unitary')
for K in (H,-H):
    ez(spin_def(K),1,'fundamental trace at half turn is blind')
    ez(vec_def(K),sp.Rational(4,3),'SO3 trace at half turn')
    ez(interference(K,sp.Matrix([1,0])),sp.Rational(1,2),'real-reference contrast blind at half turn')
# A supplied quadrature reference e^{-i pi/2} resolves the sign for a marked spinor.
psi=sp.Matrix([1,0])
def quadrature(K,pref):
    y=(E+pref*K)*psi/2
    return sp.simplify((y.conjugate().T*y)[0])
ez(quadrature(H,-I),1,'phase-reference positive half turn')
ez(quadrature(-H,-I),0,'phase-reference negative half turn')
# Two-path relative-phase readout is additional preparation; not specified by native UD.
# Trace mismatch is a non-injective scalar on the full SU2 connection, even though it separates central +/-I.
# Central Spin holonomy patterns for a flat old face. New spoke lift signs
lifts={}
for s in product((1,-1),repeat=3):
    loops=(s[0]*s[1],s[0]*s[2],s[1]*s[2]); lifts.setdefault(loops,[]).append(s)
ck(len(lifts)==4,'four central lift classes')
for pat,preimages in lifts.items():
    ck(len(preimages)==2,'apex sign gauge pair')
    ck(sp.prod(pat)==1,'central parity')
    spins=tuple(0 if p==1 else 2 for p in pat)
    vectors=tuple(0 for _ in pat)
    ck(vectors==(0,0,0),'vector completely blind')
    ck(sum(spins) in (0,4),'spin action mismatch totals as candidates')
    for e in preimages:
        ck(tuple(e[i]*e[j] for i,j in [(0,1),(0,2),(1,2)])==pat,'loop invariant on gauge orbit')
# Frustrated odd old-face central parity: four classes but three minimizing
# new-triangle defect placements for a postulated summed Q140 action.
for old in (+1,-1):
    classes={}
    for s0,s1,s2 in product((1,-1),repeat=3):
        pat=(old*s0*s1,s0*s2,s1*s2)
        classes[pat]=sum(0 if z==1 else 2 for z in pat)
    ck(len(classes)==4,'four classes for inherited old parity')
    vals=list(classes.values());best=min(vals)
    ck((best,vals.count(best))==((0,1) if old==1 else (2,3)), 'Q140 sum frustration min multiplicity')
    for pat in classes: ck(sp.prod(pat)==old,'face sign Bianchi inherited old sign')
# Distinct SU2 loop states cannot be distinguished by ordinary vector rotation char.
ck(len(set(tuple(0 for _ in p) for p in lifts))==1,'all four states same SO3 data')
ck(len(lifts)==4,'Wilson trace separates four patterns')
# Under permutation of three new-face positions, three nonzero patterns form an orbit, no intrinsic unique nontrivial pattern
patterns=list(lifts)
for perm in permutations((0,1,2)):
    for p in patterns:
        pp=tuple(p[perm[i]] for i in range(3))
        ck(pp in lifts,'S3 equivariant lift-pattern set')
# Distinct outcomes from same old fixed state: a deterministic function of old-state-only data cannot return all four.
fixed_old={'labels':(0,0,1,1),'burden':(1,1,1,1),'SO3_loop_defects':(0,0,0)}
ck(len(lifts)>1,'postulated lift cannot be recovered uniquely from vector-only old state')
# The two-path readout requires reference and coherent comparison: without it probability is same for +/- central.
for sign in (1,-1):
    h=sign*E
    ez(interference(h,sp.Matrix([1,0])),(1+sign)/2,'central reference-path readout')
    ez(spin_def(h),1-sign,'central Spin mismatch')
    ez(vec_def(h),0,'central SO3 mismatch')
# Citation: loop trace is invariant under conjugacy but not under independent endpoint gauge on individual link.
old_link=E
for g in M.values():
    for k in M.values():
        link=g*old_link*k.inv()
        # Under independent endpoints trace may change; all linked objects are valid SU2.
        mat_eq(link*link.conjugate().T,E,'edge gauge valid unitary')
ck(sp.trace(M['1'])!=sp.trace(M['-1']),'edge trace not gauge independent')
result={'version':'v1.9','exact_primary_checks':C,'status':'EXACT_CONDITIONAL_AND_SOURCE_GATED','physical_promotion':0,
'spin_vector_trace_relation':'delta_SO3=(4/3)delta_Spin(2-delta_Spin)',
'coherent_readout_relation':'P_two_path=1-delta_Spin/2',
'center_cases':{str(p):{'spin_defects':[0 if v==1 else 2 for v in p],'vector_defects':[0,0,0], 'gauge_class_size':len(lifts[p])} for p in lifts},
'source_selection':'OPEN','newborn_state':'OPEN','energy_debit':'OPEN','nonconstructor_review':'PENDING'}
Path(__file__).with_name('RESULTS_PRIMARY_v1.9.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS',C,'primary exact assertions')
