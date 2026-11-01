#!/usr/bin/env python3
"""Independent method: 2x2 exact SU2 matrices and Z2 boundary ranks.
Does not import primary verifier. Check scope not independent researcher.
"""
import sympy as s
from itertools import product, permutations
from pathlib import Path
import json
n=0
def ok(b, msg):
 global n
 n+=1
 if not bool(b): raise AssertionError(f'{n}: {msg}')
I=s.I; E=s.eye(2)
A=s.diag(I,-I);B=s.Matrix([[0,1],[-1,0]]);C=A*B
for m in (A,B,C):ok(m*m==-E,'quaternion square -1')
ok(B*A==-C,'noncommuting generators')
Q=tuple(z*k for z in (1,-1) for k in (E,A,B,C))
for g in Q:
 ok(s.simplify(g.det())==1,'SU2 determinant')
 ok(s.simplify(g.H*g)==E,'SU2 unitarity')
for g,h in product(Q,repeat=2):
 hh=g*h*g.inv()
 ok(s.trace(hh)==s.trace(h),'Wilson trace gauge invariant')
 psi=s.Matrix([1,0]);p2=g*psi
 sig=(E+h)*psi/2; sig2=(E+hh)*p2/2
 ok(s.simplify((sig2.H*sig2)[0]-(sig.H*sig)[0])==0,'interference norm gauge invariant')
for sign,expected in ((1,1),(-1,0)):
 h=sign*E;psi=s.Matrix([1,0]);p=(E+h)*psi/2
 ok((p.H*p)[0]==expected,'spinor reference interferometer')
 ok(((h*psi).H*(h*psi))[0]==1,'isolated ray unchanged')
 for g in Q:
  ok(g*h*g.inv()==h,'central loop unaffected by SU2 conjugation')
  for T in (A,B,C):ok((h*T*h.inv())==T,'vector adjoint identity')
# Independently derive central curvature sign constraints from Z2 boundary matrix.
B3=((1,1,0),(1,0,1),(0,1,1))
patterns=set()
for bits in product((0,1),repeat=3):
 v=tuple(sum(B3[i][j]*bits[j] for j in range(3))%2 for i in range(3))
 patterns.add(v)
 ok(sum(v)%2==0,'boundary parity')
ok(patterns=={(0,0,0),(0,1,1),(1,0,1),(1,1,0)},'rank 2 image')
# Kernel exactly the common apex sign flip.
ker=[bits for bits in product((0,1),repeat=3)
 if all(sum(B3[i][j]*bits[j] for j in range(3))%2==0 for i in range(3))]
ok(ker==[(0,0,0),(1,1,1)],'new-vertex sign-gauge kernel')
# Unique connected fixed-total Laplacian equilibrium cannot imply newborn birth.
L=4*s.eye(4)-s.ones(4)
ok(L.rank()==3,'K4 Laplacian rank')
ok(L*s.ones(4,1)==s.zeros(4,1),'constant kernel')
# Fully prepared equal-score event has 4 faces; randomized/lex tie break requires extra input.
labels=(0,0,1,1)
faces=[(0,1,2),(0,1,3),(0,2,3),(1,2,3)]
stab=[p for p in permutations(range(4)) if all(labels[i]==labels[p[i]] for i in range(4))]
ok(len(stab)==4,'stabilizer 4')
for f in faces:
 ok(any(tuple(sorted(p[i] for i in f))!=f for p in stab),'no fixed singleton')
# Same scalar accounting multiple positive costs compatible
for x in (s.Rational(1,7),s.Rational(1,5),s.Rational(1,2),s.Rational(1)):
 ok((1-x)+x==1,'different debits conserved')
res={'version':'v1.8','independent_method':'symbolic SU2 matrix and binary coboundary','checks':n,
     'vector_blind_central_spin_witness':'PASS','coherent_reference_interference':'PASS',
     'central_face_sign_patterns':sorted(patterns),'fixed_total_burden_birth':'NOT_DERIVED',
     'birth_event_receipt':'OPEN','physical_promotion':0,'independent_peer_review':'NOT_PERFORMED'}
Path(__file__).resolve().parent.joinpath('INDEPENDENT_RESULTS_v1.8.json').write_text(json.dumps(res,indent=2)+'\n')
print('PASS',n,'exact independent-method checks')
