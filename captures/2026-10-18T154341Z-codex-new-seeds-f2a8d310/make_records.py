"""Frozen deterministic encoded noise; verify every actual additive coordinate."""
from pathlib import Path
import json,time
import numpy as np
from bindings import P,sha,checked,check_freeze
S=(37,8191,62)
def block_metrics(d):
 m=max(abs(int(d.min())),abs(int(d.max())))
 if m<=2**27:squares=np.sum(d*d,axis=-1,dtype=np.int64)
 else:squares=np.sum(d.astype(object)**2,axis=-1)
 return m,int(squares.max())
def gates(base,record):
 scalar=0;peak=0;readings=0
 Y=np.memmap(base,dtype='<i8',mode='r',shape=S);Z=np.memmap(record,dtype='<i8',mode='r',shape=S)
 for k in range(0,8191,256):
  a=Y[:,k:k+256,:];b=Z[:,k:k+256,:]
  assert max(abs(int(a.min())),abs(int(a.max())),abs(int(b.min())),abs(int(b.max())))<2**61
  d=b-a;m,v=block_metrics(d);scalar=max(scalar,m);peak=max(peak,v);readings+=d.size
 assert readings==18790154
 return {'max_scalar_integer_error':scalar,'max_vector_integer_squared_error':peak,'per_vector_2neg20_met':peak<=2**56,'sufficient_scalar_2neg23_met':scalar<=2**25,'normalized_max_vector_squared_error':[peak,2**96],'all_scalar_differences_checked':readings}
def generate():
 start=time.monotonic();f=check_freeze();base=P/'records/BASELINE.i64le';checked(base,f['baseline_sha256']);Y=np.memmap(base,dtype='<i8',mode='r',shape=S);rows=[]
 for e in f['cases']:
  n=e['case'];path=P/f'records/{n}.i64le';assert not path.exists();rng=np.random.default_rng(e['seed']);amp=e['integer_amplitude']
  if e['mode']=='dense_sign':d=(rng.integers(0,2,size=S,dtype=np.int64)*2-1)*amp
  elif e['mode']=='block_sign':
   short=rng.integers(0,2,size=(37,(8191+511)//512,62),dtype=np.int64)*2-1;d=np.repeat(short,512,axis=1)[:,:8191,:]*amp
  elif e['mode']=='oversized_impulse':
   d=np.zeros(S,np.int64);d[:,4095,:]=(rng.integers(0,2,size=(37,62),dtype=np.int64)*2-1)*amp
  else:raise AssertionError('Unknown frozen recipe')
  z=np.memmap(path,dtype='<i8',mode='w+',shape=S);z[:]=Y+d;z.flush();del z,d
  r={'case':n,'mode':e['mode'],'seed':e['seed'],'record_sha256':sha(path),'bytes':path.stat().st_size,**gates(base,path)};rows.append(r);print(json.dumps(r),flush=True)
 checked(base,f['baseline_sha256']);dest=P/'DATA_FREEZE.json';assert not dest.exists();dest.write_text(json.dumps({'status':'ALL_FIVE_RECORDS_GENERATED_AND_FROZEN_BEFORE_FITTING','campaign_sha256':sha(P/'CAMPAIGN_FREEZE.json'),'baseline_sha256':f['baseline_sha256'],'physical_promotion':0,'records':rows,'seconds':time.monotonic()-start},indent=2))
if __name__=='__main__':generate()
