from pathlib import Path
from fractions import Fraction as F
from math import isqrt,isfinite,cos,sin,pi
import hashlib,json,copy
P=Path(__file__).resolve().parent;c=json.loads((P/'CONTRACT.json').read_text());N=c['monitor_samples'];modes=list(range(100,200));K=len(modes);T0=F(1);eta=F(c['per_mode_frequency_error_Hz']);rho=F(c['relative_affine_clock_error']);tau=F(c['per_sample_time_residual_s']);PI=F(22,7);C=F(211,20)
def gram_lower(n,jitter):
 if len({x%n for x in modes})!=K:return None,'nominal alias/rank loss'
 sums=[]
 for a in modes:
  row=F(0)
  for b in modes:
   if a==b:continue
   d=abs(a-b);q=d*rho+2*eta*T0*(1+rho)
   if q>=d or d+q>=F(n,2):return None,'geometric denominator guard'
   lower_sinc=1-(PI*(d+q)/n)**2/6
   if lower_sinc<=0:return None,'nonpositive sine lower bound'
   affine=q/((d-q)*lower_sinc);time_error=2*PI*(F(d)/T0+2*eta)*jitter
   row+=affine+time_error
  sums.append(row)
 return 1-max(sums),'bounded'
def read_energy(record):
 try:
  if not isinstance(record,dict) or set(record)!={'synthetic_fixture','samples'} or record['synthetic_fixture'] is not True:return {'status':'HOLD','reason':'synthetic control format only'}
  if not isinstance(record['samples'],list) or len(record['samples'])!=N:return {'status':'HOLD','reason':'sample count'}
  energy=F(0)
  for pair in record['samples']:
   if not isinstance(pair,list) or len(pair)!=2 or not all(isinstance(x,str) for x in pair):return {'status':'HOLD','reason':'sample encoding'}
   vals=[float.fromhex(x) for x in pair]
   if not all(isfinite(x) for x in vals):return {'status':'HOLD','reason':'nonfinite'}
   if any(float.hex(x)!=s for x,s in zip(vals,pair)):return {'status':'HOLD','reason':'noncanonical hex'}
   energy+=sum(F(x)**2 for x in vals)
  energy/=N;scale=10**12;r=isqrt(energy.numerator*scale**2//energy.denominator)
  if r*r*energy.denominator<energy.numerator*scale**2:r+=1
  rup=F(r,scale);limit=F(c['digital_RMS_ceiling_V'])
  return {'status':'PASS_DIGITAL_FIXTURE' if energy<=limit**2 else 'HOLD','energy':energy,'rms_upper':rup}
 except (ValueError,TypeError,OverflowError):return {'status':'HOLD','reason':'malformed sample'}
lam,reason=gram_lower(N,tau);assert lam>=F(9,10),reason;assert C*C*F(9,10)>=K
shares={k:F(v) for k,v in c['calibration_allocation_V'].items()};eps=sum(shares.values());assert eps==F(1,50000);assert F(1,1000000)*5==shares['quadrature_matrix']
rmax=F(c['digital_RMS_ceiling_V']);out=F(c['outside_model_TV_V']);tail=C*(rmax+eps+out)+out;assert tail<=F(1,1000)
assert gram_lower(64,tau)[0] is None;badlam,_=gram_lower(N,F(1,10000));assert badlam<F(9,10)
old_out=F(1,5000);old_bound=C*(rmax+eps+old_out)+old_out;assert old_bound>F(1,1000)
# Float waveform generation is not used for the source-family proof; output words become exact fixture inputs.
samples=[]
for j in range(N):
 t=j/N
 z=F(3,100000)*complex(cos(2*pi*100*t),sin(2*pi*100*t))+F(1,50000)*complex(cos(2*pi*199*t),sin(2*pi*199*t))+F(1,125000)*complex(cos(2*pi*400*t),sin(2*pi*400*t))+complex(3e-6,2e-6)
 samples.append([float(z.real).hex(),float(z.imag).hex()])
fixture={'synthetic_fixture':True,'samples':samples};fpath=P/'SYNTHETIC_SAMPLES.json';fpath.write_text(json.dumps(fixture,separators=(',',':'))+'\n');fixture=json.loads(fpath.read_text());read=read_energy(fixture);assert read['status']=='PASS_DIGITAL_FIXTURE'
checks=[]
for name,change in [('large_sample',lambda x:x['samples'].__setitem__(0,[float(1).hex(),float(0).hex()])),('wrong_length',lambda x:x['samples'].pop()),('nonfinite',lambda x:x['samples'][0].__setitem__(0,'inf')),('malformed',lambda x:x['samples'][0].__setitem__(0,'invalid')),('not_fixture',lambda x:x.update(synthetic_fixture=False))]:
 bad=copy.deepcopy(fixture);change(bad);r=read_energy(bad);assert r['status']=='HOLD';checks.append({'case':name,'status':'HOLD'})
# Exact nominal alias identity: exp(2pi i (1124-100)*j/1024)=1 for each integer j.
assert all(F((1124-100)*j,N).denominator==1 for j in range(N))
root=P.parents[1];bpath=root/'captures/2026-10-21T190100Z-codex-leakage-budget-094a0b3c/CERTIFICATE.json';b=json.loads(bpath.read_text());H=F(b['inherited_rounded_upper']['H0']['fraction']);fixed=F(b['fixed_error_V']['fraction']);d=fixed+(H+1)*tail+H/F(4000);phase=F(200,99)*d;assert d<F(99,10000) and phase<F(1,50)
def datum(q):return {'fraction':str(q),'approximation':float(q)}
result={'status':'PASS_EXACT_CONDITIONAL_SAMPLED_MONITOR','physical_promotion':0,'contract_sha256':hashlib.sha256((P/'CONTRACT.json').read_bytes()).hexdigest(),'base_certificate_sha256':hashlib.sha256(bpath.read_bytes()).hexdigest(),'sampled_gram_lower':datum(lam),'chosen_floor':'9/10','calibration_allocation_V':{k:str(v) for k,v in shares.items()},'sample_error_total_V':str(eps),'outside_TV_V':str(out),'design_tail_upper_V':datum(tail),'full_state_error_upper_V':datum(d),'phase_upper_rad':datum(phase),'digital_fixture':{'status':read['status'],'sha256':hashlib.sha256(fpath.read_bytes()).hexdigest(),'exact_mean_squared_norm_V2':str(read['energy']),'rms_upper_V':datum(read['rms_upper']),'scope':'Serialized synthetic binary64 values only; not empirical acquisition or calibration evidence'},'negative_controls':checks,'other_controls':{'64_samples':'HOLD_ALIAS_RANK','100us_jitter_lambda':datum(badlam),'old200uV_outside_bound_V':datum(old_bound),'nominal100_and1124_alias':'EXACT_IDENTITY'},'limits':'Source, monitor/IQ/clock/transfer and outside-TV evidence remain unverified. No continuous-time interpolation assumption; no proof of physical independence from a digital fixture.'}
(P/'CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:(v['approximation'] if isinstance(v,dict) and 'approximation' in v else v) for k,v in result.items() if k in ['status','sampled_gram_lower','design_tail_upper_V','full_state_error_upper_V','phase_upper_rad']}))
