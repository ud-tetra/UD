"""Same-team independent prospective code/formula review; zero raw or fit."""
import sys,importlib,hashlib,json
from pathlib import Path
import numpy as np
import review_data as r
P=Path(__file__).resolve().parent
ROOT=P.parent
REPO=ROOT/'ud-repo'
CAMPAIGN=ROOT/'c14_campaign'

def main():
    freeze=r.read(CAMPAIGN/'CAMPAIGN_FREEZE.json')
    r.need(tuple(freeze['case_order'])==r.CASES,'fixed exact three-case order')
    r.need(freeze['protocol_sha256']==r.sha(CAMPAIGN/'PROTOCOL.md'),'frozen campaign protocol')
    pins={case:r.sha(CAMPAIGN/'cases'/case/'FREEZE.json')for case in r.CASES}
    r.need(pins==freeze['case_freeze_sha256'],'all fixed case freeze identities')
    df={'status':'INDEPENDENT_DATA_DRIVER_FROZEN_BEFORE_RAW_OR_FIT','driver_sha256':r.sha(P/'review_data.py'),'cases':pins,'new_raw_records':0,'new_estimator_calls':0,'physical_promotion':0}
    with (P/'DATA_DRIVER_FREEZE.json').open('x')as f:json.dump(df,f,indent=2);f.write('\n')
    original=REPO/'captures/2026-10-20T032737Z-codex-fresh-one-0e3f92e1/source_v2'
    numeric=('estimator.py','certify.py','exact_math.py','numeric_math.py','proof_math.py','phase.py')
    core_caps=r.read(original/'PROFILE.json')['original_quality_caps']
    hashes={};count=0;case_rows=[]
    for case in r.CASES:
        pkg=CAMPAIGN/'cases'/case
        r.validate_freezes(pkg,REPO,case)
        r.need(not(pkg/'DATA_GENERATION_INTENT.json').exists()and not(pkg/'DATA_FREEZE.json').exists()and not(pkg/'FIT_INTENT.json').exists(),'pre-raw/pre-fit custody')
        for name in numeric:r.need(r.sha(pkg/name)==r.sha(original/name),'numerical code changed '+name)
        profile=r.read(pkg/'PROFILE.json')
        r.need(profile['case']==case and profile['original_quality_caps']==core_caps,'case and unchanged exact caps')
        r.need(profile['lag_route']=='PRESELECTED_GRAM_FROBENIUS_ONLY'and profile['source_noise_ball']==[3,1<<49]and profile['target_order']==209 and profile['rank_forced']is False,'unchanged fixed numerical qualification policy')
        for mod in ('records','common'):sys.modules.pop(mod,None)
        sys.path.insert(0,str(pkg))
        try:
            producer=importlib.import_module('records')
            hasher=hashlib.sha256()
            for prep in range(37):
                c,s=producer.pattern(prep,np.arange(8191,dtype=np.int64))
                r.need(c.shape==(8191,)and s.shape==(8191,),'producer pure pattern shape')
                r.need(np.all((c>=0)&(c<62))and np.all(np.abs(s)==1),'producer pure pattern range')
                independent=np.array([r.at(case,prep,t)for t in range(8191)],dtype=np.int64)
                r.need(np.array_equal(c,independent[:,0])and np.array_equal(s,independent[:,1]),'every pure pattern channel/sign formula')
                hasher.update(independent.astype('<i8').tobytes());count+=8191
            hashes[case]=hasher.hexdigest()
        finally:
            sys.path.pop(0)
            for mod in ('records','common'):sys.modules.pop(mod,None)
        case_rows.append({'case':case,'freeze_sha256':pins[case],'formula_positions_checked':303067,'independent_channel_sign_stream_sha256':hashes[case],'unchanged_numerical_modules':list(numeric),'actual_raw_or_fit_observed':False})
    r.need(len(set(hashes.values()))==3,'pure patterns pairwise distinct')
    controls=r.read(P/'DATA_CONTROLS.json')
    r.need(controls['status']=='PASS_INDEPENDENT_THREE_PATTERN_PURE_CONTROLS'and len(controls['rows'])==29 and all(x['pass']is True for x in controls['rows']),'29 independent controls')
    result={'status':'PASS_SAME_TEAM_PROSPECTIVE_THREE_CASE_RAW_ONLY_REVIEW','campaign_freeze_sha256':r.sha(CAMPAIGN/'CAMPAIGN_FREEZE.json'),'protocol_sha256':r.sha(CAMPAIGN/'PROTOCOL.md'),'data_driver_freeze_sha256':r.sha(P/'DATA_DRIVER_FREEZE.json'),'review_driver_sha256':r.sha(__file__),'case_reviews':case_rows,'pure_pattern_positions_checked':count,'independent_pure_controls':29,'pure_control_receipt_sha256':r.sha(P/'DATA_CONTROLS.json'),'pre_freeze_control_correction':'One hand-expected last-time period7 sign corrected from +1 to -1; recipe unchanged; no raw/fit observed','raw_only_release_recommended':True,'fit_release_recommended':False,'fit_blocked_until':'All three concrete DATA_FREEZE records, independent all-scalar/norm/projection audits, bounded metadata exposure and digest distinctness receipts, frozen independent post-audit and root all-data release','driver_assessment':'Producer case fit requires campaign all-data Boolean/root case-specific release and protocol/data hashes; root remains responsible for truthful all-case release and invocation order. Releases are custody records, not cryptographic authentication. Exclusive intents block retries. All outcome HOLDs retained.','source_scope':'Source-aware deterministic computational perturbations of exposed baseline/preparations/targets; coefficients are protocol controls; not blind, empirical, new-preparation or independent physical freshness','numerical_outputs_unknown_at_review':True,'newcase_full_reconstruction_sigma210_lower':'NOT_EVALUATED','source_H_fullfactor_frame_target_proofs':'Inherited hash-bound, not rederived','new_raw_records':0,'new_estimator_calls':0,'external_review':'PENDING','physical_promotion':0}
    with (P/'RAW_PRE_RUN_REVIEW.json').open('x')as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'status':result['status'],'pure_pattern_positions_checked':count,'receipt_sha256':r.sha(P/'RAW_PRE_RUN_REVIEW.json')}))

if __name__=='__main__':main()
