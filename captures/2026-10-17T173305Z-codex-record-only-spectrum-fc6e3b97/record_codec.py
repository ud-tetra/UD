#!/usr/bin/env python3
"""Lossless integer record codec. All deviations from the learned fit are retained."""
import argparse,time,json,hashlib
from pathlib import Path
import numpy as np
from flint import ctx,arb,acb
from proof_math import fm,arr,dyad,nearest
ctx.prec=512
SHAPE=(37,8191,62)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def blocks(proposal):
 with np.load(proposal,allow_pickle=False) as z:theta=z['theta'];coeff=z['coeff']
 cf=fm(coeff)
 for start in range(0,8191,128):
  count=min(128,8191-start);phase=np.ones((count,coeff.shape[0]),np.int64)*(1<<60)
  for j,v in enumerate(theta):
   theta_exact=arb(int(v))/(1<<60)
   for k in range(count):
    z=acb(0,(start+k)*theta_exact).exp();phase[k,2*j+1]=dyad(z.real);phase[k,2*j+2]=dyad(z.imag)
  products=arr(fm(phase)*cf);pred=np.array([nearest(v,72) for v in products.flat],np.int64).reshape(count,62,37).transpose(2,0,1)
  yield start,pred

def encode(raw,proposal,destination):
 t=time.monotonic();dst=Path(destination);dst.mkdir(exist_ok=False,parents=True);Y=np.memmap(raw,dtype='<i8',mode='r',shape=SHAPE);res=np.zeros(SHAPE,np.int16);maximum=0
 for start,pred in blocks(proposal):
  diff=Y[:,start:start+pred.shape[1],:].astype(object)-pred.astype(object);m=max(abs(int(v)) for v in diff.flat);maximum=max(maximum,m)
  if m>32767:raise ValueError('Lossless int16 codec range exceeded; do not clip or discard residuals')
  res[:,start:start+pred.shape[1],:]=diff.astype(np.int16)
 np.savez_compressed(dst/'LOSSLESS_RESIDUAL.npz',residual=res)
 # Proposal is a codec dictionary, not an assumption about the record: residuals are exact.
 import shutil;shutil.copy2(proposal,dst/'CODEC_DICTIONARY.npz')
 meta={'status':'LOSSLESS_ENCODED','raw_sha256':sha(raw),'raw_bytes':Path(raw).stat().st_size,'shape':list(SHAPE),'dtype':'<i8','quantum':[1,2**48],'dictionary_sha256':sha(dst/'CODEC_DICTIONARY.npz'),'residual_sha256':sha(dst/'LOSSLESS_RESIDUAL.npz'),'residual_dtype':'int16','maximum_absolute_integer_residual':maximum,'seconds':time.monotonic()-t,'range_error_behavior':'fail; never clip or omit'}
 (dst/'CODEC_MANIFEST.json').write_text(json.dumps(meta,indent=2));print(json.dumps(meta,indent=2));return meta

def restore(codec,destination):
 t=time.monotonic();codec=Path(codec);meta=json.loads((codec/'CODEC_MANIFEST.json').read_text());dictionary=codec/'CODEC_DICTIONARY.npz';residual=codec/'LOSSLESS_RESIDUAL.npz'
 assert sha(dictionary)==meta['dictionary_sha256'] and sha(residual)==meta['residual_sha256']
 with np.load(residual,allow_pickle=False) as z:res=z['residual']
 assert res.shape==SHAPE and res.dtype==np.int16
 out=Path(destination)
 with out.open('xb') as f:f.truncate(meta['raw_bytes'])
 Y=np.memmap(out,dtype='<i8',mode='r+',shape=SHAPE)
 for start,pred in blocks(dictionary):Y[:,start:start+pred.shape[1],:]=pred+res[:,start:start+pred.shape[1],:].astype(np.int64)
 Y.flush();del Y;digest=sha(out)
 if digest!=meta['raw_sha256']:raise ArithmeticError('Restored record hash mismatch; no certificate')
 result={'status':'PASS_LOSSLESS_RESTORATION','record_sha256':digest,'bytes':out.stat().st_size,'seconds':time.monotonic()-t};print(json.dumps(result,indent=2));return result
if __name__=='__main__':
 p=argparse.ArgumentParser();sub=p.add_subparsers(dest='command',required=True);s=sub.add_parser('encode');s.add_argument('record');s.add_argument('proposal');s.add_argument('output');s=sub.add_parser('restore');s.add_argument('codec');s.add_argument('output');a=p.parse_args()
 if a.command=='encode':encode(a.record,a.proposal,a.output)
 else:restore(a.codec,a.output)
