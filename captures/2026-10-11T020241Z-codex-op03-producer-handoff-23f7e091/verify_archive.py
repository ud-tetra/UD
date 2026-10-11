#!/usr/bin/env python3
"""Recheck a candidate OP03 bench archive against the scoped acquisition audit."""
import hashlib
import io
import json
import pathlib
import sys
import zipfile

ROOT=pathlib.Path(__file__).resolve().parent
def sha(b): return hashlib.sha256(b).hexdigest()
def only(names,suffix):
    hit=[n for n in names if n.endswith(suffix)]
    assert len(hit)==1, (suffix,hit)
    return hit[0]
def main(path):
    audit=json.loads((ROOT/'SOURCE_AUDIT.json').read_text())
    blob=pathlib.Path(path).read_bytes()
    assert sha(blob)==audit['sha256']
    with zipfile.ZipFile(io.BytesIO(blob)) as outer:
        names=outer.namelist()
        state=json.loads(outer.read(only(names,'protocol/V0_2_STATE.json')))
        readme=outer.read(only(names,'README.md')).decode()
        engine=json.loads(outer.read(only(names,'templates/ENGINE_COMMIT_TEMPLATE.json')))
        assert state['real_events']==audit['outer_state_real_events']==0
        assert audit['outer_readme_status'] in readme
        assert engine['event_engine_id'].startswith('FILL_')
        child=outer.read(only(names,audit['nested_archive']))
        assert sha(child)==audit['nested_sha256']
        with zipfile.ZipFile(io.BytesIO(child)) as inner:
            m=json.loads(inner.read(only(inner.namelist(),'ACQUISITION_MANIFEST.json')))
            assert m['current_real_event_count']==audit['nested_current_real_event_count']==0
            assert m['synthetic_controls_only'] is True
            assert m['status']==audit['nested_acquisition_manifest_status']
            assert m['scientific_evidence_included'] is False
            assert any('/synthetic/' in n for n in inner.namelist())
    print(json.dumps({'status':'SOURCE_BLOCKED / NOT_RUN',
                      'outer_sha256':sha(blob),'outer_members':len(names),
                      'inner_sha256':sha(child),'inner_members':len(inner.namelist()),
                      'outer_real_events':0,'nested_real_events':0,
                      'independent_full_endpoint_scored':0,'physical_promotion':0},indent=2))

if __name__=='__main__':
    assert len(sys.argv)==2
    main(sys.argv[1])
