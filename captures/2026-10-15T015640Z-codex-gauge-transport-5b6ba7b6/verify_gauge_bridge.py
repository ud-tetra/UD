#!/usr/bin/env python3
"""Fresh exact fixtures for the stated gauge-transport theorem; no data fitting."""
from itertools import combinations, permutations
from pathlib import Path
import hashlib,json
import sympy as s
OUT=Path(__file__).parent
checks=[]
def check(name,predicate):
 assert predicate,name
 checks.append(name)
def eq(a,b):return all(s.simplify(x)==0 for x in a-b)
def simplices(cells):
 return [sorted(set(t for cell in cells for t in combinations(cell,k+1))) for k in range(4)]
def boundary(ss,U,r):
 blocks=[]
 for k in range(1,4):
  M=s.zeros(len(ss[k-1])*r,len(ss[k])*r)
  for j,t in enumerate(ss[k]):
   for a in range(k+1):
    f=t[:a]+t[a+1:];i=ss[k-1].index(f)
    T=U[f[0],t[0]] if a==0 else s.eye(r)
    M[i*r:(i+1)*r,j*r:(j+1)*r]=(-1)**a*T
  blocks.append(M)
 offsets=[0]
 for x in ss:offsets.append(offsets[-1]+len(x)*r)
 D=s.zeros(offsets[-1])
 for k,M in enumerate(blocks,1):D[offsets[k-1]:offsets[k],offsets[k]:offsets[k+1]]=M
 return blocks,D

def gauge_blocks(ss,g):return s.diag(*[g[t[0]] for level in ss for t in level])
def native(ss):return boundary(ss,{(i,j):s.eye(1) for i in range(5) for j in range(5)},1)[1]
ss=simplices([(0,1,2,3)])
D0=native(ss);A0=D0.T-D0;P=s.zeros(15)
for i in range(4):
 for j in range(4):P[i,j]=s.Rational(1,4)
check('native_boundary_squared',D0*D0==s.zeros(15))
check('native_active_complex_structure',A0*A0==-4*(s.eye(15)-P))
# Global centralizers via direct rational linear equations; pair-sum matrices.
def skew_basis(n):
 out=[]
 for i in range(n):
  for j in range(i+1,n):
   X=s.zeros(n);X[i,j]=1;X[j,i]=-1;out.append(X)
 return out
basis=skew_basis(15)
def action(p):
 rows=[t for level in ss for t in level];M=s.zeros(15)
 for i,t in enumerate(rows):
  im=tuple(p[v] for v in t);inversions=sum(im[a]>im[b] for a in range(len(im)) for b in range(a+1,len(im)))
  M[rows.index(tuple(sorted(im))),i]=(-1)**inversions
 return M
rho=[action(p) for p in permutations(range(4))]
check('all_24_signed_actions_commute',all(M*A0==A0*M for M in rho))
def constraint_dim(matrices):
 blocks=[]
 for M in matrices:
  blocks.append(s.Matrix.hstack(*[s.Matrix(X*M-M*X).reshape(225,1) for X in basis]))
 return len(basis)-s.Matrix.vstack(*blocks).rank()
check('global_skew_centralizer_dimension_49',constraint_dim([A0])==49)
generators=[action((1,0,2,3)),action((1,2,3,0))]
check('S4_compatible_skew_dimension_3',constraint_dim(generators+[A0])==3)
# Rank-one connection with exactly one nontrivial edge.
U={(i,j):s.eye(1) for i in range(4) for j in range(4)};U[1,0]=s.Matrix([[s.I]]);U[0,1]=s.Matrix([[-s.I]])
bs,D=boundary(ss,U,1);A=D.conjugate().T-D;L=D.conjugate().T*D+D*D.conjugate().T
check('curved_generator_skew_Hermitian',A.conjugate().T==-A)
check('curvature_square_identity',-A*A==L-D*D-(D.conjugate().T)**2)
check('curvature_breaks_chain',D*D!=s.zeros(15))
check('curvature_breaks_old_Hodge_square',-A*A!=L)
curvature_ranks={'B1B2':(bs[0]*bs[1]).rank(),'B2B3':(bs[1]*bs[2]).rank(),'D2':(D*D).rank(),'Hodge_square_defect':(-A*A-L).rank()}
x=s.symbols('x');poly=s.factor(A.charpoly(x).as_expr())
# Check the analytic codimension-two coefficient for every simplex and row.
for k in [2,3]:
 actual=bs[k-2]*bs[k-1];expected=s.zeros(*actual.shape)
 for j,t in enumerate(ss[k]):
  f=t[2:];i=ss[k-2].index(f)
  expected[i,j]=(U[t[2],t[1]]*U[t[1],t[0]]-U[t[2],t[0]])[0]
 check(f'explicit_curvature_block_degree_{k}',eq(actual,expected))
