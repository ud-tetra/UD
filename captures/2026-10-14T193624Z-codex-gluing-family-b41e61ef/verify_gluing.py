from itertools import combinations
from pathlib import Path
import json
import sympy as s

root=Path(__file__).resolve().parent
def local(cell,weights=(1,1,1)):
 simp=[list(combinations(tuple(sorted(cell)),k+1)) for k in range(4)]
 flat=[f for group in simp for f in group];off=[0]
 for group in simp:off.append(off[-1]+len(group))
 A=s.zeros(15)
 for k,w in enumerate(weights,1):
  B=s.zeros(len(simp[k-1]),len(simp[k]))
  for j,t in enumerate(simp[k]):
   for i in range(k+1):B[simp[k-1].index(t[:i]+t[i+1:]),j]=(-1)**i
  A[off[k-1]:off[k],off[k]:off[k+1]]=-w*B
  A[off[k]:off[k+1],off[k-1]:off[k]]=w*B.T
 assert A.T==-A
 return flat,A
def joined(cells,weights=None):
 if weights is None:weights=[(1,1,1)]*len(cells)
 models=[local(c,w) for c,w in zip(cells,weights)]
 copies=[f for faces,A in models for f in faces]
 unique=sorted(set(copies),key=lambda f:(len(f),f));E=s.zeros(len(unique),len(copies))
 for j,f in enumerate(copies):E[unique.index(f),j]=1
 A=s.diag(*[A for faces,A in models]);multiplicities=[int(sum(E[i,j] for j in range(E.cols))) for i in range(E.rows)]
 assert E*E.T==s.diag(*multiplicities)
 Q=s.diag(*[1/s.sqrt(t) for t in multiplicities])*E
 assert Q*Q.T==s.eye(E.rows)
 return unique,E,Q,A

cases={
 'one':[(0,1,2,3)],
 'two_face':[(0,1,2,3),(0,1,2,4)],
 'five_star':[(0,1,2,3),(1,2,3,4),(0,2,3,5),(0,1,3,6),(0,1,2,7)],
 'five_chain':[(0,1,2,3),(1,2,3,4),(2,3,4,5),(3,4,5,6),(4,5,6,7)],
 'boundary_four_simplex':list(combinations(range(5),4))}
results={}
for name,cells in cases.items():
 unique,E,Q,A=joined(cells);n=A.rows;m=E.rows
 O2=E.col_join(E*A);O3=O2.col_join(E*A*A)
 d2=O2.rank();d=O3.rank()
 assert A**3+4*A==s.zeros(n) # canonical copies need no later output derivatives
 if name!='boundary_four_simplex':
  assert n==15*len(cells) and m==8*len(cells)+7
  assert d2==n and d==n
 assert d>=m
 N=s.Matrix.hstack(*O3.nullspace()) if d<n else s.zeros(n,0)
 assert E*N==s.zeros(m,n-d) and E*A*N==s.zeros(m,n-d)
 if d<n:
  assert (N.row_join(A*N)).rank()==N.cols
 # Hidden instantaneous directions and output-derivative coupling.
 Rbasis=s.Matrix.hstack(*E.nullspace()) if m<n else s.zeros(n,0)
 coupling=(E*A*Rbasis).rank()
 results[name]={'cells':cells,'copied_dimension':n,'unique_dimension':m,
  'lossless_residual_dimension':n-m,'snapshot_plus_derivative_rank':d2,
  'observable_dimension':d,'minimal_linear_dynamic_memory':d-m,
  'unobservable_dimension':n-d,'visible_hidden_coupling_rank':coupling}
 (root/f'{name}_certificate.json').write_text(json.dumps({'cells':cells,'unique_simplex_order':unique,
  'aggregation':E.tolist(),'copy_generator':A.tolist(),'rank_snapshot_derivative':d2,
  'rank_three_block_observability':d,'unobservable_basis':N.tolist()},default=int,indent=2)+'\n')

# Arbitrary nonzero local weights: verify the leaf private-coordinate block and examples.
a,b,c=s.symbols('a b c',nonzero=True,real=True)
faces,A=local((0,1,2,3),(a,b,c));facet=[i for i,f in enumerate(faces) if 3 not in f];private=[i for i,f in enumerate(faces) if 3 in f]
C=A.extract(private,facet)
assert C.T*C==s.diag(a*a,a*a,a*a,b*b,b*b,b*b,c*c)
weighted={}
for name in ('two_face','five_star','five_chain'):
 cells=cases[name];weights=[(j+1,(-1)**j*(j+2),s.Rational(j+3,2)) for j in range(len(cells))]
 unique,E,Q,A=joined(cells,weights)
 assert E.col_join(E*A).rank()==A.rows
 weighted[name]={'weights':[[str(w) for w in lane] for lane in weights],'rank':A.rows}

# Zero weight is an excluded hypothesis: one shared-face coefficient can become invisible.
cells=cases['two_face'];weights=[(1,1,0),(1,1,0)]
unique,E,Q,A=joined(cells,weights)
zero_rank=E.col_join(E*A).rank()
assert zero_rank<A.rows
results['zero_cell_exchange_negative_control']={'weights':weights,'snapshot_derivative_rank':zero_rank,'copied_dimension':A.rows,'full_observable_dimension':E.col_join(E*A).col_join(E*A*A).rank(),'scope':'excluded zero c coefficient; instantaneous rank drop alone does not establish permanent unobservability'}
_,Ez,Qz,Az=joined(cells,[(0,0,0),(0,0,0)])
assert Az==s.zeros(30) and Ez.rank()==23
results['all_zero_exchange_control']={'copied_dimension':30,'unique_dimension':23,'observable_dimension':23,'minimal_linear_dynamic_memory':0,'scope':'excluded all-zero generator; no hidden influence on future observations'}

# A decoupled hidden oscillator shows lossless storage need not equal dynamic memory generally.
Ag=s.diag(s.Matrix([[0,-1],[1,0]]),s.Matrix([[0,-2],[2,0]]));Qg=s.Matrix([[1,0,0,0],[0,1,0,0]])
assert Qg.col_join(Qg*Ag).rank()==2
results['decoupled_hidden_control']={'copied_dimension':4,'unique_dimension':2,'lossless_residual_dimension':2,'minimal_linear_dynamic_memory':0}
report={'status':'PASS','cases':results,'nonzero_weight_examples':weighted,
 'symbolic_private_block_gram':'diag(a²,a²,a²,b²,b²,b²,c²)',
 'scope':'exact finite fixtures; induction and minimality proved in manuscript; no novelty or physical promotion',
 'physical_promotion':0}
(root/'GLUING_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
