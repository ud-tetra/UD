from pathlib import Path
import os,subprocess,concurrent.futures,json,time
p=Path(__file__).resolve().parent;env=os.environ.copy();env.update({'UCX_TLS':'self','UCX_LOG_LEVEL':'error','UCX_WARN_UNUSED_ENV_VARS':'n','OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1','LD_LIBRARY_PATH':str(p.parent/'mpi-runtime/lib'),'PYTHONPATH':str(p.parent/'lammps-runtime')})
for w in [1,2,3]:assert json.loads((p/f'PAIR_CHECK_WIDTH{w}.json').read_text())['status']=='PASS'
def job(j):
 i,c,w=j;start=time.time()
 with (p/f'job_width{w}_{i}_{c}.log').open('w') as out:
  for script in ['calculate.py','energy_check.py']:
   r=subprocess.run(['python3',str(p/script),str(i),str(c),str(w)],env=env,stdout=out,stderr=subprocess.STDOUT)
   if r.returncode:return {'case_index':i,'cutoff_A':c,'width_A':w,'process_exit':r.returncode,'script':script,'seconds':time.time()-start}
 return {'case_index':i,'cutoff_A':c,'width_A':w,'process_exit':0,'seconds':time.time()-start}
rows=[]
# Interleave width variants at each cutoff to avoid selecting cases by outcome.
jobs=[(i,c,w) for c in [16,20,24] for w in [1,3] for i in range(4)]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for f in concurrent.futures.as_completed([ex.submit(job,j) for j in jobs]):
  rows.append(f.result());print(json.dumps(rows[-1]),flush=True);(p/'EXECUTION.json').write_text(json.dumps({'jobs':rows,'scope':'24 new jobs only; completion is not scientific verdict'},indent=2)+'\n')
