"""Frozen integer one-coordinate-per-vector patterns; no estimator calls."""
from pathlib import Path
import json
import numpy as np
from common import P,CASE,sha,need,freeze
BASELINE='25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59'
def pattern(prep,times):
 t=np.asarray(times,dtype=np.int64)
 if CASE=='block257_port17':c=np.full(t.shape,17,dtype=np.int64);s=np.where((prep+t//257)%2==0,1,-1)
 elif CASE=='affine62_qr13':c=(7*prep+11*t+5)%62;s=np.where(np.isin((t+3*prep)%13,[0,1,3,4,9,10,12]),1,-1)
 elif CASE=='prep_port_period7':c=np.full(t.shape,(13*prep+9)%62,dtype=np.int64);s=np.array([1,1,-1,1,-1,-1,-1],np.int64)[(t+2*prep)%7]
 else:raise ValueError('unknown frozen case')
 return c,s.astype(np.int64)
def make(baseline,path):
 freeze();path=Path(path);need(not path.exists(),'one raw output only');need(sha(baseline)==BASELINE and Path(baseline).stat().st_size==150321232,'pinned baseline');Y=np.memmap(baseline,dtype='<i8',mode='r',shape=(37,8191,62));readings=vectors=changed=0;low=None;high=None;t=np.arange(8191)
 with path.open('xb')as out:
  for prep in range(37):
   old=np.array(Y[prep],dtype='<i8',copy=True);need(int(old.min())>-(1<<63)and int(old.max())<(1<<63)-1,'raw overflow margin');c,s=pattern(prep,t);need(np.all((0<=c)&(c<62)) and np.all(np.abs(s)==1),'pattern range');delta=np.zeros_like(old);delta[t,c]=s;new=old+delta;need(np.all(new.astype(object)-old.astype(object)==delta.astype(object)),'all scalar differences');need(np.all(np.sum(delta*delta,axis=1)==1),'all exact unit vector norms');readings+=new.size;vectors+=len(new);changed+=int(np.count_nonzero(delta));low=int(new.min())if low is None else min(low,int(new.min()));high=int(new.max())if high is None else max(high,int(new.max()));out.write(new.astype('<i8').tobytes())
 del Y;path.chmod(0o444)
 return {'case':CASE,'record_sha256':sha(path),'baseline_sha256':BASELINE,'raw_bytes':path.stat().st_size,'readings_checked':readings,'vectors_checked':vectors,'changed_scalars':changed,'integer_vector_squared_norm':1,'noise_radius_exact_squared':[1,1<<96],'profile_noise_radius':[3,1<<49],'quantum':[1,1<<48],'integer_min':low,'integer_max':high,'recipe_sha256':sha(P/'RECIPE.json')}
