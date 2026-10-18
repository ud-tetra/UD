"""Exact encoded-baseline cross-Grams; floating factors are untrusted proposals."""
import argparse,json,time
from pathlib import Path
import numpy as np
from bindings import P,freeze,sha
from sketch import sketch
from numeric_math import encode
from proof_math import fm,arr

def source(replay=False):
 f=freeze();raw=P.parent/'floating-timing-work/records/ramp_clock_stress.i64le';assert sha(raw)==f['baseline_sha256'] and raw.stat().st_size==150321232
 with np.load(P/'inputs/BASE_BASIS_A.npz',allow_pickle=False) as z:ua=z['basis']
 with np.load(P/'inputs/BASE_BASIS_B.npz',allow_pickle=False) as z:ub=z['basis']
 U=np.r_[ua,ub];un,bu=encode(U);assert U.shape==(8191,209)
 Y=np.memmap(raw,dtype='<i8',mode='r',shape=(37,8191,62));X=np.array(Y.transpose(1,2,0).reshape(8191,2294),np.int64);A=sketch();maxraw=max(abs(int(X.min())),abs(int(X.max())));l1=max(sum(abs(int(v)) for v in A[:,j]) for j in range(321));assert maxraw*l1<2**63
 N=X@A;del X;bn2=sum(int(v)**2 for v in N.flat);uf=fm(un);G=arr(uf.transpose()*uf);H=arr(uf.transpose()*fm(N));SG=A.T@A
 assert sha(raw)==f['baseline_sha256'];receipt={'record_sha256':sha(raw),'readings_projected':18790154,'int64_partial_sum_bound':maxraw*l1,'raw_sketch_scale_bits':55,'basis_scale_bits':bu,'raw_sketch_norm_squared_integer':str(bn2),'physical_promotion':0,'actual_BLAS_is_not_assumed_exact':True}
 out=P/'baseline';out.mkdir(exist_ok=True)
 if replay:
  with np.load(out/'EXACT_GRAMS.npz',allow_pickle=False) as z:
   assert np.array_equal(z['basis_gram_decimal'],np.array(G,dtype=str)) and np.array_equal(z['cross_gram_decimal'],np.array(H,dtype=str)) and np.array_equal(z['sketch_gram'],SG)
  assert json.loads((out/'PROJECTION.json').read_text())==receipt
  (P/'RAW_SOURCE_REPLAY.json').write_text(json.dumps({'status':'PASS_IDENTICAL_EXACT_BASELINE_GRAMS_AND_NORM','receipt':receipt,'physical_promotion':0},indent=2))
 else:
  assert not (out/'EXACT_GRAMS.npz').exists();np.savez_compressed(out/'EXACT_GRAMS.npz',basis_gram_decimal=np.array(G,dtype=str),cross_gram_decimal=np.array(H,dtype=str),sketch_gram=SG)
  C=U.T@(N.astype(float)/2.**55);np.savez_compressed(out/'COEFFICIENT_PROPOSAL.npz',coefficient=C)
  (out/'PROJECTION.json').write_text(json.dumps(receipt,indent=2))
 print(json.dumps({'status':'BASELINE_SOURCE_REPLAY_PASS' if replay else 'EXACT_BASELINE_GRAMS_GENERATED','physical_promotion':0}),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--raw-replay',action='store_true');a=p.parse_args();source(a.raw_replay)
