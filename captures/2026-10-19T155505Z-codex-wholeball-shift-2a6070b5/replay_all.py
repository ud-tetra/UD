"""Complete primary replay plus data-only directed-basis supplement."""
import sys
sys.dont_write_bytecode=True
import argparse,json,subprocess,os
from pathlib import Path
from bounds import P,sha
def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();out=a.out.absolute();assert not out.exists();out.mkdir(parents=True);f=json.loads((P/'DIRECT_REPLAY_FREEZE.json').read_text());assert sha(__file__)==f['wrapper_sha256'];r={'status':'RUNNING','commands':[],'reviewer_identity':None,'external_review':'PENDING','physical_promotion':0}
 def go(cmd,tag):
  done=subprocess.run([sys.executable,*cmd],cwd=P,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','OPENBLAS_NUM_THREADS':'1'});q=out/(tag+'.log');q.write_bytes(done.stdout);r['commands'].append({'tag':tag,'argv':cmd,'exit_code':done.returncode,'log_sha256':sha(q)});assert done.returncode==0 and done.stdout.strip(),tag
 try:
  go(['replay.py','--repo',str(a.repo.resolve()),'--out',str(out/'primary')],'primary')
  assert json.loads((out/'primary/REPLAY_RECEIPT.json').read_text())['status']=='PASS_CLEAN_APRIORI_NORMAL_AND_CONTROL_REPLAY'
  go(['direct_replay.py','--evidence',str(out/'primary/evidence')],'data-only-direct-Gram')
  r.update(status='PASS_COMPLETE_WHOLEBALL_NORMAL_AND_DATA_ONLY_REPLAY',new_SVD_fits_raw_generation=0)
 except Exception as e:r.update(status='FAIL',error=type(e).__name__+': '+str(e));raise
 finally:(out/'REPLAY_RECEIPT.json').write_text(json.dumps(r,indent=2))
 print(json.dumps(r),flush=True)
if __name__=='__main__':main()
