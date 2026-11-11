from pathlib import Path
from fractions import Fraction as F
import json
S=json.loads(Path(__file__).with_name('SOURCE_OPERATORS.json').read_text());A=[[F(x) for x in r] for r in S['A']];groups=S['paired_sensor_indices']+[[14]];N=15

def Z(n,m=None):return [[F(0) for _ in range(m or n)] for _ in range(n)]
def I(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def tr(a):return list(map(list,zip(*a)))
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def sc(x,a):return [[x*v for v in r] for r in a]
def mul(a,b):return [[sum(x*y for x,y in zip(r,s)) for s in zip(*b)] for r in a]
def vec(a,x):return [sum(u*v for u,v in zip(r,x)) for r in a]
def rank(rows):
 a=[[F(x) for x in r] for r in rows];pivot=0
 for j in range(len(a[0])):
  k=next((i for i in range(pivot,len(a)) if a[i][j]),None)
  if k is None:continue
  a[pivot],a[k]=a[k],a[pivot];v=a[pivot][j];a[pivot]=[x/v for x in a[pivot]]
  for i in range(pivot+1,len(a)):
   if a[i][j]:
    v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[pivot])]
  pivot+=1
  if pivot==len(a):break
 return pivot
H=Z(N)
for i in range(4):
 for j in range(4):H[i][j]=F(1,4)
Q=add(I(N),sc(-1,H))
assert mul(A,A)==sc(-4,Q)
assert all(A[i][j]*H[i][j]==0 and A[i][j]*Q[i][j]==0 for i in range(N) for j in range(N))
def U(c,s):
 assert c*c+s*s==1
 u=add(add(H,sc(c,Q)),sc(s/2,A));assert mul(tr(u),u)==I(N);return u
def B(u):return [[x*x for x in r] for r in u]
C=[[F(i in g) for i in range(N)] for g in groups];L=[[F(i in g,len(g)) for g in groups] for i in range(N)]
assert mul(C,L)==I(8)
# Stronger averaging inserts uniform within-group redistribution after each sample.
def Kformula(c):
 ss=1-c*c;aa=(1+3*c)/4;bb=(1-c)/4;k=Z(8)
 for i in range(4):
  for j in range(4):k[i][j]=(aa*aa+c*c)/2 if i==j else bb*bb/2
  for j in range(4,7):k[i][j]=ss/4;k[j][i]=ss/4
  k[i][7]=ss/4;k[7][i]=ss/8
 for j in range(4,8):k[j][j]=c*c
 return k
checks=0
for c,s in [(F(1),F(0)),(F(-1),F(0)),(F(0),F(1)),(F(3,5),F(4,5)),(F(5,13),F(12,13))]:
 u=U(c,s);b=B(u);k=mul(mul(C,b),L);assert k==Kformula(c)
 assert all(sum(r)==1 for r in b) and b==tr(b)
 assert all(sum(k[i][j] for i in range(8))==1 for j in range(8)) and all(x>=0 for r in k for x in r)
 pi=[F(len(g),15) for g in groups];assert vec(k,pi)==pi
 assert all(k[i][j]*pi[j]==k[j][i]*pi[i] for i in range(8) for j in range(8));checks+=1
# Exact rational sampling fixture, independent of any requested numerical target.
c,s=F(3,5),F(4,5);u=U(c,s);b=B(u);k=Kformula(c);cb=mul(C,b)
# Same grouped stock, different micro allocation: dephasing alone is not lumpable.
left=[cb[i][0] for i in range(8)];right=[cb[i][groups[0][1]] for i in range(8)];assert left!=right
# Diagonal initial state: first step agrees, second differs from coherent evolution.
e=[F(i==0) for i in range(N)];p1=vec(b,e);coherent1=[x*x for x in vec(u,e)];assert p1==coherent1
coherent2=[x*x for x in vec(u,vec(u,e))];averaged2=vec(b,p1);assert coherent2!=averaged2
# Repeated stronger averaging closes exactly on K8.
g=[F(i==0) for i in range(8)]
for n in range(6):
 p=vec(L,g);pn=vec(b,p);gn=vec(C,pn);assert gn==vec(k,g);g=gn
# Spectral factors of stronger averaging; weighted reversible eigenspaces.
a=c*(1+3*c)/4;ee=c*c;mix=(15*c*c-7)/8
for i in range(1,4):
 v=[F(0)]*8;v[0]=1;v[i]=-1;assert vec(k,v)==[a*x for x in v]
for i in range(5,7):
 v=[F(0)]*8;v[4]=1;v[i]=-1;assert vec(k,v)==[ee*x for x in v]
# Third ee eigenvector lives in EE/body scalar contrast with zero VF component.
v=[F(0)]*8
for i in range(4,7):v[i]=F(1,3)
v[7]=-1;assert vec(k,v)==[ee*x for x in v]
v=[F(1,4)]*4+[F(-2,7)]*3+[F(-1,7)];assert vec(k,v)==[mix*x for x in v]
assert a==F(21,50) and ee==F(9,25) and mix==F(-1,5)
# Native sample memory recurrence: ALL sensor operators, hence ALL initial moments.
sensors=[]
for group in groups:
 p=Z(N)
 for i in group:p[i][i]=F(1)
 sensors.append(p)
