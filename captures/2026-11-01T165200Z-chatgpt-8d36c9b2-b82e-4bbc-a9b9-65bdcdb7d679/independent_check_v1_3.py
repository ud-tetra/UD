#!/usr/bin/env python3
"""Independent construction of 2-cell oriented incidence and facet orbit no-go.
This is a same-constructor independent implementation, NOT peer review."""
import itertools
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

n=0
def test(v):
    global n
    assert v
    n+=1

def oriented_boundary(simplex):
    return [( (-1)**j, tuple(x for i,x in enumerate(simplex) if i!=j)) for j in range(len(simplex))]

def canonical(t):
    s=list(t)
    inv=sum(s[i]>s[j] for i in range(len(s)) for j in range(i+1,len(s)))
    return tuple(sorted(s)), (-1)**inv

def aggregate_boundary(cells):
    out=defaultdict(int)
    for cell in cells:
        for coef,f in oriented_boundary(cell):
            norm,sign=canonical(f)
            out[norm]+=coef*sign
    return dict(out)

parent=(0,1,2,3)
for skipped in range(4):
    face=tuple(x for x in parent if x!=skipped)
    # Child shares face but must have opposite face orientation.
    child=(*face,4)
    raw_parent=aggregate_boundary([parent]).get(face,0)
    raw_child=aggregate_boundary([child]).get(face,0)
    if raw_child==raw_parent:
        child=(child[1],child[0],*child[2:])
    total=aggregate_boundary([parent,child])
    test(total.get(face,0)==0)
    test(len([x for x,v in total.items() if v!=0])==6)
    test(len([x for x,v in total.items() if v==0])==1)
    # Boundary of boundary vanishes for both independently.
    for one in (parent,child):
        edge=defaultdict(int)
        for c,f in oriented_boundary(one):
            for d,e in oriented_boundary(f):
                key,sgn=canonical(e)
                edge[key]+=c*d*sgn
        for v in edge.values():test(v==0)

# The group preserving the fixed decorated tetrahedron has two transpositions.
labels={0:0,1:0,2:1,3:1}
face_keys=frozenset(frozenset(f) for f in itertools.combinations(labels,3))
perms=[dict(zip(sorted(labels),p)) for p in itertools.permutations(sorted(labels)) if all(labels[i]==labels[p[j]] for j,i in enumerate(sorted(labels)))]
test(len(perms)==4)
for f in face_keys:
    test(any(frozenset(P[i] for i in f)!=f for P in perms))

# Independent exhaustive equal-input legal facet construction.
for face in face_keys:
    old=tuple(labels[i] for i in face)
    choice=0 if old.count(0)==1 else 1
    test(old.count(choice)==1)
    new=old+(choice,)
    test(sorted(new)==[0,0,1,1])

# Accounting identity is exact for any debit <= free resource; several possibilities.
for initial_free in (Fraction(1),Fraction(3),Fraction(7,2)):
    for debit in (Fraction(0),Fraction(1,2),Fraction(1)):
        if debit>initial_free: continue
        initial_total=initial_free+Fraction(4)
        end=(initial_free-debit)+(Fraction(4)+debit)
        test(initial_total==end)

data={"checks":n,"oriented_shared_face_cancelled":True,"two_cell_boundary_faces":6,"decorated_seed_automorphism_group":4,"fixed_facet_selector_forbidden":True,"status":"PASS_SCOPED"}
Path(__file__).with_name('independent_results_v1_3.json').write_text(json.dumps(data,indent=2)+'\n')
print('PASS independent exact assertions:',n)
