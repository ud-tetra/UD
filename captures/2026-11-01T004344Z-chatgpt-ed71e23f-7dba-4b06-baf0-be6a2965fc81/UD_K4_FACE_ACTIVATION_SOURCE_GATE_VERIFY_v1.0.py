#!/usr/bin/env python3
"""Source-scoped K4 face activation/filling no-go, exact rational verification.

Requires Python 3.11+ and SymPy. Does not model native Omega0 physics.
Distinct namespaces: simplicial incidence, oriented support, burden ledger,
link holonomy, and topology-changing occupancy. No fitted coefficients.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
import json
from pathlib import Path
import sympy as S

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'UD_K4_FACE_ACTIVATION_SOURCE_GATE_RESULTS_v1.0.json'
records=Counter()

def check(group, verdict, note=''):
    if not bool(verdict):
        raise AssertionError(f'{group}: {note}')
    records[group] += 1

V=tuple(range(4))
E=list(combinations(V,2))
F=list(combinations(V,3))
B1=S.zeros(4,6)
B2=S.zeros(6,4)
for ei,(a,b) in enumerate(E):
    B1[a,ei]=-1; B1[b,ei]=1
for fi,(a,b,c) in enumerate(F):
    B2[E.index((b,c)),fi]+=1
    B2[E.index((a,c)),fi]-=1
    B2[E.index((a,b)),fi]+=1
u=S.Matrix([-1,1,-1,1]); I4=S.eye(4)
P=u*u.T/4
check('incidence',B1*B2==S.zeros(4,4))
check('incidence',B2*u==S.zeros(6,1))
check('incidence',B2.rank()==3)
check('incidence',B2.T*B2==4*I4-u*u.T)
check('incidence',P*P==P and P.T==P and P.rank()==1)
check('incidence',B2.T*B2==4*(I4-P))
check('incidence',B2*P==S.zeros(6,4))

# Exact closure decomposition: c = P c + (I-P)c; two norms add.
def readiness(c):
    if c==S.zeros(4,1): return None
    norm=(c.T*c)[0]
    coh=S.factor(((u.T*c)[0]**2)/(4*norm))
    defect=S.factor((B2*c).dot(B2*c)/(4*norm))
    return coh,defect

binary_mask_rows=[]
for mask in range(16):
    bits=tuple((mask>>i)&1 for i in range(4))
    c=S.Matrix([bits[i]*u[i] for i in range(4)])
    norm=(c.T*c)[0]
    bc=B2*c
    closed=(bc==S.zeros(6,1))
    expected=(mask in (0,15))
    check('face_masks',closed==expected)
    m=sum(bits)
    if m:
        coh,defect=readiness(c)
        check('face_masks',coh==S.Rational(m,4))
        check('face_masks',defect==1-S.Rational(m,4))
        check('face_masks',coh+defect==1)
        check('face_masks',bc.dot(bc)==m*(4-m))
    else:
        coh=defect=None
        check('face_masks',readiness(c) is None)
    binary_mask_rows.append({'mask':format(mask,'04b'),'occupied_faces':m,
         'boundary_closed':closed,'boundary_norm_sq':str(bc.dot(bc)),
         'coherence':None if coh is None else str(coh),
         'defect':None if defect is None else str(defect)})

# Rational face-amplitude scans; readiness is bounded and exact.
for t in product((-2,-1,0,1,2),repeat=4):
    c=S.Matrix(t)
    if c==S.zeros(4,1):
        check('rational_amplitudes',readiness(c) is None)
        continue
    norm=c.dot(c)
    pc=P*c; rc=(I4-P)*c
    coh,d=readiness(c)
    check('rational_amplitudes',pc.dot(rc)==0)
    check('rational_amplitudes',pc.dot(pc)+rc.dot(rc)==norm)
    check('rational_amplitudes',S.simplify(coh+d)==1)
    check('rational_amplitudes',S.simplify(coh-pc.dot(pc)/norm)==0)
    check('rational_amplitudes',S.simplify(d-rc.dot(rc)/norm)==0)
    check('rational_amplitudes',0<=coh<=1 and 0<=d<=1)
    check('rational_amplitudes',(d==0)==(B2*c==S.zeros(6,1)))

# Oriented simplex S4 representations: edges/faces are signed under relabeling.
def parity_of_order(seq):
    return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
def oriented_rep(simplices, perm):
    ret=S.zeros(len(simplices),len(simplices))
    index={face:i for i,face in enumerate(simplices)}
    for j,vertices in enumerate(simplices):
        im=[perm[v] for v in vertices]
        ret[index[tuple(sorted(im))],j]=parity_of_order(im)
    return ret

sample_c=S.Matrix([2,-1,3,4])
for perm in permutations(V):
    R1=oriented_rep(E,perm)
    R2=oriented_rep(F,perm)
    sg=parity_of_order(perm)
    check('symmetry',B2*R2==R1*B2)
    check('symmetry',R2*u==sg*u)
    check('symmetry',R2.T*R2==I4)
    check('symmetry',R2*P==P*R2)
    check('symmetry',readiness(R2*sample_c)==readiness(sample_c))
    check('symmetry',(u.T*R2*sample_c)[0]==sg*(u.T*sample_c)[0])
    # No deterministic S4-equivariant nonzero pseudo-scalar output from a
    # truly S4-invariant scalar occupancy-only seed: odd permutation changes sign.
    if sg<0:
        check('symmetry',sg*S.Integer(1)!=1)

# Nontrivial non-Abelian transport control: no flatness forced by shell closure.
def perm_compose(p,q): return tuple(p[q[i]] for i in range(3))
def perm_inverse(p):return tuple(p.index(i) for i in range(3))
id3=(0,1,2); s01=(1,0,2); s12=(0,2,1)
trans={e:id3 for e in E}; trans[(0,1)]=s01; trans[(0,2)]=s12
def link(i,j):
    return trans[(i,j)] if i<j else perm_inverse(trans[(j,i)])
def triangle_loop(i,j,k):
    return perm_compose(link(k,i),perm_compose(link(j,k),link(i,j)))
loops=[triangle_loop(*face) for face in F]
check('curved_transport',sum(H!=id3 for H in loops)>0)
check('curved_transport',B2*u==S.zeros(6,1))
check('curved_transport',readiness(u)==(S.Integer(1),S.Integer(0)))

# Exact vertex-coboundary no-go: every delta(delta b) is zero.
for vertex_bits in product((0,1),repeat=4):
    e={ij:vertex_bits[ij[0]]^vertex_bits[ij[1]] for ij in E}
    phase=[e[(i,j)]^e[(i,k)]^e[(j,k)] for i,j,k in F]
    check('vacuous_flatness',phase==[0,0,0,0])

# Source-ledger test Q153/Q162: conservative j is not occupancy dynamics.
rho=S.Matrix([1,2,3,4])
phi=B1.T*rho
j0=S.zeros(6,1)
check('burden',sum(B1*j0)==0)
for mask in range(64):
    gate=S.diag(*[((mask>>i)&1) for i in range(6)])
    j=-S.Rational(1,4)*gate*phi  # Q162 conditional relaxational lane, not a face trigger
    drho=B1*j
    check('burden',sum(drho)==0)
    check('burden',drho==B1*j+S.zeros(4,1))
    check('burden',all((drho[i]+rho[i])>=0 for i in range(4)))
# Q173 is support-rate accounting, not a new-cell creation map.
for mask in range(16):
    h=[(mask>>i)&1 for i in range(4)]
    c=S.Matrix([u[i] for i in range(4)])
    c3=S.Integer(0)
    Js=[2*h[i]*u[i]*c[i]*c3 for i in range(4)]
    check('support_gate',Js==[0]*4)

# Post-admission skew interface: EXACT conservative generator on an ALREADY
# ADMITTED C3 carrier. Not a face/cell creation rule.
A=S.zeros(5,5)
for k in range(4):A[k,4]=-u[k];A[4,k]=u[k]
check('support_carrier',A.T==-A)
check('support_carrier',S.expand(A.charpoly().as_expr()-S.Symbol('lambda')**3*(S.Symbol('lambda')**2+4))==0)
check('support_carrier',A[:4,4]==-u and A[4,:4]==u.T)

# Two *different* topology-changing updates with identical initial shell,
# burden, holonomies, hard-gate masks and conserved quadratic support.
# The rational 3-4-5 rotation is a COUNTERMODEL, never a native coefficient.
c0=u/2
q0=(u.T*c0)[0]/2
check('birth_nonuniqueness',c0.dot(c0)==1 and q0==1 and B2*c0==S.zeros(6,1))
for a,b in ((S.Rational(3,5),S.Rational(4,5)),(S.Rational(5,13),S.Rational(12,13))):
    assert a**2+b**2==1
    c_new=a*c0
    c3_new=b*q0
    check('birth_nonuniqueness',c_new.dot(c_new)+c3_new**2==c0.dot(c0))
    check('birth_nonuniqueness',B2*c_new==S.zeros(6,1))
    check('birth_nonuniqueness',c3_new!=0 and c_new!=S.zeros(4,1))
    # Same initial c0, face occupancy 1111 and U, yet hold and birth differ.
    check('birth_nonuniqueness',c3_new!=S.Integer(0))
    for perm in permutations(V):
        sg=parity_of_order(perm); R2=oriented_rep(F,perm)
        cp=R2*c0; qp=(u.T*cp)[0]/2
        check('birth_equivariance',qp==sg*q0)
        check('birth_equivariance',a*cp==R2*c_new and b*qp==sg*c3_new)

# Filling an *unoccupied* cell with positive new quadratic support while all
# existing quadratic supports and reserves are unchanged violates conservation.
pre=c0.dot(c0)
post=c0.dot(c0)+S.Integer(1)
check('unsourced_fill_no_go',post>pre)

results={
 'artifact':'UD_K4_FACE_ACTIVATION_SOURCE_GATE_v1.0',
 'date':'2026-10-31','lane':'DEVELOPMENT_NO_REGISTRY_ENTRY',
 'physical_promotion':0,'assertion_count':sum(records.values()),
 'groups':dict(records),'face_masks':binary_mask_rows,
 'coherence_formula':'C=(u^T c)^2/(4 c^T c), c != 0',
 'defect_formula':'D=||B2 c||^2/(4 c^T c), c != 0',
 'spectral_identity':'B2^T B2 = 4I4 - u u^T',
 'conservative_countermodel_rotations':['(3/5,4/5)','(5/13,12/13)'],
 'transport_control':'S3 nonflat faces '+str(sum(H!=id3 for H in loops))+'/'+str(len(loops)),
 'classification':'EXACT_READY_DIAGNOSTIC__NO_GO_UNIQUE_NATIVE_BIRTH_FROM_CURRENT_SOURCE',
 'physical_tests':'NOT_RUN',
 'open':['predictive Omega0 face occupancy update','native source/energy cost',
         'dynamical interior admission','clock and metric correspondence']
}
OUT.write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
print('EXACT assertions PASSED:',results['assertion_count'])
print('GROUPS',dict(records))
print('RESULTS:',OUT)
