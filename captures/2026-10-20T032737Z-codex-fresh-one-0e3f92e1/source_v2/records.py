"""One fixed sign-negation recipe; generation requires separate root release."""
from pathlib import Path
import json,hashlib
import numpy as np
from common import P,CASE,sha,need,freeze
BASELINE='25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59'
def weights():
 v=np.pad(np.array(json.loads((P/'inputs/NULL_VECTOR.json').read_text())['vector'],np.int64),(0,1974));w=np.zeros(2294,np.int64);chosen=[]
 for prep in range(37):
  c=min(range(62),key=lambda c:(-abs(int(v[37*c+prep])),c));w[37*c+prep]=-1 if int(v[37*c+prep])>=0 else 1;chosen.append(c)
 return w,chosen

def make(baseline,path):
 freeze();path=Path(path);need(not path.exists(),'one raw output only');recipe=json.loads((P/'RECIPE.json').read_text());w,chosen=weights();need(chosen==recipe['selected_channel_by_preparation']and hashlib.sha256(w.astype('<i8').tobytes()).hexdigest()==recipe['negated_w_int64le_sha256'],'frozen recipe');need(sha(baseline)==BASELINE and Path(baseline).stat().st_size==150321232,'pinned baseline')
 Y=np.memmap(baseline,dtype='<i8',mode='r',shape=(37,8191,62));u=np.where(np.arange(8191)%2==0,1,-1).astype(np.int64);readings=vectors=changed=0;low=None;high=None
 with path.open('xb')as out:
  for prep in range(37):
   old=np.array(Y[prep],dtype='<i8',copy=True);need(int(old.min())>-(1<<63)and int(old.max())<(1<<63)-1,'raw overflow margin');delta=u[:,None]*w.reshape(62,37)[:,prep][None,:];new=old+delta;need(np.all(new.astype(object)-old.astype(object)==delta.astype(object)),'all scalar differences');need(np.all(np.sum(delta*delta,axis=1)==1),'all exact unit vector norms');readings+=new.size;vectors+=len(new);changed+=int(np.count_nonzero(delta));low=int(new.min())if low is None else min(low,int(new.min()));high=int(new.max())if high is None else max(high,int(new.max()));out.write(new.astype('<i8').tobytes())
 del Y;path.chmod(0o444)
 return {'case':CASE,'record_sha256':sha(path),'baseline_sha256':BASELINE,'raw_bytes':path.stat().st_size,'readings_checked':readings,'vectors_checked':vectors,'changed_scalars':changed,'integer_vector_squared_norm':1,'noise_radius_exact_squared':[1,1<<96],'profile_noise_radius':[3,1<<49],'quantum':[1,1<<48],'integer_min':low,'integer_max':high,'negated_w_sha256':recipe['negated_w_int64le_sha256'],'recipe_sha256':sha(P/'RECIPE.json')}
