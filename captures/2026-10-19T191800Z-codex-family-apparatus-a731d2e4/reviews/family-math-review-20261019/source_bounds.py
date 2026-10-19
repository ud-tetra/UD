"""Independent exact scalar source-bound calculation; no new records or fits."""
import sys
sys.dont_write_bytecode=True
import hashlib,json
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
from flint import arb,fmpq,ctx
ctx.prec=512
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent;P=ROOT/'cutoff-campaign-work'
load=lambda p:json.loads(Path(p).read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
a=lambda x:arb(fmpq(int(x[0]),int(x[1])))

def endpoint(x,upper=True):
 n=((x*(1<<180)).ceil() if upper else (x*(1<<180)).floor()).unique_fmpz();assert n is not None
 return [int(n),1<<180]

def run():
 fr=load(HERE/'SOURCE_BOUND_FREEZE.json')
 for p,h in fr['files'].items():assert sha(ROOT/p)==h,p
 baseline=ROOT/fr['baseline_relative'];assert sha(baseline)==fr['baseline_sha256']
 raw=np.memmap(baseline,dtype='<i8',mode='r');assert raw.size==37*8191*62
 normnum=0
 for start in range(0,raw.size,500000):normnum+=sum(int(x)**2 for x in raw[start:start+500000])
 assert normnum==552546211865498532528442731269961
 f0sq=F(normnum,1<<96);F0=a([f0sq.numerator,f0sq.denominator]).sqrt()
 vv=load(P/'inputs/NULL_VECTOR.json')['vector'];v2=sum(int(x)**2 for x in vv);assert v2==16228
 sketch_num=2*4*2294*160+v2;assert sketch_num==2952548;k2=F(sketch_num,128*128);k=a([k2.numerator,k2.denominator]).sqrt()
 h=arb(1)/(1<<48);cut=arb(1)/(1<<24);nv=37*8191;ns=nv*62;sn=arb(ns).sqrt();sv=arb(nv).sqrt()
 generation=load(P/'inputs/BASE_GENERATION.json');source=next(x for x in generation['records'] if x['record_sha256']==fr['baseline_sha256']);d0=a(source['evaluation_bounds']['scalar_waveform_error_upper'])
 anchors=load(P/'CAMPAIGN_NUMERIC_CERTIFICATES.json')['rows'];assert len(anchors)==6
 lowerpairs=[x['cutoff']['sigma209_lower'] for x in anchors];gpair=min(lowerpairs,key=lambda x:F(*x));g=a(gpair)
 tail=lambda delta:k*((d0+h/2)*sn+delta*sv)
 critical_m=(cut/(2*k)-(d0+h/2)*sn)/(h*sv);floor=critical_m.floor().unique_fmpz();assert floor is not None;m=int(floor);assert m>0
 if not tail(m*h)<cut/2:m-=1
 assert tail(m*h)<cut/2 and tail((m+1)*h)>cut/2
 rows=[]
 # Both policies are declared before arithmetic: exact-contour maximal integer
 # and conservative floor-minus-one. Neither is an actual noise tolerance limit.
 for name,mvalue in [('maximum_strict_integer_for_this_tail_contour',m),('floor_minus_one_conservative',int(floor)-1)]:
  delta=mvalue*h;noise=k*(h*sn+(delta+h)*sv);gap=g-cut-noise;assert gap>0
  critical_rho=gap/(2*k*F0);exponent=0
  while not arb(1)/(1<<exponent)<critical_rho:exponent+=1;assert exponent<100
  rho=arb(1)/(1<<exponent);assert 2*rho>=critical_rho
  low=g-k*(F0*rho+h*sn+(delta+h)*sv);high=tail(delta);assert low>cut and high<cut/2
  rows.append({'policy':name,'m':mvalue,'delta':[mvalue,1<<48],'rho':[1,1<<exponent],'rho_exponent':exponent,'sigma209_lower':endpoint(low,False),'sigma210_upper':endpoint(high),'critical_rho_upper':endpoint(critical_rho),'critical_rho_lower':endpoint(critical_rho,False),'strict_cutoff_guarantee_at_closed_chosen_radius':True,'readable':{'delta':float(delta),'rho':float(rho),'sigma209_lower':float(low.lower()),'sigma210_upper':float(high.upper())}})
 assert sha(baseline)==fr['baseline_sha256']
 for p,z in fr['files'].items():assert sha(ROOT/p)==z,p
 out={'status':'PASS_INDEPENDENT_EXACT_SOURCE_ARITHMETIC','raw_baseline_Frobenius_squared':[str(f0sq.numerator),str(f0sq.denominator)],'sketch_Frobenius_squared':[k2.numerator,k2.denominator],'null_vector_integer_squared_norm':v2,'nscalar':ns,'nvector':nv,'anchor_sigma209_min_lower':gpair,'critical_m_lower':endpoint(critical_m,False),'critical_m_upper':endpoint(critical_m),'rows':rows,'readable':{'F0':float(F0),'k':float(k),'critical_m':float(critical_m)},'freeze_sha256':sha(HERE/'SOURCE_BOUND_FREEZE.json'),'completed_utc':datetime.now(timezone.utc).isoformat(),'scope':'Scalar inequalities for explicit rank/source-error/orthogonal-transform premises. Original baseline read only, no new record/projection/estimator/phase run. Contour maximality is not actual noise tolerance or floating admission.','external_review':'PENDING','physical_promotion':0}
 q=HERE/'SOURCE_BOUNDS.json';assert not q.exists();q.write_text(json.dumps(out,indent=2));print(json.dumps(out),flush=True)

if __name__=='__main__':run()
