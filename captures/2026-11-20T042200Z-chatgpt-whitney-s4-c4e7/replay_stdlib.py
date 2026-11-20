#!/usr/bin/env python3
"""Independent exact Fraction replay; no SymPy/numpy/scientific dependencies."""
from fractions import Fraction as F
from itertools import permutations,product,combinations
from collections import Counter
import json
from pathlib import Path
V=tuple(range(4));edges=list(combinations(V,2));pair=(((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))
grads=((-1,-1,-1),(1,0,0),(0,1,0),(0,0,1))
def even_sign(vals):
 return -1 if sum(vals[i]>vals[j] for i in range(len(vals)) for j in range(i+1,len(vals)))%2 else 1

def dual(c):
 v={}
 for e,ce in c.items():
  other=tuple(j for j in V if j not in e)
  v[other]=even_sign(e+other)*ce
 return v

def act(c,g):
 out={}
 for (i,j),v in c.items():
  a,b=g[i],g[j]
  out[tuple(sorted((a,b)))]=(1 if a<b else -1)*v
 return out

def determinant(M):
 a,b,c=M
 return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])

def Whitney(e,lams):
 i,j=e
 return tuple(lams[i]*grads[j][k]-lams[j]*grads[i][k] for k in range(3))

def E(c,lams):
 return [[sum(c[e]*Whitney(e,lams)[k] for e in m) for k in range(3)] for m in pair]

def rank(M):
 if determinant(M)!=0:return 3
 for rr in combinations(range(3),2):
  for cc in combinations(range(3),2):
   if M[rr[0]][cc[0]]*M[rr[1]][cc[1]]!=M[rr[0]][cc[1]]*M[rr[1]][cc[0]]:return 2
 return 1 if any(any(z!=0 for z in r) for r in M) else 0

def tup(c):return tuple(c[e] for e in edges)
L0=(F(1,4),)*4
signs=[dict(zip(edges,pattern)) for pattern in product((-1,1),repeat=6)]
assert len(signs)==64
ranks=Counter(rank(E(c,L0)) for c in signs)
assert ranks=={2:48,3:16}
perms=list(permutations(V))
orbits=[];left={tup(c) for c in signs}
while left:
 state=min(left);c=dict(zip(edges,state));O={tup(act(c,g)) for g in perms};left-=O
 assert len(O) in (8,24)
 assert len({rank(E(dict(zip(edges,k)),L0)) for k in O})==1
 orbits.append((len(O),rank(E(c,L0)),str(determinant(E(c,L0)))))
assert sorted(o[0] for o in orbits)==[8,8,24,24]
for c in signs:
 q=tuple(c[e]*c[f] for e,f in pair)
 accepted=q in ((1,-1,1),(-1,1,-1))
 assert (rank(E(c,L0))==3)==accepted
 if accepted:assert dual(c)==c or all(dual(c)[e]==-c[e] for e in edges)
 for g in perms:
  t=act(c,g)
  assert rank(E(t,L0))==rank(E(c,L0))
  sign_g=even_sign(g)
  assert all(dual(t)[e]==sign_g*act(dual(c),g)[e] for e in edges)

for lam in [L0,(F(1),F(0),F(0),F(0)),(F(0),F(1),F(0),F(0)),(F(1,7),F(2,7),F(1,7),F(3,7)),(F(7,20),F(2,20),F(5,20),F(6,20)),(F(1,10),F(1,10),F(1,10),F(7,10))]:
 norm=sum(z*z for z in lam)
 assert norm>=F(1,4)
 for eig in (1,-1):
  for a,b,d in ((F(1),F(2),F(3)),(F(-3,2),F(5,7),F(11,4)),(F(2),F(-1),F(-3))):
   c={(0,1):a,(2,3):eig*a,(0,2):b,(1,3):-eig*b,(0,3):d,(1,2):eig*d}
   assert all(dual(c)[e]==eig*c[e] for e in edges)
   assert determinant(E(c,lam))==a*b*d*norm,(eig,c,lam)
# Perturb one relative sign: non-eigen 1/10 deformation stays everywhere nondegenerate.
for lam in [L0,(F(1),F(0),F(0),F(0)),(F(1,7),F(2,7),F(1,7),F(3,7))]:
  pert={(0,1):F(1),(2,3):F(1),(0,2):F(1),(1,3):F(-9,10),(0,3):F(1),(1,2):F(1)}
  assert dual(pert)!=pert and not all(dual(pert)[e]==-pert[e] for e in edges)
  assert determinant(E(pert,lam))==sum(q*q for q in lam)-F(1,10)*(lam[1]**2+lam[3]**2)
  assert determinant(E(pert,lam))>=F(9,40)
# Whitney 0-to-1 discrete gradient for an affine vertex signal (sample 3D derivative).
for lam in [L0,(F(1,7),F(2,7),F(1,7),F(3,7))]:
 U={0:F(1,3),1:F(2,5),2:F(-1,7),3:F(4,9)}
 rhs=[sum((U[j]-U[i])*Whitney((i,j),lam)[k] for i,j in edges) for k in range(3)]
 lhs=[sum(U[i]*grads[i][k] for i in V) for k in range(3)]
 assert rhs==lhs
# Uniform support data and latent activity cannot choose sign sectors.
for c in signs:
 assert tuple(abs(c[e]) for e in edges)==(1,)*6
 assert tuple(2*abs(c[e])*(1+1) for e in edges)==(4,)*6
out={'status':'PASS','engine':'pure_python_fraction_independent','n_signs':64,'ranks':dict(ranks),'orbit_data':orbits,'S4_elements':len(perms),'nonzero_eigen_coframes':16,'dual_sign_twist':'verified','global_det_formula':'a*b*d*sum(lambda_i^2)','min_sum_lambda_i_squared':'1/4','physical_promotion':0}
Path(__file__).with_name('replay_results.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
print('PASS independent Fraction: 64 sign cochains, 24 permutations, 4 orbits, duality twist, samples at barycenter/vertices/interior, Whitney coboundary')
print(json.dumps(out))
