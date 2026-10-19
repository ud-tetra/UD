"""Select valid fine/inherited bounds and update the static/low-frequency certificate."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import json,hashlib,argparse

def sqrtup(x):
 assert x>=0
 s=10**18;n=isqrt(x.numerator*s*s//x.denominator)
 if F(n*n,s*s)<x:n+=1
 return F(n,s)
def main(folder):
 out=Path(folder);solve_raw=(out/'SOLVE_RESULTS.json').read_bytes();fraw=(out/'LINEAR_FLUX_RESULTS.json').read_bytes();oldraw=(out/'INHERITED_CONTINUUM.json').read_bytes();s=json.loads(solve_raw);f=json.loads(fraw);old=json.loads(oldraw)
 assert f['source_solve_sha256']==old['source_solve_sha256']==hashlib.sha256(solve_raw).hexdigest()
 assert f['source_state_sha256']==hashlib.sha256((out/'STATE_WITNESS.json').read_bytes()).hexdigest()
 records=[]
 for a,b,c in zip(s['records'],f['records'],old['records']):
  assert a['omega']==b['omega']==c['omega'] and a['gamma']==b['gamma']==c['gamma'];new=F(b['reported_corrected_continuum_radius']);previous=F(c['reported_corrected_continuum_radius']);best=min(new,previous)
  raw=F(b['corrected_continuum_radius'])+sqrtup((F(a['corrected_output_real'])-F(a['raw_output_real']))**2+(F(a['corrected_output_imag'])-F(a['raw_output_imag']))**2)+F(a['reported_raw_evaluation_bound'])
  records.append({'omega':a['omega'],'gamma':a['gamma'],'new_flux_radius':str(new),'inherited_radius':str(previous),'selected_reported_corrected_radius':str(best),'selected_reported_raw_radius':str(min(raw,F(c['reported_raw_continuum_radius']))),'selected_method':'new fine flux' if new<=previous else 'inherited continuum enclosure','precision_target':'1/10','precision_passed':best<=F(1,10)})
 j0=F(s['records'][0]['corrected_output_real']);assert s['records'][0]['static_real_state_verified'];lo=F(old['static_bracket']['lower']);exact_upper=min(F(old['static_bracket']['upper']),j0+F(f['records'][0]['flux_estimator_squared']));scale=10**6;hi=F(-((-exact_upper*scale).numerator//(-exact_upper*scale).denominator),scale);assert j0<=hi<=F(old['static_bracket']['upper'])
 center=(lo+hi)/2;rad=(hi-lo)/2;ff=float(center);ev=abs(F.from_float(ff)-center);margin=F(1,10)-rad-ev
 def test(d):return d<2 and hi*hi*d*d*(d*d+4)<=margin*margin*(4-d*d)**2
 a,b=0,1999999
 while b-a>1:
  k=(a+b)//2
  if test(F(k,scale)):a=k
  else:b=k
 d=F(a,scale);radius=rad+hi*sqrtup(d*d*(d*d+4))/(4-d*d)+ev;assert test(d) and not test(F(b,scale)) and radius<=F(1,10)
 result={'status':'PASS','classification':'CONDITIONAL_FINE_FLUX_CERTIFICATES_RESONANCE_PRECISION_OPEN','source_flux_sha256':hashlib.sha256(fraw).hexdigest(),'source_inherited_sha256':hashlib.sha256(oldraw).hexdigest(),'records':records,'static_bracket':{'lower':str(lo),'upper':str(hi)},'uniform_low_frequency_strip':{'abs_omega_upper':str(d),'gamma_lower':'1/10','gamma_upper':'1','exact_proxy':str(center),'reported_proxy_hex':ff.hex(),'proxy_evaluation_bound':str(ev),'reported_output_radius':str(radius),'target':'1/10','next_microstep_fails_sufficient_test':True},'dynamic_precision_passed':all(x['precision_passed'] for x in records[1:]),'full_band_precision_certified':False,'independent_review':False,'physical_promotion':0}
 target=out/'LINEAR_SUMMARY_RESULTS.json'
 if target.exists():assert json.loads(target.read_text())==result;print('read-only replay matches LINEAR_SUMMARY_RESULTS.json')
 else:target.write_text(json.dumps(result,indent=2)+'\n')
 print('static',lo,hi,'uniform strip',d,'proxy',center)
 for r in records:print('omega',r['omega'],'best radius',float(F(r['selected_reported_corrected_radius'])),r['selected_method'],'precision',r['precision_passed'])
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('output');main(a.parse_args().output)
