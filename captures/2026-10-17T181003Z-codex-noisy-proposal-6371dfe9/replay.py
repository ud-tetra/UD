#!/usr/bin/env python3
"""Fresh campaign replay; outputs are created only in a new directory."""
import argparse,shutil,subprocess,sys,time,json,os
from pathlib import Path
P=Path(__file__).resolve().parent;a=argparse.ArgumentParser();a.add_argument('destination');args=a.parse_args();D=Path(args.destination).resolve();D.mkdir(exist_ok=False,parents=True)
for folder in ['noise-campaign','observer-work']:
 dst=D/folder;dst.mkdir();(dst/'inputs').mkdir()
 for f in (P/folder).glob('*.py'):shutil.copy2(f,dst/f.name)
 shutil.copy2(P/folder/'inputs/FROZEN_CONTRACT.json',dst/'inputs/FROZEN_CONTRACT.json')
shutil.copy2(P/'noise-campaign/CAMPAIGN_FREEZE.json',D/'noise-campaign/CAMPAIGN_FREEZE.json');(D/'noise-campaign/records').mkdir();(D/'noise-campaign/results').mkdir();start=time.monotonic();stages=[]
def run(cmd,name):
 t=time.monotonic()
 with (D/(name+'.log')).open('w') as out:subprocess.run([sys.executable,'-u',*map(str,cmd)],stdout=out,stderr=subprocess.STDOUT,env=dict(os.environ,OPENBLAS_NUM_THREADS='1'),check=True)
 stages.append({'stage':name,'seconds':time.monotonic()-t});print(stages[-1],flush=True)
run([D/'observer-work/record_codec.py','restore',P/'observer-work/codec',D/'observer-work/inputs/normalized_history.i64le'],'restore')
for script in ['make_records.py','compare_old.py','run_new_proposals.py','old_rank_diagnostic.py','certify_discovery_gap.py','run_certificates.py','test_noise.py']:run([D/'noise-campaign'/script],script)
result={'status':'PASS','seconds':time.monotonic()-start,'stages':stages,'physical_promotion':0,'independent_review':'pending'};(D/'REPLAY_RESULT.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
