"""Post-execution packaging guard; no estimator or numerical bound changes."""
import numpy as np
from bindings import P,freeze,sha
if __name__=='__main__':
 for e in freeze()['cases']:
  o=P/'results'/e['case']
  with np.load(o/'GRAM.npz',allow_pickle=False) as z:g=z['integers_decimal']
  with np.load(o/'GRAM_EIGEN.npz',allow_pickle=False) as z:q=z['Q'];d=z['eigenvalues']
  assert g.shape==(321,321) and np.array_equal(g,g.T)
  assert q.shape==(321,321) and d.shape==(321,) and np.all(d[:-1]>=d[1:])
 print('PASS: exact Gram symmetry, shapes and sorted eigenproposal structure for both hash-bound fixtures')
