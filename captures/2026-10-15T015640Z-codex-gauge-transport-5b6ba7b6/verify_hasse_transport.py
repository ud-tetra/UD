#!/usr/bin/env python3
"""Exact Hasse-link construction, independent of the ordered-vertex fixture."""
from pathlib import Path
from itertools import combinations,permutations
import sympy as s,json,hashlib
O=Path(__file__).parent
simp=[t for k in range(1,5) for t in combinations(range(4),k)];n=len(simp);I=s.eye(2)
B=s.zeros(n)
for j,t in enumerate(simp):
 if len(t)>1:
  for a in range(len(t)):B[simp.index(t[:a]+t[a+1:]),j]=(-1)**a
edges=[(i,j) for i in range(n) for j in range(n) if B[i,j]]
checks=[]
def eq(a,b):return all(s.simplify(v)==0 for v in a-b)
def check(name,v):assert v,name;checks.append(name)
def twist(U,r):
 D=s.zeros(n*r)
 for i,j in edges:D[i*r:(i+1)*r,j*r:(j+1)*r]=B[i,j]*U[i,j]
 return D
def rho(p):
 R=s.zeros(n)
 for j,t in enumerate(simp):
  v=[p[a] for a in t];sgn=(-1)**sum(v[a]>v[b] for a in range(len(v)) for b in range(a+1,len(v)))
  R[simp.index(tuple(sorted(v))),j]=sgn
 return R
check('source_f_vector',[sum(len(t)==k for t in simp) for k in range(1,5)]==[4,6,4,1])
check('source_28_incidence_links',len(edges)==28)
# Independent scalar defect.
U={(i,j):s.ones(1) for i,j in edges};e=(simp.index((0,)),simp.index((0,1)));U[e]=s.Matrix([[s.I]])
D=twist(U,1);A=D.conjugate().T-D;L=D.conjugate().T*D+D*D.conjugate().T
check('skew_Hermitian_with_curvature',A.conjugate().T==-A)
check('curvature_defect_identity',-A*A==L-D**2-(D.conjugate().T)**2)
check('nonzero_curvature_rank_one',D**2!=s.zeros(n) and (D**2).rank()==1)
check('Hodge_square_defect_rank_two',(-A*A-L).rank()==2)
# Enumerate all codimension-two diamonds, verify the signed path difference.
diamonds=[]
for i,a in enumerate(simp):
 for k,c in enumerate(simp):
  if len(c)!=len(a)+2 or not set(a)<set(c):continue
  mids=[j for j in range(n) if B[i,j] and B[j,k]];assert len(mids)==2
  j,h=mids;sign=B[i,j]*B[j,k];assert sign==-B[i,h]*B[h,k]
  check(f'diamond_{i}_{k}',eq((D*D)[i:i+1,k:k+1],sign*(U[i,j]*U[j,k]-U[i,h]*U[h,k])))
  diamonds.append((i,j,h,k))
check('18_diamonds',len(diamonds)==18)
# Linearized scalar curvature matrix has rank 14=E-V+1.
C=s.zeros(len(diamonds),len(edges))
for row,(i,j,h,k) in enumerate(diamonds):
 for pair,sgn in [((i,j),1),((j,k),1),((i,h),-1),((h,k),-1)]:C[row,edges.index(pair)]+=sgn
check('diamond_cycle_rank_14',C.rank()==14)
# Non-Abelian rank-two fixture and 24 relabelings of the connection family.
X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1);H=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
U2={(i,j):I for i,j in edges}
for pair,M in zip(edges[:3],[X,Z,H]):U2[pair]=M
D2=twist(U2,2);g=[I,X,Z,H,s.diag(1,s.I)]*3;G=s.diag(*g)
Ug={(i,j):g[i]*T*g[j].conjugate().T for (i,j),T in U2.items()}
check('U2_local_gauge_covariance',eq(twist(Ug,2),G*D2*G.conjugate().T))
for p in permutations(range(4)):
 R=rho(p);Up={}
 for (i,j),T in U2.items():
  pi=simp.index(tuple(sorted(p[v] for v in simp[i])));pj=simp.index(tuple(sorted(p[v] for v in simp[j])))
  Up[pi,pj]=T
 Rp=s.kronecker_product(R,I)
 check('signed_S4_family_'+''.join(map(str,p)),eq(twist(Up,2),Rp*D2*Rp.T))
