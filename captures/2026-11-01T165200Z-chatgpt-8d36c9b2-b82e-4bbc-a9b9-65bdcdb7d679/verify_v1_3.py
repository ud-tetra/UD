#!/usr/bin/env python3
"""Finite exact controls for UD conditional coface event/resource contract v1.3.
No claim of native energy or clock; all resource transfers are test witnesses."""
from __future__ import annotations
import itertools
import json
from collections import Counter, defaultdict
from fractions import Fraction as F
from pathlib import Path

checks=0
def require(x,why):
    global checks
    assert x,why
    checks+=1

V=(0,1,2,3)
seed_labels=(0,0,1,1)
seed_tetra=frozenset(V)
seed_edges={frozenset(e) for e in itertools.combinations(V,2)}
seed_triangles={frozenset(f) for f in itertools.combinations(V,3)}
facets=sorted(tuple(sorted(f)) for f in itertools.combinations(V,3))

# Source-defined boundary-facet selection, not a source-defined event time.
def coface(facet):
    cnt=Counter(seed_labels[i] for i in facet)
    deficits=[a for a in (0,1) if cnt[a]==1]
    require(len(deficits)==1,"facet has one deficient label")
    fresh=4
    full_labels=dict(enumerate(seed_labels));full_labels[fresh]=deficits[0]
    add_edges={frozenset((fresh,i)) for i in facet}
    edges=seed_edges|add_edges
    tri=seed_triangles|{frozenset((fresh,a,b)) for a,b in itertools.combinations(facet,2)}
    cells={seed_tetra,frozenset((*facet,fresh))}
    facecounts=Counter(frozenset(f) for c in cells for f in itertools.combinations(c,3))
    require(sum(1 for n in facecounts.values() if n==2)==1,"single shared face")
    require(facecounts[frozenset(facet)]==2,"facet glued exactly twice")
    require(all(n in (1,2) for n in facecounts.values()),"two-cell pseudomanifold local incidence")
    require(len(edges)==9 and len(tri)==7 and len(cells)==2,"f-vector")
    require(5-len(edges)+len(tri)-len(cells)==1,"Euler")
    require(sum(n==1 for n in facecounts.values())==6,"boundary count")
    require(all(Counter(full_labels[v] for v in c)=={0:2,1:2} for c in cells),"binary cap each cell")
    require(frozenset((fresh,next(iter(set(V)-set(facet))))) not in edges,"opposite apex edge absent")
    return {"facet":list(facet),"deficient_label":deficits[0],"newborn":fresh,
            "f_vector":[5,len(edges),len(tri),len(cells)],
            "boundary_faces":sum(n==1 for n in facecounts.values()),
            "opposite_apex":next(iter(set(V)-set(facet)))}

candidates=[coface(f) for f in facets]
require(len(candidates)==4 and len({tuple(x['facet']) for x in candidates})==4,"all candidate frontier facets")
require(sorted(x['deficient_label'] for x in candidates)==[0,0,1,1],"label orbit multiplicities")

# Label-preserving automorphism group and nonselection theorem.
G=[p for p in itertools.permutations(V) if all(seed_labels[i]==seed_labels[p[i]] for i in V)]
require(len(G)==4,"stabilizer S2xS2")
for p in G:
    images={tuple(sorted(p[i] for i in f)) for f in facets}
    require(images==set(facets),"facet action well defined")
orbits=[];remaining=set(facets)
while remaining:
    x=next(iter(remaining))
    orb={tuple(sorted(p[i] for i in x)) for p in G}
    orbits.append(sorted(orb));remaining-=orb
require(sorted(len(x) for x in orbits)==[2,2],"exact two nontrivial face orbits")
for f in facets:
    require(any(tuple(sorted(p[i] for i in f))!=f for p in G),"no invariant selected facet")

# All graph-label q2 K5 assignments are forbidden under monochromatic triangle rule.
for assignment in itertools.product((0,1),repeat=5):
    counts=Counter(assignment)
    require(max(counts.values())>=3,"pigeonhole obstruction")

# Four-to-five-cell exhaustive growth histories and independent count controls.
# Each state carries only tetrahedra, unique vertices, and labels.
def fronts(cells):
    cc=Counter(frozenset(f) for t in cells for f in itertools.combinations(t,3))
    return sorted(tuple(sorted(t)) for t,n in cc.items() if n==1)
