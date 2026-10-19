"""Replay frozen synthetic metadata controls only, no evidence/raw/model execution."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import validate_request_v2 as v

HERE=Path(__file__).resolve().parent

def main():
    a=argparse.ArgumentParser();a.add_argument('--output',type=Path,required=True);z=a.parse_args()
    v.output_path(z.output,HERE/'REQUEST_TEMPLATE.json')
    freeze=json.loads((HERE/'PROTOCOL_FREEZE_v0.2.json').read_text())
    for row in freeze['files']:
        b=(HERE/row['path']).read_bytes()
        if len(b)!=row['bytes'] or hashlib.sha256(b).hexdigest()!=row['sha256']:raise RuntimeError('FROZEN_BYTES_CHANGED:'+row['path'])
    p=subprocess.run([sys.executable,str(HERE/'controls_v2.py')],cwd=HERE,text=True,capture_output=True)
    if p.returncode!=0:raise RuntimeError('CONTROLS_FAILED:'+p.stderr+p.stdout)
    result=json.loads(p.stdout)
    if not result['all_pass']:raise RuntimeError('CONTROL_FAILURE')
    with z.output.open('x') as f:f.write(json.dumps(result,indent=2,allow_nan=False)+'\n')

if __name__=='__main__':main()
