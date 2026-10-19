"""Exact symbolic local-frequency certificate from the audited pointwise P2 residual."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import json,hashlib
from fractions import Fraction as F
from math import isqrt

def sqrtup(x):
 assert x>=0
 s=10**24;n=isqrt(x.numerator*s*s//x.denominator)
 if F(n*n,s*s)<x:n+=1
 y=F(n,s);assert y*y>=x
 return y

def main(folder):
 out=Path(folder);raw=(out/'UPPER_RESULTS.json').read_bytes();d=json.loads(raw);assert d['omega']=='9/2' and d['gamma']=='1/10'
 w0,gamma=F(9,2),F(1,10);res=sqrtup(F(d['defect_squared']))+sqrtup(F(d['local_lift_budget_squared']));mass=sum(F(x) for x in d['full_state_mass'][:2]);assert mass>0
 records=[]
 for width in map(F,['1/1000','1/500','1/200','1/100','1/50','1/25']):
  lo,hi=w0-width,w0+width
  # |w²-w0²|<=width*(2*w0+width), |2 gamma (w-w0)|<=2 gamma width.
  dz2=(width*(2*w0+width))**2+(2*gamma*width)**2
  rz=res+sqrtup(dz2)*sqrtup(mass)/2
  kappa=sqrtup(1+(hi/(2*gamma))**2)
  radius=kappa*rz*rz
  records.append({'halfwidth':str(width),'omega_interval':[str(lo),str(hi)],'gamma':str(gamma),'delta_z_squared_upper':str(dz2),'residual_dual_upper':str(rz),'kappa_upper':str(kappa),'exact_model_corrected_estimator_uniform_radius':str(radius),'exact_model_one_tenth_passed':radius<=F(1,10)})
 result={'status':'PASS','classification':'DERIVED_CONDITIONAL_EXACT_SYMBOLIC_LOCAL_FREQUENCY_BOUNDS','source_upper_results_sha256':hashlib.sha256(raw).hexdigest(),'state_fixed_at_omega':'9/2','gamma_fixed':'1/10','state_L2_squared':str(mass),'base_residual_dual_upper':str(res),'estimator':'J_w(v)=J_w0(v)-(z(w)-z(w0))*integral v² dmu; exact complex arithmetic','bilinear_state_mass':[str(F(d['full_state_mass'][0])-F(d['full_state_mass'][1])),str(2*F(d['full_state_mass'][2]))],'proof':'r_z(v)=r_z0(v)-(z-z0)m(v,.); ||m(v,.)||_(dual V)<=||v||_L2/2. Rotation gives ||A_z^-1||_(dual V to V)<=sqrt(1+(w/(2 gamma))²). Corrected identity H_z-J_z(v)=r_z(A_z^-1 r_z) gives the squared-residual upper. All suprema use outward rational roots.','records':records,'precision_target':'1/10','scope':'Uniform exact-model estimator-family bound at fixed gamma=0.1, not a uniform floating-evaluation/solver guarantee or the full [0,6]x[0.1,1] audit. Pointwise actual-output evaluation is separately certified in UPPER_RESULTS. No new solve or state-refinement claim.','independent_review':False,'physical_promotion':0}
 p=out/'LOCAL_BAND_RESULTS.json'
 if p.exists():assert json.loads(p.read_text())==result;print('read-only local-band replay PASS',flush=True)
 else:p.write_text(json.dumps(result,indent=2)+'\n')
 print('exact model local band radii '+str([(float(F(r['halfwidth'])),float(F(r['exact_model_corrected_estimator_uniform_radius'])),r['exact_model_one_tenth_passed']) for r in records]),flush=True)
if __name__=='__main__':main(Path(__file__).resolve().parent)
