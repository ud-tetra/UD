"""Validated exact-Gram spectrum; floating eigensystems supply untrusted proposals."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import argparse,json,time
from fractions import Fraction as F
import numpy as np
from scipy.linalg import eigh
from flint import ctx,arb,fmpq
from bindings import P,sha,freeze
from model import rules,source_tail
from proof_math import fm,arr,norm_exact,quantize64,up,down
ctx.prec=512
pair=lambda x:[x.numerator,x.denominator]
def run(case,replay=False):
 f=freeze();o=P/'results'/case;before=sha(o/'GRAM.npz')
 with np.load(o/'GRAM.npz',allow_pickle=False) as z:Gfull=np.array(z['integers_decimal'],dtype=object)
 Gfull=np.array([[int(x) for x in row] for row in Gfull],dtype=object);assert Gfull.shape==(321,321);rows=[]
 for m in f['widths']:
  t=time.monotonic();gg=Gfull[:m,:m];G=fm(gg);prop=o/f'EIGEN_{m}.npz'
  if not replay:
   assert not prop.exists();d,Q=eigh(np.asarray(gg,float)/2.**110,check_finite=False);ind=np.argsort(d)[::-1];qn=quantize64(Q[:,ind],60);dn=quantize64(d[ind],40);np.savez_compressed(prop,Q=qn,eigenvalues=dn)
  with np.load(prop,allow_pickle=False) as z:qn=z['Q'];dn=z['eigenvalues']
  assert qn.shape==(m,m) and dn.shape==(m,) and np.all(dn[:-1]>=dn[1:]);q=fm(qn)
  eta=norm_exact(arr(q.transpose()*q)-np.eye(m,dtype=object)*(1<<120),120);res=norm_exact(arr(G*q)-qn.astype(object)*dn.astype(object)[None,:]*(1<<70),170);gnorm=norm_exact(gg,110)
  assert eta<1;normq=(1+eta).sqrt();dist=eta/(1+(1-eta).sqrt());lmax=arb(max(abs(int(x)) for x in dn))/(1<<40)
  radius=gnorm*eta+res*normq+lmax*dist*(normq+1)
  rr=rules(m);row={'width':m,'Gram_sha256':before,'eigen_proposal_sha256':sha(prop),'orthogonality_defect_upper':up(eta),'eigen_residual_upper':up(res),'eigenvalue_radius_upper':up(radius),'rules':{k:pair(v) for k,v in rr.items()},'counts':{},'physical_promotion':0}
  for rule in ['common','scaled']:
   cut2=arb(fmpq(rr[rule].numerator,rr[rule].denominator));above=[];below=[];uncertain=[]
   for i,n in enumerate(dn):
    center=arb(int(n))/(1<<40)
    if center-radius>cut2:above.append(i)
    elif center+radius<cut2:below.append(i)
    else:uncertain.append(i)
   count=len(above);r={'above_count_lower':count,'above_count_upper':m-len(below),'all_values_classified':not uncertain,'saturated':count==m,'cutoff_squared':pair(rr[rule]),'cutoff_readable':float(cut2.sqrt().upper()),'status':'CERTIFIED_EXACT_SKETCH_COUNT' if not uncertain else 'HOLD_THRESHOLD_INTERSECTION'}
   if not uncertain and count:
    lo=(arb(int(dn[count-1]))/(1<<40)-radius).sqrt();hi=(arb(int(dn[0]))/(1<<40)+radius).sqrt();r.update(retained_sigma_lower=down(lo),largest_sigma_upper=up(hi),condition_upper=up(hi/lo),readable={'retained_sigma_lower':float(lo.lower()),'condition_upper':float((hi/lo).upper())})
    if count<m:
     tail=(arb(int(dn[count]))/(1<<40)+radius).sqrt();r['discarded_sigma_upper']=up(tail);r['readable']['discarded_sigma_upper']=float(tail.upper())
   row['counts'][rule]=r
  s2=source_tail(m);tail=arb(fmpq(s2.numerator,s2.denominator)).sqrt();row['comparison_rank209_tail']={'comparison_model_rank_upper':209,'encoded_sigma210_upper':up(tail),'bound_squared':pair(s2),'readable':float(tail.upper()),'exact_encoded_rank_claimed':False}
  row['seconds']=time.monotonic()-t;rows.append(row);print(json.dumps({'case':case,'width':m,'counts':row['counts'],'sigma210_bound':float(tail.upper())}),flush=True)
 assert sha(o/'GRAM.npz')==before
 result={'case':case,'status':'EXACT_ENCODED_SKETCH_SPECTRAL_ENCLOSURES','record_sha256':next(e['record_sha256'] for e in f['cases'] if e['case']==case),'rows':rows,'replay':replay,'physical_promotion':0,'independent_review':'pending','actual_BLAS_result_or_new_phase_output_certified':False}
 dest=o/('REPLAY_CERTIFICATE.json' if replay else 'CERTIFICATE.json');assert not dest.exists();dest.write_text(json.dumps(result,indent=2));return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('case');p.add_argument('--replay',action='store_true');a=p.parse_args();run(a.case,a.replay)
