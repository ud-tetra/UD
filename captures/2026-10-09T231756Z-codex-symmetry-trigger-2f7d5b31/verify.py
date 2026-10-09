"""Exact automorphism obstruction for deterministic local mask selection.

Carrier: two tetrahedra sharing face 012.  A symmetric amplitude witness is
the uniform vertex 0-chain, which is fixed by the full carrier automorphism
group and is a null mode of the native skew incidence generator.
"""
from itertools import combinations,permutations,product
from pathlib import Path
import json

cells=((0,1,2,3),(0,1,2,4))
levels=[tuple(sorted({s for c in cells for s in combinations(c,k)})) for k in (1,2,3,4)]
vertices,edges,faces,_=levels
G=[dict(zip((0,1,2,3,4),a+b)) for a in permutations((0,1,2)) for b in permutations((3,4))]
def relabel(simplex,p):return tuple(sorted(p[v] for v in simplex))
def permute(mask,p):return {relabel(s,p):v for s,v in mask.items()}
def orbit(seed,objects):return tuple(sorted({relabel(seed,p) for p in G}))
def orbits(objects):
    remaining=set(objects);out=[]
    while remaining:
        o=orbit(min(remaining),objects);assert set(o)<=remaining
        out.append(o);remaining.difference_update(o)
    return out

checks={}
def check(name,truth):
    checks[name]=bool(truth);assert truth,name
check('carrier_f_vector',[len(s) for s in levels]==[5,9,7,2])
check('group_order',len(G)==12 and len({tuple(p[i] for i in range(5)) for p in G})==12)
check('each_map_preserves_cells',all({relabel(c,p) for c in cells}==set(cells) for p in G))
EO=orbits(edges);FO=orbits(faces)
check('edge_orbits_3_6',sorted(map(len,EO))==[3,6])
check('face_orbits_1_6',sorted(map(len,FO))==[1,6])
check('edge_orbit_partition',set().union(*map(set,EO))==set(edges))
check('face_orbit_partition',set().union(*map(set,FO))==set(faces))

def invariant_masks(objects):
    out=[]
    for bits in product((0,1),repeat=len(objects)):
        m=dict(zip(objects,bits))
        if all(permute(m,p)==m for p in G):out.append(m)
    return out
EM=invariant_masks(edges);FM=invariant_masks(faces)
check('four_invariant_edge_masks',len(EM)==4)
check('four_invariant_face_masks',len(FM)==4)
check('invariants_constant_on_orbits',all(all(len({m[s] for s in o})==1 for o in EO) for m in EM) and all(all(len({m[s] for s in o})==1 for o in FO) for m in FM))
def distance(a,b):return sum(a[s]!=b[s] for s in a)
edge_dist=sorted({distance(a,b) for a in EM for b in EM if a!=b})
face_dist=sorted({distance(a,b) for a in FM for b in FM if a!=b})
check('invariant_edge_switch_sizes',edge_dist==[3,6,9])
check('invariant_face_switch_sizes',face_dist==[1,6,7])

# For a G-fixed input c=N and a G-fixed all-open pre-mask, equivariance forces
# the next mask to be G-fixed.  The invariant-mask census above then excludes
# every one-edge switch.  The one shared face is a separate singleton orbit.
N={v:1 for v in vertices}
check('uniform_vertex_state_fixed',all(permute(N,p)==N for p in G))
flat=sum((list(level) for level in levels),[])
native_derivative={s:0 for s in flat}
for high in flat:
    if len(high)==1:continue
    for j in range(len(high)):
        low=high[:j]+high[j+1:]
        sign=(-1)**j
        native_derivative[high]+=sign*N.get(low,0)
        native_derivative[low]-=sign*N.get(high,0)
check('uniform_vertex_native_null_mode',all(v==0 for v in native_derivative.values()))
zero={e:0 for e in edges}
check('single_edge_not_fixed',all(any(permute({e:int(e==target) for e in edges},p)!={e:int(e==target) for e in edges} for p in G) for target in edges))
check('single_shared_face_can_be_fixed',all(relabel((0,1,2),p)==(0,1,2) for p in G))

# A typed edge address removes the obstruction: the identity selector on an
# edge-marked input is equivariant and selects exactly that edge.
for target in edges:
    marked={e:int(e==target) for e in edges}
    for p in G:
        selected=permute(marked,p)
        assert selected=={e:int(e==relabel(target,p)) for e in edges}
check('typed_address_covariant_108_cases',True)

def face_lift(em):return {f:int(all(em[e] for e in edges if set(e)<set(f))) for f in faces}
for em in EM:
    fm=face_lift(em)
    assert all(permute(fm,p)==fm for p in G)
candidate_pairs={(face_lift(em)[(0,1,2)],face_lift(em)[(0,1,3)]) for em in EM}
check('candidate_and_lift_three_face_patterns',candidate_pairs=={(0,0),(1,0),(1,1)})

out={'claim_class':'EXACT CONDITIONAL equivariance theorem on fixed carrier; not a source-selected trigger; physical promotion 0',
     'carrier':'<0123,0124>','group':'S3 on common vertices times S2 on apices; order 12',
     'edge_orbits':[[list(s) for s in o] for o in EO], 'face_orbits':[[list(s) for s in o] for o in FO],
     'invariant_edge_masks':len(EM),'invariant_face_masks':len(FM),'edge_transition_support_sizes':edge_dist,'face_transition_support_sizes':face_dist,
     'typed_address':'a selected edge label or symmetry-breaking edge-marked state restores equivariant single-edge selection',
     'candidate_face_lift_patterns':sorted([list(x) for x in candidate_pairs]),
     'checks':checks,'passed':sum(checks.values())}
Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'passed':out['passed'],'edge_orbit_sizes':[len(x) for x in EO],'face_orbit_sizes':[len(x) for x in FO],'edge_switch_sizes':edge_dist,'face_switch_sizes':face_dist,'candidate_face_patterns':sorted(candidate_pairs)}))
