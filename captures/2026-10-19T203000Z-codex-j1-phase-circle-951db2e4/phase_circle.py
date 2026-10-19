"""Exact phase-aware output disks and rational intersections for frozen J1 flux moments."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json,hashlib,argparse

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def norm2(x):return x[0]*x[0]+x[1]*x[1]
def sqrtup(x):
 assert x>=0
 scale=10**18;n=isqrt(x.numerator*scale*scale//x.denominator)
 if F(n*n,scale*scale)<x:n+=1
 return validate_sqrt(x,F(n,scale))
def validate_sqrt(x,y):
 assert x>=0 and y>=0 and y*y>=x,'inward square-root proposal'
 return y
def validate_cov(dr,di,dc):
 assert dr>=0 and di>=0 and dr*di>=dc*dc,'indefinite flux covariance'
def params(om,ga):
 assert ga>0
 if om==0:return (F(1,2),F(0)),F(1,4)
 a=om*om;b=2*ga*om;c=(F(1,2),-a/(2*b));return c,norm2(c)
def clip(poly,nx,ny,c):
 out=[]
 for p,q in zip(poly,poly[1:]+poly[:1]):
  a=nx*p[0]+ny*p[1]-c;b=nx*q[0]+ny*q[1]-c
  if a<=0:out.append(p)
  if (a<=0)!=(b<=0):
   t=a/(a-b);out.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
 return out
def normals():
 out=[]
 for x,y in [(1,0),(4,1),(2,1),(4,3),(1,1),(3,4),(1,2),(1,4)]:
  for _ in range(4):out.append((F(x),F(y)));x,y=-y,x
 return out

def controls():
 checks=0
 for om in [F(-5),F(-9,2),F(0),F(1,10),F(4),F(9,2),F(5),F(6)]:
  c,r2=params(om,F(1,10));a=om*om;b=om/5
  for lam in [F(4),F(12),F(20),F(28),F(100),F(10**6)]:
   den=(lam-a)**2+b*b;f=(lam*(lam-a)/den,-lam*b/den)
   if om:assert norm2(add(f,(-c[0],-c[1])))==r2
   else:assert norm2(add(f,(-c[0],-c[1])))<=r2
   checks+=1
  # Three gradient modes plus a nonzero solenoidal coordinate.
  ds=[(F(1,3),F(2,5)),(F(-2,7),F(1,4)),(F(3,8),F(-1,6)),(F(2),F(1))]
  q=(F(0),F(0));err=(F(0),F(0));eta=F(0)
  for d,lam in zip(ds,[F(4),F(20),F(100),F(0)]):
   q=add(q,mul(d,d));eta+=norm2(d)
   if lam:
    den=(lam-a)**2+b*b;f=(lam*(lam-a)/den,-lam*b/den);err=add(err,mul(mul(d,d),f))
  offset=mul(c,q);assert norm2(add(err,(-offset[0],-offset[1])))<=r2*eta*eta
 # Wrong rotation sign fails at a resonant scalar mode.
 om=F(4);ga=F(1,10);c,r2=params(om,ga);f=(F(0),-om/(2*ga));wrong=(c[0],-c[1]);assert norm2(add(f,(-wrong[0],-wrong[1])))>r2
 # Dropping the solenoidal norm can make the claimed enclosure false.
 c,r2=params(F(4),F(1,10));q=(F(1),F(0));assert norm2(mul(c,q))>0
 for label,fn in [('inward sqrt',lambda:validate_sqrt(F(2),F(1))),('indefinite covariance',lambda:validate_cov(F(1),F(1),F(2))),('zero damping',lambda:params(F(4),F(0)))]:
  try:fn()
  except AssertionError:pass
  else:raise AssertionError(label+' accepted')
 # Coefficient identity in lambda: b² lambda²+(a²+b²-a lambda)²=(a²+b²)((lambda-a)²+b²).
 for a,b in [(F(16),F(4,5)),(F(81,4),F(9,10)),(F(25),F(1)),(F(36),F(1,5))]:
  A=a*a+b*b;left=[A*A,-2*A*a,a*a+b*b];right=[A*(a*a+b*b),-2*A*a,A];assert left==right
  # At lambda=a, f=-ia/b; f(infinity)=1. Their separation is exactly 2delta.
  c,d2=params(sqrtup(a),b/(2*sqrtup(a)));assert norm2((F(1),a/b))==4*d2
 return {'scalar_spectral_checks':checks,'complex_modal_plus_solenoidal_checks':8,'expected_rejections':['wrong spectral rotation sign at resonance','zero norm budget after dropping nonzero solenoidal coordinate','inward square-root proposal','indefinite flux covariance','zero damping'],'polynomial_coefficient_identities':4,'sharpness_endpoint_identities':4,'physical_promotion':0}

def main(folder):
 p=Path(folder);raw=(p/'COVARIANCE_RESULTS.json').read_bytes();src=json.loads(raw);prior=json.loads((p/'SUMMARY_RESULTS.json').read_text());solve=json.loads((p/'SOLVE_RESULTS.json').read_text());assert src['status']=='PASS';records=[]
 assert src['source_flux_witness_sha256']==hashlib.sha256((p/'FLUX_WITNESS.json').read_bytes()).hexdigest()
 assert src['source_state_sha256']==hashlib.sha256((p/'STATE_WITNESS.json').read_bytes()).hexdigest()
 assert src['source_flux_results_sha256']==hashlib.sha256((p/'FLUX_RESULTS.json').read_bytes()).hexdigest()==prior['source_flux_sha256']
 assert len(src['records'])==len(prior['records'])==len(solve['records'])==4
 for cov,old,s in zip(src['records'],prior['records'],solve['records']):
  om=F(cov['omega']);ga=F(cov['gamma']);c,d2=params(om,ga);eta=F(cov['eta_squared']);q=(F(cov['bilinear_defect_real']),F(cov['bilinear_defect_imag']));J=(F(cov['J_real']),F(cov['J_imag']));assert norm2(q)<=eta*eta
  dr,di,dc=(F(cov[k]) for k in ['d_real_norm_squared','d_imag_norm_squared','d_cross']);validate_cov(dr,di,dc);assert eta==dr+di and q==(dr-di,2*dc)
  assert cov['omega']==old['omega']==s['omega'] and cov['gamma']==old['gamma']==s['gamma']
  assert J==(F(s['corrected_output_real']),F(s['corrected_output_imag']))
  cm,dm=params(-om,ga);assert dm==d2 and cm==(c[0],-c[1]);assert add((J[0],-J[1]),mul(cm,(q[0],-q[1])))==(add(J,mul(c,q))[0],-add(J,mul(c,q))[1])
  center=add(J,mul(c,q));radius=sqrtup(d2)*eta;assert radius*radius>=d2*eta*eta
  reported=tuple(F.from_float(float(x)) for x in center);ev=sqrtup(norm2((reported[0]-center[0],reported[1]-center[1])));total=radius+ev
  # Old bounds are about the old actually reported corrected output.
  of=tuple(F.from_float(float.fromhex(x)) for x in json.loads((p/'STATE_WITNESS.json').read_text())['fixtures'][len(records)]['reported_corrected_hex']);oldradius=F(old['selected_reported_corrected_radius']);r2=radius*radius
  if om:
   # Outer rational polygon contains intersection of both guaranteed disks.
   poly=[(of[0]-oldradius,of[1]-oldradius),(of[0]+oldradius,of[1]-oldradius),(of[0]+oldradius,of[1]+oldradius),(of[0]-oldradius,of[1]+oldradius)]
   planes=[]
   for (cx,cy),rad in [(of,oldradius),(center,radius)]:
    for nx,ny in normals():
     bound=nx*cx+ny*cy+sqrtup(rad*rad*(nx*nx+ny*ny));planes.append((nx,ny,bound));poly=clip(poly,nx,ny,bound)
   assert poly,'incompatible input certificates'
   assert all(nx*x+ny*y<=bound for x,y in poly for nx,ny,bound in planes)
   # Bounding-box midpoint is a rational, reproducible proposal, not an optimum.
   pc=((min(x for x,y in poly)+max(x for x,y in poly))/2,(min(y for x,y in poly)+max(y for x,y in poly))/2);pr=sqrtup(max(norm2((x-pc[0],y-pc[1])) for x,y in poly));pev=tuple(F.from_float(float(x)) for x in pc);pe=sqrtup(norm2((pev[0]-pc[0],pev[1]-pc[1])))
   candidates=[('phase_circle',reported,total),('inherited',of,oldradius),('intersection_polygon',pev,pr+pe)]
   oldcenterbound=min(oldradius,sqrtup(max(norm2((x-of[0],y-of[1])) for x,y in poly)))
  else:
   poly=[];planes=[];candidates=[('phase_circle',reported,total),('inherited',of,oldradius)];oldcenterbound=oldradius
  method,bestcenter,best=min(candidates,key=lambda x:x[2]);records.append({'omega':str(om),'gamma':str(ga),'delta_squared':str(d2),'phase_circle_exact_center':[str(x) for x in center],'phase_circle_exact_center_radius':str(radius),'phase_circle_reported_center_hex':[float(x).hex() for x in reported],'phase_circle_center_evaluation_bound':str(ev),'phase_circle_reported_radius':str(total),'old_reported_center_hex':[float(x).hex() for x in of],'old_reported_radius':str(oldradius),'old_center_intersection_radius':str(oldcenterbound),'selected_method':method,'selected_reported_center_hex':[float(x).hex() for x in bestcenter],'selected_reported_radius':str(best),'selected_precision_passed':best<=F(1,10),'selected_proxy_passive':-om*bestcenter[1]>=0,'pointwise_sufficient_eta_squared_for_one_tenth_less_1e10_eval':str((F(1,10)-F(1,10**10))/sqrtup(d2)),'polygon_vertices':[[str(x),str(y)] for x,y in poly],'halfplanes_checked':len(planes)})
 result={'status':'PASS','classification':'DERIVED_CONDITIONAL_PHASE_AWARE_FLUX_OUTPUT_ENCLOSURES','source_covariance_sha256':hashlib.sha256(raw).hexdigest(),'uniform_band_circle_factor_upper':str(sqrtup(F(901))/2),'uniform_sufficient_eta_squared_for_one_tenth_less_1e10_eval':str((F(1,10)-F(1,10**10))/(sqrtup(F(901))/2)),'scope':'Pointwise frozen samples. New centers are derived certified transfer proxies, not new FEM solves. Circle factor applies on |omega|<=6,gamma>=1/10; band accuracy requires uniform eta bound and evaluation budget. No rate/termination claim.','records':records,'controls':controls(),'independent_review':False,'physical_promotion':0}
 target=p/'PHASE_RESULTS.json'
 if target.exists():assert json.loads(target.read_text())==result;print('read-only replay matches PHASE_RESULTS.json')
 else:target.write_text(json.dumps(result,indent=2)+'\n')
 for r in records:print('omega',r['omega'],'phase radius',float(F(r['phase_circle_reported_radius'])),'selected',r['selected_method'],float(F(r['selected_reported_radius'])),'old center bound',float(F(r['old_center_intersection_radius'])))
 print('PASS phase circle, exact covariance and outer polygon audit')
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('folder');args=a.parse_args();main(args.folder)