# Flat non-Abelian fixture, exact conjugation to the native boundary.
P=[I,X,Z,H,s.diag(1,s.I)]*3;F=s.diag(*P)
Uf={(i,j):P[i]*P[j].conjugate().T for i,j in edges};Df=twist(Uf,2)
check('flat_nonabelian_trivialization',eq(Df,F*s.kronecker_product(B,I)*F.conjugate().T))
check('flat_nonabelian_boundary_squared',eq(Df*Df,s.zeros(30)))
# A first-jet temporal gauge transformation and exact local balance.
g1=[s.Matrix([[z]]) for z in [1,s.I,-1,-s.I,1]*3];G1=s.diag(*g1)
Ug1={(i,j):g1[i]*T*g1[j].conjugate().T for (i,j),T in U.items()};Ag=twist(Ug1,1).conjugate().T-twist(Ug1,1)
Omega=s.diag(*[s.I*s.Rational(i,19) for i in range(n)]);T=s.diag(*[s.I*(i%3-1) for i in range(n)]);Op=G1*Omega*G1.conjugate().T+T
check('time_gauge_covariance',eq((Ag+Op)*G1,T*G1+G1*(A+Omega)))
# Mixed temporal curvature is independent of incidence flatness.
mixed_ok=True
for i,j in edges:
 Eold=-Omega[i,i]*U[i,j]+U[i,j]*Omega[j,j]
 Udot=T[i,i]*Ug1[i,j]-Ug1[i,j]*T[j,j]
 Enew=Udot-Op[i,i]*Ug1[i,j]+Ug1[i,j]*Op[j,j]
 mixed_ok &= eq(Enew,g1[i]*Eold*g1[j].conjugate().T)
check('mixed_temporal_curvature_covariance',mixed_ok)

c=s.Matrix([s.Rational(i+1,11)+s.I*s.Rational(i%4,7) for i in range(n)]);v=(A+Omega)*c;stock=s.Matrix([2*s.re(s.conjugate(c[i])*v[i]) for i in range(n)]);flux=s.zeros(n,1)
for i,j in edges:
 J=2*s.re(s.conjugate(c[i])*B[i,j]*U[i,j][0]*c[j]);flux[i]-=J;flux[j]+=J
check('gauge_invariant_support_current_balance',eq(stock,flux))
check('total_support_conserved',s.simplify(sum(stock))==0)
# Independent bipartite-Gram derivation of the phase-controlled spectrum.
even=[i for i,t in enumerate(simp) if (len(t)-1)%2==0];odd=[i for i in range(n) if i not in even]
A0=B.T-B;C0=A0.extract(even,odd);check('native_odd_Gram_four_I',C0.conjugate().T*C0==4*s.eye(7))
row=even.index(simp.index((0,)));col=odd.index(simp.index((0,1)))
v=C0[row,:].T;ee=s.eye(7)[:,col];w=v-ee
check('phase_update_two_plane_geometry',(ee.T*w)[0]==0 and (w.T*w)[0]==2)
for phase in [1,-1,s.I,-s.I,(3+4*s.I)/5]:
 Ut={(i,j):s.ones(1) for i,j in edges};Ut[e]=s.Matrix([[phase]]);Dt=twist(Ut,1);At=Dt.conjugate().T-Dt;Ct=At.extract(even,odd)
 delta=phase-1
 check('phase_Gram_update_'+str(phase),eq(Ct.conjugate().T*Ct,4*s.eye(7)+delta*w*ee.T+s.conjugate(delta)*ee*w.T))
 x=s.symbols('x');expected=x*(x*x+4)**5*((x*x+4)**2-4*(1-s.re(phase)))
 check('phase_full_characteristic_'+str(phase),s.expand(At.charpoly(x).as_expr()-expected)==0)
# Characteristic polynomial is only a fixture, never a physical spectrum.
x=s.symbols('x');poly=str(s.factor(A.charpoly(x).as_expr()))
r={'status':'PASS','check_count':len(checks),'checks':checks,'simplices':[list(t) for t in simp],'incidence_edges':len(edges),'diamond_count':len(diamonds),'scalar_diamond_rank':C.rank(),'curved_fixture':{'link':'vertex0 <- edge01 has i; all other Hasse links identity','D_squared_rank':1,'Hodge_square_defect_rank':2,'skew_characteristic_polynomial':poly},'scope':'Exact finite constructor verification supporting written universal proofs; no independent review or physical correspondence.','physical_promotion':0,'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(O/'HASSE_TRANSPORT_VERIFICATION_v0.1.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
