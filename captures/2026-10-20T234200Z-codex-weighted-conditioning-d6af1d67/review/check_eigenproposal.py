#!/usr/bin/env python3
"""Independent exact replay of the persisted Gram eigenproposal. No eigensolver."""
from pathlib import Path
import json,gzip,hashlib,gc
import numpy as np
from flint import fmpz_mat
P=Path(__file__).resolve().parent;W=P.parent;r=1999
sha=lambda x:hashlib.sha256(x.read_bytes()).hexdigest()
base=W/'c27_cert_v2';p=base/'EIGENPROPOSAL.bin.gz';h=sha(p);raw=gzip.decompress(p.read_bytes());assert len(raw)==8*(r*r+r)
allnums=np.frombuffer(raw,dtype='<i8');V=allnums[:r*r].reshape(r,r);d=allnums[r*r:];assert np.all(V>=-2**40)and np.all(V<=2**40)and np.all(d>=-2**60)and np.all(d<=2**60)
bind=json.loads((base/'SOURCE_BINDINGS.json').read_text());assert h==bind['eigenproposal_gzip_sha256'] and hashlib.sha256(raw).hexdigest()==bind['eigenproposal_decoded_sha256']
with np.load(base/'GRAM_MIDPOINT.npz',allow_pickle=False)as z:G=z['matrix']
# Bind the Gram to our already independently reconstructed exact midpoint.
prior=json.loads((P/'FINITE_CHECKS.json').read_text());assert sha(base/'GRAM_MIDPOINT.npz')==prior['inputs']['Gram_midpoint_npz_sha256'];assert G.shape==(r,r)and np.array_equal(G,G.T)
VM=fmpz_mat(V.tolist());VtV=VM.transpose()*VM
eta2=sum((int(VtV[i,j])-(2**80 if i==j else 0))**2 for i in range(r)for j in range(r));del VtV;gc.collect();assert eta2*256<2**160
# Compute the residual rowwise rather than retaining the whole producer product.
beta2=0
for start in range(0,r,100):
 stop=min(start+100,r);rows=fmpz_mat(G[start:stop].tolist())*VM
 for i in range(stop-start):
  for j in range(r):beta2+=(int(rows[i,j])-int(V[start+i,j])*int(d[j]))**2
assert beta2<2**156
minimum=min(map(int,d));assert minimum>9*2**40
source=json.loads((base/'ARITHMETIC_DIAGNOSTICS.json').read_text())
assert eta2==int(source['V_orthogonality_squared_numerator']) and beta2==int(source['Gram_eigen_residual_squared_numerator']) and minimum==int(source['Gram_eigenproposal_min_diagonal_numerator'])
assert sha(p)==h
result={'status':'PASS_PERSISTED_EIGENPROPOSAL_EXACT_INDEPENDENT_REPLAY','V_orthogonality_squared_numerator':str(eta2),'V_orthogonality_squared_denominator_power2':160,'Gram_eigen_residual_squared_numerator':str(beta2),'Gram_eigen_residual_squared_denominator_power2':200,'min_diagonal_numerator':str(minimum),'min_diagonal_denominator_power2':60,'residual_entries_checked':r*r,'eigenproposal_gzip_sha256':h,'eigenproposal_decoded_sha256':hashlib.sha256(raw).hexdigest(),'Gram_midpoint_npz_sha256':sha(base/'GRAM_MIDPOINT.npz'),'scope':{'no_eigensolver_or_producer_checker_execution':True,'saved_proposal_identity_directly_bound':True,'Gram_identity_from_prior_independent_complete_reconstruction':True,'physical_promotion':0,'external_review':'PENDING'}}
(P/'EIGENPROPOSAL_CHECKS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':result['status'],'all_residual_entries':r*r}))
