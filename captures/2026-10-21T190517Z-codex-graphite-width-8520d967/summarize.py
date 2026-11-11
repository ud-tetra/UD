from pathlib import Path
import numpy as np,json,hashlib,itertools
p=Path(__file__).resolve().parent;base=p.parent;cases=['21_dir_0','21_dir_10024','31_dir_10084','31_dir_10134'];h=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
for fn,sha in json.loads((p/'INHERITED_INPUTS.json').read_text()).items():assert h(base/fn)==sha,fn

def folder(name,c,w):return base/'graphite-smooth'/name/f'cutoff_{c}' if w==2 else p/f'width_{w}'/name/f'cutoff_{c}'

def response(a):
 d=len(a['K_fine']);Q=np.zeros((d,d-1))
 for j in range(d-1):scale=np.sqrt((j+1)*(j+2));Q[:j+1,j]=1/scale;Q[j+1,j]=-(j+1)/scale
 K=(a['K_fine']+a['K_fine'].T)/2
 return Q@np.linalg.solve(Q.T@K@Q,Q.T@a['g_fine'])
rows=[];inputs={};newpass=0;oldpass=0;sensitivity=[];endpoint=[]
for name in cases:
 mats={};resp={}
 for c in [16,20,24]:
  for w in [1,2,3]:
   dr=folder(name,c,w);a=np.load(dr/'MATRICES.npz');r=json.loads((dr/'RESULTS.json').read_text())['cases'][0];e=json.loads((dr/'ENERGY_CHECK.json').read_text());mats[c,w]={k:a[k] for k in ['K_fine','g_fine','group_index']};resp[c,w]=response(a)
   erows=[z for z in e['checks'] if z['h_A']<=.001];flags=[z['K_passes'] for z in erows]+[z['first_passes'] for z in erows]+[v['passes'] for z in erows for v in z['mixed']];passed=sum(flags)
   if w==2:oldpass+=passed
   else:newpass+=passed
   efail=[]
   for z in erows:
    for k in ['K_passes','first_passes']:
     if not z[k]:efail.append({'direction':z['direction'],'h_A':z['h_A'],'check':k})
    for v in z['mixed']:
     if not v['passes']:efail.append({'direction':z['direction'],'h_A':z['h_A'],'check':'mixed','axis':v['axis'],'error':v['absolute_error']})
   rows.append({'case':name,'cutoff_A':c,'width_A':w,'inherited':w==2,'folder':str(dr.relative_to(base)),'local_derivative_pass':r['all_checks_pass'],'failed_local_checks':[k for k,v in r['checks'].items() if not v],'energy_pass':all(flags),'energy_controls':len(flags),'energy_controls_passed':passed,'energy_failures':efail,'g_step_max_eV_per_A2':r['g_step_max_eV_per_A2'],'K_step_relative_F':r['K_step_relative_F'],'K_step_max_eV_per_A2':r['K_step_max_eV_per_A2'],'min_eigenvalue_eV_per_A2':r['minimum_projected_eigenvalue_eV_per_A2'],'g_column_norms':r['g_column_norms_eV_per_A2'],'max_fine_energy_g_error':max(v['absolute_error'] for z in erows for v in z['mixed']),'max_fine_energy_K_error':max(z['K_absolute_error'] for z in erows),'max_fine_first_error':max(abs(z['first_energy']-z['first_force']) for z in erows),'residual_vertical_force_max':r['initial_vertical_force_max_eV_per_A'],'response_column_norms':np.linalg.norm(resp[c,w],axis=0).tolist()})
   for fn in ['MATRICES.npz','RESULTS.json','ENERGY_CHECK.json','lammps.log','energy.log']:inputs[str((dr/fn).relative_to(base))]=h(dr/fn)
  for u,v in itertools.combinations([1,2,3],2):
   assert np.array_equal(mats[c,u]['group_index'],mats[c,v]['group_index']);diff={k:float(np.linalg.norm(mats[c,v][k]-mats[c,u][k])/np.linalg.norm(mats[c,v][k])) for k in ['K_fine','g_fine']};response_diff=float(np.linalg.norm(resp[c,v]-resp[c,u])/np.linalg.norm(resp[c,v]));sensitivity.append({'case':name,'cutoff_A':c,'width_pair_A':[u,v],'relative_F':diff,'response_relative_F':response_diff,'passes':diff['K_fine']<=1e-4 and diff['g_fine']<=1e-3})
 for w in [1,2,3]:
  diff={k:float(np.linalg.norm(mats[24,w][k]-mats[20,w][k])/np.linalg.norm(mats[24,w][k])) for k in ['K_fine','g_fine']};endpoint.append({'case':name,'width_A':w,'relative_F':diff,'passes':diff['K_fine']<=1e-4 and diff['g_fine']<=1e-3})
res={'status':'PASS_SCOPED_WIDTH_ROBUSTNESS' if all(r['local_derivative_pass'] and r['energy_pass'] for r in rows) and all(r['passes'] for r in sensitivity+endpoint) else 'HOLD_SCOPED_WIDTH_ROBUSTNESS','model_id':'KCz-C2-width-sensitivity-v0.2','rows':rows,'width_comparisons':sensitivity,'cutoff_endpoints':endpoint,'new_fine_energy_controls':{'passed':newpass,'total':576},'inherited_fine_energy_controls':{'passed':oldpass,'total':288},'input_sha256':inputs,'physical_promotion':0,'bath_inference':'HOLD','scope':'Declared width1/2/3 A and cutoff16/20/24 A grid at4 configurations, primitive-periodic vertical sector only; constructor checks, not independent review or physical bridge'}
(p/'SUMMARY.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({k:v for k,v in res.items() if k not in ['rows','width_comparisons','cutoff_endpoints','input_sha256']},indent=2))
