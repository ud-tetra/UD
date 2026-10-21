from pathlib import Path
import os,subprocess,json,concurrent.futures,numpy as np
p=Path(__file__).resolve().parent;root=p.parent;env=os.environ.copy();env.update({'UCX_TLS':'self','UCX_LOG_LEVEL':'error','UCX_WARN_UNUSED_ENV_VARS':'n','OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1','LD_LIBRARY_PATH':str(root/'mpi-runtime/lib'),'PYTHONPATH':str(root/'lammps-runtime')})
def job(i):
 with (p/f'recovery_{i}.log').open('w') as log:r=subprocess.run(['python3',str(p/'calculate.py'),str(i),'reuse'],env=env,stdout=log,stderr=subprocess.STDOUT)
 return {'index':i,'process_exit':r.returncode}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:rows=list(ex.map(job,range(4)))
assert all(r['process_exit']==0 for r in rows)
freeze=json.loads((p/'FREEZE.json').read_text());count=0
for i in range(4):
 s=freeze['inputs'][i];key=f"{s['case']}_c{s['cutoff_A']}_w{s['width_A']}";a=np.load(p/'development_failure'/key/'COLUMNS.npz');b=np.load(p/key/'COLUMNS.npz');assert a.files==b.files
 for name in a.files:assert np.array_equal(a[name],b[name]);count+=1
r={'status':'PASS','exports':rows,'arrays_identical':count,'change':'JSON scalar serialization only; raw columns reused, reciprocal controls reevaluated; no thresholds changed'};(p/'EXPORT_RECOVERY.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
