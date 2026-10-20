"""Read-only replay of both saved state/flux witnesses and parameter join."""
import sys
sys.dont_write_bytecode=True
import os,subprocess,argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
HERE=Path(__file__).resolve().parent

def state_flux(leaf):
 p=subprocess.run([sys.executable,'replay.py'],cwd=HERE/leaf,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1'),check=True,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 return leaf,p.stdout

def main(scalar_only=False):
 if not scalar_only:
  with ThreadPoolExecutor(max_workers=2) as pool:
   for leaf,log in pool.map(state_flux,['original','neighbor']):print(leaf+' saved state/flux replay\n'+log,flush=True)
 import shifted_audit,join_audit
 shifted_audit.main();join_audit.main()
 print('PASS scalar-only replay' if scalar_only else 'PASS full saved state/flux/floating/join replay',flush=True)

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--scalar-only',action='store_true');a=ap.parse_args();main(a.scalar_only)
