"""Fresh exact constructor checks; stdlib only; no archived code execution."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import json

cells=[(0,1,2,3),(0,1,2,4)]
faces=sorted(set(combinations(cells[0],3))|set(combinations(cells[1],3)))
D=[[0,0] for _ in faces]
for j,c in enumerate(cells):
    for k in range(4): D[faces.index(c[:k]+c[k+1:])][j]=(1,-1)[j]*(-1)**k
foot=[{7+j for j in range(2) if D[f][j]}|{f} for f in range(7)]
edges=[(u,v) for u,v in combinations(range(7),2) if foot[u]&foot[v]]
assert len(edges)==12
adj=[{v if u==i else u for u,v in edges if i in (u,v)} for i in range(7)]
dist=[]
for i in range(7):
    d={i:0}; todo=[i]
    for u in todo:
        for v in adj[u]:
            if v not in d: d[v]=d[u]+1;todo.append(v)
    dist.append([d[v] for v in range(7)])
bounds=[1+sum(row) for row in dist]
assert bounds==[7,10,10,10,10,10,10]
def sinks(arcs): return [v for v in range(7) if not any(u==v for u,w in arcs)]
def acyclic(arcs):
    remaining=set(range(7))
    while remaining:
        ss={v for v in remaining if not any(u==v and w in remaining for u,w in arcs)}
        if not ss: return False
        remaining-=ss
    return True
def reverse(arcs,v): return [(b,a) if v in (a,b) else (a,b) for a,b in arcs]
autos=[]
for p in permutations((0,1,2)):
    for swap in (False,True):
        m=dict(zip((0,1,2),p));m.update({3:4 if swap else 3,4:3 if swap else 4})
        q=[faces.index(tuple(sorted(m[v] for v in f))) for f in faces]
        assert {tuple(sorted((q[u],q[v]))) for u,v in edges}==set(edges)
        autos.append(q)
orientations=[]; first_max=[0]*7;max_round=0;prefix_checks=0
for bits in product((0,1),repeat=len(edges)):
    initial=[(v,u) if b else (u,v) for b,(u,v) in zip(bits,edges)]
    if not acyclic(initial): continue
    orientations.append(initial);arcs=initial;counts=[0]*7;first=[0]*7;attempts=0
    for round_number in range(1,41):
        ss=sinks(arcs);assert ss
        assert all(not (foot[u]&foot[v]) for u,v in combinations(ss,2))
        for v in ss:
            arcs=reverse(arcs,v);counts[v]+=1;attempts+=1
            if not first[v]: first[v]=attempts
            assert all(0<=counts[w]-counts[u]<=1 for u,w in initial)
            assert acyclic(arcs)
            prefix_checks+=1
        if all(first) and round_number<=7: max_round=max(max_round,round_number)
        if round_number==7: assert all(first)
    assert all(n<=b for n,b in zip(first,bounds))
    first_max=[max(a,b) for a,b in zip(first_max,first)]
    assert not all({(q[u],q[v]) for u,v in initial}==set(initial) for q in autos)
assert len(orientations)==576
# Exact local support transfers: epsilon=1/4, s=epsilon/2.
def norm(z): return sum(x*x for x in z)
contacts=[(f,j) for f in range(7) for j in range(2) if D[f][j]]
def step(z,f,mask):
    c=[D[f][j]*mask.get((f,j),0) for j in range(2)];s=F(1,8)
    fp=((1-s*s*sum(x*x for x in c))*z[f]-2*s*sum(c[j]*z[7+j] for j in range(2)))/(1+s*s*sum(x*x for x in c))
    out=z[:];out[f]=fp
    for j in range(2):out[7+j]+=s*c[j]*(z[f]+fp)
    mid=[(a+b)/2 for a,b in zip(z,out)]
    J=[F(1,2)*c[j]*mid[f]*mid[7+j] for j in range(2)]
    assert out[f]**2-z[f]**2==-sum(J)
    assert all(out[7+j]**2-z[7+j]**2==J[j] for j in range(2))
    assert norm(out)==norm(z)
    return out
control=[F(i-2,7) for i in range(9)]
pairs=[(u,v) for u,v in combinations(range(7),2) if not foot[u]&foot[v]]
assert len(pairs)==9
commutation_checks=0
for bits in product((0,1),repeat=8):
    mask=dict(zip(contacts,bits))
    for u,v in pairs:
        assert step(step(control,u,mask),v,mask)==step(step(control,v,mask),u,mask)
        commutation_checks+=1
# Attempts remain distinct from admitted transfers: all-off is identity.
assert all(step(control,f,{})==control for f in range(7))
# Orientation is auxiliary data: two acyclic choices already give different first batches.
def batch(z,arcs):
    for f in sinks(arcs):z=step(z,f,dict.fromkeys(contacts,1))
    return z
assert batch(control,edges)!=batch(control,[(v,u) for u,v in edges])
result={"status":"PASS_EXACT_CONDITIONAL","possible_orientations":4096,
"acyclic_orientations":576,"signed_carrier_automorphisms_checked_as_graph_maps":12,
"fully_automorphism_invariant_acyclic_orientations":0,
"individual_attempt_bounds":bounds,"maximum_first_attempt_indices_with_sorted_batch_accounting":first_max,
"maximum_parallel_rounds_to_first_service_all_faces":max_round,
"prefix_checks":prefix_checks,"rounds_per_orientation":40,
"disjoint_pair_mask_commutation_checks":commutation_checks,
"all_off_identity_controls":7,"initial_orientation_changes_history":True,
"native_initial_orientation":"OPEN","physical_promotion":0}
if __name__=='__main__':
    (Path(__file__).parent/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
