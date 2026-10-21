from fractions import Fraction as F
from itertools import combinations,permutations
import json
n=6;E=list(combinations(range(4),2))
def eye():return [[F(i==j) for j in range(n)] for i in range(n)]
def mm(A,B):return [[sum(a*b for a,b in zip(r,c)) for c in zip(*B)] for r in A]
def avg(As):return [[sum(A[i][j] for A in As)/len(As) for j in range(n)] for i in range(n)]
I=eye();S=[[F(set(e).isdisjoint(f)) for f in E] for e in E];R=[]
for g in permutations(range(4)):
 P=[[F(0)]*6 for _ in range(6)]
 for j,e in enumerate(E):P[E.index(tuple(sorted(g[v] for v in e)))][j]=F(1)
 R.append(P)
labels=[I]*20+[S]*4+R
T=avg(labels);declared=[[F(1,2) if e==f else F(1,6) if set(e).isdisjoint(f) else F(1,12) for f in E] for e in E]
assert len(labels)==48 and T==declared
assert all(all(sum(row)==1 for row in P) for P in labels)
iid=mm(T,T);quenched=avg([mm(P,P) for P in labels]);assert iid!=quenched
assert all(iid[i][i]==F(11,36) for i in range(6));assert all(quenched[i][i]==F(3,4) for i in range(6))
for M in (T,iid,quenched):
 assert all(sum(row)==1 for row in M) and all(x>=0 for row in M for x in row)
 assert all(sum(M[i][j] for i in range(6))==1 for j in range(6))
# Negative control: quenched-label second step cannot be scored as T^2.
assert quenched[0][0]-iid[0][0]==F(4,9)
# The matrix entries constrain probabilities, not a source measure on labels.
print(json.dumps({'status':'PASS_SCOPED_CONSTRUCTOR_ONLY','labels':{'identity_copies':20,'opposite_swap_copies':4,'unsigned_vertex_permutations':24,'total':48},'construction_status':'INVERSE_ILLUSTRATIVE_REALIZATION_NOT_RECOVERED_THM534','one_step':'both exactly T_self=1/2,T_opposite=1/6,T_cross=1/12','two_steps':{'iid_resampling_diagonal':'11/36','single_quenched_label_diagonal':'3/4','difference':'4/9'},'conclusion':'same one-step kernel does not fix hidden-label temporal law','limits':['iid versus quenched are distinct declared processes','48-label weights were selected to realize T, not derived from UD','neither realization supplies f(H), energy, action units, species or physical time','THM534 original source remains not located in bounded search'],'physical_promotion':0},indent=2))
