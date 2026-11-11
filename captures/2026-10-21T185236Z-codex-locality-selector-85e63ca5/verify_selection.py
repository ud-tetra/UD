from fractions import Fraction as F
from itertools import combinations,permutations
import json
from pathlib import Path
n=6;edges=list(combinations(range(4),2))
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def add(*As):return [[sum(A[i][j] for A in As) for j in range(len(As[0][0]))] for i in range(len(As[0]))]
def scale(c,A):return [[c*x for x in r] for r in A]
def mul(A,B):return [[sum(a*b for a,b in zip(r,c)) for c in zip(*B)] for r in A]
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def mv(A,x):return [dot(r,x) for r in A]
I=eye(n);J=[[F(1)]*n for _ in range(n)];S=[[F(set(e).isdisjoint(f)) for f in edges] for e in edges]
T=add(scale(F(5,12),I),scale(F(1,12),S),scale(F(1,12),J));H=add(I,scale(-1,T))
P0=scale(F(1,6),J);Pm=scale(F(1,2),add(I,scale(-1,S)));Ph=add(I,scale(-1,P0),scale(-1,Pm))
def Q(x,y):return add(scale(x+5*y,I),scale(y-x,S),scale(-y,J))
perms=list(permutations(range(4)));actions=[]
for g in perms:
 U=[[F(0)]*6 for _ in range(6)]
 for j,e in enumerate(edges):U[edges.index(tuple(sorted(g[v] for v in e)))][j]=F(1)
 actions.append(U)
# Exact ordered-pair orbit classification: diagonal / disjoint / sharing vertex.
orbits=[];remaining={(i,j) for i in range(6) for j in range(6)}
while remaining:
 i,j=min(remaining);orb={(edges.index(tuple(sorted(g[v] for v in edges[i]))),edges.index(tuple(sorted(g[v] for v in edges[j])))) for g in perms}
 orbits.append(orb);remaining-=orb
assert sorted(map(len,orbits))==[6,6,24]
records=[]
for x,y in [(F(1,6),F(1,12)),(F(1),F(1)),(F(2),F(1)),(F(3,2),F(1,2))]:
 M=Q(x,y);assert all(sum(r)==0 for r in M)
 assert all(M[i][j]<=0 for i in range(6) for j in range(6) if i!=j)
 assert mul(M,P0)==scale(0,I);assert mul(M,Ph)==scale(6*y,Ph);assert mul(M,Pm)==scale(2*x+4*y,Pm)
 assert all(mul(U,M)==mul(M,U) for U in actions)
 records.append({'opposite_weight':str(x),'cross_weight':str(y),'positive_levels':[str(6*y),str(2*x+4*y)],'ratio':str((2*x+4*y)/(6*y))})
assert H==Q(F(1,6),F(1,12))
Fplus=add(scale(F(3,2),H),scale(9,mul(H,H)));Fswap=add(scale(F(53,2),H),scale(-33,mul(H,H)))
assert Fplus==Q(F(3,2),F(1,2));assert Fswap==Q(F(-1,6),F(5,6))
assert all(Fplus[i][j]<=0 for i in range(6) for j in range(6) if i!=j)
pos=[(i,j,str(Fswap[i][j])) for i in range(6) for j in range(6) if i!=j and Fswap[i][j]>0]
assert len(pos)==6 and all(v=='1/6' for i,j,v in pos)
assert records[1]['ratio']!=records[2]['ratio']
# Maximal mean-conserving phase subspace, dimension 11: one velocity constraint.
ones=[F(1)]*6;assert all(sum(T[i][j] for i in range(6))==1 for j in range(6))
assert all(sum(Fplus[i][j] for i in range(6))==0 for j in range(6))
q=[F(1),0,0,0,0,0];v=[F(-1),F(1),0,0,0,0]
assert sum(v)==0 and sum(mv(Fplus,q))==0
# Positivity failure at a boundary with an admissible signed phase velocity.
q0=[F(0)]*6;assert all(x>=0 for x in q0) and v[0]<0
# A stochastic finite oscillatory Taylor update on q0 starts t*v; negativity holds
# at sufficiently small positive t because the derivative is strictly negative.
# Exact heat/implicit/CN spectral tests require scalar parameters inconsistent.
assert 2**5!=3**3 # heat mapping exp(-3t)=1/2, exp(-5t)=1/3
backward=[(F(1,1)/F(1,2)-1)/3,(F(1,1)/F(1,3)-1)/5]
cn=[2*(1-F(1,2))/(3*(1+F(1,2))),2*(1-F(1,3))/(5*(1+F(1,3)))]
assert backward[0]!=backward[1] and cn[0]!=cn[1]
out={'status':'PASS_SCOPED_CONSTRUCTOR_ONLY','relation_orbit_sizes':sorted(map(len,orbits)),'nonnegative_conductance_graph_family':'Q(x,y)=(x+5y)I+(y-x)S-yJ, x>=0,y>0','spectrum':'0(1),6y(2),(2x+4y)(3)','counterexamples':records,'spectral_assignment_filter':{'primary_weights':['3/2','1/2'],'swapped_weights':['-1/6','5/6'],'swapped_positive_offdiagonals':pos,'conclusion':'nonnegative conductances eliminate the swapped interpolation; positive-semidefinite energy alone does not; primary weights remain unselected'},'harmonic_restriction':{'source_invariant':'sum(q)','second_order_invariant':'sum(v) constant','fixed_mean_condition':'sum(v)=0; maximal dimension11','scope':'conservation transfer requirement; not full Markov dynamical equivalence'},'state_positivity':'signed phase lift is not a positivity-preserving Markov process on its entire admitted phase domain','standard_scalar_semigroup_tests':{'heat_exact_mismatch':'2^5 != 3^3','backward_euler_required_steps':list(map(str,backward)),'crank_nicolson_required_steps':list(map(str,cn)),'scope':'order-preserving assignments3->1/2,5->1/3 only; no universal functional-map no-go'},'source_law':'STILL_OPEN','physical_promotion':0}
print(json.dumps(out,indent=2))
