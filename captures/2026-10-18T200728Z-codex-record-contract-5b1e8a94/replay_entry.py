import subprocess,sys,os
from bindings import P
for script in ['structure.py','replay_package.py']:
 r=subprocess.run([sys.executable,script],cwd=P,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'});assert r.returncode==0
