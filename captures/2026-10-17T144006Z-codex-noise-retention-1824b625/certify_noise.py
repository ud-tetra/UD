"""Source-bound, conservative noise/retained-signal certificates. No large Hankel allocation."""
from pathlib import Path
from fractions import Fraction as F
import json,csv
from flint import arb,ctx
ctx.prec=512
ROOT=Path(__file__).resolve().parent
def a(x):
 x=F(x);return arb(x.numerator)/x.denominator
def pair(x):
 x=F(x);return [x.numerator,x.denominator]
def frac(x):return F(*x)
def dyadic(x,up=False,bits=160):
 """Outward dyadic bound on an Arb interval, never a floating decision."""
 y=(x*2**bits).upper() if up else (x*2**bits).lower()
 z=y.ceil() if up else y.floor()
 return F(int(z.fmpq()),2**bits)
def enc(x):return {'arb_enclosure':str(x),'display_only':float(x.mid())}
def load(name):return json.loads((ROOT/'sources'/name).read_text())
def save(name,x):(ROOT/name).write_text(json.dumps(x,indent=2)+'\n')

def modal_bounds(parent):
 out=[]
 for k,c in enumerate(parent['components']):
  lo=dyadic(arb(c['B_gram_positive_eigenvalue_lower']))
  hi=dyadic(arb(c['B_gram_max_eigenvalue_upper']),True)
  assert 0<lo<=hi
  mult=1 if c['factor_L']=='x' else 2
  out.append({'id':k,'factor_L':c['factor_L'],'root_interval':c['root_interval'],
   'rank_per_signed_frequency':c['rank_per_signed_frequency'],
   'signed_frequency_multiplicity':mult,'rank_total':mult*c['rank_per_signed_frequency'],
   'modal_positive_sigma_squared_lower':pair(lo),'modal_sigma_squared_upper':pair(hi)})
 assert len(out)==53 and sum(x['rank_total'] for x in out)==1893
 assert sum(x['signed_frequency_multiplicity'] for x in out)==105
 return out

def model_budgets(fitted,trade):
 p=F(1,2**25);tau=F(1,2**28);qplus=F(1025,1024)
 rec=trade['recommended']
 validated={k:dyadic(arb(rec[v]['arb_enclosure']),True) for k,v in {
  'eta':'history_total_metric_bound','r':'history_native_rate_bound',
  'rho':'history_final_readout_bound'}.items()}
 specs={'output_only':{'eta':F(0),'r':F(0),'sigma':F(0),'rho':F(0),'p':F(0),'tau':F(0)},
  'parent_model':{'eta':F(1,2**35),'r':F(1,2**35),'sigma':F(1,2**35),'rho':p,'p':p,'tau':tau},
  'restricted_pass_contract':{**validated,'sigma':F(0),'p':p,'tau':tau}}
 out={}
 stock=a(F(165,169)).sqrt()
 for name,s in specs.items():
  eta,r,sigma,rho,prep,timing=[a(s[k]) for k in ['eta','r','sigma','rho','p','tau']]
  e=(4*r+sigma+4*a(qplus)*eta)/(1-eta)
  g=((1+eta)/(1-eta)).sqrt()
  u0=g*((1+rho)*prep+rho*stock+stock*(4*a(qplus)+e)*timing)
  v=g*stock*e
  out[name]={'parameters':{k:pair(vv) for k,vv in s.items()},
   'u0':pair(dyadic(u0,True)),'v':pair(dyadic(v,True)),
   'generator_error_upper':enc(e),'propagator_upper':enc(g)}
 return out

def beta_squared(M,delta,budget):
 u=frac(budget['u0'])+delta;v=frac(budget['v'])
 return 37*(u*u+u*v*(M-1)+v*v*F(7*M*M-12*M+5,24))

def counts(blocks,low_frame,high_frame,beta2):
 guaranteed=[];possible2=[];possible4=[]
 for b in blocks:
  lo=low_frame**2*frac(b['modal_positive_sigma_squared_lower'])
  hi=high_frame**2*frac(b['modal_sigma_squared_upper'])
  if lo>=16*beta2:guaranteed.append(b)
  if hi>beta2:possible2.append(b) # nominal >beta => noisy may exceed2beta
  if hi>=16*beta2:possible4.append(b)
 count=lambda xs:sum(x['rank_total'] for x in xs)
 return count(guaranteed),count(possible4),count(possible2),[x['id'] for x in guaranteed]

def full_rank_noise_ceiling(M,frame,budget,minlo):
 u= a(frac(budget['u0']));v=a(frac(budget['v']))
 mean=a(F(M-1,2));variance=a(F(M*M-1,24))
 # mu2-mu^2=(M^2-1)/24 for t=(i+j)/2.
 rad=a(frame**2*minlo/F(16*37))-v*v*variance
 if not rad>0:return None
 x=rad.sqrt()-u-v*mean
 return {**enc(x),'sufficient_dyadic_ceiling':pair(dyadic(x))} if x>0 else None

