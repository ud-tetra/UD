from pathlib import Path
from decimal import Decimal as D,getcontext
import numpy as np,json,hashlib
p=Path(__file__).resolve().parent;root=p.parent;f=json.loads((p/'FREEZE.json').read_text());g=np.load(root/'graphite-map/MAPS.npz');text=(p/'sources/CH.rebo').read_text().split('# gC1 and gC2',1)[1].split('# gH',1)[0];tokens=text.split();n=int(tokens[0]);domains=list(map(D,tokens[1:1+n]));coeff=[list(map(D,tokens[1+n+i*6:1+n+(i+1)*6])) for i in range(8)];getcontext().prec=50
records=[]
for order in range(4):
 vals=[]
 for row in [coeff[1],coeff[2]]:
  c=row.copy()
  for _ in range(order):c=[D(i)*v for i,v in enumerate(c)][1:]
  vals.append(sum(v*D('-.5')**i for i,v in enumerate(c)))
 records.append({'derivative_order':order,'left':str(vals[0]),'right':str(vals[1]),'right_minus_left':str(vals[1]-vals[0])})
rows=[];arrays={}
for cfg in f['inputs']:
 c=cfg['case'];a=np.load(root/'graphite-stationary'/c/'RELAXED.npz');b=np.load(root/'graphite-stationary'/c/'HESSIAN.npz');x=a['positions_A'];N=len(x);edges=g[c+'_edges_0based'];shift=g[c+'_edge_shifts_xy_A'].copy()
 # Source graph shifts use raw input coordinate images. Align them to the saved
 # LAMMPS reference image gauge before applying the small relaxed displacement.
 pat,di=c.split('_',1);lines=(root/'graphite-target-replay/selected'/pat/di/'struct.inp.data').read_text().splitlines();lx=float(next(z for z in lines if 'xlo xhi' in z).split()[1]);ly=float(next(z for z in lines if 'ylo yhi' in z).split()[1]);xy=float(next(z for z in lines if 'xy xz yz' in z).split()[0]);L=np.array([[lx,xy],[0,ly]]);raw=g[c+'_source_positions_A'];delta=a['initial_positions_A'][:,:2]-raw[:,:2];integers=np.rint(np.linalg.solve(L,delta.T)).astype(int);offset=(L@integers).T;assert np.max(abs(delta-offset))<1e-10;shift-=offset[edges[:,1]]-offset[edges[:,0]]
 adj=[[] for i in range(N)]
 for (i,j),sh in zip(edges,shift):adj[i].append((j,np.r_[sh,0]));adj[j].append((i,np.r_[-sh,0]))
 assert all(len(v)==3 for v in adj);neighbors=np.array([[v[0] for v in z] for z in adj]);shifts=np.array([[v[1] for v in z] for z in adj])
 def angles(xx):
  bonds=xx[neighbors]-xx[:,None,:]+shifts;norm=np.linalg.norm(bonds,axis=2);assert np.max(norm)<1.7;unit=bonds/norm[:,:,None];return np.stack([np.sum(unit[:,i]*unit[:,j],axis=1) for i,j in [(0,1),(0,2),(1,2)]],axis=1)
 baseline=angles(x);d=b['primitive_P'].shape[1];nx=d-2;m=3*d-5;B=np.zeros((N,3,m));B[:,0,:nx]=b['primitive_P']@b['basis_S'];B[:,1,nx:2*nx]=b['primitive_P']@b['basis_S'];B[:,2,2*nx:]=b['primitive_P']@b['basis_Q'];case_rows=[]
 for j in cfg['columns']:
  records_j=[];allang=[]
  for h in f['steps_A']:
   ap=angles(x+h*B[:,:,j]);am=angles(x-h*B[:,:,j]);cross=(np.minimum(ap,am)<-.5)&(np.maximum(ap,am)>-.5);records_j.append({'step_A':h,'angle_triples_crossing_minus_half':int(cross.sum()),'max_angle_cosine_change':float(max(np.max(abs(ap-baseline)),np.max(abs(am-baseline))))});allang.append([am,ap])
  case_rows.append({'column':j,'ladder':records_j});arrays[c+'_column_'+str(j)+'_angles']=np.array(allang)
 arrays[c+'_baseline_angles']=baseline;rows.append({'case':c,'minimum_abs_distance_to_minus_half':float(np.min(abs(baseline+.5))),'selected_columns':case_rows})
np.savez_compressed(p/'ANGLE_DATA.npz',**arrays)
r={'source_tag':'stable_22Jul2025_update4','source_domain_values':[str(x) for x in domains],'gC1_minus_half_join':records,'join_status':'C2 matching, third derivative mismatch in actual parameter decimals','geometry_crossings':rows,'attribution':'Geometry/source diagnostic; establishes potential branch crossings, not unique attribution of full force residual to one term. Runtime binary-to-source-tag identity not independently verified.','physical_promotion':0};(p/'BRANCH_AUDIT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
