"""Post-interruption operational continuation. Original scientific code is unchanged."""
import json,argparse
from pathlib import Path
from common import P,freeze,sha
from records import generate_one
from estimator import estimate

def resume(baseline,work,source):
 f=freeze();rf=json.loads((P/'RESUME_FREEZE.json').read_text());assert sha(P/'resume.py')==rf['resume_code_sha256'] and sha(P/'PROTOCOL_FREEZE.json')==rf['original_protocol_sha256'];data=json.loads((P/'DATA_FREEZE.json').read_text());rows=[]
 for saved,record in zip(rf['completed_fits'],data['records'][:3]):
  case=P/'results'/saved['case'];assert sha(case/'RUN.json')==saved['run_sha256'];r=json.loads((case/'RUN.json').read_text());assert r['case']==record['case']
  for n,h in saved['numeric_witnesses'].items():assert sha(case/n)==h
  rows.append(r)
 work=Path(work);work.mkdir(exist_ok=False)
 for record in data['records'][3:]:
  raw=work/(record['case']+'.i64le');assert generate_one(baseline,record['recipe'],raw)==record;rows.append(estimate(raw,record));raw.unlink()
 assert len(rows)==len({r['case'] for r in rows})==6;result=dict(status='ALL_SIX_FROZEN_ESTIMATOR_OUTCOMES_RETAINED',rows=rows,physical_promotion=0);assert not(P/'RUN_EXECUTIONS.json').exists();(P/'RUN_EXECUTIONS.json').write_text(json.dumps(result,indent=2))
 from align import propose
 from frame import verify
 propose(Path(source));cert=verify(Path(source));(P/'CERTIFICATE.json').write_text(json.dumps(cert,indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--baseline',required=True);p.add_argument('--work',required=True);p.add_argument('--source',required=True);args=p.parse_args();resume(args.baseline,args.work,args.source)
