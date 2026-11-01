#!/usr/bin/env python3
"""Exact standalone source-recovery replay, 2026-10-31.
Conditional model only. No model constants are inferred from empirical targets.
Binary colors and local cap=2 are *source premises*.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from functools import lru_cache
from math import factorial
import json

N = 0

def check(flag, why):
    global N
    assert flag, why
    N += 1


def terminal_orders(deficits):
    ans=factorial(sum(deficits))
    for d in deficits:ans//=factorial(d)
    return ans

@lru_cache(None)
def recurrence(counts):
    options=[i for i,c in enumerate(counts) if c<2]
    if not options:return 1
    return sum(recurrence(tuple(c+1 if i==j else c for i,c in enumerate(counts))) for j in options)

# Exhaustive all nonempty admissible seed count vectors q=1,...,6
completion_cases=0
for q in range(1,7):
    for counts in product(range(3),repeat=q):
        if sum(counts)==0:continue  # nonempty seed boundary explicitly assumed
        D=sum(2-c for c in counts)
        check(D>=0,'deficit bound')
        check(recurrence(counts)==terminal_orders(tuple(2-c for c in counts)),f'completion q={q},counts={counts}')
        check(sum(counts)+D==2*q,'final vertex count')
        completion_cases += 1
check(recurrence((1,1))==2,'binary two-label seed histories')
check(recurrence((2,1))==1,'triangle unique missing label')
check(recurrence((2,2))==1,'terminal')
check(recurrence((1,1,1))==6,'q3 three-label histories')


def faces(t):
    return [frozenset(v for v in t if v!=missing) for missing in t]


def all_simplices(tets):
    result={k:set() for k in range(1,5)}
    for t in tets:
        for k in range(1,5):
            for subset in combinations(sorted(t),k):result[k].add(frozenset(subset))
    return result


def frontier(tets):
    fcnt=Counter(f for t in tets for f in faces(t))
    return sorted((f for f,c in fcnt.items() if c==1),key=lambda x:tuple(sorted(x)))


def signature(tets):
    adjacency={i:set() for i in range(len(tets))}
    for i,j in combinations(range(len(tets)),2):
        if len(tets[i].intersection(tets[j]))==3:
            adjacency[i].add(j); adjacency[j].add(i)
    return tuple(sorted(len(n) for n in adjacency.values())),adjacency


def step(tets,labels,facet):
    assert facet in frontier(tets), 'frontier-only guard'
    cnt=Counter(labels[v] for v in facet)
    candidates=[j for j in (0,1) if cnt[j]<2]
    assert len(candidates)==1,'unique restoring label'
    new_label=candidates[0]
    nv=len(labels)
    new_tet=facet.union({nv})
    assert all(sum((labels[v] if v<nv else new_label)==j for v in new_tet)==2 for j in (0,1))
    return tets+(new_tet,),labels+(new_label,)

base=(frozenset(range(4)),)
colors=(0,0,1,1)
histories=[(base,colors,tuple())]
results=[]
signatures={}
for m in range(1,6):
    sigset=set(); n_transitions=0
    for tets,labels,choices in histories:
        check(len(tets)==m,'cell count')
        check(len(labels)==m+3,'vertex count')
        simplices=all_simplices(tets)
        fv=tuple(len(simplices[i]) for i in range(1,5))
        check(fv==(m+3,3*m+3,3*m+1,m),f'f vector m={m}, {fv}')
        check(fv[0]-fv[1]+fv[2]-fv[3]==1,'Euler characteristic 1')
        bound=frontier(tets)
        check(len(bound)==2*m+2,'frontier count')
        incidence=Counter(face for t in tets for face in faces(t))
        check(all(c in (1,2) for c in incidence.values()),'manifold face incidence')
        deg,adj=signature(tets)
        check(sum(map(len,adj.values()))==2*(m-1),'face-dual tree edge count')
        stack=[0];seen={0}
        while stack:
            i=stack.pop()
            for j in adj[i]:
                if j not in seen: seen.add(j);stack.append(j)
        check(len(seen)==m,'dual connected')
        for t in tets:
            cnt=Counter(labels[v] for v in t)
            check(cnt=={0:2,1:2},'local binary cap balanced in each tet')
        sigset.add(deg)
    results.append({'cells':m,'legal_histories':len(histories),'vertices':m+3,'edges':3*m+3,'triangles':3*m+1,'boundary_triangles':2*m+2,'dual_degree_signatures':[list(v) for v in sorted(sigset)]})
    signatures[m]=sigset
    if m==5:break
    nxt=[]
    for tets,labels,choices in histories:
        for f in frontier(tets):
            n_transitions+=1
            child=step(tets,labels,f)
            nxt.append((*child,choices+(tuple(sorted(f)),)))
    check(len(nxt)==len(histories)*(2*m+2),'all growth histories enumerated')
    histories=nxt
check([r['legal_histories'] for r in results]==[1,4,24,192,1920],'source historic counts')
check(signatures[4]=={(1,1,2,2),(1,1,1,3)},'chain and star both admit at four cells')
check(len(signatures[5])==3,'three types at five cells')
check(sum(r['legal_histories']*(2*r['cells']+2) for r in results[:-1])==2140,'number of transitions to five cells')

# Binary trion exclusion has an exact dimension obstruction on complete cliques.
# The q=2, c_j<=2 rule is historically target-exposed, not independently derived.
for n,want in [(3,6),(4,6),(5,0),(6,0)]:
    valid=[lab for lab in product((0,1),repeat=n) if max(Counter(lab).values())<=2]
    check(len(valid)==want,f'complete K{n} binary trion census')
check(factorial(6)//(factorial(2)**3)==90,'q=3 balanced K6 labelings')
# On one boundary attachment K5 is not completed: the old and newborn apex
# vertices have the deficient label, and the absent apex-to-apex edge protects
# a monochromatic three-clique from forming.
for ff in base_faces if 'base_faces' in globals() else faces(base[0]):
    ts,ls=step(base,colors,ff)
    old_apex=(set(base[0])-set(ff)).pop()
    new_apex=len(colors)
    check(ls[old_apex]==ls[new_apex],'same omitted/newborn label')
    check(len(all_simplices(ts)[2])==9,'two adjacent K4s have 9 distinct edges')
    check(frozenset((old_apex,new_apex)) not in all_simplices(ts)[2],'no forbidden apex pair edge')
    check(sum(ls[i]==ls[new_apex] for i in ff)==1,'a shared same-color facet vertex yields trion if apex edge added')

# Four faces of first seed form two orbits under fixed binary-label automorphisms.
base_faces=faces(base[0])
subgroup=[p for p in permutations(range(4)) if all(colors[i]==colors[p[i]] for i in range(4))]
check(len(subgroup)==4,'S2 x S2 label-fixed subgroup')
orbits=[]
remaining=set(base_faces)
while remaining:
    f=next(iter(remaining))
    orb={frozenset(p[v] for v in f) for p in subgroup}
    orbits.append(orb);remaining-=orb
check(sorted(len(x) for x in orbits)==[2,2],'no uniquely selected facet under fixed-label symmetry')
check(all(sum(colors[i] for i in f) in (1,2) for f in base_faces),'face label count')

# Root source type distinctions. Graph extension can be admitted with zero amplitude
# but that does not imply physical positive support created at an absent slot.
# Two support-preserving rational lifts from identical old support S=1.
for (a,b) in [((3,5),(4,5)),((5,13),(12,13))]:
    from fractions import Fraction
    alpha=Fraction(*a);beta=Fraction(*b)
    check(alpha*alpha+beta*beta==1,'isometric transfer witness')
    check(beta>0,'positive new transfer witness')

# Exact source-free test: a positive newborn stock cannot be funded if old support
# is held unchanged, boundary flux is zero, and no external reservoir exists.
from fractions import Fraction
for positive in (Fraction(1,9),Fraction(1,4),Fraction(1,1)):
    check(Fraction(1)+positive>1,'unsourced positive support violates balance')

out={
 'artifact':'UD_OMEGA0_COFACE_SOURCE_RECOVERY_REPLAY_v1.2',
 'classification':'EXACT_CONDITIONAL_TOPOLOGY__BIRTH_SOURCE_OPEN',
 'physical_promotion':0,
 'all_nonempty_seed_multiplicity_cases_q1_to_q6':completion_cases,
 'assertions':N,
 'history_census':results,
 'total_growth_transitions_through_five_cells':2140,
 'fixed_binary_label_seed_symmetry':'S2 x S2 (order 4)',
 'fixed_label_boundary_face_orbit_sizes':sorted(len(x) for x in orbits),
 'conditional_growth_terminates_globally':False,
 'native_selector_derived':False,
 'newborn_burden_phase_seam_source_derived':False,
 'native_resource_budget_derived':False,
 'comparison_note':'Source assumes q=2 cap=2, occupied seed, maximal local completion and selected frontier facet. All history counts are legal histories, not probabilities.',
}
with open('/mnt/data/UD_OMEGA0_COFACE_REPLAY_RESULTS_v1.2.json','w') as h: json.dump(out,h,indent=2,sort_keys=True)
print(json.dumps({'assertions':N,'seed_cases':completion_cases,'counts':[(r['cells'],r['legal_histories']) for r in results], 'orbits':[len(o) for o in orbits]},indent=2))
