"""Retain every case, compare zero-fit replay, and omit authorized temporary raw."""
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent;W=P.parent/'c15_campaign';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();J=lambda p:json.loads(p.read_text());names=J(W/'CAMPAIGN_FREEZE.json')['case_order'];rows=[]
for name in names:
 case=W/'cases'/name;primary=P.parent/'c15_primary'/name;replay=P.parent/'c15_replay'/name;raw=P.parent/'c15_raw'/(name+'.i64le');run=J(case/'RUN_EXECUTIONS.json');assert len(run['rows'])==1 and run['retry_calls']==0;cert=J(primary/'CERTIFICATE.json');review=P.parent/'c15_output_review'/name/'POST_REVIEW_RECEIPT.json';a=J(review);data=J(case/'DATA_FREEZE.json')['record'];c=cert['row'];files=['CERTIFICATE.json']+([c['matrix_witness_file']]if'matrix_witness_file'in c else[]);replays={n:sha(primary/n)for n in files}
 for n,h in replays.items():assert(primary/n).read_bytes()==(replay/n).read_bytes()and sha(replay/n)==h
 assert sha(raw)==data['record_sha256']and raw.stat().st_mode&0o222==0;assert(replay/'RESOURCE.json').is_file()
 if 'source_certificate_sha256'in a:assert a['source_certificate_sha256']==sha(primary/'CERTIFICATE.json')
 rows.append({'case':name,'producer_status':c['status'],'independent_audit_status':a['status'],'raw_sha256':data['record_sha256'],'raw_bytes':raw.stat().st_size,'byte_identical_primary_replay_sha256':replays,'independent_output_review_sha256':sha(review),'actual_estimator_calls':1,'retry_calls':0,'case_qualified':c['status']=='CERTIFIED_FRESH_COMPUTATIONAL_OPERATOR_POSTERIOR_PROFILE'and a['status']=='PASS_INDEPENDENT_FRESH_RAW_BOUND_FULL_EXACT_TUPLE_AUDIT'})
receipt={'status':'PASS_TWO_BYTE_IDENTICAL_ROOT_ZERO_FIT_REPLAYS','rows':rows,'new_estimator_calls':0,'new_raw_or_factor_copies':0,'comparison_code_sha256':sha(Path(__file__)),'HOLD_outcomes_promoted':False,'external_promotion_review':'PENDING','physical_promotion':0}
with(P/'ROOT_REPLAY_RECEIPT.json').open('x')as f:json.dump(receipt,f,indent=2);f.write('\n')
base=P.parent/'c15_baseline_recovery/ramp_clock_stress.i64le';assert sha(base)=='25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59'
for x in rows:
 raw=P.parent/'c15_raw'/(x['case']+'.i64le');assert sha(raw)==x['raw_sha256'];raw.unlink();x['removed_after_all_audits_and_replay']=not raw.exists()
disposition={'status':'TWO_TEMPORARY_RAW_FILES_OMITTED_AFTER_AUDITS_AND_REPLAY','rows':[{'case':x['case'],'sha256':x['raw_sha256'],'size_bytes':x['raw_bytes'],'removed':x['removed_after_all_audits_and_replay']}for x in rows],'original_recovered_baseline_unchanged_sha256':sha(base),'recovery':'Recover exact baseline from baseline_recovery, then records.make for each frozen case to a new external raw path; exact DATA_FREEZE hash required. Recovery permits zero fits.','new_estimator_calls':0,'physical_promotion':0}
with(P/'RAW_DISPOSITION.json').open('x')as f:json.dump(disposition,f,indent=2);f.write('\n')
print(receipt['status'])
