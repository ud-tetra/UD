"""Frozen-dimension algebraic controls. These impulse records are not UD trajectories or experiments."""
from pathlib import Path
from fractions import Fraction as F
import json,tempfile,time,resource
import numpy as np
from flint import arb
from hankel_exact import HankelRecord
from spectral_certificate import certify,pair,a,bound
ROOT=Path(__file__).resolve().parent

def build():
 config=json.loads((ROOT/'sources'/'FROZEN_CONTRACT.json').read_text());rule=config['spectral_rule']
 M=4096;p=37;c=62;r=1893;data_den=2**48;T=F(*rule['selection_threshold'])
 selected=[j*p+aa for aa in range(p) for j in range(57 if aa==36 else 51)]
 assert len(selected)==r
 controls=[];start=time.monotonic()
 with tempfile.TemporaryDirectory(prefix='ud-full-H-controls-') as tmp:
  Y=np.memmap(Path(tmp)/'synthetic.i64le',dtype='<i8',mode='w+',shape=(p,2*M-1,c))
  for aa in range(p):Y[aa,56 if aa==36 else 50,aa]=data_den
  for label,w in [('clean_rank1893',F(0)),('weak_extra_rank1',F(1,2**19)),('strong_extra_rank1',F(1,2**14))]:
   Y[0,:,37]=int(w*data_den)
   H=HankelRecord(Y,data_den);cores=H.selector_cores(selected)
   cert=certify(H.energy(),*cores,r,T)
   # Independent analytic spectrum: d repeatedr-1, plus two roots of a2x2 pencil.
   d2=F(1,M*M);alpha=F(51,M)
   if w:
    discriminant=a((d2-w*w)**2+4*d2*w*w*alpha).sqrt()
    minus=(a(d2+w*w)-discriminant)/2;plus=(a(d2+w*w)+discriminant)/2
    true_tail=minus.sqrt()
    actual_above=r+int(true_tail>a(T))
   else:minus=a(0);plus=a(d2);true_tail=a(0);actual_above=r
   expected='HOLD' if label=='strong_extra_rank1' else 'CERTIFIED_NUMERIC_RECORD_SIGNATURE'
   assert cert['status']==expected
   assert (actual_above==r)==(cert['count_above_threshold_certified']==r)
   assert true_tail<=a(F(*cert['sigma_r_plus1_upper_squared'])).sqrt()
   assert plus<=a(F(*cert['sigma_1_upper_squared']))
   assert a(d2)>=a(F(*cert['sigma_r_lower_squared']))
   controls.append({'label':label,'kind':'CONSTRUCTED_NON_UD_NUMERIC_CONTROL','shape':[M*c,M*p],
    'nonzero_impulse_rank':r,'constant_extra_amplitude':pair(w),'actual_algebraic_rank':r+int(bool(w)),
    'analytic_count_above_frozen_threshold':actual_above,'analytic_sigma_r_plus1':str(true_tail),
    'certificate':cert})
  # Exact full-size action on a vector spanning all preparations. No denseH used.
  Y[0,:,37]=0;x=np.ones(H.cols,dtype=np.int64);vals,den=H.action(x)
  direct=np.zeros(H.rows,dtype=np.int64)
  for aa in range(p):
   q=56 if aa==36 else 50
   for i in range(q+1):direct[i*c+aa]=data_den
  assert all(int(v)==int(z) for v,z in zip(vals,direct)) and den==M*data_den
  # A dense separable record exercises every preparation/channel polynomial.
  # Independent sums close both actions without constructing any denseH.
  k=np.arange(1,2*M,dtype=np.int64)
  for aa in range(p):
   for cc in range(c):Y[aa,:,cc]=(aa+1)*(cc+1)*k
  x=np.array([(j+1)*(aa+1) for j in range(M) for aa in range(p)],dtype=np.int64)
  y=np.array([(i+1)*(cc+1) for i in range(M) for cc in range(c)],dtype=np.int64)
  sx=M*(M+1)//2;sj=M*(M-1)*(M+1)//3
  aa2=p*(p+1)*(2*p+1)//6;cc2=c*(c+1)*(2*c+1)//6
  hx,_=H.action(x);hty,_=H.action(y,True)
  assert all(int(hx[i*c+cc])==(cc+1)*aa2*((i+1)*sx+sj) for i in range(M) for cc in range(c))
  assert all(int(hty[j*p+aa])==(aa+1)*cc2*((j+1)*sx+sj) for j in range(M) for aa in range(p))
 out={'status':'PASS','physical_promotion':0,'independent_review':'pending',
  'scope':'Three constructed full-dimension numeric spectra, not nominal600-cell evolution or apparatus data',
  'controls':controls,'full_size_exact_polynomial_action_checked':True,
  'full_size_dense_record_action_and_adjoint_checked':True,
  'dense_Hankel_allocated':False,'history_file_bytes':p*(2*M-1)*c*8,
  'candidate_storage':'1893 implicit coordinate selectors in these controls',
  'runtime_seconds_display_only':time.monotonic()-start,
  'process_peak_RSS_KiB_display_only':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
 # Runtime/RSS are operational logs, separated to keep mathematical replay deterministic.
 perf={k:out.pop(k) for k in ['runtime_seconds_display_only','process_peak_RSS_KiB_display_only']}
 (ROOT/'FULL_SIZE_CONTROLS.json').write_text(json.dumps(out,indent=2)+'\n')
 (ROOT/'CONTROL_PERFORMANCE.json').write_text(json.dumps(perf,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='controls'}));print(json.dumps(perf))
 return out
if __name__=='__main__':build()
