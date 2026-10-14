"""Exact conditional seven-channel reconstruction and general memory-write family.

This verifier is newly authored. It does not execute imported historical code.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations
import json,math
root=Path(__file__).resolve().parent
def mat(n,m=None):return [[F(0) for _ in range(m or n)] for _ in range(n)]
def add(A,B):return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def scale(a,A):return [[a*x for x in row] for row in A]
def mul(A,B):return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))] for i in range(len(A))]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def rank(A):
 A=[r[:] for r in A];r=0
 for c in range(len(A[0])):
  p=next((i for i in range(r,len(A)) if A[i][c]),None)
  if p is None:continue
  A[p],A[r]=A[r],A[p];a=A[r][c];A[r]=[x/a for x in A[r]]
  for i in range(len(A)):
   if i!=r:
    a=A[i][c];A[i]=[x-a*y for x,y in zip(A[i],A[r])]
  r+=1
 return r
P=[[F(1,7) for _ in range(7)] for _ in range(7)]
V=mat(7);E=mat(7)
for i in range(4):
 for j in range(4):V[i][j]=F(i==j)-F(1,4)
for i in range(4,7):
 for j in range(4,7):E[i][j]=F(i==j)-F(1,3)
R=add(eye(7),scale(-1,add(P,add(V,E))))
projectors=[P,V,E,R]
assert [rank(x) for x in projectors]==[1,3,2,1]
for i,A in enumerate(projectors):
 assert mul(A,A)==A
 for j,B in enumerate(projectors):
  if i!=j:assert mul(A,B)==mat(7)
M=add(P,add(scale(F(8,21),V),scale(F(3,7),E)))
assert M==[[M[j][i] for j in range(7)] for i in range(7)]
assert all(sum(r)==1 and all(x>=0 for x in r) for r in M)
assert mul(R,M)==mat(7) and mul(M,R)==mat(7)
assert rank(M)==6
blocks=[(P,F(1)),(V,F(8,21)),(E,F(3,7)),(R,F(0))]
for A,a in blocks:assert mul(M,A)==scale(a,A)
# Verify the actual S4 action on vertices and opposite-edge partitions.
pairs=[frozenset((frozenset((0,1)),frozenset((2,3)))),frozenset((frozenset((0,2)),frozenset((1,3)))),frozenset((frozenset((0,3)),frozenset((1,2))))]
for p in permutations(range(4)):
 image=list(p)+[4+pairs.index(frozenset(frozenset(p[i] for i in edge) for edge in pair)) for pair in pairs]
 assert all(M[image[i]][image[j]]==M[i][j] for i in range(7) for j in range(7))
# Same reported spectrum and S4 symmetry, but a different positive PF vector.
t=F(3,4);v=[t]*4+[F(1)]*3;den=4*t*t+3
Palt=[[x*y/den for y in v] for x in v]
Malt=add(Palt,add(scale(F(8,21),V),scale(F(3,7),E)))
Ralt=add(eye(7),scale(-1,add(Palt,add(V,E))))
assert Malt!=M and rank(Malt)==6 and all(x>=0 for row in Malt for x in row)
assert mul(Palt,Palt)==Palt and mul(Malt,Palt)==Palt
assert mul(Malt,V)==scale(F(8,21),V) and mul(Malt,E)==scale(F(3,7),E)
assert mul(Malt,Ralt)==mat(7)
assert sum(x!=0 for row in Malt for x in row)==49
assert any(sum(row)!=1 for row in Malt)
q=F(3,4)
chi_q=q*(q-1)*(q-F(3,7))**2*(q-F(8,21))**3
assert chi_q==F(-268119,275365888) and chi_q!=0
# Exact Cayley-Hamilton witness (multiplicity-bearing polynomial).
poly=[F(1)]
for a in (F(0),F(1),F(3,7),F(3,7),F(8,21),F(8,21),F(8,21)):
 nxt=[F(0)]*(len(poly)+1)
 for i,v in enumerate(poly):nxt[i]-=a*v;nxt[i+1]+=v
 poly=nxt
power=eye(7);cm=mat(7)
for c in poly:cm=add(cm,scale(c,power));power=mul(power,M)
assert cm==mat(7)
# The symmetry-adapted five-unknown equations have unique reconstruction.
# Unknowns: VF diagonal/off-diagonal, EE diagonal/off-diagonal, cross block.
A=[[1,-1,0,0,0],[0,0,1,-1,0],[1,3,0,0,3],[0,0,1,2,4],[1,3,0,0,-4]]
assert rank([[F(x) for x in row] for row in A])==5
candidate=[F(3,7),F(1,21),F(3,7),F(0),F(1,7)]
assert [sum(F(a)*x for a,x in zip(row,candidate)) for row in A]==[F(8,21),F(3,7),F(1),F(1),F(0)]
support=sum(x!=0 for row in M for x in row)
assert support==43
# Exchange conserves excitation exactly; its square projects onto that sector.
N=[[F(0) for _ in range(4)] for _ in range(4)]
for i,a in enumerate((0,1,1,2)):N[i][i]=F(a)
exchange=mat(4);exchange[1][2]=exchange[2][1]=F(1)
one=mat(4);one[1][1]=one[2][2]=F(1)
assert mul(N,exchange)==mul(exchange,N)
assert mul(exchange,exchange)==one and mul(one,exchange)==exchange
# Exact unitary checks in the fixed phase gauge where the block is real.
for c,s in ((F(3,5),F(4,5)),(F(4,5),F(3,5))):
 U=eye(4);U[1][1]=U[2][2]=c;U[1][2]=s;U[2][1]=-s
 Ut=[[U[j][i] for j in range(4)] for i in range(4)]
 assert mul(Ut,U)==eye(4) and mul(N,U)==mul(U,N)
def entropy(weights):return -sum(float(w)*math.log(float(w)) for w in weights if w)
def h(x):return entropy([x,1-x])
def padd(a,b):
 out=[F(0)]*max(len(a),len(b))
 for i,x in enumerate(a):out[i]+=x
 for i,x in enumerate(b):out[i]+=x
 return out
def pmul(a,b):
 out=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def reused_probability(q,n):
 a=[F(1)];b=[F(0),F(1)]
 if n==0:t=a
 elif n==1:t=b
 else:
  for _ in range(1,n):a,b=b,padd([F(0)]+[2*x for x in b],[-x for x in a])
  t=b
 square=pmul(t,t);assert all(v==0 for i,v in enumerate(square) if i%2)
 return sum((v*q**(i//2) for i,v in enumerate(square) if i%2==0),F(0))
rows=[]
for q in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
 previous_H=0.0
 for n in range(17):
  active=q**n;written=[(1-q)*q**j for j in range(n)];dist=[active]+written
  assert sum(dist)==1
  residual=sum(written,F(0));assert residual==1-active
  # Arbitrary initial nonnegative energy is conserved in normalized inventory.
  assert active+residual==1
  H=entropy(dist)
  if n:assert abs(H-previous_H-float(q**(n-1))*h(q))<1e-12
  Hclosed=0 if q==1 else h(q)*float((1-q**n)/(1-q))
  assert abs(H-Hclosed)<1e-12;previous_H=H
  # Input X=0 has empty memory; X=1 has this geometric write distribution.
  zero=[F(1)]+[F(0)]*n;mix=[(a+b)/2 for a,b in zip(zero,dist)]
  D=sum(abs(a-b) for a,b in zip(zero,dist))/2;assert D==residual
  error=sum(min(a,b) for a,b in zip(zero,dist))/2;assert error==active/2
  I=entropy(mix)-H/2
  assert abs(I-(h(residual/2)-h(active)/2))<1e-12 and -1e-12<=I<=math.log(2)+1e-12
  reused=reused_probability(q,n);assert 0<=reused<=1
  if q==F(3,4) and n in (0,1,3,6,7,16):
   rows.append({'q':str(q),'writes':n,'fresh_carrier_energy_fraction':str(active),'fresh_memory_energy_fraction':str(residual),'reused_carrier_energy_fraction':str(reused),'history_entropy_conditional_active_nats':H,'retained_source_information_nats':I,'optimal_input_error_exact':str(error),'information_per_n_cell_area_coefficient':None if not n else I/n,'fresh_blank_cells':n})
assert reused_probability(F(3,4),3)==0 and reused_probability(F(3,4),6)==1
result={'status':'PASS scoped conditional reconstruction and write family','physical_promotion':0,'independent_review':'OPEN','original_matrix_recovered':False,'candidate_matrix':[[str(x) for x in row] for row in M],'candidate_assumptions':['S4 action on four VF and three EE channels','real self-adjoint operator','uniform stationary PF vector','reported sector eigenvalues; signed invariant residue kernel'],'rank':6,'charpoly_at_3over4':str(chi_q),'support_nonzeros':support,'support_mean':'43/7','same_spectrum_counterexample':{'matrix':[[str(x) for x in row] for row in Malt],'PF_vector_ratio':'VF/EE=3/4','nonnegative':True,'unit_metric_selfadjoint':True,'row_stochastic':False,'support_nonzeros':49},'support_identity_warning':'43/7 equals C07 number only under candidate assumptions; no source identity inferred','native_q_selection':'OPEN; q=cos^2(g tau/hbar) for arbitrary coupling/time','finite_memory_reuse':'coherent recurrence; six writes restore carrier for theta=pi/6','rows':rows,'history_entropy_limit_q_3over4_nats':4*h(F(3,4)),'full_controller_reset_cost':'OPEN','boundary_area_law':'NOT DERIVED','G_input':False}
(root/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
with (root/'CONDITIONAL_M_MATRIX.csv').open('w') as f:
 f.write('channel,'+','.join(['VF0','VF1','VF2','VF3','EE01_23','EE02_13','EE03_12'])+'\n')
 for name,row in zip(['VF0','VF1','VF2','VF3','EE01_23','EE02_13','EE03_12'],M):f.write(name+','+','.join(map(str,row))+'\n')
print('PASS: projectors, S4 covariance, spectrum, kernel, Cayley-Hamilton obstruction, unique conditional matrix, exchange excitation conservation, phase-gauge unitary controls, fresh-write entropy/information, coherent-reuse recurrence')
print(json.dumps(rows,indent=2))
