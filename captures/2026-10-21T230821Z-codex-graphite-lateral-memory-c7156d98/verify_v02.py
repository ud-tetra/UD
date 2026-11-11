from pathlib import Path
import json,hashlib,numpy as np
from scipy.linalg import expm
p=Path(__file__).resolve().parent;root=p.parent;f=json.loads((p/'FREEZE.json').read_text());allr=json.loads((p/'RESULTS_v02.json').read_text());th=f['thresholds'];checks=[]
for fn,sha in f['inputs'].items():assert hashlib.sha256((root/fn).read_bytes()).hexdigest()==sha
for register in ['CODE_FREEZE.json','CODE_AMENDMENT.json']:
 for fn,sha in json.loads((p/register).read_text())['files'].items():assert hashlib.sha256((p/fn).read_bytes()).hexdigest()==sha
for case,row in zip(f['cases'],allr['cases']):
 out=p/'run_v02'/case;a=np.load(out/'MODEL.npz');D=a['D'];m=len(D);n=row['vertical_dimension'];L=m-n;A=a['A'];C=a['C'];S=a['S'];U=a['A_eigenvectors'];alpha=a['A_eigenvalues'];G=a['G'];omega=np.sqrt(alpha);AiC=np.linalg.solve(A,C);H=np.load(root/'graphite-safe-full'/case/'HESSIANS.npz')['H_symmetric'];assert np.max(abs(D-H/np.linalg.eigvalsh(H)[-1]))<1e-15;assert np.max(abs(S-(D[L:,L:]-C.T@AiC)))<1e-14;assert np.linalg.norm(A@U-U*alpha)<1e-12;assert np.linalg.norm(U.T@U-np.eye(L))<1e-12
 lam,W=np.linalg.eigh(D);wf=np.sqrt(lam);Tmat=np.block([[np.zeros_like(D),np.eye(m)],[-D,np.zeros_like(D)]]);maxexp=0
 for rr in row['preparations']:
  name=rr['preparation'];r=np.load(out/(name+'.npz'));tt=r['tau'];q0=r['q0'];v0=r['v0'];co=np.cos(tt[:,None]*wf);si=np.sin(tt[:,None]*wf);q=(co*(W.T@q0)+si/wf*(W.T@v0))@W.T;v=(-si*wf*(W.T@q0)+co*(W.T@v0))@W.T;Y=r['memory_state'];z=Y[:,:n];zv=Y[:,n:2*n];R=Y[:,2*n:2*n+L];SS=Y[:,2*n+L:];eta=U.T@(q0[:L]+AiC@q0[L:]);lv=U.T@v0[:L];cc=np.cos(tt[:,None]*omega);ss=np.sin(tt[:,None]*omega);ell=(cc*eta+ss/omega*lv+R/alpha)@U.T-z@AiC.T;ev=(-omega*ss*eta+cc*lv-SS/omega)@U.T;qr=np.c_[ell,z];vr=np.c_[ev,zv];energy=.5*np.sum(vr**2,axis=1)+.5*np.einsum('ti,ij,tj->t',qr,D,qr);assert np.max(abs(energy-r['energy']))<1e-12
  values={'z_error_max':np.max(abs(z-q[:,L:])),'vertical_velocity_error_max':np.max(abs(zv-v[:,L:])),'full_position_reconstruction_error':np.max(abs(qr-q)),'full_velocity_reconstruction_error':np.max(abs(vr-v)),'energy_relative_drift':np.max(abs(energy-energy[0]))/energy[0],'omitting_initial_source_error':np.max(abs(r['omitted_source_vertical']-q[:,L:])),'quadrature_pair_change_max':np.max(abs(np.diff(r['quadrature_convolutions'],axis=0)))}
  for key,value in values.items():assert abs(value-rr[key])<1e-11
  qt=r['quadrature_times'];cq=np.cos(qt[:,None]*wf);sq=np.sin(qt[:,None]*wf);qq=(cq*(W.T@q0)+sq/wf*(W.T@v0))@W.T;acc=-qq@D.T;src=-((np.cos(qt[:,None]*omega)*eta+np.sin(qt[:,None]*omega)/omega*lv)@G);res=acc[:,L:]+qq[:,L:]@S.T+r['quadrature_convolutions'][-1]-src;assert np.max(abs(src-r['quadrature_source']))<1e-12;assert np.max(abs(res-r['quadrature_residual']))<1e-12;assert abs(np.max(abs(res))-rr['direct_history_residual_max'])<1e-11
  if name=='hidden_velocity':
   for k in [0,400,800]:
    y=expm(Tmat*tt[k])@np.r_[q0,v0];maxexp=max(maxexp,float(np.max(abs(y-np.r_[q[k],v[k]]))))
  assert rr['all_checks_pass']==all(rr['checks'].values())
 assert maxexp<th['algebra_relative'];assert row['all_checks_pass']==(all(row['model_checks'].values()) and all(v['all_checks_pass'] for v in row['preparations']));checks.append({'case':case,'recomputed_trajectories':4,'independent_first_order_exponential_max_error':maxexp,'raw_memory_reconstruction_energy_and_source':'PASS','input_identities':'PASS'})
assert allr['case_pass_count']==sum(v['all_checks_pass'] for v in allr['cases']);ver={'status':'PASS_CONSTRUCTOR_INTEGRITY','checks':checks,'physical_promotion':0,'review':'No non-constructor review; development only'};(p/'VERIFICATION_v02.json').write_text(json.dumps(ver,indent=2)+'\n');print(json.dumps(ver,indent=2))
