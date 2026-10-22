from pathlib import Path
import subprocess,concurrent.futures
p=Path(__file__).parent
def execute(i):
 with (p/f'energy_{i}.log').open('w') as f:r=subprocess.run(['python3',str(p/'energy_check.py'),str(i)],stdout=f,stderr=subprocess.STDOUT)
 print('energy',i,r.returncode,flush=True);return r.returncode
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as e:codes=list(e.map(execute,range(4)))
assert all(x==0 for x in codes)
