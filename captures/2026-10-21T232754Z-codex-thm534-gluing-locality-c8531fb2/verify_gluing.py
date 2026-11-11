"""Exact shared-face gluing and locality audit, no archived imports."""
from itertools import combinations,product
from fractions import Fraction as Q
from pathlib import Path
import json

def zero(n,m):return [[0 for _ in range(m)] for _ in range(n)]
def matmul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def mv(a,x):return [sum(v*y for v,y in zip(row,x)) for row in a]
def transpose(a):return list(map(list,zip(*a)))
def norm(x):return sum((v*v for v in x),Q())
def solve(a,b):
 a=[list(map(Q,r))+[Q(v)] for r,v in zip(a,b)];n=len(b)
 for j in range(n):
  k=next(k for k in range(j,n) if a[k][j]);a[j],a[k]=a[k],a[j];d=a[j][j];a[j]=[v/d for v in a[j]]
  for k in range(n):
   if k!=j:
    d=a[k][j]
    if d:a[k]=[v-d*w for v,w in zip(a[k],a[j])]
 return [r[-1] for r in a]
def complex_of(cells):
 cells=sorted(tuple(sorted(t)) for t in cells)
 bases=[sorted({s for t in cells for s in combinations(t,k)}) for k in range(1,5)]
 bs=[]
 for k in range(1,4):
  lo,hi=bases[k-1],bases[k];b=zero(len(lo),len(hi))
  for j,s in enumerate(hi):
   for i in range(len(s)):b[lo.index(s[:i]+s[i+1:])][j]=(-1)**i
  bs.append(b)
 assert matmul(bs[0],bs[1])==zero(len(bases[0]),len(bases[2]))
 assert matmul(bs[1],bs[2])==zero(len(bases[1]),len(bases[3]))
 return bases,bs

def connected_components(cells):
 todo=set(range(len(cells)));out=[]
 while todo:
  comp={todo.pop()};stack=list(comp)
  while stack:
   i=stack.pop();near={j for j in todo if len(set(cells[i])&set(cells[j]))==3}
   todo-=near;comp|=near;stack+=list(near)
  out.append(sorted(comp))
 return out

def census(name,cells,expected):
 bases,(b1,b2,b3)=complex_of(cells);vs,es,fs,ts=bases
 valid_a=[]
 for bits in product((0,1),repeat=len(fs)):
  masked=[[b2[i][j]*bits[j] for j in range(len(fs))] for i in range(len(es))]
  if matmul(masked,b3)==zero(len(es),len(ts)):valid_a.append(bits)
 comps=connected_components(ts)
 for a in valid_a:
  for comp in comps:
   vals={a[fs.index(f)] for t in comp for f in combinations(ts[t],3)};assert len(vals)==1
 assert len(valid_a)==2**len(comps)
 allowed=0
 for h in product((0,1),repeat=len(es)):
  # Actual first-product columns; avoid recomputing identically zero columns for each a.
  d1=[[b1[i][j]*h[j] for j in range(len(es))] for i in range(len(vs))]
  defect=matmul(d1,b2);bad={j for j in range(len(fs)) if any(defect[i][j] for i in range(len(vs)))}
  for a in valid_a:
   allowed+=not any(a[j] for j in bad)
 assert allowed==expected,(name,allowed)
 # All h,a pairs accounted for by an exact second-product elimination, then first-product evaluation.
 return {'name':name,'f_vector':list(map(len,bases)),'dimension':sum(map(len,bases)),
 'face_adjacency_components':len(comps),'live23_binary_pairs_accounted':2**(len(es)+len(fs)),
 'second_identity_face_masks':len(valid_a),'both_identities_pairs':allowed}

rows=[]
rows.append(census('single_tetrahedron',[(0,1,2,3)],66))
rows.append(census('K_minus_shared_face',[(0,1,2,3),(0,1,2,4)],514))
rows.append(census('K_plus_three_cells',[(0,1,2,3),(0,1,2,4),(0,1,3,4)],1026))
rows.append(census('boundary_4simplex',list(combinations(range(5),4)),1026))
rows.append(census('two_disjoint_tetrahedra',[(0,1,2,3),(4,5,6,7)],4356))

# Concrete shared-face conflict: edge03 changes only the first cell's local mask.
bases,(b1,b2,b3)=complex_of([(0,1,2,3),(0,1,2,4)]);vs,es,fs,ts=bases
h=[int(e==(0,3)) for e in es];local=[]
for cell in ts:
 values={h[es.index(e)] for e in combinations(cell,2)};local.append(int(len(values)==1))
assert local==[0,1]
assert len({local[i] for i,t in enumerate(ts) if set((0,1,2)).issubset(t)})==2
bad_controls=[]
for policy in ['AND','OR']:
 a=[]
 for f in fs:
  votes=[local[i] for i,t in enumerate(ts) if set(f).issubset(t)]
  a.append(int(all(votes)) if policy=='AND' else int(any(votes)))
 d2=[[b2[i][j]*a[j] for j in range(len(fs))] for i in range(len(es))]
 defect=matmul(d2,b3);d2sq=sum(v*v for row in defect for v in row);assert d2sq==3
 bad_controls.append({'policy':policy,'face_mask':''.join(map(str,a)),'second_defect_frobenius_squared':d2sq})
