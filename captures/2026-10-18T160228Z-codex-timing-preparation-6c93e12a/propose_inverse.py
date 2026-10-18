import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import numpy as np
from scipy.linalg import pinv
from bindings import P,check
from source_model import model
if __name__=='__main__':
 check();theta,N=model();H=pinv(N.astype(np.float64)/2.**67,check_finite=False)
 out=P/'RIGHT_INVERSE.npz';assert not out.exists();np.savez_compressed(out,right_inverse=H)
 print('Untrusted right inverse saved; all accuracy checked by exact residuals')
