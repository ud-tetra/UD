from pathlib import Path
import json,hashlib,numpy as np
from scipy.integrate import solve_ivp
from numpy.polynomial.legendre import leggauss
p=Path(__file__).resolve().parent;root=p.parent;f=json.loads((p/'FREEZE.json').read_text());th=f['thresholds'];ts=np.linspace(0,f['trajectory_grid']['tau_end'],f['trajectory_grid']['samples']);qt=np.linspace(0,80,17);allrows=[]
for fn,sha in f['inputs'].items():assert hashlib.sha256((root/fn).read_bytes()).hexdigest()==sha
for fn,sha in json.loads((p/'CODE_FREEZE.json').read_text())['files'].items():assert hashlib.sha256((p/fn).read_bytes()).hexdigest()==sha
for case in f['cases']:
 out=p/case;out.mkdir();H=np.load(root/'graphite-safe-full'/case/'HESSIANS.npz')['H_symmetric'];hstar=np.linalg.eigvalsh(H)[-1];D=H/hstar;m=len(D);n=(m+2)//3;L=m-n;A=D[:L,:L];C=D[:L,L:];V=D[L:,L:];alpha,U=np.linalg.eigh(A);omega=np.sqrt(alpha);G=U.T@C;AiC=np.linalg.solve(A,C);S=V-C.T@AiC;K0=G.T@(G/alpha[:,None]);lam,W=np.linalg.eigh(D);wfull=np.sqrt(lam)
 def full(t,q0,v0):
  t=np.atleast_1d(t);co=np.cos(t[:,None]*wfull);si=np.sin(t[:,None]*wfull);qq=(co*(W.T@q0)+si/wfull*(W.T@v0))@W.T;vv=(-si*wfull*(W.T@q0)+co*(W.T@v0))@W.T;aa=(-co*lam*(W.T@q0)-si*wfull*(W.T@v0))@W.T;return qq,vv,aa
 def kernel(t):return G.T@((np.cos(omega*t)/alpha)[:,None]*G)
 def normalize(z):return z/np.linalg.norm(z)
 zinit=normalize(np.sin(np.sqrt(2)*np.arange(1,n+1)));ellinit=normalize(np.sin(np.sqrt(2)*np.arange(1,L+1)));ellvel=normalize(np.cos(np.sqrt(3)*np.arange(1,L+1)));preps=[]
 for name in ['vertical_unrelaxed','conditional_lateral_equilibrium','hidden_displacement','hidden_velocity']:
  q0=np.zeros(m);v0=np.zeros(m)
  if name in ['vertical_unrelaxed','conditional_lateral_equilibrium']:q0[L:]=zinit
  if name=='conditional_lateral_equilibrium':q0[:L]=-AiC@zinit
  if name=='hidden_displacement':q0[:L]=ellinit
  if name=='hidden_velocity':v0[:L]=ellvel
  preps.append((name,q0,v0))
 transfer=[]
 for sr,si in f['transfer_s']:
  s=complex(sr,si);kh=G.T@((s/(alpha*(s*s+alpha)))[:,None]*G);eff=s*s*np.eye(n)+S+s*kh;full_inverse=np.linalg.inv(s*s*np.eye(m)+D)[L:,L:];red=np.linalg.inv(eff);transfer.append(float(np.linalg.norm(red-full_inverse)/np.linalg.norm(full_inverse)))
 pts=np.linspace(0,80,8);vectors=np.sin(np.sqrt(2)*np.outer(np.arange(1,9),np.arange(1,n+1)));vectors/=np.linalg.norm(vectors);gram=sum(vectors[i]@kernel(pts[i]-pts[j])@vectors[j] for i in range(8) for j in range(8));feat=np.sum(np.exp(1j*pts[:,None]*omega)*(vectors@G.T),axis=0);positive=np.sum(abs(feat)**2/alpha);positive_error=float(abs(gram-positive)/max(abs(positive),1e-14));algebra=max(np.linalg.norm(A-U@np.diag(alpha)@U.T)/np.linalg.norm(A),np.linalg.norm(K0-C.T@AiC)/np.linalg.norm(K0));np.savez_compressed(out/'MODEL.npz',D=D,h_star=hstar,A=A,C=C,V=V,S=S,A_eigenvalues=alpha,A_eigenvectors=U,G=G,K0=K0,full_eigenvalues=lam,full_eigenvectors=W)
 rows=[]
 for name,q0,v0 in preps:
  eta=U.T@(q0[:L]+AiC@q0[L:]);lv=U.T@v0[:L]
  def source(t):return -G.T@(np.cos(omega*t)*eta+np.sin(omega*t)/omega*lv)
  def solve(use_source):
   def rhs(t,y):
    z,v,r,s=np.split(y,[n,2*n,2*n+L]);ff=source(t) if use_source else np.zeros(n);return np.r_[v,-S@z-G.T@(r/alpha)+ff,G@v-omega*s,omega*r]
   y0=np.r_[q0[L:],v0[L:],np.zeros(2*L)];return solve_ivp(rhs,(0,80),y0,method=f['reduced_integrator']['method'],rtol=f['reduced_integrator']['rtol'],atol=f['reduced_integrator']['atol'],t_eval=ts)
  sol=solve(True);omit=solve(False);assert sol.success and omit.success;Y=sol.y.T;Z=Y[:,:n];Zv=Y[:,n:2*n];R=Y[:,2*n:2*n+L];T=Y[:,2*n+L:];co=np.cos(ts[:,None]*omega);si=np.sin(ts[:,None]*omega);ell=(co*eta+si/omega*lv+R/alpha)@U.T-Z@AiC.T;elldot=(-omega*si*eta+co*lv-T/omega)@U.T;qrec=np.c_[ell,Z];vrec=np.c_[elldot,Zv];qref,vref,aref=full(ts,q0,v0);zerr=float(np.max(abs(Z-qref[:,L:])));verr=float(np.max(abs(Zv-vref[:,L:])));zrel=float(zerr/max(np.max(abs(qref[:,L:])),1e-14));vrel=float(verr/max(np.max(abs(vref[:,L:])),1e-14));qerr=float(np.max(abs(qrec-qref)));allverr=float(np.max(abs(vrec-vref)));energy=.5*np.sum(vrec*vrec,axis=1)+.5*np.einsum('ti,ij,tj->t',qrec,D,qrec);edrift=float(np.max(abs(energy-energy[0]))/energy[0]);ablation=float(np.max(abs(omit.y.T[:,:n]-qref[:,L:])));qrefq,vrefq,arefq=full(qt,q0,v0);conv=[]
  for count in f['direct_quadrature']['Gauss_Legendre_nodes']:
   gx,gw=leggauss(count);cs=[]
   for tt in qt:
    if tt==0:cs.append(np.zeros(n));continue
    nodes=(gx+1)*tt/2;weights=gw*tt/2;vv=full(nodes,q0,v0)[1][:,L:];val=np.sum(weights[:,None]*np.cos((tt-nodes)[:,None]*omega)*(vv@G.T),axis=0)/alpha;cs.append(val@G)
   conv.append(cs)
  conv=np.array(conv);src=np.array([source(tt) for tt in qt]);resid=arefq[:,L:]+qrefq[:,L:]@S.T+conv[-1]-src;quadres=float(np.max(abs(resid)));quadchange=float(np.max(abs(conv[1]-conv[0])));acc0=float(np.max(abs(-S@q0[L:]+source(0)-(-V@q0[L:]-C.T@q0[:L]))));checks={'trajectory_absolute':max(zerr,verr,qerr,allverr)<th['trajectory_absolute'],'trajectory_relative':max(zrel,vrel)<th['trajectory_relative'],'direct_history_residual':quadres<th['quadrature_residual_absolute'],'quadrature_pair':quadchange<th['quadrature_change_absolute'],'energy_drift':edrift<th['energy_relative_drift'],'initial_acceleration':acc0<th['initial_acceleration_absolute'],'source_ablation':ablation<th['trajectory_absolute'] if name=='conditional_lateral_equilibrium' else ablation>th['ablation_minimum_visible_error']};row={'preparation':name,'all_checks_pass':bool(all(checks.values())),'checks':checks,'z_error_max':zerr,'vertical_velocity_error_max':verr,'z_error_relative':zrel,'vertical_velocity_error_relative':vrel,'full_position_reconstruction_error':qerr,'full_velocity_reconstruction_error':allverr,'energy_relative_drift':edrift,'direct_history_residual_max':quadres,'quadrature_pair_change_max':quadchange,'initial_acceleration_error':acc0,'omitting_initial_source_error':ablation};rows.append(row);np.savez_compressed(out/(name+'.npz'),tau=ts,q0=q0,v0=v0,memory_state=Y,omitted_source_vertical=omit.y.T[:,:n],energy=energy,quadrature_times=qt,quadrature_convolutions=conv,quadrature_source=src,quadrature_residual=resid);print(case+' '+name+' '+str(row['all_checks_pass']),flush=True)
 modelchecks={'SPD':bool(np.linalg.eigvalsh(S)[0]>0 and alpha[0]>0),'algebra':algebra<th['algebra_relative'],'transfer':max(transfer)<th['transfer_relative'],'positive_type':positive_error<th['positive_type_relative'] and gram>=-1e-12,'K0_PSD':np.linalg.eigvalsh(K0)[0]>=-th['algebra_relative']*np.linalg.norm(K0,2)};case_result={'case':case,'all_checks_pass':bool(all(modelchecks.values()) and all(v['all_checks_pass'] for v in rows)),'model_checks':modelchecks,'scale_h_star_eV_per_A2':hstar,'lateral_dimension':L,'vertical_dimension':n,'S_min_eigenvalue':float(np.linalg.eigvalsh(S)[0]),'K0_norm_F':float(np.linalg.norm(K0)),'algebra_relative_error':float(algebra),'transfer_relative_errors':transfer,'positive_type_relative_identity_error':positive_error,'positive_type_quadratic_value':float(gram),'preparations':rows,'physical_promotion':0};(out/'RESULTS.json').write_text(json.dumps(case_result,indent=2)+'\n');allrows.append(case_result)
r={'status':'CONSERVATIVE_LATERAL_MEMORY_CHECK_COMPLETE','case_pass_count':sum(v['all_checks_pass'] for v in allrows),'preparation_pass_count':sum(w['all_checks_pass'] for v in allrows for w in v['preparations']),'cases':allrows,'physical_promotion':0,'scope':f['scope'],'review':'constructor only; non-constructor pending'};(p/'RESULTS.json').write_text(json.dumps(r,indent=2)+'\n')
