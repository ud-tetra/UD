"""Saved-witness exact replay; optional full raw/projection regeneration without another SVD."""
import argparse,json
from pathlib import Path
from common import P,freeze,intake,sha
from validate import verify
from controls import verify as controls

def replay(repo,work,baseline=None):
 freeze();work=Path(work);work.mkdir(parents=True,exist_ok=False);source=work/'source';receipt=intake(repo,source)
 assert verify(source)==json.loads((P/'CERTIFICATE.json').read_text());assert controls()==json.loads((P/'CONTROLS.json').read_text())
 raw_receipt=[]
 if baseline is not None:
  from records import generate
  from kernel import project
  generate(baseline,work/'records',replay=True)
  for run in json.loads((P/'RUN_EXECUTIONS.json').read_text())['rows']:
   N,p=project(work/'records'/(run['case']+'.i64le'));assert run['projection'] is None or p==run['projection'];raw_receipt.append(dict(case=run['case'],record_sha256=run['record_sha256'],projection=p,all_scalar_noise_differences_rechecked=True));del N
 return dict(status='FULL_RAW_PROJECTION_AND_SAVED_WITNESS_REPLAY_PASSED' if baseline is not None else 'SAVED_WITNESS_ONLY_REPLAY_PASSED',source=receipt,raw_projection_replays=raw_receipt,new_estimator_runs=0,baseline_dependency='Pinned original synthetic baseline required for full raw regeneration; not bundled raw acquisition',physical_promotion=0)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--work',required=True);p.add_argument('--baseline');p.add_argument('--receipt',required=True);args=p.parse_args();r=replay(args.repo,args.work,args.baseline);Path(args.receipt).write_text(json.dumps(r,indent=2));print(json.dumps(r),flush=True)
