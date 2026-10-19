"""Conforming midpoint split of each coarse cell's interior octahedron diagonal."""
import sys
sys.dont_write_bytecode=True
from red_mesh import *

def center_pattern():
 mid=(F(1,4),)*4;old=[w for w,perm in pattern()];edges={tuple(sorted((w[i],w[j]))) for w in old for i,j in combinations(range(4),2) if tuple((a+b)/2 for a,b in zip(w[i],w[j]))==mid};assert len(edges)==1;edge=next(iter(edges));out=[]
 for w in old:
  if all(v in w for v in edge):
   for endpoint in edge:out.append(([mid if v==endpoint else v for v in w],F(1,16)))
  else:out.append((w,F(1,8)))
 assert len(out)==12 and sum(weight for w,weight in out)==1
 return old,out,edge

def mesh():
 p,t,_=refine(points,tets);p,t,_=edgewise(p,t);p,t,_=edgewise(p,t);q,ts,P=edgewise(p,t);assert len(p)==285 and len(t)==1024 and len(q)==1785 and len(ts)==8192
 coarseP=[[(j,x) for j,x in enumerate(row) if x] for row in P];old,ref,edge=center_pattern();qnew=q[:];newts=[];newP=[[(i,F(1))] for i in range(len(q))];vol=[];existing=set(q)
 for cell,parent in enumerate(t):
  mapping={}
  for child,weights in zip(ts[8*cell:8*cell+8],old):
   for vi,w in zip(child,weights):
    if w in mapping:assert mapping[w]==vi
    mapping[w]=vi
  c=tuple(sum(p[i][axis] for i in parent)/4 for axis in range(3));assert c not in existing;existing.add(c);index=len(qnew);qnew.append(c);mapping[(F(1,4),)*4]=index;u,v=map(mapping.get,edge);newP.append([(u,F(1,2)),(v,F(1,2))]);assert tuple((a+b)/2 for a,b in zip(q[u],q[v]))==c
  for weights,ratio in ref:
   child=tuple(mapping[w] for w in weights);newts.append(child);vol.append(ratio/512);assert abs(determinant(frame(qnew,child)))==vol[-1]
 def faces(cells):
  d={}
  for tet in cells:
   for f in combinations(sorted(tet),3):d[f]=d.get(f,0)+1
  assert all(n in [1,2] for n in d.values());return {f for f,n in d.items() if n==1}
 boundary=faces(ts);assert faces(newts)==boundary and len(boundary)==1536
 assert len(qnew)==2809 and len(newts)==12288 and sum(vol)==2
 return p,t,q,ts,coarseP,qnew,newts,newP,vol,ref
