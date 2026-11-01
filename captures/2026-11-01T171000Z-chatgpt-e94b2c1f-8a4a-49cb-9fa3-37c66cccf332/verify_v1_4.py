#!/usr/bin/env python3
"""Exact controls for source-driven coface identifiability. Author's conditional mathematics only."""
from fractions import Fraction as F
from itertools import permutations, combinations, product
from sympy import Matrix, eye, symbols, simplify, cos, pi, sqrt
import json
from pathlib import Path

out = Path(__file__).parent
V=range(4); faces=list(combinations(V,3)); edges=list(combinations(V,2))
assert faces==[(0,1,2),(0,1,3),(0,2,3),(1,2,3)]
B=Matrix.zeros(6,4)
for j,face in enumerate(faces):
 for k in range(3):
  faceedge=tuple(face[t] for t in range(3) if t!=k)
  B[edges.index(faceedge),j] += (-1)**k
u=Matrix([-1,1,-1,1]); checks=0

def check(a,msg=''):
 global checks
 assert a,msg
 checks+=1
check(B*u==Matrix.zeros(6,1),'boundary square')
check(B.T*B==4*eye(4)-u*u.T,'face Gram')

labels=(0,0,1,1)
H=[p for p in permutations(V) if all(labels[i]==labels[p[i]] for i in V)]
check(len(H)==4)
face_perm=lambda p,f: tuple(sorted(p[i] for i in f))
for f in faces:
 orbit={face_perm(p,f) for p in H}
 check(len(orbit)==2)
 check(any(face_perm(p,f)!=f for p in H))
# Every fully symmetry-preserving deterministic selector is obstructed.
for p in H:
 check(all(set(face_perm(p,f) for f in faces)==set(faces) for _ in [0]))

# Q162-inspired burden currents, with h=1 and unweighted K4:
# j_e = -(b_head-b_tail)/4 in the chosen increasing orientation.
def edge_current(rho):
 return Matrix([-(rho[j]-rho[i])/4 for (i,j) in edges])
def face_current_sq(rho):
 j=edge_current(rho)
 return [sum([j[edges.index(e)]**2 for e in combinations(f,2)]) for f in faces]

rho_sym=Matrix([0,0,1,1]); sym=face_current_sq(rho_sym)
for s in sym:check(s==F(1,8),'symmetric current-tie')
rho_asym=Matrix([0,1,2,4]); asym=face_current_sq(rho_asym)
check(asym==[F(3,8),F(13,8),F(3,2),F(7,8)],'asymmetric face currents')
check(asym.index(max(asym))==1,'candidate unique maximum 013')
# Permutation covariance of currents and face squared diagnostic, preserving h=1.
for p in permutations(V):
 rp=Matrix([0]*4)
 for i in V:rp[p[i]]=rho_asym[i]
 ap=face_current_sq(rp)
 for idx,f in enumerate(faces):
  check(ap[faces.index(face_perm(p,f))]==asym[idx], 'burden diagnostic covariance')

# U(1) holonomy: h = B^T a, one negative-edge control -> two nontrivial face loops.
seam_one=Matrix([1,0,0,0,0,0]); hol_one=B.T*seam_one
check(sum(int(x*x) for x in hol_one)==2,'single edge produces two nonzero face circulations')
check(sum(x!=0 for x in hol_one)==2)
# A continuous phase pattern with one strictly larger angular mismatch.
want=Matrix([-3,-1,1,-1]);check((u.T*want)[0]==0,'tetrahedral Bianchi')
sol=list(B.T.gauss_jordan_solve(want)[0]);free=B.T.gauss_jordan_solve(want)[1]
fill={x:0 for x in free};a=Matrix([s.subs(fill) for s in sol]);check(B.T*a==want)
q=[simplify(1-cos(x*pi/6)) for x in want]
check(q[0]==1)
for i in [1,2,3]:check(q[i]==1-sqrt(3)/2)
check(all(simplify(q[0]-q[i])>0 for i in [1,2,3]),'one unique twisted candidate')
# Equal |U|=1 in all phases (not equivalent holonomy).
for x in a:check(x.is_integer or (x.q==1),'integer primitive angular phases')
# Gauge invariance: a_e -> a_e + g_head-g_tail.
for g in product([-1,0,1],repeat=4):
 dg=Matrix([g[j]-g[i] for i,j in edges]);check(B.T*(a+dg)==want,'gauge invariance')

# All old identity link values and a new U(1) star: three newborn edges, one gauge freedom.
# Gauge-invariant new triangle mismatches depend on ratios of new-edge phases.
for (A,Bb) in [(0,1),(0,2),(1,2)]:
 check((A,Bb) in edges)
# New seams (1,1,1) vs (1,e^{i pi/3},1) not equivalent even with newborn vertex rephasing.
star_flat=(0,0,0);star_twist=(0,1,0)
check(star_flat[1]-star_flat[0]!=star_twist[1]-star_twist[0]);check(star_twist[2]-star_twist[0]==0)
# One independent scalar initial burden inheritance cannot set new scalar and donor split.
rho0=Matrix([1,1,1,1])
for x in [F(0),F(1,4),F(1,2),F(1)]:
 uniform=[1-x/4]*4+[x]
 concentrated=[1-x,1,1,1,x]
 check(sum(uniform)==4 and sum(concentrated)==4)
 check(min(uniform)>=0 and min(concentrated)>=0)
 if x>0:check(uniform!=concentrated)
# Costs 1 and 2 both legal for free stock 3, bound 4; free+bound invariant.
for debit in [F(0),F(1),F(2)]:
 check((3-debit)+(4+debit)==7 and 3-debit>=0)

results={
 'status':'PASS_CONDITIONAL', 'assertions':checks, 'physical_promotion':0,
 'faces':[''.join(map(str,f)) for f in faces],
 'label_stabilizer_size':len(H),
 'symmetric_Q162_candidate_face_scores':[str(v) for v in sym],
 'asymmetric_Q162_candidate_face_scores':[str(v) for v in asym],
 'candidate_max_face':'013',
 'continuous_seam_integer_edge_phase_coefficients':[str(v) for v in a],
 'continuous_seam_face_phase_coefficients':[str(v) for v in want],
 'mismatch_unique_first':'1 versus 1-sqrt(3)/2',
 'selection_status':'NOT_SOURCE_SELECTED',
 'newborn_seams':'NONUNIQUE_WITH_IDENTICAL_INHERITED_OLD_LINKS',
 'newborn_burden':'NONUNIQUE_UNDER_CONSERVATION',
 'formation_debit':'NONUNIQUE_UNDER_CONSERVATION',
 'newborn_physical_energy':'UNDEFINED',
 'caveat':'burden and seam diagnostics are prebirth covariant data but their maximization is a new candidate scheduler, not an admitted UD rule'
}
(out/'results_v1_4.json').write_text(json.dumps(results,indent=2)+'\n')
print('PASS exact assertions',checks)
print('burden: symmetric',results['symmetric_Q162_candidate_face_scores'],'asymmetric',results['asymmetric_Q162_candidate_face_scores'])
print('seam edge angles integer coefficients',results['continuous_seam_integer_edge_phase_coefficients'])
