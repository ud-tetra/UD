"""Verify recovered bytes and documentary linkage; no archived code execution."""
from pathlib import Path
import copy
import hashlib
import json
import re
import tarfile

ROOT = Path(__file__).parent

def verify(links, chain, members):
    assert len(links) == len({x['id'] for x in links}) == 21
    for x in links:
        assert hashlib.sha256(members[x['bundle_member']]).hexdigest() == x['sha256']
        assert x['sha256'] == x['source_provenance']['sha256']
        assert x['source_provenance']['archive_path'] == x['source_archive_path']
        catalog = members[x['catalog_bundle_member']]
        assert hashlib.sha256(catalog).hexdigest() == x['catalog_sha256']
        assert x['record'] in catalog.decode()
        assert re.search(r'(?:"' + re.escape(x['route']) + r'"|\b' + re.escape(x['route']) + r')\s*:\s*' + re.escape(x['record']), catalog.decode())
        relative = './' + x['source_archive_path'].removeprefix('portal/dist/')
        assert re.search(r'(?:\bsource|"source")\s*:\s*"' + re.escape(relative) + r'"', x['record'])
        assert x['recovery_class'] == 'PORTAL177_CATALOG_LINKED_ARTIFACT'
    manifest_bytes = members[chain['hash_manifest_bundle_member']]
    assert hashlib.sha256(manifest_bytes).hexdigest() == chain['hash_manifest_sha256']
    manifest = json.loads(manifest_bytes)
    assert len(manifest['files']) == len(chain['bound_receipts']) == 8
    assert {x['name'] for x in chain['bound_receipts']} == set(manifest['files'])
    for x in chain['bound_receipts']:
        assert hashlib.sha256(members[x['bundle_member']]).hexdigest() == x['sha256'] == manifest['files'][x['name']]
        assert x['source_provenance']['sha256'] == x['sha256']
    output = chain['execution_output']
    assert hashlib.sha256(members[output['bundle_member']]).hexdigest() == output['sha256']
    execution = members['parity-records/UD_PARITY_CARRIER_CRL2C_EXECUTION_RECORD_v0.1.md'].decode()
    assert output['sha256'] in execution
    ruling = members['parity-records/UD_PARITY_CARRIER_CRL2D_CUSTODIAN_RULING_v0.1.md'].decode()
    for x in chain['bound_receipts']:
        if x['name'] in ['UD_HODGE_EVENT_RETAINED_PARITY_CARRIER_THEOREM_v0.1.md',
                         'UD_PARITY_CARRIER_CRL2C_EXECUTION_RECORD_v0.1.md',
                         'UD_PARITY_CARRIER_CRL2D_EXTERNAL_REPLICATION_GEMINI_v0.1.md',
                         'UD_PARITY_CARRIER_CRL2D_REPLICATION_SCORE_v0.1.csv']:
            assert x['sha256'] in ruling
    report = members['parity-records/UD_PARITY_CARRIER_CRL2D_EXTERNAL_REPLICATION_GEMINI_v0.1.md'].decode()
    assert chain['external_replication']['raw_output_hash'] in report
    assert chain['external_replication']['raw_output_recovered'] is False
    assert chain['external_replication']['review_type'] == 'EXTERNAL_AI_AS_DECLARED_BY_REPORT'
    assert chain['custodian']['ruling_document_recovered'] is True
    assert chain['custodian']['named_custodian'] is None
    assert chain['custodian']['signature_or_original_attributable_approval_recovered'] is False
    assert chain['independent_human_review'] == 'NOT_ESTABLISHED_BY_RECOVERED_RECORDS'
    assert chain['new_promotion'] is False and chain['physical_promotion'] == 0

if __name__ == '__main__':
    with tarfile.open(ROOT / 'LINKED_EVIDENCE.tar.gz', 'r:gz') as archive:
        entries = archive.getmembers()
        assert len(entries) == len({x.name for x in entries})
        assert all(x.isfile() and not Path(x.name).is_absolute() and '..' not in Path(x.name).parts for x in entries)
        members = {x.name: archive.extractfile(x).read() for x in entries}
    links = json.loads((ROOT / 'SOURCE_LINKAGE.json').read_text())
    chain = json.loads((ROOT / 'RECEIPT_CHAIN.json').read_text())
    verify(links, chain, members)
    controls = []
    for name in ['source tampering', 'route substitution', 'invented custodian attribution', 'AI reclassified as human']:
        ll, cc, mm = copy.deepcopy((links, chain, members))
        if name == 'source tampering':
            mm[ll[0]['bundle_member']] += b'changed'
        elif name == 'route substitution':
            ll[0]['route'] = 'different_route'
        elif name == 'invented custodian attribution':
            cc['custodian']['named_custodian'] = 'UNSUPPORTED'
        else:
            cc['independent_human_review'] = 'PASS'
        try:
            verify(ll, cc, mm)
        except AssertionError:
            controls.append(name)
        else:
            raise AssertionError('control failed: ' + name)
    print(json.dumps({'status': 'PASS', 'catalog_linked_sources': 21,
                      'parity_manifest_receipts': 8, 'execution_output_commitment': 'HASH_MATCH',
                      'ruling_document': 'RECOVERED_WITH_ATTRIBUTION_GAP',
                      'rejection_controls': controls, 'new_promotion': False,
                      'scope': 'byte custody and documentary linkage only'}))
