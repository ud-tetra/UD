from itertools import permutations,product
from fractions import Fraction
import sympy as s,json
from geometry import nodes,edges
Pphase=s.zeros(28);Pd=s.zeros(15);aa=[1,1,-1,-1];group=[]
def act(p):
 mp=[nodes.index(tuple(sorted(p[i] for i in a))) for a in nodes];L=s.zeros(28);D=s.zeros(15)
 for j,i in enumerate(mp):D[i,j]=1
 for j,(i,k) in enumerate(edges):L[edges.index((mp[i],mp[k])),j]=1
 return L,D
for p in permutations(range(4)):
 for sig in [-1,1]:
  if all(sig*aa[i]==aa[p[i]] for i in range(4)):
   L,D=act(p);Pphase+=sig*L;Pd+=D;group.append((p,sig))
Pphase/=len(group);Pd=Pd/len(group)-s.ones(15)/15
out={}
for name in ['radial','angular']:
 if name=='angular':
  Pphase=s.zeros(28);Pd=s.zeros(15)
  for x,y in product([0,1],repeat=2):
   p=[1,0,2,3] if x else [0,1,2,3]
   if y:p[2],p[3]=p[3],p[2]
   L,D=act(p);Pphase+=(-1)**x*L/4;Pd+=(-1)**x*D/4
 B=s.Matrix.hstack(*Pphase.columnspace());D=s.Matrix.hstack(*Pd.columnspace());print(name,'phase',B.cols,'density',D.cols,flush=True)
 assert Pphase*Pphase==Pphase and Pd*Pd==Pd
 assert Pphase*B==B and Pd*D==D and s.ones(1,15)*D==s.zeros(1,D.cols)
 assert (B.cols,D.cols)==({'radial':(5,4),'angular':(7,3)}[name])
 out[name]={'phase_basis':[[str(v) for v in row] for row in B.tolist()],'density_basis':[[str(v) for v in row] for row in D.tolist()]}
open('SECTOR_BASES_v0.1.json','w').write(json.dumps(out,indent=2)+'\n')
