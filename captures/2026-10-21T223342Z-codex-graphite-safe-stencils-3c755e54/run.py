from pathlib import Path
import os,json,subprocess,concurrent.futures
p=Path(__file__).resolve().parent;root=p.parent;env=os.environ.copy();env.update({'UCX_TLS':'self','UCX_LOG_LEVEL':'error','UCX_WARN_UNUSED_ENV_VARS':'n','OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1','LD_LIBRARY_PATH':str(root/'mpi-runtime/lib'),'PYTHONPATH':str(root/'lammps-runtime')})
def job(case):
 with (p/(case+'.log')).open('w') as log:r=subprocess.run(['python3',str(p/'calculate.py'),case],env=env,stdout=log,stderr=subprocess.STDOUT)
 return {'case':case,'exit':r.returncode}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:rows=list(ex.map(job,['31_dir_10084','31_dir_10134']))
(p/'EXECUTION.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows))
