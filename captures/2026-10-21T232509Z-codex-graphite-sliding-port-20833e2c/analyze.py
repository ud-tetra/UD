from pathlib import Path
import numpy as np,json
from scipy.integrate import solve_ivp
p=Path(__file__).resolve().parent;root=p.parent;rows=[]
for case in json.loads((p/'FREEZE.json').read_text())['cases']:
 o=p/case;raw=np.load(o/'RAW.npz');plan=np.load(o/'PLAN.npz');d=raw['derivatives'];m=d.shape[-1]-2;H=np.load(root/'graphite-safe-full'/case/'HESSIANS.npz')['H_symmetric'];C=d[:2,1,:m].T;P=d[:2,1,m:].T;P=(P+P.T)/2;S=P-C.T@np.linalg.solve(H,C)
 adj=float(np.max(abs(np.diff(d,axis=1))));rel=max(float(np.linalg.norm(d[j,k+1]-d[j,k])/max(np.linalg.norm(d[j,k+1]),1e-30)) for j in range(2) for k in range(2));rep=-(raw['repeat_middle_positive_negative_forces'][:,0]-raw['repeat_middle_positive_negative_forces'][:,1])/(2*plan['steps_A'][:,1,None]);repeat=float(np.max(abs(rep-d[:,1])));rec=float(np.max(abs(d[2:,1,m:]-plan['vectors'][2:,:m]@C)));psym=float(np.max(abs(d[:2,1,m:]-d[:2,1,m:].T)));base=raw['baseline_forces'];baseerr=float(np.max(abs(base-base[0])));station=float(np.max(abs(base[:,:m])))
 hstar=np.linalg.eigvalsh(H)[-1];A=H/hstar;G0=C/hstar;V=P/hstar;alpha,U=np.linalg.eigh(A);G=U.T@G0;omega=np.sqrt(alpha);Ss=V-G0.T@np.linalg.solve(A,G0)
 t=np.linspace(0,80,801)
 def port(t):return np.array([np.sin(.2*t),.7*(1-np.cos(.13*t))])
 def vel(t):return np.array([.2*np.cos(.2*t),.091*np.sin(.13*t)])
 def acc(t):return np.array([-.04*np.sin(.2*t),.01183*np.cos(.13*t)])
 tests=[]
 for prep in ['zero','hidden']:
  q0=np.zeros(m);v0=np.zeros(m)
  if prep=='hidden':
   q0=np.sin(np.sqrt(2)*np.arange(1,m+1));q0/=np.linalg.norm(q0);v0=.3*np.cos(np.sqrt(3)*np.arange(1,m+1));v0/=np.linalg.norm(v0)/.3
  def rhs(t,y):return np.r_[y[m:],-A@y[:m]-G0@port(t)]
  full=solve_ivp(rhs,(0,80),np.r_[q0,v0],method='DOP853',rtol=1e-11,atol=1e-13,t_eval=t)
  def memory(t,y):return np.r_[G@vel(t)-omega*y[m:],omega*y[:m]]
  mem=solve_ivp(memory,(0,80),np.zeros(2*m),method='DOP853',rtol=1e-11,atol=1e-13,t_eval=t)
  source=(np.cos(t[:,None]*omega)*(U.T@q0)+np.sin(t[:,None]*omega)/omega*(U.T@v0))@G
  reference=np.array([acc(tt)+V@port(tt) for tt in t])+full.y[:m].T@G0
  reduced=np.array([acc(tt)+Ss@port(tt) for tt in t])+(mem.y[:m].T/alpha)@G+source
  err=float(np.max(abs(reference-reduced)));tests.append(dict(preparation=prep,max_force_error=err,pass_check=bool(full.success and mem.success and err<=1e-8)))
  np.savez_compressed(o/(prep+'.npz'),tau=t,internal_full=full.y,history=mem.y,force_reference=reference,force_memory=reduced,initial_q=q0,initial_v=v0)
 np.savez_compressed(o/'MODEL.npz',H=H,C=C,P=P,S=S,normalized_A=A,normalized_C=G0,normalized_P=V,alpha=alpha,U=U,G=G,baseline_port_force=base[0,m:],hstar=hstar)
 ok=bool(adj<=1e-6 and rel<=1e-5 and repeat<=1e-7 and rec<=1e-6 and psym<=1e-6 and baseerr<=1e-12 and station<=1e-7 and all(z['pass_check'] for z in tests))
 row=dict(case=case,pass_check=ok,adjacent_max=adj,port_relative_change=rel,repeat_max=repeat,reciprocity_max=rec,port_asymmetry=psym,baseline_repeat=baseerr,internal_stationarity=station,baseline_port_force_eV_per_A=base[0,m:].tolist(),S_eigenvalues_eV_per_A2=np.linalg.eigvalsh(S).tolist(),C_norm=float(np.linalg.norm(C)),K0_norm=float(np.linalg.norm(C.T@np.linalg.solve(H,C))),dynamics=tests);rows.append(row)
(p/'RESULTS.json').write_text(json.dumps(dict(all_pass=all(r['pass_check'] for r in rows),cases=rows,physical_promotion=0),indent=2)+'\n');print(json.dumps(rows,indent=2))
