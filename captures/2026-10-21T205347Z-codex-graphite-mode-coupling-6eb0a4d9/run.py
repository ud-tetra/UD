from pathlib import Path
import os,subprocess,concurrent.futures,json
p=Path(__file__).resolve().parent;root=p.parent;env=os.environ.copy();env.update({'UCX_TLS':'self','UCX_LOG_LEVEL':'error','UCX_WARN_UNUSED_ENV_VARS':'n','OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1','LD_LIBRARY_PATH':str(root/'mpi-runtime/lib'),'PYTHONPATH':str(root/'lammps-runtime')})
def job(i):
 with (p/f'job_{i}.log').open('w') as log:r=subprocess.run(['python3',str(p/'calculate.py'),str(i)],env=env,stdout=log,stderr=subprocess.STDOUT)
 return {'index':i,'process_exit':r.returncode}
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for f in concurrent.futures.as_completed([ex.submit(job,i) for i in range(36)]):
  row=f.result();rows.append(row);(p/'EXECUTION.json').write_text(json.dumps({'jobs':rows},indent=2)+'\n');print(json.dumps(row),flush=True)
