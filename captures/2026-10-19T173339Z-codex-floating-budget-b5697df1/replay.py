"""Fresh intake and exact saved-output budget replay; auxiliary frames remain fixed witnesses."""
import argparse,json,subprocess,os,sys
from pathlib import Path
from common import P,sha,intake
def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--out',required=True);args=p.parse_args();out=Path(args.out).resolve();assert not out.exists();out.mkdir(parents=True)
 f=json.loads((P/'REPLAY_FREEZE.json').read_text())
 for n,h in f['files'].items():assert sha(P/n)==h,('replay',n)
 receipt={'status':'RUNNING','commands':[],'external_review':'PENDING','physical_promotion':0,'new_raw_generation_acquisition_or_state_estimator_runs':0,'auxiliary_frame_witnesses_reused':3}
 try:
  receipt['intake']=intake(Path(args.repo).resolve(),out/'evidence')
  for script,argv in [('direct.py',['--evidence',str(out/'evidence'),'--replay']),('budget_v2.py',['--replay']),('controls.py',['--evidence',str(out/'evidence')])]:
   r=subprocess.run([sys.executable,str(P/script),*argv],cwd=P,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','OPENBLAS_NUM_THREADS':'1'},stdout=subprocess.PIPE,stderr=subprocess.STDOUT);q=out/(script+'.log');q.write_bytes(r.stdout);receipt['commands'].append({'script':script,'exit_code':r.returncode,'log_sha256':sha(q)});assert r.returncode==0 and r.stdout.strip(),script
  receipt.update(status='PASS_CLEAN_FLOATING_OUTPUT_SOURCE_BUDGET_REPLAY',actual_outputs=3,controls=5,scope='New exact source-frame residuals, retained Grams, exact normal equations, quality budgets and strict/refusal controls. Parent fullfactor/raw eligibility/other7gate proofs remain declared dependencies, not newly executed.')
 except Exception as e:receipt.update(status='FAIL',error=type(e).__name__+': '+str(e));raise
 finally:(out/'REPLAY_RECEIPT.json').write_text(json.dumps(receipt,indent=2))
 print(json.dumps(receipt),flush=True)
if __name__=='__main__':main()