g=[s.Matrix([[z]]) for z in [1,s.I,-1,-s.I]];G=gauge_blocks(ss,g)
Ug={(i,j):g[i]*U[i,j]*g[j].conjugate().T for i in range(4) for j in range(4)}
_,Dg=boundary(ss,Ug,1)
check('U1_boundary_gauge_covariance',eq(Dg,G*D*G.conjugate().T))
check('U1_generator_gauge_covariance',eq(Dg.conjugate().T-Dg,G*A*G.conjugate().T))
# Independent non-Abelian rank-two fixture (Pauli/Hadamard; exactly algebraic).
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1);H=s.Matrix([[1,1],[1,-1]])/s.sqrt(2);Y=s.Matrix([[0,-s.I],[s.I,0]])
U2={(i,j):I for i in range(4) for j in range(4)}
for pair,T in [((1,0),X),((2,1),Z),((3,2),H),((2,0),Y)]:U2[pair]=T;U2[pair[::-1]]=T.conjugate().T
b2,D2=boundary(ss,U2,2);g2=[I,H,X,s.diag(1,s.I)];G2=gauge_blocks(ss,g2)
U2g={(i,j):g2[i]*U2[i,j]*g2[j].conjugate().T for i in range(4) for j in range(4)}
_,D2g=boundary(ss,U2g,2)
check('U2_noncommuting_connection',X*Z!=Z*X)
check('U2_boundary_gauge_covariance',eq(D2g,G2*D2*G2.conjugate().T))
check('U2_square_curvature_identity',eq(-(D2.conjugate().T-D2)**2,D2.conjugate().T*D2+D2*D2.conjugate().T-D2**2-(D2.conjugate().T)**2))
# Flat rank-two transport is exactly trivializable; repeated native spectrum.
frames=[I,X,Z,H];Uf={(i,j):frames[i]*frames[j].conjugate().T for i in range(4) for j in range(4)}
_,Df=boundary(ss,Uf,2);F=gauge_blocks(ss,frames)
check('flat_connection_nilpotent',eq(Df*Df,s.zeros(30)))
check('flat_unitary_trivialization',eq(Df,F*s.kronecker_product(D0,I)*F.conjugate().T))
# Non-simply-connected exception: circle graph, no triangular faces.
circle=[[(0,),(1,),(2,)],[(0,1),(0,2),(1,2)],[],[]]
Uc={(i,j):s.eye(1) for i in range(3) for j in range(3)};Uc[1,0]=s.Matrix([[s.I]]);Uc[0,1]=s.Matrix([[-s.I]])
_,Dc=boundary(circle,Uc,1)
check('circle_flat_but_nontrivial_holonomy',Dc*Dc==s.zeros(6) and (Uc[0,2]*Uc[2,1]*Uc[1,0])[0]!=1)
# Pure-state relative phases telescope on arbitrary closed paths.
z=[1,s.I,-1,(3+4*s.I)/5]
check('state_phase_receipt_loop_is_one',s.simplify(s.prod(s.conjugate(z[i])*z[j] for i,j in [(0,1),(1,2),(2,3),(3,0)]))==1)
# Time-dependent frame term via exact first jet Gdot=TG, Omega'=G Omega G^*+T.
T=s.diag(*[s.I*(i%3-1) for i in range(15)]);Omega=s.diag(*[s.I*s.Rational(i,17) for i in range(15)])
Op=G*Omega*G.conjugate().T+T
check('temporal_connection_inhomogeneous_term',eq((Dg.conjugate().T-Dg+Op)*G,T*G+G*(A+Omega)))
# Current balance for one exact arbitrary complex state, including local skew blocks.
c=s.Matrix([s.Rational(i+1,11)+s.I*s.Rational((i*i)%7,13) for i in range(15)])
v=(A+Omega)*c;stock=s.Matrix([2*s.re(s.conjugate(c[i])*v[i]) for i in range(15)]);flux=s.zeros(15,1)
for i in range(15):
 for j in range(15):
  if D[i,j]!=0:
   J=2*s.re(s.conjugate(c[i])*D[i,j]*c[j]);flux[i]-=J;flux[j]+=J
check('exact_stock_current_balance',eq(stock,flux))
check('exact_total_norm_derivative_zero',s.simplify(sum(stock))==0)
# SU(5) normalization is conditional on the explicitly supplied embedding.
Y5=s.diag(-s.Rational(1,3),-s.Rational(1,3),-s.Rational(1,3),s.Rational(1,2),s.Rational(1,2))
check('conditional_SU5_hypercharge_trace',s.trace(Y5*Y5)==s.Rational(5,6))
check('conditional_SU5_normalized_trace',s.trace(s.Rational(3,5)*Y5*Y5)==s.Rational(1,2))
receipt={'status':'PASS','arithmetic':'exact SymPy rational/Gaussian-rational/algebraic arithmetic','check_families':checks,'count':len(checks),'curved_fixture':{'link':'U_10=i, reverse=-i, other links=1','ranks':curvature_ranks,'skew_characteristic_polynomial':str(poly),'triangle_W012':'i','triangle_normalized_curvature':1},'scope':'Finite fixtures support self-contained written proofs. No physical measurement, independent review, quantum field action or continuum limit.','physical_promotion':0,'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(OUT/'GAUGE_BRIDGE_VERIFICATION_v0.1.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
