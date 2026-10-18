import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import argparse
import numpy as np
from flint import ctx
from bindings import P,load_case
from frame_values import values
ctx.prec=512
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('case');a=p.parse_args();_,_,o,_=load_case(a.case)
 with np.load(P/'inputs/REFERENCE_PROPOSAL.npz',allow_pickle=False) as z:pp=values(z['theta'])
 with np.load(o/'FLOAT_WITNESS.npz',allow_pickle=False) as z:U=z['basis']
 D=U.T@(pp.astype(np.float64)/2.**60)
 target=o/'FRAME_REDUCTION.npz';assert not target.exists();np.savez_compressed(target,reduction=D)
 print('Untrusted auxiliary frame reduction saved; actual estimator arrays and proposal unchanged')
