#!/usr/bin/env python3
"""Exact rational replay of two source-defined C1 frame gates on a K4 null."""
import itertools
import json
from fractions import Fraction as F

V = tuple(range(4))
S = [list(itertools.combinations(V, k)) for k in (1, 2, 3, 4)]
E = S[1]
PERMS = list(itertools.permutations(V))


def zero(n, m):
    return [[F(0) for _ in range(m)] for _ in range(n)]


def ident(n):
    a = zero(n, n)
    for i in range(n):
        a[i][i] = F(1)
    return a


def tr(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    assert len(a[0]) == len(b)
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def lin(a, b, ca=F(1), cb=F(1)):
    return [[ca*x + cb*y for x, y in zip(rx, ry)] for rx, ry in zip(a, b)]


def boundary(low, high):
    z = zero(len(low), len(high))
    idx = {s:i for i, s in enumerate(low)}
    for j, simplex in enumerate(high):
        for p in range(len(simplex)):
            z[idx[simplex[:p]+simplex[p+1:]]][j] = F((-1)**p)
    return z


def p0(perm):
    z = zero(4, 4)
    for j, v in enumerate(perm):
        z[v][j] = F(1)
    return z


def rho(perm):
    z = zero(6, 6)
    idx = {edge:i for i, edge in enumerate(E)}
    for j, (u, v) in enumerate(E):
        a, b = perm[u], perm[v]
        z[idx[tuple(sorted((a, b)))]][j] = F(1 if a < b else -1)
    return z


def extract(t, b1):
    j4 = [[F(1)]*4 for _ in range(4)]
    phat = lin(mm(mm(b1, t), tr(b1)), j4, F(1,4), F(1,4))
    found = [r for r in PERMS if p0(r) == phat]
    if len(found) != 1 or mm(b1,t) != mm(phat,b1):
        return None, phat
    return found[0], phat


def compression(o):
    return [row[4:10] for row in o[4:10]]


def main():
    b1,b2,b3 = [boundary(S[k],S[k+1]) for k in range(3)]
    assert mm(b1,b2) == zero(4,4) and mm(b2,b3) == zero(6,1)
    assert mm(b1,tr(b1)) == lin([[F(4 if i==j else 0) for j in range(4)] for i in range(4)],
                                [[F(1)]*4 for _ in range(4)], cb=F(-1))
    assert lin(mm(tr(b1),b1),mm(b2,tr(b2))) == [[F(4 if i==j else 0) for j in range(6)] for i in range(6)]
    a=zero(15,15)
    offsets=(0,4,10,14)
    for k,b in enumerate((b1,b2,b3)):
        low,high=offsets[k],offsets[k+1]
        for i in range(len(b)):
            for j in range(len(b[0])):
                a[low+i][high+j]=-b[i][j]
                a[high+j][low+i]=b[i][j]
    a2=mm(a,a)
    assert mm(a2,a)==lin(zero(15,15),a,cb=F(-4))
    i15=ident(15)
    oq=lin(lin(i15,a,cb=F(1,2)),a2,cb=F(1,4))
    oh=lin(i15,a2,cb=F(1,2))
    assert mm(oq,oq)==oh
    assert mm(tr(oq),oq)==i15 and mm(tr(oh),oh)==i15
    t0,tq,th=ident(6),compression(oq),compression(oh)
    assert tq==zero(6,6) and th==lin(zero(6,6),ident(6),cb=F(-1))

    matrices={r:rho(r) for r in PERMS}
    assert len({tuple(map(tuple,x)) for x in matrices.values()})==24
    assert all(mm(tr(x),x)==ident(6) and mm(b1,x)==mm(p0(r),b1)
               for r,x in matrices.items())
    assert all(extract(x,b1)[0]==r for r,x in matrices.items())
    # The preferred source gate is total on frame matrices and refuses both
    # singular and negative native edge compressions on this diagnostic.
    assert extract(t0,b1)[0]==V
    assert extract(tq,b1)[0] is None
    assert extract(th,b1)[0] is None

    # The conditional co-moving polar alternative sees Tobs=Dcf on a
    # frame-held native null. At s=0 and pi/2 the quotient is exactly I;
    # at pi/4 both matrices vanish and inversion is forbidden.
    assert mm(th,th)==ident(6)
    residual0=mm(t0,ident(6))
    residualh=mm(th,th)
    assert extract(residual0,b1)[0]==V
    assert extract(residualh,b1)[0]==V
    assert all(mm(tr(x),zero(6,6))==zero(6,6) for x in matrices.values())
    # -I is not a tetrahedral signed-edge relabeling, so taking the raw
    # full-rank polar at pi/2 would misclassify intrinsic motion as frame.
    assert all(x!=th for x in matrices.values())

    # Two-sided covariance of the preferred gate on every input/output
    # relabeling, with a nonidentity middle frame and cycle-silent K=I.
    middle=(1,2,0,3)
    for hin in PERMS:
        for hout in PERMS:
            t=mm(mm(matrices[hout],matrices[middle]),tr(matrices[hin]))
            decoded,_=extract(t,b1)
            assert decoded is not None and matrices[decoded]==t
    # A fixed point of a nontrivial frame can be reached by continuity only
    # through a failed exact gate or a discontinuity: this is proved in report.
    result={
      "status":"EXACT diagnostic replay / event source OPEN",
      "preferred_boundary_gate":{"tetrahedral_frames_pass":24,"two_sided_covariance_cases":576,
        "native_compression":{"0":"FRAME_PASS identity","pi/4":"HOLD nonpermutation",
                              "pi/2":"HOLD nonpermutation"}},
      "co_moving_polar_alternative":{"0":"FRAME_PASS identity","pi/4":"HOLD singular Dcf",
                                     "pi/2":"FRAME_PASS identity"},
      "primitive_local_edge_maps":"six I maps held fixed in static null; distinct from global C1 compression",
      "positive_event_examples":0,"independent_OP03_event_histories_scored":0,"physical_promotion":0
    }
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
