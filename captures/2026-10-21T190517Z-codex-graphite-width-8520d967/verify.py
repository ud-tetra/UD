from pathlib import Path
import json,hashlib,numpy as np
p=Path(__file__).parent;summary=json.loads((p/'SUMMARY.json').read_text());rows=[]
for fn,sha in summary['input_sha256'].items():assert hashlib.sha256((p.parent/fn).read_bytes()).hexdigest()==sha
for lr in summary['rows']:
 name=lr['case'];c=lr['cutoff_A'];d=p.parent/lr['folder'];a=np.load(d/'MATRICES.npz');r=json.loads((d/'RESULTS.json').read_text())['cases'][0];e=json.loads((d/'ENERGY_CHECK.json').read_text());group=a['group_index'];n=len(group);dim=a['K_fine'].shape[0];counts=np.bincount(group);P=np.zeros((n,dim));P[np.arange(n),group]=1/np.sqrt(counts[group]);Q=np.zeros((dim,dim-1))
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
 rows.append({'case':name,'cutoff_A':c,'width_A':lr['width_A'],'inherited':lr['inherited'],'constructor_verification':'PASS','scientific_local_pass':lr['local_derivative_pass'],'scientific_energy_pass':lr['energy_pass']})

for er in summary['cutoff_endpoints']:
 name=er['case'];w=er['width_A'];root=p.parent/'graphite-smooth' if w==2 else p/f'width_{w}'
 a=np.load(root/name/'cutoff_20/MATRICES.npz');b=np.load(root/name/'cutoff_24/MATRICES.npz')
 diff={k:float(np.linalg.norm(b[k]-a[k])/np.linalg.norm(b[k])) for k in ['K_fine','g_fine']}
 assert all(abs(diff[k]-er['relative_F'][k])<1e-15 for k in diff)
 assert (diff['K_fine']<=1e-4 and diff['g_fine']<=1e-3)==er['passes']
for wr in summary['width_comparisons']:
 name=wr['case'];c=wr['cutoff_A'];u,v=wr['width_pair_A'];aa=[]
 for w in [u,v]:
  root=p.parent/'graphite-smooth' if w==2 else p/f'width_{w}';aa.append(np.load(root/name/f'cutoff_{c}/MATRICES.npz'))
 a,b=aa;diff={k:float(np.linalg.norm(b[k]-a[k])/np.linalg.norm(b[k])) for k in ['K_fine','g_fine']}
 assert all(abs(diff[k]-wr['relative_F'][k])<1e-15 for k in diff)
 assert (diff['K_fine']<=1e-4 and diff['g_fine']<=1e-3)==wr['passes']
 # An independent Householder gauge for the response diagnostic.
 responses=[]
 for a in aa:
  d=len(a['K_fine']);u=np.ones(d)/np.sqrt(d);v=u.copy();v[0]-=1;v/=np.linalg.norm(v);Q=(np.eye(d)-2*np.outer(v,v))[:,1:];K=(a['K_fine']+a['K_fine'].T)/2;responses.append(Q@np.linalg.solve(Q.T@K@Q,Q.T@a['g_fine']))
 rd=float(np.linalg.norm(responses[1]-responses[0])/np.linalg.norm(responses[1]));assert abs(rd-wr['response_relative_F'])<1e-11
assert len(rows)==36 and sum(not z['inherited'] for z in rows)==24
for inherited,key,total in [(False,'new_fine_energy_controls',576),(True,'inherited_fine_energy_controls',288)]:
 rr=[x for x in summary['rows'] if x['inherited']==inherited];assert sum(x['energy_controls'] for x in rr)==total;assert sum(x['energy_controls_passed'] for x in rr)==summary[key]['passed']
allpass=all(x['local_derivative_pass'] and x['energy_pass'] for x in summary['rows']) and all(x['passes'] for x in summary['width_comparisons']+summary['cutoff_endpoints'])
assert summary['status']==('PASS_SCOPED_WIDTH_ROBUSTNESS' if allpass else 'HOLD_SCOPED_WIDTH_ROBUSTNESS')
for w in [1,2,3]:
 pc=json.loads((p/f'PAIR_CHECK_WIDTH{w}.json').read_text());assert pc['status']=='PASS' and len(pc['checks'])==24
 assert hashlib.sha256((p/'plugin/pair_kcz_width.cpp').read_bytes()).hexdigest()==pc['source_sha256'];assert hashlib.sha256((p/'plugin'/f'kcz_width{w}.so').read_bytes()).hexdigest()==pc['binary_sha256']
for fn,sha in json.loads((p/'INHERITED_INPUTS.json').read_text()).items():assert hashlib.sha256((p.parent/fn).read_bytes()).hexdigest()==sha
res={'status':'CONSTRUCTOR_VERIFICATION_PASS','independent_review':'pending','checked_inputs':len(summary['input_sha256']),'rows':rows,'width_pairs_checked':len(summary['width_comparisons']),'cutoff_endpoints_checked':len(summary['cutoff_endpoints']),'pair_controls':72,'scientific_status':summary['status'],'bath_inference':'HOLD','physical_promotion':0}
(p/'VERIFICATION.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({k:v for k,v in res.items() if k!='rows'},indent=2))
