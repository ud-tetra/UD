from pathlib import Path
import json,hashlib,numpy as np
p=Path(__file__).parent;cases=['21_dir_0','21_dir_10024','31_dir_10084','31_dir_10134'];rows=[];inputs={}
for name in cases:
 matrices={};locals=[]
 for c in [16,20,24]:
  dr=p/name/f'cutoff_{c}';a=np.load(dr/'MATRICES.npz');r=json.loads((dr/'RESULTS.json').read_text())['cases'][0];e=json.loads((dr/'ENERGY_CHECK.json').read_text());matrices[c]={k:a[k] for k in ['K_fine','g_fine']}
  oldp=p.parent/'graphite-hessian'/name if c==16 else p.parent/'graphite-cutoff'/name/f'cutoff_{c}';old=np.load(oldp/'MATRICES.npz');assert np.array_equal(old['group_index'],a['group_index']);delta=a['equilibrium_positions_A'][:,2]-old['equilibrium_positions_A'][:,2];delta-=delta.mean()
  fine=[x for x in e['checks'] if x['h_A']<=.001];controls=[bool(x['K_passes']) for x in fine]+[bool(x['first_passes']) for x in fine]+[bool(v['passes']) for x in fine for v in x['mixed']]
  failures=[]
  for x in fine:
   for k in ['K_passes','first_passes']:
    if not x[k]:failures.append({'direction':x['direction'],'h_A':x['h_A'],'check':k})
   for v in x['mixed']:
    if not v['passes']:failures.append({'direction':x['direction'],'h_A':x['h_A'],'check':'mixed','axis':v['axis'],'error':v['absolute_error']})
  locals.append({'cutoff_A':c,'local_derivative_pass':r['all_checks_pass'],'failed_local_checks':[k for k,v in r['checks'].items() if not v],'energy_pass':all(controls),'energy_controls':len(controls),'energy_controls_passed':sum(controls),'energy_failures':failures,'K_step_relative_F':r['K_step_relative_F'],'K_step_max':r['K_step_max_eV_per_A2'],'g_step_max':r['g_step_max_eV_per_A2'],'min_eigenvalue_eV_per_A2':r['minimum_projected_eigenvalue_eV_per_A2'],'g_column_norms':r['g_column_norms_eV_per_A2'],'max_energy_K_error':max(x['K_absolute_error'] for x in fine),'max_energy_g_error':max(v['absolute_error'] for x in fine for v in x['mixed']),'max_energy_first_error':max(abs(x['first_energy']-x['first_force']) for x in fine),'baseline_differences_relative_F':{k:float(np.linalg.norm(a[k]-old[k])/np.linalg.norm(old[k])) for k in ['K_fine','g_fine']},'baseline_geometry_centered_max_A':float(abs(delta).max()),'residual_vertical_force_max':r['initial_vertical_force_max_eV_per_A']})
  for fn in ['MATRICES.npz','RESULTS.json','ENERGY_CHECK.json','lammps.log','energy.log']:
   fp=dr/fn;inputs[str(fp.relative_to(p))]=hashlib.sha256(fp.read_bytes()).hexdigest()
 diff={k:float(np.linalg.norm(matrices[24][k]-matrices[20][k])/np.linalg.norm(matrices[24][k])) for k in ['K_fine','g_fine']};endpoint=diff['K_fine']<=1e-4 and diff['g_fine']<=1e-3
 rows.append({'case':name,'local_by_cutoff':locals,'endpoint_20_to_24_relative_F':diff,'endpoint_gate_pass':endpoint,'case_pass':endpoint and all(z['local_derivative_pass'] and z['energy_pass'] for z in locals)})
res={'status':'PASS_SCOPED_SMOOTH_MODEL' if all(r['case_pass'] for r in rows) else 'HOLD_SCOPED_SMOOTH_MODEL','model_id':'KCz-C2-unshifted-tail-v0.1','cases':rows,'input_sha256':inputs,'scope':'Four pointwise primitive-periodic vertical sectors at three finite cutoffs; no full Bloch-sector or infinite-range claim','bath_inference':'HOLD','physical_promotion':0}
(p/'SUMMARY.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
