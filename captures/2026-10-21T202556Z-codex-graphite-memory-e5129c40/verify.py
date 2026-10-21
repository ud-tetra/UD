from pathlib import Path
import numpy as np,json,hashlib
from scipy.integrate import solve_ivp
p=Path(__file__).resolve().parent;f=json.loads((p/'FREEZE.json').read_text());src=p.parent/f['input'];assert hashlib.sha256(src.read_bytes()).hexdigest()==f['input_sha256']
d=np.load(src);m=np.load(p/'MEMORY.npz');r=json.loads((p/'RESULTS.json').read_text());rows=[]
for row in r['rows']:
 key=row['configuration'];H=d[key+'_H'];b=d[key+'_b'];Z=m[key+'_Z'];n=len(b);k=float(m[key+'_k']);a=m[key+'_a'];A=m[key+'_A'];T=np.column_stack([Z,b]);B=np.block([[A,a[:,None]],[a[None,:],np.array([[k]])]])
 assert np.linalg.norm(T@B@T.T-H)<1e-10
 # Independent adaptive first-order ODE versus original-H spectral trajectory.
 q0=b.copy();v0=np.cos(np.arange(n));v0/=np.linalg.norm(v0);initial=np.r_[q0,v0];end=4*np.pi/np.sqrt(k);ts=np.linspace(0,end,33)
 sol=solve_ivp(lambda t,y:np.r_[y[n:],-H@y[:n]],(0,end),initial,t_eval=ts,method='DOP853',rtol=2e-12,atol=2e-13)
 assert sol.success
 lam,V=np.linalg.eigh(H);w=np.sqrt(lam);c=V.T@q0;dv=V.T@v0
 q=V@(c[:,None]*np.cos(w[:,None]*ts)+dv[:,None]*np.sin(w[:,None]*ts)/w[:,None]);v=V@(-c[:,None]*w[:,None]*np.sin(w[:,None]*ts)+dv[:,None]*np.cos(w[:,None]*ts))
 err=float(np.max(np.linalg.norm(sol.y-np.vstack([q,v]),axis=0))/max(1,np.max(np.linalg.norm(np.vstack([q,v]),axis=0))))
 # Reverse velocity at endpoint and integrate forward; recover original q,-v.
 rev=solve_ivp(lambda t,y:np.r_[y[n:],-H@y[:n]],(0,end),np.r_[sol.y[:n,-1],-sol.y[n:,-1]],method='DOP853',rtol=2e-12,atol=2e-13)
 rev_err=float(np.linalg.norm(rev.y[:,-1]-np.r_[q0,-v0])/max(1,np.linalg.norm(initial)))
 assert err<1e-9 and rev_err<1e-9
 rows.append({'configuration':key,'ode_spectral_relative_error':err,'ode_reversal_relative_error':rev_err})
assert len(rows)==36 and r['status']=='PASS'
result={'status':'PASS','input_hash_match':True,'constructor_only':True,'nonconstructor_review':'PENDING','checks':rows,'max_ode_error':max(x['ode_spectral_relative_error'] for x in rows),'max_reversal_error':max(x['ode_reversal_relative_error'] for x in rows),'physical_promotion':0}
(p/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
