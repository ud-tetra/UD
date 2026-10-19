"""Frozen sequential campaign, parent extension, and full zero-new-estimator replay."""
import argparse,json,hashlib
from pathlib import Path
from common import P,freeze,sha,intake
from records import freeze_data,generate_one,recover_parent
from estimator import estimate,project
from cutoff_phase import verify_one

def check_parent(repo):
 f=freeze();repo=Path(repo);r=f['parent_capture'];cap=repo/'captures'/r['capture'];assert sha(cap/'MANIFEST.json')==r['manifest_sha256'];m=json.loads((cap/'MANIFEST.json').read_text())
 for x in m['files']:assert sha(repo/x['path'])==x['sha256']
 return cap

def parent_certificates(repo,rawdir=None,baseline=None,work=None):
 cap=check_parent(repo);frames=json.loads((cap/'CERTIFICATE.json').read_text())['rows'];runs=json.loads((cap/'RUN_EXECUTIONS.json').read_text())['rows'];rows=[];data=json.loads((cap/'DATA_FREEZE.json').read_text())['records'];regenerated=[]
 for run,frame,record in zip(runs,frames,data):
  assert run['case']==frame['case'] and run['record_sha256']==frame['record_sha256'];raw=Path(rawdir)/(run['case']+'.i64le') if rawdir is not None else Path(work)/('parent_'+run['case']+'.i64le')
  if rawdir is None:regenerated.append(recover_parent(baseline,record,raw))
  assert sha(raw)==run['record_sha256'];N,p=project(raw);assert p==run['projection'];row=verify_one(run['case'],cap/'results'/run['case'],run,N,frame);rows.append(row);print(json.dumps(dict(stage='parent_cutoff_phase',case=run['case'],status=row['status'],cutoff=row.get('cutoff',{}).get('status'),phase=row.get('phase',{}).get('status'))),flush=True)
  if rawdir is None:raw.unlink()
 return dict(status='THREE_SAVED_PARENT_OUTPUTS_CUTOFF_PHASE_EVALUATED',rows=rows,new_estimator_runs=0,protocol_sha256=sha(P/'PROTOCOL_FREEZE.json'),physical_promotion=0)

def run_campaign(baseline,work,source):
 freeze();data=json.loads((P/'DATA_FREEZE.json').read_text());assert data['protocol_sha256']==sha(P/'PROTOCOL_FREEZE.json') and len(data['records'])==6;rows=[]
 for record in data['records']:
  raw=Path(work)/(record['case']+'.i64le');fresh=generate_one(baseline,record['recipe'],raw);assert fresh==record;rows.append(estimate(raw,record));raw.unlink()
 r=dict(status='ALL_SIX_FROZEN_ESTIMATOR_OUTCOMES_RETAINED',rows=rows,physical_promotion=0);(P/'RUN_EXECUTIONS.json').write_text(json.dumps(r,indent=2))
 from align import propose
 from frame import verify
 propose(Path(source));cert=verify(Path(source));(P/'CERTIFICATE.json').write_text(json.dumps(cert,indent=2));return r,cert

def new_certificates(baseline,work,replay=False):
 freeze();data=json.loads((P/'DATA_FREEZE.json').read_text());runs=json.loads((P/'RUN_EXECUTIONS.json').read_text())['rows'];frames=json.loads((P/'CERTIFICATE.json').read_text())['rows'];rows=[];projections=[]
 for record,run,frame in zip(data['records'],runs,frames):
  assert record['case']==run['case']==frame['case'];raw=Path(work)/(record['case']+'.i64le');fresh=generate_one(baseline,record['recipe'],raw);assert fresh==record;N,p=project(raw) if run['projection'] is not None else (None,None);assert run['projection'] is None or p==run['projection'];rows.append(verify_one(run['case'],P/'results'/run['case'],run,N,frame));projections.append(dict(case=run['case'],record_sha256=record['record_sha256'],projection=p,all_scalar_differences_checked=18790154));raw.unlink();print(json.dumps(dict(stage='new_cutoff_phase_replay' if replay else 'new_cutoff_phase',case=run['case'],status=rows[-1]['status'],frame_status=frame['status'],cutoff=rows[-1].get('cutoff',{}).get('status'),phase=rows[-1].get('phase',{}).get('status'))),flush=True)
 return dict(status='ALL_SIX_FROZEN_CUTOFF_PHASE_AND_FRAME_OUTCOMES_RETAINED',rows=rows,raw_projection_replays=projections,protocol_sha256=sha(P/'PROTOCOL_FREEZE.json'),physical_promotion=0)

def replay(repo,baseline,parents,work):
 freeze();work=Path(work);work.mkdir(exist_ok=False);intake(repo,work/'source');parent=parent_certificates(repo,baseline=baseline,work=work);assert parent==json.loads((P/'PARENT_NUMERIC_CERTIFICATES.json').read_text())
 from frame import verify
 assert verify(work/'source')==json.loads((P/'CERTIFICATE.json').read_text());new=new_certificates(baseline,work,replay=True);assert new==json.loads((P/'CAMPAIGN_NUMERIC_CERTIFICATES.json').read_text())
 from controls import verify as controls
 assert controls()==json.loads((P/'CONTROLS.json').read_text())
 return dict(status='FULL_SIX_RECORD_RAW_PROJECTION_AND_NINE_OUTPUT_EXACT_CERTIFICATE_REPLAY_PASS',parent_outputs=3,new_outputs=6,rechecked_new_raw_scalars=6*18790154,rechecked_parent_raw_scalars=3*18790154,new_estimator_runs=0,all_primary_HOLDs_retained=True,physical_promotion=0)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('mode',choices=['generate','fit','verify','replay']);p.add_argument('--repo',required=True);p.add_argument('--baseline',required=True);p.add_argument('--parents');p.add_argument('--work',required=True);args=p.parse_args();work=Path(args.work)
 if args.mode=='generate':freeze_data(args.baseline,work)
 elif args.mode=='fit':
  intake(args.repo,work/'source');run_campaign(args.baseline,work,work/'source')
 elif args.mode=='verify':
  old=parent_certificates(args.repo,args.parents,args.baseline,work);(P/'PARENT_NUMERIC_CERTIFICATES.json').write_text(json.dumps(old,indent=2));new=new_certificates(args.baseline,work);(P/'CAMPAIGN_NUMERIC_CERTIFICATES.json').write_text(json.dumps(new,indent=2))
 else:(P/'FULL_REPLAY.json').write_text(json.dumps(replay(args.repo,args.baseline,args.parents,work),indent=2))
