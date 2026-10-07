import itertools,json
from collections import Counter
from fractions import Fraction

def faces(t):return [tuple(f) for f in itertools.combinations(sorted(t),3)]
def incidence(cells):return Counter(f for t in cells for f in faces(t))
seed=(0,1,2,3);facets=faces(seed);perms=list(itertools.permutations(seed));orbits=[]
for f in facets:
 orbit={tuple(sorted(p[i] for i in f)) for p in perms}
 assert orbit==set(facets);orbits.append(len(orbit))
assert sum([Fraction(1,4)]*4)==1
def attach(cells,face,apex):
 counts=incidence(cells)
 if counts.get(tuple(sorted(face)))!=1:raise ValueError('attachment requires a boundary face')
 if any(apex in t for t in cells):raise ValueError('attachment requires a fresh vertex')
 return cells+[tuple(sorted((*face,apex)))]
cells=[seed];apex=4;rounds=[]
for n in range(5):
 counts=incidence(cells);boundary=[f for f,c in counts.items() if c==1];interior=sum(c==2 for c in counts.values())
 assert set(counts.values())<={1,2}
 assert 4*len(cells)==len(boundary)+2*interior
 assert len(cells)==2*3**n-1 and len(boundary)==4*3**n and interior==len(cells)-1
 dual_edges=sum(c==2 for c in counts.values());assert dual_edges==len(cells)-1
 rounds.append({'round':n,'cells':len(cells),'boundary_faces':len(boundary),'interior_faces':interior})
 if n<4:
  for f in sorted(boundary):
   before=incidence(cells);new=attach(cells,f,apex);after=incidence(new)
   assert sum(v==1 for v in after.values())-sum(v==1 for v in before.values())==2
   assert after[f]==2 and sum(v==2 for v in after.values())==sum(v==2 for v in before.values())+1
   cells=new;apex+=1
controls=[]
interior_face=next(f for f,c in incidence(cells).items() if c==2)
for label,face,new_apex in [('interior face rejected',interior_face,apex),('nonfresh apex rejected',next(f for f,c in incidence(cells).items() if c==1),0)]:
 try:attach(cells,face,new_apex)
 except ValueError:controls.append(label)
 else:raise AssertionError(label+' failed')
print(json.dumps({'status':'PASS','face_count':len(facets),'permutations':len(perms),'face_orbit_sizes':orbits,'conditional_symmetric_face_weight':'1/4','rounds':rounds,'controls':controls,'verified_scope':'finite abstract fresh-vertex boundary gluing; no dense-selector replay or physical model','independent_review':'pending','physical_promotion':0},indent=2))
