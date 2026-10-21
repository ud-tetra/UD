from pathlib import Path
import hashlib,json,platform,datetime
import numpy as np,scipy
from numerical_replay import build
C=Path(__file__).parent;R=C.parents[1]
def sha(b):return hashlib.sha256(b).hexdigest()
def write(n,v):(C/n).write_text(json.dumps(v,indent=2)+'\n')
settings={'level':4,'N':256,'metric':'identity','model':'source-clean R6b; no added disorder or connectivity','probes':[.00133,1e-8],'k':10,'ncv':64,'maxiter':12800,'eigsh_tol':1e-12,'rng_seed':20261021,'dense_driver':'evd','cluster_atol':1e-10,'cluster_rtol':1e-12,'residual_tol':5e-12,'orthogonality_tol':1e-10,'theta_eigenvalue_tol':1e-10,'theta_projector_tol':1e-10,'coupled_projector_tol':1e-4,'cluster_policy':'span from first cluster eigenvalue, not rounded values or chained gaps; numerical grouping not an exact degeneracy theorem','incomplete_policy':'report rank deficiency; do not compare partial returned projector as complete; retain all vectors/failures','numeric_interpretation':'Residual and projector checks certify this finite computation only; not physical thresholds','prior_contract_sha256':'75942451ae44fc907450f72500ac27db4b81e8e0cd27e5d8a5023cd6622a6e10','registration':'development freeze; historically exposed; not independent preregistration','physical_promotion':0}
theta,rho,full,depth,parity=build(4)
rng=np.random.default_rng(settings['rng_seed']);initial_state=rng.bit_generator.state;v0=rng.standard_normal(512);v0/=np.linalg.norm(v0)
assert np.array_equal(full,full.T) and np.array_equal(theta,theta.T)
labels=np.arange(256)//64;f_labels=np.r_[labels,labels]
assert np.all(full[f_labels[:,None]!=f_labels[None,:]]==0)
# Independently check the structural diagonal:12 cousin weights and48 second-cousin weights.
assert np.max(np.abs(np.diag(theta)-(12*(185/192)**4+48*(185/192)**6)))<1e-12
np.savez_compressed(C/'INPUTS.npz',theta=theta,rho=rho,full=full,depth=depth,parity=parity,v0=v0)
write('SETTINGS.json',settings)
source=[]
for name in ('docs/hmulti_r6b.py','docs/r6b_version_b.py'):
 p=R/name;source.append({'path':name,'sha256':sha(p.read_bytes())})
def ah(a):return sha(np.ascontiguousarray(a,dtype='<f8').tobytes())
receipt={'status':'FROZEN_BEFORE_EIGENSOLVER_EXECUTION','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_commit':'c6b66d68a25b655627d6eb6f1bf6f96a13e2121b','source_files':source,'runner_sha256':sha((C/'numerical_replay.py').read_bytes()),'prepare_sha256':sha(Path(__file__).read_bytes()),'settings_sha256':sha((C/'SETTINGS.json').read_bytes()),'input_sha256':sha((C/'INPUTS.npz').read_bytes()),'matrix_hash_format':'C-contiguous little-endian float64 data; shapes separately recorded','matrices':{'theta':{'shape':list(theta.shape),'sha256':ah(theta)},'rho':{'shape':list(rho.shape),'sha256':ah(rho)},'full':{'shape':list(full.shape),'sha256':ah(full)}},'v0_sha256':ah(v0),'rng_initial_state':initial_state,'runtime':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'machine':platform.machine(),'threads':'OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 supplied at invocation'},'physical_promotion':0,'independent_review':'PENDING'}
write('PRE_RUN_RECEIPT.json',receipt);print(json.dumps({'frozen':True,'settings_sha256':receipt['settings_sha256'],'matrix_full_sha256':receipt['matrices']['full']['sha256']}))
