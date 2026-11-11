from pathlib import Path
import numpy as np,json,sys
root=Path(__file__).resolve().parent.parent;sys.path.insert(0,str(root/'graphite-branch-aware'));from geometry import setup,clearance
p=root/'graphite-branch-aware';out=root/'graphite-branch-aware-addendum';old=json.loads((p/'FAILURE_LOCALIZATION.json').read_text());rows=[]
for case in json.loads((p/'FREEZE.json').read_text())['inputs']:
 a=np.load(root/'graphite-stationary'/case/'RELAXED.npz');bas=np.load(root/'graphite-stationary'/case/'HESSIAN.npz');P=bas['primitive_P'];d=P.shape[1];m=3*d-5;nx=d-2;B=np.zeros((len(P),3,m));B[:,0,:nx]=P@bas['basis_S'];B[:,1,nx:2*nx]=P@bas['basis_S'];B[:,2,2*nx:]=P@bas['basis_Q'];nei,b=setup(root,case,a);raw=np.load(p/case/'MATRIX_RAW.npz');knots=np.array([-.6666666667,-.5,-.3333333333]);mat=raw['matrices']
 for pair in range(2):
  D=mat[pair+1]-mat[pair]
  for j in np.flatnonzero(np.max(abs(D),axis=0)>=1e-6):
   h=raw['fine_steps_A'][j];disp=B[:,:,j];db=disp[nei]-disp[:,None,:];st=[]
   for hh in [2*h,h,h/2]:
    aa=[]
    for sign in [-1,1]:
     bb=b+sign*hh*db;u=bb/np.linalg.norm(bb,axis=2)[:,:,None];aa.append(np.stack([np.sum(u[:,i]*u[:,k],axis=1) for i,k in [(0,1),(0,2),(1,2)]],axis=1))
    lo=np.minimum(*aa);hi=np.maximum(*aa);st.append({'step_A':hh,'crossing_counts':{str(k):int(np.sum((lo<k)&(hi>k))) for k in knots}})
   c,n,res=clearance(nei,b,disp,knots);rows.append({'case':case,'kind':'matrix_column','column_0based':int(j),'row_of_max_0based':int(np.argmax(abs(D[:,j]))),'pair_index':pair,'max_abs_change':float(np.max(abs(D[:,j]))),'nearest_crossing_A':c,'stencils':st})
dirs=[z for z in old['failures'] if z['kind']=='direction'];r={'status':'COMPLETE_FAILED_COLUMN_REGISTER','matrix_failing_columns':len(rows),'failing_directions':len(dirs),'failures':rows+dirs,'correction':'Prior FAILURE_LOCALIZATION.json listed only the worst entry in each failed matrix. It did not enumerate all failed columns. Three-probe language in the v0.1 next-step recommendation is superseded by five probes. Frozen raw data, case gates, all 2/4 outcomes and the 24/24 fine directional comparisons are unchanged.','physical_promotion':0};(out/'FAILURE_REGISTER.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
