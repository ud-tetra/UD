"""Postexecution structural intake guard; numerical verifier/gates are unchanged."""
import json
import numpy as np
from bindings import P,freeze
if __name__=='__main__':
 rows=[]
 for e in freeze()['cases']:
  n=e['case'];d=P/'inputs'/n
  if n=='dense_unit':continue
  for name,shape,key in [('BASIS_A.npz',(4096,209),'basis'),('BASIS_B.npz',(4095,209),'basis'),('PHASE_PROPOSAL.npz',(209,),'two_step_phase')]:
   with np.load(d/name,allow_pickle=False) as z:a=z[key];assert a.shape==shape and np.all(np.isfinite(a))
  with np.load(d/'FLOAT_META.npz',allow_pickle=False) as z:
   for k in ['shift','eigenvectors','inverse']:assert z[k].shape==(209,209) and np.all(np.isfinite(z[k]))
   for k in ['eigenvalues','angles']:assert z[k].shape==(209,) and np.all(np.isfinite(z[k]))
  with np.load(P/'results'/n/'PROPOSALS.npz',allow_pickle=False) as z:assert z['coefficient'].shape==(209,321) and z['alignment'].shape==(209,209)
  rows.append(n)
 r={'status':'PASS','cases':rows,'postexecution_packaging_guard':True,'numerical_gates_unchanged':True,'physical_promotion':0};(P/'ARCHIVE_STRUCTURE.json').write_text(json.dumps(r,indent=2));print(json.dumps(r))
