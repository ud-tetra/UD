"""Full raw-to-integer-projection replay; frozen gate/recipe unchanged."""
import json
import numpy as np
from certify import P,sha,up,arb
from sketch import sketch
f=json.loads((P/'FREEZE.json').read_text())
for n,h in f['code_sha256'].items():assert sha(P/n)==h
base=P.parent/'floating-timing-work/records/ramp_clock_stress.i64le';raw=P.parent/'uniform-two-work/records/cyclic_unit.i64le'
assert sha(base)=='25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59' and sha(raw)==f['record_sha256']
Y=np.memmap(base,dtype='<i8',mode='r',shape=(37,8191,62));Z=np.memmap(raw,dtype='<i8',mode='r',shape=Y.shape)
peak=0;count=0
for k in range(0,8191,256):
 d=Z[:,k:k+256]-Y[:,k:k+256];assert np.max(np.abs(d))<=1;peak=max(peak,int(np.sum(d*d,axis=-1).max()));count+=d.size
assert peak==1 and count==18790154
X=np.array(Z.transpose(1,2,0).reshape(8191,2294),np.int64);A=sketch();l1=int(np.abs(A).sum(axis=0).max());mx=max(abs(int(Y.min())),abs(int(Y.max())))+1;assert mx==30100665057351 and mx*l1<2**63
N=X@A;ranges=[(0,2731),(2731,5462),(5462,8191)]
for k,(a,b) in enumerate(ranges):
 with np.load(P/'results'/f'INTEGER_{k}.npz') as z:assert np.array_equal(N[a:b],z['numerator'])
L=np.abs(A).reshape(62,37,321).max(axis=0).sum(axis=0);nmax=max(abs(int(N.min())),abs(int(N.max())));upper=nmax+2*int(L.max());assert upper<2**53
r={'status':'PASS_ALL_RAW_DIFFERENCES_AND_EXACT_INTEGER_PROJECTION','readings_checked':count,'vector_integer_squared_error_max':peak,'integer_projection_entries_checked':int(N.size),'raw_sha256':sha(raw),'baseline_sha256':sha(base),'all_encoded_ball_integer_product_bound':mx*l1,'all_encoded_ball_numerator_upper':upper,'exact_binary64_projection_for_encoded_ball':True,'legacy_uniform_projection_exactness_claimed':False,'uniform_SVD_phase_claimed':False,'physical_promotion':0}
(P/'RAW_PROJECTION_REPLAY.json').write_text(json.dumps(r,indent=2));print(json.dumps(r))
