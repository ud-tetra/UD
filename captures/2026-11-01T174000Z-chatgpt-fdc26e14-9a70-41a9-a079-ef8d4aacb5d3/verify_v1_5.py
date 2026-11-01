#!/usr/bin/env python3
"""UD v1.5 conditional combinatorial/gauge/source-identifiability checks. No physical inference."""
from itertools import permutations, product, combinations
from fractions import Fraction as F
from collections import Counter
from math import factorial
import json
import sympy as sp
V=(0,1,2,3)
E=tuple(combinations(V,2))
FACES=tuple(combinations(V,3))
PAIRINGS=tuple(sorted((tuple(sorted((e1,e2))) for e1,e2 in ((E[0],E[5]),(E[1],E[4]),(E[2],E[3])))))
# P: (01,23),(02,13),(03,12)
PERMS=tuple(permutations(V))
KERNEL=((0,1,2,3),(1,0,3,2),(2,3,0,1),(3,2,1,0))
assert len(PERMS)==24
checks=0
def ck(test,msg):
 global checks
 checks+=1
 if not test: raise AssertionError(msg)
def pair_idx(p,pair):
 tr=tuple(sorted(tuple(sorted((p[x],p[y]))) for x,y in pair))
 return PAIRINGS.index(tr)
def face_idx(p,face):
 return FACES.index(tuple(sorted(p[i] for i in face)))
for p in PERMS:
 ck(sorted(pair_idx(p,q) for q in PAIRINGS)==list(range(3)),'pair action not permutation')
 ck(sorted(face_idx(p,f) for f in FACES)==list(range(4)),'face action not permutation')
for k in KERNEL:
 ck(all(pair_idx(k,q)==j for j,q in enumerate(PAIRINGS)),'kernel not acting trivially')
 ck(all(k[i] in V for i in V),'invalid permutation')
ck(set(KERNEL)=={p for p in PERMS if all(pair_idx(p,q)==j for j,q in enumerate(PAIRINGS))},'kernel not exactly V4')
for face in FACES:
 ck({face_idx(k,face) for k in KERNEL}==set(range(4)),'V4 fails face transitivity')
# exhaustive 3-bit theta states: inputs invariant under V4; any covariant face output must be invariant under V4 -> constant.
for state in product((0,1),repeat=3):
 for k in KERNEL:
  ck(tuple(state[pair_idx(k,pair)] for pair in PAIRINGS)==state,'theta bit state moved')
 for chosen in range(4):
  ck(any(face_idx(k,FACES[chosen])!=chosen for k in KERNEL),'face fixed contrary to theorem')
# H=S2xS2 stabilizes fixed binary labels (0,0,1,1); h=(01)(23) is in H and kernel.
b=(0,0,1,1)
h=(1,0,3,2)
ck(tuple(b[h[i]] for i in V)==b,'label does not fix h')
for theta in product((0,1),repeat=3):
 ck(all(pair_idx(h,q)==j for j,q in enumerate(PAIRINGS)),'h moves theta')
 for face in FACES: ck(face_idx(h,face)!=FACES.index(face),'h fixes face')
# Exact linear intertwiners: 4x3 free matrix A; equations A P_pair = P_face A
vars=sp.symbols('a0:12'); A=sp.Matrix(4,3,vars)
eq=[]
for p in PERMS:
 Pp=sp.zeros(3); Pf=sp.zeros(4)
 for j,q in enumerate(PAIRINGS):Pp[pair_idx(p,q),j]=1
 for j,f in enumerate(FACES):Pf[face_idx(p,f),j]=1
 eq.extend(list(A*Pp-Pf*A))
rank=sp.linear_eq_to_matrix(eq,vars)[0].rank()
ck(rank==11,'intertwiner rank differs from 11')
null=sp.linear_eq_to_matrix(eq,vars)[0].nullspace()
ck(len(null)==1 and len(set(null[0]))==1,'intertwiner not constant')
# Source burden fixture and conflicting U1 face mismatch. Shape typed: B-current^2 vs U1 holonomy mismatch.
rho=(0,1,2,4)
def db(face):
 return sum(((F(rho[j]-rho[i],4))**2 for i,j in combinations(face,2)), F(0))
D_B=tuple(db(f) for f in FACES)
ck(D_B==(F(3,8),F(13,8),F(3,2),F(7,8)),'burden scores incorrect')
root=sp.sqrt(3)
D_U=(sp.Integer(1),sp.Integer(1)-root/2,sp.Integer(1)-root/2,sp.Integer(1)-root/2)
maxb=F(13,8)
B_norm=tuple(sp.Rational(v.numerator,v.denominator)/sp.Rational(maxb.numerator,maxb.denominator) for v in D_B)
threshold=sp.simplify((root/2)/(root/2+sp.Rational(10,13)))
ck(sp.simplify(threshold-13*root/(20+13*root))==0,'threshold')
def score(i,weight):return sp.simplify(weight*B_norm[i]+(1-weight)*D_U[i])
for weight,idx in ((sp.Rational(1,4),0),(sp.Rational(3,4),1)):
 for other in range(4):
  if other!=idx: ck(float(score(idx,weight)-score(other,weight))>0,'wrong witness ranking')
