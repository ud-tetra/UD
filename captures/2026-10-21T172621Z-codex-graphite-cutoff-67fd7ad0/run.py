import concurrent.futures,subprocess,pathlib
p=pathlib.Path(__file__).parent
jobs=[(i,c) for c in ['20','24'] for i in range(4)]
def execute(job):
 i,c=job
 with (p/f'case_{i}_{c}.log').open('w') as f:
  r=subprocess.run(['python3','-u',str(p/'calculate.py'),str(i),c],stdout=f,stderr=subprocess.STDOUT)
 print(i,c,r.returncode,flush=True)
 return r.returncode
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:
 codes=list(e.map(execute,jobs))
assert all(x==0 for x in codes)
