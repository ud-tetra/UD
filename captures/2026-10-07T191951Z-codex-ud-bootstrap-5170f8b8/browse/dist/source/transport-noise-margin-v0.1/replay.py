#!/usr/bin/env python3
"""Finite exact profile search and exhaustive integer L-infinity separation."""
import json,itertools,hashlib
from fractions import Fraction as F
from functools import reduce
from operator import xor
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parent
raw=json.loads((R/'sources/MATRICES.json').read_text())['tetrahedron']
nodes=raw['nodes'];A=np.array(raw['skew_generator_A'],dtype=np.int64)
colors=[reduce(xor,s,0) for s in nodes]
checks=[]
def check(n,b):
 assert bool(b),n
 checks.append(n)
check('XOR labels are distinct in every neighbor set',all(len({colors[j] for j in range(15) if A[i,j]})==sum(A[i]!=0) for i in range(15)))
check('color multiplicities 3 4 4 4',[colors.count(i) for i in range(4)]==[3,4,4,4])
best=None;tested=valid=0;ties=[]
for w in itertools.combinations(range(1,33),4):
 if w[-1]>2*w[0]:continue
 tested+=1
 subset=sorted(sum(w[i] for i in range(4) if bits>>i&1) for bits in range(16))
 gap=min(b-a for a,b in zip(subset,subset[1:]))
 if not gap:continue
 valid+=1;Q=4*sum(a*a for a in w)-w[-1]**2
 score=F(4*w[0]*gap,Q)
 if best is None or score>best:best=score;ties=[w]
 elif score==best:ties.append(w)
check('finite profile optimum 4/125 with 4200 tested 3640 admitted',best==F(4,125) and tested==4200 and valid==3640)
check('retained minimal representative among tied optima',ties[0]==(4,5,6,8))
w=(8,4,5,6);a=np.array([w[c] for c in colors],dtype=np.int64);Q=int(a@a)
check('normalized profile has stock ratio 4 and denominator 500',Q==500 and max(a)**2==4*min(a)**2)
signs=np.array([(1,)+x for x in itertools.product((-1,1),repeat=14)],dtype=np.int64)
def derivatives(amp):
 c=signs*amp
 return 2*c*(c@A.T)
d=derivatives(a)
check('all 16384 derivative signatures distinct',len(set(map(tuple,d.tolist())))==16384)
# All ordered pairs in integer arithmetic; blocks avoid a 16384 squared by15 array.
minimum=10**9;pair=None
for start in range(0,len(d),128):
 batch=d[start:start+128]
 dist=np.zeros((len(batch),len(d)),dtype=np.int64)
 for k in range(15):np.maximum(dist,np.abs(batch[:,None,k]-d[None,:,k]),out=dist)
 dist[np.arange(len(batch)),np.arange(start,start+len(batch))]=10**9
 idx=np.unravel_index(np.argmin(dist),dist.shape);v=int(dist[idx])
 if v<minimum:minimum=v;pair=(start+int(idx[0]),int(idx[1]))
check('exhaustive full-state derivative separation meets local lower bound',F(minimum,Q)>=best)
delta=F(minimum,Q)
# Independent general local subset certificate, not nearest-neighbor floating-point lookup.
local=[]
for i in range(15):
 weights=[int(a[j]) for j in range(15) if A[i,j]]
 sums=sorted(sum(weights[j] for j in range(len(weights)) if b>>j&1) for b in range(2**len(weights)))
 gap=min(y-x for x,y in zip(sums,sums[1:]))
 local.append(F(4*int(a[i])*gap,Q))
check('independent local certificate 4/125',min(local)==best)
K=max(F(2*int(a[i])*sum(int(a[j]) for j in range(15) if A[i,j]),Q) for i in range(15))
u=F(1,1000);readout=F(1,100);stock_debit=K*(2*u+u*u)
check('source-independent perturbation coefficient 92/125',K==F(92,125))
check('declared relative-stock and derivative errors fit proved lower margin',readout+stock_debit<best/2)
u2=F(1,100);readout2=F(1,50);debit2=K*(2*u2+u2*u2)
check('one-percent stock and 1/50 derivative allocation fit exact half gap',readout2+debit2<delta/2 and delta==F(2,25))
# Exact maximum-bottleneck spanning tree via descending Kruskal.
edges=[]
for i in range(15):
 for j in range(i+1,15):
  if A[i,j]:edges.append((F(2*int(a[i])*int(a[j]),Q),i,j))
parent=list(range(15))
def find(i):
 while parent[i]!=i:i=parent[i]
 return i
tree=[]
for cap,i,j in sorted(edges,reverse=True):
 if find(i)!=find(j):parent[find(i)]=find(j);tree.append((cap,i,j))
bottleneck=min(e[0] for e in tree)
check('bottleneck tree spans every address',len(tree)==14 and len({find(i) for i in range(15)})==1)
# Optimality witness: removing every edge at or below bottleneck disconnects graph.
parent=list(range(15))
for cap,i,j in edges:
 if cap>bottleneck:parent[find(i)]=find(j)
check('strictly better tree bottleneck is obstructed by a cut',len({find(i) for i in range(15)})>1)
check('equal-stock tree margin 2/15 exceeds selected tree bottleneck',F(2,15)>bottleneck)
eq=derivatives(np.ones(15,dtype=np.int64))
check('equal-stock derivative collisions retained',len(set(map(tuple,eq.tolist())))==16256)
result={'status':'PASS','exact_checks':len(checks),'checks':checks,'finite_search':{'range':'four distinct integers 1..32; max/min <=2','tested':tested,'admitted':valid,'best_certified_margin':str(best),'tied_weights':ties},'profile':{'color_weights':w,'address_weights':a.tolist(),'Q':Q,'stock_range':4},'exact_derivative_gap':str(delta),'integer_gap':minimum,'closest_ray_indices':pair,'closest_sign_rays':[signs[i].tolist() for i in pair],'closest_derivatives':[d[i].tolist() for i in pair],'local_lower_bound':str(best),'K':str(K),'uncertainty_contract':{'relative_stock_error':str(u),'derivative_error':str(readout),'stock_debit':str(stock_debit),'total_error':str(readout+stock_debit),'proved_half_margin':str(best/2)},'expanded_contract':{'relative_stock_error':str(u2),'derivative_error':str(readout2),'stock_debit':str(debit2),'total_error':str(readout2+debit2),'exact_half_margin':str(delta/2),'slack':str(delta/2-readout2-debit2)},'tree_bottleneck':str(bottleneck),'tree':[[str(cap),i,j] for cap,i,j in tree],'physical_promotion':0,'independent_review':'PENDING','matrix_sha256':hashlib.sha256((R/'sources/MATRICES.json').read_bytes()).hexdigest()}
(R/'REPLAY_RECEIPT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
