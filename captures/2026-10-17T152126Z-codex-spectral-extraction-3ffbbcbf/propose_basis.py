"""Optional untrusted numerical proposal. Only run_certificate.py can certify its result.

FFT actions and randomized block power iteration never allocate H. No proposal
convergence, random seed or floating QR is accepted as a spectral certificate.
"""
from pathlib import Path
import argparse,json,tempfile
import numpy as np
from scipy.fft import next_fast_len,rfft,irfft
from hankel_exact import HankelRecord,release_map,file_sha

class FloatActions:
 def __init__(self,record):
  self.h=record;self.length=next_fast_len(3*record.M-2);nf=self.length//2+1
  self.spectrum=np.empty((record.p,record.c,nf),dtype=np.complex128)
  for aa in range(record.p):
   self.spectrum[aa]=rfft(np.asarray(record.Y[aa,:,:].T,dtype=np.float64),n=self.length,axis=-1)/record.den
 def action(self,x,transpose=False):
  h=self.h;n_in=h.c if transpose else h.p;n_out=h.p if transpose else h.c
  x=np.asarray(x,dtype=np.float64).reshape(h.M,n_in)
  transformed=rfft(x[::-1,:].T,n=self.length,axis=-1)
  result=np.einsum('acf,cf->af',self.spectrum,transformed,optimize=True) if transpose else np.einsum('acf,af->cf',self.spectrum,transformed,optimize=True)
  values=irfft(result,n=self.length,axis=-1)[:,h.M-1:2*h.M-1]
  return values.T.reshape(-1)
 def block(self,x,transpose=False):return np.column_stack([self.action(x[:,j],transpose) for j in range(x.shape[1])])

def propose(record,rank,path,block_size=8,power_steps=3,seed=172026):
 if not 0<rank<=min(record.rows,record.cols):raise ValueError('Invalid target rank')
 path=Path(path)
 if path.exists():raise FileExistsError(path)
 path.parent.mkdir(parents=True,exist_ok=True);A=FloatActions(record);rng=np.random.default_rng(seed)
 with tempfile.TemporaryDirectory(prefix='ud-basis-proposal-',dir=path.parent) as tmp:
  basis=np.lib.format.open_memmap(Path(tmp)/'proposal.npy',dtype='<f8',mode='w+',shape=(record.cols,rank),fortran_order=True)
  def orth(q,count):
   for repeat in range(2):
    for start in range(0,count,32):
     V=basis[:,start:min(start+32,count)];q-=V@(V.T@q);release_map(basis)
   q,R=np.linalg.qr(q,mode='reduced')
   if not np.all(np.isfinite(q)) or min(abs(np.diag(R)))<1e-300:raise ArithmeticError('Proposal failed; HOLD, not a change of rank target')
   return q
  for start in range(0,rank,block_size):
   count=min(block_size,rank-start)
   q=orth(A.block(rng.standard_normal((record.rows,count)),True),start)
   for _ in range(power_steps):q=orth(A.block(A.block(q),True),start)
   basis[:,start:start+count]=q;basis.flush();release_map(basis)
  result=np.lib.format.open_memmap(path,dtype='<i8',mode='w+',shape=(record.cols,rank),fortran_order=True)
  for start in range(0,rank,8):
   q=basis[:,start:start+8]
   if np.max(np.abs(q))>1:raise ArithmeticError('Candidate range invalid; HOLD')
   result[:,start:start+8]=np.rint(q*2**60).astype(np.int64);release_map(basis)
  result.flush();release_map(result)
 return path

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('data');p.add_argument('output_candidate')
 p.add_argument('--contract',default=str(Path(__file__).resolve().parent/'sources'/'FROZEN_CONTRACT.json'));args=p.parse_args()
 c=json.loads(Path(args.contract).read_text());fmt=c['data_format']
 expected=json.loads((Path(__file__).resolve().parent/'sources'/'PARENT_FREEZE_CERTIFICATE.json').read_text())['protocol_sha256']
 if file_sha(args.contract)!=expected:raise ValueError('Frozen protocol hash mismatch')
 if Path(args.data).stat().st_size!=fmt['bytes']:raise ValueError('Incomplete record')
 Y=np.memmap(args.data,dtype=fmt['dtype'],mode='r',shape=tuple(fmt['shape']))
 H=HankelRecord(Y,fmt['scale'][1]);propose(H,c['spectral_rule']['target_count'],args.output_candidate)
 print(json.dumps({'status':'UNTRUSTED_NUMERICAL_PROPOSAL_ONLY','candidate':args.output_candidate,'spectral_certificate':False}))