def build():
 parent=load('PARENT_PREPARATION_CERTIFICATE.json')
 fitted=load('PARENT_FITTED_CERTIFICATE.json');trade=load('PARENT_TRADEOFF_CERTIFICATE.json')
 assert parent['history_rank_excited']==1893 and parent['preparations']==37
 blocks=modal_bounds(parent);budgets=model_budgets(fitted,trade)
 C=frac(fitted['common_scale_family']['temporal_C_upper_rational'])
 assert C==F(1828864,1021) and C<1792
 minlo=min(frac(b['modal_positive_sigma_squared_lower']) for b in blocks)
 maxhi=max(frac(b['modal_sigma_squared_upper']) for b in blocks)
 protocols=[];rows=[]
 for M in [2048,4096,8192]:
  low,high=1-C/M,1+C/M
  assert low>0
  protocol={'M':M,'step_normalized':[1,2],'raw_vectors_per_preparation':2*M-1,
   'last_time':[M-1,1],'scalar_outputs':37*62*(2*M-1),
   'temporal_epsilon_upper':pair(C/M),'frame_low':pair(low),'frame_high':pair(high),
   'nominal_rank':1893,'nominal_sigma_min_lower':enc(a(low**2*minlo).sqrt()),
   'nominal_sigma_max_upper':enc(a(high**2*maxhi).sqrt()),'models':{}}
  for name,budget in budgets.items():
   samples=[]
   for n in range(30,7,-1):
    delta=F(1,2**n);beta2=beta_squared(M,delta,budget)
    lower,upper4,upper2,ids=counts(blocks,low,high,beta2)
    row={'model':name,'M':M,'delta_exponent':-n,'delta':pair(delta),
     'beta_squared_upper':pair(beta2),'guaranteed_retained_count':lower,
     'reference_count_at_4beta_upper':upper4,'observed_count_above_2beta_upper':upper2,
     'retained_block_ids':ids}
    if lower:
     s2=low**2*min(frac(blocks[i]['modal_positive_sigma_squared_lower']) for i in ids)
     cond=(a(high**2*maxhi).sqrt()+a(beta2).sqrt())/(a(s2).sqrt()-a(beta2).sqrt())
     row['top_d_condition_upper']=enc(cond)
    samples.append(row);rows.append(row)
   # Each step is an exact sufficient boundary for admitting the entire block.
   stairs=[]
   for b in blocks:
    ceiling=full_rank_noise_ceiling(M,low,budget,frac(b['modal_positive_sigma_squared_lower']))
    if ceiling is not None:
     stairs.append({'block_id':b['id'],'rank_total':b['rank_total'],
      'per_vector_noise_ceiling':ceiling})
   protocol['models'][name]={'full_1893_noise_ceiling':full_rank_noise_ceiling(M,low,budget,minlo),
    'samples':samples,'block_admission_boundaries':stairs}
  protocols.append(protocol)
 out={'status':'DERIVED_CONDITIONAL_INTERVAL_CONSTRUCTOR_VERIFIED','physical_promotion':0,
  'independent_review':'pending','lane':'development; no registry entry',
  'scope':'Original real62-channel shell and explicit37 preparations; normalized Hankel; fixed constant common rate within1+/-1/1024',
  'precision_bits':512,'outward_dyadic_bits':160,'modal_blocks':blocks,'budgets':budgets,
  'perturbation_contract':'Per62-vector additive error <=delta, adversarial across all inputs and times; model response error <=u0+delta+v*t',
  'count_rule':'d=sum ranks for blocks with (1-C/M)^2*l_block >=16*beta^2. At leastd observed singular values exceed2beta; at most U=sum ranks with (1+C/M)^2*u_block > beta^2 can exceed2beta.',
  'zero_modes':'Nominal747-dimensional dynamical kernel unchanged; no recovery claimed',
  'protocols':protocols,'not_claimed':['Measured performance','Exact partial ranks from block extrema',
   'Recovery of individual modal orC10 coordinates from thresholding','Automatic relaxation of six-ratio calibration tolerances',
   'Characteristic13 transfer','Subspace-angle certification','Universal noise or information lower bounds']}
 save('NOISE_RETENTION_CERTIFICATE.json',out)
 choices=[]
 for exponent,maxcond in [(-20,2029),(-19,2246),(-16,323),(-14,98),(-12,25)]:
  p=protocols[1]
  s=next(s for s in p['models']['restricted_pass_contract']['samples'] if s['delta_exponent']==exponent)
  assert arb(s['top_d_condition_upper']['arb_enclosure'])<maxcond
  choices.append({'axis_samples':4096,'per62_vector_additive_error_ceiling':s['delta'],
   'sufficient_per_scalar_additive_error_ceiling':pair(frac(s['delta'])/8),
   'guaranteed_retained_count':s['guaranteed_retained_count'],'top_d_condition_upper_integer':maxcond,
   'Hankel_operator_error_bound':enc(a(frac(s['beta_squared_upper'])).sqrt()),
   'observed_selection_threshold':enc(2*a(frac(s['beta_squared_upper'])).sqrt()),
   'status':'PROPOSED_CONDITIONAL_CONTRACT; no apparatus execution'})
 save('ACQUISITION_CHOICES.json',{'physical_promotion':0,'independent_review':'pending',
  'family':'restricted-pass contract only; all model assumptions and calibration gates retained',
  'scalar_to_vector_reason':'sqrt(62)<8; eightfold smaller per-scalar absolute errors suffice deterministically',
  'choices':choices})
 with (ROOT/'NOISE_RETENTION_CURVE.csv').open('w',newline='') as f:
  w=csv.writer(f);w.writerow(['model','axis_samples','vector_error_delta','guaranteed_retained_count','reference_count_at_4beta_upper','observed_count_above_2beta_upper'])
  for r in rows:w.writerow([r['model'],r['M'],str(frac(r['delta'])),r['guaranteed_retained_count'],r['reference_count_at_4beta_upper'],r['observed_count_above_2beta_upper']])
 return out
if __name__=='__main__':
 d=build()
 for p in d['protocols']:
  print('M',p['M'])
  for name,m in p['models'].items():
   print(name,'full1893delta',m['full_1893_noise_ceiling'])
   print([(s['delta_exponent'],s['guaranteed_retained_count']) for s in m['samples'] if s['delta_exponent'] in [-20,-18,-16,-14,-12,-10]])
