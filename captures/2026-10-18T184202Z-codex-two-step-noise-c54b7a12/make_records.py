import json,argparse,time
from pathlib import Path
import numpy as np
from bindings import P,freeze,sha
from sketch import sketch
from noise_math import signs
from proof_math import fm,arr
SHAPE=(37,8191,62)

def generate(destination=None):
 f=freeze();base=P.parent/'floating-timing-work/records/ramp_clock_stress.i64le';assert sha(base)==f['baseline_sha256'];dest=P/'records' if destination is None else Path(destination)
 if destination is not None:dest.mkdir(parents=True,exist_ok=False)
 Y=np.memmap(base,dtype='<i8',mode='r',shape=SHAPE);A=sketch();rows=[]
 for mode in ['dense_sign','coherent_dc']:
  pattern=signs(mode);X=np.array(pattern.transpose(1,2,0).reshape(8191,2294),np.int64);assert max(sum(abs(int(x)) for x in A[:,j]) for j in range(321))<2**63;N=X@A;G=arr(fm(N).transpose()*fm(N));gp=(P/f'NOISE_GRAM_{mode}.npz') if destination is None else dest/f'NOISE_GRAM_{mode}.npz';np.savez_compressed(gp,integers_decimal=np.array(G,dtype=str));del X,N
  for e in [e for e in f['cases'] if e['mode']==mode]:
   n=e['case'];amp=e['integer_amplitude'];path=dest/f'{n}.i64le';assert not path.exists()
   with path.open('xb') as out:out.truncate(150321232)
   Z=np.memmap(path,dtype='<i8',mode='r+',shape=SHAPE);Z[:]=Y+amp*pattern;Z.flush();del Z
   Z=np.memmap(path,dtype='<i8',mode='r',shape=SHAPE);maximum=0;peak=0;count=0
   for k in range(0,8191,256):
    a=Y[:,k:k+256,:];b=Z[:,k:k+256,:];assert max(abs(int(a.min())),abs(int(a.max())),abs(int(b.min())),abs(int(b.max())))<2**61
    diff=b-a;assert np.array_equal(diff,amp*pattern[:,k:k+256,:]);maximum=max(maximum,max(abs(int(diff.min())),abs(int(diff.max()))));sq=np.sum(diff*diff,axis=-1,dtype=np.int64);peak=max(peak,int(sq.max()));count+=diff.size
   assert count==18790154 and maximum==amp and peak==62*amp*amp and peak<2**63
   r={'case':n,'mode':mode,'integer_amplitude':amp,'record_sha256':sha(path),'bytes':path.stat().st_size,'all_raw_noise_readings_checked':count,'max_scalar_integer_error':maximum,'max_vector_integer_squared_error':peak,'vector_noise_squared':[peak,1<<96],'per_vector_2neg20_met':peak<=1<<56,'sufficient_scalar_2neg23_met':maximum<=1<<25,'unit_noise_Gram_sha256':sha(gp),'pattern_time_constant':mode=='coherent_dc','error_reference':'Encoded PR195 stress record, not original nominal clean record'};rows.append(r);print(json.dumps(r),flush=True);del Z
  del pattern,G
 assert sha(base)==f['baseline_sha256']
 if destination is None:
  target=P/'DATA_FREEZE.json';assert not target.exists();target.write_text(json.dumps({'status':'ALL_NOISY_RECORD_HASHES_AND_EXACT_GATES_FROZEN_BEFORE_FITTING','noise_freeze_sha256':sha(P/'NOISE_FREEZE.json'),'baseline_sha256':f['baseline_sha256'],'physical_promotion':0,'records':rows},indent=2))
 else:
  old=json.loads((P/'DATA_FREEZE.json').read_text());assert rows==old['records'];(dest/'RAW_REGENERATION_RECEIPT.json').write_text(json.dumps({'status':'PASS_ALL_RAW_HASHES_AND_NOISE_GRAMS_IDENTICAL','records':rows,'physical_promotion':0},indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--destination');a=p.parse_args();generate(a.destination)
