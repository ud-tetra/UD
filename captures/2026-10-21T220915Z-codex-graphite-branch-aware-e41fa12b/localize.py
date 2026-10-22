from pathlib import Path
import numpy as np,json
from geometry import setup,clearance
p=Path(__file__).resolve().parent;root=p.parent;r=json.loads((p/'RESULTS.json').read_text());records=[]
for row in r['cases']:
 case=row['case'];a=np.load(root/'graphite-stationary'/case/'RELAXED.npz');bas=np.load(root/'graphite-stationary'/case/'HESSIAN.npz');P=bas['primitive_P'];d=P.shape[1];m=3*d-5;nx=d-2;B=np.zeros((len(P),3,m));B[:,0,:nx]=P@bas['basis_S'];B[:,1,nx:2*nx]=P@bas['basis_S'];B[:,2,2*nx:]=P@bas['basis_Q'];nei,b=setup(root,case,a);raw=np.load(p/case/'MATRIX_RAW.npz');dr=np.load(p/case/'DIRECTION_RAW.npz');knots=np.array([-.6666666667,-.5,-.3333333333])
 def counts(disp,steps):
  db=disp[nei]-disp[:,None,:];rows=[]
  for h in steps:
   ang=[]
   for sign in [-1,1]:
    bb=b+sign*h*db;u=bb/np.linalg.norm(bb,axis=2)[:,:,None];ang.append(np.stack([np.sum(u[:,i]*u[:,j],axis=1) for i,j in [(0,1),(0,2),(1,2)]],axis=1))
   lo=np.minimum(*ang);hi=np.maximum(*ang);rows.append({'step_A':float(h),'endpoint_crossing_counts_by_knot':{str(k):int(np.sum((lo<k)&(hi>k))) for k in knots}})
  return rows
 for k,pair in enumerate(row['matrix_step_pairs']):
  if pair['max_abs']<1e-6:continue
  i,j=pair['worst_entry'];h=raw['fine_steps_A'][j];c,n,res=clearance(nei,b,B[:,:,j],knots);records.append({'case':case,'kind':'matrix','entry':[i,j],'max_abs_change':pair['max_abs'],'nearest_crossing_A':c,'stencils':counts(B[:,:,j],[2*h,h,h/2])})
 for rr in row['directions']:
  if rr['adjacent_max_abs']<1e-6:continue
  i=rr['index'];disp=np.einsum('nam,m->na',B,dr['vectors'][i]);c,n,res=clearance(nei,b,disp,knots,hmax=2.5e-5);records.append({'case':case,'kind':'direction','index':i,'role':rr['role'],'frequency':'sqrt(3)' if i==4 else None,'max_adjacent_change':rr['adjacent_max_abs'],'adjacent_max_abs_changes':[float(np.max(abs(v))) for v in np.diff(dr['derivatives'][i],axis=0)],'nearest_crossing_A':None if not np.isfinite(c) else c,'stencils':counts(disp,dr['steps_A'])})
result={'status':'POST_RESULT_DIAGNOSTIC_ONLY','failures':records,'inference':'Failed coarse stencils coincide with gC knot crossings; no force-component isolation or unique angular-term attribution newly performed. Retained fine/audit comparisons pass in all four full matrices. Protocol and outcomes unchanged.','physical_promotion':0};(p/'FAILURE_LOCALIZATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
