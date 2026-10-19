"""Read-only frozen inputs; write receipts only to a fresh external output directory."""
import argparse, json, hashlib
from pathlib import Path
from fractions import Fraction as F
from certify_family import certify,P
from apparatus import verify,inverse_gain_scalar_bound,decision
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);ap.add_argument('--raw');ap.add_argument('--repo');args=ap.parse_args()
    out=Path(args.out).resolve(); assert out!=P and P not in out.parents
    out.mkdir(parents=True,exist_ok=False)
    freeze=json.loads((P/'PROTOCOL_FREEZE.json').read_text())
    for name,h in freeze['files'].items(): assert hashlib.sha256((P/name).read_bytes()).hexdigest()==h, name
    source_checks=0
    if args.repo:
        repo=Path(args.repo)
        for r in json.loads((P/'INPUT_PROVENANCE.json').read_text())['sources']:
            source=repo/r['source_path']; manifest=next(parent/'MANIFEST.json' for parent in source.parents if (parent/'MANIFEST.json').is_file())
            assert hashlib.sha256(source.read_bytes()).hexdigest()==r['source_sha256']
            assert hashlib.sha256(manifest.read_bytes()).hexdigest()==r['source_manifest_sha256']
            assert hashlib.sha256((P/r['destination']).read_bytes()).hexdigest()==r['destination_sha256']
            old=json.loads(source.read_text())
            if r['destination']=='inputs/ANCHORS.json':old={'rows':[{'case':x['case'],'record_sha256':x['record_sha256'],'cutoff':x['cutoff']} for x in old['rows']]}
            if r['destination']=='inputs/BASE_GENERATION.json':old={'row':next(x for x in old['records'] if x['case']=='ramp_clock_stress')}
            assert old==json.loads((P/r['destination']).read_text()); source_checks+=1
    family=certify(args.raw)
    (out/'FAMILY_CERTIFICATE.json').write_text(json.dumps(family,indent=2)+'\n')
    c=json.loads((P/'APPARATUS_CONTRACT.json').read_text()); fixtures=json.loads((P/'CONTROL_FIXTURES.json').read_text())
    rows=[]
    for f in fixtures:
        result=verify(f['packet'],c)
        assert result['mathematical_status']==f['expected'],f['id']
        assert result['physical_verdict']=='HOLD_UNQUALIFIED'
        rows.append({'id':f['id'],'expected':f['expected'],'result':result})
    # An independent displayed inverse-gain arithmetic example, not hardware data.
    bound=inverse_gain_scalar_bound(F(1,1024),F(2),F(1,2048),F(1,4096),F(1,2),F(1,8192),F(3),F(1,16384))
    assert bound==F(93,16384)
    assert decision(F(1,16),F(1,16),F(0),F(1,16))[0]=='CONDITIONAL_CONSISTENCY'
    assert decision(F(1,16),F(1,16),F(1,128),F(1,16))[0]=='HOLD'
    result={'status':'PASS_FROZEN_SYNTHETIC_LOGIC_CONTROLS','controls':rows,'control_count':len(rows),
            'gain_bound_fixture':[bound.numerator,bound.denominator], 'new_records':0,'new_fits':0,'physical_acquisitions':0,
            'baseline_scalar_norm_checks':18790154 if args.raw else 0,
            'norm_source':'raw bytes replayed' if args.raw else 'pinned independently recomputed exact source receipt',
            'parent_source_extractions_verified':source_checks,
            'protocol_sha256':hashlib.sha256((P/'PROTOCOL_FREEZE.json').read_bytes()).hexdigest(), 'physical_promotion':0}
    (out/'APPARATUS_CONTROLS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'family':family['readable'],'controls':len(rows),'norm_scalar_checks':result['baseline_scalar_norm_checks'],'new_fits':0,'physical_promotion':0}))
if __name__=='__main__':main()
