from pathlib import Path
import json,hashlib
import numpy as np
root=Path(__file__).parent;prior=root.parent/'graphite-hessian';cases=['21_dir_0','21_dir_10024','31_dir_10084','31_dir_10134'];summaries=[]
for name in cases:
 records={};matrices={}
 for cutoff in [16,20,24]:
  p=prior/name if cutoff==16 else root/name/f'cutoff_{cutoff}'
  r=json.loads((p/'RESULTS.json').read_text())['cases'][0];a=np.load(p/'MATRICES.npz');assert hashlib.sha256((p/'MATRICES.npz').read_bytes()).hexdigest()==r['matrix_sha256'];assert hashlib.sha256((p/'lammps.log').read_bytes()).hexdigest()==r['final_log_sha256']
  records[cutoff]=r;matrices[cutoff]={k:a[k] for k in ['K_fine','g_fine','group_index']}
 assert np.array_equal(matrices[16]['group_index'],matrices[20]['group_index']) and np.array_equal(matrices[20]['group_index'],matrices[24]['group_index'])
 differences={}
 for a,b in [(16,20),(20,24),(16,24)]:
  differences[f'{a}_to_{b}']={key:float(np.linalg.norm(matrices[b][key]-matrices[a][key])/np.linalg.norm(matrices[b][key])) for key in ['K_fine','g_fine']}
 energy=json.loads((root/name/'ENERGY_CHECK.json').read_text());assert hashlib.sha256((root/name/'energy.log').read_bytes()).hexdigest()==energy['log_sha256']
 tail=differences['20_to_24'];cutpass=tail['K_fine']<=1e-4 and tail['g_fine']<=1e-3
 erows=[r for r in energy['checks'] if r['h_A']<=.001]
 summaries.append({'case':name,'cutoff_differences_relative_F':differences,'minimum_stiffness_by_cutoff_eV_per_A2':{str(c):records[c]['minimum_projected_eigenvalue_eV_per_A2'] for c in records},'coupling_norm_x_by_cutoff_eV_per_A2':{str(c):records[c]['g_column_norms_eV_per_A2'][0] for c in records},'cutoff_gate_pass':bool(cutpass),'local_derivative_checks_pass_by_cutoff':{str(c):records[c]['all_checks_pass'] for c in records},'local_derivative_failed_checks_by_cutoff':{str(c):[k for k,v in records[c]['checks'].items() if not v] for c in records},'directional_energy_force_pass':energy['all_fine_checks_pass'],'max_fine_energy_K_absolute_error':max(r['K_absolute_error'] for r in erows),'max_fine_energy_g_absolute_error':max(v['absolute_error'] for r in erows for v in r['mixed'])})
result={'status':'PASS_SCOPED_NUMERICAL' if all(r['cutoff_gate_pass'] and r['directional_energy_force_pass'] and all(r['local_derivative_checks_pass_by_cutoff'].values()) for r in summaries) else 'HOLD_SCOPED_FAILURE','cases':summaries,'physical_promotion':0,'scope':'finite-cutoff sensitivity and selected directional energy-force checks; not infinite-range convergence, all-entry energy verification or physical identification'}
(root/'SUMMARY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
