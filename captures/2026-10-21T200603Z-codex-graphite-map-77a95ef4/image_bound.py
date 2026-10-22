from pathlib import Path
import numpy as np,json
p=Path(__file__).parent;base=p.parent;a=np.load(p/'MAPS.npz');rows=[]
for name in ['21_dir_0','21_dir_10024','31_dir_10084','31_dir_10134']:
 pat,di=name.split('_',1);ls=(base/'graphite-target-replay/selected'/pat/di/'struct.inp.data').read_text().splitlines();L=np.array([[float(next(x for x in ls if 'xlo xhi' in x).split()[1]),float(next(x for x in ls if 'xy xz yz' in x).split()[0])],[0,float(next(x for x in ls if 'ylo yhi' in x).split()[1])]]);inv=np.linalg.inv(L);x=a[name+'_source_positions_A'];types=a[name+'_types'];edges=a[name+'_edges_0based'];shift=a[name+'_edge_shifts_xy_A'];neighbors=[set() for _ in range(len(x))]
 for i,j in edges:neighbors[i].add(j);neighbors[j].add(i)
 twohop=all(len(set().union(*(neighbors[j] for j in neighbors[i]))-neighbors[i]-{i})>0 for i in range(len(x)))
 span=np.max([np.ptp(x[types==t,:2]@inv.T,axis=0) for t in [1,2]],axis=0);lower=float(np.min((3-span)/np.linalg.norm(inv,axis=1)));bond=x[edges[:,1],:2]-x[edges[:,0],:2]+shift;upper=2*float(np.linalg.norm(bond,axis=1).max());assert twohop and lower>upper
 rows.append({'case':name,'omitted_image_distance_lower_bound_A':lower,'neighbor4_distance_upper_bound_A':upper,'twohop_distinct_vertex_exists':twohop,'passes':True})
res={'status':'PASS','proof':'An omitted image has |k_a|>=3; r>= (3-fractional_span_a)/||row_a(L^-1)|| for that coordinate. Distinct two-hop vertices bound4th-neighbor distance by2 times max selected edge length. Lower bound exceeds this upper bound.','rows':rows,'scope':'Geometric completeness check for the source neighbor search, no gate or map changed','physical_promotion':0};(p/'IMAGE_BOUND.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
