from pathlib import Path
import json,hashlib,numpy as np
from common import ROOT,load,directions,clearance,input_guard
p=Path(__file__).resolve().parent;f=json.loads((p/'FREEZE.json').read_text());r=json.loads((p/'RESULTS.json').read_text());t=f['thresholds'];records=[]
for fn,sha in f['inputs'].items():assert hashlib.sha256((ROOT/fn).read_bytes()).hexdigest()==sha
for register in ['CODE_FREEZE.json','PRECHECK_SEAL.json']:
 for fn,sha in json.loads((p/register).read_text())['files'].items():assert hashlib.sha256((p/fn).read_bytes()).hexdigest()==sha
for case,row in zip(f['cases'],r['cases']):
 assert case==row['case'];out=p/case;a,B,nei,b=load(case);m=B.shape[2];flat=B.reshape(-1,m);assert np.max(abs(flat.T@flat-np.eye(m)))<1e-12;plan=np.load(out/'PLAN.npz');raw=np.load(out/'RAW.npz');V,names=directions(m);vectors=np.concatenate([np.eye(m),V]);assert np.array_equal(vectors,plan['vectors']);x=a['positions_A'];minmargin=np.inf
 for j,w in enumerate(vectors):
  disp=np.einsum('nam,m->na',B,w);cap=1.25e-5 if j<m else 2.5e-5;c,_,_=clearance(nei,b,disp,f['branch_knots'],hmax=cap);top=min(cap,.8*c);assert np.array_equal(plan['steps_A'][j],[top,.8*top,.6*top]);metrics,safe=input_guard(x,B,nei,b,disp,plan['steps_A'][j],np.array(f['branch_knots']));assert np.array_equal(metrics,plan['input_metrics'][j]);assert np.array_equal(safe,plan['branch_safe'][j]);minmargin=min(minmargin,float(np.min(metrics[3])))
 ds=-(raw['positive_negative_forces'][:,:,0]-raw['positive_negative_forces'][:,:,1])/(2*plan['steps_A'][:,:,None]);assert np.array_equal(ds,raw['derivatives']);Hs=ds[:m].transpose(1,2,0);H=(Hs[1]+Hs[1].T)/2;stored=np.load(out/'HESSIANS.npz')
 for key,val in zip(['H_coarse','H_middle','H_audit','H_symmetric'],[*Hs,H]):assert np.array_equal(stored[key],val)
 deltas=[Hs[1]-Hs[0],Hs[2]-Hs[1]];absolute=max(np.max(abs(v)) for v in deltas);relative=max(np.linalg.norm(v)/np.linalg.norm(H) for v in deltas);colrelative=max(np.linalg.norm(v[:,j])/np.linalg.norm(Hs[1,:,j]) for v in deltas for j in range(m));sym=np.linalg.norm(Hs[1]-Hs[1].T)/np.linalg.norm(H);ev=np.linalg.eigvalsh(H);specth=max(1e-7,10*max(np.linalg.norm(v,2) for v in deltas));assert np.max(abs(stored['eigenvalues']-ev))<1e-12;assert abs(row['eigenvalue_min']-ev[0])<1e-12
 dabs=[];drel=[];sabs=[];srel=[]
 for i,w in enumerate(V):
  dd=ds[m+i];e=dd[1]-H@w;delta=np.diff(dd,axis=0);dabs.append(np.max(abs(e)));drel.append(np.linalg.norm(e)/np.linalg.norm(H@w));sabs.append(np.max(abs(delta)));srel.append(max(np.linalg.norm(v)/np.linalg.norm(dd[1]) for v in delta));rr=row['directions'][i];assert abs(rr['agreement_abs']-dabs[-1])<1e-12;assert abs(rr['step_abs']-sabs[-1])<1e-12
 rep=-(raw['repeat_middle_positive_negative_forces'][:,0]-raw['repeat_middle_positive_negative_forces'][:,1])/(2*plan['steps_A'][:,1,None]);repmax=np.max(abs(rep-ds[:,1]));base=raw['baseline_forces'];assert np.max(abs(base-a['projected_force']))<1e-12
 checks={'feasibility':bool(np.all(plan['branch_safe'])) and np.min(plan['steps_A'])>=t['min_step_A'] and np.max(plan['input_metrics'][:,0,:])<=t['input_direction_norm_error'],'matrix_step_absolute':absolute<t['absolute_eV_per_A2'],'matrix_step_relative':relative<t['relative'] and colrelative<t['relative'],'antisymmetry':sym<t['antisymmetry_relative'],'directional_agreement':max(dabs)<t['absolute_eV_per_A2'] and max(drel)<t['relative'],'directional_step_stability':max(sabs)<t['absolute_eV_per_A2'] and max(srel)<t['relative'],'all_middle_repeats':repmax<t['repeat_derivative_absolute'],'stationarity':np.max(abs(base))<=t['stationarity_eV_per_A'],'baseline_repeats':np.max(abs(base-base[0]))<=t['baseline_repeat_absolute'],'local_positive_stability':ev[0]>specth};assert row['checks']=={k:bool(v) for k,v in checks.items()};assert row['all_checks_pass']==all(checks.values())
 got=[]
 for j in range(m):
  for k in range(2):
   v=ds[j,k+1]-ds[j,k]
   if np.max(abs(v))>=t['absolute_eV_per_A2'] or np.linalg.norm(v)/np.linalg.norm(ds[j,1])>=t['relative']:got.append((j,k))
 assert got==[(v['column_0based'],v['pair_index']) for v in row['all_failed_columns']];records.append({'case':case,'columns':m,'directions':9,'all_geometry_and_rounding_plans_reproduced':True,'minimum_sampled_knot_distance':minmargin,'raw_differences':'byte-identical','spectra_and_full_flags':'recomputed','complete_failed_column_register':'recomputed','basis_and_stationary_identity':'PASS'})
assert r['pass_count']==sum(v['all_checks_pass'] for v in r['cases']);v={'status':'PASS_CONSTRUCTOR_INTEGRITY','records':records,'physical_promotion':0,'review':'Constructor recomputation only; non-constructor review pending','scope':'Numerical guards and tests, not interval bounds, physical identification, full Bloch stability or independent review'};(p/'VERIFICATION.json').write_text(json.dumps(v,indent=2)+'\n');print(json.dumps({'status':v['status'],'cases':len(records)}))
