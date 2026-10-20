"""Two-stage custody: root-authorized raw freeze, then one unchanged estimator call."""
import argparse,json,os
from pathlib import Path
from common import P,CASE,freeze,sha,need,write_new,shared_raw,guard,reserve
# Import estimator first: it fixes BLAS/OpenMP threads before NumPy loads.
import estimator,records

def data(baseline,raw):
 freeze();release=json.loads((P/'ROOT_DATA_RELEASE.json').read_text());need(release['raw_generation_released']is True and release['protocol_sha256']==sha(P/'FREEZE.json'),'raw-only root release');need(not(P/'DATA_GENERATION_INTENT.json').exists()and not(P/'DATA_FREEZE.json').exists(),'one data generation');raw=guard(raw);raw.parent.mkdir(parents=True,exist_ok=True);reserve(raw.parent,150321232+25000000);write_new(P/'DATA_GENERATION_INTENT.json',{'case':CASE,'protocol_sha256':sha(P/'FREEZE.json'),'new_raw_generation_intent':1,'estimator_calls':0})
 try:
  record=records.make(baseline,raw);N,projection=estimator.project(raw);del N;record['projection']=projection;need(sha(raw)==record['record_sha256'],'post-projection raw');receipt={'status':'EXACT_ONE_INPUT_FROZEN_BEFORE_FIT','protocol_sha256':sha(P/'FREEZE.json'),'record':record,'new_estimator_calls':0,'shared_raw_read_only':True,'physical_promotion':0}
 except Exception as exc:
  write_new(P/'DATA_GENERATION_HOLD.json',{'status':'HOLD_INPUT_GENERATION_OR_PROJECTION','exception':{'type':type(exc).__name__,'message':str(exc)},'no_retry_or_replacement':True});raise
 write_new(P/'DATA_FREEZE.json',receipt);freeze();print('ONE_DATA_FROZEN_NO_FIT',flush=True)

def fit(raw):
 freeze();reserve(Path(raw).parent,25000000);d=shared_raw(raw);release=json.loads((P/'ROOT_FIT_RELEASE.json').read_text());need(release['one_estimator_call_released']is True and release['protocol_sha256']==sha(P/'FREEZE.json')and release['data_freeze_sha256']==sha(P/'DATA_FREEZE.json'),'fit root release');need(isinstance(release['independent_data_review_sha256'],str)and len(release['independent_data_review_sha256'])==64,'independent data review identity');need(not(P/'FIT_INTENT.json').exists()and not(P/'RUN_EXECUTIONS.json').exists(),'one fit intent only');write_new(P/'FIT_INTENT.json',{'case':CASE,'data_freeze_sha256':sha(P/'DATA_FREEZE.json'),'protocol_sha256':sha(P/'FREEZE.json'),'actual_call_intent':1,'retry_allowed':False});returned=None
 try:
  r=estimator.estimate(raw,d['record']);returned=r;need(r['case']==CASE and r['record_sha256']==d['record']['record_sha256']and r['projection']==d['record']['projection'],'actual output data binding');shared_raw(raw)
 except Exception as exc:r={'case':CASE,'record_sha256':d['record']['record_sha256'],'execution_status':'HOLD_ONE_FIT_DRIVER_EXCEPTION','exception':{'type':type(exc).__name__,'message':str(exc)},'estimator_return_if_any':returned,'policy':'No retry/replacement/rank forcing/fallback'}
 write_new(P/'RUN_EXECUTIONS.json',{'status':'ONE_ACTUAL_ESTIMATOR_INTENT_FINISHED','protocol_sha256':sha(P/'FREEZE.json'),'data_freeze_sha256':sha(P/'DATA_FREEZE.json'),'rows':[r],'new_control_calls':0,'retry_calls':0,'physical_promotion':0});freeze()

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('mode',choices=['data','fit']);p.add_argument('--repo',required=True);p.add_argument('--raw',required=True);p.add_argument('--baseline');p.add_argument('--execute-once',action='store_true');q=p.parse_args();os.environ['UD_REPO']=str(Path(q.repo).resolve())
 if q.mode=='data':need(q.baseline is not None,'baseline required');data(Path(q.baseline).resolve(),q.raw)
 else:need(q.execute_once,'explicit one-shot invocation required');fit(Path(q.raw).resolve())
