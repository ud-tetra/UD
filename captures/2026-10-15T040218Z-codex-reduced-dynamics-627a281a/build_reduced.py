from pathlib import Path
from itertools import combinations
import json
import numpy as np
import scipy.linalg as la
import scipy.sparse as sp
R=Path(__file__).resolve().parent
data=json.load(open(R/'baseline/COMPLEX_AND_ACTION.json'))
cells=[[tuple(c) for c in cs] for cs in data['simplices']]
acts=data['signed_simplex_permutations']
ids=[{c:i for i,c in enumerate(cs)} for cs in cells]
orbits=[];loc=[];signloc=[]
for d,cs in enumerate(cells):
 seen=set();oo=[];where={};ss={}
 for i in range(len(cs)):
  if i in seen:continue
  o=[];j=i;sg=1
  for l in range(10):
   assert j not in seen
   where[j]=(len(oo),l);ss[j]=sg;o.append(j);seen.add(j)
   sg*=acts[d][j]['sign'];j=acts[d][j]['destination']
  assert j==i and sg==1
  oo.append(o)
 orbits.append(oo);loc.append(where);signloc.append(ss)
polys=[];full=[]
for d in range(1,4):
 coeff=np.zeros((10,len(orbits[d-1]),len(orbits[d])),dtype=np.int64)
 for col,o in enumerate(orbits[d]):
  c=cells[d][o[0]]
  for k in range(d+1):
   f=ids[d-1][c[:k]+c[k+1:]];row,l=loc[d-1][f]
   coeff[l,row,col]+=(-1)**k*signloc[d-1][f]
 polys.append(coeff)
 rows=[];cols=[];vals=[]
 for col,c in enumerate(cells[d]):
  for k in range(d+1):rows.append(ids[d-1][c[:k]+c[k+1:]]);cols.append(col);vals.append((-1)**k)
 full.append(sp.csc_matrix((vals,(rows,cols)),shape=(len(cells[d-1]),len(cells[d])),dtype=np.int64))
R.mkdir(exist_ok=True)
out={'convention':'B_k(z) is integral Laurent polynomial modulo z^10=1; B_k,m=B_k(exp(2 pi i m/10)); A upper -a_k B_k,m and lower a_k B_k,m dagger','orbit_representatives':[[o[0] for o in oo] for oo in orbits],'signed_orbits':[ [{'indices':o,'signs':[signloc[d][j] for j in o]} for o in oo] for d,oo in enumerate(orbits)],'B_polynomial_entries':[[{'row':int(i),'col':int(j),'power':int(l),'coefficient':int(c[l,i,j])} for l,i,j in zip(*np.nonzero(c))] for c in polys],'block_dimensions':[12,72,120,60]}
(R/'REDUCED_GENERATORS.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
np.savez_compressed(R/'polynomial_arrays.npz',**{f'B{d+1}':a for d,a in enumerate(polys)})
def basis(m,d):
 Q=np.zeros((len(cells[d]),len(orbits[d])),dtype=complex)
 for a,o in enumerate(orbits[d]):
  for l,i in enumerate(o):Q[i,a]=signloc[d][i]*np.exp(-2j*np.pi*m*l/10)/np.sqrt(10)
 return Q
spec=[]
for m in range(10):
 z=np.exp(2j*np.pi*m/10)
 bs=[sum(z**l*c[l] for l in range(10)) for c in polys]
 for d,b in enumerate(bs):assert la.norm(full[d]@basis(m,d+1)-basis(m,d)@b)<1e-11
 assert max(la.norm(bs[d]@bs[d+1]) for d in range(2))<1e-11
 vals=[]
 for d,b in enumerate(bs):
  G=b@b.conj().T if d<2 else b.conj().T@b
  e=la.eigvalsh(G);clusters=[]
  for v in e:
   if not clusters or abs(v-clusters[-1][0])>1e-7:clusters.append([float(v),1])
   else:clusters[-1][1]+=1
  vals.append(clusters)
 spec.append({'m':m,'B1_B2_B3_squared_singular_spectra':vals})
 print(m,vals,flush=True)
(R/'NUMERICAL_DISCOVERY.json').write_text(json.dumps(spec,indent=2)+'\n')
