"""Exact source-bound response/closure and declared coarse mixing verification."""
from fractions import Fraction as F
from itertools import combinations,permutations
import json

def zero(n,m=None):return [[F(0) for j in range(m or n)] for i in range(n)]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def transpose(a):return list(map(list,zip(*a)))
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(x,a):return [[x*v for v in r] for r in a]
def mm(a,b):return [[sum(x*y for x,y in zip(r,s)) for s in zip(*b)] for r in a]
def mv(a,v):return [sum(x*y for x,y in zip(r,v)) for r in a]
def outer(x,y):return [[a*b for b in y] for a in x]
def trace(a):return sum(a[i][i] for i in range(len(a)))
# Declared filled-tetrahedron chain source, sorted simplex orientations.
verts=tuple(range(4));simp=[list(combinations(verts,k+1)) for k in range(4)];offset=[0,4,10,14];A=zero(15);boundaries=[]
for k in range(1,4):
 B=zero(len(simp[k-1]),len(simp[k]))
 for j,sigma in enumerate(simp[k]):
  for i in range(k+1):B[simp[k-1].index(sigma[:i]+sigma[i+1:])][j]=F((-1)**i)
 boundaries.append(B)
 for i in range(len(B)):
  for j in range(len(B[0])):A[offset[k-1]+i][offset[k]+j]=-B[i][j];A[offset[k]+j][offset[k-1]+i]=B[i][j]
assert add(A,transpose(A))==zero(15)
assert mm(boundaries[0],boundaries[1])==zero(4,4) and mm(boundaries[1],boundaries[2])==zero(6,1)
P0=zero(15)
for i in range(4):
 for j in range(4):P0[i][j]=F(1,4)
assert mm(A,A)==scale(F(-4),add(eye(15),scale(-1,P0)))
pairings=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
sensors=[[i,offset[2]+simp[2].index(tuple(v for v in verts if v!=i))] for i in verts]+[[offset[1]+simp[1].index(e) for e in m] for m in pairings]
def stocks(c):return [sum(c[i]**2 for i in inds) for inds in sensors]
def stock_dot(c):
 dc=mv(A,c);return [sum(2*c[i]*dc[i] for i in inds) for inds in sensors]
cplus=[F(0)]*15;cplus[0]=1;cplus[4]=1;cminus=cplus.copy();cminus[4]=-1
assert stocks(cplus)==stocks(cminus) and stock_dot(cplus)!=stock_dot(cminus)
assert stock_dot(cminus)==[-v for v in stock_dot(cplus)]
for c in [cplus,cminus]:
 M=outer(c,c);dc=mv(A,c);assert add(mm(A,M),mm(M,transpose(A)))==add(outer(dc,c),outer(c,dc))
 assert trace(add(mm(A,M),mm(M,transpose(A))))==0
body=[F(0)]*15;body[offset[2]]=1;body[14]=1
assert sum(stock_dot(body))==-2*body[14]*mv(A,body)[14] and sum(stock_dot(body))!=0
# Exact aggregation of the 28 native Hasse incidence currents.
weights=[[F(i in inds) for i in range(15)] for inds in sensors]+[[F(i==14) for i in range(15)]]
incidences=[(i,j) for i in range(15) for j in range(i+1,15) if A[i][j]]
assert len(incidences)==28
D8=[[w[i]-w[j] for i,j in incidences] for w in weights];D7=D8[:7]
assert all(sum(D8[a][k] for a in range(8))==0 for k in range(28))
def rank(matrix):
 a=[r[:] for r in matrix];pivot=0
 for j in range(len(a[0])):
  found=next((i for i in range(pivot,len(a)) if a[i][j]),None)
  if found is None:continue
  a[pivot],a[found]=a[found],a[pivot];v=a[pivot][j];a[pivot]=[x/v for x in a[pivot]]
  for i in range(len(a)):
   if i!=pivot and a[i][j]:
    v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[pivot])]
  pivot+=1
  if pivot==len(a):break
 return pivot
assert rank(D8)==7 and rank(D7)==7
for c in [cplus,cminus,body]:
 J=[2*A[i][j]*c[i]*c[j] for i,j in incidences]
 assert mv(D7,J)==stock_dot(c)
 dc=mv(A,c);assert mv(D8,J)==stock_dot(c)+[2*c[14]*dc[14]]
