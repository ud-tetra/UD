"""Check source custody and authority separation; no governance enactment."""
from pathlib import Path
import copy
import hashlib
import json

ROOT = Path(__file__).parent

def verify(x):
    assert x['physical_promotion'] == 0
    sources = {s['id']: s for s in x['sources']}
    assert len(sources) == 5
    texts = {}
    for key, s in sources.items():
        b = (ROOT / s['path']).read_bytes()
        assert hashlib.sha256(b).hexdigest() == s['sha256']
        texts[key] = b.decode()
    rows = {r['id']: r for r in x['provisions']}
    assert len(rows) == 24
    for row in rows.values():
        assert row['section'] in texts[row['source_id']]
        assert row['source_sha256'] == sources[row['source_id']]['sha256']
        assert row['new_enactment'] is False
    for i in range(1, 7):
        assert rows[f'CRL-{i}']['authority'] == 'PROPOSAL'
    updated = texts['UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0_UPDATED_20260914.md']
    assert '**Status:** active governance amendment.' in updated
    assert '**Status:** governance proposal.' in updated
    assert updated.startswith(texts['21-UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md'])
    for i in range(1, 10):
        assert rows[f'TOPO-7.{i}']['authority'] == 'ACTIVE_SOURCE_DECLARED'
    for i in range(1, 9):
        assert rows[f'REP-R{i:02}']['authority'].endswith('REPOSITORY_PENDING')
    reviews = x['review_provenance']
    assert {'constructor', 'external_ai', 'independent_human', 'custodian'} <= set(reviews)
    assert reviews['github_pr77_review_submissions'] == []
    assert reviews['external_ai']['receipts'] == []
    assert reviews['independent_human']['receipts'] == []
    assert reviews['custodian']['ruling_receipt_recovered'] is False
    assert x['promotion_record_contract']['permitted_now'] is False
    required = set(x['promotion_record_contract']['required_fields'])
    assert {'exact_version_or_hash', 'non_constructor_review_receipt',
            'attributable_ruling_receipt', 'custodian_identity'} <= required

if __name__ == '__main__':
    obj = json.loads((ROOT / 'GOVERNANCE_CROSSWALK.json').read_text())
    verify(obj)
    controls = []
    for case in ['blanket proposal adoption', 'unreceipted promotion', 'summary treated as ruling']:
        x = copy.deepcopy(obj)
        if case == 'blanket proposal adoption':
            x['provisions'][0]['authority'] = 'ACTIVE'
        elif case == 'unreceipted promotion':
            x['promotion_record_contract']['permitted_now'] = True
        else:
            x['review_provenance']['custodian']['ruling_receipt_recovered'] = True
        try:
            verify(x)
        except AssertionError:
            controls.append(case)
        else:
            raise AssertionError('control accepted: ' + case)
    print(json.dumps({'status': 'PASS', 'provisions': 24, 'source_objects': 5,
                      'rejection_controls': controls, 'physical_promotion': 0,
                      'scope': 'source hashes, locators and authority separation only'}))
