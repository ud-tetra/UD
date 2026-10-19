"""Replay frozen synthetic controls only; never run or fetch an experimental record."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve().parent

def main():
    a=argparse.ArgumentParser();a.add_argument('--output',type=Path,required=True);z=a.parse_args()
    f=json.loads((HERE/'PROTOCOL_FREEZE.json').read_text())
    for row in f['files']:
        b=(HERE/row['path']).read_bytes()
        if len(b)!=row['bytes'] or hashlib.sha256(b).hexdigest()!=row['sha256']:
            raise RuntimeError('FROZEN_BYTES_CHANGED:'+row['path'])
    r=subprocess.run([sys.executable,str(HERE/'controls.py')],cwd=HERE,text=True,capture_output=True)
    if r.returncode!=0:raise RuntimeError('CONTROL_PROCESS_FAILED:'+r.stderr+r.stdout)
    out=json.loads(r.stdout)
    if not out['all_pass']:raise RuntimeError('CONTROL_FAILURE')
    z.output.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')

if __name__=='__main__':main()
