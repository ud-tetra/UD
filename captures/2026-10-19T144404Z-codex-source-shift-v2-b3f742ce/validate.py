"""Evaluate known PR212 outputs under separately versioned source allowance.

--campaign requires the complete newly executed byte-bound parent replay.
No new proposer/SVD or source raw generation is claimed.
"""
import json, argparse
from pathlib import Path
from source_math import P, sha, freeze, derive, evaluate

def run(campaign):
    freeze()
    receipt=json.loads((campaign/'REPLAY_RECEIPT.json').read_text())
    assert receipt['status']=='PASS_COMPLETE_CAMPAIGN_REPLAY'
    assert receipt['cases']==3 and receipt['admitted']==2 and receipt['HOLD']==1
    assert receipt['helper_hashes_before_after_verified'] is True
    assert receipt['new_SVD_or_estimator_runs']==0
    for log in receipt['logs']:
        p=campaign/(log['tag']+'.log')
        assert log['exit_code']==0 and sha(p)==log['log_sha256']
    work=campaign/'adversarial-admission-work'
    assert sha(work/'GATE_RESULTS.json')==sha(P/'inputs/GATE_RESULTS.json')
    assert sha(work/'EXACT_SHIFT_EXCEEDANCE.json')==sha(P/'inputs/EXACT_SHIFT_EXCEEDANCE.json')
    rows=[]
    for row in json.loads((work/'GATE_RESULTS.json').read_text())['rows']:
        r=evaluate(row['metrics'],row['raw_eligible'])
        r.update(case=row['case'],record_sha256=row['record_sha256'],
                 original_PR210_policy_status=row['status'])
        rows.append(r);print(json.dumps(r),flush=True)
    result={'status':'SAVED_OUTPUT_V2_EVALUATION','rows':rows,
            'source_allowance':derive(), 'parent_replay_receipt_sha256':sha(campaign/'REPLAY_RECEIPT.json'),
            'no_new_estimator_SVD_or_raw_generation':True,
            'known_record_posthoc_certificate':True, 'external_review':'PENDING','physical_promotion':0}
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--campaign',type=Path,required=True);p.add_argument('--replay',action='store_true');args=p.parse_args()
    r=run(args.campaign);dest=P/'ACTUAL_V2.json'
    if args.replay:
        # Receipt hash is execution-specific; the complete numerical outcome must match.
        old=json.loads(dest.read_text());assert old['rows']==r['rows'] and old['source_allowance']==r['source_allowance']
    else:
        assert not dest.exists();dest.write_text(json.dumps(r,indent=2))
