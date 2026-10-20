"""Root byte replay comparison and authorized temporary raw omission after all audits."""
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent;W=P.parent/'c14_campaign';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();J=lambda p:json.loads(p.read_text());names=J(W/'CAMPAIGN_FREEZE.json')['case_order'];rows=[]
for name in names:
 case=W/'cases'/name;primary=P.parent/'c14_primary'/name;replay=P.parent/'c14_replay'/name;raw=P.parent/'c14_raw'/(name+'.i64le');run=J(case/'RUN_EXECUTIONS.json');assert len(run['rows'])==1 and run['retry_calls']==0;cert=J(primary/'CERTIFICATE.json');a=J(P.parent/'c14_post_review'/name/'POST_REVIEW_RECEIPT.json');assert a['status']=='PASS_INDEPENDENT_FRESH_RAW_BOUND_FULL_EXACT_TUPLE_AUDIT';assert a['source_certificate_sha256']==sha(primary/'CERTIFICATE.json');c=cert['row'];files=['CERTIFICATE.json']+([c['matrix_witness_file']]if'matrix_witness_file'in c else[]);replays={n:sha(primary/n)for n in files}
 for n,h in replays.items():assert (primary/n).read_bytes()==(replay/n).read_bytes() and sha(replay/n)==h
 assert sha(raw)==c['record_sha256'] and raw.stat().st_mode&0o222==0;assert (replay/'RESOURCE.json').is_file()
 rows.append({'case':name,'status':c['status'],'raw_sha256':c['record_sha256'],'raw_bytes':raw.stat().st_size,'byte_identical_primary_replay_sha256':replays,'independent_output_review_sha256':sha(P.parent/'c14_post_review'/name/'POST_REVIEW_RECEIPT.json'),'actual_estimator_calls':1,'retry_calls':0})
receipt={'status':'PASS_ALL_THREE_BYTE_IDENTICAL_ROOT_ZERO_FIT_REPLAYS','rows':rows,'new_estimator_calls':0,'new_raw_or_factor_copies':0,'comparison_code_sha256':sha(Path(__file__)),'same_team_independent_implementation_review':True,'external_promotion_review':'PENDING','physical_promotion':0}
with(P/'ROOT_REPLAY_RECEIPT.json').open('x')as f:json.dump(receipt,f,indent=2);f.write('\n')
base=P.parent/'c14_baseline_recovery/ramp_clock_stress.i64le';assert sha(base)=='25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59'
for x in rows:
 raw=P.parent/'c14_raw'/(x['case']+'.i64le');assert sha(raw)==x['raw_sha256'];raw.unlink();x['removed_after_all_audits_and_replay']=not raw.exists()
disposition={'status':'THREE_TEMPORARY_RAW_FILES_OMITTED_AFTER_COMPLETE_AUDITS_AND_REPLAY','rows':[{'case':x['case'],'sha256':x['raw_sha256'],'size_bytes':x['raw_bytes'],'removed':x['removed_after_all_audits_and_replay']}for x in rows],'original_recovered_baseline_unchanged_sha256':sha(base),'frozen_omission_protocol':str(W/'PROTOCOL.md'),'recovery':'Recover exact baseline from baseline_recovery then records.make for each frozen case to external new raw path; require exact DATA_FREEZE raw SHA before using. No new fit permitted by recovery.','new_estimator_calls':0,'physical_promotion':0}
with(P/'RAW_DISPOSITION.json').open('x')as f:json.dump(disposition,f,indent=2);f.write('\n')
print('PASS_ROOT_REPLAY_AND_FROZEN_RAW_OMISSION')
