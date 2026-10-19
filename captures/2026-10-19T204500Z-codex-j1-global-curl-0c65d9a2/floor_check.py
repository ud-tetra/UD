"""Exact obstruction for phase-circle precision using any piecewise constant correction."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import json,hashlib,argparse
from curl_circle import params

def main(folder):
 p=Path(folder);raw=(p/'CONSTANT_FLOOR_RESULTS.json').read_bytes();floor=json.loads(raw);old=json.loads((p/'FLUX_RESULTS.json').read_text());cov=json.loads((p/'CURL_COVARIANCE_RESULTS.json').read_text());records=[]
 assert floor['source_flux_witness_sha256']==hashlib.sha256((p/'FLUX_WITNESS.json').read_bytes()).hexdigest()
 assert floor['source_flux_results_sha256']==hashlib.sha256((p/'FLUX_RESULTS.json').read_bytes()).hexdigest()
 assert len(floor['records'])==len(old['records'])==len(cov['records'])==4
 for f,o,v in zip(floor['records'],old['records'],cov['records']):
  assert f['omega']==o['omega']==v['omega'] and f['gamma']==o['gamma']==v['gamma']
  low=F(f['constant_correction_eta_squared_floor']);assert low==F(o['flux_norm_squared'])-F(f['cell_mean_flux_norm_squared']) and 0<=low<=F(v['eta_squared'])
  _,d2=params(F(f['omega']),F(f['gamma']));s=10**18;r=isqrt(d2.numerator*s*s//d2.denominator);rlo=F(r,s)*low;assert rlo*rlo<=d2*low*low
  records.append({'omega':f['omega'],'gamma':f['gamma'],'eta_squared_floor':str(low),'phase_circle_radius_lower':str(rlo),'constant_only_circle_precision_obstruction':d2*low*low>F(1,100)})
 result={'status':'PASS','source_floor_sha256':hashlib.sha256(raw).hexdigest(),'scope':'Fixed frozen RT1 flux plus arbitrary piecewise constant cell corrections. Obstruction applies only to the phase-circle delta*eta² certificate at the listed points. It does not lower-bound actual transfer error or rule out another certificate/nonconstant corrections.','records':records,'independent_review':False,'physical_promotion':0}
 t=p/'FLOOR_CHECK_RESULTS.json'
 if t.exists():assert json.loads(t.read_text())==result;print('read-only replay matches FLOOR_CHECK_RESULTS.json')
 else:t.write_text(json.dumps(result,indent=2)+'\n')
 for x in records:print('omega',x['omega'],'eta floor',float(F(x['eta_squared_floor'])),'circle radius floor',float(F(x['phase_circle_radius_lower'])),'constant-only obstruction',x['constant_only_circle_precision_obstruction'])
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('folder');main(a.parse_args().folder)