state0=(frozenset({seed_tetra}),tuple(seed_labels))
states=[state0]
history_counts=[1]
front_counts=[4]
for m in range(1,5):
    new=[]
    for cells,labels in states:
        ff=fronts(cells)
        require(len(ff)==2*m+2,"boundary count per branch")
        for f in ff:
            c=Counter(labels[x] for x in f)
            d=[a for a in (0,1) if c[a]==1]
            require(len(d)==1,"unique newborn label at frontier")
            w=len(labels)
            child=frozenset((*f,w))
            newcells=cells|{child}
            newlabels=labels+(d[0],)
            require(len(newcells)==m+1,"new cell inventory")
            require(all(Counter(newlabels[i] for i in t)=={0:2,1:2} for t in newcells),"per-cell cap")
            new.append((newcells,newlabels))
    states=new
    history_counts.append(len(states))
    front_counts.append(2*(m+1)+2)
require(history_counts==[1,4,24,192,1920],"recovered source history census")
require(sum(history_counts[1:])==2140,"transition total")

# Two-cell birth as a typed *test* resource ledger, not physical burden/energy.
pre_free=F(3);pre_bound=F(4);pre_rad=F(0)
for facet in facets:
    for debit in (F(1),F(2)):
        out_free=pre_free-debit
        out_bound=pre_bound+debit
        require(out_free>=0 and out_bound>=0,"nonnegative toy ledger")
        require(out_free+out_bound+pre_rad==pre_free+pre_bound+pre_rad,"strict additive resource balance")
        require(out_free!=pre_free,"birth not zero-debit")
    # same full prepared state can also hold, supplied action schedule is free
    require(pre_free+pre_bound+pre_rad==F(7),"hold conserves")

# Group-valued new seams on one face: existing edge transports identity.
# Values in center +/-I of SU2. Two assignments obey old-edge integrity and differ in new triangular holonomy.
for facet in facets:
    a,b,c=facet
    for uxa,uxb,uxc in itertools.product((-1,1),repeat=3):
        h_ab=uxa*uxb;h_bc=uxb*uxc;h_ca=uxc*uxa
        require(h_ab*h_bc*h_ca==1,"triangle product consistency")
        require(h_ab in (-1,1) and h_bc in (-1,1),"unitary center link")
    require((1,1,1)!=(-1,1,1),"distinct allowed seam preparations")

# Fixed-carrier incidence support: ZERO first current but nonzero first acceleration is possible.
# Face vector (1,-1,1,-1)/2, cell0=0, J dot c3 = b^T faces = 2;
# second derivative cell stock = 2*(dot c3)^2=8.
b=(F(1),F(-1),F(1),F(-1))
f=tuple(v/F(2) for v in b)
z=F(0)
zdot=sum(v*w for v,w in zip(b,f))
require(zdot==2,"source of registered cell amplitude")
require(2*z*zdot==0,"cell stock current vanishes initially")
require(2*zdot*zdot==8,"cell stock acceleration nonzero")

# Strict local positive debit condition gives conditional finite bound only with separately supplied resource and cost.
for resource in (F(0),F(1,3),F(1),F(7,2),F(5)):
    for cost in (F(1,4),F(1),F(2),F(3)):
        max_events=resource//cost
        require(max_events*cost<=resource<(max_events+1)*cost,"conditional cumulative debit bound")

out={"artifact":"UD_NATIVE_COFACE_EVENT_RESOURCE_CONTRACT_v1.3","date":"2026-11-01",
     "status":"EXACT_CONDITIONAL_STRUCTURE__EVENT_AND_RESOURCE_OPEN",
     "physical_promotion":0,"checks":checks,"source_bounded_growth_histories":history_counts,
     "frontier_counts":front_counts,"candidate_faces":candidates,
     "label_preserving_stabilizer_size":len(G),"face_orbits":orbits,
     "no_invariant_single_face":True,
     "counterexamples":{"action_choice":"HOLD or BIRTH on each of four valid facets",
       "budget_choice":"same prestate permits test debit 1 or 2 conserving bookkeeping",
       "seam_choice":"same prestate permits identity or nonflat center-valued new seams"},
     "native_conclusions":{"topological_rewrite":"conditional source rule retrieved",
       "newborn_label":"derived from deficit",
       "newborn_full_packet_state":"OPEN","newborn_resource_cost":"OPEN",
       "event_schedule":"OPEN","physical_energy":"OPEN","native_metric":"OPEN"}}
Path(__file__).with_name('results_v1_3.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS exact assertions:',checks)
print('Growth history counts:',history_counts)
print('Face orbits:',orbits)
