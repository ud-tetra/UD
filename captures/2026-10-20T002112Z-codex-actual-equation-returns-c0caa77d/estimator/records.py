"""Exact encoded top1/top2 recipes, no floating state estimation."""
import hashlib,json
from pathlib import Path
import numpy as np
from common import P,sha,freeze
SHAPE=(37,8191,62)
def recipes():
 source=json.loads((P/'inputs/QUALITY_SOURCE.json').read_text())
 return source['rows']
def weights(count):
 v=np.pad(np.array(json.loads((P/'inputs/NULL_VECTOR.json').read_text())['vector'],np.int64),(0,1974));w=np.zeros(2294,np.int64);selected=[]
 for prep in range(37):
  channels=sorted(range(62),key=lambda c:(-abs(int(v[37*c+prep])),c))[:count]
  for c in channels:w[37*c+prep]=1 if int(v[37*c+prep])>=0 else -1
  selected.append(channels)
 return w,selected

def generate(baseline,path,source):
 freeze();path=Path(path)
 if path.exists():raise RuntimeError('HOLD raw path exists')
 assert source['id'] in ['null_top1_alternating','null_top2_alternating']
 count=1 if source['id']=='null_top1_alternating' else 2
 w,selected=weights(count);assert selected==source['selected_channels_by_preparation'];assert hashlib.sha256(w.astype('<i8').tobytes()).hexdigest()==source['w_int64le_sha256']
 assert sha(baseline)==source['baseline_sha256'] and Path(baseline).stat().st_size==37*8191*62*8
 Y=np.memmap(baseline,dtype='<i8',mode='r',shape=SHAPE);u=np.where(np.arange(8191)%2==0,1,-1).astype(np.int64);readings=0;vectors=0;changed=0;minimum=None;maximum=None
 with path.open('xb') as out:
  for prep in range(37):
   original=np.array(Y[prep],dtype='<i8',copy=True);assert int(original.min())>-(1<<63) and int(original.max())<(1<<63)-1
   delta=u[:,None]*w.reshape(62,37)[:,prep][None,:]
   record=original+delta
   assert np.all(record.astype(object)-original.astype(object)==delta.astype(object))
   norms=np.sum(delta*delta,axis=1);assert np.all(norms==count) and 4*count<=9
   readings+=record.size;vectors+=len(norms);changed+=int(np.count_nonzero(delta));minimum=int(record.min()) if minimum is None else min(minimum,int(record.min()));maximum=int(record.max()) if maximum is None else max(maximum,int(record.max()));out.write(record.astype('<i8').tobytes())
 del Y
 h=sha(path);assert h==source['raw_int64le_sha256']
 return {'case':source['id'],'record_sha256':h,'baseline_sha256':source['baseline_sha256'],'raw_bytes':path.stat().st_size,'readings_checked':readings,'vectors_checked':vectors,'integer_vector_squared_norm':count,'changed_scalars':changed,'radius_upper':[3,1<<49],'integer_min':minimum,'integer_max':maximum,'w_sha256':source['w_int64le_sha256']}