def serial(a):return [[str(x) for x in row] for row in a]
from pathlib import Path
Path(__file__).with_name('OPERATORS.json').write_text(json.dumps({'A':serial(A),'simplex_basis':[list(sigma) for degree in simp for sigma in degree],'paired_sensor_indices':sensors,'body_index':14,'current_incidence_pairs':incidences,'D7':serial(D7),'D8':serial(D8),'convention':'J_ij=2 A_ij M_ij for i<j; D_a,ij=w_a,i-w_a,j','status':'exact declared aggregation; sensor map candidate'},indent=2)+'\n')

# Five declared mixing hypotheses reduce to three off-diagonal weights.
def transfer(q,r,t):
 T=zero(7)
 for i in range(7):
  for j in range(7):
   if i<4 and j<4:T[i][j]=1-3*q-3*r if i==j else q
   elif i>=4 and j>=4:T[i][j]=1-2*t-4*r if i==j else t
   else:T[i][j]=r
 return T
E=eye(7);Qv=zero(7);Qe=zero(7);mean=scale(F(1,7),[[F(1)]*7 for _ in range(7)])
for i in range(4):
 for j in range(4):Qv[i][j]=F(i==j)-F(1,4)
for i in range(4,7):
 for j in range(4,7):Qe[i][j]=F(i==j)-F(1,3)
Pm=add(add(add(E,scale(-1,mean)),scale(-1,Qv)),scale(-1,Qe));Ps=[mean,Qv,Qe,Pm]
assert [trace(p) for p in Ps]==[1,3,2,1]
for i,p in enumerate(Ps):
 for j,b in enumerate(Ps):assert mm(p,b)==p if i==j else mm(p,b)==zero(7)
# Coefficient-wise identity, exact for all q,r,t.
for q,r,t in [(F(0),F(0),F(0)),(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1))]:
 T=transfer(q,r,t);ev=[F(1),1-4*q-3*r,1-3*t-4*r,1-7*r]
 rhs=zero(7)
 for p,x in zip(Ps,ev):rhs=add(rhs,scale(x,p))
 assert T==rhs
 assert all(sum(row)==1 for row in T) and T==transpose(T)
matching=[frozenset(map(frozenset,p)) for p in pairings];actions=[]
for p in permutations(verts):
 a=list(p)+[4+matching.index(frozenset(frozenset(p[i] for i in edge) for edge in m)) for m in matching];actions.append(a)
T=transfer(F(1,20),F(1,10),F(1,12));assert all(v>=0 for row in T for v in row)
for a in actions:assert [[T[a[i]][a[j]] for j in range(7)] for i in range(7)]==T
Tpower=eye(7);ev=[F(1),F(1)-4*F(1,20)-3*F(1,10),F(1)-3*F(1,12)-4*F(1,10),F(1)-7*F(1,10)]
for n in range(6):
 rhs=zero(7)
 for p,x in zip(Ps,ev):rhs=add(rhs,scale(x**n,p))
 assert Tpower==rhs;Tpower=mm(Tpower,T)
f=F(2,3);w=(1-f)/7;uniform=transfer(w,w,w);assert uniform==add(mean,scale(f,add(E,scale(-1,mean))))
result={'status':'PASS','physical_promotion':0,'independent_review':'pending','lane':'development — no registry entry','native_chain_dimensions':[4,6,4,1],'grouped_current_response':{'incidences':28,'D8_rank':7,'D7_rank':7,'cycle_kernel_dimension':21,'grouped_stocks_with_body':8},'native_source_checks':['boundary squared zero','A skew','A squared active identity','exact covariance lift and trace conservation'],'paired_stock_sensor_map':{'status':'CANDIDATE_DECLARED_MAP_WITH_EXACT_ALGEBRA','VF_then_EE_indices':sensors,'body_coordinate_excluded':14},'native_closure_counterexample':{'same_stocks':[str(v) for v in stocks(cplus)],'plus_derivative':[str(v) for v in stock_dot(cplus)],'minus_derivative':[str(v) for v in stock_dot(cminus)],'body_exchange_stock_derivative':str(sum(stock_dot(body)))},'declared_markov_law':{'free_source_weights':['q_VF','r_cross','t_EE'],'projector_ranks':[1,3,2,1],'sector_response_factors':['1','1-4q-3r','1-3t-4r','1-7r'],'group_actions_checked':24,'power_rounds_checked':list(range(6)),'uniform_active_determinant':'f^6','full_scalar_mass_conservation':'f=1 only'},'numerical_target_evaluated':False,'scope':'Native moment algebra is exact under declared chain generator; paired sensors and Markov interpretation require source admission; no native seven-channel closure, constitutive weights, clock or physical bridge is claimed'}
print(json.dumps(result,indent=2))
