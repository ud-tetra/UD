from pathlib import Path
from fractions import Fraction as F
from itertools import permutations
import json,hashlib
C=Path(__file__).parent
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def tr(a):return list(map(list,zip(*a)))
def mm(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(a,x):return [[x*y for y in r] for r in a]
def comm(a,b):return add(mm(a,b),scale(mm(b,a),-1))
def zero(a):return all(x==0 for r in a for x in r)
def serialize(a):return [[str(x) for x in r] for r in a]
def write(n,d):(C/n).write_text(json.dumps(d,indent=2)+'\n')
n=6;I=eye(n);J=[[F(1) for j in range(n)] for i in range(n)]
edges=[(0,1),(2,3),(0,2),(1,3),(0,3),(1,2)]
S=[[F(j==i^1) for j in range(n)] for i in range(n)]
D=[[F((1,-1,1)[i//2] if j==i^1 else 0) for j in range(n)] for i in range(n)]
T=[[F(1,2) if i==j else F(1,6) if j==i^1 else F(1,12) for j in range(n)] for i in range(n)]
Pp=scale(add(I,S),F(1,2));Pm=scale(add(I,scale(S,-1)),F(1,2))
E1=scale(J,F(1,6));Eh=add(Pp,scale(E1,-1));Et=Pm
H=add(I,scale(T,-1));assert T==tr(T) and all(sum(r)==1 for r in T)
assert mm(S,S)==I and mm(D,D)==I and zero(comm(S,D))
assert zero(comm(T,S)) and not zero(comm(T,D))
for E,lam,rank in [(E1,F(1),1),(Eh,F(1,2),2),(Et,F(1,3),3)]:
 assert mm(E,E)==E and E==tr(E) and sum(E[i][i] for i in range(n))==rank
 assert mm(T,E)==scale(E,lam)
assert add(add(E1,Eh),Et)==I
joint={}
for s in (1,-1):
 for h in (1,-1):
  p=scale(mm(add(I,scale(S,s)),add(I,scale(D,h))),F(1,4));assert mm(p,p)==p
  joint[f'S{s:+}_star{h:+}']={'matrix':serialize(p),'rank':int(sum(p[i][i] for i in range(n)))}
assert [joint[k]['rank'] for k in joint]==[2,1,1,2]
counts={'unsigned':0,'canonical_signed':0}
for perm in permutations(range(4)):
 for signed,key in [(False,'unsigned'),(True,'canonical_signed')]:
  P=[[F(0) for _ in range(n)] for _ in range(n)]
  for j,(a,b) in enumerate(edges):
   x,y=perm[a],perm[b];k=edges.index(tuple(sorted((x,y))));P[k][j]=F(-1 if signed and x>y else 1)
  counts[key]+=int(zero(comm(T,P)))
assert counts=={'unsigned':24,'canonical_signed':2}
# The orthonormal Pplus injection has columns (e_2j+e_2j+1)/sqrt2.
E=[[F(i//2==j) for j in range(3)] for i in range(6)]
assert mm(tr(E),E)==scale(eye(3),2)
tp=scale(mm(mm(tr(E),T),E),F(1,2))
assert tp==[[F(i==j,2)+F(1,6) for j in range(3)] for i in range(3)]
# Corrected coupling, evaluated without floating radical approximations.
a=[0,-1];b=[2,-1];YY=[[F(a[i]*a[j],6)+F(b[i]*b[j],18) for j in range(2)] for i in range(2)]
assert YY==[[F(2,9),F(-1,9)],[F(-1,9),F(2,9)]]
assert YY[0][0]+YY[1][1]==F(4,9) and YY[0][0]*YY[1][1]-YY[0][1]**2==F(1,27)
# Nonunitary coordinate change preserves the norm only with transported metric.
U=eye(n);U[0][0]=2;V=eye(n);V[0][0]=F(1,2)
Gnew=mm(tr(V),V);Tnew=mm(mm(U,T),V)
assert mm(Gnew,Tnew)==mm(tr(Tnew),Gnew)
x=[[F(i==0)] for i in range(n)]
def inner(a,b,g):return mm(mm(tr(a),g),b)[0][0]
def fidelity(x,t,g):
 y=mm(t,x);return inner(x,y,g)**2/(inner(x,x,g)*inner(y,y,g))
assert fidelity(x,T,I)==fidelity(mm(U,x),Tnew,Gnew)
assert fidelity(x,T,I)!=fidelity(mm(U,x),Tnew,I)
spec={'specification':'UD corrected six-channel particle-candidate algebra v0.1','status':'FROZEN_DEVELOPMENT_SPECIFICATION__NOT_PREREGISTERED','physical_promotion':0,'coordinate_order':[list(e) for e in edges],'scalar_field':'real matrices with optional mathematical complexification; physical Hilbert map unproved','metric':{'G':serialize(I),'type':'declared dimensionless positive definite reference metric','change_of_coordinates':'x_new=U x; T_new=U T U^-1; G_new=(U^-1)^dagger G U^-1','allowed_fixed_metric_changes':'unitary; orthogonal in the real register'},'operators':{'T':serialize(T),'S_opposite_pair':serialize(S),'star_declared_channel_involution':serialize(D),'H_diagnostic_I_minus_T':serialize(H)},'spectral_projectors':{'lambda_1':serialize(E1),'lambda_1_2':serialize(Eh),'lambda_1_3':serialize(Et)},'joint_S_star_projectors':joint,'coupling_contract':{'Pplus_orthonormal_basis':'p_j=(e_2j+e_2j+1)/sqrt2, j=0,1,2','u':['1/sqrt3']*3,'w1':['1/sqrt2','-1/sqrt2','0'],'w2':['1/sqrt6','1/sqrt6','-2/sqrt6'],'L1':'p0','L2':'p2','R':'p1','H_j':'u w_j^T + w_j u^T within Pplus','Y':[['0','2/sqrt18'],['-1/sqrt6','-1/sqrt18']],'YY_dagger':serialize(YY),'singular_values_squared':['1/3','1/9'],'basis_scope':'real orthonormal Higgs-basis rotations; absolute determinant invariant; entrywise nonzero not invariant'},'typing_limits':['unsigned edge permutation representation is distinct from signed simplicial chains','joint S/star decomposition is not preserved by T in general','T is a declared discrete positive kernel; H is a diagnostic quadratic form, no new temporal generator or physical energy law inferred','no species identification, VEV, mass map, physical action coefficient or clock supplied'],'source_commit':'c6b66d68a25b655627d6eb6f1bf6f96a13e2121b','sources':['docs/THM-561_Weak_Color_Mass_Split_v1.0.md','docs/THM-563a_Four_Sector_Chirality_v1.0.md','docs/THM-565a_Nonzero_LR_Higgs_Element_v1.0.md','docs/THM-566_Yukawa_Ratio_Root3_v1.0.md','docs/THM-LS1_Retention_Fidelity_v1.0.md'],'independent_review':'PENDING'}
write('FROZEN_OPERATORS.json',spec)
digest=hashlib.sha256((C/'FROZEN_OPERATORS.json').read_bytes()).hexdigest()
write('FREEZE_RECEIPT.json',{'status':'FROZEN_SCOPED_CONSTRUCTOR_MATHEMATICS','sha256':digest,'file':'FROZEN_OPERATORS.json','physical_promotion':0,'registration':'NOT_PREREGISTERED','checked':['positive reference metric and transported-metric covariance','T symmetry/stochasticity and exact spectral projectors','joint involution projector dimensions','T/star noncommutation','unsigned24 vs signed2 permutation commutations','coupling Gram invariants and admitted zero entry'],'symmetry_commuting_counts':counts,'independent_review':'PENDING'})
print(json.dumps({'status':'PASS','frozen_sha256':digest,'physical_promotion':0}))