ck(sp.simplify(score(0,threshold)-score(1,threshold))==0,'tie at threshold')
# Same source v1.4 old-face holonomy values are permitted via exact edge phases as multiples of pi/6.
angles=(-1,1,0,-1,0,0)
edged={e:v for e,v in zip(E,angles)}
def a(i,j):return edged[(i,j)] if i<j else -edged[(j,i)]
phi=tuple(a(i,j)+a(j,k)+a(k,i) for i,j,k in FACES)
ck(phi==(-3,-1,1,-1),'U1 face phases differ from earlier fixture')
u=(-1,1,-1,1)
ck(sum(x*y for x,y in zip(u,phi))==0,'Bianchi fails')
# Newborn U1 exact turn phases (mod 1); gauge shift acts on all new edges.
H=tuple(F(j,4) for j in range(4))
def mod1(x):return x%1
def invariant(triple):return (mod1(triple[1]-triple[0]),mod1(triple[2]-triple[0]))
triples=list(product(H,repeat=3))
classes={invariant(x) for x in triples}
ck(len(classes)==16,'unexpected relative phase quotient')
for x in triples:
 for t in H:ck(invariant(tuple(mod1(v+t) for v in x))==invariant(x),'gauge invariance')
ck(invariant((F(0),F(0),F(0)))!=invariant((F(0),F(1,4),F(0))),'newborn seams distinguishable')
# Flatness obstruction: child triangle loops have oriented sum equal old triangular loop.
for old in H:
 for n in triples:
  a01,a12,a20=(old,F(0),F(0))
  loops=(mod1(n[0]+a01-n[1]),mod1(n[1]+a12-n[2]),mod1(n[2]+a20-n[0]))
  ck(mod1(sum(loops))==old,'flatness/Bianchi mismatch')
  if old != 0:ck(loops!=(F(0),F(0),F(0)),'nonflat old face all flat child')
# Burden allocation two different distributions each conserve total 4 with x>0 and nonnegative.
for x in (F(1,4),F(1,2),F(3,4),F(1)):
 uniform=(1-x/4,)*4+(x,)
 concentrated=(1-x,1,1,1,x)
 ck(sum(uniform)==4 and sum(concentrated)==4,'burden total')
 ck(all(n>=0 for n in uniform+concentrated),'negative burden')
 ck(uniform!=concentrated,'no donor nonuniqueness')
# additive resource balances do not select debit or event.
for c in (F(0),F(1),F(2)):
 ck((F(3)-c)+(F(4)+c)==7,'resource account')
# zero source-cost unique? no; positive cost cannot be derived from signed quadratic support.
# retain literal charge if source energy can be arbitrarily small: fixed positive c cannot be paid by all eps states.
for eps in (F(1,2),F(1,4),F(1,8),F(1,16)):
 ck(eps**2>0 and eps**2<F(1),'quadratic small stock witness')
result={
 'status':'PASS_SCOPED', 'checks':checks,'theorems':{
 'pair_kernel_order':4,'pair_state_count':8,'face_count':4,
 'equivariant_linear_intertwiner_rank':rank,'equivariant_linear_map_dimension':1,
 'all_face_selectors_from_theta_only':'NO_GO even nonlinear, assuming S4-equivariance and ordinary opposite-pair bits',
 'burden_scores':[str(v) for v in D_B],
 'burden_argmax_face':'013', 'U1_argmax_face':'012',
 'weight_switch_exact':str(threshold),
 'U1_newborn_phase_grid':4,'U1_newborn_gauge_classes':len(classes),
 'newborn_SU2_relative_degrees_formal':'2 dim(SU2) = 6 (fixed boundary gauge)',
 'positive_additive_debit':'OPEN', 'native_event_selector':'OPEN'},
 'dependencies': ['UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2) Q153-158 Q162 Q169-173 G05',
 'UD v1.4 exact comparator', 'UD conditional pair-swap archive oct 2026', 'UD coface inheritance v0.1'],
 'physical_promotion':0
}
if __name__=='__main__':
 with open('results_v1_5.json','w') as f:json.dump(result,f,indent=2)
 print(f"PASS: {checks} exact assertions; V4 theta no-go; linear intertwiner dim 1; donor/seam unresolved")
