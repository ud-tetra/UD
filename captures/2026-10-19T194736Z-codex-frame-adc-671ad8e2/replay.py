"""Replay frozen scalar bounds and tiny byte-level controls in a fresh external directory."""
import argparse,json,hashlib,zipfile
from pathlib import Path
from apparatus_record import verify,digest
from family_phase import certify
from make_fixtures import generate
P=Path(__file__).resolve().parent
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--data',required=True);ap.add_argument('--out',required=True);ap.add_argument('--repo');args=ap.parse_args()
    out=Path(args.out).resolve();need=out!=P and P not in out.parents;assert need
    out.mkdir(parents=True,exist_ok=False);data=Path(args.data).resolve()
    frozen=json.loads((P/'PROTOCOL_FREEZE.json').read_text())
    for n,h in frozen['files'].items():assert digest(P/n)==h,n
    df=json.loads((data/'DATA_FREEZE.json').read_text())
    for n,h in df['files'].items():assert digest(data/n)==h,n
    sourcechecks=0
    if args.repo:
        repo=Path(args.repo)
        for row in json.loads((P/'INPUT_PROVENANCE.json').read_text())['sources']:
            original=repo/row['source_path'];manifest=repo/Path(row['source_path']).parts[0]/Path(row['source_path']).parts[1]/'MANIFEST.json'
            assert digest(original)==digest(P/row['destination'])==row['sha256']
            assert digest(manifest)==row['manifest_sha256'];sourcechecks+=1
    # Rebuild data only, never execute a script from inside the frozen archive.
    generate(out/'rebuilt_data')
    for n in ['FIXTURES.zip','CONTROL_INDEX.json','DATA_FREEZE.json']:
        assert (out/'rebuilt_data'/n).read_bytes()==(data/n).read_bytes(),n
    target=out/'bundles';target.mkdir()
    with zipfile.ZipFile(data/'FIXTURES.zip') as z:
        assert len(z.namelist())==len(df['members'])==len(set(z.namelist()))
        for member in df['members']:
            n=member['path'];p=(target/n).resolve();assert target.resolve() in p.parents
            b=z.read(n);assert len(b)==member['size_bytes'] and hashlib.sha256(b).hexdigest()==member['sha256']
            p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
    rows=[]
    for row in json.loads((data/'CONTROL_INDEX.json').read_text()):
        result=verify(target/row['id'],row['expected_contract_sha256'])
        assert result['status']==row['expected'],(row['id'],result)
        assert result['physical_verdict']==row['physical_expected']=='HOLD_UNQUALIFIED'
        for key,pair in row['exact_expectations'].items():assert result[key]==pair,(row['id'],key,result.get(key),pair)
        if result['status']!='HOLD_INPUT_EVIDENCE':
            assert result['heldout_independence']==result['unaliased_identification']=='NOT_CERTIFIED'
        rows.append({'id':row['id'],'expected':row['expected'],'result':result})
    family=certify();(out/'FAMILY_PHASE_CERTIFICATE.json').write_text(json.dumps(family,indent=2)+'\n')
    summary={'status':'PASS_FROZEN_BYTE_CONTROLS','rows':rows,'controls':len(rows),'source_receipts_checked':sourcechecks,
             'physical_verdicts_hold':len(rows),'actual_apparatus_acquisitions':0,'new_estimator_fits':0,
             'tiny_adc_fixture_bundles':len(rows),'raw_scalars_successfully_scanned':sum(r['result'].get('raw_scalar_readings_checked',0) for r in rows),
             'frozen_generator_rebuild_byte_identical':True,'protocol_sha256':digest(P/'PROTOCOL_FREEZE.json'),'physical_promotion':0}
    (out/'APPARATUS_RESULTS.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({'controls':len(rows),'results':{s:sum(r['result']['status']==s for r in rows) for s in sorted({r['result']['status'] for r in rows})},'ideal_phase_upper':family['ideal_rows'][0]['readable']['nearest_some_target_phase_error_upper'],'strict_unique_phase':family['ideal_rows'][0]['strict_unique_target_bound_pass'],'physical_promotions':0}))
if __name__=='__main__':main()
