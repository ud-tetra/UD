from fractions import Fraction as F
import numpy as np
from flint import arb,fmpq
from bindings import freeze

def signs(mode):
 f=freeze();rng=np.random.default_rng(f['seeds'][mode])
 if mode=='dense_sign':return rng.integers(0,2,size=(37,8191,62),dtype=np.int64)*2-1
 if mode=='coherent_dc':return np.repeat(rng.integers(0,2,size=(37,1,62),dtype=np.int64)*2-1,8191,axis=1)
 raise AssertionError('Unknown frozen family')
def noise_upper(G,amp):
 trace=sum(int(G[j,j]) for j in range(321));row=max(sum(abs(int(x)) for x in G[j]) for j in range(321));return arb(min(trace,row)).sqrt()*amp/(1<<55)
def raw_bound(amp):return arb(62).sqrt()*amp/(1<<48)
