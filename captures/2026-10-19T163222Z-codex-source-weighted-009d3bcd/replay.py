"""Fresh data-only intake, exact weighted constants, graph, and refusal controls."""
import argparse,json,subprocess,os,sys
from pathlib import Path
from common import P,sha,intake
def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--out',required=True);a=p.parse_args();out=Path(a.out).resolve();assert not out.exists();out.mkdir(parents=True)
 f=json.loads((P/'REPLAY_FREEZE.json').read_text())
 for n,h in f['files'].items():assert sha(P/n)==h,('replay freeze',n)
 receipt={'status':'RUNNING','commands':[],'external_review':'PENDING','physical_promotion':0,'new_raw_generation_acquisition_or_state_estimator_runs':0,'auxiliary_inverse_proposals_reused':1}
 try:
  receipt['intake']=intake(Path(a.repo).resolve(),out/'evidence')
  for script,args in [('weights.py',['--evidence',str(out/'evidence'),'--replay']),('graph.py',['--replay']),('controls.py',['--evidence',str(out/'evidence')])]:
   result=subprocess.run([sys.executable,str(P/script),*args],cwd=P,env={**os.environ,'OPENBLAS_NUM_THREADS':'1','PYTHONDONTWRITEBYTECODE':'1'},stdout=subprocess.PIPE,stderr=subprocess.STDOUT);log=out/(script+'.log');log.write_bytes(result.stdout);receipt['commands'].append({'script':script,'exit_code':result.returncode,'log_sha256':sha(log)});assert result.returncode==0 and result.stdout.strip(),script
  receipt.update(status='PASS_CLEAN_SOURCE_WEIGHTED_ENCODED_BALL_REPLAY',bound_rows=12,controls=5,scope='New exact source-weighted calculations and unchanged-premise graph bound. Pinned parent raw custody/order/fullfactor proofs remain dependencies; not rerun or promoted.')
 except Exception as e:receipt.update(status='FAIL',error=type(e).__name__+': '+str(e));raise
 finally:(out/'REPLAY_RECEIPT.json').write_text(json.dumps(receipt,indent=2))
 print(json.dumps(receipt),flush=True)
if __name__=='__main__':main()