def advance(p):return mul(mul(tr(u),p),u)
def flatten(p):return [p[i][j] for i in range(N) for j in range(i,N)]
memory_coeff=[F(1),F(-41,25),F(246,125),F(-246,125),F(41,25)] # C5=sum coeff_j Cj
current_coeff=[F(-1),F(16,25),F(-166,125),F(16,25)]
orbits=[];current_orbits=[]
for p in sensors:
 orbit=[p]
 for _ in range(5):orbit.append(advance(orbit[-1]))
 rhs=Z(N)
 for coefficient,op in zip(memory_coeff,orbit):rhs=add(rhs,sc(coefficient,op))
 assert rhs==orbit[5];orbits.append(orbit)
 deriv=add(mul(p,A),mul(tr(A),p));ops=[deriv]
 for _ in range(4):ops.append(advance(ops[-1]))
 rhs=Z(N)
 for coefficient,op in zip(current_coeff,ops):rhs=add(rhs,sc(coefficient,op))
 assert rhs==ops[4];current_orbits.append(ops)
assert rank([flatten(x) for x in orbits[0][:5]])==5
assert rank([flatten(x) for x in current_orbits[0][:4]])==4
ranks=[rank([flatten(orbits[i][j]) for i in range(7) for j in range(n)]) for n in range(1,6)]
with_body_rank=rank([flatten(orbits[i][j]) for i in range(8) for j in range(5)])
# All 28 signed-current observables satisfy the five-order native rule.
# Individual stationary circulations need not vanish; only aggregate derivatives lose the constant mode.
individual_current_count=0;stationary_current_count=0
for i,j in S['current_incidence_pairs']:
 p=Z(N);p[i][j]=A[i][j];p[j][i]=A[i][j]
 ops=[p]
 for _ in range(5):ops.append(advance(ops[-1]))
 rhs=Z(N)
 for coefficient,op in zip(memory_coeff,ops):rhs=add(rhs,sc(coefficient,op))
 assert rhs==ops[5];individual_current_count+=1
 d1=add(mul(p,A),mul(tr(A),p));d2=add(mul(d1,A),mul(tr(A),d1))
 d3=add(mul(d2,A),mul(tr(A),d2));d4=add(mul(d3,A),mul(tr(A),d3))
 stationary=add(add(p,sc(F(5,16),d2)),sc(F(1,64),d4))
 if stationary!=Z(N):stationary_current_count+=1
assert individual_current_count==28

# Negative control: the same recurrence coefficients must not certify a changed sample step.
u_other=U(F(5,13),F(12,13))
x=e[:];history=[]
for _ in range(5):
 history.append(vec(C,[v*v for v in x]));x=vec(u,x)
expected=[sum(memory_coeff[j]*history[j][i] for j in range(5)) for i in range(8)]
assert expected==vec(C,[v*v for v in x])
x4=e[:]
for _ in range(4):x4=vec(u,x4)
changed=vec(u_other,x4);changed_output=vec(C,[v*v for v in changed])
assert expected!=changed_output

result={'status':'PASS','physical_promotion':0,'independent_review':'pending','lane':'development — no registry entry','numerical_target_evaluated':False,'sampling_fixture':{'cos_2h':str(c),'sin_2h':str(s),'physical_clock':'OPEN'},'coordinate_averaging':{'one_step_diagonal_input':'PASS','repeated_native_equivalence':'FAIL_AS_EXPECTED','second_step_L1_difference':str(sum(abs(x-y) for x,y in zip(coherent2,averaged2))),'paired_plus_body_strong_lumpability':'FAIL_AS_EXPECTED','same_lump_vertex_output':list(map(str,left)),'same_lump_face_output':list(map(str,right))},'stronger_averaging':{'rule':'discard correlations and reset every two-coordinate lump to equal diagonal allocation after every sample','closed_state_dimension':8,'response':'K8=C8 (U elementwise squared) L8','source_formula_points_checked':checks,'stationary_weights':[str(x) for x in pi],'fixture_sector_factors':[str(a),str(ee),str(mix)],'sector_multiplicities':[3,3,1],'quadratic_discrepancy_ceiling_per_step':str(a*a),'native_mechanism':'OPEN; averaging/redistribution is an additional operation'},'native_memory':{'paired_stock_history_order':5,'individual_signed_currents_checked':individual_current_count,'individual_currents_with_possible_stationary_component':stationary_current_count,'signed_aggregate_response_history_order':4,'operator_identity_checked_sensors':8,'single_VF_scalar_minimal_orders':[5,4],'seven_sensor_observable_span_ranks':ranks,'retains_coherent_dynamics':True,'admissibility':'history must be compatible with a PSD native moment; unchanged A and uniform declared h','scalar_history_order_is_not_joint_minimal_packet_size':True,'changed_sample_step':'REJECTED_AS_EXPECTED','observable_memory_dimension_at_fixture':ranks[-1],'observable_memory_dimension_including_body':with_body_rank}}
Path(__file__).with_name('RESPONSE_KERNELS.json').write_text(json.dumps({'U_fixture':[[str(x) for x in r] for r in u],'B15_fixture':[[str(x) for x in r] for r in b],'K8_fixture':[[str(x) for x in r] for r in k],'C8':[[str(x) for x in r] for r in C],'L8':[[str(x) for x in r] for r in L],'history_coefficients_C5_from_C0_C4':list(map(str,memory_coeff)),'history_coefficients_J4_from_J0_J3':list(map(str,current_coeff))},indent=2)+'\n')
print(json.dumps(result,indent=2))
