#!/usr/bin/env python3
"""Independent topology/Boolean audit; does not import native_defect_and_readout.
Uses embedded planar grid combinatorics, Euler characteristic, and exact Fraction.
"""
import itertools
import math
from collections import Counter,defaultdict
from fractions import Fraction
from pathlib import Path
import json


def planar(grid,excise):
    v={(x,y) for x in range(grid+1) for y in range(grid+1)}
    faces=[]
    for x in range(grid):
        for y in range(grid):
            faces.extend([tuple(sorted(((x,y),(x+1,y),(x+1,y+1)))),
                          tuple(sorted(((x,y),(x,y+1),(x+1,y+1))))])
    if excise:
        center=(grid//2,grid//2)
        faces=[f for f in faces if center not in f]
    v={p for f in faces for p in f}
    edges={tuple(sorted(edge)) for f in faces for edge in itertools.combinations(f,2)}
    graph=defaultdict(set)
    for a,b in edges:graph[a].add(b);graph[b].add(a)
    start=next(iter(v));seen={start};todo=[start]
    while todo:
        q=todo.pop()
        for w in graph[q]-seen:seen.add(w);todo.append(w)
    assert seen==v
    return (len(v),len(edges),len(faces))


def raw_enum():
    counts=Counter()
    for t1,t2,l1,l2 in itertools.product(range(2),repeat=4):
        g=int(bool(t1*l1 or t2*l2));w=int(bool(t1*t2*(l1 or l2)))
        counts[(w,g)]+=1
    assert dict(counts)=={(0,0):9,(0,1):4,(1,1):3}
    expected=Fraction(math.comb(24,2))*sum(Fraction(v,16)**2 for v in counts.values())**3
    assert expected==Fraction(10272513,524288)
    return counts,expected


def main():
    report=[]
    for n in (4,6,8):
        before=planar(n,False);after=planar(n,True)
        assert before[0]-before[1]+before[2]==1
        assert after[0]-after[1]+after[2]==0
        assert before[2]-after[2]==6
        # Product with interval has the same integral H1 as planar annulus.
        report.append({"grid":n,"planar_before":before,"planar_after":after,
                       "euler_before":1,"euler_after":0,"star_triangles_removed":6,
                       "expected_tetra_removed_height2":6*3*2})
    counts,expected=raw_enum()
    output={"checker":"independent planar Euler and raw 4-bit enumeration",
            "topology":report,
            "pair_counts":{str(k):v for k,v in counts.items()},
            "iid_24_replay_expectation":str(expected),
            "physical_promotion":0,
            "note":"Checks Euler and raw enumeration independently. Integral homology proof uses the planar annulus x interval homeomorphism; not inferred solely from Euler characteristic."}
    path=Path(__file__).parent/'INDEPENDENT_AUDIT.json'
    path.write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps(output,indent=2))

if __name__=='__main__':main()
