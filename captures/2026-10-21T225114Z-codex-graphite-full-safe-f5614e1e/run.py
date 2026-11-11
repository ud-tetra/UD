from pathlib import Path
import os,json,subprocess,concurrent.futures
p=Path(__file__).resolve().parent;root=p.parent;assert json.loads((p/'FEASIBILITY.json').read_text())['all_pass'];env=os.environ.copy();env.update({'UCX_TLS':'self','UCX_LOG_LEVEL':'error','UCX_WARN_UNUSED_ENV_VARS':'n','OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1','LD_LIBRARY_PATH':str(root/'mpi-runtime/lib'),'PYTHONPATH':str(root/'lammps-runtime')})
def job(case):
 with (p/(case+'.log')).open('w') as log:r=subprocess.run(['python3',str(p/'calculate.py'),case],env=env,stdout=log,stderr=subprocess.STDOUT)
 return {'case':case,'exit':r.returncode}
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for v in concurrent.futures.as_completed([ex.submit(job,c) for c in json.loads((p/'FREEZE.json').read_text())['cases']]):
  row=v.result();rows.append(row);(p/'EXECUTION.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(row),flush=True)
