#!/usr/bin/env python3
"""Exact deterministic integer noise recipes. Each output is a complete encoded record."""
from pathlib import Path
import json,hashlib,shutil,time
import numpy as np
P=Path(__file__).resolve().parent;S=(37,8191,62);base=P.parent/'observer-work/inputs/normalized_history.i64le';Y=np.memmap(base,dtype='<i8',mode='r',shape=S);spec=json.loads((P/'CAMPAIGN_FREEZE.json').read_text());rows=[];start=time.monotonic()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(base)==spec['baseline_raw_sha256']
for name in spec['discovery_cases']:
 path=P/'records'/f'{name}.i64le'
 if path.exists():raise FileExistsError(path)
 if name=='clean':shutil.copyfile(base,path);peak=0
 else:
  d=np.zeros(S,np.int64)
  if name in ['single_vector','strong_rank_breach']:d[0,4095,0]=2**28 if name=='single_vector' else 2**48
  elif name=='dense_sign':
   rng=np.random.default_rng(spec['seeds'][name]);d=(rng.integers(0,2,size=S,dtype=np.int64)*2-1)*2**25
  else:
   rng=np.random.default_rng(spec['seeds'][name]);sgn=rng.integers(0,2,size=(37,62),dtype=np.int64)*2-1
   if name=='coherent_dc':d[:]=sgn[:,None,:]*2**25
   elif name=='ramp':
    # Floor rational ramp, retaining every integer point in [-2^25,2^25].
    ramp=(np.arange(8191,dtype=np.int64)*2*2**25)//8190-2**25;d[:]=sgn[:,None,:]*ramp[None,:,None]
   elif name=='weak_extra_tone':
    # Pure integer period127 triangular clock, not a float sine oracle.
    t=np.arange(8191,dtype=np.int64)%127;v=np.minimum(t,127-t);clock=(v*2*2**25)//63-2**25;d[:]=sgn[:,None,:]*clock[None,:,None]
  if name=='strong_rank_breach':peak=(2**48)**2
  else:peak=int(np.max(np.sum(d*d,axis=2,dtype=np.int64)))
  z=np.memmap(path,dtype='<i8',mode='w+',shape=S);z[:]=Y+d;z.flush();del z,d
 rows.append({'case':name,'sha256':sha(path),'bytes':path.stat().st_size,'max_vector_integer_squared_error':peak,'per_vector_budget_met':peak<=2**56,'normalized_max_vector_squared_error':[peak,2**96]});print(name,rows[-1],flush=True)
(P/'RECORD_MANIFEST.json').write_text(json.dumps({'status':'GENERATED','records':rows,'seconds':time.monotonic()-start,'campaign_sha256':sha(P/'CAMPAIGN_FREEZE.json')},indent=2))
