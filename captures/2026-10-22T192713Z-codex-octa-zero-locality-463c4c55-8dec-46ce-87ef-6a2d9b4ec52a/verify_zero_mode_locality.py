"""Exact zero-mode locality obstruction for midpoint-octahedral refinement.

Stand-alone finite graph reconstruction; proof of the universal metric statement
is given in the accompanying note. Standard library rational checks only.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import json


def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a): return [list(row) for row in zip(*a)]


def energy(edges,z): return sum((z[j]-z[i])**2 for i,j in edges)


def main():
    old_xyz=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
    shell=[tuple(s if axis==k else 0 for k in range(3))
           for axis in range(3) for s in (-1,1)]
    shell_id={x:i for i,x in enumerate(shell)}
    mids={(i,j):shell_id[tuple((old_xyz[i][k]+old_xyz[j][k])//2
                                     for k in range(3))]
          for i,j in combinations(range(4),2)}
    inner=[tuple(sorted((6,)+tuple(shell_id[tuple(signs[axis]
                  if axis==k else 0 for k in range(3))]
                  for axis in range(3))))
           for signs in product((-1,1),repeat=3)]
    corner=[tuple(sorted((7+i,)+tuple(mids[p] for p in mids if i in p)))
            for i in range(4)]
    edges=sorted(set(pair for cell in inner+corner
                     for pair in combinations(cell,2)))
    assert len(edges)==30 and set(range(11))==set(v for e in edges for v in e)
    assert all((6,7+i) not in edges for i in range(4))
    assert all(any((m,6) in edges and (m,7+i) in edges for m in range(6))
               for i in range(4))
    b=[[0 for _ in edges] for _ in range(11)]
    for j,(u,v) in enumerate(edges):b[u][j],b[v][j]=-1,1
    # S0 embeds only the four old vertices; the old constant mode is u.
    s=[[int(i==7+j) for j in range(4)] for i in range(11)]
    u=[1]*4
    assert [sum(row) for row in s]==[0]*7+[1]*4
    # Every one-hop vertex metric has H0[center,old]=0. With coarse
    # pullback I, z=H0 S0 u fixes z_old=1 and z_center=0.
    # Minimize ||B^T z||^2 over the six unrestricted midpoint values.
    zstar=[Q(2,3)]*6+[Q(0)]+[Q(1)]*4
    assert energy(edges,zstar)==4
    lap=matmul(b,transpose(b))
    grad=matmul(lap,[[x] for x in zstar])
    assert all(grad[i][0]==0 for i in range(6))
    # Strict convexity in midpoint variables: all have an edge to center.
    # Exact decomposition: E(z)=4+sum_{old-mid,mid-center,mid-mid}
    # (delta_j-delta_i)^2, with fixed deltas at old and center equal 0.
    for trial in ((Q(0),)*6,(Q(1),)*6,
                  tuple(Q(i,7) for i in range(6))):
        z=list(trial)+[Q(0)]+[Q(1)]*4
        delta=[z[i]-zstar[i] for i in range(11)]
        assert energy(edges,z)==4+energy(edges,delta)

    # The lower bound is sharp within SPD, S4-invariant, one-hop H0:
    # H_old=I, H_mid,old=1/3 on incidences, H_mid,mid=10 I,
    # H_center,center=1. Positive definiteness follows from
    # sum_(old-mid) (x_old+x_mid)^2/3 + (10-2/3)sum_mid x_mid^2
    # + x_center^2, which vanishes only for x=0.
    hlocal=[[Q(int(i==j)) if i>=7 or i==6 else Q(10)*int(i==j)
             for j in range(11)] for i in range(11)]
    for (i,j),m in mids.items():
        hlocal[m][7+i]=hlocal[7+i][m]=Q(1,3)
        hlocal[m][7+j]=hlocal[7+j][m]=Q(1,3)
    zlocal=[row[0] for row in matmul(hlocal,matmul(s,[[x] for x in u]))]
    assert zlocal==zstar and energy(edges,zlocal)==4

    # A two-hop witness at grade zero, built from equivariant barycentric D0.
    d=[[Q(0) for _ in range(11)] for _ in range(4)]
    for i in range(4):d[i][7+i]=1;d[i][6]=Q(1,4)
    for (i,j),m in mids.items():d[i][m]=d[j][m]=Q(1,2)
    assert matmul(d,s)==[[int(i==j) for j in range(4)] for i in range(4)]
    n=[[int(i==j)-matmul(s,d)[i][j] for j in range(11)] for i in range(11)]
    h=[[x+y for x,y in zip(a,brow)] for a,brow in
       zip(matmul(transpose(d),d),matmul(transpose(n),n))]
    assert matmul(transpose(s),matmul(h,s))==[
        [int(i==j) for j in range(4)] for i in range(4)]
    zz=matmul(h,matmul(s,[[x] for x in u]))
    assert [row[0] for row in zz]==[Q(1)]*11
    assert [h[6][7+i] for i in range(4)]==[Q(1,4)]*4
    assert energy(edges,[row[0] for row in zz])==0
    result={"lane":"EXACT conditional zero-mode locality no-go; physical promotion 0",
            "fine_vertices":11,"fine_edges":30,
            "centroid_to_each_old_vertex_graph_distance":2,
            "coarse_constant_mode_dimension":1,
            "local_one_hop_metric_centroid_to_old_zero":True,
            "exact_intertwining_requires_sum_centroid_to_old":1,
            "S4_invariant_exact_intertwining_requires_each_centroid_to_old":"1/4",
            "sharp_min_BtH0S0u_squared_for_unit_coarse_metric":4,
            "sharp_min_attained_by_S4_invariant_one_hop_SPD_H0":True,
            "sharp_min_for_normalized_u_over_two":1,
            "conditional_dynamic_action_lower_bound":"1/M if H1 <= M I",
            "two_hop_vertex_metric_witness_center_old_entries":["1/4"]*4,
            "scope":"Fixed S0, connected 30-edge graph, weighted incidence up block; full-grade two-hop sufficiency not established; no material kernel or friction."}
    (Path(__file__).parent/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({"status":"PASS","edges":len(edges),"min_energy":4,
                      "center_old":result['two_hop_vertex_metric_witness_center_old_entries']}))


if __name__=='__main__':main()
