from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

def z(n,m):return [[F(0) for j in range(m)] for i in range(n)]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def tr(A):return list(map(list,zip(*A)))
def mm(A,B):return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def sc(c,A):return [[c*x for x in row] for row in A]
def ad(*As):return [[sum(A[i][j] for A in As) for j in range(len(As[0][0]))] for i in range(len(As[0]))]
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def mv(A,v):return [dot(r,v) for r in A]
def cols(V):return tr(V)
def norm(v):return dot(v,v)
N=23;tops=[(0,1,2,3),(0,1,2,4)];simp=[sorted({s for t in tops for s in combinations(t,k+1)}) for k in range(4)];flat=sum(simp,[]);ix={s:i for i,s in enumerate(flat)};A=z(N,N)
for group in simp[1:]:
 for s in group:
  for j in range(len(s)):
   lo=ix[s[:j]+s[j+1:]];hi=ix[s];A[hi][lo]=F((-1)**j);A[lo][hi]=-F((-1)**j)
I=eye(N);L=sc(-1,mm(A,A));P3=sc(F(1,6),mm(L,ad(sc(5,I),sc(-1,L))));P5=sc(F(1,10),mm(L,ad(L,sc(-3,I))));P0=ad(I,sc(-1,P3),sc(-1,P5))
assert ad(P0,P3,P5)==I
# Recovered THM561 T on ascending UNSIGNED edge coordinates.
edges=list(combinations(range(4),2));T=[[F(1,2) if e==f else F(1,6) if set(e).isdisjoint(f) else F(1,12) for f in edges] for e in edges];H=ad(eye(6),sc(-1,T))
u0=[F(1)]*6
b=[[F(int(j==k)+int(j==5-k)) for j in range(6)] for k in range(3)]
u1=[x-y for x,y in zip(b[0],b[1])];u2=[x+y-2*w for x,y,w in zip(b[0],b[1],b[2])]
anti=[[F(int(j==k)-int(j==5-k)) for j in range(6)] for k in range(3)]
Uvec=[u0,u1,u2]+anti;U=cols(Uvec);Ui=[[x/norm(v) for x in v] for v in Uvec];assert mm(Ui,U)==eye(6)
hvals=[F(0),F(1,2),F(1,2),F(2,3),F(2,3),F(2,3)]
for u,h in zip(Uvec,hvals):assert mv(H,u)==[h*x for x in u]
Fop=ad(sc(F(3,2),H),sc(9,mm(H,H)));lam=[0,3,3,5,5,5]
for u,l in zip(Uvec,lam):assert mv(Fop,u)==[l*x for x in u]
Falt=ad(sc(F(53,2),H),sc(-33,mm(H,H)))
for u,l in zip(Uvec,[0,5,5,3,3,3]):assert mv(Falt,u)==[l*x for x in u]
# Scalar-only L E = s E H cannot retain both positive H eigenspaces.
scalar_checks=[]
for l1,l2 in [(3,5),(5,3)]:
 s1=F(l1,1)/F(1,2);s2=F(l2,1)/F(2,3)
 assert s1!=s2
 scalar_checks.append({'image_of_half':l1,'image_of_two_thirds':l2,'required_scales':[str(s1),str(s2)]})
# Injections cannot collapse distinct source eigenspaces at the same L eigenvalue?
# A common scalar s keeps eigenvalues distinct; only two assignments above exist.
# Choose rational, pairwise orthogonal q axes with isotropic A pairing.
def axes(P,count):
 chosen=[]
 for raw in tr(P):
  v=list(raw)
  for q in chosen:
   aq=mv(A,q)
   for w in (q,aq):
    c=dot(v,w)/norm(w);v=[x-c*y for x,y in zip(v,w)]
  if norm(v):chosen.append(v)
  if len(chosen)==count:break
 assert len(chosen)==count
 return chosen
v0=[F(int(len(s)==1)) for s in flat];Vvec=[v0]+axes(P3,2)+axes(P5,3);V=cols(Vvec);E=mm(V,Ui)
assert mm(L,E)==mm(E,Fop)
assert mm(tr(E),mm(A,E))==z(6,6)
# Reduced phase coordinates: q0,q1..q5,v1..v5. Harmonic momentum is fixed zero.
Dvec=Vvec+[[x/F(lam[j]) for x in mv(sc(-1,A),Vvec[j])] for j in range(1,6)];D=cols(Dvec);K=z(11,11)
for j in range(1,6):K[j][j+5]=F(1);K[j+5][j]=-F(lam[j])
assert mm(A,D)==mm(D,K)
G=mm(tr(D),D);assert all(G[i][j]==0 for i in range(11) for j in range(11) if i!=j);assert all(G[i][i]>0 for i in range(11))
B=[[x/G[i][i] for x in row] for i,row in enumerate(tr(D))]
assert mm(B,D)==eye(11) and mm(B,mm(A,D))==K
assert ad(mm(tr(K),G),mm(G,K))==z(11,11)
W=mm(D,B);assert mm(W,W)==W and mm(W,A)==mm(A,W)
# Rational orthogonal commuting phase change: two equally compatible embeddings.
C=ad(P0,sc(F(-1,2),P3),sc(F(1,2),mm(A,P3)),sc(F(-2,3),P5),sc(F(1,3),mm(A,P5)))
assert mm(tr(C),C)==I and mm(C,A)==mm(A,C)
Dalt=mm(C,D);assert Dalt!=D and mm(A,Dalt)==mm(Dalt,K) and mm(tr(Dalt),Dalt)==G
# Omitted zero-mode momentum creates a Jordan drift; skew target cannot realize it.
# If A p=q0 and A q0=0, then ||q0||²=<q0,A p>=-<A q0,p>=0, contradiction.
assert mv(A,v0)==[F(0)]*23 and norm(v0)>0
out={'status':'PASS_SCOPED_CONSTRUCTOR_ONLY','direct_generator_map':'NO_INJECTIVE_MAP: real nonpositive transport generator versus skew A','scalar_laplacian_map':{'verdict':'NO_INJECTIVE_MAP_FOR_s_POSITIVE','assignments':scalar_checks},'inverse_spectral_interpolation':{'f(H)':'(3/2)H+9H^2','alternative':'(53/2)H-33H^2 swaps target eigenvalues','source_selected':False},'conditional_phase_lift':{'source_dimension':11,'target_dimension':23,'rank':11,'unobserved_complement_dimension':12,'removed_coordinate':'harmonic momentum; retain harmonic displacement','AD_equals_DK':True,'BD_identity':True,'metric_diagonal':[str(G[i][i]) for i in range(11)],'metric_status':'pulled back; not assumed legacy Euclidean phase metric','two_distinct_same_metric_embeddings':True},'limits':['inverse native-spectral interpolation is not a source law','no particle labels, physical action or clock calibration','no geometric J1 metric or global symmetry intertwiner asserted','no full 12D harmonic-drift lift','readout is a mathematical candidate, not an apparatus'], 'physical_promotion':0}
# Exact matrices permit independent identity checking without reproducing axis selection.
witness={'A':A,'T':T,'H':H,'Fop':Fop,'E':E,'D':D,'K':K,'G':G,'B':B,'Dalt':Dalt}
enc=lambda a:[[str(x) for x in row] for row in a]
if __name__=='__main__':
 p=Path(__file__).resolve().parent
 (p/'MAP_WITNESSES.json').write_text(json.dumps({k:enc(v) for k,v in witness.items()},indent=2)+'\n')
 print(json.dumps(out,indent=2))
