from pathlib import Path
import json,hashlib,numpy as np
p=Path(__file__).parent;summary=json.loads((p/'SUMMARY.json').read_text());rows=[]
for fn,sha in summary['input_sha256'].items():assert hashlib.sha256((p/fn).read_bytes()).hexdigest()==sha
for cr in summary['cases']:
 for lr in cr['local_by_cutoff']:
  name=cr['case'];c=lr['cutoff_A'];d=p/name/f'cutoff_{c}';a=np.load(d/'MATRICES.npz');r=json.loads((d/'RESULTS.json').read_text())['cases'][0];e=json.loads((d/'ENERGY_CHECK.json').read_text());group=a['group_index'];n=len(group);dim=a['K_fine'].shape[0];counts=np.bincount(group);P=np.zeros((n,dim));P[np.arange(n),group]=1/np.sqrt(counts[group]);Q=np.zeros((dim,dim-1))
  for j in range(dim-1):sc=np.sqrt((j+1)*(j+2));Q[:j+1,j]=1/sc;Q[j+1,j]=-(j+1)/sc
  for step in ['coarse','fine']:
   assert np.max(abs(P.T@a['raw_K_columns_'+step]-a['K_'+step]))<1e-12
   assert np.max(abs(P.T@a['raw_g_'+step]-a['g_'+step]))<1e-12
  K=a['K_fine'];g=a['g_fine'];eig=np.linalg.eigvalsh(Q.T@((K+K.T)/2)@Q);assert np.max(abs(eig-a['eigenvalues_projected']))<1e-11
  assert hashlib.sha256((d/'lammps.log').read_bytes()).hexdigest()==r['final_log_sha256'];assert hashlib.sha256((d/'energy.log').read_bytes()).hexdigest()==e['log_sha256'];assert hashlib.sha256((d/'MATRICES.npz').read_bytes()).hexdigest()==r['matrix_sha256']
  dirs={'first_Helmert':Q[:,0],'last_Helmert':Q[:,-1],'breathing':np.where(np.arange(dim)<dim//2,-1.,1.)/np.sqrt(dim)}
  for er in e['checks']:
   v=dirs[er['direction']];h=er['h_A'];ep,e0,em=er['raw_energies_eV'];ke=(ep-2*e0+em)/h**2;first=(ep-em)/(2*h);kref=float(v@K@v);fref=float(-((P@v)@a['vertical_forces']))
   assert abs(ke-er['K_energy'])<1e-12 and abs(kref-er['K_force'])<1e-12;assert bool(abs(ke-kref)<=1e-5+1e-4*abs(kref))==er['K_passes'];assert bool(abs(first-fref)<=2e-7)==er['first_passes']
   for gr in er['mixed']:
    ee=gr['raw_energies_eV'];ge=(ee[0]-ee[1]-ee[2]+ee[3])/(4*h*h);ref=float(v@g[:,gr['axis']]);assert abs(ge-gr['energy_mixed'])<1e-12 and abs(ref-gr['force_mixed'])<1e-12;assert bool(abs(ge-ref)<=2e-5+1e-3*abs(ref))==gr['passes']
  checks={'K_step_relative':np.linalg.norm(a['K_fine']-a['K_coarse'])/np.linalg.norm(K)<=1e-5,'K_step_max':np.max(abs(a['K_fine']-a['K_coarse']))<=1e-6,'g_step_max':np.max(abs(a['g_fine']-a['g_coarse']))<=1e-7,'symmetry':np.linalg.norm(K-K.T)/np.linalg.norm(K)<=1e-6,'translation_null':np.linalg.norm(K@np.ones(dim)/np.sqrt(dim))/np.linalg.norm(K)<=1e-6,'projected_positive':eig[0]>0}
  for key,val in checks.items():assert bool(val)==r['checks'][key]
  kleak=[];gleak=[]
  for step in ['coarse','fine']:
   C=a['raw_K_columns_'+step];G=a['raw_g_'+step]
   kleak.append(np.linalg.norm(C-P@a['K_'+step])/np.linalg.norm(C));gleak.append(np.linalg.norm(G-P@a['g_'+step])/max(np.linalg.norm(G),1e-30))
  assert bool(max(kleak)<=1e-5)==r['checks']['K_sector_invariance'];assert bool(max(gleak)<=1e-5)==r['checks']['g_sector_invariance']
  fine=[x for x in e['checks'] if x['h_A']<=.001];flags=[x['K_passes'] for x in fine]+[x['first_passes'] for x in fine]+[v['passes'] for x in fine for v in x['mixed']]
  assert all(flags)==lr['energy_pass'] and sum(flags)==lr['energy_controls_passed'] and len(flags)==lr['energy_controls']
  assert all(r['checks'].values())==lr['local_derivative_pass']
  rows.append({'case':name,'cutoff_A':c,'constructor_verification':'PASS','scientific_local_pass':lr['local_derivative_pass'],'scientific_energy_pass':lr['energy_pass']})
 a20=np.load(p/cr['case']/'cutoff_20/MATRICES.npz');a24=np.load(p/cr['case']/'cutoff_24/MATRICES.npz')
 endpoint={key:float(np.linalg.norm(a24[key]-a20[key])/np.linalg.norm(a24[key])) for key in ['K_fine','g_fine']}
 assert all(abs(endpoint[k]-cr['endpoint_20_to_24_relative_F'][k])<1e-15 for k in endpoint)
 assert (endpoint['K_fine']<=1e-4 and endpoint['g_fine']<=1e-3)==cr['endpoint_gate_pass']
 assert (cr['endpoint_gate_pass'] and all(z['local_derivative_pass'] and z['energy_pass'] for z in cr['local_by_cutoff']))==cr['case_pass']
assert summary['status']==('PASS_SCOPED_SMOOTH_MODEL' if all(x['case_pass'] for x in summary['cases']) else 'HOLD_SCOPED_SMOOTH_MODEL')
assert json.loads((p/'PAIR_CHECK.json').read_text())['status']=='PASS'
res={'status':'CONSTRUCTOR_VERIFICATION_PASS','independent_review':'pending','checked_inputs':len(summary['input_sha256']),'rows':rows,'scientific_status':summary['status'],'bath_inference':'HOLD','physical_promotion':0};(p/'VERIFICATION.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
