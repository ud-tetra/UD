"""Constructor-side checks on the frozen runtime angular records and force receipts."""
from pathlib import Path
import json,hashlib,numpy as np
R=Path(__file__).resolve().parent
out={}
for c in ('21_dir_0','21_dir_10024'):
 j=json.loads((R/f'{c}_runtime_trace.json').read_text())
 a=np.load(R/f'{c}_runtime_middle_records.npz');b=np.load(R/f'{c}_python_middle_records.npz')
 assert np.array_equal(a['ids_1based'],b['ids_1based'])
 assert len(a['ids_1based'])==3024
 h=2e-5;terms=a['projected_force_eV_per_A']
 S=-((-3*terms[:,0]+4*terms[:,1]-terms[:,2])-(3*terms[:,0]-4*terms[:,3]+terms[:,4]))/(2*h)
 row=next(r for r in j['rows'] if r['h_A']==h)
 assert np.max(abs(S-a['side_S_eV_per_A2']))<1e-12
 assert abs(np.sum(S)-row['runtime_direct_angle_S_eV_per_A2'])<1e-11
 changed=np.any(a['segment'][:,1:]!=a['segment'][:,0,None],axis=1)
 assert np.sum(changed)==row['changed_segment_calls']
 assert abs(np.sum(S[changed])-row['changed_segment_S_eV_per_A2'])<1e-11
 assert abs(np.sum(S[~changed])-row['unchanged_segment_S_eV_per_A2'])<1e-11
 assert j['baseline_plugin_vs_builtin_raw_force_max_abs_eV_per_A']==0.0
 assert all(r['plugin_vs_builtin_raw_force_max_abs_eV_per_A']==0.0 for r in j['rows'])
 assert max(r['plugin_vs_archived_first_layer_max_abs_eV_per_A'] or 0 for r in j['rows'])<5e-12
 cos_err=np.max(abs(a['cos_A']-b['cos_A']))
 force_err=np.max(abs(a['projected_force_eV_per_A']-b['projected_force_eV_per_A']))
 branch_different=a['segment']!=b['segment']
 assert np.max(abs(a['cos_A'][branch_different]+.5))<1e-12
 assert cos_err<3e-14 and force_err<2e-14
 out[c]={'raw_force_plugin_vs_builtin_max_abs_eV_per_A':0.0,
         'archive_first_layer_max_abs_eV_per_A':max(r['plugin_vs_archived_first_layer_max_abs_eV_per_A'] or 0 for r in j['rows']),
         'runtime_vs_python_max_cos_delta':float(cos_err),
         'runtime_vs_python_max_per_call_projected_force_eV_per_A':float(force_err),
         'segment_disagreements_at_near_join':int(np.sum(branch_different)),
         'middle_step_direct_angle_S_eV_per_A2':float(np.sum(S)),
         'middle_step_full_minus_direct_eV_per_A2':row['full_minus_direct_eV_per_A2'],
         'call_count':len(a['ids_1based'])}
print(json.dumps(out,indent=2))
(R/'runtime_trace_verification.json').write_text(json.dumps(out,indent=2)+'\n')
