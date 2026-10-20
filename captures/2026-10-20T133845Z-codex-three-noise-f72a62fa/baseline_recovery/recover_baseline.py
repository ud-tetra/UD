"""Reviewed PR195 formulas, baseline-only recovery; no estimator imports or calls."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,time,platform
import numpy as np
import flint
from flint import arb,acb,fmpq,fmpz_mat,ctx
ctx.prec=512
P=Path(__file__).resolve().parent
def nearest(n,s):
 q,r=divmod(int(n),1<<s);half=1<<(s-1);return q+int(r>half or(r==half and q%2))
def fm(a):return fmpz_mat(a.tolist())
def arr(a):return np.array(a.tolist(),dtype=object)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as z:
  for b in iter(lambda:z.read(1048576),b''):h.update(b)
 return h.hexdigest()
BITS=96;Q=1<<BITS;SHAPE=(37,8191,62)
def rounded(n,bits):return nearest(int(n),bits)
def mul(z,w):return (rounded(z[0]*w[0]-z[1]*w[1],BITS),rounded(z[0]*w[1]+z[1]*w[0],BITS))
def phase(theta,t):
 t=F(t);angle=arb(int(theta))*arb(fmpq(t.numerator,t.denominator))/(1<<60);z=acb(0,angle).exp();r=[]
 for v in [z.real,z.imag]:
  # Unique nearest integer, including all interval uncertainty.
  n=(v*Q).mid().unique_fmpz()
  if n is None:n=int((v*Q).mid().floor().unique_fmpz())
  else:n=int(n)
  # Either n or its nearest adjacent integer; this is only proposal selection.
  opts=[n-1,n,n+1];valid=[x for x in opts if abs(v-arb(x)/Q)<=arb(1)/Q]
  assert valid,'HOLD: anchor rounding error not enclosed'
  r.append(min(valid,key=lambda x:float(abs(v-arb(x)/Q).mid())))
 return tuple(r)
def timing(e,a,k):
 s=1 if a%2==0 else -1
 if e['origin']=='zero':o=F(0)
 elif e['origin']=='alternating_quarter':o=F(s,4)
 elif e['origin']=='ramp_half':o=F(a-18,36)
 else:raise AssertionError('Unknown origin recipe')
 eps=s*F(*e['rate']);u=s*(1 if k%2==0 else -1)*F(*e['jitter'])
 return o,eps,u

def phase_matrix(theta,e,a,count=8191):
 o,eps,_=timing(e,a,0);out=np.empty((count,105),np.int64);out[:,0]=1<<60
 for j,t in enumerate(theta):
  cur=phase(t,o);step=phase(t,1+eps);jp=phase(t,timing(e,a,0)[2]);jm=phase(t,timing(e,a,1)[2])
  for k in range(count):
   z=mul(cur,jp if k%2==0 else jm);out[k,2*j+1]=rounded(z[0],36);out[k,2*j+2]=rounded(z[1],36);cur=mul(cur,step)
 return out

def evaluation_bounds(B):
 # Each phase component differs from exact waveform by <2^-60.
 # The exact coefficient contraction is rounded once to raw2^-48.
 max_l1=max(sum(abs(int(x)) for x in B[1:,c]) for c in range(B.shape[1]))
 scalar=F(max_l1,1<<120)+F(1,1<<49)
 return {'phase_component_error_strict_upper':[1,1<<60],'max_oscillatory_coefficient_integer_l1':max_l1,'scalar_waveform_error_upper':[scalar.numerator,scalar.denominator],'vector_waveform_error_squared_upper':[62*scalar.numerator**2,scalar.denominator**2],'original_clean_residual_inherited':False,'exact_source_contraction_and_final_quantization':True}

def main():
 start=time.monotonic();f=json.loads((P/'RECOVERY_FREEZE.json').read_text());repo=P.parent/'ud-repo'
 for n,h in f['repository_sources'].items():assert sha(repo/n)==h,n
 assert sha(__file__)==f['recovery_source_sha256']
 assert sha(P/'REFERENCE_PROPOSAL.npz')==f['reference_proposal_sha256']
 e=f['expected_original_generation_row']['recipe'];path=P/'ramp_clock_stress.i64le'
 with np.load(P/'REFERENCE_PROPOSAL.npz',allow_pickle=False)as z:theta=z['theta'];B=z['coeff']
 assert B.shape==(105,2294);bounds=evaluation_bounds(B);maximum=0;readings=0
 with path.open('xb')as z:z.truncate(150321232)
 Y=np.memmap(path,dtype='<i8',mode='r+',shape=SHAPE)
 for a in range(37):
  ph=phase_matrix(theta,e,a);cols=np.arange(a,2294,37);products=arr(fm(ph)*fm(B[:,cols]));raw=np.array([nearest(int(v),72)for v in products.flat],np.int64).reshape(8191,62)
  Y[a]=raw;maximum=max(maximum,max(abs(int(raw.min())),abs(int(raw.max()))));readings+=raw.size
  print(json.dumps({'preparation':a,'readings_generated':readings}),flush=True)
 Y.flush();del Y;assert readings==18790154 and maximum<2**61
 Y=np.memmap(path,dtype='<i8',mode='r',shape=SHAPE);assert np.all(np.abs(Y)<2**61);del Y
 row={'case':e['case'],'record_sha256':sha(path),'bytes':path.stat().st_size,'encoded_readings_checked':readings,'max_absolute_raw_integer':maximum,'timing_model_membership':'VALIDATED_WAVEFORM_ERROR_BOUND','recipe':e,'evaluation_bounds':bounds,'additive_to_old_clean_gate_claimed':False}
 assert row==f['expected_original_generation_row'],'HOLD baseline differs from source'
 path.chmod(0o444)
 result={'status':'PASS_EXACT_BASELINE_RECOVERY','recovery_freeze_sha256':sha(P/'RECOVERY_FREEZE.json'),'original_generation_row':row,'source_record_hash_matches':True,'new_estimator_calls':0,'source_aware_computational_only':True,'physical_promotion':0,'external_promotion_review':'PENDING','versions':{'python':platform.python_version(),'numpy':np.__version__,'python_flint':flint.__version__},'elapsed_seconds':time.monotonic()-start}
 with(P/'RECOVERY_RECEIPT.json').open('x')as z:json.dump(result,z,indent=2);z.write('\n')
 print(json.dumps(result),flush=True)
if __name__=='__main__':main()
