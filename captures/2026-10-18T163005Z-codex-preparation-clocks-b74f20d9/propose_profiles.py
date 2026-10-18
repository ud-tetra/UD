import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import numpy as np
from scipy.linalg import pinv
from flint import ctx
from bindings import P,check
from source_model import source,rotate,coefficients
ctx.prec=512
if __name__=='__main__':
 f=check();theta,B,A=source();out=P/'profiles';out.mkdir(exist_ok=False)
 for e in f['profiles']:
  Bo,c,s=rotate(theta,B,e['offsets']);N=coefficients(Bo,A);H=pinv(N.astype(float)/2.**127,check_finite=False);np.savez_compressed(out/f"{e['name']}.npz",cos_num=c,sin_num=s,right_inverse=H)
 print('Four untrusted rotated coefficient right-inverse witnesses saved')
