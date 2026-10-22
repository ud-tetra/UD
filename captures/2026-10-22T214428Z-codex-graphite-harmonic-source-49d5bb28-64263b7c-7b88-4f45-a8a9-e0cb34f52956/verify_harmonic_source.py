"""Exact source projection on the previous immutable seven-cell K7 carrier."""
from pathlib import Path
from fractions import Fraction as F
import contextlib
import io
import json
import runpy

base = Path(__file__).resolve().parents[2]
prior = base / 'captures/2026-10-22T211409Z-codex-graphite-honeycomb-5e20b9a6-101b-4fce-8c91-a1d4070ba2d8/verify_honeycomb_h1.py'
with contextlib.redirect_stdout(io.StringIO()):
    carrier = runpy.run_path(str(prior))
B1, B2, M, G = [carrier[k] for k in ('B1', 'B2', 'M', 'G')]
mm, trans, rank, zeros = [carrier[k] for k in ('mm', 'trans', 'rank', 'zeros')]
edge_labels = carrier['edgelabels']
assert mm(trans(M),trans(B1)) == zeros(2,14)
assert mm(trans(M),B2) == zeros(2,7)

orbits=[]
seen=set()
for (i,k),e in edge_labels.items():
    if e in seen:
        continue
    orbit=[]
    for _ in range(3):
        ee=edge_labels[(i,k)]
        assert ee not in seen
        seen.add(ee)
        orbit.append(ee)
        i,k=4*i%7,(4*k-1)%7
    orbits.append(orbit)
assert len(orbits)==7 and len(seen)==21
expected_orbits=[[0,9,4],[1,6,13],[2,10,18],[3,7,20],
                 [5,8,16],[11,14,12],[15,17,19]]
assert orbits==expected_orbits

# K_r = M^T P_r B1^T, constructed without a numerical pseudo-inverse.
Ks=[[[sum(M[e][a]*B1[v][e] for e in orb) for v in range(14)]
     for a in range(2)] for orb in orbits]
assert [[sum(Ks[r][a][v] for r in range(7)) for v in range(14)]
        for a in range(2)] == zeros(2,14)
Q=[[sum(Ks[i][0][v]*Ks[j][0][v] for v in range(14))
    for j in range(7)] for i in range(7)]
expected4=[[2,0,-1,-1,0,0,0],
           [0,4,-1,0,-1,-2,0],
           [-1,-1,4,-1,0,-1,0],
           [-1,0,-1,4,-1,0,-1],
           [0,-1,0,-1,4,-1,-1],
           [0,-2,-1,0,-1,4,0],
           [0,0,0,-1,-1,0,2]]
assert [[4*x for x in row] for row in Q] == expected4
assert rank(Q)==6 and all(sum(row)==0 for row in Q)
# 4Q is a connected weighted graph Laplacian. This independently
# proves PSD and makes the unique uniform null transparent.
assert all(expected4[i][j]<=0 for i in range(7) for j in range(7) if i!=j)
assert all(expected4[i][i]==-sum(expected4[i][j] for j in range(7) if j!=i)
           for i in range(7))
seen_vertices={0}
while True:
    expanded=seen_vertices | {j for i in seen_vertices for j in range(7)
                                if i!=j and expected4[i][j]<0}
    if expanded==seen_vertices:
        break
    seen_vertices=expanded
assert len(seen_vertices)==7
for i in range(7):
    for j in range(7):
        sym=[[sum(Ks[i][a][v]*Ks[j][b][v]+Ks[j][a][v]*Ks[i][b][v]
                  for v in range(14))/2 for b in range(2)] for a in range(2)]
        assert sym == [[Q[i][j]*G[a][b] for b in range(2)] for a in range(2)]
# The independent bilayer source is [-K/2, +K/2], hence Gram αG/2.
for r in range(7):
    K=Ks[r]
    C=[[-x/2 for x in row]+[x/2 for x in row] for row in K]
    assert mm(C,trans(C)) == [[Q[r][r]*G[a][b]/2 for b in range(2)]
                               for a in range(2)]
print(json.dumps({'status':'EXACT_CONDITIONAL_CONSTRUCTOR_CHECK',
                  'edge_orbits':orbits,'4Q':expected4,'rank_Q':rank(Q),
                  'kernel_Q':'span of (1,1,1,1,1,1,1)',
                  'bilayer_gram':'alpha(w) G / 2',
                  'material_weights':'OPEN'},indent=2))
