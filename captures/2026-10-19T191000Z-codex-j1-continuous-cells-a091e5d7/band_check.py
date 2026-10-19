"""Exact continuous parameter-cell propagation and low-frequency output certificate."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json,hashlib,argparse
TOL=F(1,10);GAMMAS=list(map(F,['1/10','3/20','1/5','1/4','3/10','2/5','1/2','3/5','4/5','1']))
D2=F(399,2500)
def sqrtup(x):
 assert x>=0
 scale=10**18;n=isqrt(x.numerator*scale*scale//x.denominator)
 if F(n*n,scale*scale)<x:n+=1
 r=F(n,scale);assert r*r>=x
 return r

def static_pass(delta,gmax,S,r,ev=F(0)):
 assert 0<=delta<2 and gmax>0 and 0<=r<TOL
 return S*S*delta*delta*(delta*delta+4*gmax*gmax)<=(TOL-r-ev)**2*(4-delta*delta)**2

def static_width(gmax,S,r,ev=F(0)):
 lo,hi=0,1999999
 while hi-lo>1:
  k=(lo+hi)//2
  if static_pass(F(k,10**6),gmax,S,r,ev):lo=k
  else:hi=k
 delta=F(lo,10**6)
 assert static_pass(delta,gmax,S,r,ev) and not static_pass(F(hi,10**6),gmax,S,r,ev)
 bound=r+S*sqrtup(delta*delta*(delta*delta+4*gmax*gmax))/(4-delta*delta)
 assert bound+ev<=TOL
 return delta,bound

def validate_cover(cells):
 for ga,gb in zip(GAMMAS,GAMMAS[1:]):
  row=sorted((c for c in cells if F(c['gamma_lower'])==ga and F(c['gamma_upper'])==gb),key=lambda c:F(c['omega_lower']))
  assert row and F(row[0]['omega_lower'])==0 and F(row[-1]['omega_upper'])==6,'missing band endpoint'
  end=F(0)
  for c in row:
   a,b=F(c['omega_lower']),F(c['omega_upper']);assert a==end and a<b,'cell gap/overlap';end=b
 assert len(cells)==sum(sum(F(c['gamma_lower'])==a and F(c['gamma_upper'])==b for c in cells) for a,b in zip(GAMMAS,GAMMAS[1:])),'unexpected damping cell'

def propagate(a,b,ga,gb,anchor):
 assert F(1,10)<=ga<=gb<=1 and 0<=a<=b<=6
 om,g0,cx,cy,R,Q=anchor;t0=om*om;im0=2*g0*om
 delta2=max((a*a-t0)**2,(b*b-t0)**2)+max((2*ga*a-im0)**2,(2*gb*b-im0)**2)
 for omc in [a,b]:
  for gac in [ga,gb]:assert (omc*omc-t0)**2+(2*gac*omc-im0)**2<=delta2
 variation=sqrtup(delta2*20*Q/D2)
 return R+variation,delta2,variation

def main(folder):
 out=Path(folder);solve_raw=(out/'INPUT_SOLVES.json').read_bytes();enc_raw=(out/'INPUT_ENCLOSURES.json').read_bytes();solves=json.loads(solve_raw);enc=json.loads(enc_raw)
 assert solves['status']==enc['status']=='PASS' and enc['input_sha256']==hashlib.sha256(solve_raw).hexdigest()
 br=solves['records'][0]['static_continuum_bracket'];lo,hi=F(br['lower']),F(br['upper']);center=(lo+hi)/2;static_r=(hi-lo)/2
 anchors=[(F(0),F(1,10),center,F(0),static_r,hi/4)]
 for s,e in zip(solves['records'][1:],enc['records'][1:]):
  assert s['omega']==e['omega'] and s['gamma']==e['gamma'];om,ga=F(s['omega']),F(s['gamma']);Q=-min(F(p[1]) for p in e['polygon_vertices'])/(2*ga*om);assert Q>=0
  R=F(e['certified_reported_output_radius'])-F(s['reported_corrected_evaluation_error_bound']);assert R>=0
  anchors.append((om,ga,F(s['corrected_output_real']),F(s['corrected_output_imag']),R,Q))
 static_ev=sqrtup((F.from_float(float(center))-center)**2)
 gain=sqrtup(F(1000000,399));cells=[];widths=[]
 for ga,gb in zip(GAMMAS,GAMMAS[1:]):
  d,rad=static_width(gb,hi,static_r,static_ev);widths.append({'gamma_lower':str(ga),'gamma_upper':str(gb),'certified_abs_omega_upper':str(d),'error_radius':str(rad),'reported_surrogate_error_radius':str(rad+static_ev),'next_microstep_fails_this_sufficient_test':True})
  cells.append({'gamma_lower':str(ga),'gamma_upper':str(gb),'omega_lower':'0','omega_upper':str(d),'center_real':str(center),'center_imag':'0','radius':str(rad),'method':'static spectral variation','precision_passed':True})
  cuts=[d]+[F(i,4) for i in range(1,25) if F(i,4)>d]
  for a,b in zip(cuts,cuts[1:]):
   candidates=[]
   for k,anchor in enumerate(anchors):
    rad,delta2,var=propagate(a,b,ga,gb,anchor);candidates.append((rad,k,delta2,var))
   rad,k,delta2,var=min(candidates);anchor=anchors[k];method='anchor resolvent propagation';cx,cy=anchor[2],anchor[3]
   if gain<rad:rad=gain;cx=cy=F(0);method='prior global gain disk'
   cells.append({'gamma_lower':str(ga),'gamma_upper':str(gb),'omega_lower':str(a),'omega_upper':str(b),'center_real':str(cx),'center_imag':str(cy),'radius':str(rad),'method':method,'precision_passed':rad<=TOL,'best_anchor_index':k,'anchor_delta_z_squared_upper':str(delta2),'anchor_variation_upper':str(var)})
 for cell in cells:
  cx,cy=F(cell['center_real']),F(cell['center_imag']);fr,fi=float(cx),float(cy)
  ev=sqrtup((F.from_float(fr)-cx)**2+(F.from_float(fi)-cy)**2)
  cell['reported_center_real_hex']=fr.hex();cell['reported_center_imag_hex']=fi.hex();cell['center_evaluation_error_bound']=str(ev);cell['reported_surrogate_radius']=str(F(cell['radius'])+ev);cell['precision_passed']=F(cell['reported_surrogate_radius'])<=TOL
 validate_cover(cells)
 try:validate_cover(cells[1:])
 except AssertionError:pass
 else:raise AssertionError('missing-cell control accepted')
 try:propagate(F(4),F(5),F(0),F(1),anchors[1])
 except AssertionError:pass
 else:raise AssertionError('undamped out-of-scope cell accepted')
 # Exact completed-square denominator identity at a symbolic coefficient level in t.
 # (lambda-t)^2+t/25 = (t-lambda+1/50)^2+(lambda-4)/25+399/2500.
 for lam in [F(4),F(5),F(20)]:
  assert [F(1),-2*lam+F(1,25),lam*lam]==[F(1),-2*(lam-F(1,50)),(lam-F(1,50))**2+(lam-4)/25+F(399,2500)]
 covered_area=sum(F(w['certified_abs_omega_upper'])*(F(w['gamma_upper'])-F(w['gamma_lower'])) for w in widths)
 result={'status':'PASS','classification':'CONDITIONAL_CONTINUOUS_CELL_ENCLOSURES_PARTIAL_PRECISION_COVERAGE','source_solve_sha256':hashlib.sha256(solve_raw).hexdigest(),'source_enclosure_sha256':hashlib.sha256(enc_raw).hexdigest(),'target_absolute_error':str(TOL),'proxy_scope':'Each cell has an exact rational surrogate and recorded binary64 center hex with exact posterior evaluation bound. No new Galerkin solve or experiment. Negative-frequency cells are conjugates.','static_center':str(center),'static_input_radius':str(static_r),'uniform_full_damping_strip':dict(widths[-1],gamma_lower='1/10'),'damping_dependent_precision_strips':widths,'positive_frequency_cell_count':len(cells),'precision_passing_cells':sum(c['precision_passed'] for c in cells),'all_cells_valid_enclosures':True,'full_band_precision_passed':all(c['precision_passed'] for c in cells),'positive_band_area':str(F(6)*F(9,10)),'certified_precision_area':str(covered_area),'max_radius':str(max(F(c['reported_surrogate_radius']) for c in cells)),'anchors':[{'omega':str(a[0]),'gamma':str(a[1]),'center_real':str(a[2]),'center_imag':str(a[3]),'anchor_radius':str(a[4]),'L2_solution_norm_squared_upper':str(a[5])} for a in anchors],'cells':cells,'controls':{'missing_cell_rejected':True,'out_of_scope_zero_damping_rejected':True,'next_microstep_sufficient_bound_rejected':True},'independent_review':False,'physical_promotion':0}
 p=out/'RESULTS.json'
 if p.exists():assert json.loads(p.read_text())==result;print('read-only exact replay matches RESULTS.json')
 else:p.write_text(json.dumps(result,indent=2)+'\n')
 print('PASS',len(cells),'continuous positive-frequency cells;',result['precision_passing_cells'],'meet1/10; full-band precision',result['full_band_precision_passed'])
 for w in widths:print(w['gamma_lower'],w['gamma_upper'],'|omega|<=',w['certified_abs_omega_upper'],'radius',float(F(w['error_radius'])))
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('output');args=a.parse_args();main(args.output)
