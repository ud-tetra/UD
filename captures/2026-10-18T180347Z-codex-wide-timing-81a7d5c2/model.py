from fractions import Fraction as F
import json,numpy as np
from flint import arb,fmpq
from bindings import P

def sketch():
 old=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64)
 short=np.array(json.loads((P/'inputs/NULL_VECTOR.json').read_text())['vector'],np.int64);v=np.pad(short,(0,1974));assert int(v@v)==16228 and np.all(v@old==0)
 new=np.random.default_rng(184052).choice([-1.,1.],size=(2294,160)).astype(np.int64)
 A=np.column_stack((2*old,v,2*new));assert A.shape==(2294,321)
 return A

def rules(width):
 A=sketch()[:,:width];s2=F(sum(int(x)**2 for x in A.flat),1<<14)
 old=F(371097,4096);tau=F(*json.loads((P/'inputs/SKETCH_RULE.json').read_text())['cutoff'])
 return {'sketch_Frobenius_squared':s2,'common':tau*tau,'scaled':tau*tau*s2/old,'additive_vector_noise_squared':F(37*8191,1<<40)*s2}

def source_tail(width):
 with np.load(P/'inputs/REFERENCE_PROPOSAL.npz',allow_pickle=False) as z:B=z['coeff']
 L=max(sum(abs(int(x)) for x in B[1:,c]) for c in range(2294));delta=F(L,1<<120)+F(1,1<<49)
 return 8191*2294*delta*delta*rules(width)['sketch_Frobenius_squared']
