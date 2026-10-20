"""Aggregate concrete input/review custody before any campaign estimator call."""
import json,subprocess
from pathlib import Path
import review_data as r
P=Path(__file__).resolve().parent;ROOT=P.parent
CAMPAIGN=ROOT/'c14_campaign';REPO=ROOT/'ud-repo';RROOT=ROOT/'c14_root';POST=ROOT/'c14_post_review'

def main():
    cf=r.read(CAMPAIGN/'CAMPAIGN_FREEZE.json');exposure=r.read(RROOT/'EXPOSURE_RECEIPT.json')
    r.need(exposure['prior_commit']==cf['base_commit'],'same pinned exposure commit')
    r.need(exposure['status']=='PASS_BOUNDED_NO_PRIOR_DIGEST_MATCH_AND_THREE_DISTINCT','bounded root exposure status')
    r.need(len(exposure['rows'])==3 and tuple(z['case']for z in exposure['rows'])==r.CASES,'complete exposure case order')
    post=r.read(POST/'POST_DRIVER_FREEZE.json');pr=r.read(POST/'PRE_RUN_POST_REVIEW.json')
    r.need(r.sha(POST/'review_post.py')==post['driver_sha256']and r.sha(POST/'post_math.py')==post['post_math_sha256'],'post drivers frozen')
    r.need(post['campaign_freeze_sha256']==r.sha(CAMPAIGN/'CAMPAIGN_FREEZE.json')and post['cases']==cf['case_freeze_sha256'],'post all-case pins')
    r.need(pr['post_driver_freeze_sha256']==r.sha(POST/'POST_DRIVER_FREEZE.json')and pr['post_controls_sha256']==r.sha(POST/'POST_CONTROLS.json'),'post prospective review/control pins')
    pcs=r.read(POST/'POST_CONTROLS.json');r.need(len(pcs['rows'])==18 and all(q['pass']is True for q in pcs['rows']),'all18postmathcontrols')
    ff=r.read(RROOT/'FIT_DRIVER_FREEZE.json')
    r.need(r.sha(RROOT/'run_fits.py')==ff['code_sha256']and ff['campaign_freeze_sha256']==r.sha(CAMPAIGN/'CAMPAIGN_FREEZE.json')and tuple(ff['case_order'])==r.CASES and ff['no_retry']is True,'frozen ordered once-only root driver')
    r.need(not(RROOT/'CAMPAIGN_FIT_INTENT.json').exists()and not(CAMPAIGN/'ALL_DATA_FIT_RELEASE.json').exists(),'must precede fit release and any root fit intent')
    rows=[]
    for index,case in enumerate(r.CASES):
        producer=CAMPAIGN/'cases'/case;r.validate_freezes(producer,REPO,case)
        r.need(not(producer/'FIT_INTENT.json').exists(),'no fit before review')
        dp=producer/'DATA_FREEZE.json';ap=P/'data'/case/'DATA_REVIEW_RECEIPT.json';d=r.read(dp);a=r.read(ap)
        r.need(a['status']=='PASS_INDEPENDENT_THREE_PATTERN_RAW_AND_SEPARATED_PROJECTION'and a['case']==d['record']['case']==case,'independent concrete case qualification')
        r.need(a['data_freeze_sha256']==r.sha(dp)and a['source_freeze_sha256']==r.sha(producer/'FREEZE.json'),'data review source/data binding')
        r.need(a['record_sha256']==d['record']['record_sha256']and a['integer_projection_sha256']==d['record']['projection']['integer_bytes_sha256']and a['dyadic_projection_sha256']==d['record']['projection']['projection_bytes_sha256'],'all actual record/projection identities')
        r.need(a['scalar_differences_checked']==18790154 and a['vectors_checked']==303067 and a['changed_scalars']==303067 and a['input_read_only_and_unchanged']is True,'all concrete input arithmetic checks')
        row=exposure['rows'][index];r.need(row['record_sha256']==a['record_sha256']and row['data_freeze_sha256']==r.sha(dp)and row['prior_text_digest_matches']==[]and row['exit_code']==1,'bounded exposure concrete identity')
        grep=subprocess.run(['git','grep','-n','-F',a['record_sha256'],cf['base_commit'],'--','*.json','*.md','*.py'],cwd=REPO,capture_output=True,text=True)
        r.need(grep.returncode==1 and not grep.stdout and not grep.stderr,'independent bounded prior committed-text exposure replay')
        r.need(r.sha(ROOT/'c14_raw'/(case+'.i64le'))==a['record_sha256'],'final pre-fit raw identity')
        rows.append({'case':case,'record_sha256':a['record_sha256'],'data_freeze_sha256':r.sha(dp),'data_review_sha256':r.sha(ap),'producer_freeze_sha256':r.sha(producer/'FREEZE.json'),'independent_exposure_replay_exit_code':1,'one_unchanged_estimator_call_recommended':True})
    r.need(len({x['record_sha256']for x in rows})==3,'actual three input digests distinct')
    result={'status':'PASS_SAME_TEAM_ALL_THREE_CONCRETE_INPUTS_PRE_FIT_REVIEW','cases':rows,'campaign_freeze_sha256':r.sha(CAMPAIGN/'CAMPAIGN_FREEZE.json'),'raw_pre_run_review_sha256':r.sha(P/'RAW_PRE_RUN_REVIEW.json'),'data_driver_freeze_sha256':r.sha(P/'DATA_DRIVER_FREEZE.json'),'root_exposure_receipt_sha256':r.sha(RROOT/'EXPOSURE_RECEIPT.json'),'post_driver_freeze_sha256':r.sha(POST/'POST_DRIVER_FREEZE.json'),'post_pre_run_review_sha256':r.sha(POST/'PRE_RUN_POST_REVIEW.json'),'post_controls_sha256':r.sha(POST/'POST_CONTROLS.json'),'root_fit_driver_freeze_sha256':r.sha(RROOT/'FIT_DRIVER_FREEZE.json'),'fit_review_code_sha256':r.sha(__file__),'scalar_differences_checked':3*18790154,'vectors_checked':3*303067,'projection_entries_checked':3*2629311,'actual_estimator_calls_so_far':0,'one_unchanged_call_per_fixed_case_recommended':True,'maximum_estimator_calls':3,'no_retry_or_replacement':True,'frozen_order_review':'Root driver loops over fixedthreecase order once with exclusive campaignintent/logs and subprocess once per case; nonzero outcome is recorded and does not trigger retry or replacement; case driver has exclusive fitintent and records output/exception','custody_scope':'Root release truthfulness and frozen expected files; no cryptographic caller authentication asserted','exposure_scope':'Independent replay at pinned0dc7dd7 committedJSON/Markdown/Python only; no global novelty or blind/physical freshness','source_scope':'Same exposed baseline/model/preparations/targets; computational sensitivity only; fullfactor/frame/targets inherited hash-bound','newcase_full_reconstruction_sigma210_lower':'NOT_EVALUATED','numerical_outputs_unknown_at_review':True,'external_review':'PENDING','physical_promotion':0}
    with (P/'FIT_PRE_RUN_REVIEW.json').open('x')as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'status':result['status'],'sha256':r.sha(P/'FIT_PRE_RUN_REVIEW.json'),'actual_estimator_calls_so_far':0}))

if __name__=='__main__':main()
