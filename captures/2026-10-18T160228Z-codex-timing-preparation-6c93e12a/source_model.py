import json
import numpy as np
from bindings import P
from proof_math import fm,arr

def model():
 with np.load(P/'inputs/REFERENCE_PROPOSAL.npz',allow_pickle=False) as z:theta=z['theta'];coeff=z['coeff']
 W=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64);v=np.pad(np.array(json.loads((P/'inputs/NULL_VECTOR.json').read_text())['vector'],np.int64),(0,1974));A=np.column_stack((2*W,v))
 return theta,arr(fm(coeff)*fm(A))
