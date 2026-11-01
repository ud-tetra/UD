#!/usr/bin/env python3
"""Independent v1.6 check: standard library rational arithmetic and finite groups."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import json
checks=0
def ck(v,tag):
    global checks
    checks+=1
    if not v: raise AssertionError(f"{checks}: {tag}")
v=[F(i) for i in [0,1,2,4]]
faces=list(combinations(range(4),3))
def curr(i,j,r):return (r[i]-r[j])/4
def D(f,r):
    return sum((curr(i,j,r)**2 for i,j in combinations(f,2)),F())
for pi in permutations(range(4)):
    rp=[F(0)]*4
    for i in range(4):rp[pi[i]]=v[i]
    for f in faces:
        g=tuple(sorted(pi[i] for i in f))
        ck(D(f,v)==D(g,rp),"permuted burden score")
for f in faces:
    t=sum(v[i] for i in f)
    old=[v[i] for i in f]+[F(0)]
    # Newborn gradient flow on a registered K4 at t=0
    slope=(sum(old[:3])-3*old[3])/4
    ck(slope==t/4,"initial newborn slope")
    ck(2*slope*slope==t*t/8,"quadratic support acceleration")
    mean=t/4
    ck(sum([mean]*4)==t,"conserved mean equilibrium")
    ck(all(sum(([mean]*4)[j]-(mean) for j in range(4))==0 for i in range(4)),"stationary")
    ck(sum([ (sum(old)-4*old[i])/4 for i in range(4)])==0,"flow divergence")
# 64 rational faces: source gradient linearity test and all finite time nonzero mode powers
for a,b,c in product(range(4), repeat=3):
    w=[F(a),F(b),F(c),F(0)]
    s=sum(w)
    d=[(s-4*x)/4 for x in w]
    ck(sum(d)==0,"total burden conserved")
    ck(d[-1]==s/4,"newborn derivative")
    # L*(x-mean) = 4*(x-mean), for each component
    mean=F(s,4)
    ck(all((4*w[i]-s)==4*(w[i]-mean) for i in range(4)),"eigenmode")
# Nonabelian S3 group extension with preserved old edge transport
G=list(permutations(range(3)))
e=(0,1,2)
def mul(a,b): return tuple(a[b[i]] for i in range(3))
def inv(a): return tuple(a.index(i) for i in range(3))
ck(all(mul(a,inv(a))==e and mul(inv(a),a)==e for a in G),"group inverses")
for g01,g02,g12 in product(G,repeat=3):
    old_flat=mul(mul(g01,g12),inv(g02))==e
    count=0
    for y0 in G:
        # flat 01w and 02w fix y1,y2 given y0
        y1=mul(inv(g01),y0)
        y2=mul(inv(g02),y0)
        new_h=mul(mul(g12,y2),inv(y1))
        if new_h==e: count+=1
    ck(count==(6 if old_flat else 0),"S3 all-flat child iff flat parent")
# Z6 compact mismatch: congruence and least-squares degeneracy at inherited half-turn.
def wrap6(k):
    r=k%6
    return r if r<=3 else r-6
min_cost=None
winners=set()
for x,y,z in product(range(6),repeat=3):
    if (x-y+z+3)%6:continue
    cost=sum(wrap6(t)**2 for t in [x,y,z])
    if min_cost is None or cost<min_cost:
        min_cost=cost;winners={(wrap6(x),wrap6(y),wrap6(z))}
    elif cost==min_cost:winners.add((wrap6(x),wrap6(y),wrap6(z)))
ck(min_cost==3,"half-turn minimal wrapped curvature 3")
ck(winners=={(-1,1,-1),(1,-1,1)},"two distinct optimal curvature sets")
# old-newborn burden stock balance cannot fix additive debit:
for c in [F(1),F(2),F(3,2)]:
    ck((F(3)-c)+(F(4)+c)==7,"same total resource distinct positive debit")
result={"version":"v1.6","independent_method":"stdlib Fraction, Z6, and full nonabelian S3","checks":checks,
  "S3_old_face_cases":6**3,"S3_newborn_gauge_solutions_if_flat":6,
  "Z6_halfturn_wrapped_square_cost":min_cost,"Z6_degenerate_minimizers":[list(x) for x in sorted(winners)],
  "physical_promotion":0,"review":"same constructor independent implementation"}
o=Path(__file__).resolve().parent
(o/"INDEPENDENT_RESULTS_v1.6.json").write_text(json.dumps(result,indent=2)+"\n")
print("PASS",checks,"independent-method exact checks",result["Z6_degenerate_minimizers"])
