"""Exact outer polygons for continuum moment/passivity disks and a frozen output test."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json,argparse,hashlib
TOL=F(1,10);EVAL_ALLOWANCE=F(1,10**10)
def validate_sqrt(x,y):
 assert x>=0 and y>=0 and y*y>=x,'inward square-root bound'
 return y
def accepts(radius,target=TOL):
 assert radius>=0 and target>=0
 return radius<=target
def sqrtup(x):
 assert x>=0
 scale=10**18;n=isqrt(x.numerator*scale*scale//x.denominator)
 if F(n*n,scale*scale)<x:n+=1
 y=F(n,scale);return validate_sqrt(x,y)

def disks(om,ga,S):
 t=om*om;b=2*ga*om;m=F(20);M=F(400);assert b>0 and S*M>m*m
 out=[('source_mass',F(0),-m/(2*b),m*m/(4*b*b)),('static_energy',S/2,-S*t/(2*b),S*S*(1+t*t/(b*b))/4)]
 L=F(4);A=M-L*m;d=(t-L)**2+b*b;cx=(A-2*m*(t-L))/(2*d);cy=-(2*m*b+A*(t-L)/b)/(2*d)
 out.append(('source_gap_moment',cx,cy,cx*cx+cy*cy-m*m/d))
 Delta=S*M-m*m;C=M-2*m*t+S*(t*t+b*b);assert C>0
 cx=(Delta+2*m*m-2*S*m*t)/(2*C);cy=-(2*S*m*b+Delta*t/b)/(2*C)
 out.append(('joint_gram',cx,cy,cx*cx+cy*cy-S*m*m/C))
 assert all(r>=0 for name,x,y,r in out)
 return out

def clip(poly,nx,ny,c):
 if not poly:return []
 result=[]
 for a,b in zip(poly,poly[1:]+poly[:1]):
  fa=nx*a[0]+ny*a[1]-c;fb=nx*b[0]+ny*b[1]-c;ia=fa<=0;ib=fb<=0
  if ia:result.append(a)
  if ia!=ib:
   s=fa/(fa-fb);result.append((a[0]+s*(b[0]-a[0]),a[1]+s*(b[1]-a[1])))
 # Exact duplicate removal; no floating angular sort or tolerance.
 cleaned=[]
 for p in result:
  if not cleaned or p!=cleaned[-1]:cleaned.append(p)
 if len(cleaned)>1 and cleaned[0]==cleaned[-1]:cleaned.pop()
 return cleaned

def normals():
 out=[]
 for x,y in [(1,0),(4,1),(2,1),(4,3),(1,1),(3,4),(1,2),(1,4)]:
  for _ in range(4):out.append((x,y));x,y=-y,x
 assert len(set(out))==32
 return out

def check_fixture(rec,S):
 om=F(rec['omega']);ga=F(rec['gamma']);cx=F(rec['corrected_output_real']);cy=F(rec['corrected_output_imag']);old=F(rec['corrected_continuum_error_bound']);ev=F(rec['reported_corrected_evaluation_error_bound']);eta2=F(rec['flux_estimator_squared']);kap=F(rec['spectral_factor_upper'])
 assert ev<=EVAL_ALLOWANCE and old==kap*eta2
 if om==0:
  bracket=rec['static_continuum_bracket'];poly=[(F(bracket['lower']),F(0)),(F(bracket['upper']),F(0))];dc=[];planes=[]
 else:
  dc=disks(abs(om),ga,S)
  if om<0:dc=[(name,x,-y,r) for name,x,y,r in dc]
  dc.append(('posterior_flux',cx,cy,old*old));m=F(20);b=2*ga*abs(om);R=m/(2*b);Y=-R if om>0 else R
  poly=[(-R,Y-R),(R,Y-R),(R,Y+R),(-R,Y+R)];planes=[]
  for name,x,y,r2 in dc:
   for nx,ny in normals():
    upper=nx*x+ny*y+sqrtup(r2*(nx*nx+ny*ny));planes.append((F(nx),F(ny),upper));poly=clip(poly,F(nx),F(ny),upper)
  # lambda>=4 and passive sign; these do not assume a discrete spectral gap.
  q=(om*om-4)/(2*ga*om);planes.extend([(-F(1),q,F(0)),(F(0),F(1 if om>0 else -1),F(0))])
  for nx,ny,c in planes[-2:]:poly=clip(poly,nx,ny,c)
  assert len(poly)>=3,'empty necessary-condition enclosure'
  assert all(nx*x+ny*y<=c for x,y in poly for nx,ny,c in planes)
 distance2=max((x-cx)**2+(y-cy)**2 for x,y in poly);radius=sqrtup(distance2);final=min(old,radius)+ev
 raw_offset=F(rec['raw_continuum_error_bound'])-old;assert raw_offset>=0
 raw_radius=min(old,radius)+raw_offset
 threshold=(TOL-ev)/kap
 return {'omega':str(om),'gamma':str(ga),'old_reported_output_radius':str(old+ev),'moment_polygon_radius_about_exact_corrected_output':str(radius),'certified_reported_output_radius':str(final),'reported_raw_output_radius':str(raw_radius),'raw_output_test_passed':accepts(raw_radius),'relative_to':'reported corrected output; evaluation bound added once','improved_or_equal':final<=old+ev,'absolute_tolerance':str(TOL),'pointwise_output_test_passed':accepts(final),'pointwise_flux_threshold_eta_squared':str(threshold),'pointwise_flux_test_passed':eta2<=threshold,'polygon_vertices':[[str(x),str(y)] for x,y in poly],'disk_parameters':[{'name':name,'center_real':str(x),'center_imag':str(y),'radius_squared':str(r)} for name,x,y,r in dc],'rational_halfplanes_checked':len(planes)}

def controls(S):
 records=[]
 # Exact two-atom spectral measure: mass20, energy400, inverse moment25/21<=S.
 assert F(25,21)<=S
 for om in [F(4),F(9,2),F(5)]:
  t=om*om;b=om/5;x=sum(F(10)*(lam-t)/((lam-t)**2+b*b) for lam in [F(12),F(28)]);y=-sum(F(10)*b/((lam-t)**2+b*b) for lam in [F(12),F(28)])
  for name,cx,cy,r in disks(om,F(1,10),S):assert (x-cx)**2+(y-cy)**2<=r
  records.append({'omega':str(om),'two_atom_measure_inside_all_disks':True})
 # Upward imaginary transfer is rejected by the passive source-mass disk.
 name,cx,cy,r=disks(F(4),F(1,10),S)[0];assert (0-cx)**2+(1-cy)**2>r
 try:validate_sqrt(F(2),F(1))
 except AssertionError:pass
 else:raise AssertionError('inward square-root proposal accepted')
 assert not accepts(F(25)) and accepts(TOL) and not accepts(TOL+F(1,10**18)), 'precision gate boundary error'
 return {'spectral_controls':records,'expected_rejections':['active upper-half-plane transfer','inward sqrt proposal','25-unit envelope at1/10 precision gate']}

def main(folder):
 out=Path(folder);raw=(out/'INPUT_RESULTS.json').read_bytes();source=json.loads(raw)
 assert source['status']=='PASS' and source['physical_promotion']==0
 br=source['records'][0]['static_continuum_bracket'];S=F(br['upper']);records=[check_fixture(r,S) for r in source['records']]
 conjugate_checks=[]
 for rec,record in zip(source['records'],records):
  if F(rec['omega'])==0:continue
  mirrored=rec.copy();mirrored['omega']=str(-F(rec['omega']));mirrored['corrected_output_imag']=str(-F(rec['corrected_output_imag']));other=check_fixture(mirrored,S)
  assert other['certified_reported_output_radius']==record['certified_reported_output_radius']
  conjugate_checks.append({'omega':record['omega'],'negative_frequency_radius_matches':True})
 result={'status':'PASS','conjugate_checks':conjugate_checks,'classification':'CONDITIONAL_CONTINUUM_MOMENT_POLYGON_AND_FROZEN_OUTPUT_GATE','input_sha256':hashlib.sha256(raw).hexdigest(),'fixed_source_mass':20,'fixed_source_energy':400,'continuum_lambda_lower':4,'static_upper':str(S),'absolute_output_target':str(TOL),'evaluation_allowance':str(EVAL_ALLOWANCE),'band_kappa_upper':str(sqrtup(F(901))),'uniform_sufficient_eta_squared':str((TOL-EVAL_ALLOWANCE)/sqrtup(F(901))),'band_test_passed':False,'band_test_scope':'Four points only. The uniform sufficient condition requires coverage of the entire declared band, not four sampled certificates. No termination guarantee.','records':records,'controls':controls(S),'independent_review':False,'physical_promotion':0}
 target=out/'RESULTS.json'
 if target.exists():assert json.loads(target.read_text())==result;print('read-only replay matches RESULTS.json')
 else:target.write_text(json.dumps(result,indent=2)+'\n')
 for r in records:print('omega',r['omega'],'radius',float(F(r['certified_reported_output_radius'])),'precision gate',r['pointwise_output_test_passed'])
 print('PASS exact disk/polygon checks; precision target unmet at dynamic samples')
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('output');args=a.parse_args();main(args.output)
