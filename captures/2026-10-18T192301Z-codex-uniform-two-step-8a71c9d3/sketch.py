import json,numpy as np
from bindings import P

def sketch():
 old=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64);v=np.pad(np.array(json.loads((P/'inputs/NULL_VECTOR.json').read_text())['vector'],np.int64),(0,1974));new=np.random.default_rng(184052).choice([-1.,1.],size=(2294,160)).astype(np.int64)
 assert int(v@v)==16228 and np.all(v@old==0)
 return np.column_stack((2*old,v,2*new))
