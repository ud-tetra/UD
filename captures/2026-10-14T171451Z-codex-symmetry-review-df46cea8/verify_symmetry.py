"""Exact finite symmetry certificates for the declared signed S4 carrier."""
from itertools import combinations,permutations
from pathlib import Path
import json
import sympy as s

root=Path(__file__).resolve().parent
perms=list(permutations(range(4)))
simp=[list(combinations(range(4),k+1)) for k in range(4)]
off=[0]
for a in simp:off.append(off[-1]+len(a))
def parity(t):
 return (-1)**sum(t[i]>t[j] for i in range(len(t)) for j in range(i+1,len(t)))
def action(g,k):
 M=s.zeros(len(simp[k]))
 for j,f in enumerate(simp[k]):
  t=tuple(g[i] for i in f);M[simp[k].index(tuple(sorted(t))),j]=parity(t)
 return M
def cycles(g):
 seen=set();sizes=[]
 for j in range(4):
  if j not in seen:
   i=j;n=0
   while i not in seen:seen.add(i);n+=1;i=g[i]
   sizes.append(n)
 return tuple(sorted(sizes,reverse=True))
types=[(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)]
sizes=[1,6,3,8,6]
chars={'A1':[1,1,1,1,1],'A2':[1,-1,1,1,-1],
 'E':[2,0,2,-1,0],'T1':[3,-1,-1,0,1],'T2':[3,1,-1,0,-1]}
def inner(a,b):return sum(s.Rational(n,24)*x*y for n,x,y in zip(sizes,a,b))
for a in chars:
 for b in chars:assert inner(chars[a],chars[b])==int(a==b)
B={}
for k in (1,2,3):
 M=s.zeros(len(simp[k-1]),len(simp[k]))
 for j,t in enumerate(simp[k]):
  for i in range(k+1):M[simp[k-1].index(t[:i]+t[i+1:]),j]=(-1)**i
 B[k]=M
channels=[]
for k in (1,2,3):
 A=s.zeros(15);A[off[k-1]:off[k],off[k]:off[k+1]]=-B[k]
 A[off[k]:off[k+1],off[k-1]:off[k]]=B[k].T;channels.append(A)
canonical=sum(channels,s.zeros(15))
chain_chars={};reps={}
for g in perms:
 blocks=[action(g,k) for k in range(4)];R=s.diag(*blocks);reps[g]=R
 assert R.T*R==s.eye(15)
 for k in (1,2,3):assert blocks[k-1]*B[k]==B[k]*blocks[k]
 assert R*canonical==canonical*R
 c=[s.trace(M) for M in blocks]
 key=types.index(cycles(g))
 if key in chain_chars:assert chain_chars[key]==c
 else:chain_chars[key]=c
for g in perms:
 for h in perms:
  gh=tuple(g[h[i]] for i in range(4));assert reps[g]*reps[h]==reps[gh]
table=[[int(chain_chars[j][k]) for j in range(5)] for k in range(4)]
assert table==[[4,2,0,1,0],[6,0,-2,0,0],[4,-2,0,1,0],[1,-1,1,1,-1]]
decomp=[{label:int(inner(row,ch)) for label,ch in chars.items()} for row in table]
total=[sum(row[j] for row in table) for j in range(5)]
assert inner(total,total)==13
for k,P in enumerate([-A*A/4 for A in channels]):
 assert P.T==P and P*P==P and P.rank()==[6,6,2][k]
for i in range(3):
 for j in range(3):
  if i!=j:assert channels[i]*channels[j]==s.zeros(15)
a,b,c=s.symbols('a b c',real=True)
x=s.symbols('x')
weighted=a*channels[0]+b*channels[1]+c*channels[2]
expected=x*(x*x+4*a*a)**3*(x*x+4*b*b)**3*(x*x+4*c*c)
assert s.expand(weighted.charpoly(x).as_expr()-expected)==0
upper=s.zeros(15)
for k in (1,2,3):upper[off[k-1]:off[k],off[k]:off[k+1]]=B[k]
D=upper+upper.T;U=s.diag(*[s.I**k for k in range(4) for f in simp[k]])
assert U*D*U.conjugate().T==s.I*canonical

squaretypes=[]
for typ in types:
 g=next(g for g in perms if cycles(g)==typ);gg=tuple(g[g[i]] for i in range(4));squaretypes.append(types.index(cycles(gg)))
symchar=[(chars['T2'][j]**2+chars['T2'][squaretypes[j]])/s.Integer(2) for j in range(5)]
assert {name:int(inner(symchar,ch)) for name,ch in chars.items()}=={'A1':1,'A2':0,'E':1,'T1':0,'T2':1}
context={name:int(inner([x*y for x,y in zip(chars['E'],ch)],chars['T2'])) for name,ch in chars.items()}
assert context=={'A1':0,'A2':0,'E':0,'T1':1,'T2':1}
even=[g for g in perms if parity(g)==1]
assert sum(s.trace(reps[g])**2 for g in even)/12==25

# Explicit compatible T2 context tensor from Paper III section 10.1.
Q=s.Matrix([[0,s.sqrt(2)/2,-s.sqrt(2)/2],[s.sqrt(6)/3,-s.sqrt(6)/6,-s.sqrt(6)/6],[s.sqrt(3)/3,s.sqrt(3)/3,s.sqrt(3)/3]])
P=s.diag(1,1,-1);diags=[s.diag(s.sqrt(3)/2,-s.sqrt(3)/2,0),s.diag(s.Rational(1,2),s.Rational(1,2),-1)]
V=s.Matrix([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]])/2
def clean(M):return M.applyfunc(s.simplify)
def gamma(v):return (P*diags[0]*Q.T*v).row_join(P*diags[1]*Q.T*v)
checks=0
for g in perms:
 R4=action(g,0);R=V.T*R4*V
 rc=clean(Q*R*Q.T);ro=P*R*P.T
 re=clean(s.Matrix(2,2,lambda i,j:s.Rational(2,3)*s.trace(diags[i]*R*diags[j]*R.T)))
 for j in range(3):
  v=s.eye(3)[:,j];assert clean(gamma(rc*v)*re-ro*gamma(v))==s.zeros(3,2);checks+=1

report={'status':'PASS','exact_group_composition_checks':576,'boundary_equivariance_checks':72,
 'class_order':['identity','transposition','double transposition','3-cycle','4-cycle'],
 'class_sizes':sizes,'irreducible_characters':chars,'signed_chain_characters':table,'chain_decomposition':decomp,
 'commutant_dimensions':{'full_S4':13,'self_adjoint_S4':10,'skew_adjoint_S4':3,'full_A4':25},
 'weighted_characteristic_polynomial':str(s.factor(expected)),
 'invariant_sector_ranks':[6,6,2],'context_multiplicities':context,'gamma_covariance_checks':checks,
 'skew_to_dirac_phase_equivalence':'PASS','scope':'finite exact constructor verification; no novelty or physical promotion',
 'physical_promotion':0}
(root/'SYMMETRY_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
(root/'EXACT_SYMMETRY_MATRICES.json').write_text(json.dumps({'simplex_order':simp,'boundaries':{str(k):M.tolist() for k,M in B.items()},'channel_generators':[A.tolist() for A in channels]},default=int,indent=2)+'\n')
print(json.dumps(report))
