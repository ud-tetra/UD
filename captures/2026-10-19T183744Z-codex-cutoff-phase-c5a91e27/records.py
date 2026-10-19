"""Six exact same-clock-parity preparations, with fixed paired onehot correlations."""
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from common import P,freeze,sha
SHAPE=(37,8191,62);BYTES=150321232

def rotation(offset):
 M=np.eye(37,dtype=np.int64)*5
 for p in [0,1]:
  g=np.roll(np.arange(p,37,2),-offset)
  for k in range(0,len(g)-1,2):
   i,j=map(int,g[k:k+2]);M[i,i]=M[j,j]=3;M[i,j]=-4;M[j,i]=4
 assert np.array_equal(M@M.T,np.eye(37,dtype=np.int64)*25)
 return M

def transform(spec):
 kind=spec['transform'];M=np.zeros((37,37),np.int64);den=1
 if kind in ['signed_reverse','signed_shuffle']:
  rng=np.random.Generator(np.random.PCG64(spec.get('transform_seed',0)))
  for p in [0,1]:
   g=np.arange(p,37,2);perm=g[::-1] if kind=='signed_reverse' else rng.permutation(g)
   for i,(j,b) in enumerate(zip(g,perm)):M[j,b]=1 if(i+p)%2==0 else -1
 elif kind=='R1':M=rotation(1);den=5
 elif kind in ['R1R0','R1R0_transpose']:
  M=rotation(1)@rotation(0);den=25
  if kind.endswith('transpose'):M=M.T
 else:raise ValueError(kind)
 assert np.array_equal(M@M.T,np.eye(37,dtype=np.int64)*(den*den));assert all(i%2==j%2 for i,j in zip(*np.nonzero(M)));assert max(np.abs(M).sum(axis=1))<=49
 return M,den

