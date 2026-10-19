"""Readonly replay of frozen signed fixtures; no signing or key generation."""
import argparse,json,zipfile,hashlib
from pathlib import Path
from authenticated_record import verify,digest
P=Path(__file__).resolve().parent
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--data',required=True);ap.add_argument('--expected-data-freeze-sha256',required=True);ap.add_argument('--out',required=True);x=ap.parse_args()
    out=Path(x.out).resolve();assert out!=P and P not in out.parents;out.mkdir(parents=True,exist_ok=False);data=Path(x.data)
    freeze=json.loads((P/'PROTOCOL_FREEZE.json').read_text())
    for n,h in freeze['files'].items():assert digest(P/n)==h,n
    assert digest(data/'DATA_FREEZE.json')==x.expected_data_freeze_sha256,'EXTERNAL_DATA_FREEZE_PIN'
    df=json.loads((data/'DATA_FREEZE.json').read_text())
    for n,h in df['files'].items():assert digest(data/n)==h,n
    dest=out/'evidence';dest.mkdir()
    with zipfile.ZipFile(data/'AUTH_FIXTURES.zip') as z:
        assert len(z.namelist())==len(set(z.namelist()))==len(df['members'])
        for row in df['members']:
            p=(dest/row['path']).resolve();assert dest.resolve() in p.parents
            b=z.read(row['path']);assert len(b)==row['size_bytes'] and hashlib.sha256(b).hexdigest()==row['sha256']
            p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
    index=json.loads((data/'CONTROL_INDEX.json').read_text());plan=json.loads((P/'CONTROL_PLAN.json').read_text())
    assert len(index)==len({r['id'] for r in index})==plan['planned_controls']
    assert {r['id']:r['expected'] for r in index}=={r['id']:r['expected'] for r in plan['rows']}
    rows=[]
    for row in index:
        result=verify(dest/'bundles'/row['id'],dest/row['policy_path'],row['expected_policy_sha256'],row['expected_admission_sha256'],row['verification_utc'])
        assert result['status']==row['expected'],(row['id'],result)
        assert result['physical_verdict']==row['physical_expected']=='HOLD_UNQUALIFIED'
        if 'signature_status' in result:
            assert result['signature_status']=='VERIFIED_UNDER_CALLER_PINNED_POLICY'
            assert result['calibration_truth']==result['heldout_independence']==result['unaliased_identification']=='NOT_CERTIFIED'
            assert result['analytic_envelope']['checked_scalars']==496
        rows.append({'id':row['id'],'expected':row['expected'],'result':result})
    # Same frozen run is intentionally idempotent in this stateless verifier.
    first=json.loads((data/'CONTROL_INDEX.json').read_text())[0]
    again=verify(dest/'bundles'/first['id'],dest/first['policy_path'],first['expected_policy_sha256'],first['expected_admission_sha256'],first['verification_utc'])
    assert again==rows[0]['result']
    result={'status':'PASS_FROZEN_AUTHENTICATION_AND_ANALYTIC_CONTROLS','rows':rows,'controls':len(rows),'physical_holds':len(rows),'same_run_replay_idempotent':True,'new_key_generation_calls':0,'new_signing_calls':0,'actual_apparatus_acquisitions':0,'real_independently_trusted_keys_supplied':0,'physical_promotion':0,'protocol_sha256':digest(P/'PROTOCOL_FREEZE.json'),'externally_pinned_data_freeze_sha256':x.expected_data_freeze_sha256}
    (out/'AUTH_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'controls':len(rows),'statuses':{s:sum(r['result']['status']==s for r in rows) for s in sorted({r['result']['status'] for r in rows})},'physical_holds':len(rows),'key_generation_or_signing_in_replay':0}))
if __name__=='__main__':main()
