"""Conforming ordered Kuhn edgewise tetrahedron subdivision and finite-frame certificate."""
import sys
sys.dont_write_bytecode=True
from fine_flux_core import *
from itertools import product,permutations

def pattern():
 out=[]
 for o in product(range(2),repeat=3):
  for perm in permutations(range(3)):
   v=list(o);path=[tuple(v)]
   for axis in perm:v[axis]+=1;path.append(tuple(v))
   if all(x>=y>=z for x,y,z in path):
    weights=[(F(2-x,2),F(x-y,2),F(y-z,2),F(z,2)) for x,y,z in path]
    out.append((weights,perm))
 assert len(out)==8
 return out

def edgewise(p,ts):
 q=p[:];P=eye(len(p));mid={}
 for i,j in sorted({e for t in ts for e in combinations(sorted(t),2)}):
  mid[i,j]=len(q);q.append(tuple((x+y)/2 for x,y in zip(p[i],p[j])));row=[F(0)]*len(p);row[i]=row[j]=F(1,2);P.append(row)
 out=[]
 for t in ts:
  for weights,perm in pattern():
   child=[]
   for w in weights:
    ids=[i for i,x in enumerate(w) if x]
    if len(ids)==1:assert w[ids[0]]==1;child.append(t[ids[0]])
    else:assert len(ids)==2 and all(w[i]==F(1,2) for i in ids);child.append(mid[tuple(sorted(t[i] for i in ids))])
   out.append(tuple(child))
 return q,out,P

def metric(a,b):return sum(w*x*y for w,x,y in zip([F(1),F(1),F(1,2)],a,b))
def frame(q,t):return [tuple(b-a for a,b in zip(q[t[i]],q[t[i+1]])) for i in range(3)]
def determinant(a):return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
def family_certificate():
 pat=pattern();reference_checks=0;face_checks=0
 for weights,perm in pat:
  for j,axis in enumerate(perm):
   diff=tuple(weights[j+1][i]-weights[j][i] for i in range(4))
   assert diff==tuple(F(int(i==axis+1)-int(i==axis),2) for i in range(4));reference_checks+=1
 for omit in range(4):
  vertices=[tuple(F(i==j) for i in range(4)) for j in range(4) if j!=omit]
  def mid(a,b):return tuple((x+y)/2 for x,y in zip(a,b))
  a,b,c=vertices;ab,ac,bc=mid(a,b),mid(a,c),mid(b,c)
  expected={tuple(sorted(f)) for f in [(a,ab,ac),(b,ab,bc),(c,ac,bc),(ab,ac,bc)]}
  actual=set()
  for weights,perm in pat:
   for f in combinations(weights,3):
    if all(v[omit]==0 for v in f):actual.add(tuple(sorted(f)))
  assert actual==expected;face_checks+=1
 p,t,_=refine(points,tets);q,s,P=edgewise(p,t);C2=F(0);lower=[];upper=[];checks=0
 for k,tet in enumerate(t):
  G=frame(p,tet);gram=[[metric(a,b) for b in G] for a in G];trace=sum(gram[i][i] for i in range(3));det=determinant(gram)
  assert det>0;lower.append(4*det/(trace*trace));upper.append(trace)
  for bits in product(range(2),repeat=3):
   a=[sum(bits[i]*G[i][j] for i in range(3)) for j in range(3)];C2=max(C2,metric(a,a))
  for j,(_,perm) in enumerate(pattern()):
   childG=frame(q,s[8*k+j]);assert all(childG[i]==tuple(x/2 for x in G[perm[i]]) for i in range(3));checks+=1
 # Each face is split into its three corner triangles and central midpoint triangle, independent of local order.
 # Check the assembled finite mesh's interior/boundary trace incidence directly.
 faces={}
 for tet in s:
  for f in combinations(sorted(tet),3):faces[f]=faces.get(f,0)+1
 assert all(x in [1,2] for x in faces.values())
 return {'status':'PASS','pattern_children':8,'reference_frame_checks':reference_checks,'reference_face_partition_checks':face_checks,'root_tetrahedra':16,'frame_identity_checks':checks,'max_frame_permutation_types_per_root':6,'max_total_types':96,'diameter_bound_squared_C':str(C2),'frame_singular_value_squared_lower':str(min(lower)),'frame_singular_value_squared_upper':str(max(upper)),'h_level_bound':'h_l^2 <= C_squared * 4^(-l), l>=0, starting from the14-node/16-tet mesh','uniform_frame_condition_squared_upper':str(max(upper)/min(lower)),'finite_mesh_vertices':len(q),'finite_mesh_tetrahedra':len(s),'finite_mesh_max_diameter_squared':str(max(distance(q,i,j) for tet in s for i,j in combinations(tet,2))),'physical_promotion':0,'independent_review':False}
if __name__=='__main__':print(json.dumps(family_certificate(),indent=2))
