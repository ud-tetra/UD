import json,pathlib
p=pathlib.Path(__file__).parent
d=json.loads((p/'TRIAGE.json').read_text()); r=json.loads((p/'NATIVE_RELATIONS.json').read_text())
assert len(d['prs'])==55 and len({x['number'] for x in d['prs']})==55
assert all(x['integrity']['sha']==x['head'] and x['integrity']['conclusion']=='success' for x in d['prs'])
assert sum(len(x['files']) for x in d['prs'])==1519
assert all(x['local_merge_tree']['clean'] and x['local_merge_tree']['base']==d['main'] for x in d['prs'])
assert all(x['reviews']==[] for x in d['prs'])
assert len(r['hierarchy'])==7 and all(x['pass'] and sorted(x['expected'])==sorted(x['actual']) for x in r['hierarchy'])
assert len({n for x in r['hierarchy'] for n in x['actual']})==37
assert {(x['n'],b) for x in r['blocking'] for b in x['blocked']}=={(33,34),(137,136),(138,136),(138,137)}
print('PASS: 55 PR receipts, 37 original child links, four blockers')
