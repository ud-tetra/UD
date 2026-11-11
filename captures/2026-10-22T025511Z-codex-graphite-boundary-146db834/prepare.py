from pathlib import Path
import json,hashlib,datetime,numpy as np
from common import ROOT,load,positions,directions
p=Path(__file__).resolve().parent;old=json.loads((ROOT/'graphite-free-sliding/FREEZE.json').read_text());cases=['21_dir_0','21_dir_10024'];steps=np.array([2e-5,1e-5,5e-6]);radii=np.array([4e-5,2e-5,1e-5,5e-6]);f={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'main_observed':old['main_observed'],'cases':cases,'steps_A':steps.tolist(),'sample_radii_A':radii.tolist(),'physical_promotion':0,'lane':'Development — no registry entry','scope':'New boundary-aware qualification of two unchanged released stationary references.81 coordinates+9 directions per case. Source-conditioned numerical protocol, not blind physical preregistration.','boundary_rule':'Any triple may cross the source-verified C2 join at-.5; no sampled crossing at other gC knots. This broadens geometric eligibility only, with all derivative thresholds unchanged.17 rounded-position samples across each largest stencil; nearest-neighbor bonds<1.7A. No interval proof or every-potential-branch certificate.','estimator':'Qplus=(-3F0+4F(h)-F(2h))/(-2h); Qminus=(3F0-4F(-h)+F(-2h))/(-2h). Retain mean(Qplus,Qminus) at h=1e-5. Three fixed h; no response-adaptive fallback.','thresholds':{'absolute':1e-6,'relative':1e-5,'antisymmetry_relative':1e-6,'stationarity':1e-7,'baseline_repeat':1e-12,'repeat_absolute':1e-7,'input_direction_error':1e-6},'qualification':'Both side estimates at every h must agree abs/relative; both adjacent steps for each side and averaged estimate must agree abs/relative per probe. Full matrix symmetry; all9 directional probes agree with symmetrized middle matrix. Positive stiffness iff lambda_min>max(1e-7,10*max spectral adjacent averaged-matrix discrepancy). Reverse repeat four middle-estimator force samples.','inputs':dict(old['inputs']),'prior_protocol':'graphite-boundary-stencil v0.1 failed geometry and aborted all4 shards before force evaluation. v0.2 broadens eligibility of the already verified C2 join, adds one-sided coordinate-rounding diagnostics; thresholds unchanged. No convergence-order assumption across interior crossings.'}
for c in cases:
 fn=f'graphite-free-sliding/{c}/RELAXED.npz';f['inputs'][fn]=hashlib.sha256((ROOT/fn).read_bytes()).hexdigest()
for fn in ['graphite-free-sliding/common.py','graphite-safe-full/common.py']:
 f['inputs'][fn]=hashlib.sha256((ROOT/fn).read_bytes()).hexdigest()
(p/'FREEZE.json').write_text(json.dumps(f,indent=2)+'\n');rows=[];seal={}
for c in cases:
 o=p/c;o.mkdir();a,B,nei,b=load(c);m=B.shape[-1];V,names=directions(m);V=np.r_[np.eye(m),V];x=a['positions_A'];u=b/np.linalg.norm(b,axis=2)[:,:,None];pairs=[(0,1),(0,2),(1,2)];theta=np.stack([np.sum(u[:,i]*u[:,j],axis=1) for i,j in pairs],axis=1);eligible=abs(theta+.5)<=1e-10;knots=np.array([-.6666666667,-.5,-.3333333333]);branch0=theta[:,:,None]>=knots;metrics=[];safe=[];crosscount=[]
 for w in V:
  disp=np.einsum('nam,m->na',B,w);errors=[]
  for h in radii:
   xp=positions(x,disp,h);xm=positions(x,disp,-h);eff=np.asarray((xp.astype(np.longdouble)-xm.astype(np.longdouble))/(2*np.longdouble(h)),dtype=float);errors.append(np.linalg.norm(eff-disp))
  for h in steps:
   xp=positions(x,disp,h).astype(np.longdouble);x2p=positions(x,disp,2*h).astype(np.longdouble);xm=positions(x,disp,-h).astype(np.longdouble);x2m=positions(x,disp,-2*h).astype(np.longdouble);xx0=x.astype(np.longdouble)
   for eff in [(-3*xx0+4*xp-x2p)/(2*np.longdouble(h)),(3*xx0-4*xm+x2m)/(2*np.longdouble(h))]:errors.append(float(np.linalg.norm(np.asarray(eff,dtype=float)-disp)))
  ok=True;cross=np.zeros(theta.shape,dtype=bool);maxbond=0.
  for t in np.linspace(-1,1,17):
   xx=positions(x,disp,t*radii[0]);bb=b+(xx-x)[nei]-(xx-x)[:,None,:];lens=np.linalg.norm(bb,axis=2);maxbond=max(maxbond,float(lens.max()));uu=bb/lens[:,:,None];th=np.stack([np.sum(uu[:,i]*uu[:,j],axis=1) for i,j in pairs],axis=1);changed=(th[:,:,None]>=knots)!=branch0;ok=bool(ok and not np.any(changed[:,:,[0,2]]) );cross|=changed[:,:,1]
  metrics.append(errors);safe.append(ok and maxbond<1.7);crosscount.append(int(cross.sum()))
 metrics=np.array(metrics);safe=np.array(safe);ok=bool(safe.all() and metrics.max()<=1e-6 and np.max(abs(a['projected_force']))<=1e-7);np.savez_compressed(o/'PLAN.npz',vectors=V,radii_A=radii,input_errors=metrics,branch_safe=safe,allowed_boundary_triples=eligible,crossed_triples_count=crosscount)
 row=dict(case=c,preflight_pass=ok,probes=len(V),boundary_triples=int(eligible.sum()),max_input_error=float(metrics.max()),max_crossed_triples=max(crosscount));rows.append(row);seal[c+'/PLAN.npz']=hashlib.sha256((o/'PLAN.npz').read_bytes()).hexdigest();print(row)
(p/'FEASIBILITY.json').write_text(json.dumps({'all_pass':all(r['preflight_pass'] for r in rows),'cases':rows},indent=2)+'\n');seal['FEASIBILITY.json']=hashlib.sha256((p/'FEASIBILITY.json').read_bytes()).hexdigest();(p/'PRECHECK_SEAL.json').write_text(json.dumps({'files':seal},indent=2)+'\n')
