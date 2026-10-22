"""Exact P1 finite-element mass matrix on the 12-cell tetrahedral refinement."""
from fractions import Fraction as Q
from itertools import combinations,product
from pathlib import Path
import json


def det3(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])


def volume(cell,xyz):
    a,b,c,d=[xyz[i] for i in cell]
    return Q(abs(det3(tuple(b[i]-a[i] for i in range(3)),
                      tuple(c[i]-a[i] for i in range(3)),
                      tuple(d[i]-a[i] for i in range(3)))),6)


def main():
    old=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
    shell=[tuple(sign if axis==k else 0 for k in range(3))
           for axis in range(3) for sign in (-1,1)]
    xyz=shell+[(0,0,0)]+old
    index={v:i for i,v in enumerate(shell)}
    mid={(i,j):index[tuple((old[i][axis]+old[j][axis])//2 for axis in range(3))]
         for i,j in combinations(range(4),2)}
    inner=[tuple(sorted((6,)+tuple(index[tuple(signs[axis] if axis==k
            else 0 for k in range(3))] for axis in range(3))))
           for signs in product((-1,1),repeat=3)]
    corners=[tuple(sorted((7+i,)+tuple(mid[p] for p in mid if i in p)))
             for i in range(4)]
    cells=inner+corners
    vols=[volume(t,xyz) for t in cells]
    assert vols==[Q(1,6)]*8+[Q(1,3)]*4
    assert sum(vols)==Q(8,3)
    edges=sorted(set(e for t in cells for e in combinations(t,2)))
    assert len(edges)==30
    # Exact consistent P1 tetra mass: V/20 times 2 on diagonal, 1 off.
    h=[[Q(0) for _ in range(11)] for _ in range(11)]
    for cell,v in zip(cells,vols):
        for i in cell:
            for j in cell:
                h[i][j]+=v*Q(2 if i==j else 1,20)
    assert all(h[i][j]==h[j][i] for i in range(11) for j in range(11))
    assert sum(map(sum,h))==Q(8,3)
    # Sylvester/LDL diagonal pivots give a fully exact SPD check.
    pivots=[];a=[row[:] for row in h]
    for k in range(11):
        pivot=a[k][k];assert pivot>0;pivots.append(pivot)
        for i in range(k+1,11):
            for j in range(k+1,11):
                a[i][j]-=a[i][k]*a[k][j]/pivot
        for i in range(k+1,11):a[i][k]=a[k][i]=Q(0)
    assert all(h[6][7+i]==0 for i in range(4))
    assert all(h[7+i][7+j]==(Q(1,30) if i==j else 0)
               for i in range(4) for j in range(4))
    coarse=[Q(1) if i>=7 else Q(0) for i in range(11)]
    z=[sum(h[i][j]*coarse[j] for j in range(11)) for i in range(11)]
    assert z==[Q(1,30)]*6+[Q(0)]+[Q(1,30)]*4
    hn=[[30*x for x in row] for row in h]
    zn=[30*x for x in z]
    assert zn==[Q(1)]*6+[Q(0)]+[Q(1)]*4
    residual=[zn[j]-zn[i] for i,j in edges]
    residual_sq=sum(x*x for x in residual)
    assert residual_sq==6
    assert sum(bool(x) for x in residual)==6
    assert all({i,j}=={6,m} for (i,j),x in zip(edges,residual) if x for m in [i if j==6 else j])
    # Standard P1 nodal prolongation differs from S0 injection. It gives
    # midpoint values 1/2 at edge endpoints and centroid values 1/4.
    t=[[Q(0) for _ in range(4)] for _ in range(11)]
    for i in range(4):t[7+i][i]=1;t[6][i]=Q(1,4)
    for (i,j),v in mid.items():t[v][i]=t[v][j]=Q(1,2)
    assert [sum(row) for row in t]==[Q(1)]*11
    coarse_mass=[[sum(t[p][i]*h[p][q]*t[q][j]
                       for p in range(11) for q in range(11))
                  for j in range(4)] for i in range(4)]
    assert coarse_mass==[[Q(4,15) if i==j else Q(2,15)
                          for j in range(4)] for i in range(4)]
    z_fe=[sum(row) for row in h]
    assert z_fe==[Q(1,3)]*6+[Q(1,3)]+[Q(1,12)]*4
    residual_fe_sq=sum((z_fe[j]-z_fe[i])**2 for i,j in edges)
    assert residual_fe_sq==Q(3,4)
    # The sharp universal one-hop bound is 4; this local P1 rule gives 6.
    out={"lane":"EXACT conditional P1 finite-element mass audit; physical promotion 0",
         "inner_cell_volumes":["1/6"]*8,"corner_cell_volumes":["1/3"]*4,
         "total_volume":"8/3","mesh_vertices":11,"mesh_edges":30,
         "consistent_mass_rule":"H_ij=sum_cells V_cell*(2 if i=j else 1)/20 for i,j in cell",
         "matrix_SPD_exact_LDL":True,"ldl_pivots":[str(x) for x in pivots],
         "old_vertex_pullback":"I/30","unit_coarse_scale":30,
         "normalized_centroid_old_entries":[0]*4,
         "normalized_HS0u_by_vertex_class":{"midpoints":1,"centroid":0,"old_vertices":1},
         "normalized_incidence_covector_squared":6,
         "normalized_u_over_two_unit_H1_action_squared":"3/2",
         "sharp_one_hop_lower_bound":4,
         "P1_prolongation_midpoint_weights":"1/2 per incident old endpoint",
         "P1_prolongation_centroid_weights":"1/4 per old vertex",
         "P1_coarse_pullback":{"diagonal":"4/15","off_diagonal":"2/15"},
         "P1_prolongated_uniform_H1_covector_by_class":{
             "midpoints":"1/3","centroid":"1/3","old_vertices":"1/12"},
         "P1_prolongated_uniform_incidence_covector_squared":"3/4",
         "scope":"3D volume P1 scalar mass on this mesh only; neither graphite sheet mass nor physical damping or friction."}
    (Path(__file__).parent/'RESULTS.json').write_text(json.dumps(out,indent=2)+'\\n')
    print(json.dumps({"status":"PASS","volume":out['total_volume'],
                      "mass_residual_squared":str(residual_sq),
                      "P1_uniform_residual_squared":str(residual_fe_sq),"nonzero_edges":6}))

if __name__=='__main__':main()
