"""Custody and graph checks only. Never execute recovered source programs."""
from pathlib import Path
import copy
import hashlib
import io
import json
import tarfile

ROOT = Path(__file__).parent

def check(graph, old, coverage, reviews, members):
    nodes = {n['id']: n for n in graph['nodes']}
    assert len(nodes) == len(graph['nodes']) == 197
    assert len(graph['edges']) == 314 and len(graph['target_closure']) == 107
    assert all(nodes[n['id']] == n for n in old['nodes'])
    assert len(old['nodes']) == 53
    sources = {s['id']: s for s in graph['sources']}
    assert len(sources) == len(coverage) == 45
    assert sum(c['original_copy_verified'] for c in coverage) == 24
    for c in coverage:
        source = sources[c['id']]
        raw = members[c['snapshot_member']]
        assert hashlib.sha256(raw).hexdigest() == source['sha256'] == c['snapshot_sha256']
        if c['original_copy_verified']:
            assert hashlib.sha256(members[c['original_bundle_member']]).hexdigest() == source['original_sha256']
        else:
            assert c['original_bundle_member'] is None
    pairs = {(e['from'], e['to']) for e in graph['edges']}
    assert len(pairs) == 314
    for e in graph['edges']:
        assert e['from'] in nodes and e['to'] in nodes
        assert e['kind'] in {'proof_premise', 'constitutive_assumption', 'evaluation_requirement'}
        assert e['reason'] and e['citations']
    coverage_by_id = {c['id']: c for c in coverage}
    seen, active = set(), set()
    def visit(key):
        assert key not in active, ('cycle', key)
        if key in seen:
            return
        active.add(key)
        for dep in nodes[key]['dependencies']:
            visit(dep)
        active.remove(key)
        seen.add(key)
    for key, n in nodes.items():
        visit(key)
        assert set(n['dependencies']) == {e['from'] for e in graph['edges'] if e['to'] == key}
        for c in n['citations']:
            source = sources[c['source_id']]
            assert c['snapshot_sha256'] == source['sha256'] and c['section']
            assert c['anchor_text'] in members[coverage_by_id[c['source_id']]['snapshot_member']].decode()
    for target in graph['target_closure']:
        assert target['direct_premises'] == nodes[target['target']]['dependencies']
    for excluded in graph['excluded_inferences']:
        assert (excluded['from'], excluded['to']) not in pairs
    for scenario in graph['scenarios']:
        seeds = set(scenario['changes'])
        reached = set(seeds)
        while True:
            more = reached | {e['to'] for e in graph['edges'] if e['from'] in reached}
            if more == reached:
                break
            reached = more
        assert set(scenario['must_affect']) <= reached - seeds
        assert not set(scenario['must_preserve']) & (reached - seeds)
    assert len(graph['scenarios']) == 38
    for r in reviews['records']:
        assert hashlib.sha256(members[r['bundle_member']]).hexdigest() == r['sha256']
    assert reviews['external_ai']['replicator'] == 'Gemini'
    assert reviews['external_ai']['evidence_level'] == 'ATTRIBUTED_SUMMARY_ONLY'
    assert reviews['external_ai']['full_replication_receipt_recovered'] is False
    assert reviews['independent_human']['status'] == 'NOT_ESTABLISHED_BY_RECOVERED_RECORDS'
    assert reviews['custodian']['ruling_receipt_recovered'] is False
    assert reviews['physical_promotion'] == 0

if __name__ == '__main__':
    with tarfile.open(ROOT / 'RECOVERED_SOURCES.tar.gz', 'r:gz') as archive:
        entries = archive.getmembers()
        assert all(e.isfile() and not Path(e.name).is_absolute() and '..' not in Path(e.name).parts for e in entries)
        assert len({e.name for e in entries}) == len(entries)
        members = {e.name: archive.extractfile(e).read() for e in entries}
    graph = json.loads(members['graphs/dependencies-v0.14.json'])
    old = json.loads(members['graphs/dependencies-v0.3.json'])
    coverage = json.loads((ROOT / 'SOURCE_COVERAGE.json').read_text())
    reviews = json.loads((ROOT / 'REVIEW_PROVENANCE.json').read_text())
    check(graph, old, coverage, reviews, members)
    controls = []
    for case in ['source tampering', 'edge-type conflation', 'AI classified as human', 'summary classified as ruling']:
        gg, rr, mm = copy.deepcopy((graph, reviews, members))
        if case == 'source tampering':
            mm[coverage[0]['snapshot_member']] += b'changed'
        elif case == 'edge-type conflation':
            gg['edges'][0]['kind'] = 'textual_reference'
        elif case == 'AI classified as human':
            rr['independent_human']['status'] = 'PASS'
        else:
            rr['custodian']['ruling_receipt_recovered'] = True
        try:
            check(gg, old, coverage, rr, mm)
        except AssertionError:
            controls.append(case)
        else:
            raise AssertionError('failed rejection control: ' + case)
    print(json.dumps({'status': 'PASS', 'nodes': 197, 'edges': 314, 'targets': 107,
                      'source_snapshots': 45, 'declared_original_copies': 24, 'snapshot_only': 21,
                      'unchanged_prior_nodes': 53, 'propagation_scenarios': 38,
                      'review_records': 6, 'rejection_controls': controls,
                      'scope': 'custody and graph structure; no independent theorem replay'}))
