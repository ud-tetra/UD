import argparse,json,time,resource
from fractions import Fraction as F
import numpy as np
from flint import ctx,arb
from bindings import P,sha,check
from source_model import model
from proof_math import fm,arr,up,down
from numeric_math import encode
from operator_bounds import gram_norm
from frame_values import constants
from calibration_math import budget
ctx.prec=512

def run(replay=False):
 start=time.monotonic();f=check();theta,N=model();ch=fm(N);path=P/'RIGHT_INVERSE.npz';before=sha(path)
 with np.load(path,allow_pickle=False) as z:H=z['right_inverse']
 assert H.shape==(161,105);hn,bh=encode(H);r=arr(ch*fm(hn)-fm(np.eye(105,dtype=object))*(1<<(67+bh)))
 rho,rreceipt=gram_norm(r,67+bh);h,hreceipt=gram_norm(hn,bh);cn,creceipt=gram_norm(N.T,67)
 assert rho<1 and h>0;gamma=(1-rho)/h;omega2=F(sum(int(t)**2 for t in theta),1<<120);omega=(arb(omega2.numerator)/arb(omega2.denominator)).sqrt()
 c=json.loads((P/'inputs/PHASE_STABILITY_CERTIFICATE.json').read_text())['constants'];cc=constants(theta)
 assert all(c[k]==v for k,v in cc.items()),'Frame conditioning/separation must replay'
 metrics={'coefficient_sigma_lower':down(gamma),'coefficient_norm_upper':up(cn),'right_inverse_residual_upper':up(rho),'right_inverse_norm_upper':up(h),'Omega_upper':up(omega),'Omega_squared_exact':[omega2.numerator,omega2.denominator]}
 rows=[]
 for p in f['preparation_fractions']:rows.append({'family':'preparation_margin','parameter':p,**budget(c,metrics,F(*p),0,0,0,False)})
 for name,exponents in [('jitter',f['jitter_exponents']),('clock_rate',f['clock_rate_exponents']),('raw_additive',f['raw_noise_exponents'])]:
  for k in exponents:
   value=F(1,1<<k);args=[value if name=='jitter' else F(0),value if name=='clock_rate' else F(0),value if name=='raw_additive' else F(0)]
   rows.append({'family':name,'parameter_exponent':k,**budget(c,metrics,F(*f['grid_preparation_fraction']),*args)})
 j=f['joint_control'];joint=budget(c,metrics,F(*j['preparation_fraction']),F(*j['jitter']),F(*j['clock_rate']),F(*j['raw_delta']))
 largest={}
 for family in ['jitter','clock_rate','raw_additive']:
  passed=[r for r in rows if r['family']==family and r['unique_phase_matching']];largest[family]=min(passed,key=lambda r:r['parameter_exponent']) if passed else None
 result={'status':'CONDITIONAL_PREPARATION_CLOCK_BUDGET_CERTIFICATE','physical_promotion':0,'independent_review':'pending','same_team_review_only':True,'metrics':metrics,'Gram_receipts':{'inverse_residual':rreceipt,'inverse_norm':hreceipt,'coefficient_norm':creceipt},'right_inverse_binary_scale_bits':bh,'right_inverse_sha256':before,'frame_constants_recomputed':True,'rows':rows,'largest_passing_budgets_on_frozen_grids':largest,'joint_control':joint,'actual_floating_estimator_convergence_certified':False,'SI_clock_accuracy_certified':False,'unwrapped_principal_band_interpolation_is_assumed':True,'raw_full_2neg20_matching_certified':next(r['unique_phase_matching'] for r in rows if r['family']=='raw_additive' and r['parameter_exponent']==20),'replay':replay,'wall_seconds':time.monotonic()-start,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'readable':{'coefficient_sigma_lower':float(gamma.lower()),'coefficient_norm_upper':float(cn.upper()),'right_inverse_residual_upper':float(rho.upper()),'right_inverse_norm_upper':float(h.upper()),'Omega_upper':float(omega.upper())}}
 assert sha(path)==before;check();out=P/('REPLAY_CERTIFICATE.json' if replay else 'BUDGET_CERTIFICATE.json');assert not out.exists();out.write_text(json.dumps(result,indent=2));print(json.dumps({'metrics':result['readable'],'largest_passing_exponents':{k:v['parameter_exponent'] if v else None for k,v in largest.items()},'joint':joint.get('readable'),'full_2neg20':result['raw_full_2neg20_matching_certified']},indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');a=p.parse_args();run(a.replay)
