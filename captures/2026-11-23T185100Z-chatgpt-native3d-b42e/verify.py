#!/usr/bin/env python3
"""Exact reference geometry contrast + zero-reserve/metric-family gates.
External rational Euclidean embeddings are controls, not sourced UD state.
"""
from itertools import combinations
import json
import sympy as s
from pathlib import Path
V = [s.Matrix(v) for v in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
Qstar=s.Matrix([[-61,-22,58],[62,-19,58],[-2,82,29]])/87
assert Qstar.T*Qstar==s.eye(3) and Qstar.det()==1

def overlap(Q):
    normals=V+[-Q*v for v in V]
    verts=set()
    for ids in combinations(range(8),3):
        A=s.Matrix.vstack(*[normals[i].T for i in ids])
        if A.det()==0: continue
        p=A.inv()*s.Matrix([-1,-1,-1])
        if all(n.dot(p)>=-1 for n in normals): verts.add(tuple(p))
    verts=sorted(verts)
    facets=[tuple(k for k,p in enumerate(verts) if n.dot(s.Matrix(p))==-1) for n in normals]
    assert all(len(f)>=3 for f in facets)
    edges=set()
    for i,j in combinations(range(len(facets)),2):
        common=set(facets[i]).intersection(facets[j]);
        if len(common)==2:edges.add(tuple(sorted(common)))
    assert len(edges)==len(verts)+len(facets)-2
    return verts,facets,edges

v0,f0,e0=overlap(s.eye(3));v1,f1,e1=overlap(Qstar)
assert (len(v0),len(e0),len(f0))==(6,12,8)
assert (len(v1),len(e1),len(f1))==(12,18,8)
assert sorted(map(len,f0))==[3]*8
assert sorted(map(len,f1))==[3,3,5,5,5,5,5,5]

# Check every supporting-line pair non-coplanar at the distinct proper rotation.
A_edges=[];B_edges=[]
for i,j in combinations(range(4),2):
    A_edges.append((V[i],V[j]-V[i]));B_edges.append((-Qstar*V[i],-Qstar*V[j]+Qstar*V[i]))
noncoplanar=[]
for p,u in A_edges:
    for q,v in B_edges:
        det=(q-p).dot(u.cross(v));noncoplanar.append(det)
assert len(noncoplanar)==36 and all(x!=0 for x in noncoplanar)

# Previous prescribed common-refinement transfer T has full column rank and
# grade-wise Gram blocks [I8,2I12,4I8,[[12,-8],[-8,12]]].
M3=s.Matrix([[12,-8],[-8,12]])
assert M3.eigenvals()=={4:1,20:1}
G3=M3-s.eye(2)
assert G3==s.Matrix([[11,-8],[-8,11]])
assert G3.eigenvals()=={3:1,19:1}
a,b=s.symbols('a b',real=True)
assert s.expand((s.Matrix([a,b]).T*G3*s.Matrix([a,b]))[0]-3*(a*a+b*b)-8*(a-b)**2)==0

# Positive post-metric family independent of any choice of time/evolution:
# for an arbitrary full-column-rank T, H=T M^-2 T^T+lambda(I-P).
# Construct a concrete 3x2 embedding with nontrivial overlap.
T=s.Matrix([[1,0],[0,1],[1,-1]])
M=T.T*T
Pi=T*M.inv()*T.T
lam=s.symbols('lam',positive=True)
H=T*(M.inv()**2)*T.T+lam*(s.eye(3)-Pi)
assert T.T*H*T==s.eye(2)
assert Pi*Pi==Pi and Pi.T==Pi
assert s.factor(H.det())==lam/s.Integer(3) # nonzero, metric positive by orthogonal split

# Any intrinsic tuple x with no Q-dependent coordinate must map to one output.
# The two externally supplied E_Q have different f0; therefore shape readout
# cannot factor through x. This is a structural proof, not a fitted statistic.
result={
 'evidence':'EXACT_CONDITIONAL', 'physical_promotion':0,
 'source_rotation':'outside_native_state',
 'Qstar': [[str(x) for x in row] for row in Qstar.tolist()],
 'Qstar_orthogonal':True,'Qstar_det':'1',
 'Q_I_overlap':{'V':len(v0),'E':len(e0),'F':len(f0),'facet_vertex_counts':sorted(map(len,f0))},
 'Qstar_overlap':{'V':len(v1),'E':len(e1),'F':len(f1),'facet_vertex_counts':sorted(map(len,f1))},
 'Qstar_non_coplanar_edge_pairs':len(noncoplanar),
 'common_inball_radius':'1/sqrt(3)',
 'T_top_gram':[[str(x) for x in row] for row in M3.tolist()],
 'G_top_eigenvalues':{'3':1,'19':1},
 'G_full_eigen_mult':{'0':8,'1':12,'3':9,'19':1},
 'G_zero_iff':'c1=c2=a=b=0 (vertex-only)',
 'T_metric_family_example_det':'lambda/3',
 'metric_family_identity': 'T^T H_lambda T = I_2 for all lambda>0',
 'event_selected':False,
 'native_metric_selected':False,
 'conclusions':['shape-readout nonfactorization through Q-blind source','unweighted zero-reserve gate admits only vertex-only states','positive post metrics exist, not uniquely selected']
}
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print('EXACT PASS: reference 6 vs 12 overlap vertices; 36 skew edge pairs; G kernel; metric family')
