"""Refined static lower bound and honest recentering of inherited continuum enclosures."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json,hashlib,argparse
TOL=F(1,10)
def sqrtup(x):
 assert x>=0
 nscale=10**18;n=isqrt(x.numerator*nscale*nscale//x.denominator)
 if F(n*n,nscale*nscale)<x:n+=1
 return F(n,nscale)
def main(folder):
 out=Path(folder);newraw=(out/'SOLVE_RESULTS.json').read_bytes();new=json.loads(newraw);oldraw=(out/'OLD_SOLVES.json').read_bytes();old=json.loads(oldraw);encraw=(out/'OLD_ENCLOSURES.json').read_bytes();enc=json.loads(encraw)
 assert new['status']==old['status']==enc['status']=='PASS' and enc['input_sha256']==hashlib.sha256(oldraw).hexdigest()
 assert new['records'][0]['static_real_state_verified'] is True
 hi=F(old['records'][0]['static_continuum_bracket']['upper']);j0=F(new['records'][0]['corrected_output_real']);assert F(new['records'][0]['corrected_output_imag'])==0 and j0<=hi
 grid=10**6;lo=F((j0*grid).numerator//(j0*grid).denominator,grid);assert lo>=F(old['records'][0]['static_continuum_bracket']['lower'])
 center=(lo+hi)/2;rad=(hi-lo)/2;fr=float(center);ev=abs(F.from_float(fr)-center)
 def passes(d):return d<2 and hi*hi*d*d*(d*d+4)<=(TOL-rad-ev)**2*(4-d*d)**2
 a,b=0,1999999
 while b-a>1:
  k=(a+b)//2
  if passes(F(k,grid)):a=k
  else:b=k
 delta=F(a,grid);bound=rad+hi*sqrtup(delta*delta*(delta*delta+4))/(4-delta*delta)+ev
 assert passes(delta) and not passes(F(b,grid)) and bound<=TOL
 records=[]
 for n,o,e in zip(new['records'],old['records'],enc['records']):
  assert n['omega']==o['omega']==e['omega'] and n['gamma']==o['gamma']==e['gamma']
  jr,ji=F(n['corrected_output_real']),F(n['corrected_output_imag']);nr=sqrtup((jr-F(o['corrected_output_real']))**2+(ji-F(o['corrected_output_imag']))**2)
  old_ref_radius=F(e['certified_reported_output_radius'])-F(o['reported_corrected_evaluation_error_bound'])
  if F(n['omega'])==0:ref_radius=hi-jr;method='new real energy lower bound plus inherited upper'
  else:
   polygon_radius=sqrtup(max((F(p[0])-jr)**2+(F(p[1])-ji)**2 for p in e['polygon_vertices']));ref_radius=min(old_ref_radius+nr,polygon_radius);method='inherited polygon/triangle recentered; no new flux certificate'
  rr=ref_radius+F(n['reported_corrected_evaluation_bound']);rawr=ref_radius+sqrtup((jr-F(n['raw_output_real']))**2+(ji-F(n['raw_output_imag']))**2)+F(n['reported_raw_evaluation_bound']);records.append({'omega':n['omega'],'gamma':n['gamma'],'corrected_reference_real':str(jr),'corrected_reference_imag':str(ji),'change_from128_cell_corrected_output_upper':str(nr),'reported_corrected_continuum_radius':str(rr),'reported_raw_continuum_radius':str(rawr),'precision_target':str(TOL),'precision_passed':rr<=TOL,'method':method})
 result={'status':'PASS','classification':'CONDITIONAL_REFINED_STATIC_CERTIFICATE_DYNAMIC_CONTINUUM_ACCURACY_OPEN','source_solve_sha256':hashlib.sha256(newraw).hexdigest(),'old_solve_sha256':hashlib.sha256(oldraw).hexdigest(),'old_enclosure_sha256':hashlib.sha256(encraw).hexdigest(),'static_bracket':{'lower':str(lo),'upper':str(hi)},'uniform_gamma1_10_to1_strip':{'absolute_omega_upper':str(delta),'exact_proxy':str(center),'reported_proxy_real_hex':fr.hex(),'proxy_evaluation_error':str(ev),'reported_error_bound':str(bound),'precision_target':str(TOL),'next_microstep_fails_sufficient_bound':True},'records':records,'new_dynamic_flux_certificate':False,'independent_review':False,'physical_promotion':0}
 p=out/'CONTINUUM_RESULTS.json'
 if p.exists():assert json.loads(p.read_text())==result;print('read-only replay matches CONTINUUM_RESULTS.json')
 else:p.write_text(json.dumps(result,indent=2)+'\n')
 print('static bracket',lo,hi,'uniform low strip',delta,'radius',float(bound))
 for r in records:print('omega',r['omega'],'continuum radius',float(F(r['reported_corrected_continuum_radius'])),'precision',r['precision_passed'])
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('output');main(a.parse_args().output)
