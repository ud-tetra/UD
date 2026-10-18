"""Fresh deterministic cyclic one-channel quantum, frozen before generation."""
import json,argparse
from pathlib import Path
import numpy as np
from bindings import P,freeze,sha
parser=argparse.ArgumentParser();parser.add_argument('--regenerate');args=parser.parse_args()
f=freeze();base=P.parent/'floating-timing-work/records/ramp_clock_stress.i64le';assert sha(base)==f['baseline_sha256'];raw=(P/'records/cyclic_unit.i64le') if args.regenerate is None else Path(args.regenerate);raw.parent.mkdir(parents=True,exist_ok=True);assert not raw.exists();Y=np.memmap(base,dtype='<i8',mode='r',shape=(37,8191,62))
with raw.open('xb') as s:s.truncate(150321232)
Z=np.memmap(raw,dtype='<i8',mode='r+',shape=Y.shape);Z[:]=Y;t=np.arange(8191)
for a in range(37):Z[a,t,(a+t)%62]+=1-2*((a+t//62)%2)
Z.flush();del Z;Z=np.memmap(raw,dtype='<i8',mode='r',shape=Y.shape);count=0
for k in range(0,8191,256):
 d=Z[:,k:k+256,:]-Y[:,k:k+256,:];expected=np.zeros_like(d);tt=np.arange(k,min(k+256,8191))
 for a in range(37):expected[a,np.arange(len(tt)),(a+tt)%62]=1-2*((a+tt//62)%2)
 assert np.array_equal(d,expected) and np.all(np.sum(d*d,axis=-1)==1);count+=d.size
assert count==18790154 and sha(base)==f['baseline_sha256'];row={'case':'cyclic_unit','record_sha256':sha(raw),'bytes':150321232,'readings_checked':count,'nonzero_noise_readings':37*8191,'max_vector_integer_squared_error':1,'vector_noise_squared':[1,1<<96],'scalar_gate_2neg23_met':True,'vector_gate_2neg20_met':True,'error_reference':'Encoded PR195 stress baseline, not nominal clean record'}
target=P/'DATA_FREEZE.json'
if args.regenerate is not None:
 assert json.loads(target.read_text())['records']==[row]
 (raw.parent/'RAW_NOISE_REGENERATION.json').write_text(json.dumps({'status':'PASS_IDENTICAL_RAW_NOISE_AND_ALL_GATES','record':row,'physical_promotion':0},indent=2))
else:
 assert not target.exists()
 target.write_text(json.dumps({'status':'RAW_HASH_AND_ALL_DIFFERENCES_FROZEN_BEFORE_FITTING','protocol_freeze_sha256':sha(P/'PROTOCOL_FREEZE.json'),'baseline_sha256':f['baseline_sha256'],'records':[row],'physical_promotion':0},indent=2));print(json.dumps(row),flush=True)
