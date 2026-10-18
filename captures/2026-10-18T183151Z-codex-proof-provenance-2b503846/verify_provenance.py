"""Validate custody and typed provenance, not scientific theorem truth."""
from pathlib import Path
import copy
import hashlib
import json

ROOT = Path(__file__).parent

def validate(g, records, coverage):
    nodes = {n['id']: n for n in g['nodes']}
    assert len(nodes) == len(g['nodes']) == 53
    assert len(g['edges']) == 53 and len(g['target_closure']) == 20
    sources = {s['id']: s for s in g['sources']}
    assert len(sources) == len(coverage) == 12
    assert len({r['claim_id'] for r in records}) == len(records) == 53
    assert {r['claim_id'] for r in records} == set(nodes)
    for s in sources.values():
        raw = (ROOT / 'sources' / (s['id'] + '.txt')).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == s['sha256']
    for c in coverage:
        assert c['snapshot_sha256'] == sources[c['source_id']]['sha256']
        assert c['snapshot_commit'] == '77d18b76a8222a04baefa69f7b700b589b858939'
    pairs = {(e['from'], e['to']) for e in g['edges']}
    assert len(pairs) == len(g['edges'])
    for e in g['edges']:
        assert e['from'] in nodes and e['to'] in nodes
        assert e['kind'] in {'proof_premise', 'constitutive_assumption', 'evaluation_requirement'}
        assert e['reason'] and e['citations']
    visiting, done = set(), set()
    def walk(key):
        assert key not in visiting
        if key in done:
            return
        visiting.add(key)
        for p in nodes[key]['dependencies']:
            walk(p)
        visiting.remove(key)
        done.add(key)
    for key in nodes:
        walk(key)
    for r in records:
        n = nodes[r['claim_id']]
        assert r['status'] == n['status']
        assert r['origin']['source_citations'] == n['citations']
        incoming = [e for e in g['edges'] if e['to'] == n['id']]
        expected = [{'id': e['from'], 'kind': e['kind'], 'reason': e['reason']} for e in incoming]
        assert r['dependencies'] == expected
        assert set(n['dependencies']) == {e['from'] for e in incoming}
        assert r['reviews']['github_pr71_submissions'] == 0
        assert r['reviews']['independent_human'] == 'NO_ATTRIBUTABLE_RECEIPT_IN_THIS_AUDIT'
        for c in n['citations']:
            s = sources[c['source_id']]
            assert c['snapshot_sha256'] == s['sha256'] and c['section']
            assert c['anchor_text'] in (ROOT / 'sources' / (s['id'] + '.txt')).read_text()
    for x in g['excluded_inferences']:
        assert (x['from'], x['to']) not in pairs
    for t in g['target_closure']:
        assert t['direct_premises'] == nodes[t['target']]['dependencies']
    for s in g['scenarios']:
        changed = set(s['changes'])
        reached = set(changed)
        while True:
            new = reached | {e['to'] for e in g['edges'] if e['from'] in reached}
            if new == reached:
                break
            reached = new
        affected = reached - changed
        assert set(s['must_affect']) <= affected
        assert not set(s['must_preserve']) & affected

if __name__ == '__main__':
    g = json.loads((ROOT / 'SOURCE_GRAPH_v0.3.json').read_text())
    records = json.loads((ROOT / 'CLAIM_PROVENANCE.json').read_text())
    coverage = json.loads((ROOT / 'SOURCE_COVERAGE.json').read_text())
    validate(g, records, coverage)
    controls = []
    for name in ['edge kind conflation', 'scientific status promotion', 'source hash mutation', 'false independent review']:
        gg, rr, cc = copy.deepcopy((g, records, coverage))
        if name == 'edge kind conflation':
            gg['edges'][0]['kind'] = 'text_citation'
        elif name == 'scientific status promotion':
            rr[0]['status'] = 'PHYSICALLY_IDENTIFIED'
        elif name == 'source hash mutation':
            gg['sources'][0]['sha256'] = '0' * 64
        else:
            rr[0]['reviews']['independent_human'] = 'PASSED'
        try:
            validate(gg, rr, cc)
        except AssertionError:
            controls.append(name)
        else:
            raise AssertionError('rejection control did not reject: ' + name)
    print(json.dumps({'status': 'PASS', 'nodes': 53, 'edges': 53, 'sources': 12,
                      'targets': 20, 'propagation_scenarios': len(g['scenarios']),
                      'rejection_controls': controls, 'scope': 'provenance and graph structure only'}))
