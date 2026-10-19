"""New nominal synthetic preparations and one-quantum perturbations, before any fit."""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from common import P,freeze,sha
SHAPE=(37,8191,62)
def transforms(kind,seed):
 M=np.zeros((37,37),np.int64);den=5 if kind=='rational_pair' else 1;rng=np.random.default_rng(seed)
 for parity in [0,1]:
  group=np.arange(parity,37,2);perm=np.roll(group,-1) if kind=='signed_cycle' else (rng.permutation(group) if kind=='signed_shuffle' else group)
  if kind=='rational_pair':
   for k in range(0,len(group)-1,2):
    i,j=map(int,group[k:k+2]);M[i,i]=M[j,j]=3;M[i,j]=-4;M[j,i]=4
   if len(group)%2:M[int(group[-1]),int(group[-1])]=5
  else:
   for i,b in zip(group,perm):M[i,b]=1 if (int(i)//2)%2==0 else -1
 assert np.array_equal(M@M.T,np.eye(37,dtype=np.int64)*den*den)
 assert all(i%2==j%2 for i,j in zip(*np.nonzero(M)))
 return M,den
def nominal(Y,M,den,j):
 active=np.flatnonzero(M[j]);v=sum((int(M[j,k])*np.array(Y[k],np.int64) for k in active),np.zeros((8191,62),np.int64))
 if den==1:return v
 assert den==5;q=v//5;rem=v-5*q;out=q+(rem>=3);assert np.max(np.abs(5*out-v))<=2
 return out
def model_bounds(kind):
 parent=json.loads((P/'inputs/BASE_GENERATION.json').read_text());r=next(x for x in parent['records'] if x['record_sha256']=='25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59');d0=F(*r['evaluation_bounds']['scalar_waveform_error_upper']);quantum=F(1,1<<48);dnom=F(7,5)*d0+F(2,5)*quantum if kind=='rational_pair' else d0;squared=62*dnom*dnom+2*dnom*quantum+quantum*quantum
 return {'inherited_scalar_source_error':[d0.numerator,d0.denominator],'fresh_nominal_scalar_source_error':[dnom.numerator,dnom.denominator],'fresh_vector_squared_source_error':[squared.numerator,squared.denominator],'scope':'Before-sketch temporal-family linearity plus encoded rounding; not original-baseline raw ball or per-preparation norm conservation.'}
def generate(baseline,destination,replay=False):
 f=freeze();baseline=Path(baseline);assert sha(baseline)==f['baseline_sha256'];Y=np.memmap(baseline,dtype='<i8',mode='r',shape=SHAPE);mx=max(abs(int(Y.min())),abs(int(Y.max())));assert 7*mx<2**63
 dest=Path(destination);dest.mkdir(parents=True,exist_ok=False);rows=[];times=np.arange(8191)
 for e in f['cases']:
  name=e['case'];M,den=transforms(e['kind'],e['transform_seed']);rng=np.random.default_rng(e['noise_seed']);channels=rng.integers(0,62,size=(37,8191));signs=2*rng.integers(0,2,size=(37,8191))-1;raw=dest/(name+'.i64le')
  with raw.open('xb') as stream:stream.truncate(150321232)
  Z=np.memmap(raw,dtype='<i8',mode='r+',shape=SHAPE);clean_hash=hashlib.sha256();checks=0
  for j in range(37):
   v=nominal(Y,M,den,j);clean_hash.update(v.astype('<i8').tobytes());z=v.copy();z[times,channels[j]]+=signs[j];Z[j]=z
  Z.flush();del Z;Z=np.memmap(raw,dtype='<i8',mode='r',shape=SHAPE);maximum=0
  for j in range(37):
   v=nominal(Y,M,den,j);diff=np.array(Z[j])-v;expected=np.zeros_like(diff);expected[times,channels[j]]=signs[j];assert np.array_equal(diff,expected) and np.all(np.sum(diff*diff,axis=1)==1);checks+=diff.size;maximum=max(maximum,max(abs(int(Z[j].min())),abs(int(Z[j].max()))))
  assert checks==18790154;del Z
  row={'case':name,'record_sha256':sha(raw),'nominal_sha256':clean_hash.hexdigest(),'bytes':150321232,'readings_checked':checks,'per_new_nominal_vector_integer_error_squared_max':1,'raw_quantum':[1,1<<48],'max_absolute_raw_integer':maximum,'transform_integer_matrix':M.tolist(),'transform_denominator':den,'recipe':e,'source_error_bounds':model_bounds(e['kind']),'new_physical_data':False,'old_original_baseline_ball_eligibility_claimed':False};rows.append(row);print(json.dumps({k:row[k] for k in ['case','record_sha256','nominal_sha256','max_absolute_raw_integer']}),flush=True)
 assert sha(baseline)==f['baseline_sha256'] and len({r['record_sha256'] for r in rows})==len(rows)
 result={'status':'ALL_FRESH_PREPARATION_RECORDS_FROZEN_BEFORE_ESTIMATOR','protocol_sha256':sha(P/'PROTOCOL_FREEZE.json'),'records':rows,'physical_promotion':0}
 if replay:assert json.loads((P/'DATA_FREEZE.json').read_text())==result
 else:assert not (P/'DATA_FREEZE.json').exists();(P/'DATA_FREEZE.json').write_text(json.dumps(result,indent=2))
 return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--baseline',required=True);p.add_argument('--destination',required=True);p.add_argument('--replay',action='store_true');args=p.parse_args();generate(args.baseline,args.destination,args.replay)
