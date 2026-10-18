import argparse,json,time,resource
from fractions import Fraction as F
import numpy as np
from flint import ctx,arb
from bindings import P,check,sha
from source_model import source,rotate,coefficients
from numeric_math import encode
from operator_bounds import gram_norm
from proof_math import fm,arr,up,down
from frame_values import constants
from prep_math import budget
ctx.prec=512

def inverse_certificate(N,H,bits,rounding):
 hn,bh=encode(H);assert H.shape==(161,105);R=arr(fm(N)*fm(hn)-fm(np.eye(105,dtype=object))*(1<<(bits+bh)));rho,rr=gram_norm(R,bits+bh);h,hr=gram_norm(hn,bh)
 if not (rho<1 and h>0):return {'status':'HOLD_RIGHT_INVERSE','rho_upper':up(rho),'h_upper':up(h)}
 gamma=(1-rho)/h-rounding
 if not gamma>0:return {'status':'HOLD_ROTATION_EXCITATION','rho_upper':up(rho),'h_upper':up(h),'rounding_upper':up(rounding)}
 return {'status':'CERTIFIED_EXCITATION','gamma_lower':down(gamma),'rho_upper':up(rho),'h_upper':up(h),'rotation_rounding_upper':up(rounding),'inverse_residual_Gram':rr,'inverse_norm_Gram':hr,'right_inverse_binary_scale_bits':bh,'readable_gamma_lower':float(gamma.lower())}

def run(replay=False):
 start=time.monotonic();f=check();theta,B,A=source();s2=F(sum(int(x)**2 for x in A.flat),2**14);s=(arb(s2.numerator)/arb(s2.denominator)).sqrt();omega2=F(sum(int(t)**2 for t in theta),2**120);omega=(arb(omega2.numerator)/arb(omega2.denominator)).sqrt()
 energy=np.zeros((52,37),dtype=object)
 for j in range(52):
  x=B[2*j+1].astype(object).reshape(62,37);y=B[2*j+2].astype(object).reshape(62,37);energy[j]=np.sum(x*x+y*y,axis=0)
 total_energy=sum(int(x) for x in energy.flat);weighted=sum(int(theta[j])**2*int(x) for j in range(52) for x in energy[j]);weighted_f=F(weighted,2**240);Koff=s*(arb(weighted_f.numerator)/arb(weighted_f.denominator)).sqrt();rounding=(arb(total_energy).sqrt()/(1<<60))*s/(1<<59)
 L=[]
 for a in range(37):L.append(up(sum((arb(int(theta[j]))*arb(int(energy[j,a])).sqrt()/(1<<120) for j in range(52)),arb(0))))
 c=json.loads((P/'inputs/PHASE_STABILITY_CERTIFICATE.json').read_text())['constants'];cc=constants(theta);assert all(c[k]==v for k,v in cc.items());assert s2==F(371097,4096) and F(*c['noise_transfer_squared'])==37*8191*s2
 profiles=[]
 for e in f['profiles']:
  path=P/'profiles'/f"{e['name']}.npz";hsh=sha(path)
  with np.load(path,allow_pickle=False) as z:co=z['cos_num'];si=z['sin_num'];H=z['right_inverse']
  Bo,cnew,snew=rotate(theta,B,e['offsets']);assert np.array_equal(co,cnew) and np.array_equal(si,snew);N=coefficients(Bo,A);eps=arb(0) if all(F(*v)==0 for v in e['offsets']) else rounding
  inv=inverse_certificate(N,H,127,eps);profiles.append({'name':e['name'],'offsets':e['offsets'],'witness_sha256':hsh,'coefficient_scale_bits':127,**inv});assert sha(path)==hsh
 baseline=profiles[0];assert baseline['name']=='zero' and baseline['status']=='CERTIFIED_EXCITATION'
 metrics={'baseline_gamma_lower':baseline['gamma_lower'],'sketch_norm_upper':up(s),'offset_multiplier_upper':up(Koff),'Omega_upper':up(omega),'per_preparation_Lipschitz_upper':L,'weighted_offset_energy_squared_exact':[weighted_f.numerator,weighted_f.denominator],'raw_nonstationary_energy_squared_exact':[total_energy,2**120]}
 rows=[]
 for k in f['offset_box_exponents']:rows.append({'family':'offset_excitation_box','parameter_exponent':k,**budget(c,metrics,F(1,2**k),0,0,0,0,model_floor=False)})
 for fraction in f['preparation_fractions']:rows.append({'family':'preparation_margin','parameter':fraction,**budget(c,metrics,F(*f['grid_offset_box']),F(*fraction),0,0,0,model_floor=False)})
 for family,exp in [('jitter',f['jitter_exponents']),('rate',f['rate_exponents'])]:
  for k in exp:rows.append({'family':family,'parameter_exponent':k,**budget(c,metrics,F(*f['grid_offset_box']),F(*f['grid_preparation_fraction']),F(1,2**k) if family=='jitter' else 0,F(1,2**k) if family=='rate' else 0,0)})
 j=f['joint_control'];joint=budget(c,metrics,F(*j['offset_box']),F(*j['preparation_fraction']),F(*j['jitter']),F(*j['rate']),F(*j['raw_delta']))
 for e in profiles:
  if e['status']=='CERTIFIED_EXCITATION':e['joint_clock_budget']=budget(c,metrics,0,F(*j['preparation_fraction']),F(*j['jitter']),F(*j['rate']),F(*j['raw_delta']),profile_gamma=e['gamma_lower'])
 maxima={}
 for family in ['offset_excitation_box','jitter','rate']:
  good=[x for x in rows if x['family']==family and x['unique_phase_matching']];maxima[family]=min(good,key=lambda x:x['parameter_exponent']) if good else None
 out={'status':'CONDITIONAL_PREPARATION_SPECIFIC_CLOCK_CERTIFICATE','physical_promotion':0,'independent_review':'pending','metrics':metrics,'profiles':profiles,'rows':rows,'largest_passing_frozen_grid_budgets':maxima,'joint_control':joint,'frame_constants_recomputed':True,'sketch_source_norm_recomputed':True,'same_team_review_only':True,'new_actual_phase_estimator_execution':False,'SI_clock_accuracy_certified':False,'principal_band_interpolation_assumed':True,'replay':replay,'wall_seconds':time.monotonic()-start,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'readable':{'baseline_gamma_lower':baseline['readable_gamma_lower'],'offset_multiplier_upper':float(Koff.upper()),'raw_preparation_Lipschitz_aggregate_upper':None}}
 # Aggregate readable quantity has no role in acceptance.
 out['readable']['raw_preparation_Lipschitz_aggregate_upper']=float(sum((arb(v[0])/v[1])**2 for v in L).sqrt().upper())
 check();dest=P/('REPLAY_CERTIFICATE.json' if replay else 'CERTIFICATE.json');assert not dest.exists();dest.write_text(json.dumps(out,indent=2));print(json.dumps({'metrics':out['readable'],'profiles':[{k:v for k,v in e.items() if k in ['name','status','readable_gamma_lower']} for e in profiles],'largest_passing_exponents':{k:v['parameter_exponent'] if v else None for k,v in maxima.items()},'joint':joint.get('readable')},indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');a=p.parse_args();run(a.replay)
