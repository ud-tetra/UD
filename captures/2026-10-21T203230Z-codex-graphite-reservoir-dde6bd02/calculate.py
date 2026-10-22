from pathlib import Path
import json,hashlib,numpy as np
from scipy.integrate import solve_ivp
p=Path(__file__).resolve().parent;f=json.loads((p/'FREEZE.json').read_text());src=p.parent/f['input'];assert hashlib.sha256(src.read_bytes()).hexdigest()==f['input_sha256'];d=np.load(src);rows=[]
for key in sorted(x[:-2] for x in d.files if x.endswith('_A')):
 A=d[key+'_A'];a=d[key+'_a'];k=float(d[key+'_k']);om=np.sqrt(k);X=np.cos(np.arange(1,len(a)+1));X/=np.linalg.norm(X);c=float(a@X)
 for gr in f['gamma_over_sqrt_k']:
  gamma=gr*om
  for nr in f['nu_over_sqrt_k']:
   nu=nr*om;period=2*np.pi/nu;zh=-c/complex(k-nu*nu,gamma*nu);z0=zh.real;v0=(1j*nu*zh).real
   def state_energy(t,z,v):
    x=X*np.cos(nu*t);vx=-nu*X*np.sin(nu*t)
    return .5*(vx@vx+v*v+x@A@x+2*z*(a@x)+k*z*z)
   def fun(t,y):
    z,v=y[:2];x=X*np.cos(nu*t);vx=-nu*X*np.sin(nu*t);force=(A-nu*nu*np.eye(len(a)))@x+a*z
    return [v,-gamma*v-k*z-c*np.cos(nu*t),float(force@vx),gamma*v*v]
   sol=solve_ivp(fun,(0,period),[z0,v0,0,0],method='DOP853',rtol=2e-12,atol=2e-13,dense_output=True)
   assert sol.success;zf,vf,W,Q=sol.y[:,-1];power=.5*gamma*nu*nu*abs(zh)**2;expected=power*period;E0=state_energy(0,z0,v0);Et=state_energy(period,zf,vf)
   errs={'work_prediction':float(abs(W-expected)/max(1,abs(expected))), 'export_prediction':float(abs(Q-expected)/max(1,abs(expected))), 'cycle_energy_balance':float(abs(Et-E0-W+Q)/max(1,abs(E0),abs(W),abs(Q))), 'state_return':float(np.linalg.norm([zf-z0,vf-v0])/max(1,np.linalg.norm([z0,v0])))}
   ts=np.linspace(0,period,101);ys=sol.sol(ts);balances=[abs(state_energy(t,y[0],y[1])-E0-y[2]+y[3]) for t,y in zip(ts,ys.T)];errs['path_energy_balance']=float(max(balances)/max(1,abs(E0),abs(W),abs(Q)))
   row={'configuration':key,'gamma_ratio':gr,'frequency_ratio':nr,'overlap':c,'mean_power_model_units':float(power),'drive_work':float(W),'export':float(Q),'errors':errs,'pass':bool(max(errs.values())<f['tolerance'] and (gamma==0 or power>0))};rows.append(row)
r={'status':'PASS' if all(x['pass'] for x in rows) else 'FAIL','configurations':36,'controls':len(rows),'maximum_errors':{e:max(x['errors'][e] for x in rows) for e in rows[0]['errors']},'lossless_max_abs_cycle_work':max(abs(x['drive_work']) for x in rows if x['gamma_ratio']==0),'positive_loss_controls':sum(x['gamma_ratio']>0 and x['mean_power_model_units']>0 for x in rows),'rows':rows,'physical_promotion':0,'native_bath':'HOLD'}
(p/'RESULTS.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k!='rows'},indent=2))
