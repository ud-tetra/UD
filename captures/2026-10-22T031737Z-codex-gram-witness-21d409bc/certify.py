from fractions import Fraction as F
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent;c=json.loads((P/'CONTRACT.json').read_text());modes=list(range(100,200));K=len(modes);T0=F(1);rho=F(c['relative_interval_error']);eta=F(c['per_mode_frequency_error_Hz']);cap=F(1,1000);C=F(211,20)
def gram_lower(e,r):
 sums=[]
 for n in modes:
  row=F(0)
  for m in modes:
   if m==n:continue
   d=abs(n-m);q=d*r+2*e*T0*(1+r)
   if q>=d:return None
   row+=q/(d-q)
  sums.append(row)
 return 1-max(sums)
def evaluate(e,r,rms,outside):
 lam=gram_lower(e,r)
 if lam is None:return {'status':'HOLD','reason':'frequency uncertainty permits pair collision'}
 if lam<F(9,10):return {'status':'HOLD','reason':'selected lambda floor not certified','lambda_lower':str(lam)}
 assert C*C*lam>=K
 tail=C*(rms+F(1,50000))+outside
 return {'status':'PASS_CONDITIONAL' if tail<=cap else 'HOLD','reason':'tail ceiling' if tail>cap else 'joint lambda and tail sufficient gates','lambda_lower':str(lam),'tail_upper_V':str(tail)}
lam=gram_lower(eta,rho);assert lam>=F(9,10);assert C*C*F(9,10)>=K
rms=F(c['monitor_RMS_V']);out=F(c['outside_model_TV_V']);positive=evaluate(eta,rho,rms,out);assert positive['status']=='PASS_CONDITIONAL'
checks=[('nominal_orthogonality',gram_lower(F(0),F(0))==1),('prior_60uV',evaluate(eta,rho,F(3,50000),out)['status']=='HOLD'),('50mHz',evaluate(F(1,20),rho,rms,out)['status']=='HOLD'),('500mHz_collision',evaluate(F(1,2),rho,rms,out)['status']=='HOLD'),('outside_300uV',evaluate(eta,rho,rms,F(3,10000))['status']=='HOLD')]
assert all(v for _,v in checks)
# Actual distinct-tone counterexample to an orthogonal RMS-to-TV inference with no separation premise.
delta=F(1,10**6);near_rms_upper=F(22,7)*delta;assert near_rms_upper<F(1,100000) and 2>1000*near_rms_upper
# Reconstruct the prior full-state leakage budget with the new certified tail ceiling.
root=P.parents[1];bpath=root/'captures/2026-10-21T190100Z-codex-leakage-budget-094a0b3c/CERTIFICATE.json';b=json.loads(bpath.read_text());H=F(b['inherited_rounded_upper']['H0']['fraction']);fixed=F(b['fixed_error_V']['fraction']);tail=F(positive['tail_upper_V']);error=fixed+(H+1)*tail+H/F(4000);phase=F(200,99)*error;assert error<F(99,10000) and phase<F(1,50)
def datum(q):return {'fraction':str(q),'approximation':float(q)}
result={'status':'PASS_EXACT_CONDITIONAL_GRAM_WITNESS','physical_promotion':0,'contract_sha256':hashlib.sha256((P/'CONTRACT.json').read_bytes()).hexdigest(),'base_certificate_sha256':hashlib.sha256(bpath.read_bytes()).hexdigest(),'mode_count':K,'lambda_lower':datum(lam),'chosen_lambda_floor':'9/10','chosen_norm_factor':'211/20','tail_upper_V':datum(tail),'full_state_error_upper_V':datum(error),'phase_upper_rad':datum(phase),'positive':positive,'controls':[{'case':n,'pass':v} for n,v in checks],'negative_details':{'prior60uV':evaluate(eta,rho,F(3,50000),out),'50mHz':evaluate(F(1,20),rho,rms,out),'500mHz':evaluate(F(1,2),rho,rms,out),'outside300uV':evaluate(eta,rho,rms,F(3,10000))},'near_collision':{'distinct_frequency_separation_Hz':str(delta),'coefficient_magnitudes':['1','1'],'actual_tail_TV_V':'2','normalized_complex_RMS_upper_V':str(near_rms_upper),'scope':'Centered one-second interval; two distinct tones with opposite coefficients. This is an actual source counterexample, not a failed sufficient bound.'},'limitations':'Bounds on frequency, duration, monitor L2 error, completeness and outside-mode variation remain unmeasured; no empirical admission.'}
(P/'CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:(v['approximation'] if isinstance(v,dict) and 'approximation' in v else v) for k,v in result.items() if k in ['status','lambda_lower','tail_upper_V','full_state_error_upper_V','phase_upper_rad']}))
# Optional diagnostic only. NumPy values are not used in exact acceptance.
try:
 import numpy as np
 cases=[]
 for name,offsets in [('alternating',np.array([float(eta)*(-1)**j for j in range(K)])),('ramp',np.linspace(-float(eta),float(eta),K))]:
  f=np.array(modes)+offsets;d=f[:,None]-f[None,:];G=np.sinc(d*(1+float(rho)));actual=float(np.linalg.eigvalsh(G)[0]);assert actual+1e-10>=float(lam);cases.append({'case':name,'minimum_eigenvalue':actual})
 (P/'NUMERICAL_DIAGNOSTICS.json').write_text(json.dumps({'scope':'Two synthetic constant-offset patterns; not proof for uncertainty family','cases':cases,'acceptance_uses_numpy':False},indent=2)+'\n')
except ImportError:
 (P/'NUMERICAL_DIAGNOSTICS.json').write_text(json.dumps({'status':'SKIPPED_NUMPY_UNAVAILABLE','exact_certificate_unaffected':True},indent=2)+'\n')
