"""Exact encoded-record sketch Grams. No floating BLAS result is assumed exact."""
import argparse,json,time
from pathlib import Path
import numpy as np
from bindings import P,freeze,sha
from model import sketch
from proof_math import fm,arr

def project(case,root):
 f=freeze();e=next(e for e in f['cases'] if e['case']==case);raw=Path(root)/f'{case}.i64le';assert raw.stat().st_size==150321232 and sha(raw)==e['record_sha256'];t=time.monotonic()
 Y=np.memmap(raw,dtype='<i8',mode='r',shape=(37,8191,62));X=np.array(Y.transpose(1,2,0).reshape(8191,2294),np.int64);A=sketch()
 maxraw=max(abs(int(X.min())),abs(int(X.max())));l1=max(sum(abs(int(x)) for x in A[:,j]) for j in range(321));assert maxraw*l1<2**63
 N=X@A;G=arr(fm(N).transpose()*fm(N));assert sha(raw)==e['record_sha256']
 receipt={'case':case,'record_sha256':e['record_sha256'],'encoded_readings_projected':18790154,'integer_partial_sum_bound':maxraw*l1,'shape':[321,321],'scale_bits':110,'exact_integer_projection':True,'actual_BLAS_sketch_rounding_verified':False,'physical_promotion':0}
 return G,receipt,time.monotonic()-t
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('case');p.add_argument('--records',required=True);p.add_argument('--replay',action='store_true');a=p.parse_args();g,r,seconds=project(a.case,a.records);o=P/'results'/a.case;o.mkdir(exist_ok=True)
 if a.replay:
  with np.load(o/'GRAM.npz',allow_pickle=False) as z:old=z['integers_decimal']
  assert np.array_equal(old,np.array(g,dtype=str));assert json.loads((o/'PROJECTION.json').read_text())==r
  dest=o/'PROJECTION_REPLAY.json';assert not dest.exists();dest.write_text(json.dumps({'status':'PASS_IDENTICAL_EXACT_RAW_GRAM','receipt':r,'seconds':seconds},indent=2))
 else:
  assert not (o/'GRAM.npz').exists();np.savez_compressed(o/'GRAM.npz',integers_decimal=np.array(g,dtype=str));(o/'PROJECTION.json').write_text(json.dumps(r,indent=2))
 print(json.dumps({'case':a.case,'stage':'exact_raw_Gram_replay' if a.replay else 'exact_raw_Gram','seconds':seconds}),flush=True)