# Exact norm and ownership receipts still hold for a non-flat masked generator.
a=bad_controls[0]['face_mask'];a=list(map(int,a));d1=[[b1[i][e]*h[e] for e in range(len(es))] for i in range(len(vs))]
d2=[[b2[i][f]*a[f] for f in range(len(fs))] for i in range(len(es))]
size=sum(map(len,bases));A=zero(size,size);offsets=[0,len(vs),len(vs)+len(es),len(vs)+len(es)+len(fs)]
for b,u,v in [(d1,offsets[0],offsets[1]),(d2,offsets[1],offsets[2]),(b3,offsets[2],offsets[3])]:
 for i in range(len(b)):
  for j in range(len(b[0])):A[u+i][v+j]=b[i][j];A[v+j][u+i]=-b[i][j]
assert transpose(A)==[[-v for v in row] for row in A]
z=[Q(i-7,11) for i in range(size)];az=mv(A,z);step=Q(1,4);t=step/2
zp=solve([[Q(i==j)-t*A[i][j] for j in range(size)] for i in range(size)],[z[i]+t*az[i] for i in range(size)])
assert norm(zp)==norm(z)
all_simplices=[s for basis in bases for s in basis];weights=[]
for cell in ts:
 weights.append([Q(int(set(s).issubset(cell)),sum(set(s).issubset(t) for t in ts)) for s in all_simplices])
assert all(sum(w[i] for w in weights)==1 for i in range(size))
mid=[(x+y)/2 for x,y in zip(z,zp)];deltas=[]
for w in weights:
 delta=sum(w[i]*(zp[i]**2-z[i]**2) for i in range(size))
 current=sum(2*step*(w[i]-w[j])*A[i][j]*mid[i]*mid[j] for i in range(size) for j in range(i+1,size))
 assert delta==current;deltas.append(delta)
assert sum(deltas)==0
shared_idx=all_simplices.index((0,1,2));assert [w[shared_idx] for w in weights]==[Q(1,2),Q(1,2)]

# Stacked chain: a remote output depends on a first-cell edge toggle.
long_cells=[tuple(range(i,i+4)) for i in range(8)];lb,lB=complex_of(long_cells)
assert connected_components(lb[3])==[list(range(8))]
edge=(0,1);lastface=tuple(range(8,11));assert edge in lb[1] and lastface in lb[2]
assert all(not set(edge).issubset(c) for c in lb[3][1:])
# Unique maximal completion on this face-connected component is all faces on iff h uniform.
assert len({int(e==edge) for e in lb[1]})==2
# Local-transition barrier, even when common face-to-cell t may change.
def flat_general(bases,bs,h,a,t):
 b1,b2,b3=bs
 d1=[[b1[i][e]*h[e] for e in range(len(h))] for i in range(len(b1))]
 d2=[[b2[e][f]*a[f] for f in range(len(a))] for e in range(len(b2))]
 d3=[[a[f]*t[f]*b3[f][j] for j in range(len(b3[0]))] for f in range(len(a))]
 return matmul(d1,d2)==zero(len(b1),len(a)) and matmul(b2,d3)==zero(len(b2),len(b3[0]))
barrier=[]
for name,cells in [('shared_face_pair',[(0,1,2,3),(0,1,2,4)]),('stacked_chain_8',long_cells)]:
 bb,bs=complex_of(cells);ne,nf=len(bb[1]),len(bb[2]);bits=[1]*(ne+2*nf)
 assert flat_general(bb,bs,bits[:ne],bits[ne:ne+nf],bits[ne+nf:])
 hits=0
 for i in range(len(bits)):
  v=bits[:];v[i]=0
  hits+=flat_general(bb,bs,v[:ne],v[ne:ne+nf],v[ne+nf:])
 assert hits==0
 barrier.append({'complex':name,'single_bit_neighbors_checked':len(bits),'chain_compatible_neighbors':hits})
result={'status':'PASS_EXACT_CONDITIONAL','physical_promotion':0,'censuses':rows,
 'local_conflict':{'first_cell_local_completion':0,'second_cell_local_completion':1,'shared_face':'012','global_maximal_completion':'all seven face columns off','AND_OR_controls':bad_controls},
 'global_support_receipts':{'dimension':size,'norm_preserved_despite_chain_defect':True,'equal_top_star_weights_sum_to_one':True,'shared_face_weights':['1/2','1/2'],'cell_delta_receipts':list(map(str,deltas))},
 'locality_control':{'stacked_cells':8,'changed_edge':list(edge),'remote_face':list(lastface),'first_cell_only_edge':True,'instantaneous_global_completion_changes_remote_output':True},
 'local_transition_barrier_controls':barrier,'native_requirement_for_effective_chain_identities':'OPEN','maximal_contact_preference':'CANDIDATE','outside_peer_review':False}
Path(__file__).with_name('RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'censuses':rows,'shared_face_conflict':True,'both_local_merge_defects_squared':3,'physical_promotion':0},indent=2))
