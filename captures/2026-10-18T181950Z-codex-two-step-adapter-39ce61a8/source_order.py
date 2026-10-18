"""Source-aware encoded-sketch order at the separately frozen precision cutoff."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import argparse,json,time
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy.linalg import eigh
from flint import ctx,arb,fmpq
from bindings import P,case,freeze,sha
from sketch import sketch
from proof_math import fm,arr,norm_exact,quantize64,up,down
ctx.prec=512

def run(n,records=None,replay=False):
 e=case(n);o=P/'results'/n;o.mkdir(exist_ok=True);q=1+104*len(e['classes'])
 if not replay:
  raw=Path(records)/f'{n}.i64le';assert raw.stat().st_size==150321232 and sha(raw)==e['record_sha256'];Y=np.memmap(raw,dtype='<i8',mode='r',shape=(37,8191,62));X=np.array(Y.transpose(1,2,0).reshape(8191,2294),np.int64);A=sketch();maxraw=max(abs(int(X.min())),abs(int(X.max())));l1=max(sum(abs(int(x)) for x in A[:,j]) for j in range(321));assert maxraw*l1<2**63;N=X@A;G=fm(N).transpose()*fm(N);gg=arr(G);assert sha(raw)==e['record_sha256']
  assert not (o/'GRAM.npz').exists();np.savez_compressed(o/'GRAM.npz',integers_decimal=np.array(gg,dtype=str));d,Q=eigh(np.asarray(gg,float)/2.**110,check_finite=False);ind=np.argsort(d)[::-1];np.savez_compressed(o/'GRAM_EIGEN.npz',Q=quantize64(Q[:,ind],60),eigenvalues=quantize64(d[ind],40));(o/'RAW_PROJECTION.json').write_text(json.dumps({'record_sha256':e['record_sha256'],'readings_projected':18790154,'integer_partial_sum_bound':maxraw*l1,'physical_promotion':0},indent=2))
 with np.load(o/'GRAM.npz',allow_pickle=False) as z:gg=np.array([[int(x) for x in r] for r in z['integers_decimal']],object)
 with np.load(o/'GRAM_EIGEN.npz',allow_pickle=False) as z:qn=z['Q'];dn=z['eigenvalues']
 G=fm(gg);Q=fm(qn);eta=norm_exact(arr(Q.transpose()*Q)-np.eye(321,dtype=object)*(1<<120),120);r=norm_exact(arr(G*Q)-qn.astype(object)*dn.astype(object)[None,:]*(1<<70),170);assert eta<1;normq=(1+eta).sqrt();dist=eta/(1+(1-eta).sqrt());radius=norm_exact(gg,110)*eta+r*normq+arb(max(abs(int(x)) for x in dn))/(1<<40)*dist*(normq+1)
 with np.load(P/'inputs/REFERENCE_PROPOSAL.npz',allow_pickle=False) as z:B=z['coeff']
 L=max(sum(abs(int(x)) for x in B[1:,c]) for c in range(2294));delta=F(L,1<<120)+F(1,1<<49);s2=F(sum(int(x)**2 for x in sketch().flat),1<<14);eps2=8191*2294*delta*delta*s2;eps=arb(fmpq(eps2.numerator,eps2.denominator)).sqrt();cut=arb(fmpq(*freeze()['source_precision_cutoff']));center=arb(int(dn[q-1]))/(1<<40)
 success=bool(center-radius>cut*cut and eps<cut)
 result={'status':'CERTIFIED_SOURCE_PRECISION_ORDER' if success else 'HOLD_SOURCE_PRECISION_EXCITATION','case':n,'source_comparison_rank_upper':q,'exact_encoded_count_above_source_cutoff':q if success else None,'qth_squared_lower':down(center-radius),'qplus1_sigma_upper':up(eps),'source_precision_cutoff':freeze()['source_precision_cutoff'],'Gram_sha256':sha(o/'GRAM.npz'),'eigenproposal_sha256':sha(o/'GRAM_EIGEN.npz'),'eigenvalue_radius_upper':up(radius),'uses_source_comparison_rank_and_generation_bound':True,'original_instrument_noise_rule_changed':False,'physical_promotion':0,'replay':replay}
 if center-radius>0:result['qth_sigma_lower']=down((center-radius).sqrt());result['readable']={'qth_sigma_lower':float((center-radius).sqrt().lower()),'qplus1_sigma_upper':float(eps.upper())}
 dest=o/('ORDER_REPLAY.json' if replay else 'ORDER_CERTIFICATE.json');assert not dest.exists();dest.write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2));return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('case');p.add_argument('--records');p.add_argument('--replay',action='store_true');a=p.parse_args();run(a.case,a.records,a.replay)
