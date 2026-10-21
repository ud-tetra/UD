import os,subprocess,concurrent.futures,json
from pathlib import Path
p=Path(__file__).resolve().parent;root=p.parent;env=os.environ.copy();env.update(UCX_TLS='self',UCX_LOG_LEVEL='error',UCX_WARN_UNUSED_ENV_VARS='n',OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1',LD_LIBRARY_PATH=str(root/'mpi-runtime/lib'),PYTHONPATH=str(root/'lammps-runtime'))
def run(c):
 with (p/(c+'.log')).open('w') as log:r=subprocess.run(['python3',str(p/'relax.py'),c],env=env,stdout=log,stderr=subprocess.STDOUT)
 return c,r.returncode
with concurrent.futures.ThreadPoolExecutor(4) as ex:r=list(ex.map(run,json.loads((p/'FREEZE.json').read_text())['cases']))
(p/'RELAX_EXECUTION.json').write_text(json.dumps(r));print(r)
