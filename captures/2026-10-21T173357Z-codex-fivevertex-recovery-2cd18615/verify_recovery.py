from fractions import Fraction as F
from itertools import combinations,permutations
import json

def mm(A,B):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def sc(c,A):return [[c*x for x in row] for row in A]
def ad(A,B):return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def ident(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def trace(A):return sum(A[i][i] for i in range(len(A)))
def chain(tops):
 simplices=[sorted({s for t in tops for s in combinations(t,k+1)}) for k in range(len(tops[0]))]
 flat=sum(simplices,[]);idx={s:i for i,s in enumerate(flat)};n=len(flat);A=[[F(0)]*n for _ in range(n)]
 for group in simplices[1:]:
  for s in group:
   for j in range(len(s)):
    lo=idx[s[:j]+s[j+1:]];hi=idx[s];A[hi][lo]=F((-1)**j);A[lo][hi]=-F((-1)**j)
 return simplices,A
out={}
for name,tops in [('J1_diagonal_Kminus',[(0,1,2,3),(0,1,2,4)]),('pentachoron_boundary',list(combinations(range(5),4)))]:
 s,A=chain(tops);n=len(A);L=sc(-1,mm(A,A));I=ident(n)
 if name.startswith('J1'):
  P3=sc(F(1,6),mm(L,ad(sc(5,I),sc(-1,L))));P5=sc(F(1,10),mm(L,ad(L,sc(-3,I))))
  assert mm(P3,P3)==P3 and mm(P5,P5)==P5 and mm(P3,P5)==sc(0,I)
  assert trace(P3)==8 and trace(P5)==14
  out[name]={'f':[len(x) for x in s],'L_eigenvalues_multiplicities':{'0':1,'3':8,'5':14},'positive_frequency_ratio':'sqrt(5/3)','status':'unit incidence metric only'}
 else:
  P=sc(F(1,5),L);assert mm(P,P)==P and trace(P)==28
  out[name]={'f':[len(x) for x in s],'L_eigenvalues_multiplicities':{'0':2,'5':28},'positive_frequency':'sqrt(5)','status':'unit incidence metric only'}
# Reconstruct THM561 transport exactly on UNSIGNED six-edge basis.
edges=list(combinations(range(4),2));n=6;I=ident(n)
S=[[F(set(e).isdisjoint(f)) for f in edges] for e in edges]
T=[[F(1,2) if e==f else F(1,6) if set(e).isdisjoint(f) else F(1,12) for f in edges] for e in edges]
assert all(sum(row)==1 for row in T)
Pplus=sc(F(1,2),ad(I,S));Pminus=sc(F(1,2),ad(I,sc(-1,S)))
assert mm(T,S)==mm(S,T);assert mm(T,Pminus)==sc(F(1,3),Pminus)
Q=mm(ad(T,sc(-1,I)),ad(T,sc(F(-1,2),I)));assert mm(Q,Pplus)==sc(0,I)
assert trace(Pplus)==3 and trace(Pminus)==3
commute_unsigned=0;commute_signed=0
for g in permutations(range(4)):
 U=[[F(0)]*6 for _ in range(6)];R=[[F(0)]*6 for _ in range(6)]
 for j,(a,b) in enumerate(edges):
  raw=(g[a],g[b]);i=edges.index(tuple(sorted(raw)));U[i][j]=F(1);R[i][j]=F(1 if raw[0]<raw[1] else -1)
 commute_unsigned+=mm(U,T)==mm(T,U);commute_signed+=mm(R,T)==mm(T,R)
assert commute_unsigned==24 and commute_signed<24
# Boundary cannot map a vector in its kernel to nonzero output.
s,A=chain([(0,1,2,3)]);idx={x:i for i,x in enumerate(sum(s,[]))}
faces=s[2];tet=tuple(range(4));coeff=[F((-1)**tet.index(next(v for v in tet if v not in f))) for f in faces]
B=[[A[idx[f]][idx[e]] for f in faces] for e in s[1]] # raising entries = boundary entries transposed
assert mm(B,[[x] for x in coeff])==[[F(0)] for e in s[1]]
out['THM561_transport']={'spectrum':{'1':1,'1/2':2,'1/3':3},'unsigned_S4_commuting':commute_unsigned,'signed_S4_commuting':commute_signed,'H_on_Pminus':'(2/3) I; degenerate but nonzero'}
out['THM562_scope']={'boundary_kernel_annihilated':True,'kernel_cannot_be_mixed_by_boundary_alone':True,'physical_species_identification':'NOT_DERIVED'}
out['physical_promotion']=0;out['status']='PASS_SCOPED_CONSTRUCTOR_ONLY'
print(json.dumps(out,indent=2))
