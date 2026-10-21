"""Read pinned repository source data; no imported code is executed."""
import hashlib,json,subprocess
from pathlib import Path

root=Path(__file__).resolve().parents[2] if Path(__file__).resolve().parent.parent.name=='captures' else Path(__file__).resolve().parents[1]/'ud-repo'
here=Path(__file__).resolve().parent
rel='captures/2026-10-18T183151Z-codex-proof-provenance-2b503846/sources/L65.txt'
data=(root/rel).read_bytes(); d=json.loads(data); rows=d['rows']; ids=[r['id'] for r in rows]
assert len(rows)==448==d['typed_objects']==len(set(ids))
selected={r['id']:r for r in rows if r['id'] in ['G06','O09','O10','O11','O12','O13','O14','O15']}
assert len(selected)==8
assert selected['O14']['exact_form']=='A_0/hbar; equivalently A_0 = eta_A hbar'
assert '[B_0]=M' in selected['O15']['exact_form']
assert 'closed history = pi sum' in selected['O09']['exact_form']
out={'source_path':rel,'sha256':hashlib.sha256(data).hexdigest(),
     'base_commit':'ed2290e8ff6105a173a0eba4f242b840926cafb6',
     'scientific_revision':d['scientific_revision'],'source_baseline':d['source_baseline'],
     'declared_rows':d['typed_objects'],'actual_rows':len(rows),'unique_ids':len(set(ids)),
     'inspected_rows':selected,'full_dimensional_audit':False,
     'literal_O13_equality_chain':'DIMENSIONAL_TEXT_DEFECT_FLAGGED',
     'v085_recovered':False,'EXIT-03_specification_recovered':False,'physical_promotion':0}
(here/'SOURCE_AUDIT.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: older-source inventory and eight selected rows inspected; O13 flag retained.')
