"""New bounded source-faithful R6b reconstruction; no archived module is imported."""
from pathlib import Path
import json,hashlib,traceback,warnings
import numpy as np
from scipy.linalg import eigh
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import eigsh,ArpackNoConvergence
C=Path(__file__).parent
def sha(b):return hashlib.sha256(b).hexdigest()
def write(n,v):(C/n).write_text(json.dumps(v,indent=2,allow_nan=False)+'\n')
def build(level=4):
 N=4**level;eta=185/192;rho=np.zeros((N,N));theta=np.zeros((N,N))
 for i in range(N):
  for j in range(i+1,N):
   if i//4==j//4:
    w=eta**2;rho[i,j]-=w;rho[j,i]-=w;rho[i,i]+=w;rho[j,j]+=w
   if i//64==j//64 and i//4!=j//4:
    w=eta**4 if i//16==j//16 else eta**6
    theta[i,j]-=w;theta[j,i]-=w;theta[i,i]+=w;theta[j,j]+=w
 depths=[];parities=[]
 for i in range(N):
  digits=[(i//4**k)%4 for k in range(level-1,-1,-1)]
  h=next((k+1 for k,d in enumerate(digits) if d),level);depths.append(h);parities.append((-1)**sum(digits))
  rho[i,i]+=(7/192)*(1-eta**h)
 x=1-eta**np.array(depths);y=eta**np.array(depths)-eta**(2*np.array(depths))
 cross=np.array(parities)*eta**2*(1-eta)*x*y
 cross[np.abs(cross)<=1e-18]=0
 full=np.block([[rho,np.diag(cross)],[np.diag(cross),theta]])
 return theta,rho,full,np.array(depths),np.array(parities)
def metrics(v):
 W=float(np.vdot(v,v).real)
 if W==0:return {'W':0,'defined':False}
 q=np.abs(v)**2/W;N=len(q);wc=q.reshape(-1,64).sum(axis=1)
 cipr=float(wc@wc);glob=float(N*(q@q));conditioned=glob/((N/64)*cipr)
 fc=[float(64*(block@block)/(w*w)) if w>0 else None for block,w in zip(q.reshape(-1,64),wc)]
 return {'W':W,'defined':True,'global_F':glob,'component_IPR':cipr,'effective_components':1/cipr,'conditioned_F':conditioned,'component_weights':wc.tolist(),'F_per_component':fc,'low_weight_numerical_flag':W<1e-12}
def clusters(w,s):
 out=[];start=0
 for i in range(1,len(w)):
  tol=s['cluster_atol']+s['cluster_rtol']*max(abs(float(w[start])),abs(float(w[i])))
  if abs(w[i]-w[start])>tol:out.append(np.arange(start,i));start=i
 out.append(np.arange(start,len(w)));return out
def checks(A,w,V,s):
 norm=float(np.linalg.norm(A,np.inf));res=np.linalg.norm(A@V-V*w,axis=0)
 scaled=res/np.maximum(1,norm+np.abs(w));orth=float(np.linalg.norm(V.T@V-np.eye(len(w)),ord='fro'))
 return {'max_absolute_residual':float(max(res,default=0)),'max_scaled_residual':float(max(scaled,default=0)),'orthogonality_frobenius':orth,'residual_pass':bool(np.all(scaled<=s['residual_tol'])),'orthogonality_pass':orth<=s['orthogonality_tol']}
def run():
 s=json.loads((C/'SETTINGS.json').read_text());f=json.loads((C/'PRE_RUN_RECEIPT.json').read_text())
 assert sha((C/'SETTINGS.json').read_bytes())==f['settings_sha256']
 assert sha(Path(__file__).read_bytes())==f['runner_sha256']
 assert sha((C/'INPUTS.npz').read_bytes())==f['input_sha256']
 z=np.load(C/'INPUTS.npz');theta=z['theta'];rho=z['rho'];A=z['full'];v0=z['v0'];N=s['N']
 payload={k:z[k] for k in z.files};failures=[];summary={'checks':{},'theta':{},'coupled':{},'probes':[]}
 def dense(H):return eigh(H,driver='evd',check_finite=True)
 wt,Vt=dense(theta);payload.update(theta_eigenvalues=wt,theta_eigenvectors=Vt)
 summary['checks']['theta_dense']=checks(theta,wt,Vt,s)
 eta=185/192;a=eta**4;b=eta**6;targets=[(0.,4),(12*a+48*b,192),(64*b,12),(16*a+48*b,48)]
 targets.sort();theta_records=[]
 I=np.eye(64);E4=(np.arange(64)[:,None]//4==np.arange(64)[None,:]//4)/4
 E16=(np.arange(64)[:,None]//16==np.arange(64)[None,:]//16)/16;E64=np.ones((64,64))/64
 exact_projectors={0.:E64,12*a+48*b:I-E4,64*b:E16-E64,16*a+48*b:E4-E16}
 for target,mult in targets:
  idx=np.where(np.abs(wt-target)<=s['theta_eigenvalue_tol'])[0];V=Vt[:,idx]
  P=V@V.T;expected=np.kron(np.eye(4),exact_projectors[target]);err=float(np.linalg.norm(P-expected,'fro'))
  theta_records.append({'expected_eigenvalue':target,'expected_rank':mult,'returned_rank':len(idx),'max_eigenvalue_error':float(max(np.abs(wt[idx]-target),default=0)),'projector_error_frobenius':err,'pass':len(idx)==mult and err<=s['theta_projector_tol']})
 zero_idx=np.where(np.abs(wt)<=s['theta_eigenvalue_tol'])[0];zero=Vt[:,zero_idx]
 summary['theta']={'exact_spectrum_comparison':theta_records,'zero_modes':[metrics(zero[:,i]) for i in range(zero.shape[1])],'zero_projector_density':metrics(np.sqrt(np.maximum(np.diag(zero@zero.T),0)/len(zero_idx)))}
 w,V=dense(A);payload.update(coupled_eigenvalues=w,coupled_eigenvectors=V)
 summary['checks']['coupled_dense']=checks(A,w,V,s)
 # Independent blockwise eigensolve, retaining the original global coordinate order.
 wb=[];vb=[]
 for comp in range(4):
  idx=np.r_[np.arange(comp*64,(comp+1)*64),N+np.arange(comp*64,(comp+1)*64)]
  e,U=dense(A[np.ix_(idx,idx)]);emb=np.zeros((2*N,len(e)));emb[idx,:]=U;wb.extend(e);vb.append(emb)
 wb=np.asarray(wb);Vb=np.column_stack(vb);order=np.argsort(wb);wb=wb[order];Vb=Vb[:,order]
 payload.update(blockwise_eigenvalues=wb,blockwise_eigenvectors=Vb)
 summary['checks']['blockwise_dense']=checks(A,wb,Vb,s)
 cs=clusters(w,s);cluster_rows=[]
 for ci,idx in enumerate(cs):
  Q=V[:,idx];B=Vb[:,idx];P=Q@Q.T;Pb=B@B.T
  err=float(np.linalg.norm(P-Pb,'fro')/max(1,np.sqrt(len(idx))))
  left=float(w[idx[0]]-w[idx[0]-1]) if idx[0] else None
  right=float(w[idx[-1]+1]-w[idx[-1]]) if idx[-1]+1<len(w) else None
  theta_trace=float(np.trace(P[N:,N:]));rho_trace=float(np.trace(P[:N,:N]))
  row={'id':ci,'indices':[int(idx[0]),int(idx[-1])],'rank':len(idx),'lambda_min':float(w[idx[0]]),'lambda_max':float(w[idx[-1]]),'gap_left':left,'gap_right':right,'relative_projector_error_global_vs_blockwise':err,'theta_weight_mean':theta_trace/len(idx),'rho_weight_mean':rho_trace/len(idx),'projector_pass':err<=s['coupled_projector_tol']}
  if theta_trace/len(idx)>.6:
   row['theta_projector_density']=metrics(np.sqrt(np.maximum(np.diag(P)[N:],0)/theta_trace))
   for name,U in [('global',V[:,idx]),('blockwise',Vb[:,idx])]:
    ms=[metrics(U[N:,j]) for j in range(U.shape[1])];keep=[x for x in ms if x['defined']]
    row[name+'_theta_mode_ranges']={key:[min(x[key] for x in keep),max(x[key] for x in keep)] for key in ['W','global_F','conditioned_F','effective_components']}
  cluster_rows.append(row)
 summary['coupled']={'dimension':len(w),'numerical_clusters':cluster_rows,'global_vs_blockwise_eigenvalue_max_error':float(max(np.abs(w-wb))),'all_cluster_projectors_pass':all(x['projector_pass'] for x in cluster_rows)}
 for pi,sigma in enumerate(s['probes']):
  call={'sigma':sigma,'k':s['k'],'which':'LM','mode':'normal','tol':s['eigsh_tol'],'maxiter':s['maxiter'],'ncv':s['ncv'],'v0_hash':f['v0_sha256'],'rng':s['rng_seed']}
  try:
   with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter('always');ew,EV=eigsh(csc_matrix(A),k=s['k'],sigma=sigma,which='LM',v0=v0.copy(),ncv=s['ncv'],maxiter=s['maxiter'],tol=s['eigsh_tol'],mode='normal',rng=s['rng_seed'])
   call['warnings']=[str(x.message) for x in caught];call['solver_status']='RETURNED'
  except ArpackNoConvergence as exc:
   ew=exc.eigenvalues;EV=exc.eigenvectors;call['solver_status']='ARPACK_PARTIAL';call['error']=str(exc);failures.append({'probe':sigma,'traceback':traceback.format_exc()})
  except Exception as exc:
   failures.append({'probe':sigma,'traceback':traceback.format_exc()});call.update(solver_status='FAILED',error=str(exc));summary['probes'].append(call);continue
  order=np.argsort(ew);ew=ew[order];EV=EV[:,order];payload[f'probe{pi}_eigenvalues']=ew;payload[f'probe{pi}_eigenvectors']=EV
  call['checks']=checks(A,ew,EV,s);call['modes']=[];coverage={}
  for j,lam in enumerate(ew):
   nearest=int(np.argmin(np.abs(w-lam)));ci=next(i for i,idx in enumerate(cs) if nearest in idx)
   coverage.setdefault(ci,[]).append(j);call['modes'].append({'eigenvalue':float(lam),'reference_cluster':ci,'rho':metrics(EV[:N,j]),'theta':metrics(EV[N:,j])})
  call['cluster_coverage']=[]
  for ci,jj in coverage.items():
   Q=V[:,cs[ci]];U=EV[:,jj];contained=float(np.linalg.norm(U-Q@(Q.T@U),'fro')/max(1,np.sqrt(len(jj))))
   complete=len(jj)==len(cs[ci]);entry={'reference_cluster':ci,'returned_rank':len(jj),'reference_rank':len(cs[ci]),'subspace_containment_error':contained,'coverage_status':'COMPLETE' if complete else 'INCOMPLETE_EIGENSPACE'}
   if complete:entry['relative_projector_error']=float(np.linalg.norm(U@U.T-Q@Q.T,'fro')/max(1,np.sqrt(len(jj))))
   call['cluster_coverage'].append(entry)
  summary['probes'].append(call)
 allchecks=all(v['residual_pass'] and v['orthogonality_pass'] for v in summary['checks'].values())
 allchecks=allchecks and all(x['pass'] for x in theta_records) and summary['coupled']['all_cluster_projectors_pass']
 for p in summary['probes']:
  if 'checks' in p:allchecks=allchecks and p['checks']['residual_pass'] and p['checks']['orthogonality_pass']
  else:allchecks=False
 np.savez_compressed(C/'NUMERICAL_PAYLOAD.npz',**payload)
 summary.update(status='PASS_NUMERICAL_SCOPED' if allchecks and not failures else 'REVIEW_REQUIRED',failure_log=failures,payload_sha256=sha((C/'NUMERICAL_PAYLOAD.npz').read_bytes()),pre_run_receipt_sha256=sha((C/'PRE_RUN_RECEIPT.json').read_bytes()),physical_promotion=0,independent_review='PENDING',scope='Fresh source-faithful clean R6b L4 reconstruction; not recovered historical execution, not VersionB disorder, not experiment')
 write('RESULTS.json',summary)
 print(json.dumps({'status':summary['status'],'theta_pass':all(x['pass'] for x in theta_records),'coupled_clusters':len(cs),'max_dense_scaled_residual':summary['checks']['coupled_dense']['max_scaled_residual'],'projector_max_error':max(x['relative_projector_error_global_vs_blockwise'] for x in cluster_rows),'probes':[{'sigma':p['sigma'],'status':p['solver_status'],'coverage':p.get('cluster_coverage')} for p in summary['probes']]}))
if __name__=='__main__':run()