def noise(spec):
 t=np.arange(8191)[None,:];j=np.arange(37)[:,None];kind=spec['noise']
 if kind=='stationary':channels=np.zeros((37,8191),np.int64);signs=np.ones_like(channels)
 elif kind=='cycle':channels=(7*j+3*t)%62;signs=np.where((j+t)%2==0,1,-1)
 elif kind=='block1024':
  rng=np.random.Generator(np.random.PCG64(spec['noise_seed']));ch=rng.integers(0,62,size=(37,8));sg=2*rng.integers(0,2,size=(37,8))-1;channels=ch[:,np.arange(8191)//1024];signs=sg[:,np.arange(8191)//1024]
 elif kind in ['period2','period4']:
  channels=np.broadcast_to(((5*j+1)%62 if kind=='period2' else (11*j+2)%62),SHAPE[:2]).copy();signs=np.broadcast_to((np.where(t%2==0,1,-1) if kind=='period2' else np.where(t%4<2,1,-1)),SHAPE[:2]).copy()
 elif kind=='directed_spatial':
  rng=np.random.Generator(np.random.PCG64(spec['noise_seed']));ch=rng.integers(0,62,size=37);sg=2*rng.integers(0,2,size=37)-1;channels=np.broadcast_to(ch[:,None],SHAPE[:2]).copy();signs=sg[:,None]*np.where(t%4<2,1,-1)
 else:raise ValueError(kind)
 assert channels.shape==signs.shape==SHAPE[:2] and np.all((channels>=0)&(channels<62)) and np.all(signs*signs==1)
 return channels,signs

def nominal(Y,M,den,j):
 active=np.flatnonzero(M[j]);v=sum((int(M[j,k])*np.array(Y[k],np.int64) for k in active),np.zeros((8191,62),np.int64))
 if den==1:return v
 q=v//den;rem=v-den*q;out=q+(rem>den//2);assert np.max(np.abs(den*out-v))<=den//2
 return out

def generate_one(baseline,spec,raw):
 f=freeze();baseline=Path(baseline);assert sha(baseline)==f['baseline_sha256'];Y=np.memmap(baseline,dtype='<i8',mode='r',shape=SHAPE);mx=max(abs(int(Y.min())),abs(int(Y.max())));assert 49*mx+25<2**63;M,den=transform(spec);channels,signs=noise(spec);raw=Path(raw);assert not raw.exists();raw.parent.mkdir(parents=True,exist_ok=True)
 with raw.open('xb') as stream:stream.truncate(BYTES)
 Z=np.memmap(raw,dtype='<i8',mode='r+',shape=SHAPE);times=np.arange(8191);nominal_sha=hashlib.sha256()
 for j in range(37):
  v=nominal(Y,M,den,j);nominal_sha.update(v.astype('<i8').tobytes());v[times,channels[j]]+=signs[j];Z[j]=v
 Z.flush();del Z;Z=np.memmap(raw,dtype='<i8',mode='r',shape=SHAPE);checked=0;maximum=0
 for j in range(37):
  diff=np.array(Z[j])-nominal(Y,M,den,j);wanted=np.zeros_like(diff);wanted[times,channels[j]]=signs[j];assert np.array_equal(diff,wanted) and np.all((diff*diff).sum(axis=1)==1);checked+=diff.size;maximum=max(maximum,max(abs(int(Z[j].min())),abs(int(Z[j].max()))))
 del Z,Y;assert checked==18790154
 old=json.loads((P/'inputs/BASE_GENERATION.json').read_text());d0=F(*next(r['evaluation_bounds']['scalar_waveform_error_upper'] for r in old['records'] if r['record_sha256']==f['baseline_sha256']));qraw=F(1,1<<48);rowmax=int(np.abs(M).sum(axis=1).max());dnom=F(rowmax,den)*d0+F(den//2,den)*qraw;vec2=62*dnom*dnom+2*dnom*qraw+qraw*qraw
 return dict(case=spec['case'],recipe=spec,record_sha256=sha(raw),nominal_sha256=nominal_sha.hexdigest(),bytes=BYTES,readings_checked=checked,transform_integer_matrix=M.tolist(),transform_denominator=den,maximum_numerator_row_L1=rowmax,nominal_scalar_source_error=[dnom.numerator,dnom.denominator],vector_squared_source_error=[vec2.numerator,vec2.denominator],per_new_nominal_vector_integer_squared_error_max=1,raw_quantum=[1,1<<48],max_absolute_raw_integer=maximum,old_original_baseline_ball_eligibility_claimed=False,new_physical_data=False,per_preparation_norm_conservation_claimed=False)

def freeze_data(baseline,work):
 f=freeze();rows=[];work=Path(work);work.mkdir(exist_ok=False)
 for spec in f['cases']:
  raw=work/(spec['case']+'.i64le');r=generate_one(baseline,spec,raw);rows.append(r);raw.unlink();print(json.dumps(dict(stage='pre_fit_data_freeze',case=spec['case'],record_sha256=r['record_sha256'])),flush=True)
 result=dict(status='ALL_SIX_RAW_HASHES_FROZEN_BEFORE_ANY_NEW_FIT',protocol_sha256=sha(P/'PROTOCOL_FREEZE.json'),records=rows,storage_policy='Each transient raw file may be removed after complete hashing/checks; bitidentical regeneration is mandatory before its single fit. No case selection or retuning.',physical_promotion=0);assert not(P/'DATA_FREEZE.json').exists();(P/'DATA_FREEZE.json').write_text(json.dumps(result,indent=2));return result

def recover_parent(baseline,record,raw):
 """Regenerate a pinned prior record from its saved exact matrix and RNG recipe."""
 f=freeze();assert sha(baseline)==f['baseline_sha256'];M=np.array(record['transform_integer_matrix'],np.int64);den=record['transform_denominator'];assert np.array_equal(M@M.T,np.eye(37,dtype=np.int64)*(den*den));Y=np.memmap(baseline,dtype='<i8',mode='r',shape=SHAPE);mx=max(abs(int(Y.min())),abs(int(Y.max())));assert 49*mx+25<2**63;rng=np.random.Generator(np.random.PCG64(record['recipe']['noise_seed']));channels=rng.integers(0,62,size=(37,8191));signs=2*rng.integers(0,2,size=(37,8191))-1;raw=Path(raw);assert not raw.exists()
 with raw.open('xb') as s:s.truncate(BYTES)
 Z=np.memmap(raw,dtype='<i8',mode='r+',shape=SHAPE);times=np.arange(8191);clean=hashlib.sha256()
 for j in range(37):
  v=nominal(Y,M,den,j);clean.update(v.astype('<i8').tobytes());v[times,channels[j]]+=signs[j];Z[j]=v
 Z.flush();del Z;Z=np.memmap(raw,dtype='<i8',mode='r',shape=SHAPE)
 for j in range(37):
  diff=np.array(Z[j])-nominal(Y,M,den,j);wanted=np.zeros_like(diff);wanted[times,channels[j]]=signs[j];assert np.array_equal(diff,wanted) and np.all((diff*diff).sum(axis=1)==1)
 del Z,Y;assert clean.hexdigest()==record['nominal_sha256'] and sha(raw)==record['record_sha256'];return dict(case=record['case'],record_sha256=record['record_sha256'],rechecked_parent_raw_scalars=18790154)
