"""All-readings eligibility and exact raw-projected SKETCH Grams."""
import argparse,json
from pathlib import Path
import numpy as np
from scipy.linalg import svd
from bindings import P,sha,freeze,entry,basis
from sketch import sketch
from numeric_math import encode
from proof_math import fm,arr

def eligibility(n,replay=False):
 f=freeze();e=entry(n);base=P.parent/f['baseline_path'];raw=P.parent/e['raw_path'];assert sha(base)==f['baseline_sha256'] and sha(raw)==e['record_sha256'] and raw.stat().st_size==150321232
 Y=np.memmap(base,dtype='<i8',mode='r',shape=(37,8191,62));Z=np.memmap(raw,dtype='<i8',mode='r',shape=Y.shape);count=0;peak=0;large=False
 for k in range(0,8191,256):
  y=Y[:,k:k+256];z=Z[:,k:k+256];assert max(abs(int(y.min())),abs(int(y.max())),abs(int(z.min())),abs(int(z.max())))<2**61;d=z-y;mx=max(abs(int(d.min())),abs(int(d.max())))
  if mx>1<<25:large=True
  else:peak=max(peak,int(np.sum(d*d,axis=-1,dtype=np.int64).max()))
  count+=d.size
 assert count==18790154 and sha(base)==f['baseline_sha256'] and sha(raw)==e['record_sha256'];passed=not large and peak<=1
 result={'case':n,'status':'RAW_BALL_ELIGIBLE' if passed else 'HOLD_RAW_NOISE_BALL','record_sha256':sha(raw),'baseline_sha256':sha(base),'readings_checked':count,'max_vector_integer_squared_error':None if large else peak,'vector_error_scale_squared':1<<96,'noise_budget':[1,1<<48],'error_reference':'Encoded PR195 stress record','physical_promotion':0,'not_a_phase_failure_claim':not passed,'replay':replay};o=P/'results'/n;o.mkdir(exist_ok=True);dest=o/('RAW_REPLAY.json' if replay else 'RAW_ELIGIBILITY.json');assert not dest.exists();dest.write_text(json.dumps(result,indent=2));return passed

def project(n,replay=False):
 f=freeze();e=entry(n);raw=P.parent/e['raw_path'];assert sha(raw)==e['record_sha256'];U=basis(n);U0=basis('baseline');un,bu=encode(U);u0,b0=encode(U0);assert U.shape==(8191,209)
 Y=np.memmap(raw,dtype='<i8',mode='r',shape=(37,8191,62));X=np.array(Y.transpose(1,2,0).reshape(8191,2294),np.int64);A=sketch();mx=max(abs(int(X.min())),abs(int(X.max())));l1=max(sum(abs(int(v)) for v in A[:,j]) for j in range(321));assert mx*l1<2**63;N=X@A;del X
 uf=fm(un);G=arr(uf.transpose()*uf);H=G if n=='baseline' else arr(uf.transpose()*fm(u0));K=arr(uf.transpose()*fm(N));bn2=sum(int(v)**2 for v in N.flat);o=P/'results'/n
 receipt={'case':n,'record_sha256':sha(raw),'readings_projected':18790154,'basis_bits':bu,'reference_basis_bits':b0,'sketch_bits':55,'sketch_norm_squared_integer':str(bn2),'int64_partial_sum_bound':mx*l1,'physical_promotion':0};assert sha(raw)==e['record_sha256']
 if replay:
  with np.load(o/'EXACT_GRAMS.npz',allow_pickle=False) as z:
   for key,x in [('basis',G),('reference_cross',H),('sketch_cross',K)]:assert np.array_equal(z[key],np.array(x,dtype=str))
  assert json.loads((o/'PROJECTION.json').read_text())==receipt
  (o/'PROJECTION_REPLAY.json').write_text(json.dumps({'status':'PASS_IDENTICAL_EXACT_SKETCH_GRAMS','receipt':receipt},indent=2))
 else:
  assert not (o/'EXACT_GRAMS.npz').exists();np.savez_compressed(o/'EXACT_GRAMS.npz',basis=np.array(G,dtype=str),reference_cross=np.array(H,dtype=str),sketch_cross=np.array(K,dtype=str));(o/'PROJECTION.json').write_text(json.dumps(receipt,indent=2))
  C=U.T@(N.astype(float)/2.**55);l,s,rt=svd(U.T@U0,check_finite=False);O=l@rt;np.savez_compressed(o/'PROPOSALS.npz',coefficient=C,alignment=O)
 print(json.dumps({'case':n,'exact_sketch_projected':True,'replay':replay}),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--raw-replay',action='store_true');a=p.parse_args()
 for e in freeze()['cases']:
  if eligibility(e['case'],a.raw_replay):project(e['case'],a.raw_replay)
