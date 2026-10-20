"""Freeze all input receipts before exactly one estimator invocation per case."""
import argparse,json,os,tempfile
from pathlib import Path
from common import P,repo,freeze,sha,write_new
import records,estimator

def prepare(baseline):
 f=freeze();assert not (P/'DATA_FREEZE.json').exists() and not (P/'attempts').exists();rows=[]
 for source in records.recipes():
  with tempfile.TemporaryDirectory(prefix='ud-adversarial-data-') as temp:
   raw=Path(temp)/'record.i64le';row=records.generate(baseline,raw,source);N,projection=estimator.project(raw);row['projection']=projection;assert sha(raw)==row['record_sha256'];del N;rows.append(row)
 if [x['case'] for x in rows]!=f['cases']:raise RuntimeError('HOLD case order')
 write_new(P/'DATA_FREEZE.json',{'status':'ALL_TWO_DATA_CHECKED_BEFORE_ANY_FIT','protocol_sha256':sha(P/'PROTOCOL_FREEZE.json'),'records':rows,'new_estimator_calls':0,'physical_promotion':0});print('ALL_TWO_DATA_FROZEN',flush=True)

def fit(baseline):
 f=freeze();data=json.loads((P/'DATA_FREEZE.json').read_text());assert data['protocol_sha256']==sha(P/'PROTOCOL_FREEZE.json') and data['status']=='ALL_TWO_DATA_CHECKED_BEFORE_ANY_FIT';assert [x['case'] for x in data['records']]==f['cases'];assert not (P/'attempts').exists() and not (P/'RUN_EXECUTIONS.json').exists();(P/'attempts').mkdir();runs=[]
 for source,expected in zip(records.recipes(),data['records']):
  returned=None
  try:
   with tempfile.TemporaryDirectory(prefix='ud-adversarial-fit-') as temp:
    raw=Path(temp)/'record.i64le';actual=records.generate(baseline,raw,source);N,projection=estimator.project(raw);actual['projection']=projection;del N;assert actual==expected
    write_new(P/'attempts'/(source['id']+'_START.json'),{'case':source['id'],'record_sha256':actual['record_sha256'],'data_freeze_sha256':sha(P/'DATA_FREEZE.json'),'estimator_call_intent':1,'retry_allowed':False})
    run=estimator.estimate(raw,actual);returned=run;assert run['record_sha256']==expected['record_sha256'];assert run['projection']==expected['projection']
  except Exception as exc:
   run={'case':source['id'],'record_sha256':expected['record_sha256'],'execution_status':'HOLD_DRIVER_EXCEPTION','error':{'type':type(exc).__name__,'message':str(exc)},'estimator_return_if_any':returned,'policy':'Retain failure; no retry or replacement; continue fixed remaining case'}
  runs.append(run)
 write_new(P/'RUN_EXECUTIONS.json',{'status':'FIXED_TWO_CASE_EXECUTION_COMPLETE','protocol_sha256':sha(P/'PROTOCOL_FREEZE.json'),'data_freeze_sha256':sha(P/'DATA_FREEZE.json'),'rows':runs,'retry_calls':0,'physical_promotion':0});freeze()

def main():
 p=argparse.ArgumentParser();p.add_argument('mode',choices=['data','fit']);p.add_argument('--repo',required=True);p.add_argument('--baseline',required=True);p.add_argument('--execute-once',action='store_true');a=p.parse_args();os.environ['UD_REPO']=str(Path(a.repo).resolve());baseline=Path(a.baseline).resolve()
 if a.mode=='data':prepare(baseline)
 else:
  if not a.execute_once:raise RuntimeError('HOLD explicit one-run command required')
  fit(baseline)
if __name__=='__main__':main()
